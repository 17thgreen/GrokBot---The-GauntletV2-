"""Shared Catalyst Cycle-5 helpers: OHLCV slices, forward returns, stats, seals."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

import numpy as np
import pandas as pd

from .costs import DEFAULT_COSTS
from .metrics import concentration_frac, distinct_signal_days, mean_or_none, newey_west_mean_se
from .trades_loader import HOLDOUT_START_MS

BAR_MS = 300_000
CLOSE_OFFSET_MS = 299_999

# Funding-only RESEARCH bounds (SEAL_LOCK open)
FUND_RESEARCH_FIRST = pd.Timestamp("2021-01-03T04:00:00Z")
FUND_RESEARCH_LAST = pd.Timestamp("2024-05-27T06:15:00Z")
# Joint OI RESEARCH
OI_RESEARCH_FIRST = pd.Timestamp("2021-12-01T00:00:00Z")
OI_RESEARCH_LAST = pd.Timestamp("2024-05-27T06:15:00Z")
VALIDATION_FIRST = pd.Timestamp("2024-05-27T06:20:00Z")
VALIDATION_LAST = pd.Timestamp("2025-07-14T15:00:00Z")

CEM_CATALYST = [
    "CEM-20260911-001",
    "CEM-20260911-002",
    "CEM-20260910-001",
    "CEM-20260910-002",
    "CEM-20260910-003",
]


def load_ohlcv_open_slices(
    ohlcv_dir: Path,
    symbol: str,
    *,
    include_validation: bool = True,
) -> pd.DataFrame:
    """Load warmup+research(+validation) OHLCV; NEVER open sealed holdout."""
    slices = Path(ohlcv_dir) / "slices"
    sealed = Path(ohlcv_dir) / "sealed"
    # Path.exists only — do not read sealed parquet
    _ = (sealed / f"{symbol}_5m_HISTORICAL_HOLDOUT.parquet").exists()

    parts = [
        slices / f"{symbol}_5m_WARMUP_PREFIX.parquet",
        slices / f"{symbol}_5m_RESEARCH.parquet",
    ]
    if include_validation:
        parts.append(slices / f"{symbol}_5m_VALIDATION.parquet")
    frames = []
    for p in parts:
        if not p.exists():
            raise FileNotFoundError(p)
        # Guard: refuse any path under sealed/
        if "sealed" in p.parts:
            raise RuntimeError(f"refusing sealed path: {p}")
        frames.append(pd.read_parquet(p))
    df = pd.concat(frames, ignore_index=True)
    df = df.sort_values("open_time_ms").drop_duplicates(subset=["open_time_ms"], keep="first")
    df = df.loc[df["open_time_ms"] < HOLDOUT_START_MS].reset_index(drop=True)
    if (df["open_time_ms"] >= HOLDOUT_START_MS).any():
        raise AssertionError("holdout rows leaked into OHLCV frame")
    df["timestamp"] = pd.to_datetime(df["open_time_ms"], unit="ms", utc=True)
    if "close_time_ms" not in df.columns:
        df["close_time_ms"] = df["open_time_ms"] + CLOSE_OFFSET_MS
    return df


def slice_mask(
    df: pd.DataFrame,
    which: str,
    *,
    research_first: pd.Timestamp,
    research_last: pd.Timestamp,
) -> pd.Series:
    ot = pd.to_datetime(df["open_time_ms"], unit="ms", utc=True)
    if which == "research":
        return (ot >= research_first) & (ot <= research_last)
    if which == "validation":
        return (ot >= VALIDATION_FIRST) & (ot <= VALIDATION_LAST)
    raise ValueError(which)


def forward_gross_bps_open_to_open(
    open_: np.ndarray,
    direction: np.ndarray,
    *,
    delta_exec_bars: int = 1,
    h_bars: int,
) -> np.ndarray:
    """[A] Entry at open[i+delta_exec_bars]; exit open[entry+h_bars].

    Consistent with prior Examiner trade-flow harness (next-bar open after decision).
    Gross bps = direction * (exit/entry - 1) * 1e4.
    """
    if delta_exec_bars < 1:
        raise ValueError("Δ_exec bars must be >= 1 for primary Catalyst cells")
    if h_bars < 1:
        raise ValueError("h_bars must be >= 1")
    n = len(open_)
    gross = np.full(n, np.nan, dtype=np.float64)
    entry_idx = np.arange(n) + delta_exec_bars
    exit_idx = entry_idx + h_bars
    valid = exit_idx < n
    ei = entry_idx[valid]
    xi = exit_idx[valid]
    ent = open_[ei]
    ex = open_[xi]
    with np.errstate(divide="ignore", invalid="ignore"):
        ret = (ex / ent - 1.0) * 1e4
    d = direction[np.where(valid)[0]]
    vi = np.where(valid)[0]
    gross[vi] = d * ret
    bad = ~np.isfinite(ent) | ~np.isfinite(ex) | (ent <= 0) | ~np.isfinite(d)
    gross[vi[bad]] = np.nan
    return gross


def bar_log_return(close: np.ndarray) -> np.ndarray:
    out = np.full(len(close), np.nan, dtype=np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        out[1:] = np.log(close[1:] / close[:-1])
    return out


def trailing_z(x: np.ndarray, L: int) -> np.ndarray:
    """Trailing z-score of x using window ending at t inclusive; min_periods=L."""
    s = pd.Series(np.asarray(x, dtype=np.float64))
    mu = s.rolling(L, min_periods=L).mean()
    sd = s.rolling(L, min_periods=L).std(ddof=0)
    z = (s - mu) / sd.replace(0.0, np.nan)
    return z.to_numpy(dtype=np.float64)


def trailing_quantile(x: np.ndarray, L: int, q: float) -> np.ndarray:
    s = pd.Series(np.asarray(x, dtype=np.float64))
    return s.rolling(L, min_periods=L).quantile(q).to_numpy(dtype=np.float64)


def signal_stats(df: pd.DataFrame, C: float = DEFAULT_COSTS.C_base) -> dict[str, Any]:
    sig = df.loc[df["signal"] & df["gross_bps"].notna()]
    n = int(len(sig))
    days = distinct_signal_days(df.assign(timestamp=df["timestamp"]), "signal")
    gross = sig["gross_bps"].to_numpy(dtype=float) if n else np.array([])
    mu = mean_or_none(gross)
    hit = float(np.mean(gross > 0)) if n else None
    mu_nw, se = newey_west_mean_se(gross, lag=max(1, int(df.attrs.get("nw_lag", 1)))) if n else (None, None)
    z = 1.959963984540054
    ci_lo = (mu_nw - z * se) if (mu_nw is not None and se is not None) else None
    ci_hi = (mu_nw + z * se) if (mu_nw is not None and se is not None) else None
    conc = concentration_frac(df.assign(timestamp=df["timestamp"]), "signal")
    return {
        "signal_count": n,
        "distinct_utc_days": days,
        "mean_gross_bps": mu,
        "mean_net_1x": (mu - C) if mu is not None else None,
        "mean_net_2x": (mu - 2 * C) if mu is not None else None,
        "mean_net_3x": (mu - 3 * C) if mu is not None else None,
        "hit_rate": hit,
        "nw_ci_low": ci_lo,
        "nw_ci_high": ci_hi,
        "concentration_day_frac": conc,
        "C_base_bps": C,
        "C_tag": "[A]",
        "funding_carry_over_hold_bps": 0,
        "funding_carry_tag": "[U] not modeled; reported 0",
    }


def maybe_load_bar_flow(cache_dir: Path, symbol: str) -> Optional[pd.DataFrame]:
    p = Path(cache_dir) / f"{symbol}_bar_flow.parquet"
    if not p.exists():
        return None
    flow = pd.read_parquet(p)
    flow = flow.loc[flow["open_time_ms"] < HOLDOUT_START_MS].reset_index(drop=True)
    return flow
