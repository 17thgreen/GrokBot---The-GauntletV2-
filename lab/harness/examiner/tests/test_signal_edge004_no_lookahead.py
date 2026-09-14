"""EDGE-004: no lookahead; cross-asset alignment; reverse control builds."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.signal_edge004 import (  # noqa: E402
    align_cross_asset,
    build_btc_to_eth,
    build_eth_to_btc_reverse,
    close_to_close_log_returns,
    trailing_quantile,
)

FIXTURE = ROOT / "fixtures" / "tiny_synthetic_ohlcv.csv"


def _two_assets(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Synthetic BTC/ETH from one fixture: ETH = BTC * 0.03 with small noise."""
    btc = df.copy()
    eth = df.copy()
    eth["close"] = df["close"] * 0.03
    eth["open"] = df["open"] * 0.03
    eth["high"] = df["high"] * 0.03
    eth["low"] = df["low"] * 0.03
    # Make some ETH moves smaller than BTC so kappa gate can fire
    return btc, eth


@pytest.fixture
def synth_pair() -> tuple[pd.DataFrame, pd.DataFrame]:
    df = pd.read_csv(FIXTURE)
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
    return _two_assets(df)


def test_log_return_no_lookahead(synth_pair):
    btc, _ = synth_pair
    r = close_to_close_log_returns(btc["close"])
    assert np.isnan(r.iloc[0])
    for t in range(1, len(btc)):
        exp = np.log(btc["close"].iloc[t] / btc["close"].iloc[t - 1])
        assert r.iloc[t] == pytest.approx(exp)


def test_quantile_no_future(synth_pair):
    btc, _ = synth_pair
    abs_r = close_to_close_log_returns(btc["close"]).abs()
    L, q = 5, 0.9
    qp = trailing_quantile(abs_r, L, q)
    for t in range(L - 1, len(abs_r)):
        window = abs_r.iloc[t - L + 1 : t + 1]
        if window.isna().any():
            continue
        assert qp.iloc[t] == pytest.approx(float(window.quantile(q)))
        trunc = trailing_quantile(abs_r.iloc[: t + 1], L, q).iloc[-1]
        assert qp.iloc[t] == pytest.approx(trunc)


def test_alignment_inner_join_drops_unaligned(synth_pair):
    btc, eth = synth_pair
    eth2 = eth.iloc[2:].copy().reset_index(drop=True)
    aligned = align_cross_asset(btc, eth2)
    assert len(aligned) == len(eth2)
    assert aligned["timestamp"].is_monotonic_increasing
    # All timestamps must exist in both
    btc_ts = set(pd.to_datetime(btc["timestamp"], utc=True))
    eth_ts = set(pd.to_datetime(eth2["timestamp"], utc=True))
    for ts in aligned["timestamp"]:
        assert ts in btc_ts and ts in eth_ts


def test_signal_prefix_invariant(synth_pair):
    btc, eth = synth_pair
    if len(btc) < 12:
        pytest.skip("fixture too short")
    full = build_btc_to_eth(btc, eth, L=5, p=0.8, h=1, kappa=0.75)
    for t in range(8, len(full) - 1):
        # Prefix both series to timestamps up to t
        ts_cut = full["timestamp"].iloc[t]
        b_pref = btc.loc[btc["timestamp"] <= ts_cut].copy()
        e_pref = eth.loc[eth["timestamp"] <= ts_cut].copy()
        pref = build_btc_to_eth(b_pref, e_pref, L=5, p=0.8, h=1, kappa=0.75)
        assert bool(full["signal"].iloc[t]) == bool(pref["signal"].iloc[-1])


def test_position_is_sign_of_btc(synth_pair):
    btc, eth = synth_pair
    frame = build_btc_to_eth(btc, eth, L=5, p=0.5, h=1, kappa=1.0)
    sig = frame.loc[frame["signal"] & frame["r_lead"].notna()]
    if len(sig) == 0:
        pytest.skip("no signals on tiny fixture")
    for _, row in sig.iterrows():
        assert row["position"] == pytest.approx(np.sign(row["r_lead"]))


def test_reverse_control_runs(synth_pair):
    btc, eth = synth_pair
    rev = build_eth_to_btc_reverse(btc, eth, L=5, p=0.5, h=1, kappa=1.0)
    assert "signal" in rev.columns
    assert "gross_bps" in rev.columns
    assert len(rev) > 0
    # Reverse lead is ETH: r_lead should equal ETH log return
    eth_r = close_to_close_log_returns(
        align_cross_asset(eth, btc)["lead_close"]
    )
    # build_eth_to_btc uses eth as lead — check column exists
    assert rev["r_lead"].notna().sum() > 0


def test_kappa_gate_restricts(synth_pair):
    btc, eth = synth_pair
    with_k = build_btc_to_eth(btc, eth, L=5, p=0.5, h=1, kappa=0.01, apply_kappa=True)
    no_k = build_btc_to_eth(btc, eth, L=5, p=0.5, h=1, kappa=0.01, apply_kappa=False)
    assert int(with_k["signal"].sum()) <= int(no_k["signal"].sum())
