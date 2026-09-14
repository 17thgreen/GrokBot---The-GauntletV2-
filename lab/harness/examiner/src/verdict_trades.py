"""Falsification gates for trade-flow edges EDGE-20260911-001/002."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

from .verdict import InstrumentVerdict


@dataclass
class TradeFlowVerdict:
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


def matches_or_beats(
    real_mean: Optional[float],
    control_mean: Optional[float],
    ci_low: Optional[float] = None,
    ci_high: Optional[float] = None,
) -> Optional[bool]:
    if real_mean is None or control_mean is None:
        return None
    if ci_low is not None and ci_high is not None:
        if ci_low <= control_mean <= ci_high:
            return True
    return bool(control_mean >= real_mean)


def evaluate_trade_flow(
    *,
    instrument: str,
    signal_count: int,
    distinct_utc_days: int,
    mean_gross_bps: Optional[float],
    net_1x: Optional[float],
    net_2x: Optional[float],
    net_3x: Optional[float],
    concentration_frac: Optional[float],
    ohlcv_redundant: Optional[bool],
    placebo_beats: Optional[bool],
    gates: dict[str, Any],
    extra_fail_reasons: Optional[list[str]] = None,
    validation_reached: bool = False,
    validation_net_1x: Optional[float] = None,
    cemetery: Optional[list[str]] = None,
) -> TradeFlowVerdict:
    """FAIL if net@1x<=0 OR OHLCV nested redundant OR placebo matches/beats.

    Also FAIL-INSUFFICIENT on min signals/days; concentration kill.
    """
    details: dict[str, Any] = {
        "signal_count": signal_count,
        "distinct_utc_days": distinct_utc_days,
        "mean_gross_bps": mean_gross_bps,
        "net_1x": net_1x,
        "net_2x": net_2x,
        "net_3x": net_3x,
        "concentration_frac": concentration_frac,
        "ohlcv_redundant": ohlcv_redundant,
        "placebo_beats": placebo_beats,
        "validation_reached": validation_reached,
        "validation_net_1x": validation_net_1x,
        "cemetery_citations": cemetery
        or ["CEM-20260910-001", "CEM-20260910-002", "CEM-20260910-003"],
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
        return TradeFlowVerdict(
            instrument=instrument,
            verdict="FAIL-INSUFFICIENT",
            reasons=reasons,
            details=details,
        )

    fail: list[str] = []
    if mean_gross_bps is None or mean_gross_bps <= 0:
        fail.append(f"mean gross <= 0 after Δ_exec (gross={mean_gross_bps})")
    if net_1x is None or net_1x <= 0:
        fail.append(f"net@1× <= 0 after Δ_exec (net_1x={net_1x})")
    if ohlcv_redundant is True:
        fail.append("REDUNDANT vs OHLCV-only nested control (matches/beats)")
    if placebo_beats is True:
        fail.append("placebo matches or beats primary within CI noise")
    conc_kill = float(gates.get("concentration_kill_frac", 0.05))
    if concentration_frac is not None and concentration_frac <= conc_kill:
        fail.append(
            f"effect concentrated: day_frac={concentration_frac} <= {conc_kill}"
        )
    if extra_fail_reasons:
        fail.extend(extra_fail_reasons)
    if validation_reached:
        if validation_net_1x is None or validation_net_1x <= 0:
            fail.append(f"VALIDATION net@1× <= 0 (net={validation_net_1x})")

    if fail:
        return TradeFlowVerdict(
            instrument=instrument, verdict="FAIL", reasons=fail, details=details
        )

    promising = (
        mean_gross_bps is not None
        and mean_gross_bps > 0
        and net_1x is not None
        and net_1x > 0
        and net_2x is not None
        and net_2x > 0
        and ohlcv_redundant is False
        and placebo_beats is False
        and (concentration_frac is None or concentration_frac > conc_kill)
    )
    if promising and validation_reached and validation_net_1x is not None and validation_net_1x > 0:
        return TradeFlowVerdict(
            instrument=instrument,
            verdict="VALIDATION_PASS",
            reasons=["RESEARCH+VALIDATION cleared trade-flow gates"],
            details=details,
        )
    if promising:
        return TradeFlowVerdict(
            instrument=instrument,
            verdict="WEAK",
            reasons=["RESEARCH cleared FAIL+2x; VALIDATION not confirmed or skipped"],
            details=details,
        )
    weak = []
    if net_2x is None or net_2x <= 0:
        weak.append(f"fails 2x cost stress (net_2x={net_2x})")
    if not weak:
        weak.append("passes FAIL gates but not full PROMISING criteria")
    return TradeFlowVerdict(
        instrument=instrument, verdict="WEAK", reasons=weak, details=details
    )
