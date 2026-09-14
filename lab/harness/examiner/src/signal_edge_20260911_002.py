"""EDGE-20260911-002: large-trade same-side clustering + persistence — no lookahead.

S* = trailing p-quantile of trade size over L_size prints ending at t (from cache)
LRG_side = signed notional of prints with size >= S* in W
CLUST = |LRG_side| / total notional
PERS = agreement of sign(LRG) across K sub-windows
Fire: CLUST >= C* AND PERS >= P* AND |LRG| >= V_min AND max_print_share <= α
Direction = sign(LRG_side)

Not L2-005/006. Cite CEM-20260910-001/002/003.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .signal_edge_20260911_001 import (
    _log_return,
    forward_gross_bps_delta_exec,
    ohlcv_only_nested_signal,
    trailing_ols_resid,
    trailing_quantile_abs,
)
from .trades_loader import HOLDOUT_START_MS, assert_no_holdout_trades


def build_edge002_frame(
    bar_flow: pd.DataFrame,
    *,
    C_star: float = 0.50,
    P_star: float = 0.67,
    V_min: float = 0.0,
    alpha_single: float = 0.50,
    delta_exec_ms: int = 500,
    h_bars: int = 1,
    mode: str = "primary",
) -> pd.DataFrame:
    """Build EDGE-002 signal frame.

    mode:
      - primary: real large-print clustering + PERS
      - scramble_sides: use lrg_side_scrambled / recompute clust from abs
      - size_shuffle: use size-rank shuffle columns
      - kill_pers: primary but ignore PERS gate (set PERS pass)
      - single_spike: kill_pers alias for spike-only (PERS off)
    """
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
    with np.errstate(divide="ignore", invalid="ignore"):
        range_t = (high - low) / close

    if mode == "scramble_sides":
        ls = df["lrg_side_scrambled"].to_numpy(dtype=np.float64)
        tot = df["total_notional_1m"].to_numpy(dtype=np.float64)
        cl = np.abs(ls) / np.maximum(tot, 1e-12)
        pe = df["pers"].to_numpy(dtype=np.float64)  # persistence on real large mask; conservative
    elif mode == "size_shuffle":
        ls = df["lrg_side_size_shuf"].to_numpy(dtype=np.float64)
        cl = df["clust_size_shuf"].to_numpy(dtype=np.float64)
        pe = df["pers_size_shuf"].to_numpy(dtype=np.float64)
    else:
        ls = df["lrg_side"].to_numpy(dtype=np.float64)
        cl = df["clust"].to_numpy(dtype=np.float64)
        pe = df["pers"].to_numpy(dtype=np.float64)

    max_share = df["max_print_share"].to_numpy(dtype=np.float64)
    s_star = df["s_star"].to_numpy(dtype=np.float64)

    require_pers = mode not in ("kill_pers", "single_spike")
    filled = (
        df["feature_filled"].to_numpy(dtype=bool)
        if "feature_filled" in df.columns
        else np.ones(len(df), dtype=bool)
    )
    ok = (
        np.isfinite(ls)
        & np.isfinite(cl)
        & np.isfinite(s_star)
        & (max_share <= alpha_single)
        & (np.abs(ls) >= V_min)
        & np.isfinite(r)
        & filled
    )
    fire = ok & (cl >= C_star)
    if require_pers:
        fire = fire & (pe >= P_star)

    direction = np.sign(ls)
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
    out["LRG_side"] = ls
    out["CLUST"] = cl
    out["PERS"] = pe
    out["signal"] = fire
    out["direction"] = np.where(fire, direction, 0.0)
    out["gross_bps"] = np.where(fire, gross, np.nan)
    out["timestamp"] = pd.to_datetime(out["open_time_ms"], unit="ms", utc=True)
    out["mode"] = mode
    return out


# re-export nested control helper
__all__ = [
    "build_edge002_frame",
    "ohlcv_only_nested_signal",
    "trailing_ols_resid",
    "trailing_quantile_abs",
]
