"""Falsification gates for Cycle-5 Catalyst edges 004/005/006."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

from .verdict_trades import matches_or_beats


@dataclass
class CatalystVerdict:
    instrument: str
    verdict: str
    reasons: list[str] = field(default_factory=list)
    details: dict[str, Any] = field(default_factory=dict)


def evaluate_catalyst(
    *,
    instrument: str,
    signal_count: int,
    distinct_utc_days: int,
    mean_gross_bps: Optional[float],
    net_1x: Optional[float],
    net_2x: Optional[float],
    net_3x: Optional[float],
    concentration_frac: Optional[float],
    nested_beats: dict[str, Optional[bool]],
    extra_fail_reasons: Optional[list[str]] = None,
    gates: Optional[dict[str, Any]] = None,
    validation_reached: bool = False,
    validation_net_1x: Optional[float] = None,
    cemetery: Optional[list[str]] = None,
) -> CatalystVerdict:
    gates = gates or {
        "research_signals": 30,
        "research_distinct_utc_days": 10,
        "validation_signals": 15,
        "concentration_kill_frac": 0.05,
    }
    details: dict[str, Any] = {
        "signal_count": signal_count,
        "distinct_utc_days": distinct_utc_days,
        "mean_gross_bps": mean_gross_bps,
        "net_1x": net_1x,
        "net_2x": net_2x,
        "net_3x": net_3x,
        "concentration_frac": concentration_frac,
        "nested_beats": nested_beats,
        "validation_reached": validation_reached,
        "validation_net_1x": validation_net_1x,
        "cemetery_citations": cemetery
        or [
            "CEM-20260911-001",
            "CEM-20260911-002",
            "CEM-20260910-001",
            "CEM-20260910-002",
            "CEM-20260910-003",
        ],
    }
    min_sig = int(gates["research_signals"])
    min_days = int(gates["research_distinct_utc_days"])
    if signal_count < min_sig or distinct_utc_days < min_days:
        reasons = []
        if signal_count < min_sig:
            reasons.append(f"RESEARCH signals {signal_count} < min {min_sig}")
        if distinct_utc_days < min_days:
            reasons.append(f"RESEARCH distinct days {distinct_utc_days} < min {min_days}")
        return CatalystVerdict(instrument, "FAIL-INSUFFICIENT", reasons, details)

    fail: list[str] = []
    if mean_gross_bps is None or mean_gross_bps <= 0:
        fail.append(f"mean gross <= 0 (gross={mean_gross_bps})")
    if net_1x is None or net_1x <= 0:
        fail.append(f"net@1× <= 0 (net_1x={net_1x})")
    for name, flag in nested_beats.items():
        if flag is True:
            fail.append(f"REDUNDANT / control beats: {name}")
    conc_kill = float(gates["concentration_kill_frac"])
    if concentration_frac is not None and concentration_frac <= conc_kill:
        fail.append(f"effect concentrated: day_frac={concentration_frac} <= {conc_kill}")
    if extra_fail_reasons:
        fail.extend(extra_fail_reasons)
    if validation_reached:
        if validation_net_1x is None or validation_net_1x <= 0:
            fail.append(f"VALIDATION net@1× <= 0 (net={validation_net_1x})")
    if fail:
        return CatalystVerdict(instrument, "FAIL", fail, details)

    promising = (
        mean_gross_bps is not None
        and mean_gross_bps > 0
        and net_1x is not None
        and net_1x > 0
        and net_2x is not None
        and net_2x > 0
        and all(v is False for v in nested_beats.values() if v is not None)
        and (concentration_frac is None or concentration_frac > conc_kill)
    )
    if promising and validation_reached and validation_net_1x is not None and validation_net_1x > 0:
        return CatalystVerdict(
            instrument, "VALIDATION_PASS", ["RESEARCH+VALIDATION cleared"], details
        )
    if promising:
        return CatalystVerdict(
            instrument,
            "WEAK",
            ["RESEARCH cleared FAIL+2x; VALIDATION not confirmed or skipped"],
            details,
        )
    weak = []
    if net_2x is None or net_2x <= 0:
        weak.append(f"fails 2x cost stress (net_2x={net_2x})")
    if not weak:
        weak.append("passes FAIL gates but not full PROMISING criteria")
    return CatalystVerdict(instrument, "WEAK", weak, details)


def aggregate_btc_eth(
    btc: CatalystVerdict,
    eth: CatalystVerdict,
    *,
    btc_gross: Optional[float],
    eth_gross: Optional[float],
) -> tuple[str, list[str]]:
    """Lab aggregate; kill if BTC/ETH disagree on gross sign when both measured."""
    reasons: list[str] = []
    if (
        btc_gross is not None
        and eth_gross is not None
        and btc_gross != 0
        and eth_gross != 0
        and (btc_gross > 0) != (eth_gross > 0)
    ):
        reasons.append(
            f"BTC/ETH disagree on gross sign (BTC={btc_gross}, ETH={eth_gross})"
        )
    ranks = {
        "FAIL-INSUFFICIENT": 0,
        "FAIL": 1,
        "WEAK": 2,
        "PROMISING": 3,
        "VALIDATION_PASS": 4,
    }
    worst = btc if ranks.get(btc.verdict, -1) <= ranks.get(eth.verdict, -1) else eth
    if reasons:
        return "FAIL", reasons + list(worst.reasons)
    if btc.verdict.startswith("FAIL") or eth.verdict.startswith("FAIL"):
        all_r = [f"BTC:{btc.verdict}"] + btc.reasons + [f"ETH:{eth.verdict}"] + eth.reasons
        verdict = (
            "FAIL-INSUFFICIENT"
            if "INSUFFICIENT" in btc.verdict or "INSUFFICIENT" in eth.verdict
            else "FAIL"
        )
        return verdict, all_r
    if btc.verdict == "VALIDATION_PASS" and eth.verdict == "VALIDATION_PASS":
        return "VALIDATION_PASS", ["BTC and ETH VALIDATION_PASS"]
    return worst.verdict, list(worst.reasons) + [
        f"BTC={btc.verdict}",
        f"ETH={eth.verdict}",
    ]


__all__ = [
    "CatalystVerdict",
    "evaluate_catalyst",
    "aggregate_btc_eth",
    "matches_or_beats",
]
