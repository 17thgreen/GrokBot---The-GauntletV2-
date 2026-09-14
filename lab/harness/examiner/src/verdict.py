"""Provisional verdict logic per PROV-MEAS package §8.

FAIL / WEAK / PROMISING / VALIDATION_PASS / FAIL-INSUFFICIENT / UNTESTED
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional


VERDICTS = (
    "UNTESTED",
    "FAIL-INSUFFICIENT",
    "FAIL",
    "WEAK",
    "PROMISING",
    "VALIDATION_PASS",
)


@dataclass
class InstrumentVerdict:
    instrument: str
    verdict: str
    reasons: list[str] = field(default_factory=list)
    details: dict[str, Any] = field(default_factory=dict)


def _met_research_mins(research: dict[str, Any], gates: dict[str, Any]) -> tuple[bool, list[str]]:
    reasons = []
    sc = research.get("signal_count", 0) or 0
    days = research.get("distinct_utc_days", 0) or 0
    if sc < gates["research_signals"]:
        reasons.append(
            f"RESEARCH signals {sc} < min {gates['research_signals']}"
        )
    if days < gates["research_distinct_utc_days"]:
        reasons.append(
            f"RESEARCH distinct days {days} < min {gates['research_distinct_utc_days']}"
        )
    return (len(reasons) == 0, reasons)


def evaluate_instrument(
    *,
    instrument: str,
    research: dict[str, Any],
    validation: Optional[dict[str, Any]],
    gates: dict[str, Any],
    grid_w_pass: bool,
    qlo_cliff: bool,
    placebo_beats: bool,
    concentration_frac: Optional[float],
    net_1x: Optional[float],
    net_2x: Optional[float],
    net_3x: Optional[float],
    gap_ci_excludes_zero_research: Optional[bool],
    validation_net_1x: Optional[float] = None,
    validation_gap_ci_excludes_zero: Optional[bool] = None,
    validation_signal_count: int = 0,
    research_only: bool = False,
) -> InstrumentVerdict:
    """Apply §8 gates. All inputs must come from executed metrics (or None)."""
    reasons: list[str] = []
    details: dict[str, Any] = {
        "research": research,
        "validation": validation,
        "grid_w_pass": grid_w_pass,
        "qlo_cliff": qlo_cliff,
        "placebo_beats": placebo_beats,
        "concentration_frac": concentration_frac,
        "net_1x": net_1x,
        "net_2x": net_2x,
        "net_3x": net_3x,
    }

    ok_mins, min_reasons = _met_research_mins(research, gates)
    if not ok_mins:
        return InstrumentVerdict(
            instrument=instrument,
            verdict="FAIL-INSUFFICIENT",
            reasons=min_reasons,
            details=details,
        )

    # FAIL checks (§8.1)
    fail_reasons: list[str] = []
    if net_1x is None or net_1x <= 0:
        fail_reasons.append(f"primary net at 1x <= 0 on RESEARCH (net_1x={net_1x})")
    if gap_ci_excludes_zero_research is False or gap_ci_excludes_zero_research is None:
        fail_reasons.append("low-high RV gap CI covers 0 (or undefined) on RESEARCH")
    conc_kill = gates.get("concentration_kill_frac", 0.05)
    if concentration_frac is not None and concentration_frac <= conc_kill:
        fail_reasons.append(
            f"effect concentrated: day_frac={concentration_frac} <= {conc_kill}"
        )
    if not grid_w_pass:
        fail_reasons.append("parameter grid: fewer than 2/3 W keep gap sign")
    if placebo_beats:
        fail_reasons.append("placebo matches or beats real gap within CI noise")

    # Validation fail if reached
    validation_reached = (
        not research_only
        and validation is not None
        and validation_signal_count >= gates.get("validation_signals", 50)
    )
    if validation_reached:
        if validation_net_1x is None or validation_net_1x <= 0:
            fail_reasons.append(
                f"VALIDATION net at 1x <= 0 (net={validation_net_1x})"
            )
        if (
            validation_gap_ci_excludes_zero is False
            or validation_gap_ci_excludes_zero is None
        ):
            fail_reasons.append("VALIDATION gap CI covers 0 (or undefined)")

    if fail_reasons:
        return InstrumentVerdict(
            instrument=instrument,
            verdict="FAIL",
            reasons=fail_reasons,
            details=details,
        )

    # PROMISING criteria (§8.3) — need 2x also
    promising_ok = (
        net_1x is not None
        and net_1x > 0
        and net_2x is not None
        and net_2x > 0
        and gap_ci_excludes_zero_research is True
        and grid_w_pass
        and not qlo_cliff
        and not placebo_beats
        and (concentration_frac is None or concentration_frac > conc_kill)
    )

    validation_pass_ok = False
    if promising_ok and validation_reached:
        validation_pass_ok = (
            validation_net_1x is not None
            and validation_net_1x > 0
            and validation_gap_ci_excludes_zero is True
        )

    if validation_pass_ok:
        return InstrumentVerdict(
            instrument=instrument,
            verdict="VALIDATION_PASS",
            reasons=["PROMISING + VALIDATION slice pass (provisional ceiling)"],
            details=details,
        )

    if promising_ok and not validation_reached:
        # RESEARCH promising but validation not confirmed
        if research_only:
            reasons.append("CONDITIONAL research-only; VALIDATION not evaluated")
        else:
            reasons.append("RESEARCH PROMISING gates met; VALIDATION incomplete or skipped")
        # Still need validation for full PROMISING per §8.3.7 — without it → WEAK/PROMISING borderline
        # Spec: PROMISING requires VALIDATION net>0 and gap CI excludes 0.
        # So without validation → cannot award PROMISING; award WEAK with note.
        return InstrumentVerdict(
            instrument=instrument,
            verdict="WEAK",
            reasons=reasons
            + ["PROMISING requires VALIDATION confirmation per §8.3.7"],
            details=details,
        )

    if promising_ok and validation_reached and not validation_pass_ok:
        return InstrumentVerdict(
            instrument=instrument,
            verdict="WEAK",
            reasons=["RESEARCH strong but VALIDATION did not confirm"],
            details=details,
        )

    # WEAK: passes FAIL gates on gross / optimistic; fails 2x; fragile (§8.2)
    weak_reasons: list[str] = []
    if net_2x is None or net_2x <= 0:
        weak_reasons.append(f"fails 2x cost stress (net_2x={net_2x})")
    if net_3x is not None and net_3x <= 0:
        weak_reasons.append("fails 3x stress → WEAK not FAIL if 1x/2x hold")
    if qlo_cliff:
        weak_reasons.append("Q_lo single-point cliff flag")
    if not weak_reasons:
        weak_reasons.append("passes FAIL gates but not full PROMISING criteria")

    return InstrumentVerdict(
        instrument=instrument,
        verdict="WEAK",
        reasons=weak_reasons,
        details=details,
    )


def aggregate_lab_verdict(per_instrument: list[InstrumentVerdict]) -> str:
    """Side-by-side aggregate: worst non-UNTESTED drives headline; empty → UNTESTED."""
    if not per_instrument:
        return "UNTESTED"
    order = {
        "FAIL": 0,
        "FAIL-INSUFFICIENT": 1,
        "WEAK": 2,
        "PROMISING": 3,
        "VALIDATION_PASS": 4,
        "UNTESTED": 5,
    }
    # Headline = min rank among instruments (most severe)
    return min(per_instrument, key=lambda v: order.get(v.verdict, 99)).verdict
