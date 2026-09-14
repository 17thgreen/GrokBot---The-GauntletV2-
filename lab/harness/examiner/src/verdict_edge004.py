"""EDGE-20260910-004 falsification gates (cross-asset lead/lag).

FAIL RESEARCH primary if any:
1. Mean gross ETH sign-aligned forward <= 0
2. Net @1x <= 0
3. Reverse matches/beats within CI noise
4. Timestamp-shuffle matches/beats
5. Effect on <=5% of RESEARCH days
6. p-grid: <2/3 keep sign
7. VALIDATION (if reached): net@1x <= 0

No low-high gap CI requirement (unlike EDGE-001/003).
Cite CEM-20260910-001 / CEM-20260910-002 — NOT a rescue.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

from .verdict import InstrumentVerdict, aggregate_lab_verdict  # re-export


@dataclass
class Edge004Verdict:
    instrument: str
    verdict: str
    reasons: list[str] = field(default_factory=list)
    details: dict[str, Any] = field(default_factory=dict)

    def to_instrument_verdict(self) -> InstrumentVerdict:
        return InstrumentVerdict(
            instrument=self.instrument,
            verdict=self.verdict,
            reasons=list(self.reasons),
            details=dict(self.details),
        )


def evaluate_edge004(
    *,
    instrument: str = "BTC_ETH",
    signal_count: int,
    distinct_utc_days: int,
    mean_gross_bps: Optional[float],
    net_1x: Optional[float],
    net_2x: Optional[float],
    net_3x: Optional[float],
    concentration_frac: Optional[float],
    p_grid_keep_sign_count: int,
    p_grid_n: int = 3,
    reverse_matches_or_beats: Optional[bool],
    shuffle_matches_or_beats: Optional[bool],
    gates: dict[str, Any],
    validation_reached: bool = False,
    validation_net_1x: Optional[float] = None,
    research_only: bool = False,
) -> Edge004Verdict:
    """Apply EDGE-004 card falsification. Inputs must be code-measured or None."""
    details: dict[str, Any] = {
        "signal_count": signal_count,
        "distinct_utc_days": distinct_utc_days,
        "mean_gross_bps": mean_gross_bps,
        "net_1x": net_1x,
        "net_2x": net_2x,
        "net_3x": net_3x,
        "concentration_frac": concentration_frac,
        "p_grid_keep_sign_count": p_grid_keep_sign_count,
        "reverse_matches_or_beats": reverse_matches_or_beats,
        "shuffle_matches_or_beats": shuffle_matches_or_beats,
        "validation_reached": validation_reached,
        "validation_net_1x": validation_net_1x,
        "research_only": research_only,
        "cemetery_citations": ["CEM-20260910-001", "CEM-20260910-002"],
    }

    min_sig = int(gates.get("research_signals", 200))
    min_days = int(gates.get("research_distinct_utc_days", 20))
    if signal_count < min_sig or distinct_utc_days < min_days:
        reasons = []
        if signal_count < min_sig:
            reasons.append(f"RESEARCH signals {signal_count} < min {min_sig}")
        if distinct_utc_days < min_days:
            reasons.append(
                f"RESEARCH distinct days {distinct_utc_days} < min {min_days}"
            )
        return Edge004Verdict(
            instrument=instrument,
            verdict="FAIL-INSUFFICIENT",
            reasons=reasons,
            details=details,
        )

    fail_reasons: list[str] = []

    # 1. Mean gross <= 0
    if mean_gross_bps is None or mean_gross_bps <= 0:
        fail_reasons.append(
            f"mean gross ETH sign-aligned forward <= 0 (gross={mean_gross_bps})"
        )

    # 2. Net @1x <= 0
    if net_1x is None or net_1x <= 0:
        fail_reasons.append(f"net @1x C_base <= 0 (net_1x={net_1x})")

    # 3. Reverse matches/beats
    if reverse_matches_or_beats is True:
        fail_reasons.append(
            "reverse ETH→BTC matches or beats BTC→ETH within CI noise"
        )

    # 4. Timestamp shuffle matches/beats
    if shuffle_matches_or_beats is True:
        fail_reasons.append(
            "timestamp-shuffle placebo matches or beats BTC→ETH within CI noise"
        )

    # 5. Concentration <= 5% of days
    conc_kill = float(gates.get("concentration_kill_frac", 0.05))
    if concentration_frac is not None and concentration_frac <= conc_kill:
        fail_reasons.append(
            f"effect on <=5% of RESEARCH days (day_frac={concentration_frac})"
        )

    # 6. p-grid <2/3 keep sign
    min_keep = int(gates.get("grid_p_stability_min_keep_sign", 2))
    # also accept fraction: need keep >= ceil(2/3 * n) ≈ 2 for n=3
    need = max(min_keep, int((2 * p_grid_n + 2) // 3))  # ceil(2n/3)
    if p_grid_keep_sign_count < need:
        fail_reasons.append(
            f"p-grid: {p_grid_keep_sign_count}/{p_grid_n} keep sign (<2/3)"
        )

    # 7. VALIDATION net@1x <= 0 if reached
    if validation_reached and not research_only:
        if validation_net_1x is None or validation_net_1x <= 0:
            fail_reasons.append(
                f"VALIDATION net@1x <= 0 (net={validation_net_1x})"
            )

    if fail_reasons:
        return Edge004Verdict(
            instrument=instrument,
            verdict="FAIL",
            reasons=fail_reasons,
            details=details,
        )

    # Survived FAIL gates — grade strength
    promising = (
        mean_gross_bps is not None
        and mean_gross_bps > 0
        and net_1x is not None
        and net_1x > 0
        and net_2x is not None
        and net_2x > 0
        and p_grid_keep_sign_count >= need
        and reverse_matches_or_beats is False
        and shuffle_matches_or_beats is False
        and (concentration_frac is None or concentration_frac > conc_kill)
    )

    if promising and validation_reached and validation_net_1x is not None and validation_net_1x > 0:
        return Edge004Verdict(
            instrument=instrument,
            verdict="VALIDATION_PASS",
            reasons=["RESEARCH + VALIDATION pass provisional EDGE-004 gates"],
            details=details,
        )

    if promising and (research_only or not validation_reached):
        return Edge004Verdict(
            instrument=instrument,
            verdict="WEAK",
            reasons=[
                "RESEARCH cleared FAIL gates and 2x stress; VALIDATION not confirmed"
            ],
            details=details,
        )

    weak_reasons: list[str] = []
    if net_2x is None or net_2x <= 0:
        weak_reasons.append(f"fails 2x cost stress (net_2x={net_2x})")
    if not weak_reasons:
        weak_reasons.append("passes FAIL gates but not full PROMISING criteria")
    return Edge004Verdict(
        instrument=instrument,
        verdict="WEAK",
        reasons=weak_reasons,
        details=details,
    )


def matches_or_beats_within_ci(
    real_mean: Optional[float],
    control_mean: Optional[float],
    ci_low: Optional[float],
    ci_high: Optional[float],
) -> Optional[bool]:
    """True if control matches (inside real CI) or beats (control >= real)."""
    if real_mean is None or control_mean is None:
        return None
    if ci_low is not None and ci_high is not None:
        if ci_low <= control_mean <= ci_high:
            return True
    return bool(control_mean >= real_mean)
