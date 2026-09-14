"""Prove RV / Q_lo use only completed bars ending at t — no future leakage."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.signal_edge001 import (  # noqa: E402
    build_trade_frame,
    close_to_close_returns,
    compute_features,
    realized_vol,
    trailing_quantile,
)

FIXTURE = ROOT / "fixtures" / "tiny_synthetic_ohlcv.csv"


@pytest.fixture
def synth_df() -> pd.DataFrame:
    df = pd.read_csv(FIXTURE)
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
    return df


def test_fixture_labeled_synthetic():
    label = (ROOT / "fixtures" / "README_FIXTURES.md").read_text()
    assert "SYNTHETIC" in label
    assert "NEVER" in label


def test_rv_matches_manual_window(synth_df):
    r = close_to_close_returns(synth_df["close"])
    W = 3
    rv = realized_vol(r, W)
    # At index t, RV = r[t-W+1]^2 + ... + r[t]^2
    for t in range(W, len(r)):  # need W returns; r[0] is NaN so start later
        window = r.iloc[t - W + 1 : t + 1]
        if window.isna().any():
            assert np.isnan(rv.iloc[t]) or rv.isna().iloc[t]
            continue
        expected = float((window**2).sum())
        assert rv.iloc[t] == pytest.approx(expected)


def test_quantile_no_future(synth_df):
    r = close_to_close_returns(synth_df["close"])
    W, L, q = 3, 5, 0.4
    rv = realized_vol(r, W)
    qlo = trailing_quantile(rv, L, q)
    for t in range(len(rv)):
        if t < L - 1 or rv.iloc[t - L + 1 : t + 1].isna().any():
            continue
        window = rv.iloc[t - L + 1 : t + 1]
        expected = float(window.quantile(q))
        assert qlo.iloc[t] == pytest.approx(expected)
        # Future bars must not affect: recompute with truncated series
        trunc = rv.iloc[: t + 1]
        q_trunc = trailing_quantile(trunc, L, q).iloc[-1]
        assert qlo.iloc[t] == pytest.approx(q_trunc)


def test_prefix_invariance_features(synth_df):
    """Features at t computed on full series == features at t on series[:t+1]."""
    W, L, Q_lo = 3, 5, 0.33
    full = compute_features(synth_df, W=W, L=L, Q_lo=Q_lo)
    for t in range(L + W, len(synth_df)):
        prefix = compute_features(synth_df.iloc[: t + 1].copy(), W=W, L=L, Q_lo=Q_lo)
        for col in ("RV", "Q_lo_trail"):
            a = full[col].iloc[t]
            b = prefix[col].iloc[-1]
            if np.isnan(a) and np.isnan(b):
                continue
            assert a == pytest.approx(b), f"lookahead at t={t} col={col}"


def test_forward_return_uses_future_only_for_label(synth_df):
    """gross_bps at t may use close[t+h] (label), but signal must not."""
    frame = build_trade_frame(synth_df, W=3, L=5, Q_lo=0.4, h=1, epsilon=1e-8)
    # Signal columns must be prefix-invariant
    for t in range(8, len(synth_df) - 1):
        pref = build_trade_frame(
            synth_df.iloc[: t + 1].copy(), W=3, L=5, Q_lo=0.4, h=1, epsilon=1e-8
        )
        assert bool(frame["signal"].iloc[t]) == bool(pref["signal"].iloc[-1])
