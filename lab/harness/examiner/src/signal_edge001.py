"""EDGE-20260910-001 signal: low-RV continuation with no lookahead.

RV_t = sum of squared close-to-close returns over W completed bars ending at t.
Q_lo = trailing empirical quantile of RV over L completed bars ending at t.
Signal when RV_t <= Q_lo and |r_t| > epsilon.
Position = Sign(r_t); exit flat at close t+h.
Gross forward bps (sign-aligned): Sign(r_t) * (close[t+h]/close[t]-1)*1e4
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def close_to_close_returns(close: pd.Series) -> pd.Series:
    """r_t = close[t]/close[t-1] - 1; first bar NaN (no prior)."""
    return close.pct_change()


def realized_vol(r: pd.Series, W: int) -> pd.Series:
    """RV_t = sum of r^2 over W completed bars ending at t (inclusive).

    Uses rolling sum of squared returns with window W; requires W non-NaN
    observations. No future bars enter the window.
    """
    if W < 1:
        raise ValueError("W must be >= 1")
    sq = r.pow(2)
    # min_periods=W ensures incomplete warmup is NaN
    return sq.rolling(window=W, min_periods=W).sum()


def trailing_quantile(series: pd.Series, L: int, q: float) -> pd.Series:
    """Trailing empirical quantile over L completed bars ending at t.

    No future bars; uses expanding-into-rolling window of past L values of series.
    """
    if L < 1:
        raise ValueError("L must be >= 1")
    if not (0.0 < q < 1.0):
        raise ValueError("q must be in (0,1)")
    return series.rolling(window=L, min_periods=L).quantile(q)


def compute_features(
    df: pd.DataFrame,
    W: int,
    L: int,
    Q_lo: float,
    Q_hi: float = 0.80,
) -> pd.DataFrame:
    """Add r, RV, Q_lo_trail, Q_hi_trail columns. Index preserved."""
    out = df.copy()
    out["r"] = close_to_close_returns(out["close"])
    out["RV"] = realized_vol(out["r"], W)
    out["Q_lo_trail"] = trailing_quantile(out["RV"], L, Q_lo)
    out["Q_hi_trail"] = trailing_quantile(out["RV"], L, Q_hi)
    return out


def fire_signal(features: pd.DataFrame, epsilon: float) -> pd.Series:
    """Boolean signal: RV <= Q_lo and |r| > epsilon; False where features incomplete."""
    rv = features["RV"]
    qlo = features["Q_lo_trail"]
    r = features["r"]
    ok = rv.notna() & qlo.notna() & r.notna()
    return ok & (rv <= qlo) & (r.abs() > epsilon)


def high_rv_mask(features: pd.DataFrame) -> pd.Series:
    """Contrast bin: RV >= Q_hi_trail (diagnostic only)."""
    rv = features["RV"]
    qhi = features["Q_hi_trail"]
    ok = rv.notna() & qhi.notna()
    return ok & (rv >= qhi)


def sign_aligned_forward_bps(close: pd.Series, r: pd.Series, h: int) -> pd.Series:
    """Gross forward return in bps, sign-aligned with Sign(r_t).

    Sign(r_t) * (close[t+h]/close[t] - 1) * 1e4
    Last h bars are NaN (no future available).
    """
    if h < 1:
        raise ValueError("h must be >= 1")
    fwd = close.shift(-h) / close - 1.0
    sign = np.sign(r.to_numpy(dtype=float))
    # np.sign(0)=0 → no contribution; signals already require |r|>eps
    aligned = sign * fwd.to_numpy(dtype=float) * 1e4
    return pd.Series(aligned, index=close.index, name="gross_bps")


def build_trade_frame(
    df: pd.DataFrame,
    W: int,
    L: int,
    Q_lo: float,
    h: int,
    epsilon: float,
    Q_hi: float = 0.80,
) -> pd.DataFrame:
    """Full feature + signal + forward gross bps frame for one cell."""
    feat = compute_features(df, W=W, L=L, Q_lo=Q_lo, Q_hi=Q_hi)
    feat["signal"] = fire_signal(feat, epsilon)
    feat["high_rv"] = high_rv_mask(feat)
    feat["gross_bps"] = sign_aligned_forward_bps(feat["close"], feat["r"], h)
    feat["position"] = np.where(feat["signal"], np.sign(feat["r"]), 0.0)
    return feat
