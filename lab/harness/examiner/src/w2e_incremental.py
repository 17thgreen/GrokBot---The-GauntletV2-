"""W2-E strike-distance vs mid incremental maps vs MKT-KALSHI-15M-MID.

Frozen no-fit map for DRAFT-FEAT-20260913-002 composed with
DRAFT-ABST-20260913-002. Speak only on T-5m headlines when FLOOR_STRIKE
knowable. Pull only on disagreement. No Φ(z). No sibling blend. No annex.
L3 is not the oracle. No trading.
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

# Frozen scored parameters (immutable; not fit on PM-003).
LAMBDA_SCORED = 0.25
DELTA_SCORED = 0.002
EPS = 1e-4
LAMBDA_ROBUST = (0.15, 0.25, 0.35)
DELTA_ROBUST = (0.001, 0.002, 0.004)
PLACEBO_SEED = 20260913
MIN_N_KILL = 80
S_MAX_LAG_MS = 90_000

HEADLINE_BTC = "KALSHI|15m|BTC|T-5m|mid"
HEADLINE_ETH = "KALSHI|15m|ETH|T-5m|mid"
HEADLINES = (HEADLINE_BTC, HEADLINE_ETH)

CELL_SEED_OFFSET = {
    HEADLINE_BTC: 1,
    HEADLINE_ETH: 2,
}

# Gate allowlist (DRAFT-ABST-20260913-002) — headlines only; no annex.
HEADLINE_CELLS = {HEADLINE_BTC, HEADLINE_ETH}


def _clip(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, float(x)))


def _sign(x: float) -> int:
    if x > 0.0:
        return 1
    if x < 0.0:
        return -1
    return 0


def gate_decision(cell_key: str, *, k_knowable: bool) -> str:
    """DRAFT-ABST-20260913-002 eligibility. No annex."""
    if cell_key not in HEADLINE_CELLS:
        return "ABSTAIN"
    if not k_knowable:
        return "ABSTAIN"
    return "ALLOW_SPEAK_HEADLINE"


def signed_distance(s_t: float, k: float) -> Optional[float]:
    if (
        s_t is None
        or k is None
        or not math.isfinite(s_t)
        or not math.isfinite(k)
        or k <= 0
        or s_t <= 0
    ):
        return None
    return (s_t - k) / k


def p_dist_from_d(d: float, delta: float = DELTA_SCORED, eps: float = EPS) -> float:
    ramp = _clip(d / delta, -1.0, 1.0)
    return _clip(0.5 + 0.5 * ramp, eps, 1.0 - eps)


def is_agree(d: float, m_t: float) -> bool:
    """agree = (d==0) or (m==0.5) or sign(d)==sign(m-0.5)."""
    if d == 0.0:
        return True
    if m_t == 0.5:
        return True
    return _sign(d) == _sign(m_t - 0.5)


@dataclass(frozen=True)
class W2ERow:
    cell_id: str
    contract_id: str
    asset: str
    checkpoint: str
    time_remaining_sec: int
    decision_time: str
    decision_time_ms: int
    open_time: str
    m_t: float
    y: int
    k: Optional[float]
    s_t: Optional[float]
    d: Optional[float]
    bar_open_time_ms: Optional[int]
    bar_close_time_ms: Optional[int]
    lag_ms: Optional[int]
    gate: str
    k_knowable: bool
    s_ok: bool
    agree: Optional[bool]
    speak: bool  # True iff ALLOW and K/S ok and disagreement → blend


def incremental_verdict(d_brier: float, d_logloss: float, n: int) -> dict[str, str]:
    """Skill requires both Δ < 0. N < 80 → FAIL-INSUFFICIENT. Not NO_EDGE."""
    if n < MIN_N_KILL:
        return {
            "verdict": "REDUNDANT / FAIL-INSUFFICIENT",
            "reason": (
                f"N={n} < {MIN_N_KILL}; FAIL-INSUFFICIENT "
                "(not NO_EDGE; not Champion)"
            ),
        }
    if d_brier < 0.0 and d_logloss < 0.0:
        return {
            "verdict": "INCREMENTAL_RESEARCH",
            "reason": (
                "both ΔBrier<0 and ΔLogLoss<0 vs mid-only on USED_RESEARCH; "
                "not validation; not sealed holdout; not trading; not Champion"
            ),
        }
    if d_brier >= 0.0 and d_logloss >= 0.0:
        return {
            "verdict": "REDUNDANT / FAIL-INSUFFICIENT",
            "reason": (
                "ΔBrier≥0 and ΔLogLoss≥0 vs mid-only on headline; "
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


def apply_map(
    rows: Sequence[W2ERow],
    *,
    lam: float = LAMBDA_SCORED,
    delta: float = DELTA_SCORED,
    d_override: Optional[Sequence[Optional[float]]] = None,
    s_override: Optional[Sequence[Optional[float]]] = None,
    force_always_blend: bool = False,
) -> list[float]:
    """W2-E frozen map. ABSTAIN / missing / agree → p=m; else blend.

    d_override / s_override used for placebos only.
    force_always_blend: ablation — blend on all ALLOW+KS rows (ignore agree).
    """
    out: list[float] = []
    for i, r in enumerate(rows):
        if r.gate != "ALLOW_SPEAK_HEADLINE":
            out.append(r.m_t)
            continue
        if lam == 0.0:
            out.append(r.m_t)
            continue

        s_t = s_override[i] if s_override is not None else r.s_t
        k = r.k
        if s_t is None or k is None or not math.isfinite(float(s_t)) or not math.isfinite(float(k)) or float(k) <= 0:
            out.append(r.m_t)
            continue

        if d_override is not None:
            d = d_override[i]
            if d is None or not math.isfinite(float(d)):
                out.append(r.m_t)
                continue
            d = float(d)
        else:
            d_val = signed_distance(float(s_t), float(k))
            if d_val is None:
                out.append(r.m_t)
                continue
            d = d_val

        agree = is_agree(d, r.m_t)
        if agree and not force_always_blend:
            out.append(r.m_t)
            continue

        p_dist = p_dist_from_d(d, delta=delta, eps=EPS)
        out.append(_clip((1.0 - lam) * r.m_t + lam * p_dist, EPS, 1.0 - EPS))
    return out


def score_forecast(
    rows: Sequence[W2ERow],
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
            "N_unit": "scored decision-events (checkpoint × contract after TEST-007 excludes)",
            "Brier_model": "UNTESTED",
            "Brier_market": "UNTESTED",
            "ΔBrier": "UNTESTED",
            "LogLoss_model": "UNTESTED",
            "LogLoss_market": "UNTESTED",
            "ΔLogLoss": "UNTESTED",
            "mean(m)": "UNTESTED",
            "mean(p)": "UNTESTED",
            "mean(d)_speak": "UNTESTED",
            "mean(m)_speak": "UNTESTED",
            "mean(p)_speak": "UNTESTED",
            "speak_rate": "UNTESTED",
            "n_speak": 0,
            "n_agree": 0,
            "n_fail_closed_missing_KS": 0,
            "ECE": "UNTESTED",
            "ECE_market": "UNTESTED",
            "WR": "UNTESTED",
            "CI": "UNTESTED",
            "EV_gross": "UNTESTED",
            "EV_net": "UNTESTED",
            "cost_sensitivity": "UNTESTED",
            "cell_verdict": "REDUNDANT / FAIL-INSUFFICIENT",
            "cell_reason": "N=0",
        }

    m = [r.m_t for r in rows]
    y = [r.y for r in rows]
    p_list = [float(pi) for pi in p]
    if len(p_list) != n:
        raise ValueError("p length must match rows")

    n_speak = sum(1 for r in rows if r.speak)
    n_agree = sum(1 for r in rows if r.agree is True)
    n_fail_closed = sum(
        1
        for r in rows
        if r.gate == "ALLOW_SPEAK_HEADLINE" and (not r.k_knowable or not r.s_ok)
    )
    # Also count ABSTAIN due to missing K/S among headline candidates
    n_fail_closed = sum(1 for r in rows if (not r.k_knowable) or (not r.s_ok))

    speak_idx = [i for i, r in enumerate(rows) if r.speak]
    if speak_idx:
        mean_m_speak = float(sum(m[i] for i in speak_idx) / len(speak_idx))
        mean_p_speak = float(sum(p_list[i] for i in speak_idx) / len(speak_idx))
        d_speak = [rows[i].d for i in speak_idx if rows[i].d is not None]
        mean_d_speak: Any = float(sum(d_speak) / len(d_speak)) if d_speak else "UNTESTED"
    else:
        mean_m_speak = "UNTESTED"
        mean_p_speak = "UNTESTED"
        mean_d_speak = "UNTESTED"

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

    wr_block = descriptive_wr(p_list, y)
    rel_p = reliability_table(p_list, y)
    rel_m = reliability_table(m, y)
    ece_p = expected_calibration_error(p_list, y)
    ece_m = expected_calibration_error(m, y)
    underpowered_p = cell_underpowered_for_calibration(rel_p, n)
    underpowered_m = cell_underpowered_for_calibration(rel_m, n)
    if underpowered_p:
        ece_out: Any = "UNTESTED"
        ece_note = (
            f"ECE UNTESTED: thin bins / underpowered "
            f"(N={n}, powered_bins={rel_p.get('powered_bin_count', 0)}; "
            f"need ≥{MIN_POWERED_BINS_FOR_CAL} bins n≥20 and/or N≥{MIN_N_FOR_ECE})"
        )
    else:
        ece_out = ece_p
        ece_note = "powered bins present; ECE on p_t (model)"
    ece_m_out: Any = "UNTESTED" if underpowered_m else ece_m

    v = incremental_verdict(d_brier, d_ll, n)
    contracts = sorted({r.contract_id for r in rows})
    days = sorted({r.decision_time[:10] for r in rows if r.decision_time})
    s_vals = [r.s_t for r in rows if r.s_t is not None]
    k_vals = [r.k for r in rows if r.k is not None]

    return {
        "feature_id": feature_id,
        "map": map_label,
        "N": n,
        "N_unit": "scored decision-events (checkpoint × contract after TEST-007 excludes)",
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
        "mean(m)": mean_m_speak if speak_idx else mean_m,
        "mean(p)": mean_p_speak if speak_idx else mean_p,
        "mean(d)": mean_d_speak,
        "mean(m)_all": mean_m,
        "mean(p)_all": mean_p,
        "mean(m)_speak": mean_m_speak,
        "mean(p)_speak": mean_p_speak,
        "mean(d)_speak": mean_d_speak,
        "mean(S_t)": float(sum(s_vals) / len(s_vals)) if s_vals else "UNTESTED",
        "mean(K)": float(sum(k_vals) / len(k_vals)) if k_vals else "UNTESTED",
        "n_speak": n_speak,
        "n_agree": n_agree,
        "n_fail_closed_missing_KS": n_fail_closed,
        "speak_rate": float(n_speak / n) if n else 0.0,
        "abstention": "gate_ABSTAIN_or_missing_KS_or_agree→p=m",
        "abstention_rate": float((n - n_speak) / n) if n else 0.0,
        "WR": wr_block["WR"],
        "WR_definition": "p_t>0.5⇒YES; p_t<0.5⇒NO; p_t==0.5 excluded; descriptive only",
        "N_WR": wr_block.get("N_WR"),
        "N_tie_excluded": wr_block.get("N_tie_excluded"),
        "CI": wr_block["CI"],
        "CI_method": wr_block.get("CI_method", "Wilson"),
        "Calibration": {
            "reliability_table_model": rel_p,
            "reliability_table_market": rel_m,
            "ECE_model": ece_out,
            "ECE_market": ece_m_out,
            "note": ece_note,
            "underpowered": underpowered_p,
        },
        "ECE": ece_out,
        "ECE_market": ece_m_out,
        "EV_gross": "UNTESTED",
        "EV_net": "UNTESTED",
        "cost_sensitivity": "UNTESTED",
        "cell_verdict": v["verdict"],
        "cell_reason": v["reason"],
        "contract_ids_scored": contracts,
    }


def placebo_lambda_zero(rows: Sequence[W2ERow]) -> list[float]:
    """λ=0 diagnostic — must give Δ=0."""
    return apply_map(rows, lam=0.0)


def placebo_flip_sign_d(rows: Sequence[W2ERow], cell_id: str) -> list[float]:
    """Flip sign of d_t; should not beat the true sign."""
    ordered = sorted(
        rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec)
    )
    # seed retained for determinism parity with other placebos (unused for pure flip)
    _ = random.Random(PLACEBO_SEED + CELL_SEED_OFFSET.get(cell_id, 0))
    overrides: list[Optional[float]] = []
    for r in ordered:
        if r.d is None:
            overrides.append(None)
        else:
            overrides.append(-float(r.d))
    return apply_map(ordered, lam=LAMBDA_SCORED, delta=DELTA_SCORED, d_override=overrides)


def placebo_shuffle_s(rows: Sequence[W2ERow], cell_id: str) -> list[float]:
    """Shuffle S_t within cell leaving K,m fixed; recompute d from shuffled S."""
    ordered = sorted(
        rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec)
    )
    s_vals = [r.s_t for r in ordered]
    rng = random.Random(PLACEBO_SEED + 100 + CELL_SEED_OFFSET.get(cell_id, 0))
    shuffled = s_vals[:]
    rng.shuffle(shuffled)
    return apply_map(ordered, lam=LAMBDA_SCORED, delta=DELTA_SCORED, s_override=shuffled)


def package_verdict(headline_blocks: dict[str, dict[str, Any]]) -> tuple[str, str]:
    """Both headlines must show both-Δ skill. One works other inverts → kill."""
    results = []
    for cid in HEADLINES:
        block = headline_blocks[cid]
        n = block["N"]
        if n == 0 or block["ΔBrier"] == "UNTESTED":
            results.append(("insufficient", cid, block))
            continue
        d_b = float(block["ΔBrier"])
        d_ll = float(block["ΔLogLoss"])
        skill = d_b < 0.0 and d_ll < 0.0 and n >= MIN_N_KILL
        results.append(("skill" if skill else "fail", cid, block))

    skills = [r for r in results if r[0] == "skill"]
    fails = [r for r in results if r[0] != "skill"]

    if len(skills) == 2:
        return (
            "INCREMENTAL_RESEARCH",
            (
                "Both headlines improve Brier and LogLoss vs mid on USED_RESEARCH. "
                "Not validation. Not sealed holdout. Not a Champion. No trading. "
                "L3 ≠ oracle; CONDITIONAL join."
            ),
        )

    if len(skills) == 1 and len(fails) == 1:
        good = skills[0][1]
        bad = fails[0][1]
        bad_b = fails[0][2]
        return (
            "REDUNDANT / FAIL-INSUFFICIENT",
            (
                f"One headline works ({good}) and the other fails/inverts ({bad}: "
                f"ΔBrier={bad_b['ΔBrier']}, ΔLogLoss={bad_b['ΔLogLoss']}, N={bad_b['N']}). "
                "Kill — no pooled rescue. REDUNDANT / FAIL-INSUFFICIENT "
                "(not NO_EDGE; not Champion). USED_RESEARCH; holdout closed; no trading. "
                "L3 ≠ oracle; CONDITIONAL join."
            ),
        )

    return (
        "REDUNDANT / FAIL-INSUFFICIENT",
        (
            "Neither headline improves both Brier and LogLoss vs mid "
            f"(BTC={headline_blocks[HEADLINE_BTC]['cell_verdict']}; "
            f"ETH={headline_blocks[HEADLINE_ETH]['cell_verdict']}). "
            "REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE; not Champion). "
            "USED_RESEARCH; holdout closed; no trading. "
            "L3 ≠ oracle; CONDITIONAL join."
        ),
    )
