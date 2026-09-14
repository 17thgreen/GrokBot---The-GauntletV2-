"""EDGE-20260910-003 signal: range-expansion snapback — no lookahead.

range_t = (high - low) / close  [A card lock]
r_t     = log(close[t] / close[t-1])  [card SIGNAL]
Q_p     = trailing empirical p-quantile of range over L completed bars ending at t
Signal when range_t >= Q_p and |r_t| > epsilon
Position = -Sign(r_t); exit flat at close t+h
Gross fade bps = (-Sign(r_t)) * (close[t+h]/close[t]-1) * 1e4

Contrast (diagnostic): range below trailing median with |r|>ε; same fade position.
Cite CEM-20260910-001: opposite activity conditioning — NOT a rescue of EDGE-001.
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


def range_normalized(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """range_t = (high - low) / close  [A]."""
    c = close.astype(float).replace(0.0, np.nan)
    return ((high.astype(float) - low.astype(float)) / c).rename("range")


def trailing_quantile(series: pd.Series, L: int, q: float) -> pd.Series:
    """Trailing empirical quantile over L completed bars ending at t (no future)."""
    if L < 1:
        raise ValueError("L must be >= 1")
    if not (0.0 < q < 1.0):
        raise ValueError("q must be in (0,1)")
    return series.rolling(window=L, min_periods=L).quantile(q)


def compute_features(
    df: pd.DataFrame,
    L: int,
    p: float,
    contrast_q: float = 0.5,
) -> pd.DataFrame:
    """Add r, range, Q_hi_trail (p), Q_med_trail (contrast). Index preserved."""
    out = df.copy()
    out["r"] = close_to_close_log_returns(out["close"])
    out["range"] = range_normalized(out["high"], out["low"], out["close"])
    out["Q_hi_trail"] = trailing_quantile(out["range"], L, p)
    out["Q_med_trail"] = trailing_quantile(out["range"], L, contrast_q)
    return out


def fire_signal(features: pd.DataFrame, epsilon: float) -> pd.Series:
    """Boolean: range >= Q_p and |r| > epsilon; False where incomplete."""
    rng = features["range"]
    qhi = features["Q_hi_trail"]
    r = features["r"]
    ok = rng.notna() & qhi.notna() & r.notna()
    return ok & (rng >= qhi) & (r.abs() > epsilon)


def non_extreme_mask(features: pd.DataFrame, epsilon: float) -> pd.Series:
    """Contrast bin: range < trailing median and |r| > epsilon."""
    rng = features["range"]
    qmed = features["Q_med_trail"]
    r = features["r"]
    ok = rng.notna() & qmed.notna() & r.notna()
    return ok & (rng < qmed) & (r.abs() > epsilon)


def fade_forward_bps(close: pd.Series, r: pd.Series, h: int) -> pd.Series:
    """Gross fade return in bps: (-Sign(r_t)) * (close[t+h]/close[t]-1) * 1e4.

    Last h bars NaN (no future available for label).
    """
    if h < 1:
        raise ValueError("h must be >= 1")
    fwd = close.shift(-h) / close - 1.0
    sign = np.sign(r.to_numpy(dtype=float))
    aligned = (-sign) * fwd.to_numpy(dtype=float) * 1e4
    return pd.Series(aligned, index=close.index, name="gross_bps")


def build_trade_frame(
    df: pd.DataFrame,
    L: int,
    p: float,
    h: int,
    epsilon: float,
    contrast_q: float = 0.5,
) -> pd.DataFrame:
    """Full feature + signal + contrast + fade gross bps for one cell."""
    feat = compute_features(df, L=L, p=p, contrast_q=contrast_q)
    feat["signal"] = fire_signal(feat, epsilon)
    # Alias low_range / high_rv for metrics.slice_metrics high_col contrast
    feat["low_range"] = non_extreme_mask(feat, epsilon)
    feat["high_rv"] = feat["low_range"]  # reuse default high_col name in slice_metrics
    feat["gross_bps"] = fade_forward_bps(feat["close"], feat["r"], h)
    feat["position"] = np.where(feat["signal"], -np.sign(feat["r"]), 0.0)
    return feat
