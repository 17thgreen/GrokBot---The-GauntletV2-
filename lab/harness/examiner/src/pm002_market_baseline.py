"""PM-002 market baseline helpers — m_t calibration vs resolution. No model. No trading."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any, Iterable, Optional, Sequence

# Pre-registered reliability bins (BINARY_EXAMINER_SPEC / Examiner Order).
RELIABILITY_BINS: tuple[tuple[float, float], ...] = (
    (0.02, 0.50),
    (0.50, 0.55),
    (0.55, 0.60),
    (0.60, 0.70),
    (0.70, 0.80),
    (0.80, 0.90),
    (0.90, 0.98),
)

NEAR_DEG_LO = 0.02
NEAR_DEG_HI = 0.98
LOGLOSS_EPS = 1e-15

# Power honesty thresholds (declared before scoring).
MIN_N_FOR_WR_CI = 30
MIN_N_FOR_BIN_RATE_CI = 20
MIN_POWERED_BINS_FOR_CAL = 2  # need ≥2 non-thin bins for powered calibration claim
MIN_N_FOR_ECE = 100

# Checkpoint map from freeze / Clock (Kalshi 15m).
KALSHI_REM_TO_LABEL = {
    840: "T-14m",
    600: "T-10m",
    300: "T-5m",
    60: "T-1m",
    0: "T-0",
}
PRIMARY_REMS = (840, 600, 300)
PRIMARY_ASSETS = ("BTC", "ETH")

FORBIDDEN_MT_FIELDS = ("LAST_PRICE_DOLLARS", "OUTCOME_PRICES")


@dataclass(frozen=True)
class ScoredRow:
    cell_id: str
    contract_id: str
    venue: str
    asset: str
    window: str
    checkpoint: str
    time_remaining_sec: int
    decision_time: str
    m_t: float
    implied_p_method: str
    y: int  # 1=YES, 0=NO
    resolution: str


def is_near_degenerate(p: Optional[float]) -> bool:
    if p is None or not math.isfinite(p):
        return True
    return p <= NEAR_DEG_LO or p >= NEAR_DEG_HI


def accept_mid_row(row: dict[str, Any]) -> bool:
    """Primary/annex Kalshi mid filter: method==mid, not near-deg, finite."""
    if row.get("implied_p_method") != "mid":
        return False
    return not is_near_degenerate(row.get("implied_p"))


def accept_poly_last_row(row: dict[str, Any]) -> bool:
    """Poly annex: last-print only, non-T−0, not near-deg. Never mid."""
    if row.get("venue") != "POLYMARKET_GLOBAL":
        return False
    if row.get("implied_p_method") != "last":
        return False
    if row.get("time_remaining_sec") == 0:
        return False
    return not is_near_degenerate(row.get("implied_p"))


def resolve_y(resolution: Optional[str]) -> Optional[int]:
    if resolution == "YES":
        return 1
    if resolution == "NO":
        return 0
    return None  # VOID / DISPUTED / missing → out of scored N


def wilson_ci(k: int, n: int, z: float = 1.96) -> Optional[tuple[float, float]]:
    """Wilson score interval for binomial proportion. None if n==0."""
    if n <= 0:
        return None
    phat = k / n
    z2 = z * z
    denom = 1.0 + z2 / n
    center = (phat + z2 / (2.0 * n)) / denom
    half = (z / denom) * math.sqrt((phat * (1.0 - phat) + z2 / (4.0 * n)) / n)
    return (max(0.0, center - half), min(1.0, center + half))


def brier_score(m: Sequence[float], y: Sequence[int]) -> Optional[float]:
    n = len(m)
    if n == 0:
        return None
    return float(sum((mi - yi) ** 2 for mi, yi in zip(m, y)) / n)


def log_loss(m: Sequence[float], y: Sequence[int], eps: float = LOGLOSS_EPS) -> Optional[float]:
    n = len(m)
    if n == 0:
        return None
    total = 0.0
    for mi, yi in zip(m, y):
        p = min(1.0 - eps, max(eps, float(mi)))
        total += -(yi * math.log(p) + (1 - yi) * math.log(1.0 - p))
    return float(total / n)


def descriptive_wr(m: Sequence[float], y: Sequence[int]) -> dict[str, Any]:
    """WR: m_t > 0.5 ⇒ YES pred; m_t < 0.5 ⇒ NO pred; m_t == 0.5 excluded from WR.

    Descriptive only — not a skill claim.
    """
    hits = 0
    n_wr = 0
    n_tie = 0
    for mi, yi in zip(m, y):
        if mi == 0.5:
            n_tie += 1
            continue
        pred_yes = mi > 0.5
        n_wr += 1
        if pred_yes and yi == 1:
            hits += 1
        elif (not pred_yes) and yi == 0:
            hits += 1
    if n_wr == 0:
        return {
            "WR": "UNTESTED",
            "WR_definition": "mid>0.5⇒YES; mid<0.5⇒NO; mid==0.5 excluded",
            "N_WR": 0,
            "N_tie_excluded": n_tie,
            "CI": "UNTESTED",
            "CI_method": "Wilson",
        }
    wr = hits / n_wr
    out: dict[str, Any] = {
        "WR": wr,
        "WR_definition": "mid>0.5⇒YES; mid<0.5⇒NO; mid==0.5 excluded",
        "N_WR": n_wr,
        "N_tie_excluded": n_tie,
        "hits": hits,
        "CI_method": "Wilson",
    }
    if n_wr < MIN_N_FOR_WR_CI:
        out["CI"] = "UNTESTED"
        out["CI_reason"] = f"N_WR={n_wr} < MIN_N_FOR_WR_CI={MIN_N_FOR_WR_CI}"
    else:
        ci = wilson_ci(hits, n_wr)
        out["CI"] = {"low": ci[0], "high": ci[1], "level": 0.95} if ci else "UNTESTED"
    return out


def reliability_table(m: Sequence[float], y: Sequence[int]) -> dict[str, Any]:
    """Per-bin reliability. Too-thin → UNTESTED for that bin (no pooling)."""
    bins_out: list[dict[str, Any]] = []
    powered = 0
    for lo, hi in RELIABILITY_BINS:
        idxs = [i for i, mi in enumerate(m) if lo <= mi < hi]
        n = len(idxs)
        label = f"[{lo:.2f},{hi:.2f})"
        if n < MIN_N_FOR_BIN_RATE_CI:
            bins_out.append(
                {
                    "bin": label,
                    "n": n,
                    "mean_m": "UNTESTED" if n == 0 else float(sum(m[i] for i in idxs) / n),
                    "obs_rate": "UNTESTED",
                    "CI": "UNTESTED",
                    "reason": f"n={n} < MIN_N_FOR_BIN_RATE_CI={MIN_N_FOR_BIN_RATE_CI}; not pooled",
                }
            )
            continue
        ys = [y[i] for i in idxs]
        ms = [m[i] for i in idxs]
        k = sum(ys)
        rate = k / n
        ci = wilson_ci(k, n)
        powered += 1
        bins_out.append(
            {
                "bin": label,
                "n": n,
                "mean_m": float(sum(ms) / n),
                "obs_rate": rate,
                "CI": {"low": ci[0], "high": ci[1], "level": 0.95} if ci else "UNTESTED",
                "CI_method": "Wilson",
            }
        )
    return {
        "bins": bins_out,
        "powered_bin_count": powered,
        "min_n_per_bin": MIN_N_FOR_BIN_RATE_CI,
        "pooling": False,
    }


def expected_calibration_error(m: Sequence[float], y: Sequence[int]) -> Any:
    """ECE over pre-registered bins. UNTESTED if N or powered bins insufficient."""
    n = len(m)
    if n < MIN_N_FOR_ECE:
        return "UNTESTED"
    # Also require enough mass in powered bins
    weighted = 0.0
    mass = 0
    for lo, hi in RELIABILITY_BINS:
        idxs = [i for i, mi in enumerate(m) if lo <= mi < hi]
        nb = len(idxs)
        if nb < MIN_N_FOR_BIN_RATE_CI:
            continue
        rate = sum(y[i] for i in idxs) / nb
        mean_m = sum(m[i] for i in idxs) / nb
        weighted += (nb / n) * abs(rate - mean_m)
        mass += nb
    if mass < MIN_N_FOR_ECE:
        return "UNTESTED"
    return float(weighted)


def cell_underpowered_for_calibration(rel: dict[str, Any], n: int) -> bool:
    return (
        n < MIN_N_FOR_ECE
        or rel.get("powered_bin_count", 0) < MIN_POWERED_BINS_FOR_CAL
    )


def score_cell(rows: Sequence[ScoredRow]) -> dict[str, Any]:
    """Full metric dict for one cell — every required key present."""
    m = [r.m_t for r in rows]
    y = [r.y for r in rows]
    n = len(rows)
    wr_block = descriptive_wr(m, y) if n else {
        "WR": "UNTESTED",
        "WR_definition": "mid>0.5⇒YES; mid<0.5⇒NO; mid==0.5 excluded",
        "N_WR": 0,
        "N_tie_excluded": 0,
        "CI": "UNTESTED",
        "CI_method": "Wilson",
    }
    rel = reliability_table(m, y) if n else {
        "bins": [
            {
                "bin": f"[{lo:.2f},{hi:.2f})",
                "n": 0,
                "mean_m": "UNTESTED",
                "obs_rate": "UNTESTED",
                "CI": "UNTESTED",
                "reason": "N=0",
            }
            for lo, hi in RELIABILITY_BINS
        ],
        "powered_bin_count": 0,
        "min_n_per_bin": MIN_N_FOR_BIN_RATE_CI,
        "pooling": False,
    }
    ece = expected_calibration_error(m, y) if n else "UNTESTED"
    underpowered = cell_underpowered_for_calibration(rel, n)
    brier_m = brier_score(m, y) if n else "UNTESTED"
    ll_m = log_loss(m, y) if n else "UNTESTED"
    mean_m = float(sum(m) / n) if n else "UNTESTED"

    contracts = sorted({r.contract_id for r in rows})
    days = sorted({r.decision_time[:10] for r in rows if r.decision_time})

    if n == 0:
        cell_verdict = "FAIL-INSUFFICIENT"
        cal_note = "N=0"
    elif underpowered:
        cell_verdict = "FAIL-INSUFFICIENT"
        cal_note = (
            f"powered calibration underpowered: N={n}, powered_bins="
            f"{rel.get('powered_bin_count', 0)} "
            f"(need ≥{MIN_POWERED_BINS_FOR_CAL} bins with n≥{MIN_N_FOR_BIN_RATE_CI} "
            f"and/or N≥{MIN_N_FOR_ECE} for ECE); thin bins UNTESTED, not pooled"
        )
    else:
        cell_verdict = "BASELINE_MEASURED"
        cal_note = "powered bins present; ECE computed if N allows"

    return {
        "N": n,
        "N_unit": "scored decision-events (checkpoint × contract after filters)",
        "contract_count": len(contracts),
        "distinct_utc_days": len(days),
        "span_utc": {"min": min(days) if days else None, "max": max(days) if days else None},
        "WR": wr_block["WR"],
        "WR_definition": wr_block["WR_definition"],
        "N_WR": wr_block.get("N_WR"),
        "N_tie_excluded": wr_block.get("N_tie_excluded"),
        "CI": wr_block["CI"],
        "CI_method": wr_block.get("CI_method", "Wilson"),
        "Brier_model": "UNTESTED",
        "LogLoss_model": "UNTESTED",
        "Calibration": {
            "reliability_table": rel,
            "ECE": ece,
            "note": cal_note,
        },
        "Brier_market": brier_m,
        "LogLoss_market": ll_m,
        "LogLoss_eps": LOGLOSS_EPS,
        "ΔBrier": "UNTESTED",
        "ΔLogLoss": "UNTESTED",
        "gap": "UNTESTED",
        "EV_gross": "UNTESTED",
        "EV_net": "UNTESTED",
        "abstention_rate": "UNTESTED",
        "cost_sensitivity": "UNTESTED",
        "mean(m_t)": mean_m,
        "underpowered_calibration": underpowered,
        "cell_verdict": cell_verdict,
        "contract_ids_scored": contracts,
    }


def primary_cell_id(asset: str, rem: int) -> str:
    return f"KALSHI|15m|{asset}|{KALSHI_REM_TO_LABEL[rem]}|mid"


def poly_checkpoint_label(window: str, rem: int) -> str:
    """Map rem to declared label for Poly annex."""
    if rem in KALSHI_REM_TO_LABEL:
        return KALSHI_REM_TO_LABEL[rem]
    # 5m Poly uses 240≈T-4m, 180≈T-3m
    if window == "5m" and rem == 240:
        return "T-4m"
    if window == "5m" and rem == 180:
        return "T-3m"
    return f"rem={rem}"


def assert_no_pm001_price_as_mt(m_t_source_fields: Iterable[str]) -> None:
    """Raise if any forbidden PM-001 terminal price field is used as the m_t source.

    Label records may *contain* LAST_PRICE_DOLLARS / OUTCOME_PRICES; that is fine.
    Forbidden is assigning those fields to m_t.
    """
    bad = set(m_t_source_fields) & set(FORBIDDEN_MT_FIELDS)
    if bad:
        raise AssertionError(f"Forbidden PM-001 price fields used as m_t: {bad}")


def m_t_from_checkpoint(row: dict[str, Any]) -> float:
    """m_t = checkpoint implied_p only (never PM-001 terminal prices)."""
    assert_no_pm001_price_as_mt(["implied_p"])  # implied_p is allowed
    if "implied_p" not in row or row["implied_p"] is None:
        raise ValueError("checkpoint missing implied_p for m_t")
    return float(row["implied_p"])
