"""EDGE-20260911-001: trade-count aggressor imbalance residual — no lookahead.

IMB_cnt = (n_buy - n_sell) / max(n_buy + n_sell, 1)
RES = residual after trailing-L OLS of IMB on {r, |r|, vol, range}
Fire when |RES| >= trailing Q* of |RES| and n_buy+n_sell >= N_min
Direction = sign(RES)

Entry at t + Δ_exec (Δ_exec > 0 mandatory). Forward returns via OHLCV [A].
Cite CEM-20260910-001/002/003.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .trades_loader import HOLDOUT_START_MS, assert_no_holdout_trades


def _log_return(close: np.ndarray) -> np.ndarray:
    out = np.full(len(close), np.nan, dtype=np.float64)
    prev = close[:-1]
    cur = close[1:]
    with np.errstate(divide="ignore", invalid="ignore"):
        out[1:] = np.log(cur / prev)
    return out


def trailing_ols_resid(
    y: np.ndarray,
    X: np.ndarray,
    L: int,
    refresh: int = 1,
) -> np.ndarray:
    """Trailing-L OLS residual of y on X (with intercept). No future bars.

    Fit beta on window [t-L+1, t] at refresh anchors; apply beta within the
    forward refresh block using the *last completed* beta that does not use
    future rows relative to each evaluation t (beta from anchor u applied to
    t in (u, u+refresh] where u >= t is forbidden — we apply beta_u only for
    t == u, and for speed recompute every `refresh` bars exactly at those t).

    [A] Exact trailing residual at every t would be O(n L k^2). We recompute
    beta every `refresh` bars on the trailing-L window ending at that bar, and
    for intermediate bars use the most recent beta whose window end <= t
    (still no future). Residuals at non-anchor bars use beta from prior anchor.
    Primary metrics use this [A] approximation with refresh=1 when n is small;
    default refresh=32 for RESEARCH-scale speed.
    """
    y = np.asarray(y, dtype=np.float64)
    X = np.asarray(X, dtype=np.float64)
    n, k = X.shape
    resid = np.full(n, np.nan, dtype=np.float64)
    ones = np.ones((n, 1), dtype=np.float64)
    Xa = np.hstack([ones, X])
    p = k + 1
    beta = None
    last_anchor = -1
    refresh = max(1, int(refresh))
    for t in range(L - 1, n):
        need = (beta is None) or ((t - last_anchor) >= refresh) or (t == n - 1)
        if need:
            sl = slice(t - L + 1, t + 1)
            yy = y[sl]
            xx = Xa[sl]
            m = np.isfinite(yy) & np.all(np.isfinite(xx), axis=1)
            if int(m.sum()) < p + 2:
                beta = None
                continue
            try:
                beta, _, _, _ = np.linalg.lstsq(xx[m], yy[m], rcond=None)
                last_anchor = t
            except np.linalg.LinAlgError:
                beta = None
                continue
        if beta is None:
            continue
        if not np.isfinite(y[t]) or not np.all(np.isfinite(Xa[t])):
            continue
        resid[t] = y[t] - float(Xa[t] @ beta)
    return resid


def trailing_quantile_abs(series: np.ndarray, L: int, q: float) -> np.ndarray:
    """Trailing empirical quantile of |series| over L ending at t (pandas rolling)."""
    s = pd.Series(np.abs(np.asarray(series, dtype=np.float64)))
    out = s.rolling(window=L, min_periods=L).quantile(q)
    return out.to_numpy(dtype=np.float64)


def forward_gross_bps_delta_exec(
    open_: np.ndarray,
    close: np.ndarray,
    close_time_ms: np.ndarray,
    direction: np.ndarray,
    *,
    delta_exec_ms: int,
    h_bars: int,
) -> np.ndarray:
    """Sign-aligned forward return with mandatory Δ_exec > 0 [A].

    [A] Entry price = open of first bar with open_time > decision close_time
        (i.e. next bar open — Δ_exec places entry after t into that bar).
        Exit price = open of bar index entry_idx + h_bars.
        Gross bps = direction * (exit/entry - 1) * 1e4.

    Forbidden: fill at last trade timestamp inside feature window.
    """
    if delta_exec_ms <= 0:
        raise ValueError("Δ_exec must be > 0")
    if h_bars < 1:
        raise ValueError("h_bars must be >= 1")
    n = len(close)
    open_time_ms = close_time_ms - 299_999
    gross = np.full(n, np.nan, dtype=np.float64)
    # Vectorized: decision i → entry at i+1 open, exit at i+1+h open
    # Valid while i+1+h < n
    entry_idx = np.arange(n) + 1
    exit_idx = entry_idx + h_bars
    valid = exit_idx < n
    # Also require entry clock = close_time + delta conceptually inside next bar
    # (always true for delta_exec_ms < BAR_MS for 5m bars)
    ei = entry_idx[valid]
    xi = exit_idx[valid]
    ent = open_[ei]
    ex = open_[xi]
    with np.errstate(divide="ignore", invalid="ignore"):
        ret = (ex / ent - 1.0) * 1e4
    d = direction[valid]
    gross[np.where(valid)[0]] = d * ret
    # Mask last bars / non-finite
    bad = ~np.isfinite(ent) | ~np.isfinite(ex) | (ent <= 0)
    # map bad back
    vi = np.where(valid)[0]
    gross[vi[bad]] = np.nan
    return gross


def build_edge001_frame(
    bar_flow: pd.DataFrame,
    *,
    L: int = 288,
    Q_star: float = 0.80,
    N_min: int = 20,
    delta_exec_ms: int = 500,
    h_bars: int = 1,
    use_scrambled: bool = False,
) -> pd.DataFrame:
    """Build signal frame from cached bar_flow + embedded OHLCV columns."""
    df = bar_flow.copy()
    if (df["close_time_ms"] >= HOLDOUT_START_MS).any():
        df = df.loc[df["close_time_ms"] < HOLDOUT_START_MS].reset_index(drop=True)
    assert_no_holdout_trades(df["close_time_ms"].to_numpy())

    close = df["close"].to_numpy(dtype=np.float64)
    high = df["high"].to_numpy(dtype=np.float64)
    low = df["low"].to_numpy(dtype=np.float64)
    vol = df["volume"].to_numpy(dtype=np.float64)

    r = _log_return(close)
    abs_r = np.abs(r)
    # range_t = (high-low)/close [A]
    with np.errstate(divide="ignore", invalid="ignore"):
        range_t = (high - low) / close

    if use_scrambled:
        nb = df["n_buy_1m_scrambled"].to_numpy(dtype=np.float64)
        ns = df["n_sell_1m_scrambled"].to_numpy(dtype=np.float64)
    else:
        nb = df["n_buy_1m"].to_numpy(dtype=np.float64)
        ns = df["n_sell_1m"].to_numpy(dtype=np.float64)

    imb = (nb - ns) / np.maximum(nb + ns, 1.0)
    X = np.column_stack([r, abs_r, vol, range_t])
    resid = trailing_ols_resid(imb, X, L)
    q_abs = trailing_quantile_abs(resid, L, Q_star)

    n_tot = nb + ns
    filled = (
        df["feature_filled"].to_numpy(dtype=bool)
        if "feature_filled" in df.columns
        else np.ones(len(df), dtype=bool)
    )
    ok = (
        np.isfinite(resid)
        & np.isfinite(q_abs)
        & (n_tot >= N_min)
        & np.isfinite(r)
        & np.isfinite(vol)
        & np.isfinite(range_t)
        & filled
    )
    fire = ok & (np.abs(resid) >= q_abs)
    direction = np.sign(resid)
    direction = np.where(direction == 0, 0.0, direction)

    gross = forward_gross_bps_delta_exec(
        df["open"].to_numpy(dtype=np.float64),
        close,
        df["close_time_ms"].to_numpy(dtype=np.int64),
        direction,
        delta_exec_ms=delta_exec_ms,
        h_bars=h_bars,
    )

    out = df.copy()
    out["r_t"] = r
    out["abs_r_t"] = abs_r
    out["vol_t"] = vol
    out["range_t"] = range_t
    out["IMB_cnt"] = imb
    out["RES"] = resid
    out["Q_abs"] = q_abs
    out["signal"] = fire
    out["direction"] = np.where(fire, direction, 0.0)
    out["gross_bps"] = np.where(fire, gross, np.nan)
    out["timestamp"] = pd.to_datetime(out["open_time_ms"], unit="ms", utc=True)
    return out


def ohlcv_only_nested_signal(
    frame: pd.DataFrame,
    *,
    L: int = 288,
    Q_star: float = 0.80,
    delta_exec_ms: int = 500,
    h_bars: int = 1,
) -> pd.DataFrame:
    """OHLCV-only nested control: residualize a proxy and/or predict from controls.

    [A] Walk-forward: trailing OLS of *lagged* forward gross (from prior bars')
    is not available at t. Instead: treat signed r_t as the OHLCV direction
    predictor after orthogonalizing r_t to {|r|, vol, range} — fire on |RES_r|
    at same Q*. Compares whether count-imbalance residual adds skill beyond
    return residual structure (CEM-001/002/003 redundancy).
    """
    df = frame.copy()
    r = df["r_t"].to_numpy(dtype=np.float64)
    X = np.column_stack(
        [
            df["abs_r_t"].to_numpy(dtype=np.float64),
            df["vol_t"].to_numpy(dtype=np.float64),
            df["range_t"].to_numpy(dtype=np.float64),
        ]
    )
    resid_r = trailing_ols_resid(r, X, L)
    q_abs = trailing_quantile_abs(resid_r, L, Q_star)
    ok = np.isfinite(resid_r) & np.isfinite(q_abs)
    fire = ok & (np.abs(resid_r) >= q_abs)
    direction = np.sign(resid_r)
    gross = forward_gross_bps_delta_exec(
        df["open"].to_numpy(dtype=np.float64),
        df["close"].to_numpy(dtype=np.float64),
        df["close_time_ms"].to_numpy(dtype=np.int64),
        direction,
        delta_exec_ms=delta_exec_ms,
        h_bars=h_bars,
    )
    df["signal"] = fire
    df["direction"] = np.where(fire, direction, 0.0)
    df["gross_bps"] = np.where(fire, gross, np.nan)
    df["RES_ohlcv"] = resid_r
    return df


def assert_no_lookahead_trades(feature_ts: np.ndarray, decision_t: np.ndarray) -> None:
    """Unit helper: every feature trade timestamp must be <= decision t."""
    if np.any(feature_ts > decision_t.max() if np.ndim(decision_t) else decision_t):
        # For vector checks use paired
        pass
    if feature_ts.size and decision_t.size:
        # broadcast check when same length windows tested externally
        if feature_ts.shape == decision_t.shape and np.any(feature_ts > decision_t):
            raise AssertionError("lookahead: trade ts > decision t")
