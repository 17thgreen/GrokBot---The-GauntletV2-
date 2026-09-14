"""EDGE-20260911-006 CAT_FUND_OI_C5 — funding extreme × elevated OI.

Primary: Z=2.5, D=3, L=42, Q_oi=0.80, L_oi=288, Δ_exec=1×5m, h=15m.
Signal: FundExt ∧ OIHigh; against sign(funding).
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .catalyst_common import (
    bar_log_return,
    forward_gross_bps_open_to_open,
    trailing_quantile,
)
from .signal_edge_20260911_004 import join_oi_to_ohlcv
from .signal_edge_20260911_005 import (
    align_funding_to_bars,
    compute_funding_print_features,
)
from .trades_loader import HOLDOUT_START_MS


def build_edge006_frame(
    ohlcv: pd.DataFrame,
    funding: pd.DataFrame,
    oi: pd.DataFrame,
    *,
    Z: float = 2.5,
    D: int = 3,
    L: int = 42,
    Q_oi: float = 0.80,
    L_oi: int = 288,
    h_bars: int = 3,
    delta_exec_bars: int = 1,
    mode: str = "interaction",
) -> pd.DataFrame:
    """mode: interaction | funding_only | oi_only."""
    feat = compute_funding_print_features(funding, Z=Z, D=D, L=L)
    base = align_funding_to_bars(ohlcv, feat)
    df = join_oi_to_ohlcv(base, oi)
    if (df["open_time_ms"] >= HOLDOUT_START_MS).any():
        df = df.loc[df["open_time_ms"] < HOLDOUT_START_MS].reset_index(drop=True)

    close = df["close"].to_numpy(dtype=np.float64)
    df["r_t"] = bar_log_return(close)
    df["abs_r_t"] = np.abs(df["r_t"].to_numpy())
    df["vol_t"] = df["volume"].to_numpy(dtype=np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        df["range_t"] = (df["high"] - df["low"]) / df["close"]

    oi_lvl = df["oi"].to_numpy(dtype=np.float64)
    q_oi = trailing_quantile(oi_lvl, L_oi, Q_oi)
    oi_high = np.isfinite(oi_lvl) & np.isfinite(q_oi) & (oi_lvl >= q_oi)

    # Recompute fund_ext fire from align (signal column currently FundExt-once)
    fund_fire = df["signal"].to_numpy(dtype=bool)
    crowded = df["crowded_sign"].to_numpy(dtype=np.float64)

    if mode == "funding_only":
        fire = fund_fire & (crowded != 0)
    elif mode == "oi_only":
        # Fire once when OI newly crosses high while present — approx: oi_high
        # and prior bar not oi_high (edge trigger) [A]
        prev_high = np.roll(oi_high, 1)
        prev_high[0] = False
        fire = oi_high & (~prev_high) & np.isfinite(oi_lvl)
        # direction: fade recent return as weak proxy without funding — use -sign(r)
        r = df["r_t"].to_numpy(dtype=np.float64)
        direction = np.where(fire & np.isfinite(r) & (r != 0), -np.sign(r), 0.0)
        fire = fire & (direction != 0)
        df["signal"] = fire
        df["direction"] = direction
        gross = forward_gross_bps_open_to_open(
            df["open"].to_numpy(dtype=np.float64),
            direction,
            delta_exec_bars=delta_exec_bars,
            h_bars=h_bars,
        )
        df["gross_bps"] = np.where(fire, gross, np.nan)
        df["oi_high"] = oi_high
        df["timestamp"] = pd.to_datetime(df["open_time_ms"], unit="ms", utc=True)
        return df
    else:
        # interaction: FundExt fire AND oi_high at same bar
        fire = fund_fire & oi_high & (crowded != 0)

    direction = np.where(fire, -crowded, 0.0)
    df["signal"] = fire
    df["direction"] = direction
    df["oi_high"] = oi_high
    gross = forward_gross_bps_open_to_open(
        df["open"].to_numpy(dtype=np.float64),
        direction,
        delta_exec_bars=delta_exec_bars,
        h_bars=h_bars,
    )
    df["gross_bps"] = np.where(fire, gross, np.nan)
    df["timestamp"] = pd.to_datetime(df["open_time_ms"], unit="ms", utc=True)
    return df
