"""EDGE-20260910-004 signal: BTC lead → ETH response (cross-asset) — no lookahead.

r = close-to-close log returns (BTC and ETH).
Q_p = trailing p-quantile of |r_lead| over L completed lead bars ending at t.
Fire when: |r_lead_t| >= Q_p AND |r_follow_t| <= kappa * |r_lead_t|
Position on follow = Sign(r_lead_t); exit flat at close t+h.
Align on exchange event timestamps; drop unaligned bars.

Cite CEM-20260910-001 / CEM-20260910-002 — NOT a rescue of either.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def close_to_close_log_returns(close: pd.Series) -> pd.Series:
    """r_t = log(close[t]/close[t-1]); first bar NaN."""
    prev = close.shift(1)
    with np.errstate(divide="ignore", invalid="ignore"):
        r = np.log(close.astype(float) / prev.astype(float))
    return pd.Series(r, index=close.index, name="r")


def trailing_quantile(series: pd.Series, L: int, q: float) -> pd.Series:
    """Trailing empirical quantile over L completed bars ending at t (no future)."""
    if L < 1:
        raise ValueError("L must be >= 1")
    if not (0.0 < q < 1.0):
        raise ValueError("q must be in (0,1)")
    return series.rolling(window=L, min_periods=L).quantile(q)


def align_cross_asset(
    lead_df: pd.DataFrame,
    follow_df: pd.DataFrame,
    *,
    lead_prefix: str = "lead",
    follow_prefix: str = "follow",
) -> pd.DataFrame:
    """Inner-join on timestamp; drop unaligned bars. Preserves sorted unique timestamps."""
    need = ["timestamp", "open", "high", "low", "close", "volume"]
    for name, df in (("lead", lead_df), ("follow", follow_df)):
        missing = [c for c in need if c not in df.columns]
        if missing:
            raise ValueError(f"{name} OHLCV missing columns: {missing}")

    L = lead_df[need].copy().rename(
        columns={c: f"{lead_prefix}_{c}" if c != "timestamp" else c for c in need}
    )
    F = follow_df[need].copy().rename(
        columns={c: f"{follow_prefix}_{c}" if c != "timestamp" else c for c in need}
    )
    # Ensure timestamp comparable
    L["timestamp"] = pd.to_datetime(L["timestamp"], utc=True)
    F["timestamp"] = pd.to_datetime(F["timestamp"], utc=True)
    L = L.drop_duplicates(subset=["timestamp"], keep="first")
    F = F.drop_duplicates(subset=["timestamp"], keep="first")
    merged = pd.merge(L, F, on="timestamp", how="inner", validate="one_to_one")
    merged = merged.sort_values("timestamp").reset_index(drop=True)
    return merged


def build_trade_frame_cross(
    lead_df: pd.DataFrame,
    follow_df: pd.DataFrame,
    *,
    L: int,
    p: float,
    h: int,
    kappa: float,
    apply_kappa: bool = True,
) -> pd.DataFrame:
    """Aligned cross-asset features + signal + sign-aligned forward gross bps on follow.

    Gross bps = Sign(r_lead_t) * (close_follow[t+h]/close_follow[t] - 1) * 1e4
    Last h bars have NaN labels (no future).
    """
    if h < 1:
        raise ValueError("h must be >= 1")
    if kappa < 0:
        raise ValueError("kappa must be >= 0")

    aligned = align_cross_asset(lead_df, follow_df)
    out = aligned.copy()
    out["r_lead"] = close_to_close_log_returns(out["lead_close"])
    out["r_follow"] = close_to_close_log_returns(out["follow_close"])
    out["abs_r_lead"] = out["r_lead"].abs()
    out["abs_r_follow"] = out["r_follow"].abs()
    out["Q_p"] = trailing_quantile(out["abs_r_lead"], L, p)

    ok = (
        out["r_lead"].notna()
        & out["r_follow"].notna()
        & out["Q_p"].notna()
    )
    large_lead = out["abs_r_lead"] >= out["Q_p"]
    if apply_kappa:
        kappa_ok = out["abs_r_follow"] <= (kappa * out["abs_r_lead"])
        out["signal"] = ok & large_lead & kappa_ok
    else:
        out["signal"] = ok & large_lead
        out["kappa_gate_skipped"] = True

    # Forward simple return on follow asset
    fwd = out["follow_close"].shift(-h) / out["follow_close"] - 1.0
    sign = np.sign(out["r_lead"].to_numpy(dtype=float))
    out["gross_bps"] = pd.Series(
        sign * fwd.to_numpy(dtype=float) * 1e4,
        index=out.index,
        name="gross_bps",
    )
    out["position"] = np.where(out["signal"], sign, 0.0)
    # Alias for metrics helpers that expect high_rv contrast column
    out["high_rv"] = False
    return out


def build_btc_to_eth(
    btc: pd.DataFrame,
    eth: pd.DataFrame,
    *,
    L: int,
    p: float,
    h: int,
    kappa: float,
    apply_kappa: bool = True,
) -> pd.DataFrame:
    """Primary claim: BTC lead → trade ETH."""
    return build_trade_frame_cross(
        btc, eth, L=L, p=p, h=h, kappa=kappa, apply_kappa=apply_kappa
    )


def build_eth_to_btc_reverse(
    btc: pd.DataFrame,
    eth: pd.DataFrame,
    *,
    L: int,
    p: float,
    h: int,
    kappa: float,
) -> pd.DataFrame:
    """Control: ETH lead → trade BTC under same p/L/h/kappa."""
    return build_trade_frame_cross(
        eth, btc, L=L, p=p, h=h, kappa=kappa, apply_kappa=True
    )


def timestamp_shuffle_btc(
    btc: pd.DataFrame,
    eth: pd.DataFrame,
    *,
    L: int,
    p: float,
    h: int,
    kappa: float,
    seed: int = 20260910,
) -> pd.DataFrame:
    """Placebo: shuffle BTC OHLCV rows relative to timestamps, then realign to ETH.

    Keeps ETH timeline fixed; BTC price path is randomly reassigned to BTC timestamps
    (circular-safe permutation of row content excluding timestamp).
    """
    rng = np.random.default_rng(seed)
    btc_sh = btc.copy().reset_index(drop=True)
    n = len(btc_sh)
    if n == 0:
        return build_btc_to_eth(btc, eth, L=L, p=p, h=h, kappa=kappa)
    perm = rng.permutation(n)
    price_cols = [c for c in ("open", "high", "low", "close", "volume") if c in btc_sh.columns]
    shuffled_vals = btc_sh[price_cols].iloc[perm].reset_index(drop=True)
    btc_sh[price_cols] = shuffled_vals.to_numpy()
    return build_btc_to_eth(btc_sh, eth, L=L, p=p, h=h, kappa=kappa)
