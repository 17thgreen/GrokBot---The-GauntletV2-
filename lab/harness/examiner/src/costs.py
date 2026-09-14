"""Provisional cost stack [A] for PROV-MEAS-20260910-001.

C_base = fees 4 + spread 2 + slip 1 = 7.0 bps round-trip [A]
Stress: 1x=7, 2x=14, 3x=21; gross C=0 diagnostic only
Latency stress: +1 and +3 bp added to 1x C — LATENCY_STRESS_[A]
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class CostAssumption:
    fees_rt: float = 4.0
    spread_rt: float = 2.0
    slippage_rt: float = 1.0
    tag: str = "[A]"

    @property
    def C_base(self) -> float:
        return self.fees_rt + self.spread_rt + self.slippage_rt


DEFAULT_COSTS = CostAssumption()


def net_bps(gross_bps: float, C: float) -> float:
    return gross_bps - C


def stress_schedule(C_base: float = 7.0) -> dict[str, float]:
    """Locked cost stress rows. Keys are labels for reports."""
    return {
        "GROSS_C0_DIAGNOSTIC": 0.0,  # never a promotion input
        "C_1x": C_base * 1.0,
        "C_2x": C_base * 2.0,
        "C_3x": C_base * 3.0,
        "LATENCY_STRESS_+1bp_[A]": C_base * 1.0 + 1.0,
        "LATENCY_STRESS_+3bp_[A]": C_base * 1.0 + 3.0,
    }


def apply_costs(gross_series, C: float):
    """Element-wise net = gross - C (bps)."""
    return gross_series - C


def promotion_cost_keys() -> tuple[str, ...]:
    """Cost keys eligible for FAIL/PROMISING gates (excludes gross diagnostic)."""
    return ("C_1x", "C_2x", "C_3x")
