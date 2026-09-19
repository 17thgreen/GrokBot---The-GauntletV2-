"""F1 incremental forecast maps vs MKT-KALSHI-15M-MID.

Frozen no-fit maps for FEAT-20260912-001 (frozen σ) and
FEAT-20260912-002 (trailing RV σ). No MLE. No ensemble. No trading.
Never uses EXPIRATION_VALUE. Never uses incomplete-bar close.
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
LAMBDA_SCORED = 0.35
LAMBDA_ROBUST = (0.20, 0.35, 0.50)
SIGMA_BTC = 0.55
SIGMA_ETH = 0.70
EPS_P = 1e-4
W_RV = 60
ANN_FACTOR = math.sqrt(365.25 * 24 * 60)  # 1m RMS → annualized
TAU_YEAR_SEC = 365.25 * 24 * 3600
PLACEBO_SEED = 20260912
S_MAX_LAG_MS = 90_000  # card: missing if no L3 bar within 90s of t

HEADLINE_CELLS = (
    "KALSHI|15m|BTC|T-5m|mid",
    "KALSHI|15m|ETH|T-5m|mid",
)
ANNEX_CELLS = (
    "KALSHI|15m|BTC|T-14m|mid",
    "KALSHI|15m|ETH|T-14m|mid",
    "KALSHI|15m|BTC|T-10m|mid",
    "KALSHI|15m|ETH|T-10m|mid",
)
ALL_CELLS = HEADLINE_CELLS + ANNEX_CELLS

CELL_SEED_OFFSET = {
    "KALSHI|15m|BTC|T-5m|mid": 1,
    "KALSHI|15m|ETH|T-5m|mid": 2,
    "KALSHI|15m|BTC|T-14m|mid": 3,
    "KALSHI|15m|ETH|T-14m|mid": 4,
    "KALSHI|15m|BTC|T-10m|mid": 5,
    "KALSHI|15m|ETH|T-10m|mid": 6,
}

SIGMA_FROZEN = {"BTC": SIGMA_BTC, "ETH": SIGMA_ETH}


def _clip(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, float(x)))


def phi(z: float) -> float:
    """Standard normal CDF via erf."""
    return 0.5 * (1.0 + math.erf(float(z) / math.sqrt(2.0)))


def tau_years(time_remaining_sec: float) -> float:
    return float(time_remaining_sec) / TAU_YEAR_SEC


def p_struct_digital(s_t: float, k: float, sigma: float, tau: float) -> Optional[float]:
    """Φ(ln(S/K)/(σ√τ)). Missing if invalid inputs."""
    if (
        s_t is None
        or k is None
        or sigma is None
        or not math.isfinite(s_t)
        or not math.isfinite(k)
        or not math.isfinite(sigma)
        or not math.isfinite(tau)
        or s_t <= 0
        or k <= 0
        or sigma <= 0
        or tau <= 0
    ):
        return None
    z = math.log(s_t / k) / (sigma * math.sqrt(tau))
    if not math.isfinite(z):
        return None
    return phi(z)


def blend_p(m_t: float, p_struct: float, lam: float = LAMBDA_SCORED, eps: float = EPS_P) -> float:
    return _clip((1.0 - lam) * m_t + lam * p_struct, eps, 1.0 - eps)


@dataclass(frozen=True)
class FeatRow:
    cell_id: str
    contract_id: str
    asset: str
    checkpoint: str
    time_remaining_sec: int
    decision_time: str
    decision_time_ms: int
    m_t: float
    y: int
    k: float  # FLOOR_STRIKE
    s_t: float
    bar_open_time_ms: int
    bar_close_time_ms: int
    sigma_frozen: float
    sigma_rv: Optional[float]  # None if W incomplete or σ=0
    join_ok_open_eq_decision_minus_60s: bool


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
            f"(ΔBrier={d_brier:.8f}, ΔLogLoss={d_ll:.8f}); "
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
    k_vals = [r.k for r in rows]
    sig_f = [r.sigma_frozen for r in rows]
    sig_rv = [r.sigma_rv for r in rows if r.sigma_rv is not None]

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
        "mean(S_t)": float(sum(s_vals) / n),
        "mean(K)": float(sum(k_vals) / n),
        "mean(σ_frozen)": float(sum(sig_f) / n) if sig_f else "UNTESTED",
        "mean(σ_rv)": float(sum(sig_rv) / len(sig_rv)) if sig_rv else "UNTESTED",
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


def apply_feat001(
    rows: Sequence[FeatRow],
    lam: float = LAMBDA_SCORED,
    eps: float = EPS_P,
    *,
    sigma_override: Optional[Sequence[Optional[float]]] = None,
) -> list[float]:
    """Frozen-σ structural blend. sigma_override used for placebos only."""
    out: list[float] = []
    for i, r in enumerate(rows):
        sig = r.sigma_frozen if sigma_override is None else sigma_override[i]
        if sig is None:
            raise ValueError(f"missing sigma for {r.contract_id}")
        tau = tau_years(r.time_remaining_sec)
        ps = p_struct_digital(r.s_t, r.k, float(sig), tau)
        if ps is None:
            raise ValueError(f"p_struct missing for {r.contract_id}")
        out.append(blend_p(r.m_t, ps, lam=lam, eps=eps))
    return out


def apply_feat002(
    rows: Sequence[FeatRow],
    lam: float = LAMBDA_SCORED,
    eps: float = EPS_P,
    *,
    sigma_override: Optional[Sequence[Optional[float]]] = None,
) -> list[float]:
    """RV-σ structural blend. Rows must already have finite sigma_rv (or override)."""
    out: list[float] = []
    for i, r in enumerate(rows):
        sig = r.sigma_rv if sigma_override is None else sigma_override[i]
        if sig is None or not math.isfinite(sig) or sig <= 0:
            raise ValueError(f"missing/invalid sigma_rv for {r.contract_id}")
        tau = tau_years(r.time_remaining_sec)
        ps = p_struct_digital(r.s_t, r.k, float(sig), tau)
        if ps is None:
            raise ValueError(f"p_struct missing for {r.contract_id}")
        out.append(blend_p(r.m_t, ps, lam=lam, eps=eps))
    return out


def rows_for_feat001(rows: Sequence[FeatRow]) -> list[FeatRow]:
    keep: list[FeatRow] = []
    for r in rows:
        if not math.isfinite(r.s_t) or r.s_t <= 0:
            continue
        if not math.isfinite(r.k) or r.k <= 0:
            continue
        if r.time_remaining_sec <= 0:
            continue
        if not math.isfinite(r.sigma_frozen) or r.sigma_frozen <= 0:
            continue
        tau = tau_years(r.time_remaining_sec)
        if p_struct_digital(r.s_t, r.k, r.sigma_frozen, tau) is None:
            continue
        keep.append(r)
    return keep


def rows_for_feat002(rows: Sequence[FeatRow]) -> list[FeatRow]:
    keep: list[FeatRow] = []
    for r in rows:
        if r.sigma_rv is None or not math.isfinite(r.sigma_rv) or r.sigma_rv <= 0:
            continue
        if not math.isfinite(r.s_t) or r.s_t <= 0:
            continue
        if not math.isfinite(r.k) or r.k <= 0:
            continue
        if r.time_remaining_sec <= 0:
            continue
        tau = tau_years(r.time_remaining_sec)
        if p_struct_digital(r.s_t, r.k, r.sigma_rv, tau) is None:
            continue
        keep.append(r)
    return keep


def placebo_shuffle_sigma_rv(rows: Sequence[FeatRow], cell_id: str) -> list[float]:
    """Shuffle σ_t across rows leaving (S,K,τ,m) fixed; same FEAT-002 formula."""
    ordered = sorted(rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec))
    sigs = [r.sigma_rv for r in ordered]
    rng = random.Random(PLACEBO_SEED + CELL_SEED_OFFSET[cell_id])
    shuffled = sigs[:]
    rng.shuffle(shuffled)
    return apply_feat002(ordered, lam=LAMBDA_SCORED, sigma_override=shuffled)


def rv_earns_keep(d_brier_002: float, d_ll_002: float, d_brier_001: float, d_ll_001: float) -> dict[str, Any]:
    """002 beats 001 on Δ if both Δ more negative (better skill)."""
    better_brier = d_brier_002 < d_brier_001
    better_ll = d_ll_002 < d_ll_001
    earns = better_brier and better_ll
    return {
        "earns_keep": earns,
        "better_ΔBrier": better_brier,
        "better_ΔLogLoss": better_ll,
        "ΔBrier_002": d_brier_002,
        "ΔBrier_001": d_brier_001,
        "ΔLogLoss_002": d_ll_002,
        "ΔLogLoss_001": d_ll_001,
        "note": (
            "RV earns keep iff both ΔBrier and ΔLogLoss strictly more negative "
            "than FEAT-001 on same cell / same comparable N; else RV REDUNDANT vs sister"
        ),
    }
