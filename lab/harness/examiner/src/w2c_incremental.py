"""W2-C sibling-mid incremental maps vs MKT-KALSHI-15M-MID.

Frozen no-fit map for DRAFT-FEAT-20260913-001 composed with
DRAFT-ABST-20260913-001. Speak only on ALLOW_SPEAK_HEADLINE.
Annex BTC T-14m is DARK. No λ search. No trading.
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

# Frozen scored blend (immutable; not fit on PM-003).
LAMBDA_SCORED = 0.25
EPS = 1e-4
LAMBDA_ROBUST = (0.15, 0.25, 0.35)
PLACEBO_SEED = 20260913
MIN_N_KILL = 80

HEADLINE_A = "KALSHI|15m|ETH|T-14m|mid"
HEADLINE_B = "KALSHI|15m|BTC|T-10m|mid"
HEADLINES = (HEADLINE_A, HEADLINE_B)
ANNEX_DARK = "KALSHI|15m|BTC|T-14m|mid"  # DARK — do not score as speak

CELL_SEED_OFFSET = {
    HEADLINE_A: 1,
    HEADLINE_B: 2,
    ANNEX_DARK: 3,
}

# Gate allowlist (DRAFT-ABST-20260913-001) — constants only.
ELIGIBLE_CELLS = {
    "KALSHI|15m|ETH|T-14m|mid",
    "KALSHI|15m|BTC|T-10m|mid",
    "KALSHI|15m|BTC|T-14m|mid",
}
HEADLINE_CELLS = {HEADLINE_A, HEADLINE_B}
ANNEX_CELLS = {ANNEX_DARK}


def _clip(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, float(x)))


def gate_decision(cell_key: str, *, opts_in_annex: bool = False) -> str:
    """DRAFT-ABST-20260913-001 eligibility. Feature does NOT opt in annex."""
    if cell_key not in ELIGIBLE_CELLS:
        return "ABSTAIN"
    if cell_key in HEADLINE_CELLS:
        return "ALLOW_SPEAK_HEADLINE"
    if cell_key in ANNEX_CELLS and opts_in_annex:
        return "ALLOW_SPEAK_ANNEX"
    return "ABSTAIN"


@dataclass(frozen=True)
class W2CRow:
    cell_id: str
    contract_id: str
    sibling_contract_id: Optional[str]
    asset: str
    sibling_asset: str
    checkpoint: str
    time_remaining_sec: int
    decision_time: str
    open_time: str
    close_time: str
    m_t: float
    m_star: Optional[float]
    y: int
    gate: str
    speak: bool


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
    rows: Sequence[W2CRow],
    *,
    lam: float = LAMBDA_SCORED,
    m_star_override: Optional[Sequence[Optional[float]]] = None,
) -> list[float]:
    """On ABSTAIN or missing sibling: p=m. On ALLOW_SPEAK_*: blend."""
    out: list[float] = []
    for i, r in enumerate(rows):
        m_star = (
            m_star_override[i]
            if m_star_override is not None
            else r.m_star
        )
        if r.gate not in ("ALLOW_SPEAK_HEADLINE", "ALLOW_SPEAK_ANNEX"):
            out.append(r.m_t)
            continue
        if m_star is None or not math.isfinite(float(m_star)):
            out.append(r.m_t)
            continue
        if lam == 0.0:
            out.append(r.m_t)
            continue
        out.append(blend_p(r.m_t, float(m_star), lam=lam))
    return out


def score_forecast(
    rows: Sequence[W2CRow],
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
            "mean(m*)": "UNTESTED",
            "abstention": "none",
            "abstention_rate": 0.0,
            "n_speak": 0,
            "n_fail_closed_missing_sibling": 0,
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

    m_stars = [r.m_star for r in rows if r.m_star is not None and math.isfinite(r.m_star)]
    n_speak = sum(1 for r, pi in zip(rows, p_list) if abs(pi - r.m_t) > 1e-15)
    # More precise speak count from gate+sibling
    n_speak = sum(
        1
        for r in rows
        if r.gate in ("ALLOW_SPEAK_HEADLINE", "ALLOW_SPEAK_ANNEX")
        and r.m_star is not None
        and math.isfinite(r.m_star)
    )
    n_fail_closed = sum(
        1
        for r in rows
        if r.gate in ("ALLOW_SPEAK_HEADLINE", "ALLOW_SPEAK_ANNEX")
        and (r.m_star is None or not math.isfinite(float(r.m_star or float("nan"))))
    )

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
    mean_mstar = float(sum(m_stars) / len(m_stars)) if m_stars else "UNTESTED"

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
        "mean(m)": mean_m,
        "mean(p)": mean_p,
        "mean(m*)": mean_mstar,
        "n_speak": n_speak,
        "n_fail_closed_missing_sibling": n_fail_closed,
        "abstention": "gate_ABSTAIN_or_missing_sibling→p=m",
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


def placebo_shuffle_mstar(rows: Sequence[W2CRow], cell_id: str) -> list[float]:
    """Shuffle m* within cell (fixed seed), leave m_t fixed; same blend."""
    ordered = sorted(
        rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec)
    )
    stars = [r.m_star for r in ordered]
    rng = random.Random(PLACEBO_SEED + CELL_SEED_OFFSET.get(cell_id, 0))
    shuffled = stars[:]
    rng.shuffle(shuffled)
    return apply_map(ordered, lam=LAMBDA_SCORED, m_star_override=shuffled)


def placebo_lambda_zero(rows: Sequence[W2CRow]) -> list[float]:
    """λ=0 diagnostic — must give Δ=0."""
    return apply_map(rows, lam=0.0)


def placebo_wrong_window(
    rows: Sequence[W2CRow],
    pool_by_asset_rem: dict[tuple[str, int], list[tuple[str, str, float]]],
) -> list[float]:
    """Wrong-window sibling: opposite asset same rem, different OPEN/CLOSE.

    pool entries: (open_time, close_time, m_star) for sibling asset at rem.
    Deterministic seeded pick of a different window when available.
    """
    ordered = sorted(
        rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec)
    )
    overrides: list[Optional[float]] = []
    for i, r in enumerate(ordered):
        key = (r.sibling_asset, r.time_remaining_sec)
        pool = pool_by_asset_rem.get(key, [])
        wrong = [
            m
            for (ot, ct, m) in pool
            if (ot, ct) != (r.open_time, r.close_time)
        ]
        if not wrong:
            overrides.append(None)  # fail-closed → p=m
            continue
        rng = random.Random(PLACEBO_SEED + 1000 + CELL_SEED_OFFSET.get(r.cell_id, 0) + i)
        overrides.append(wrong[rng.randrange(len(wrong))])
    return apply_map(ordered, lam=LAMBDA_SCORED, m_star_override=overrides)


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
                "Not validation. Not sealed holdout. Not a Champion. No trading."
            ),
        )

    # one works other fails/inverts
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
                "(not NO_EDGE; not Champion). USED_RESEARCH; holdout closed; no trading."
            ),
        )

    return (
        "REDUNDANT / FAIL-INSUFFICIENT",
        (
            "Neither headline improves both Brier and LogLoss vs mid "
            f"(A={headline_blocks[HEADLINE_A]['cell_verdict']}; "
            f"B={headline_blocks[HEADLINE_B]['cell_verdict']}). "
            "REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE; not Champion). "
            "USED_RESEARCH; holdout closed; no trading."
        ),
    )
