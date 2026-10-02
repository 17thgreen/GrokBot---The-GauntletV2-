#!/usr/bin/env python3
"""TEST-20260913-002 — W2C-INCREMENTAL vs MKT-KALSHI-15M-MID.

Sibling same-window mid blend (λ=0.25 frozen) on DRAFT-ABST headlines only.
Annex BTC T-14m DARK. No PM-002. No Poly. No CF. No L3. No trading.
invented_numbers=false.
"""

from __future__ import annotations

import json
import math
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.pm003_market_baseline import (  # noqa: E402
    EXPECTED_CHECKPOINTS_SHA256,
    KALSHI_REM_TO_LABEL,
    DataIntegrityError,
    accept_mid_row,
    assert_kalshi_only,
    assert_no_pm001_price_as_mt,
    m_t_from_checkpoint,
    primary_cell_id,
    resolve_y,
    verify_checkpoints_sha256,
)
from src.w2c_incremental import (  # noqa: E402
    ANNEX_DARK,
    EPS,
    HEADLINE_A,
    HEADLINE_B,
    HEADLINES,
    LAMBDA_ROBUST,
    LAMBDA_SCORED,
    MIN_N_KILL,
    PLACEBO_SEED,
    W2CRow,
    apply_map,
    gate_decision,
    package_verdict,
    placebo_lambda_zero,
    placebo_shuffle_mstar,
    placebo_wrong_window,
    score_forecast,
)

LAB = Path("/workspace/lab")
CHECKPOINTS = LAB / "data/DATA-PROV-PM-003/derived/checkpoints.ndjson"
COVERAGE = LAB / "data/DATA-PROV-PM-003/derived/contract_coverage.ndjson"
KALSHI_LABELS = LAB / "data/DATA-PROV-PM-001/normalized/kalshi_15m_btc_eth_resolved.ndjson"
OUT_DIR = LAB / "harness/examiner/out"
ARCHIVE_TESTS = LAB / "archive/tests"
ARCHIVE_AUDIT = LAB / "archive/audit"

TEST_ID = "TEST-20260913-002"
PACKAGE = "W2C-INCREMENTAL"
INCUMBENT = "MKT-KALSHI-15M-MID"
FEATURE_ID = "DRAFT-FEAT-20260913-001"
GATE_ID = "DRAFT-ABST-20260913-001"

AUTHORITY = [
    "governance/EXAMINER_ORDER_TEST-20260913-002-W2C.md",
    "archive/features/DRAFT-FEAT-20260913-001-W2C-sibling-mid.md",
    "archive/features/DRAFT-ABST-20260913-001-W2C-bad-cal.md",
    "data/DATA-PROV-PM-003/provenance/DATA_VERDICT_W2C_SIBLING_JOIN.md",
]

TARGET_REMS = {840, 600}  # headlines + annex rem; T-5m not scored
SIBLING = {"BTC": "ETH", "ETH": "BTC"}


def _load_ndjson(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def _index_labels(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    idx: dict[str, dict[str, Any]] = {}
    for r in rows:
        cid = r.get("CONTRACT_ID")
        nid = r.get("VENUE_NATIVE_ID")
        if cid:
            idx[cid] = r
        if nid:
            idx[nid] = r
    return idx


def _join_label(row: dict[str, Any], idx: dict[str, dict[str, Any]]) -> dict[str, Any] | None:
    return idx.get(row.get("contract_id", "")) or idx.get(row.get("venue_native_id", ""))


def _near_deg(ip: Any) -> bool:
    if ip is None:
        return True
    try:
        x = float(ip)
    except (TypeError, ValueError):
        return True
    return x <= 0.02 or x >= 0.98


def _is_void(lab: dict[str, Any]) -> bool:
    st = str(lab.get("STATUS") or "").upper()
    res = str(lab.get("RESOLUTION") or "").upper()
    return st in ("VOID", "DISPUTED") or res in ("VOID", "DISPUTED")


def enrich_checkpoints(
    checkpoints: list[dict],
    coverage: list[dict],
    kalshi_idx: dict[str, dict],
) -> tuple[list[dict], dict[str, Any]]:
    cov = {c["contract_id"]: c for c in coverage}
    enriched: list[dict] = []
    stats = {
        "missing_coverage": 0,
        "missing_pm001": 0,
        "open_close_mismatch_vs_pm001": 0,
    }
    for r in checkpoints:
        if r.get("venue") != "KALSHI" or r.get("window") != "15m":
            continue
        cid = r["contract_id"]
        c = cov.get(cid)
        lab = _join_label(r, kalshi_idx)
        if c is None:
            stats["missing_coverage"] += 1
            continue
        if lab is None:
            stats["missing_pm001"] += 1
            continue
        if lab.get("OPEN_TIME") != c.get("open_time") or lab.get("CLOSE_TIME") != c.get(
            "close_time"
        ):
            stats["open_close_mismatch_vs_pm001"] += 1
        er = dict(r)
        er["open_time"] = c["open_time"]
        er["close_time"] = c["close_time"]
        er["STATUS"] = lab.get("STATUS")
        er["RESOLUTION"] = lab.get("RESOLUTION")
        er["_label"] = lab
        enriched.append(er)
    return enriched, stats


def build_sibling_index(enriched: list[dict]) -> dict[tuple, list[dict]]:
    """Key: (open_time, close_time, asset, rem) → mid rows passing TEST-007 excludes."""
    idx: dict[tuple, list[dict]] = defaultdict(list)
    for r in enriched:
        rem = r.get("time_remaining_sec")
        if rem not in TARGET_REMS | {300}:
            continue
        if r.get("implied_p_method") != "mid":
            continue
        if not accept_mid_row(r):
            continue
        if _is_void(r):
            continue
        y = resolve_y(r.get("RESOLUTION"))
        if y is None:
            continue
        key = (r["open_time"], r["close_time"], r["asset"], int(rem))
        idx[key].append(r)
    return idx


def collect_headline_rows(
    enriched: list[dict],
    sibling_mid_index: dict[tuple, list[dict]],
) -> tuple[dict[str, list[W2CRow]], dict[str, Any], dict[tuple[str, int], list[tuple[str, str, float]]]]:
    """Build scored headline rows with Clock-certified sibling join. Annex not scored."""
    cells: dict[str, list[W2CRow]] = {cid: [] for cid in HEADLINES}
    stats: dict[str, Any] = {
        "candidates": 0,
        "excluded_method_not_mid": 0,
        "excluded_near_deg": 0,
        "excluded_void_or_other": 0,
        "excluded_no_y": 0,
        "scored": 0,
        "n_speak": 0,
        "n_fail_closed_missing_sibling": 0,
        "per_cell": {
            cid: {
                "candidates": 0,
                "scored": 0,
                "speak": 0,
                "fail_closed": 0,
                "excluded_method_not_mid": 0,
                "excluded_near_deg": 0,
                "excluded_void": 0,
            }
            for cid in HEADLINES
        },
        "annex_dark_not_scored": ANNEX_DARK,
        "void_bucket": [],
    }

    # Pool for wrong-window placebo: usable sibling mids by (asset, rem)
    pool: dict[tuple[str, int], list[tuple[str, str, float]]] = defaultdict(list)
    for key, rows in sibling_mid_index.items():
        ot, ct, asset, rem = key
        for s in rows:
            pool[(asset, rem)].append((ot, ct, float(m_t_from_checkpoint(s))))

    for r in enriched:
        rem = r.get("time_remaining_sec")
        asset = r.get("asset")
        if rem not in TARGET_REMS or asset not in ("BTC", "ETH"):
            continue
        cell = primary_cell_id(asset, rem)
        # Only headlines scored; annex DARK
        if cell not in HEADLINES:
            continue
        cs = stats["per_cell"][cell]
        stats["candidates"] += 1
        cs["candidates"] += 1

        if r.get("implied_p_method") != "mid":
            stats["excluded_method_not_mid"] += 1
            cs["excluded_method_not_mid"] += 1
            continue
        if not accept_mid_row(r):
            stats["excluded_near_deg"] += 1
            cs["excluded_near_deg"] += 1
            continue
        if _is_void(r):
            stats["excluded_void_or_other"] += 1
            cs["excluded_void"] += 1
            stats["void_bucket"].append(
                {
                    "contract_id": r.get("contract_id"),
                    "resolution": r.get("RESOLUTION"),
                    "status": r.get("STATUS"),
                }
            )
            continue
        y = resolve_y(r.get("RESOLUTION"))
        if y is None:
            stats["excluded_no_y"] += 1
            cs["excluded_void"] += 1
            continue

        m_t = float(m_t_from_checkpoint(r))
        gate = gate_decision(cell, opts_in_annex=False)
        assert gate == "ALLOW_SPEAK_HEADLINE"

        sib_asset = SIBLING[asset]
        sib_key = (r["open_time"], r["close_time"], sib_asset, int(rem))
        cands = sibling_mid_index.get(sib_key, [])
        m_star: Optional[float] = None
        sib_cid: Optional[str] = None
        if cands:
            # Deterministic: unique expected; take first sorted by contract_id
            sib = sorted(cands, key=lambda x: x["contract_id"])[0]
            # Clock: same decision_time / rem required
            if (
                sib["decision_time"] == r["decision_time"]
                and sib["time_remaining_sec"] == r["time_remaining_sec"]
                and sib["open_time"] == r["open_time"]
                and sib["close_time"] == r["close_time"]
            ):
                m_star = float(m_t_from_checkpoint(sib))
                sib_cid = sib["contract_id"]
            # else treat as missing (look-ahead / mismatch) → fail-closed

        speak = m_star is not None and math.isfinite(m_star)
        if speak:
            stats["n_speak"] += 1
            cs["speak"] += 1
        else:
            stats["n_fail_closed_missing_sibling"] += 1
            cs["fail_closed"] += 1

        cells[cell].append(
            W2CRow(
                cell_id=cell,
                contract_id=r["contract_id"],
                sibling_contract_id=sib_cid,
                asset=asset,
                sibling_asset=sib_asset,
                checkpoint=KALSHI_REM_TO_LABEL[int(rem)],
                time_remaining_sec=int(rem),
                decision_time=r.get("decision_time") or "",
                open_time=r["open_time"],
                close_time=r["close_time"],
                m_t=m_t,
                m_star=m_star,
                y=y,
                gate=gate,
                speak=speak,
            )
        )
        stats["scored"] += 1
        cs["scored"] += 1

    return cells, stats, pool


def _fmt_num(x: Any, nd: int = 6) -> str:
    if x == "UNTESTED" or x is None:
        return "UNTESTED"
    if isinstance(x, float):
        return f"{x:.{nd}f}"
    return str(x)


def build_markdown(payload: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append(f"# {payload['TEST_ID']} — {payload['package']} vs {payload['incumbent']}")
    lines.append("")
    lines.append(f"**TEST_ID:** `{payload['TEST_ID']}`")
    lines.append(f"**Package:** `{payload['package']}`")
    lines.append(f"**Feature:** `{FEATURE_ID}` (sibling same-window mid blend, λ={LAMBDA_SCORED} frozen)")
    lines.append(f"**Gate:** `{GATE_ID}` (speak only on ALLOW_SPEAK_HEADLINE)")
    lines.append(f"**Incumbent:** `{payload['incumbent']}` (TEST-20260911-007 mid-only)")
    lines.append("**Purpose:** W2-C sibling-mid incrementality vs Kalshi mid on two AMD-005 headlines")
    lines.append(
        f"**DATA:** `{payload['data']['dataset_id']}` checkpoints + PM-001 OPEN/CLOSE + labels"
    )
    lines.append("**Join:** DATA_VERDICT_W2C_SIBLING_JOIN CLEARED (join only)")
    lines.append("**Slice use:** USED_RESEARCH — not validation, not sealed holdout")
    lines.append(f"**Overall verdict:** `{payload['overall_verdict']}`")
    lines.append(f"**invented_numbers:** `{payload['invented_numbers']}`")
    lines.append("**Trading:** FORBIDDEN")
    lines.append("**PM-002 / Poly / CF / L3 / EXPIRATION_VALUE:** not used")
    lines.append(f"**Annex `{ANNEX_DARK}`:** DARK — not scored as speak")
    lines.append(f"**Run UTC:** `{payload['run_utc']}`")
    lines.append(f"**SHA256 verified:** `{payload['data']['sha256_verified']}`")
    lines.append("")
    lines.append("## Authority")
    for a in payload["authority"]:
        lines.append(f"- `{a}`")
    lines.append("")
    lines.append("## Frozen map")
    lines.append(
        "- On ABSTAIN or missing sibling: p_t = m_t"
    )
    lines.append(
        f"- On ALLOW_SPEAK_HEADLINE: "
        f"p_t = clip((1-{LAMBDA_SCORED})*m_t + {LAMBDA_SCORED}*m*_t, {EPS}, 1-{EPS})"
    )
    lines.append(
        "- m*_t = opposite-asset same OPEN/CLOSE same rem mid (Clock-certified)"
    )
    lines.append(
        f"- Scored λ={LAMBDA_SCORED} only. Robustness λ∈{list(LAMBDA_ROBUST)} annex — do not pick winner."
    )
    lines.append("- λ=0 diagnostic must give Δ=0.")
    lines.append("")
    lines.append("## Filters / join")
    lines.append("- venue=KALSHI, window=15m; BTC/ETH **separate** (no pool)")
    lines.append("- DATA-PROV-PM-003 1208-slice only — **no** PM-002 union")
    lines.append("- `implied_p_method == mid` only; last-fallback excluded")
    lines.append("- exclude `implied_p ≤ 0.02` or `≥ 0.98` (near-deg) on **both** sides")
    lines.append("- VOID/DISPUTED out of scored N / sibling → missing")
    lines.append("- Sibling key: same OPEN_TIME + CLOSE_TIME + rem; same decision_time")
    lines.append("- Missing sibling → fail-closed p_t := m_t")
    lines.append("- No Poly. No CF. No L3. No EXPIRATION_VALUE. No in-sample refit.")
    lines.append("")
    lines.append(
        "**Sign convention:** ΔBrier = Brier_model − Brier_market; "
        "ΔLogLoss = LogLoss_model − LogLoss_market; **negative = skill** vs mid."
    )
    lines.append("")
    lines.append(
        f"**Skill rule:** both Δ < 0 on a headline. Kill if either Δ ≥ 0, N < {MIN_N_KILL}, "
        "or one headline works and the other inverts. Not NO_EDGE. Not Champion."
    )
    lines.append("")
    lines.append(f"## Overall reason")
    lines.append(payload["overall_reason"])
    lines.append("")
    lines.append("## Headlines (AMD-005, no pool)")
    lines.append("")
    lines.append(
        "| Cell | N | Brier_model | Brier_market | ΔBrier | LogLoss_model | "
        "LogLoss_market | ΔLogLoss | mean(m) | mean(p) | mean(m*) | ECE | Verdict |"
    )
    lines.append(
        "|------|--:|------------:|-------------:|-------:|--------------:|"
        "---------------:|---------:|--------:|--------:|---------:|-----|---------|"
    )
    for cid in HEADLINES:
        c = payload["headlines"][cid]
        lines.append(
            f"| `{cid}` | {c['N']} | {_fmt_num(c['Brier_model'])} | "
            f"{_fmt_num(c['Brier_market'])} | {_fmt_num(c['ΔBrier'])} | "
            f"{_fmt_num(c['LogLoss_model'])} | {_fmt_num(c['LogLoss_market'])} | "
            f"{_fmt_num(c['ΔLogLoss'])} | {_fmt_num(c['mean(m)'], 4)} | "
            f"{_fmt_num(c['mean(p)'], 4)} | {_fmt_num(c['mean(m*)'], 4)} | "
            f"{_fmt_num(c['ECE'])} | `{c['cell_verdict']}` |"
        )
    lines.append("")
    for cid in HEADLINES:
        c = payload["headlines"][cid]
        lines.append(f"### `{cid}`")
        lines.append(f"- n_speak={c['n_speak']}; fail_closed_missing_sibling={c['n_fail_closed_missing_sibling']}")
        lines.append(f"- Reason: {c['cell_reason']}")
        lines.append(f"- Calibration: {c['Calibration']['note']}")
        lines.append(f"- ECE_market: {_fmt_num(c.get('ECE_market'))}")
        lines.append("- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no trading)")
        lines.append("")

    lines.append("## Robustness annex (λ∈{0.15,0.25,0.35}; not headline; do not pick winner)")
    lines.append("")
    lines.append("| Cell | λ | N | ΔBrier | ΔLogLoss | Verdict |")
    lines.append("|------|--:|--:|-------:|---------:|---------|")
    for cid in HEADLINES:
        for lam_s, block in payload["robustness"][cid].items():
            lines.append(
                f"| `{cid}` | {lam_s} | {block['N']} | {_fmt_num(block['ΔBrier'])} | "
                f"{_fmt_num(block['ΔLogLoss'])} | `{block['cell_verdict']}` |"
            )
    lines.append("")
    lines.append("## Placebos (report, not headline switch)")
    lines.append("")
    lines.append("| Placebo | Cell | N | ΔBrier | ΔLogLoss | Notes |")
    lines.append("|---------|------|--:|-------:|---------:|-------|")
    for name, by_cell in payload["placebos"].items():
        for cid in HEADLINES:
            block = by_cell[cid]
            note = block.get("placebo_note", "")
            lines.append(
                f"| `{name}` | `{cid}` | {block['N']} | {_fmt_num(block['ΔBrier'])} | "
                f"{_fmt_num(block['ΔLogLoss'])} | {note} |"
            )
    lines.append("")
    lines.append(f"- placebo_seed: `{PLACEBO_SEED}`")
    lines.append(
        "- λ=0 must give ΔBrier=0 and ΔLogLoss=0 (identity vs mid)."
    )
    lines.append("")
    lines.append("## Filter / join stats")
    lines.append("```json")
    filt = {k: v for k, v in payload["filter_stats"].items() if k != "void_bucket"}
    lines.append(json.dumps(filt, indent=2))
    lines.append("```")
    lines.append("")
    lines.append("## Integrity")
    lines.append("")
    lines.append(f"- checkpoints.ndjson sha256: `{payload['data']['checkpoints_sha256']}`")
    lines.append(f"- expected: `{payload['data']['checkpoints_sha256_expected']}`")
    lines.append(f"- sha256_verified: `{payload['data']['sha256_verified']}`")
    lines.append(f"- venues: `{payload['data']['venue_check']['venues']}`")
    lines.append("- PM-002 / Poly / CF / L3 / EXPIRATION_VALUE: **not used**")
    lines.append("- m_t / m*: PM-003 checkpoint mid only")
    lines.append("- No λ retune; no gate retune; no annex sneak; no pool")
    lines.append("")
    lines.append("## Overall package verdict")
    lines.append(f"**`{payload['overall_verdict']}`** — {payload['overall_reason']}")
    lines.append("")
    lines.append(
        "FAIL-INSUFFICIENT ≠ NO_EDGE. This is **not** a Champion / strategy PASS. "
        "No trading authorization. Holdout closed."
    )
    lines.append("")
    lines.append("## Artifacts")
    for p in payload["artifact_paths"]:
        lines.append(f"- `{p}`")
    lines.append("")
    return "\n".join(lines)


def _write_integrity_fail(reason: str) -> int:
    run_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out_stem = f"{TEST_ID}-{PACKAGE}"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_TESTS.mkdir(parents=True, exist_ok=True)
    ARCHIVE_AUDIT.mkdir(parents=True, exist_ok=True)
    payload = {
        "TEST_ID": TEST_ID,
        "package": PACKAGE,
        "overall_verdict": "DATA_INTEGRITY_FAIL",
        "overall_reason": reason,
        "invented_numbers": False,
        "trading": "FORBIDDEN",
        "run_utc": run_utc,
        "authority": AUTHORITY,
    }
    out_json = OUT_DIR / f"{out_stem}.json"
    out_md = OUT_DIR / f"{out_stem}.md"
    out_json.write_text(json.dumps(payload, indent=2) + "\n")
    out_md.write_text(
        f"# {TEST_ID} — DATA_INTEGRITY_FAIL\n\n"
        f"{reason}\n\ninvented_numbers: false\nTrading: FORBIDDEN\n"
    )
    (ARCHIVE_TESTS / f"{out_stem}.json").write_text(out_json.read_text())
    (ARCHIVE_TESTS / f"{out_stem}.md").write_text(out_md.read_text())
    print(f"DATA_INTEGRITY_FAIL: {reason}", file=sys.stderr)
    return 2


def main() -> int:
    assert_no_pm001_price_as_mt(["implied_p"])

    try:
        digest = verify_checkpoints_sha256(CHECKPOINTS)
    except DataIntegrityError as e:
        return _write_integrity_fail(str(e))

    checkpoints = _load_ndjson(CHECKPOINTS)
    try:
        venue_check = assert_kalshi_only(checkpoints)
    except DataIntegrityError as e:
        return _write_integrity_fail(str(e))

    coverage = _load_ndjson(COVERAGE)
    kalshi_labels = _load_ndjson(KALSHI_LABELS)
    kalshi_idx = _index_labels(kalshi_labels)

    enriched, enrich_stats = enrich_checkpoints(checkpoints, coverage, kalshi_idx)
    sibling_idx = build_sibling_index(enriched)
    cells, filt, pool = collect_headline_rows(enriched, sibling_idx)
    filt["enrich"] = enrich_stats

    map_label = (
        f"p=clip((1-{LAMBDA_SCORED})*m + {LAMBDA_SCORED}*m_star, {EPS}, 1-{EPS}) "
        f"on ALLOW_SPEAK_HEADLINE; else p=m"
    )

    headlines: dict[str, Any] = {}
    for cid in HEADLINES:
        rows = cells[cid]
        # Stable order for scoring / placebos
        rows = sorted(rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec))
        cells[cid] = rows
        p = apply_map(rows, lam=LAMBDA_SCORED)
        headlines[cid] = score_forecast(
            rows, p, feature_id=FEATURE_ID, map_label=map_label
        )

    # Robustness annex — do not pick winner
    robustness: dict[str, Any] = {}
    for cid in HEADLINES:
        robustness[cid] = {}
        for lam in LAMBDA_ROBUST:
            p = apply_map(cells[cid], lam=lam)
            robustness[cid][str(lam)] = score_forecast(
                cells[cid],
                p,
                feature_id=FEATURE_ID,
                map_label=f"robustness λ={lam} (annex only)",
            )

    # Placebos
    placebos: dict[str, Any] = {
        "shuffle_mstar_within_cell": {},
        "lambda_0": {},
        "wrong_window_sibling": {},
    }
    for cid in HEADLINES:
        rows = cells[cid]
        # shuffle
        p_shuf = placebo_shuffle_mstar(rows, cid)
        ordered = sorted(
            rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec)
        )
        sh = score_forecast(
            ordered,
            p_shuf,
            feature_id=FEATURE_ID,
            map_label="placebo: shuffle m* within cell",
        )
        sh["placebo_note"] = "m* shuffled within cell; m fixed"
        placebos["shuffle_mstar_within_cell"][cid] = sh

        # λ=0
        p0 = placebo_lambda_zero(rows)
        z = score_forecast(
            rows, p0, feature_id=FEATURE_ID, map_label="placebo: λ=0 (must Δ=0)"
        )
        db = z["ΔBrier"]
        dll = z["ΔLogLoss"]
        ok0 = (
            isinstance(db, float)
            and isinstance(dll, float)
            and abs(db) < 1e-15
            and abs(dll) < 1e-15
        )
        z["placebo_note"] = f"λ=0 identity check pass={ok0}"
        z["lambda0_delta_zero"] = ok0
        placebos["lambda_0"][cid] = z

        # wrong window
        p_wrong = placebo_wrong_window(rows, pool)
        w = score_forecast(
            ordered,
            p_wrong,
            feature_id=FEATURE_ID,
            map_label="placebo: wrong-window sibling",
        )
        w["placebo_note"] = "opposite-asset same rem, different OPEN/CLOSE"
        placebos["wrong_window_sibling"][cid] = w

    overall, reason = package_verdict(headlines)
    run_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out_stem = f"{TEST_ID}-{PACKAGE}"
    out_json = OUT_DIR / f"{out_stem}.json"
    out_md = OUT_DIR / f"{out_stem}.md"

    payload: dict[str, Any] = {
        "TEST_ID": TEST_ID,
        "package": PACKAGE,
        "feature": FEATURE_ID,
        "gate": GATE_ID,
        "incumbent": INCUMBENT,
        "purpose": "w2c_sibling_mid_incrementality_vs_kalshi_mid",
        "lambda_scored": LAMBDA_SCORED,
        "lambda_robustness_annex": list(LAMBDA_ROBUST),
        "eps": EPS,
        "annex_dark": ANNEX_DARK,
        "trading": "FORBIDDEN",
        "invented_numbers": False,
        "overall_verdict": overall,
        "overall_reason": reason,
        "run_utc": run_utc,
        "authority": AUTHORITY,
        "data": {
            "dataset_id": "DATA-PROV-PM-003",
            "slice_use": "USED_RESEARCH",
            "checkpoints": str(CHECKPOINTS),
            "checkpoints_sha256": digest,
            "checkpoints_sha256_expected": EXPECTED_CHECKPOINTS_SHA256,
            "sha256_verified": digest == EXPECTED_CHECKPOINTS_SHA256,
            "coverage": str(COVERAGE),
            "labels_kalshi": str(KALSHI_LABELS),
            "labels_poly": None,
            "m_t_source": "DATA-PROV-PM-003 derived checkpoints.implied_p (mid)",
            "m_star_source": "opposite-asset same OPEN/CLOSE same rem mid (Clock CLEARED join)",
            "forbidden_m_t": ["LAST_PRICE_DOLLARS", "OUTCOME_PRICES", "EXPIRATION_VALUE"],
            "pm002_checkpoints_read": False,
            "poly_scored": False,
            "cf_used": False,
            "l3_used": False,
            "venue_check": venue_check,
            "join_verdict": "CLEARED",
            "join_verdict_path": "data/DATA-PROV-PM-003/provenance/DATA_VERDICT_W2C_SIBLING_JOIN.md",
        },
        "headlines": headlines,
        "headline_order": list(HEADLINES),
        "robustness": robustness,
        "placebos": placebos,
        "placebo_seed": PLACEBO_SEED,
        "filter_stats": {
            **{k: v for k, v in filt.items() if k != "void_bucket"},
            "void_bucket_n": len(filt["void_bucket"]),
            "void_bucket": filt["void_bucket"],
        },
        "sign_conventions": {
            "ΔBrier": "Brier_model − Brier_market; negative = skill vs mid",
            "ΔLogLoss": "LogLoss_model − LogLoss_market; negative = skill vs mid",
            "skill": "both Δ < 0 required; either Δ ≥ 0 → REDUNDANT / FAIL-INSUFFICIENT",
            "N_kill": MIN_N_KILL,
            "not": ["NO_EDGE", "Champion"],
        },
        "forbidden": [
            "retune λ or gate",
            "raw 0/1",
            "T−1 incumbent",
            "CF/L3",
            "EXPIRATION_VALUE",
            "PM-002 union",
            "Poly",
            "annex sneak / pool",
            "trading",
            "invented numbers",
        ],
        "artifact_paths": [],
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_TESTS.mkdir(parents=True, exist_ok=True)
    ARCHIVE_AUDIT.mkdir(parents=True, exist_ok=True)

    arch_json = ARCHIVE_TESTS / f"{out_stem}.json"
    arch_md = ARCHIVE_TESTS / f"{out_stem}.md"
    arch_short_json = ARCHIVE_TESTS / f"{TEST_ID}.json"
    arch_short_md = ARCHIVE_TESTS / f"{TEST_ID}.md"
    audit_path = ARCHIVE_AUDIT / f"2026-09-13-{TEST_ID}-{PACKAGE}-examiner.md"

    payload["artifact_paths"] = [
        str(out_json),
        str(out_md),
        str(arch_json),
        str(arch_md),
        str(arch_short_json),
        str(arch_short_md),
        str(audit_path),
    ]

    out_json.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n")
    md = build_markdown(payload)
    out_md.write_text(md)
    arch_json.write_text(out_json.read_text())
    arch_md.write_text(md)
    arch_short_json.write_text(
        json.dumps(
            {
                "TEST_ID": TEST_ID,
                "package": PACKAGE,
                "verdict": overall,
                "invented_numbers": False,
                "trading": "FORBIDDEN",
                "full": str(arch_json),
            },
            indent=2,
        )
        + "\n"
    )
    arch_short_md.write_text(
        f"# {TEST_ID}\n"
        f"**Package:** {PACKAGE} · **Verdict:** `{overall}`\n"
        f"See `{out_stem}.md` for full card.\n"
    )
    audit_path.write_text(
        "# Audit pointer\n\n"
        f"- TEST: `{TEST_ID}`\n"
        f"- Package: `{PACKAGE}` vs `{INCUMBENT}`\n"
        f"- Feature: `{FEATURE_ID}` · Gate: `{GATE_ID}`\n"
        f"- Headlines: `{HEADLINE_A}`, `{HEADLINE_B}`\n"
        f"- Annex `{ANNEX_DARK}`: DARK\n"
        f"- Verdict: `{overall}`\n"
        f"- invented_numbers: false\n"
        f"- Trading: FORBIDDEN\n"
        f"- SHA256 verified: `{digest}`\n"
        f"- PM-002 / Poly / CF / L3: not used\n"
        f"- Join: DATA_VERDICT_W2C_SIBLING_JOIN CLEARED\n"
        f"- Artifacts: `{out_json}`\n"
        f"- Archive: `{arch_json}`\n"
        f"- DATA: DATA-PROV-PM-003 checkpoints + PM-001 OPEN/CLOSE + labels\n"
        f"- Purpose: W2-C sibling-mid incrementality vs mid (USED_RESEARCH; not validation)\n"
    )

    print(f"TEST_ID={TEST_ID}")
    print(f"overall_verdict={overall}")
    print(f"sha256_verified={digest}")
    for cid in HEADLINES:
        c = headlines[cid]
        print(
            f"HEADLINE\t{cid}\tN={c['N']}\t"
            f"dB={c['ΔBrier']}\tdLL={c['ΔLogLoss']}\t"
            f"mean_mstar={c['mean(m*)']}\tverdict={c['cell_verdict']}"
        )
    for cid in HEADLINES:
        z = placebos["lambda_0"][cid]
        print(f"PLACEBO_λ0\t{cid}\tdB={z['ΔBrier']}\tdLL={z['ΔLogLoss']}\tok={z['lambda0_delta_zero']}")
    print(f"wrote {out_json}")
    print(f"wrote {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
