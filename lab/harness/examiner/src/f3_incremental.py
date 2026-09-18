"""F3 incremental forecast maps vs MKT-KALSHI-15M-MID.

Frozen no-fit maps for FEAT-20260912-003 (spread shrink) and
FEAT-20260912-004 (last−mid). No MLE. No ensemble. No trading.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass
from typing import Any, Optional, Sequence

from .pm002_market_baseline import (
    LOGLOSS_EPS,
    MIN_N_FOR_ECE,
    MIN_POWERED_BINS_FOR_CAL,
    brier_score,
    cell_underpowered_for_calibration,
    descriptive_wr,
    expected_calibration_error,
    log_loss,
    reliability_table,
)

# Frozen headline parameters (immutable; not fit on PM-003).
FEAT003_S0 = 0.05
FEAT004_KAPPA = 1.0
FEAT004_EPS = 1e-4

# Robustness annex only — not headline, no post-hoc switch.
FEAT003_S0_ROBUST = (0.02, 0.10)
FEAT004_KAPPA_ROBUST = (0.5, 2.0)
PLACEBO_SEED = 20260912

PRIMARY_CELL = "KALSHI|15m|BTC|T-5m|mid"
ANNEX_CELLS = (
    "KALSHI|15m|BTC|T-14m|mid",
    "KALSHI|15m|ETH|T-14m|mid",
    "KALSHI|15m|BTC|T-10m|mid",
    "KALSHI|15m|ETH|T-10m|mid",
    "KALSHI|15m|ETH|T-5m|mid",
)
ALL_CELLS = (PRIMARY_CELL,) + ANNEX_CELLS

CELL_SEED_OFFSET = {
    "KALSHI|15m|BTC|T-5m|mid": 1,
    "KALSHI|15m|BTC|T-14m|mid": 2,
    "KALSHI|15m|ETH|T-14m|mid": 3,
    "KALSHI|15m|BTC|T-10m|mid": 4,
    "KALSHI|15m|ETH|T-10m|mid": 5,
    "KALSHI|15m|ETH|T-5m|mid": 6,
}


def _clip(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, float(x)))


def feat003_p(m_t: float, s_t: float, s0: float = FEAT003_S0) -> float:
    """p_t = (1-λ) m_t + λ·0.5, λ = clip(s_t / s0, 0, 1)."""
    if s0 <= 0:
        raise ValueError("s0 must be positive")
    lam = _clip(s_t / s0, 0.0, 1.0)
    return (1.0 - lam) * m_t + lam * 0.5


def feat004_p(
    m_t: float,
    delta_t: float,
    kappa: float = FEAT004_KAPPA,
    eps: float = FEAT004_EPS,
) -> float:
    """p_t = clip(m_t + κ·δ_t, ε, 1-ε)."""
    return _clip(m_t + kappa * delta_t, eps, 1.0 - eps)


@dataclass(frozen=True)
class FeatRow:
    cell_id: str
    contract_id: str
    asset: str
    checkpoint: str
    time_remaining_sec: int
    decision_time: str
    m_t: float
    y: int
    yes_bid: float
    yes_ask: float
    last: Optional[float]
    s_t: float
    delta_t: Optional[float]


def incremental_verdict(d_brier: float, d_logloss: float) -> dict[str, str]:
    """Skill requires both Δ < 0. Otherwise REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)."""
    if d_brier < 0.0 and d_logloss < 0.0:
        return {
            "verdict": "INCREMENTAL_RESEARCH",
            "reason": (
                "both ΔBrier<0 and ΔLogLoss<0 vs mid-only on USED_RESEARCH; "
                "not validation; not sealed holdout; not trading"
            ),
        }
    if d_brier >= 0.0 and d_logloss >= 0.0:
        return {
            "verdict": "REDUNDANT / FAIL-INSUFFICIENT",
            "reason": (
                "ΔBrier≥0 and ΔLogLoss≥0 vs mid-only on primary/cell; "
                "REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)"
            ),
        }
    return {
        "verdict": "REDUNDANT / FAIL-INSUFFICIENT",
        "reason": (
            "does not improve both Brier and LogLoss vs mid-only "
            f"(ΔBrier={d_brier:.8f}, ΔLogLoss={d_logloss:.8f}); "
            "REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)"
        ),
    }


def score_forecast(
    rows: Sequence[FeatRow],
    p: Sequence[float],
    *,
    feature_id: str,
    map_label: str,
) -> dict[str, Any]:
    """Required incrementality metrics + BINARY_EXAMINER keys (UNTESTED if unused)."""
    n = len(rows)
    if n == 0:
        return {
            "feature_id": feature_id,
            "map": map_label,
            "N": 0,
            "N_unit": "scored decision-events (checkpoint × contract after filters)",
            "Brier_model": "UNTESTED",
            "Brier_market": "UNTESTED",
            "ΔBrier": "UNTESTED",
            "LogLoss_model": "UNTESTED",
            "LogLoss_market": "UNTESTED",
            "ΔLogLoss": "UNTESTED",
            "mean(m_t)": "UNTESTED",
            "mean(p_t)": "UNTESTED",
            "abstention": "none",
            "abstention_rate": 0.0,
            "ECE": "UNTESTED",
            "WR": "UNTESTED",
            "CI": "UNTESTED",
            "gap": "UNTESTED",
            "EV_gross": "UNTESTED",
            "EV_net": "UNTESTED",
            "cost_sensitivity": "UNTESTED",
            "cell_verdict": "FAIL-INSUFFICIENT",
            "cell_reason": "N=0",
        }

    m = [r.m_t for r in rows]
    y = [r.y for r in rows]
    p_list = [float(pi) for pi in p]
    if len(p_list) != n:
        raise ValueError("p length must match rows")

    brier_m = brier_score(m, y)
    brier_p = brier_score(p_list, y)
    ll_m = log_loss(m, y)
    ll_p = log_loss(p_list, y)
    assert brier_m is not None and brier_p is not None
    assert ll_m is not None and ll_p is not None
    d_brier = float(brier_p - brier_m)
    d_ll = float(ll_p - ll_m)
    mean_m = float(sum(m) / n)
    mean_p = float(sum(p_list) / n)
    mean_gap = float(sum(pi - mi for pi, mi in zip(p_list, m)) / n)
    mean_abs_gap = float(sum(abs(pi - mi) for pi, mi in zip(p_list, m)) / n)

    wr_block = descriptive_wr(p_list, y)
    rel = reliability_table(p_list, y)
    ece = expected_calibration_error(p_list, y)
    underpowered = cell_underpowered_for_calibration(rel, n)
    if underpowered:
        ece_out: Any = "UNTESTED"
        ece_note = (
            f"ECE UNTESTED: thin bins / underpowered "
            f"(N={n}, powered_bins={rel.get('powered_bin_count', 0)}; "
            f"need ≥{MIN_POWERED_BINS_FOR_CAL} bins n≥20 and/or N≥{MIN_N_FOR_ECE})"
        )
    else:
        ece_out = ece
        ece_note = "powered bins present; ECE on p_t"

    v = incremental_verdict(d_brier, d_ll)
    contracts = sorted({r.contract_id for r in rows})
    days = sorted({r.decision_time[:10] for r in rows if r.decision_time})
    s_vals = [r.s_t for r in rows]
    d_vals = [r.delta_t for r in rows if r.delta_t is not None]

    return {
        "feature_id": feature_id,
        "map": map_label,
        "N": n,
        "N_unit": "scored decision-events (checkpoint × contract after filters)",
        "contract_count": len(contracts),
        "distinct_utc_days": len(days),
        "span_utc": {"min": min(days) if days else None, "max": max(days) if days else None},
        "Brier_model": float(brier_p),
        "Brier_market": float(brier_m),
        "ΔBrier": d_brier,
        "ΔBrier_convention": "Brier_model − Brier_market; negative = skill vs mid",
        "LogLoss_model": float(ll_p),
        "LogLoss_market": float(ll_m),
        "ΔLogLoss": d_ll,
        "ΔLogLoss_convention": "LogLoss_model − LogLoss_market; negative = skill vs mid",
        "LogLoss_eps": LOGLOSS_EPS,
        "mean(m_t)": mean_m,
        "mean(p_t)": mean_p,
        "mean(s_t)": float(sum(s_vals) / n) if s_vals else "UNTESTED",
        "mean(|δ_t|)": float(sum(abs(d) for d in d_vals) / len(d_vals)) if d_vals else "UNTESTED",
        "mean(δ_t)": float(sum(d_vals) / len(d_vals)) if d_vals else "UNTESTED",
        "abstention": "none",
        "abstention_rate": 0.0,
        "WR": wr_block["WR"],
        "WR_definition": "p_t>0.5⇒YES; p_t<0.5⇒NO; p_t==0.5 excluded; descriptive only",
        "N_WR": wr_block.get("N_WR"),
        "N_tie_excluded": wr_block.get("N_tie_excluded"),
        "CI": wr_block["CI"],
        "CI_method": wr_block.get("CI_method", "Wilson"),
        "Calibration": {
            "reliability_table": rel,
            "ECE": ece_out,
            "note": ece_note,
            "underpowered": underpowered,
        },
        "ECE": ece_out,
        "gap": {"mean": mean_gap, "mean_abs": mean_abs_gap, "definition": "p_t − m_t"},
        "EV_gross": "UNTESTED",
        "EV_net": "UNTESTED",
        "cost_sensitivity": "UNTESTED",
        "cell_verdict": v["verdict"],
        "cell_reason": v["reason"],
        "contract_ids_scored": contracts,
    }


def apply_feat003(rows: Sequence[FeatRow], s0: float = FEAT003_S0) -> list[float]:
    return [feat003_p(r.m_t, r.s_t, s0=s0) for r in rows]


def apply_feat004(
    rows: Sequence[FeatRow], kappa: float = FEAT004_KAPPA, eps: float = FEAT004_EPS
) -> list[float]:
    out: list[float] = []
    for r in rows:
        if r.delta_t is None:
            raise ValueError(f"missing delta_t for {r.contract_id}")
        out.append(feat004_p(r.m_t, r.delta_t, kappa=kappa, eps=eps))
    return out


def placebo_shuffle_s(rows: Sequence[FeatRow], cell_id: str) -> list[float]:
    """Shuffle s_t within cell (fixed seed), then same FEAT-003 formula."""
    ordered = sorted(rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec))
    s_vals = [r.s_t for r in ordered]
    rng = random.Random(PLACEBO_SEED + CELL_SEED_OFFSET[cell_id])
    shuffled = s_vals[:]
    rng.shuffle(shuffled)
    return [feat003_p(r.m_t, s, s0=FEAT003_S0) for r, s in zip(ordered, shuffled)]


def placebo_signflip_delta(rows: Sequence[FeatRow]) -> list[float]:
    """Sign-flip δ_t, then same FEAT-004 formula."""
    out: list[float] = []
    for r in rows:
        if r.delta_t is None:
            raise ValueError(f"missing delta_t for {r.contract_id}")
        out.append(feat004_p(r.m_t, -r.delta_t, kappa=FEAT004_KAPPA, eps=FEAT004_EPS))
    return out


def rows_for_feat003(rows: Sequence[FeatRow]) -> list[FeatRow]:
    """Drop missing bid/ask / non-finite spread."""
    keep: list[FeatRow] = []
    for r in rows:
        if not math.isfinite(r.s_t):
            continue
        if not math.isfinite(r.yes_bid) or not math.isfinite(r.yes_ask):
            continue
        keep.append(r)
    return keep


def rows_for_feat004(rows: Sequence[FeatRow]) -> list[FeatRow]:
    """Drop missing last / δ."""
    keep: list[FeatRow] = []
    for r in rows:
        if r.last is None or r.delta_t is None:
            continue
        if not math.isfinite(r.last) or not math.isfinite(r.delta_t):
            continue
        keep.append(r)
    return keep
