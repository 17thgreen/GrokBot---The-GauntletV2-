"""F4 wick-gated structural Φ(z) incremental maps vs MKT-KALSHI-15M-MID.

Frozen no-fit map for DRAFT-FEAT-20260914-008 composed with
DRAFT-ABST-20260914-008. Speak (blend) only on ALLOW + wick rows.
Off-wick → p=m (Feature silence; Δ=0 by construction). Lock B only.
θ/W/λ frozen — no search. No PM-003. L3 ≠ oracle. No trading.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass
from typing import Any, Optional, Sequence

from .f1_incremental import blend_p, phi, p_struct_digital, tau_years
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

# Frozen map (immutable; not fit on PM-004).
EPS = 1e-4
THETA = 1.5
W_WICK = 5
LAMBDA_SCORED = 0.35
LAMBDA_ROBUST = (0.20, 0.35, 0.50)
W_SIGMA = 60
ANN_FACTOR = math.sqrt(365.25 * 24 * 60)  # 1m RMS → annualized
TAU_YEAR_SEC = 365.25 * 24 * 3600
MIN_PER_MIN_FACTOR = math.sqrt(W_WICK / (365.25 * 24 * 60))
PLACEBO_SEED = 20260914
MIN_N_WICK_KILL = 80

HEADLINE_BTC = "KALSHI|15m|BTC|T-5m|mid"
HEADLINE_ETH = "KALSHI|15m|ETH|T-5m|mid"
HEADLINES = (HEADLINE_BTC, HEADLINE_ETH)

CELL_SEED_OFFSET = {
    HEADLINE_BTC: 1,
    HEADLINE_ETH: 2,
}


def _clip(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, float(x)))


@dataclass(frozen=True)
class F4Row:
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
    k: Optional[float]
    s_t: Optional[float]
    s_tW: Optional[float]
    sigma_hat: Optional[float]
    z: Optional[float]
    p_s: Optional[float]
    wick: bool
    lookback_ok: bool
    gate: str  # ALLOW_SPEAK_HEADLINE | ABSTAIN
    bar_end_ms: Optional[int]
    bar_open_ms: Optional[int]
    l3_source: str  # L3-002 | L3-001-edge | missing
    speak: bool  # True iff ALLOW and wick (blend applied)


def wick_threshold(sigma_hat: float) -> float:
    return float(THETA) * float(sigma_hat) * MIN_PER_MIN_FACTOR


def is_wick(s_t: float, s_tW: float, sigma_hat: float) -> bool:
    if s_t <= 0 or s_tW <= 0 or sigma_hat <= 0:
        return False
    if not (math.isfinite(s_t) and math.isfinite(s_tW) and math.isfinite(sigma_hat)):
        return False
    move = abs(math.log(s_t / s_tW))
    return move > wick_threshold(sigma_hat)


def gate_decision(
    cell_key: str,
    *,
    mid_ok: bool,
    lookback_ok: bool,
) -> str:
    """DRAFT-ABST-20260914-008 eligibility. Wick fire is Feature silence, not gate."""
    if cell_key not in HEADLINES:
        return "ABSTAIN"
    if not mid_ok or not lookback_ok:
        return "ABSTAIN"
    return "ALLOW_SPEAK_HEADLINE"


def incremental_verdict(
    d_brier: float, d_logloss: float, n: int, n_wick: int
) -> dict[str, str]:
    """Skill requires both Δ < 0 on full cell. N_wick < 80 kills. Not NO_EDGE."""
    if n_wick < MIN_N_WICK_KILL:
        return {
            "verdict": "REDUNDANT / FAIL-INSUFFICIENT",
            "reason": (
                f"N_wick={n_wick} < {MIN_N_WICK_KILL}; FAIL-INSUFFICIENT "
                "(not NO_EDGE; not Champion)"
            ),
        }
    if n < MIN_N_WICK_KILL:
        return {
            "verdict": "REDUNDANT / FAIL-INSUFFICIENT",
            "reason": (
                f"N={n} < {MIN_N_WICK_KILL}; FAIL-INSUFFICIENT "
                "(not NO_EDGE; not Champion)"
            ),
        }
    if d_brier < 0.0 and d_logloss < 0.0:
        return {
            "verdict": "PROMISING",
            "reason": (
                "both ΔBrier<0 and ΔLogLoss<0 vs mid-only on full cell "
                "(USED_RESEARCH); not validation; not sealed holdout; "
                "not trading; not Champion"
            ),
        }
    if d_brier >= 0.0 and d_logloss >= 0.0:
        return {
            "verdict": "REDUNDANT / FAIL-INSUFFICIENT",
            "reason": (
                "ΔBrier≥0 and ΔLogLoss≥0 vs mid-only on full cell; "
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
    rows: Sequence[F4Row],
    *,
    lam: float = LAMBDA_SCORED,
    wick_override: Optional[Sequence[bool]] = None,
    sign_flip_ps: bool = False,
    reverse_gate: bool = False,
) -> list[float]:
    """F4 frozen map. ABSTAIN / missing / off-wick → p=m; wick → blend.

    Overrides are for placebos only.
    """
    out: list[float] = []
    for i, r in enumerate(rows):
        if r.gate != "ALLOW_SPEAK_HEADLINE" or not r.lookback_ok:
            out.append(r.m_t)
            continue
        if lam == 0.0:
            out.append(r.m_t)
            continue
        wick = bool(r.wick) if wick_override is None else bool(wick_override[i])
        if reverse_gate:
            speak = not wick
        else:
            speak = wick
        if not speak:
            out.append(r.m_t)
            continue
        if r.p_s is None or not math.isfinite(float(r.p_s)):
            out.append(r.m_t)
            continue
        ps = float(r.p_s)
        if sign_flip_ps:
            # Flip structural signal about 0.5: p_s' = 1 - p_s
            ps = 1.0 - ps
        out.append(blend_p(r.m_t, ps, lam=lam, eps=EPS))
    return out


def score_forecast(
    rows: Sequence[F4Row],
    p: Sequence[float],
    *,
    feature_id: str,
    map_label: str,
) -> dict[str, Any]:
    n = len(rows)
    n_wick = sum(1 for r in rows if r.speak)
    n_allow = sum(1 for r in rows if r.gate == "ALLOW_SPEAK_HEADLINE")
    n_abstain = sum(1 for r in rows if r.gate == "ABSTAIN")
    n_off_wick = sum(
        1
        for r in rows
        if r.gate == "ALLOW_SPEAK_HEADLINE" and r.lookback_ok and not r.wick
    )

    if n == 0:
        return {
            "feature_id": feature_id,
            "map": map_label,
            "N": 0,
            "N_unit": "scored decision-events (Sep-12 PM-004 mid T-5m after filters)",
            "N_wick": 0,
            "n_speak": 0,
            "n_allow": 0,
            "n_abstain": 0,
            "n_off_wick": 0,
            "speak_rate": "UNTESTED",
            "Brier_model": "UNTESTED",
            "Brier_market": "UNTESTED",
            "ΔBrier": "UNTESTED",
            "LogLoss_model": "UNTESTED",
            "LogLoss_market": "UNTESTED",
            "ΔLogLoss": "UNTESTED",
            "mean(m)": "UNTESTED",
            "mean(p)": "UNTESTED",
            "mean(m)_speak": "UNTESTED",
            "mean(p)_speak": "UNTESTED",
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

    speak_idx = [i for i, r in enumerate(rows) if r.speak]
    if speak_idx:
        mean_m_speak: Any = float(sum(m[i] for i in speak_idx) / len(speak_idx))
        mean_p_speak: Any = float(sum(p_list[i] for i in speak_idx) / len(speak_idx))
    else:
        mean_m_speak = "UNTESTED"
        mean_p_speak = "UNTESTED"

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

    v = incremental_verdict(d_brier, d_ll, n, n_wick)
    contracts = sorted({r.contract_id for r in rows})
    days = sorted({r.decision_time[:10] for r in rows if r.decision_time})
    s_vals = [r.s_t for r in rows if r.s_t is not None]
    k_vals = [r.k for r in rows if r.k is not None]
    sig_vals = [r.sigma_hat for r in rows if r.sigma_hat is not None]
    ps_vals = [r.p_s for r in rows if r.p_s is not None and r.speak]

    # Wick-subset Δ annex (not a leaderboard / not kill axis for skill claim)
    wick_rows = [rows[i] for i in speak_idx]
    wick_p = [p_list[i] for i in speak_idx]
    wick_annex: dict[str, Any]
    if wick_rows:
        wm = [r.m_t for r in wick_rows]
        wy = [r.y for r in wick_rows]
        wb_m = brier_score(wm, wy)
        wb_p = brier_score(wick_p, wy)
        wl_m = log_loss(wm, wy)
        wl_p = log_loss(wick_p, wy)
        assert wb_m is not None and wb_p is not None
        assert wl_m is not None and wl_p is not None
        wick_annex = {
            "N_wick": len(wick_rows),
            "Brier_model": float(wb_p),
            "Brier_market": float(wb_m),
            "ΔBrier": float(wb_p - wb_m),
            "LogLoss_model": float(wl_p),
            "LogLoss_market": float(wl_m),
            "ΔLogLoss": float(wl_p - wl_m),
            "note": "annex only — skill scored on full cell; off-wick Δ=0 by construction",
        }
    else:
        wick_annex = {
            "N_wick": 0,
            "Brier_model": "UNTESTED",
            "Brier_market": "UNTESTED",
            "ΔBrier": "UNTESTED",
            "LogLoss_model": "UNTESTED",
            "LogLoss_market": "UNTESTED",
            "ΔLogLoss": "UNTESTED",
            "note": "annex only — no wick rows",
        }

    return {
        "feature_id": feature_id,
        "map": map_label,
        "N": n,
        "N_unit": "scored decision-events (Sep-12 PM-004 mid T-5m after filters)",
        "N_wick": n_wick,
        "n_speak": n_wick,
        "n_allow": n_allow,
        "n_abstain": n_abstain,
        "n_off_wick": n_off_wick,
        "n_fail_closed_missing": n_abstain,
        "speak_rate": float(n_wick / n) if n else 0.0,
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
        "mean(m)_all": mean_m,
        "mean(p)_all": mean_p,
        "mean(m)_speak": mean_m_speak,
        "mean(p)_speak": mean_p_speak,
        "mean(S_t)": float(sum(s_vals) / len(s_vals)) if s_vals else "UNTESTED",
        "mean(K)": float(sum(k_vals) / len(k_vals)) if k_vals else "UNTESTED",
        "mean(σhat)": float(sum(sig_vals) / len(sig_vals)) if sig_vals else "UNTESTED",
        "mean(p_s)_speak": (
            float(sum(ps_vals) / len(ps_vals)) if ps_vals else "UNTESTED"
        ),
        "abstention": "Cartographer ABSTAIN → p:=m; Feature silence off-wick → p:=m",
        "abstention_rate": float(n_abstain / n) if n else 0.0,
        "WR": wr_block["WR"],
        "WR_definition": "p_t>0.5⇒YES; p_t<0.5⇒NO; p_t==0.5 excluded; descriptive only",
        "N_WR": wr_block.get("N_WR"),
        "N_tie_excluded": wr_block.get("N_tie_excluded"),
        "CI": wr_block["CI"],
        "CI_method": wr_block.get("CI_method", "Wilson"),
        "Calibration": {
            "reliability_table": rel_p,
            "ECE": ece_out,
            "note": ece_note,
            "underpowered": underpowered_p,
        },
        "ECE": ece_out,
        "ECE_market": ece_m_out,
        "gap": {"mean": mean_gap, "mean_abs": mean_abs_gap, "definition": "p_t − m_t"},
        "EV_gross": "UNTESTED",
        "EV_net": "UNTESTED",
        "cost_sensitivity": "UNTESTED",
        "wick_subset_annex": wick_annex,
        "cell_verdict": v["verdict"],
        "cell_reason": v["reason"],
        "contract_ids_scored": contracts,
    }


def package_verdict(headline_blocks: dict[str, dict[str, Any]]) -> tuple[str, str]:
    """Both headlines must show both-Δ skill and N_wick≥80. One-asset invert kills."""
    results = []
    for cid in HEADLINES:
        block = headline_blocks[cid]
        n = block["N"]
        n_wick = int(block.get("N_wick") or 0)
        if n == 0 or block["ΔBrier"] == "UNTESTED":
            results.append(("insufficient", cid, block))
            continue
        d_b = float(block["ΔBrier"])
        d_ll = float(block["ΔLogLoss"])
        skill = (
            d_b < 0.0
            and d_ll < 0.0
            and n_wick >= MIN_N_WICK_KILL
            and n >= MIN_N_WICK_KILL
        )
        results.append(("skill" if skill else "fail", cid, block))

    skills = [r for r in results if r[0] == "skill"]
    fails = [r for r in results if r[0] != "skill"]

    stamp = (
        "Sep-12 PM-004; lock B; L3 ≠ oracle; no PM-003; θ/W frozen no search; "
        "Governor SIGN F4."
    )

    if len(skills) == 2:
        return (
            "PROMISING",
            (
                "Both headlines improve Brier and LogLoss vs mid on full cell "
                "(USED_RESEARCH). Not validation. Not sealed holdout. Not Champion. "
                "No trading. " + stamp
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
                f"ΔBrier={bad_b['ΔBrier']}, ΔLogLoss={bad_b['ΔLogLoss']}, "
                f"N={bad_b['N']}, N_wick={bad_b.get('N_wick')}). "
                "Kill — no pooled rescue. REDUNDANT / FAIL-INSUFFICIENT "
                "(not NO_EDGE; not Champion). USED_RESEARCH; holdout closed; no trading. "
                + stamp
            ),
        )

    return (
        "REDUNDANT / FAIL-INSUFFICIENT",
        (
            "Neither headline improves both Brier and LogLoss vs mid on full cell "
            f"(BTC={headline_blocks[HEADLINE_BTC]['cell_verdict']}; "
            f"ETH={headline_blocks[HEADLINE_ETH]['cell_verdict']}). "
            "REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE; not Champion). "
            "USED_RESEARCH; holdout closed; no trading. "
            + stamp
        ),
    )


def placebo_lambda_zero(rows: Sequence[F4Row]) -> list[float]:
    return apply_map(rows, lam=0.0)


def placebo_shuffle_wick(rows: Sequence[F4Row], cell_id: str) -> list[float]:
    """Shuffle wick labels within cell; m / p_s / lookback fixed."""
    ordered = sorted(
        rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec)
    )
    # Only shuffle among ALLOW+lookback_ok rows' wick flags; keep ABSTAIN as False.
    flags = []
    allow_idx = []
    for i, r in enumerate(ordered):
        if r.gate == "ALLOW_SPEAK_HEADLINE" and r.lookback_ok:
            flags.append(bool(r.wick))
            allow_idx.append(i)
        else:
            flags.append(False)
    rng = random.Random(PLACEBO_SEED + 200 + CELL_SEED_OFFSET.get(cell_id, 0))
    allow_flags = [flags[i] for i in allow_idx]
    rng.shuffle(allow_flags)
    for j, i in enumerate(allow_idx):
        flags[i] = allow_flags[j]
    return apply_map(ordered, lam=LAMBDA_SCORED, wick_override=flags)


def placebo_reverse_gate(rows: Sequence[F4Row]) -> list[float]:
    """Blend only when NO wick (reverse of card)."""
    return apply_map(rows, lam=LAMBDA_SCORED, reverse_gate=True)


def placebo_sign_flip_ps(rows: Sequence[F4Row]) -> list[float]:
    """Sign-flip p_struct on wick rows (p_s → 1−p_s)."""
    return apply_map(rows, lam=LAMBDA_SCORED, sign_flip_ps=True)
