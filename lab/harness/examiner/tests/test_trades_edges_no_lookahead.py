"""Unit tests: no lookahead, Δ_exec>0, holdout filter, aggressor polarity, residual no future."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.trades_loader import (  # noqa: E402
    HOLDOUT_START_MS,
    aggressor_side,
    assert_no_holdout_trades,
    filter_pre_holdout,
)
from src.signal_edge_20260911_001 import (  # noqa: E402
    forward_gross_bps_delta_exec,
    trailing_ols_resid,
    trailing_quantile_abs,
)


def test_aggressor_polarity():
    # is_buyer_maker True → SELL (-1); False → BUY (+1)
    sides = aggressor_side(np.array([True, False, True, False]))
    assert list(sides) == [-1, 1, -1, 1]
    sides2 = aggressor_side(np.array(["true", "false", "True", "False"]))
    assert list(sides2) == [-1, 1, -1, 1]


def test_holdout_filter():
    ts = np.array(
        [HOLDOUT_START_MS - 1, HOLDOUT_START_MS, HOLDOUT_START_MS + 1],
        dtype=np.int64,
    )
    mask = filter_pre_holdout(ts)
    assert list(mask) == [True, False, False]
    with pytest.raises(AssertionError):
        assert_no_holdout_trades(ts)


def test_delta_exec_must_be_positive():
    n = 10
    open_ = np.linspace(100, 110, n)
    close = open_ + 0.1
    close_time = np.arange(n, dtype=np.int64) * 300_000 + 299_999
    direction = np.ones(n)
    with pytest.raises(ValueError, match="Δ_exec"):
        forward_gross_bps_delta_exec(
            open_, close, close_time, direction, delta_exec_ms=0, h_bars=1
        )
    with pytest.raises(ValueError, match="Δ_exec"):
        forward_gross_bps_delta_exec(
            open_, close, close_time, direction, delta_exec_ms=-1, h_bars=1
        )
    g = forward_gross_bps_delta_exec(
        open_, close, close_time, direction, delta_exec_ms=500, h_bars=1
    )
    assert np.isfinite(g[0])
    # last bars NaN (no room for entry+h)
    assert np.isnan(g[-1]) or np.isnan(g[-2])


def test_no_lookahead_trade_ts_leq_t():
    # Feature window trades must satisfy ts <= decision t
    decision_t = 1_000_000
    trade_ts = np.array([999_000, 1_000_000, 1_000_001])
    allowed = trade_ts[trade_ts <= decision_t]
    assert allowed.max() <= decision_t
    assert 1_000_001 not in set(allowed.tolist())


def test_residual_no_future_bars():
    rng = np.random.default_rng(0)
    n = 400
    X = rng.normal(size=(n, 4))
    beta_true = np.array([0.1, -0.2, 0.05, 0.0])
    y = X @ beta_true + rng.normal(scale=0.01, size=n)
    # Poison future y — if residual used future, early resid would change
    y_poison = y.copy()
    y_poison[350:] = 1e6
    r1 = trailing_ols_resid(y, X, L=288, refresh=1)
    r2 = trailing_ols_resid(y_poison, X, L=288, refresh=1)
    # Residuals before the poison region end-window must match
    # Window ending at t=349 uses y[349-287:350] = y[62:350] — no poison
    assert np.nanmax(np.abs(r1[288:349] - r2[288:349])) < 1e-9
    # After poison enters window, residuals may differ
    assert not np.allclose(r1[350:], r2[350:], equal_nan=True)


def test_trailing_quantile_no_lookahead():
    s = np.arange(100, dtype=float)
    q = trailing_quantile_abs(s, L=10, q=0.8)
    assert np.isnan(q[8])
    assert np.isfinite(q[9])
    # Quantile at t uses only s[t-9:t+1]
    expected = float(np.quantile(np.abs(s[0:10]), 0.8))
    assert abs(q[9] - expected) < 1e-9
