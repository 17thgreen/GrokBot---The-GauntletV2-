"""W2-D implied-variance vs |Coinbase 1m| incremental maps vs MKT-KALSHI-15M-MID.

Frozen no-fit map for DRAFT-FEAT-20260913-006 composed with
DRAFT-ABST-20260913-006. Speak only on T-3m (rem=180) headlines under
Policy B (bar_end < decision_time). Sign of v discarded. Not FEAT-005.
No CF. No Map 2. No Φ(z). No Poly last. No Policy A. No annex. No trading.
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

# Frozen scored parameters (immutable; not fit on PM-003/007).
EPS = 1e-4
LAMBDA_SCORED = 0.25
C_SCORED = 80.0
W_SCORED = 0.08
LAMBDA_ROBUST = (0.15, 0.25, 0.40)
C_ROBUST = (50.0, 80.0, 120.0)
W_ROBUST = (0.05, 0.08, 0.12)
PLACEBO_SEED = 20260913
MIN_N_KILL = 80
GRAN = 60
TARGET_REM = 180

HEADLINE_BTC = "KALSHI|15m|BTC|T-3m|mid"
HEADLINE_ETH = "KALSHI|15m|ETH|T-3m|mid"
HEADLINES = (HEADLINE_BTC, HEADLINE_ETH)

CELL_SEED_OFFSET = {
    HEADLINE_BTC: 1,
    HEADLINE_ETH: 2,
}

HEADLINE_CELLS = {HEADLINE_BTC, HEADLINE_ETH}
ASSET_TO_PRODUCT = {"BTC": "BTC-USD", "ETH": "ETH-USD"}


def primary_cell_id_t3m(asset: str) -> str:
    return f"KALSHI|15m|{asset}|T-3m|mid"


def _clip(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, float(x)))


def last_completed_start_policy_b(dec_ts: int) -> int:
    """Policy B: bar_end < decision_time (equiv. bar_end <= dec-1)."""
    aligned_end = ((int(dec_ts) - 1) // GRAN) * GRAN
    return aligned_end - GRAN


def velocity_from_closes(bar_close: float, prior_close: float) -> Optional[float]:
    if (
        bar_close is None
        or prior_close is None
        or not math.isfinite(float(bar_close))
        or not math.isfinite(float(prior_close))
        or float(prior_close) <= 0
    ):
        return None
    return (float(bar_close) - float(prior_close)) / float(prior_close)


def gate_decision(
    cell_key: str,
    *,
    mid_ok: bool,
    bar_ok: bool,
    prior_ok: bool,
    not_locked: bool,
) -> str:
    """DRAFT-ABST-20260913-006 eligibility. Policy B only. No annex."""
    if cell_key not in HEADLINE_CELLS:
        return "ABSTAIN"
    if not mid_ok or not bar_ok or not prior_ok or not not_locked:
        return "ABSTAIN"
    return "ALLOW_SPEAK_HEADLINE"


@dataclass(frozen=True)
class IVRVRow:
    cell_id: str
    contract_id: str
    asset: str
    checkpoint: str
    time_remaining_sec: int
    decision_time: str
    decision_time_ms: int
    open_time: str
    close_time: str
    m_t: float
    y: int
    bar_start_s: Optional[int]
    bar_end_s: Optional[int]
    bar_close: Optional[float]
    prior_close: Optional[float]
    v: Optional[float]  # signed; feature uses abs(v) only
    rv: Optional[float]  # abs(v); sign discarded
    gate: str
    bar_ok: bool
    prior_ok: bool
    not_locked: bool
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
            "verdict": "PROMISING",
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
    rows: Sequence[IVRVRow],
    *,
    lam: float = LAMBDA_SCORED,
    c: float = C_SCORED,
    w: float = W_SCORED,
    rv_override: Optional[Sequence[Optional[float]]] = None,
) -> list[float]:
    """W2-D frozen map. ABSTAIN / missing → p=m; else clipped (iv − c·rv) pull.

    Sign of v is discarded (rv = |v|). Not FEAT-005 signed CB-VEL.
    rv_override used for placebos only.
    """
    out: list[float] = []
    for i, r in enumerate(rows):
        if r.gate != "ALLOW_SPEAK_HEADLINE" or not r.speak:
            out.append(r.m_t)
            continue
        if lam == 0.0:
            out.append(r.m_t)
            continue

        if rv_override is not None:
            rv = rv_override[i]
        else:
            rv = r.rv
        if rv is None or not math.isfinite(float(rv)):
            out.append(r.m_t)
            continue

        m = float(r.m_t)
        iv = m * (1.0 - m)
        resid = iv - float(c) * float(rv)
        out.append(_clip(m + float(lam) * _clip(resid, -float(w), float(w)), EPS, 1.0 - EPS))
    return out


def score_forecast(
    rows: Sequence[IVRVRow],
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
            "mean(rv)_speak": "UNTESTED",
            "mean(m)_speak": "UNTESTED",
            "mean(p)_speak": "UNTESTED",
            "speak_rate": "UNTESTED",
            "n_speak": 0,
            "n_abstain": 0,
            "n_fail_closed_missing": 0,
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
    n_abstain = n - n_speak
    n_fail_closed = sum(
        1 for r in rows if (not r.bar_ok) or (not r.prior_ok) or (not r.not_locked)
    )

    speak_idx = [i for i, r in enumerate(rows) if r.speak]
    if speak_idx:
        mean_m_speak = float(sum(m[i] for i in speak_idx) / len(speak_idx))
        mean_p_speak = float(sum(p_list[i] for i in speak_idx) / len(speak_idx))
        rv_speak = [rows[i].rv for i in speak_idx if rows[i].rv is not None]
        mean_rv_speak: Any = (
            float(sum(rv_speak) / len(rv_speak)) if rv_speak else "UNTESTED"
        )
        iv_speak = [m[i] * (1.0 - m[i]) for i in speak_idx]
        mean_iv_speak = float(sum(iv_speak) / len(speak_idx))
    else:
        mean_m_speak = "UNTESTED"
        mean_p_speak = "UNTESTED"
        mean_rv_speak = "UNTESTED"
        mean_iv_speak = "UNTESTED"

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

    v_all = incremental_verdict(d_brier, d_ll, n)
    contracts = sorted({r.contract_id for r in rows})
    days = sorted({r.decision_time[:10] for r in rows if r.decision_time})
    bar_closes = [r.bar_close for r in rows if r.bar_close is not None]
    prior_closes = [r.prior_close for r in rows if r.prior_close is not None]

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
        "mean(rv)": mean_rv_speak,
        "mean(iv)_speak": mean_iv_speak,
        "mean(m)_all": mean_m,
        "mean(p)_all": mean_p,
        "mean(m)_speak": mean_m_speak,
        "mean(p)_speak": mean_p_speak,
        "mean(rv)_speak": mean_rv_speak,
        "mean(bar_close)": (
            float(sum(bar_closes) / len(bar_closes)) if bar_closes else "UNTESTED"
        ),
        "mean(prior_close)": (
            float(sum(prior_closes) / len(prior_closes)) if prior_closes else "UNTESTED"
        ),
        "n_speak": n_speak,
        "n_abstain": n_abstain,
        "n_fail_closed_missing": n_fail_closed,
        "speak_rate": float(n_speak / n) if n else 0.0,
        "abstention": "gate_ABSTAIN_or_missing_bar/prior/m_or_locked→p=m",
        "abstention_rate": float(n_abstain / n) if n else 0.0,
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
        "cell_verdict": v_all["verdict"],
        "cell_reason": v_all["reason"],
        "contract_ids_scored": contracts,
    }


def placebo_lambda_zero(rows: Sequence[IVRVRow]) -> list[float]:
    """λ=0 diagnostic — must give Δ=0."""
    return apply_map(rows, lam=0.0)


def placebo_shuffle_rv(rows: Sequence[IVRVRow], cell_id: str) -> list[float]:
    """Shuffle rv within cell leaving m fixed."""
    ordered = sorted(
        rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec)
    )
    rv_vals = [r.rv for r in ordered]
    rng = random.Random(PLACEBO_SEED + 100 + CELL_SEED_OFFSET.get(cell_id, 0))
    shuffled = rv_vals[:]
    rng.shuffle(shuffled)
    return apply_map(
        ordered,
        lam=LAMBDA_SCORED,
        c=C_SCORED,
        w=W_SCORED,
        rv_override=shuffled,
    )


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

    stamp = (
        "Mid join CLEARED; CB join CLEARED under lock B; "
        "Policy A not scored; sign of v discarded; not FEAT-005; no rem shop."
    )

    if len(skills) == 2:
        return (
            "PROMISING",
            (
                "Both headlines improve Brier and LogLoss vs mid on USED_RESEARCH. "
                "Not validation. Not sealed holdout. Not a Champion. No trading. "
                + stamp
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
                + stamp
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
            + stamp
        ),
    )
