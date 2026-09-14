"""Prove range / Q_p use only completed bars ending at t — no future leakage (EDGE-003)."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.signal_edge003 import (  # noqa: E402
    build_trade_frame,
    close_to_close_log_returns,
    compute_features,
    range_normalized,
    trailing_quantile,
)

FIXTURE = ROOT / "fixtures" / "tiny_synthetic_ohlcv.csv"


@pytest.fixture
def synth_df() -> pd.DataFrame:
    df = pd.read_csv(FIXTURE)
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
    return df


def test_range_definition(synth_df):
    rng = range_normalized(synth_df["high"], synth_df["low"], synth_df["close"])
    expected = (synth_df["high"] - synth_df["low"]) / synth_df["close"]
    assert rng.equals(expected) or np.allclose(rng, expected)


def test_log_return(synth_df):
    r = close_to_close_log_returns(synth_df["close"])
    assert np.isnan(r.iloc[0])
    for t in range(1, len(synth_df)):
        exp = np.log(synth_df["close"].iloc[t] / synth_df["close"].iloc[t - 1])
        assert r.iloc[t] == pytest.approx(exp)


def test_quantile_no_future_range(synth_df):
    rng = range_normalized(synth_df["high"], synth_df["low"], synth_df["close"])
    L, q = 5, 0.9
    qhi = trailing_quantile(rng, L, q)
    for t in range(len(rng)):
        if t < L - 1:
            continue
        window = rng.iloc[t - L + 1 : t + 1]
        if window.isna().any():
            continue
        expected = float(window.quantile(q))
        assert qhi.iloc[t] == pytest.approx(expected)
        trunc = rng.iloc[: t + 1]
        q_trunc = trailing_quantile(trunc, L, q).iloc[-1]
        assert qhi.iloc[t] == pytest.approx(q_trunc)


def test_prefix_invariance_features(synth_df):
    L, p = 5, 0.9
    full = compute_features(synth_df, L=L, p=p)
    for t in range(L + 2, len(synth_df)):
        prefix = compute_features(synth_df.iloc[: t + 1].copy(), L=L, p=p)
        for col in ("range", "Q_hi_trail", "Q_med_trail"):
            a = full[col].iloc[t]
            b = prefix[col].iloc[-1]
            if np.isnan(a) and np.isnan(b):
                continue
            assert a == pytest.approx(b), f"lookahead at t={t} col={col}"


def test_signal_prefix_invariant_not_label(synth_df):
    frame = build_trade_frame(synth_df, L=5, p=0.8, h=1, epsilon=1e-8)
    for t in range(8, len(synth_df) - 1):
        pref = build_trade_frame(
            synth_df.iloc[: t + 1].copy(), L=5, p=0.8, h=1, epsilon=1e-8
        )
        assert bool(frame["signal"].iloc[t]) == bool(pref["signal"].iloc[-1])


def test_position_is_fade(synth_df):
    frame = build_trade_frame(synth_df, L=5, p=0.5, h=1, epsilon=1e-12)
    sig = frame.loc[frame["signal"] & frame["r"].notna()]
    if len(sig) == 0:
        pytest.skip("no signals on tiny fixture at p=0.5")
    for _, row in sig.iterrows():
        assert row["position"] == pytest.approx(-np.sign(row["r"]))
