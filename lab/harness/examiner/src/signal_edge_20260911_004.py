"""EDGE-20260911-004 CAT_OI_SHOCK_C5 — OI shock + divergence + flush trigger.

Primary: Z=2.5, L_oi=288, Q_lo=0.33, T_wait=2×5m, Δ_exec=1×5m, h=10m,
direction=flush-with-trigger.
Trigger aggression [A]: sign(r) of first bar with |r|>ε (ε=5e-05) if trades
trigger unavailable.
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
from .trades_loader import HOLDOUT_START_MS

EPS_TRIGGER = 5e-05


def join_oi_to_ohlcv(ohlcv: pd.DataFrame, oi: pd.DataFrame) -> pd.DataFrame:
    """Left-join OI level on open_time == create_time_ms. No forward-fill."""
    df = ohlcv.copy()
    if (df["open_time_ms"] >= HOLDOUT_START_MS).any():
        df = df.loc[df["open_time_ms"] < HOLDOUT_START_MS].reset_index(drop=True)
    oi2 = oi[["create_time_ms", "sum_open_interest"]].drop_duplicates("create_time_ms")
    oi2 = oi2.rename(columns={"create_time_ms": "open_time_ms", "sum_open_interest": "oi"})
    out = df.merge(oi2, on="open_time_ms", how="left")
    return out


def build_edge004_frame(
    ohlcv: pd.DataFrame,
    oi: pd.DataFrame,
    *,
    Z: float = 2.5,
    L_oi: int = 288,
    Q_lo: float = 0.33,
    T_wait: int = 2,
    h_bars: int = 2,
    delta_exec_bars: int = 1,
    eps: float = EPS_TRIGGER,
    divergence: bool = True,
) -> pd.DataFrame:
    """Build OI-shock flush-with-trigger frame.

    If divergence=False, require LARGE |r| instead of small (kill-control cohort).
    """
    df = join_oi_to_ohlcv(ohlcv, oi)
    close = df["close"].to_numpy(dtype=np.float64)
    r = bar_log_return(close)
    abs_r = np.abs(r)
    oi_lvl = df["oi"].to_numpy(dtype=np.float64)
    # ΔOI only on consecutive bars both with OI present (gap abstention) [V Clock]
    doi = np.full(len(df), np.nan, dtype=np.float64)
    present = np.isfinite(oi_lvl)
    both = present[1:] & present[:-1]
    doi[1:] = np.where(both, oi_lvl[1:] - oi_lvl[:-1], np.nan)
    abs_doi = np.abs(doi)
    z_doi = trailing_z(abs_doi, L_oi)
    q_abs_r = trailing_quantile(abs_r, L_oi, Q_lo)

    shock = np.isfinite(z_doi) & (z_doi >= Z) & np.isfinite(doi)
    if divergence:
        div = np.isfinite(q_abs_r) & np.isfinite(abs_r) & (abs_r <= q_abs_r)
    else:
        # large-|r| discovery cohort control
        q_hi = trailing_quantile(abs_r, L_oi, 1.0 - Q_lo)
        div = np.isfinite(q_hi) & np.isfinite(abs_r) & (abs_r >= q_hi)

    candidate = shock & div

    # Trigger within T_wait bars after candidate bar t (exclusive of t)
    n = len(df)
    fire = np.zeros(n, dtype=bool)
    direction = np.zeros(n, dtype=np.float64)
    trigger_of = np.full(n, -1, dtype=np.int64)
    # Mark candidate bars; search forward
    cand_idx = np.where(candidate)[0]
    claimed_triggers = set()
    for t in cand_idx:
        trig = None
        d = 0.0
        for k in range(1, T_wait + 1):
            j = t + k
            if j >= n:
                break
            if not np.isfinite(r[j]):
                continue
            if abs(r[j]) > eps:
                trig = j
                d = float(np.sign(r[j]))
                break
        if trig is None or d == 0.0:
            continue
        if trig in claimed_triggers:
            continue
        # Fire at trigger bar t* (knowable); entry at t*+Δ_exec
        fire[trig] = True
        direction[trig] = d
        trigger_of[trig] = t
        claimed_triggers.add(trig)

    df["r_t"] = r
    df["abs_r_t"] = abs_r
    df["vol_t"] = df["volume"].to_numpy(dtype=np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        df["range_t"] = (df["high"] - df["low"]) / df["close"]
    df["doi"] = doi
    df["z_abs_doi"] = z_doi
    df["signal"] = fire
    df["direction"] = direction
    df["shock_bar"] = trigger_of

    gross = forward_gross_bps_open_to_open(
        df["open"].to_numpy(dtype=np.float64),
        direction,
        delta_exec_bars=delta_exec_bars,
        h_bars=h_bars,
    )
    df["gross_bps"] = np.where(fire, gross, np.nan)
    df["timestamp"] = pd.to_datetime(df["open_time_ms"], unit="ms", utc=True)
    return df


def ohlcv_nested_vol_div(
    frame: pd.DataFrame,
    *,
    L: int = 288,
    Q_lo: float = 0.33,
    Z_vol: float = 2.5,
    T_wait: int = 2,
    h_bars: int = 2,
    delta_exec_bars: int = 1,
    eps: float = EPS_TRIGGER,
) -> pd.DataFrame:
    """OHLCV nested without OI: high |Δvolume| z + small |r|, then flush trigger."""
    df = frame.copy()
    vol = df["vol_t"].to_numpy(dtype=np.float64) if "vol_t" in df.columns else df["volume"].to_numpy(dtype=np.float64)
    dvol = np.full(len(df), np.nan)
    dvol[1:] = np.diff(vol)
    abs_dvol = np.abs(dvol)
    z = trailing_z(abs_dvol, L)
    r = df["r_t"].to_numpy(dtype=np.float64)
    abs_r = np.abs(r)
    q = trailing_quantile(abs_r, L, Q_lo)
    candidate = np.isfinite(z) & (z >= Z_vol) & np.isfinite(q) & (abs_r <= q)
    n = len(df)
    fire = np.zeros(n, dtype=bool)
    direction = np.zeros(n, dtype=np.float64)
    claimed = set()
    for t in np.where(candidate)[0]:
        for k in range(1, T_wait + 1):
            j = t + k
            if j >= n:
                break
            if np.isfinite(r[j]) and abs(r[j]) > eps:
                if j in claimed:
                    break
                fire[j] = True
                direction[j] = float(np.sign(r[j]))
                claimed.add(j)
                break
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
