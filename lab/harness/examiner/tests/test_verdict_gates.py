"""Verdict gate logic per package §8."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.verdict import aggregate_lab_verdict, evaluate_instrument, InstrumentVerdict  # noqa: E402

GATES = {
    "research_signals": 200,
    "validation_signals": 50,
    "holdout_signals": 50,
    "research_distinct_utc_days": 20,
    "concentration_kill_frac": 0.05,
}


def _research(sc=250, days=25, **kwargs):
    base = {"signal_count": sc, "distinct_utc_days": days}
    base.update(kwargs)
    return base


def test_fail_insufficient():
    iv = evaluate_instrument(
        instrument="BTC",
        research=_research(sc=10, days=2),
        validation=None,
        gates=GATES,
        grid_w_pass=True,
        qlo_cliff=False,
        placebo_beats=False,
        concentration_frac=0.5,
        net_1x=1.0,
        net_2x=0.5,
        net_3x=-1.0,
        gap_ci_excludes_zero_research=True,
    )
    assert iv.verdict == "FAIL-INSUFFICIENT"


def test_fail_net_nonpositive():
    iv = evaluate_instrument(
        instrument="BTC",
        research=_research(),
        validation={"signal_count": 60},
        gates=GATES,
        grid_w_pass=True,
        qlo_cliff=False,
        placebo_beats=False,
        concentration_frac=0.4,
        net_1x=-0.1,
        net_2x=-1.0,
        net_3x=-2.0,
        gap_ci_excludes_zero_research=True,
        validation_net_1x=1.0,
        validation_gap_ci_excludes_zero=True,
        validation_signal_count=60,
    )
    assert iv.verdict == "FAIL"


def test_fail_concentration():
    iv = evaluate_instrument(
        instrument="ETH",
        research=_research(),
        validation={"signal_count": 60},
        gates=GATES,
        grid_w_pass=True,
        qlo_cliff=False,
        placebo_beats=False,
        concentration_frac=0.01,
        net_1x=2.0,
        net_2x=1.0,
        net_3x=0.1,
        gap_ci_excludes_zero_research=True,
        validation_net_1x=1.0,
        validation_gap_ci_excludes_zero=True,
        validation_signal_count=60,
    )
    assert iv.verdict == "FAIL"
    assert any("concentrated" in r for r in iv.reasons)


def test_validation_pass():
    iv = evaluate_instrument(
        instrument="BTC",
        research=_research(),
        validation={"signal_count": 80},
        gates=GATES,
        grid_w_pass=True,
        qlo_cliff=False,
        placebo_beats=False,
        concentration_frac=0.3,
        net_1x=3.0,
        net_2x=1.5,
        net_3x=-0.5,  # 3x fail alone → still ok for VALIDATION_PASS per §8.3
        gap_ci_excludes_zero_research=True,
        validation_net_1x=1.2,
        validation_gap_ci_excludes_zero=True,
        validation_signal_count=80,
    )
    assert iv.verdict == "VALIDATION_PASS"


def test_aggregate_worst_wins():
    a = InstrumentVerdict("BTC", "VALIDATION_PASS")
    b = InstrumentVerdict("ETH", "FAIL")
    assert aggregate_lab_verdict([a, b]) == "FAIL"


def test_untested_aggregate_empty():
    assert aggregate_lab_verdict([]) == "UNTESTED"
