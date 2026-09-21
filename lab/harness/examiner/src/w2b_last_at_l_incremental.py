"""W2-B Poly last_L vs Kalshi m_L incremental maps vs m_L incumbent.

Frozen no-fit map for DRAFT-FEAT-20260913-007 composed with
DRAFT-ABST-20260913-007. Speak only on BTC/ETH T-5m mid headlines when
last_L and m_L both exist under DATA_VERDICT_W2B_INCUMBENT_AT_OBS.
Incumbent = m_L at Poly obs_time L. NOT decision-time mid.
last ≠ mid. No Map 2. No CF. No sibling. No CB-VEL. No W2-D. No annex.
No retune. No trading.
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

# Frozen scored parameters (immutable; not fit on the pairable set).
EPS = 1e-4
LAMBDA_SCORED = 0.20
W_SCORED = 0.12
LAMBDA_ROBUST = (0.10, 0.20, 0.30)
W_ROBUST = (0.08, 0.12, 0.16)
PLACEBO_SEED = 20260913
MIN_N_KILL = 80
TARGET_REM = 300

HEADLINE_BTC = "KALSHI|15m|BTC|T-5m|mid"
HEADLINE_ETH = "KALSHI|15m|ETH|T-5m|mid"
HEADLINES = (HEADLINE_BTC, HEADLINE_ETH)

CELL_SEED_OFFSET = {
    HEADLINE_BTC: 1,
    HEADLINE_ETH: 2,
}

HEADLINE_CELLS = {HEADLINE_BTC, HEADLINE_ETH}


def primary_cell_id_t5m(asset: str) -> str:
    return f"KALSHI|15m|{asset}|T-5m|mid"


def _clip(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, float(x)))


def gate_decision(
    cell_key: str,
    *,
    last_ok: bool,
    m_L_ok: bool,
    mid_rule_ok: bool,
) -> str:
    """DRAFT-ABST-20260913-007 eligibility. Incumbent = m_L. No annex."""
    if cell_key not in HEADLINE_CELLS:
        return "ABSTAIN"
    if not last_ok or not m_L_ok or not mid_rule_ok:
        return "ABSTAIN"
    return "ALLOW_SPEAK_HEADLINE"


@dataclass(frozen=True)
class W2BRow:
    cell_id: str
    contract_id: str
    kalshi_ticker: str
    poly_contract_id: str
    asset: str
    checkpoint: str
    time_remaining_sec: int
    decision_time: str
    decision_time_ms: int
    open_time: str
    close_time: str
    L_obs_time: str
    L_unix: int
    last_L: Optional[float]
    m_L: Optional[float]
    m_L_bar_end_ts: Optional[int]
    m_L_yes_bid: Optional[float]
    m_L_yes_ask: Optional[float]
    m_decision_time: Optional[float]  # documented only; NEVER incumbent
    obs_lag_sec: Optional[float]
    y: int
    gate: str
    last_ok: bool
    m_L_ok: bool
    mid_rule_ok: bool
    speak: bool


def incremental_verdict(d_brier: float, d_logloss: float, n: int) -> dict[str, str]:
    """Skill requires both Δ < 0 vs m_L. N < 80 → FAIL-INSUFFICIENT. Not NO_EDGE."""
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
                "both ΔBrier<0 and ΔLogLoss<0 vs m_L on USED_RESEARCH; "
                "not validation; not sealed holdout; not trading; not Champion; "
                "NOT vs decision-time mid"
            ),
        }
    if d_brier >= 0.0 and d_logloss >= 0.0:
        return {
            "verdict": "REDUNDANT / FAIL-INSUFFICIENT",
            "reason": (
                "ΔBrier≥0 and ΔLogLoss≥0 vs m_L on headline; "
                "REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)"
            ),
        }
    return {
        "verdict": "REDUNDANT / FAIL-INSUFFICIENT",
        "reason": (
            "does not improve both Brier and LogLoss vs m_L "
            f"(ΔBrier={d_brier:.8f}, ΔLogLoss={d_logloss:.8f}); "
            "REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)"
        ),
    }


def apply_map(
    rows: Sequence[W2BRow],
    *,
    lam: float = LAMBDA_SCORED,
    w: float = W_SCORED,
    last_override: Optional[Sequence[Optional[float]]] = None,
    flip_sign: bool = False,
) -> list[float]:
    """W2-B frozen map. ABSTAIN / missing → p=m_L; else clipped (last_L − m_L) pull.

    Incumbent is m_L. Decision-time mid is never used as p fallback.
    last_override / flip_sign used for placebos only.
    """
    out: list[float] = []
    for i, r in enumerate(rows):
        if r.m_L is None or not math.isfinite(float(r.m_L)):
            # Should not appear in scored set; fail-closed identity impossible.
            raise ValueError(f"scored row missing m_L: {r.contract_id}")
        m = float(r.m_L)
        if r.gate != "ALLOW_SPEAK_HEADLINE" or not r.speak:
            out.append(m)
            continue
        if lam == 0.0:
            out.append(m)
            continue

        if last_override is not None:
            last = last_override[i]
        else:
            last = r.last_L
        if last is None or not math.isfinite(float(last)):
            out.append(m)
            continue

        b = float(last) - m
        if flip_sign:
            b = -b
        out.append(_clip(m + float(lam) * _clip(b, -float(w), float(w)), EPS, 1.0 - EPS))
    return out


def score_forecast(
    rows: Sequence[W2BRow],
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
            "N_unit": (
                "Wave 005 T-5m pairable OC-twin rows with m_L "
                "(DATA_VERDICT_W2B_INCUMBENT_AT_OBS)"
            ),
            "Brier_model": "UNTESTED",
            "Brier_market": "UNTESTED",
            "ΔBrier": "UNTESTED",
            "LogLoss_model": "UNTESTED",
            "LogLoss_market": "UNTESTED",
            "ΔLogLoss": "UNTESTED",
            "mean(m)": "UNTESTED",
            "mean(p)": "UNTESTED",
            "mean(last_L)_speak": "UNTESTED",
            "mean(m)_speak": "UNTESTED",
            "mean(p)_speak": "UNTESTED",
            "mean(b)_speak": "UNTESTED",
            "mean(obs_lag_sec)": "UNTESTED",
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
            "incumbent": "m_L",
            "decision_time_mid_as_incumbent": False,
        }

    m = [float(r.m_L) for r in rows]  # type: ignore[arg-type]
    y = [r.y for r in rows]
    p_list = [float(pi) for pi in p]
    if len(p_list) != n:
        raise ValueError("p length must match rows")

    n_speak = sum(1 for r in rows if r.speak)
    n_abstain = n - n_speak
    n_fail_closed = sum(
        1 for r in rows if (not r.last_ok) or (not r.m_L_ok) or (not r.mid_rule_ok)
    )

    speak_idx = [i for i, r in enumerate(rows) if r.speak]
    if speak_idx:
        mean_m_speak = float(sum(m[i] for i in speak_idx) / len(speak_idx))
        mean_p_speak = float(sum(p_list[i] for i in speak_idx) / len(speak_idx))
        lasts = [rows[i].last_L for i in speak_idx if rows[i].last_L is not None]
        mean_last_speak: Any = (
            float(sum(float(x) for x in lasts) / len(lasts)) if lasts else "UNTESTED"
        )
        bs = [
            float(rows[i].last_L) - float(rows[i].m_L)  # type: ignore[arg-type]
            for i in speak_idx
            if rows[i].last_L is not None and rows[i].m_L is not None
        ]
        mean_b_speak: Any = float(sum(bs) / len(bs)) if bs else "UNTESTED"
    else:
        mean_m_speak = "UNTESTED"
        mean_p_speak = "UNTESTED"
        mean_last_speak = "UNTESTED"
        mean_b_speak = "UNTESTED"

    lags = [r.obs_lag_sec for r in rows if r.obs_lag_sec is not None]
    mean_lag: Any = float(sum(lags) / len(lags)) if lags else "UNTESTED"

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

    return {
        "feature_id": feature_id,
        "map": map_label,
        "N": n,
        "N_unit": (
            "Wave 005 T-5m pairable OC-twin rows with m_L "
            "(DATA_VERDICT_W2B_INCUMBENT_AT_OBS); NOT 604 invented"
        ),
        "contract_count": len(contracts),
        "distinct_utc_days": len(days),
        "span_utc": {"min": min(days) if days else None, "max": max(days) if days else None},
        "Brier_model": float(brier_p),
        "Brier_market": float(brier_m),
        "ΔBrier": d_brier,
        "ΔBrier_convention": "Brier_model − Brier_m_L; negative = skill vs m_L",
        "LogLoss_model": float(ll_p),
        "LogLoss_market": float(ll_m),
        "ΔLogLoss": d_ll,
        "ΔLogLoss_convention": "LogLoss_model − LogLoss_m_L; negative = skill vs m_L",
        "LogLoss_eps": LOGLOSS_EPS,
        "mean(m)": mean_m,
        "mean(p)": mean_p,
        "mean(m)_all": mean_m,
        "mean(p)_all": mean_p,
        "mean(m)_speak": mean_m_speak,
        "mean(p)_speak": mean_p_speak,
        "mean(last_L)_speak": mean_last_speak,
        "mean(b)_speak": mean_b_speak,
        "mean(obs_lag_sec)": mean_lag,
        "n_speak": n_speak,
        "n_abstain": n_abstain,
        "n_fail_closed_missing": n_fail_closed,
        "speak_rate": float(n_speak / n) if n else 0.0,
        "abstention": "gate_ABSTAIN_or_missing_last_L/m_L/mid-rule→p=m_L",
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
        "incumbent": "m_L",
        "decision_time_mid_as_incumbent": False,
        "Δ_vs_decision_time_mid": "UNTESTED / out of scope (not this instrument)",
        "contract_ids_scored": contracts,
    }


def placebo_lambda_zero(rows: Sequence[W2BRow]) -> list[float]:
    """λ=0 diagnostic — must give Δ=0 vs m_L."""
    return apply_map(rows, lam=0.0)


def placebo_shuffle_last(rows: Sequence[W2BRow], cell_id: str) -> list[float]:
    """Shuffle last_L within cell leaving m_L fixed."""
    ordered = sorted(
        rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec)
    )
    last_vals = [r.last_L for r in ordered]
    rng = random.Random(PLACEBO_SEED + 100 + CELL_SEED_OFFSET.get(cell_id, 0))
    shuffled = last_vals[:]
    rng.shuffle(shuffled)
    return apply_map(
        ordered,
        lam=LAMBDA_SCORED,
        w=W_SCORED,
        last_override=shuffled,
    )


def placebo_flip_sign_b(rows: Sequence[W2BRow]) -> list[float]:
    """Flip sign of b = last_L − m_L."""
    return apply_map(rows, lam=LAMBDA_SCORED, w=W_SCORED, flip_sign=True)


def package_verdict(headline_blocks: dict[str, dict[str, Any]]) -> tuple[str, str]:
    """Both headlines must show both-Δ skill vs m_L. One works other inverts → kill."""
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
        "Join DATA_VERDICT_W2B_INCUMBENT_AT_OBS; incumbent = m_L at Poly obs_time; "
        "last ≠ mid; NOT decision-time mid; 004 not retuned; 45s lag honesty."
    )

    if len(skills) == 2:
        return (
            "PROMISING",
            (
                "Both headlines improve Brier and LogLoss vs m_L on USED_RESEARCH. "
                "Not validation. Not sealed holdout. Not a Champion. No trading. "
                "Δ vs decision-time mid remains UNTESTED / out of scope. "
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
            "Neither headline improves both Brier and LogLoss vs m_L "
            f"(BTC={headline_blocks[HEADLINE_BTC]['cell_verdict']}; "
            f"ETH={headline_blocks[HEADLINE_ETH]['cell_verdict']}). "
            "REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE; not Champion). "
            "USED_RESEARCH; holdout closed; no trading. "
            + stamp
        ),
    )
