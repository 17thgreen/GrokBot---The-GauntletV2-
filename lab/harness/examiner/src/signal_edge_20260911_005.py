"""EDGE-20260911-005 CAT_FUND_EXT_C5 — funding extremes only.

Primary: Z=2.5, D=3, L=42, Δ_exec=1×5m, h=15m (h=5/10 report-only).
calc_time <= t only; no predicted funding / premiumIndex.
Position = -sign(funding).
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .catalyst_common import (
    bar_log_return,
    forward_gross_bps_open_to_open,
    trailing_quantile,
    trailing_z,
)
from .funding_loader import assert_calc_time_knowable
from .trades_loader import HOLDOUT_START_MS


def compute_funding_print_features(
    funding: pd.DataFrame,
    *,
    Z: float = 2.5,
    D: int = 3,
    L: int = 42,
) -> pd.DataFrame:
    """Per-print z and FundExt flag (no bar clock yet)."""
    f = funding.sort_values("calc_time").drop_duplicates("calc_time").reset_index(drop=True)
    rate = f["last_funding_rate"].to_numpy(dtype=np.float64)
    z = trailing_z(rate, L)
    sign = np.sign(rate)
    extreme = np.isfinite(z) & (np.abs(z) >= Z) & (sign != 0)
    # D consecutive same-sign extremes ending at i
    fund_ext = np.zeros(len(f), dtype=bool)
    for i in range(len(f)):
        if i + 1 < D:
            continue
        window = slice(i - D + 1, i + 1)
        if not np.all(extreme[window]):
            continue
        if len(set(sign[window].tolist())) != 1:
            continue
        fund_ext[i] = True
    out = f.copy()
    out["z_funding"] = z
    out["fund_ext"] = fund_ext
    out["crowded_sign"] = sign
    return out


def align_funding_to_bars(
    ohlcv: pd.DataFrame,
    funding_feat: pd.DataFrame,
) -> pd.DataFrame:
    """Attach latest knowable funding print features to each bar.

    Decision t = close_time_ms. Print knowable iff calc_time <= t.
    Fire once per extreme print: on the first bar with close_time >= calc_time
    when that print has fund_ext=True. [A]
    """
    df = ohlcv.copy()
    if (df["open_time_ms"] >= HOLDOUT_START_MS).any():
        df = df.loc[df["open_time_ms"] < HOLDOUT_START_MS].reset_index(drop=True)

    close_t = df["close_time_ms"].to_numpy(dtype=np.int64)
    calc = funding_feat["calc_time"].to_numpy(dtype=np.int64)
    # asof: for each bar, index of last funding print with calc_time <= close_t
    idx = np.searchsorted(calc, close_t, side="right") - 1
    valid = idx >= 0

    z = np.full(len(df), np.nan)
    rate = np.full(len(df), np.nan)
    crowded = np.zeros(len(df), dtype=np.float64)
    calc_used = np.full(len(df), -1, dtype=np.int64)
    fund_ext_print = np.zeros(len(df), dtype=bool)
    z[valid] = funding_feat["z_funding"].to_numpy()[idx[valid]]
    rate[valid] = funding_feat["last_funding_rate"].to_numpy()[idx[valid]]
    crowded[valid] = funding_feat["crowded_sign"].to_numpy()[idx[valid]]
    calc_used[valid] = calc[idx[valid]]
    fund_ext_print[valid] = funding_feat["fund_ext"].to_numpy()[idx[valid]]

    assert_calc_time_knowable(calc_used[valid], close_t[valid])

    # First bar per extreme print
    fire = np.zeros(len(df), dtype=bool)
    seen = set()
    for i in range(len(df)):
        if not valid[i] or not fund_ext_print[i]:
            continue
        ct = int(calc_used[i])
        if ct in seen:
            continue
        # first bar where this print is knowable
        if close_t[i] >= ct:
            fire[i] = True
            seen.add(ct)

    direction = np.where(fire, -crowded, 0.0)
    # If crowded sign 0, no trade
    direction = np.where(crowded == 0, 0.0, direction)
    fire = fire & (direction != 0)

    return df.assign(
        z_funding=z,
        funding_rate=rate,
        crowded_sign=crowded,
        funding_calc_time=calc_used,
        signal=fire,
        direction=direction,
    )


def build_edge005_frame(
    ohlcv: pd.DataFrame,
    funding: pd.DataFrame,
    *,
    Z: float = 2.5,
    D: int = 3,
    L: int = 42,
    h_bars: int = 3,
    delta_exec_bars: int = 1,
) -> pd.DataFrame:
    feat = compute_funding_print_features(funding, Z=Z, D=D, L=L)
    df = align_funding_to_bars(ohlcv, feat)
    close = df["close"].to_numpy(dtype=np.float64)
    df["r_t"] = bar_log_return(close)
    df["abs_r_t"] = np.abs(df["r_t"].to_numpy())
    df["vol_t"] = df["volume"].to_numpy(dtype=np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        df["range_t"] = (df["high"] - df["low"]) / df["close"]

    gross = forward_gross_bps_open_to_open(
        df["open"].to_numpy(dtype=np.float64),
        df["direction"].to_numpy(dtype=np.float64),
        delta_exec_bars=delta_exec_bars,
        h_bars=h_bars,
    )
    df["gross_bps"] = np.where(df["signal"].to_numpy(), gross, np.nan)
    df["timestamp"] = pd.to_datetime(df["open_time_ms"], unit="ms", utc=True)
    return df


def ohlcv_nested_fade_extreme(
    frame: pd.DataFrame,
    *,
    L: int = 288,
    Q: float = 0.80,
    h_bars: int = 3,
    delta_exec_bars: int = 1,
) -> pd.DataFrame:
    """OHLCV nested: fade large |r| bars (no funding)."""
    df = frame.copy()
    abs_r = df["abs_r_t"].to_numpy(dtype=np.float64)
    q = trailing_quantile(abs_r, L, Q)
    r = df["r_t"].to_numpy(dtype=np.float64)
    ok = np.isfinite(abs_r) & np.isfinite(q) & np.isfinite(r) & (r != 0)
    fire = ok & (abs_r >= q)
    direction = np.where(fire, -np.sign(r), 0.0)
    gross = forward_gross_bps_open_to_open(
        df["open"].to_numpy(dtype=np.float64),
        direction,
        delta_exec_bars=delta_exec_bars,
        h_bars=h_bars,
    )
    df["signal"] = fire
    df["direction"] = direction
    df["gross_bps"] = np.where(fire, gross, np.nan)
    return df


def trade_flow_nested_from_flow(
    frame: pd.DataFrame,
    bar_flow: pd.DataFrame,
    *,
    L: int = 288,
    Q_star: float = 0.80,
    N_min: int = 20,
    h_bars: int = 3,
    delta_exec_bars: int = 1,
) -> pd.DataFrame:
    """Optional trade-flow nested using cached bar_flow IMB extreme (CEM family)."""
    from .signal_edge_20260911_001 import trailing_ols_resid, trailing_quantile_abs

    df = frame.copy()
    cols = ["open_time_ms", "n_buy_1m", "n_sell_1m"]
    if "feature_filled" in bar_flow.columns:
        cols.append("feature_filled")
    merged = df[["open_time_ms"]].merge(
        bar_flow[cols].drop_duplicates("open_time_ms"),
        on="open_time_ms",
        how="left",
    )
    nb = merged["n_buy_1m"].to_numpy(dtype=np.float64)
    ns = merged["n_sell_1m"].to_numpy(dtype=np.float64)
    if "feature_filled" in merged.columns:
        filled = merged["feature_filled"].fillna(False).to_numpy(dtype=bool)
    else:
        filled = np.isfinite(nb) & np.isfinite(ns)
    imb = (nb - ns) / np.maximum(nb + ns, 1.0)
    r = df["r_t"].to_numpy(dtype=np.float64)
    X = np.column_stack(
        [
            r,
            df["abs_r_t"].to_numpy(dtype=np.float64),
            df["vol_t"].to_numpy(dtype=np.float64),
            df["range_t"].to_numpy(dtype=np.float64),
        ]
    )
    resid = trailing_ols_resid(imb, X, L, refresh=32)
    q_abs = trailing_quantile_abs(resid, L, Q_star)
    n_tot = nb + ns
    ok = np.isfinite(resid) & np.isfinite(q_abs) & (n_tot >= N_min) & filled
    fire = ok & (np.abs(resid) >= q_abs)
    direction = np.where(fire, np.sign(resid), 0.0)
    gross = forward_gross_bps_open_to_open(
        df["open"].to_numpy(dtype=np.float64),
        direction,
        delta_exec_bars=delta_exec_bars,
        h_bars=h_bars,
    )
    df["signal"] = fire
    df["direction"] = direction
    df["gross_bps"] = np.where(fire, gross, np.nan)
    return df
