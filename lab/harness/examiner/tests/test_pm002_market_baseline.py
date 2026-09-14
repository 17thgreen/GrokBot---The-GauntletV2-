"""Unit tests for PM-002 market baseline Examiner guards."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.pm002_market_baseline import (  # noqa: E402
    FORBIDDEN_MT_FIELDS,
    PRIMARY_ASSETS,
    PRIMARY_REMS,
    ScoredRow,
    accept_mid_row,
    accept_poly_last_row,
    assert_no_pm001_price_as_mt,
    is_near_degenerate,
    primary_cell_id,
    score_cell,
)


def test_exclude_near_degenerate():
    assert is_near_degenerate(0.02) is True
    assert is_near_degenerate(0.01) is True
    assert is_near_degenerate(0.98) is True
    assert is_near_degenerate(0.99) is True
    assert is_near_degenerate(0.021) is False
    assert is_near_degenerate(0.979) is False
    assert is_near_degenerate(None) is True


def test_method_mid_only():
    good = {"implied_p_method": "mid", "implied_p": 0.55}
    bad_last = {"implied_p_method": "last", "implied_p": 0.55}
    bad_deg = {"implied_p_method": "mid", "implied_p": 0.01}
    assert accept_mid_row(good) is True
    assert accept_mid_row(bad_last) is False
    assert accept_mid_row(bad_deg) is False


def test_no_pm001_price_as_mt():
    # Checkpoint implied_p / quotes are allowed sources; terminal PM-001 prices are not.
    assert_no_pm001_price_as_mt(["implied_p", "yes_bid", "yes_ask"])
    with pytest.raises(AssertionError):
        assert_no_pm001_price_as_mt(["LAST_PRICE_DOLLARS"])
    with pytest.raises(AssertionError):
        assert_no_pm001_price_as_mt(["OUTCOME_PRICES", "implied_p"])
    # Labels may contain forbidden fields; using them as m_t source is the violation.
    label_fields = ["CONTRACT_ID", "RESOLUTION", "LAST_PRICE_DOLLARS", "OUTCOME_PRICES"]
    with pytest.raises(AssertionError):
        assert_no_pm001_price_as_mt(label_fields)
    for f in FORBIDDEN_MT_FIELDS:
        assert f in ("LAST_PRICE_DOLLARS", "OUTCOME_PRICES")


def test_six_cells_separate():
    ids = [primary_cell_id(a, rem) for rem in PRIMARY_REMS for a in PRIMARY_ASSETS]
    assert len(ids) == 6
    assert len(set(ids)) == 6
    # score separately — different rows must not pool
    rows_a = [
        ScoredRow(
            cell_id=ids[0],
            contract_id="A",
            venue="KALSHI",
            asset="BTC",
            window="15m",
            checkpoint="T-14m",
            time_remaining_sec=840,
            decision_time="2026-09-11T00:00:00Z",
            m_t=0.6,
            implied_p_method="mid",
            y=1,
            resolution="YES",
        )
    ]
    rows_b = [
        ScoredRow(
            cell_id=ids[1],
            contract_id="B",
            venue="KALSHI",
            asset="ETH",
            window="15m",
            checkpoint="T-14m",
            time_remaining_sec=840,
            decision_time="2026-09-11T00:00:00Z",
            m_t=0.4,
            implied_p_method="mid",
            y=0,
            resolution="NO",
        )
    ]
    sa = score_cell(rows_a)
    sb = score_cell(rows_b)
    assert sa["N"] == 1
    assert sb["N"] == 1
    assert sa["mean(m_t)"] != sb["mean(m_t)"]
    assert sa["Brier_model"] == "UNTESTED"
    assert sa["ΔBrier"] == "UNTESTED"
    assert sa["EV_gross"] == "UNTESTED"


def test_poly_never_as_mid():
    mid_poly = {
        "venue": "POLYMARKET_GLOBAL",
        "implied_p_method": "mid",
        "implied_p": 0.5,
        "time_remaining_sec": 300,
    }
    last_t0 = {
        "venue": "POLYMARKET_GLOBAL",
        "implied_p_method": "last",
        "implied_p": 0.5,
        "time_remaining_sec": 0,
    }
    last_ok = {
        "venue": "POLYMARKET_GLOBAL",
        "implied_p_method": "last",
        "implied_p": 0.5,
        "time_remaining_sec": 300,
    }
    assert accept_poly_last_row(mid_poly) is False
    assert accept_poly_last_row(last_t0) is False
    assert accept_poly_last_row(last_ok) is True


def test_untested_keys_always_present():
    s = score_cell([])
    for k in (
        "Brier_model",
        "LogLoss_model",
        "ΔBrier",
        "ΔLogLoss",
        "gap",
        "EV_gross",
        "EV_net",
        "abstention_rate",
        "cost_sensitivity",
    ):
        assert s[k] == "UNTESTED"
