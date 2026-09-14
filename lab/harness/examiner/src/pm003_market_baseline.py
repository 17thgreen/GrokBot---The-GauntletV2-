"""PM-003 market baseline helpers.

Reuses PM-002 scoring honesty (bins, Wilson, ECE gates, UNTESTED keys).
No model. No trading. No Poly. No PM-002 union.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any, Iterable

from .pm002_market_baseline import (  # reuse — do not reinvent
    FORBIDDEN_MT_FIELDS,
    KALSHI_REM_TO_LABEL,
    LOGLOSS_EPS,
    MIN_N_FOR_BIN_RATE_CI,
    MIN_N_FOR_ECE,
    MIN_N_FOR_WR_CI,
    MIN_POWERED_BINS_FOR_CAL,
    NEAR_DEG_HI,
    NEAR_DEG_LO,
    PRIMARY_ASSETS,
    PRIMARY_REMS,
    RELIABILITY_BINS,
    ScoredRow,
    accept_mid_row,
    assert_no_pm001_price_as_mt,
    brier_score,
    cell_underpowered_for_calibration,
    descriptive_wr,
    expected_calibration_error,
    is_near_degenerate,
    log_loss,
    m_t_from_checkpoint,
    primary_cell_id,
    reliability_table,
    resolve_y,
    score_cell,
    wilson_ci,
)

EXPECTED_CHECKPOINTS_SHA256 = (
    "90e38c2f23e224def13db05924f6470a1e738778882f6b0cc17ed708b3143765"
)


class DataIntegrityError(Exception):
    """Hard fail: hash mismatch, PM-002 union, or non-Kalshi rows."""


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_checkpoints_sha256(
    path: Path, expected: str = EXPECTED_CHECKPOINTS_SHA256
) -> str:
    digest = sha256_file(path)
    if digest != expected:
        raise DataIntegrityError(
            f"DATA_INTEGRITY_FAIL: {path} sha256={digest} expected={expected}"
        )
    return digest


def extract_ids(
    rows: Iterable[dict[str, Any]],
    keys: tuple[str, ...] = ("contract_id", "venue_native_id", "CONTRACT_ID", "VENUE_NATIVE_ID"),
) -> set[str]:
    out: set[str] = set()
    for r in rows:
        for k in keys:
            v = r.get(k)
            if v:
                out.add(str(v))
    return out


def assert_no_pm002_overlap(pm003_ids: set[str], pm002_ids: set[str]) -> dict[str, Any]:
    overlap = sorted(pm003_ids & pm002_ids)
    if overlap:
        raise DataIntegrityError(
            f"DATA_INTEGRITY_FAIL: PM-002 overlap forbidden ({len(overlap)} ids); "
            "no union, no PM-002 checkpoint rows"
        )
    return {"overlap_count": 0, "overlap_ids": [], "pm003_id_n": len(pm003_ids), "pm002_id_n": len(pm002_ids)}


def assert_kalshi_only(checkpoints: Iterable[dict[str, Any]]) -> dict[str, Any]:
    counts: dict[str, int] = {}
    for r in checkpoints:
        v = str(r.get("venue") or "MISSING")
        counts[v] = counts.get(v, 0) + 1
    bad = {k: n for k, n in counts.items() if k != "KALSHI"}
    if bad:
        raise DataIntegrityError(
            f"DATA_INTEGRITY_FAIL: non-KALSHI venues in PM-003 checkpoints: {bad}"
        )
    return {"venues": counts, "poly_rows": 0}


__all__ = [
    "FORBIDDEN_MT_FIELDS",
    "KALSHI_REM_TO_LABEL",
    "LOGLOSS_EPS",
    "MIN_N_FOR_BIN_RATE_CI",
    "MIN_N_FOR_ECE",
    "MIN_N_FOR_WR_CI",
    "MIN_POWERED_BINS_FOR_CAL",
    "NEAR_DEG_HI",
    "NEAR_DEG_LO",
    "PRIMARY_ASSETS",
    "PRIMARY_REMS",
    "RELIABILITY_BINS",
    "EXPECTED_CHECKPOINTS_SHA256",
    "DataIntegrityError",
    "ScoredRow",
    "accept_mid_row",
    "assert_kalshi_only",
    "assert_no_pm001_price_as_mt",
    "assert_no_pm002_overlap",
    "brier_score",
    "cell_underpowered_for_calibration",
    "descriptive_wr",
    "expected_calibration_error",
    "extract_ids",
    "is_near_degenerate",
    "log_loss",
    "m_t_from_checkpoint",
    "primary_cell_id",
    "reliability_table",
    "resolve_y",
    "score_cell",
    "sha256_file",
    "verify_checkpoints_sha256",
    "wilson_ci",
]
