#!/usr/bin/env python3
"""TEST — PM-002 MARKET BASELINE Examiner.

Venue calibration of m_t vs official resolution. No strategy. No model p_t.
Trading forbidden. invented_numbers=false.
"""

from __future__ import annotations

import hashlib
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.pm002_market_baseline import (  # noqa: E402
    PRIMARY_ASSETS,
    PRIMARY_REMS,
    ScoredRow,
    accept_mid_row,
    accept_poly_last_row,
    assert_no_pm001_price_as_mt,
    m_t_from_checkpoint,
    poly_checkpoint_label,
    primary_cell_id,
    resolve_y,
    score_cell,
    KALSHI_REM_TO_LABEL,
)

LAB = Path("/workspace/lab")
CHECKPOINTS = LAB / "data/DATA-PROV-PM-002/derived/checkpoints.ndjson"
KALSHI_LABELS = LAB / "data/DATA-PROV-PM-001/normalized/kalshi_15m_btc_eth_resolved.ndjson"
POLY_LABELS = LAB / "data/DATA-PROV-PM-001/normalized/polymarket_global_5m_15m_btc_eth_resolved.ndjson"
OUT_DIR = LAB / "harness/examiner/out"
ARCHIVE_TESTS = LAB / "archive/tests"
ARCHIVE_AUDIT = LAB / "archive/audit"

TEST_ID = "TEST-20260911-006"
PACKAGE = "PM002-MARKET-BASELINE"

AUTHORITY = [
    "governance/EXAMINER_ORDER_PM002_MARKET_BASELINE.md",
    "governance/PM002_COVERAGE_FROZEN_2026-09-11.md",
    "governance/BINARY_EXAMINER_SPEC.md",
    "data/DATA-PROV-PM-002/provenance/DATA_VERDICT_DATA-PROV-PM-002.md",
]


def _load_ndjson(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


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


def collect_primary(checkpoints: list[dict], kalshi_idx: dict) -> tuple[dict[str, list[ScoredRow]], dict[str, Any]]:
    cells: dict[str, list[ScoredRow]] = {
        primary_cell_id(a, rem): [] for a in PRIMARY_ASSETS for rem in PRIMARY_REMS
    }
    stats = {
        "candidates": 0,
        "excluded_method_not_mid": 0,
        "excluded_near_deg": 0,
        "excluded_no_label": 0,
        "excluded_void_or_other": 0,
        "scored": 0,
        "void_bucket": [],
    }
    for r in checkpoints:
        if r.get("venue") != "KALSHI" or r.get("window") != "15m":
            continue
        rem = r.get("time_remaining_sec")
        if rem not in PRIMARY_REMS:
            continue
        asset = r.get("asset")
        if asset not in PRIMARY_ASSETS:
            continue
        stats["candidates"] += 1
        if r.get("implied_p_method") != "mid":
            stats["excluded_method_not_mid"] += 1
            continue
        if not accept_mid_row(r):
            stats["excluded_near_deg"] += 1
            continue
        lab = _join_label(r, kalshi_idx)
        if lab is None:
            stats["excluded_no_label"] += 1
            continue
        # m_t from checkpoint implied_p only (never PM-001 terminal prices)
        m_t = m_t_from_checkpoint(r)
        y = resolve_y(lab.get("RESOLUTION"))
        if y is None:
            stats["excluded_void_or_other"] += 1
            stats["void_bucket"].append(
                {
                    "contract_id": r.get("contract_id"),
                    "resolution": lab.get("RESOLUTION"),
                    "status": lab.get("STATUS"),
                }
            )
            continue
        cell = primary_cell_id(asset, rem)
        cells[cell].append(
            ScoredRow(
                cell_id=cell,
                contract_id=r["contract_id"],
                venue="KALSHI",
                asset=asset,
                window="15m",
                checkpoint=KALSHI_REM_TO_LABEL[rem],
                time_remaining_sec=int(rem),
                decision_time=r.get("decision_time") or "",
                m_t=m_t,
                implied_p_method="mid",
                y=y,
                resolution=lab["RESOLUTION"],
            )
        )
        stats["scored"] += 1
    return cells, stats


def collect_kalshi_t1m_annex(checkpoints: list[dict], kalshi_idx: dict) -> dict[str, list[ScoredRow]]:
    cells: dict[str, list[ScoredRow]] = {}
    for asset in PRIMARY_ASSETS:
        cell = f"KALSHI|15m|{asset}|T-1m|mid"
        cells[cell] = []
        for r in checkpoints:
            if r.get("venue") != "KALSHI" or r.get("window") != "15m":
                continue
            if r.get("asset") != asset or r.get("time_remaining_sec") != 60:
                continue
            if not accept_mid_row(r):
                continue
            lab = _join_label(r, kalshi_idx)
            if lab is None:
                continue
            y = resolve_y(lab.get("RESOLUTION"))
            if y is None:
                continue
            m_t = m_t_from_checkpoint(r)
            cells[cell].append(
                ScoredRow(
                    cell_id=cell,
                    contract_id=r["contract_id"],
                    venue="KALSHI",
                    asset=asset,
                    window="15m",
                    checkpoint="T-1m",
                    time_remaining_sec=60,
                    decision_time=r.get("decision_time") or "",
                    m_t=m_t,
                    implied_p_method="mid",
                    y=y,
                    resolution=lab["RESOLUTION"],
                )
            )
    return cells


def collect_poly_annex(checkpoints: list[dict], poly_idx: dict) -> dict[str, list[ScoredRow]]:
    cells: dict[str, list[ScoredRow]] = defaultdict(list)
    for r in checkpoints:
        if not accept_poly_last_row(r):
            continue
        lab = _join_label(r, poly_idx)
        if lab is None:
            continue
        y = resolve_y(lab.get("RESOLUTION"))
        if y is None:
            continue
        m_t = m_t_from_checkpoint(r)
        window = r.get("window") or ""
        rem = int(r["time_remaining_sec"])
        ck = poly_checkpoint_label(window, rem)
        cell = f"POLYMARKET_GLOBAL|{window}|{r['asset']}|{ck}|last"
        cells[cell].append(
            ScoredRow(
                cell_id=cell,
                contract_id=r["contract_id"],
                venue="POLYMARKET_GLOBAL",
                asset=r["asset"],
                window=window,
                checkpoint=ck,
                time_remaining_sec=rem,
                decision_time=r.get("decision_time") or "",
                m_t=m_t,
                implied_p_method="last",
                y=y,
                resolution=lab["RESOLUTION"],
            )
        )
    return dict(cells)


def _fmt_ci(ci: Any) -> str:
    if ci == "UNTESTED" or ci is None:
        return "UNTESTED"
    if isinstance(ci, dict):
        return f"[{ci['low']:.4f}, {ci['high']:.4f}] (Wilson 95%)"
    return str(ci)


def _fmt_num(x: Any, nd: int = 6) -> str:
    if x == "UNTESTED" or x is None:
        return "UNTESTED"
    if isinstance(x, float):
        return f"{x:.{nd}f}"
    return str(x)


def build_markdown(payload: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append(f"# {payload['TEST_ID']} — PM-002 MARKET BASELINE")
    lines.append("")
    lines.append(f"**TEST_ID:** `{payload['TEST_ID']}`")
    lines.append(f"**Package:** `{payload['package']}`")
    lines.append("**Purpose:** venue calibration of $m_t$ — **not** a strategy")
    lines.append(f"**DATA:** `{payload['data']['dataset_id']}` checkpoints + PM-001 resolution labels")
    lines.append(f"**Overall verdict:** `{payload['overall_verdict']}`")
    lines.append(f"**invented_numbers:** `{payload['invented_numbers']}`")
    lines.append("**Trading:** FORBIDDEN")
    lines.append("**Model p_t:** none (UNTESTED for all model metrics)")
    lines.append(f"**Run UTC:** `{payload['run_utc']}`")
    lines.append("")
    lines.append("## Authority")
    for a in payload["authority"]:
        lines.append(f"- `{a}`")
    lines.append("")
    lines.append("## Filters (primary)")
    lines.append("- venue=KALSHI, window=15m, assets BTC/ETH separate")
    lines.append("- checkpoints: T-14m (rem≈840), T-10m (rem≈600), T-5m (rem≈300) — labels from rem map; actual rem values verified in data")
    lines.append("- `implied_p_method == mid` only; exclude last-fallback")
    lines.append("- exclude `implied_p ≤ 0.02` or `≥ 0.98`")
    lines.append("- VOID/DISPUTED out of scored N (void bucket separate)")
    lines.append("- **Do not** use PM-001 `LAST_PRICE_DOLLARS` / `OUTCOME_PRICES` as $m_t$")
    lines.append("- Never pool Kalshi+Poly; never score Poly as mid")
    lines.append("")
    lines.append("## WR definition (descriptive only)")
    lines.append("`mid > 0.5` ⇒ YES prediction; `mid < 0.5` ⇒ NO; `mid == 0.5` excluded from WR denominator. **Not a skill claim.**")
    lines.append("")
    lines.append("## Primary cells")
    lines.append("")
    lines.append(
        "| Cell | N | WR | CI | Brier_market | LogLoss_market | mean(m_t) | Calibration note | Verdict |"
    )
    lines.append("|------|--:|---:|----|-------------:|---------------:|----------:|------------------|---------|")
    for cell_id in payload["primary_cell_order"]:
        c = payload["primary_cells"][cell_id]
        lines.append(
            f"| `{cell_id}` | {c['N']} | {_fmt_num(c['WR'], 4)} | {_fmt_ci(c['CI'])} | "
            f"{_fmt_num(c['Brier_market'])} | {_fmt_num(c['LogLoss_market'])} | "
            f"{_fmt_num(c['mean(m_t)'], 4)} | {c['Calibration']['note']} | `{c['cell_verdict']}` |"
        )
    lines.append("")
    lines.append("### Reliability tables (pre-registered bins; thin → UNTESTED, not pooled)")
    lines.append("")
    for cell_id in payload["primary_cell_order"]:
        c = payload["primary_cells"][cell_id]
        lines.append(f"#### `{cell_id}`")
        lines.append("")
        lines.append("| Bin | n | mean_m | obs_rate | CI |")
        lines.append("|-----|--:|-------:|---------:|----|")
        for b in c["Calibration"]["reliability_table"]["bins"]:
            lines.append(
                f"| {b['bin']} | {b['n']} | {_fmt_num(b.get('mean_m'), 4)} | "
                f"{_fmt_num(b.get('obs_rate'), 4)} | {_fmt_ci(b.get('CI'))} |"
            )
        lines.append(f"- ECE: `{_fmt_num(c['Calibration']['ECE'])}`")
        lines.append("")
    lines.append("## UNTESTED keys (no model / no strategy)")
    lines.append(
        "Brier_model, LogLoss_model, ΔBrier, ΔLogLoss, gap, EV_gross, EV_net, "
        "abstention_rate, cost_sensitivity — all **UNTESTED** on every cell."
    )
    lines.append("")
    lines.append("## Filter / join stats (primary)")
    lines.append("```json")
    lines.append(json.dumps(payload["primary_filter_stats"], indent=2))
    lines.append("```")
    lines.append("")
    lines.append("## Annex A — Poly last-print non-T−0 (weaker; NOT mid)")
    lines.append("")
    lines.append("Scored as last-print benchmark only. Lag caveat per Clock. Never pooled with Kalshi.")
    lines.append("")
    lines.append("| Cell | N | WR | Brier_market | LogLoss_market | mean(m_t) | Verdict |")
    lines.append("|------|--:|---:|-------------:|---------------:|----------:|---------|")
    for cell_id in sorted(payload["annex_poly"].keys()):
        c = payload["annex_poly"][cell_id]
        lines.append(
            f"| `{cell_id}` | {c['N']} | {_fmt_num(c['WR'], 4)} | "
            f"{_fmt_num(c['Brier_market'])} | {_fmt_num(c['LogLoss_market'])} | "
            f"{_fmt_num(c['mean(m_t)'], 4)} | `{c['cell_verdict']}` |"
        )
    lines.append("")
    lines.append("## Annex B — Kalshi T−1m mid (CLEARED_WITH_STRONG_CAVEAT)")
    lines.append("")
    lines.append("High near-degeneracy at T−1m; last-fallback excluded. Optional annex only.")
    lines.append("")
    lines.append("| Cell | N | WR | Brier_market | LogLoss_market | mean(m_t) | Verdict |")
    lines.append("|------|--:|---:|-------------:|---------------:|----------:|---------|")
    for cell_id in sorted(payload["annex_kalshi_t1m"].keys()):
        c = payload["annex_kalshi_t1m"][cell_id]
        lines.append(
            f"| `{cell_id}` | {c['N']} | {_fmt_num(c['WR'], 4)} | "
            f"{_fmt_num(c['Brier_market'])} | {_fmt_num(c['LogLoss_market'])} | "
            f"{_fmt_num(c['mean(m_t)'], 4)} | `{c['cell_verdict']}` |"
        )
    lines.append("")
    lines.append("## Overall package verdict")
    lines.append(f"**`{payload['overall_verdict']}`** — {payload['overall_reason']}")
    lines.append("")
    lines.append("This is **not** a strategy PASS. No trading authorization.")
    lines.append("")
    lines.append("## Artifacts")
    for p in payload["artifact_paths"]:
        lines.append(f"- `{p}`")
    lines.append("")
    lines.append(f"checkpoints.ndjson sha256: `{payload['data']['checkpoints_sha256']}`")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    assert_no_pm001_price_as_mt(["implied_p"])  # allowed source field
    checkpoints = _load_ndjson(CHECKPOINTS)
    kalshi_labels = _load_ndjson(KALSHI_LABELS)
    poly_labels = _load_ndjson(POLY_LABELS)
    kalshi_idx = _index_labels(kalshi_labels)
    poly_idx = _index_labels(poly_labels)

    primary_rows, filt = collect_primary(checkpoints, kalshi_idx)
    primary_scores = {cid: score_cell(rows) for cid, rows in primary_rows.items()}
    # Stable order
    primary_order = [
        primary_cell_id(a, rem) for rem in PRIMARY_REMS for a in PRIMARY_ASSETS
    ]

    annex_t1 = {cid: score_cell(rows) for cid, rows in collect_kalshi_t1m_annex(checkpoints, kalshi_idx).items()}
    annex_poly = {cid: score_cell(rows) for cid, rows in collect_poly_annex(checkpoints, poly_idx).items()}

    all_under = all(primary_scores[c]["underpowered_calibration"] for c in primary_order)
    any_n = any(primary_scores[c]["N"] > 0 for c in primary_order)
    if not any_n:
        overall = "FAIL-INSUFFICIENT"
        reason = "No scored primary decision-events."
    elif all_under:
        overall = "FAIL-INSUFFICIENT"
        reason = (
            "All six primary cells underpowered for named calibration "
            "(thin reliability bins / ECE). Descriptive WR/Brier/LogLoss/mean(m_t) "
            "are MEASURED where N>0; powered calibration claim not supported. "
            "NOT NO_EDGE."
        )
    else:
        overall = "BASELINE_MEASURED"
        reason = "At least one primary cell supports powered calibration metrics; package is honest baseline measurement (not strategy PASS)."

    run_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out_stem = f"{TEST_ID}-{PACKAGE}"
    out_json = OUT_DIR / f"{out_stem}.json"
    out_md = OUT_DIR / f"{out_stem}.md"

    payload: dict[str, Any] = {
        "TEST_ID": TEST_ID,
        "package": PACKAGE,
        "purpose": "market_baseline_m_t_calibration",
        "strategy": None,
        "model_p_t": None,
        "trading": "FORBIDDEN",
        "invented_numbers": False,
        "overall_verdict": overall,
        "overall_reason": reason,
        "run_utc": run_utc,
        "authority": AUTHORITY,
        "data": {
            "dataset_id": "DATA-PROV-PM-002",
            "checkpoints": str(CHECKPOINTS),
            "checkpoints_sha256": _sha256_file(CHECKPOINTS),
            "labels_kalshi": str(KALSHI_LABELS),
            "labels_poly": str(POLY_LABELS),
            "m_t_source": "DATA-PROV-PM-002 derived checkpoints.implied_p (mid)",
            "forbidden_m_t": ["LAST_PRICE_DOLLARS", "OUTCOME_PRICES"],
        },
        "primary_cell_order": primary_order,
        "primary_cells": primary_scores,
        "primary_filter_stats": {
            **{k: v for k, v in filt.items() if k != "void_bucket"},
            "void_bucket_n": len(filt["void_bucket"]),
            "void_bucket": filt["void_bucket"],
        },
        "annex_poly": annex_poly,
        "annex_kalshi_t1m": annex_t1,
        "annex_notes": {
            "poly": "CLEARED_WEAKER_LAST_PRINT — never score as mid; never pool with Kalshi",
            "kalshi_t1m": "CLEARED_WITH_STRONG_CAVEAT — high near-deg; mid only",
        },
        "sign_conventions": {
            "ΔBrier": "Brier_model − Brier_market (UNTESTED — no model)",
            "ΔLogLoss": "LogLoss_model − LogLoss_market (UNTESTED — no model)",
            "WR": "descriptive mid>0.5⇒YES; not skill",
            "LogLoss_eps": 1e-15,
        },
        "artifact_paths": [],
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_TESTS.mkdir(parents=True, exist_ok=True)
    ARCHIVE_AUDIT.mkdir(parents=True, exist_ok=True)

    md = build_markdown(payload)
    # Write JSON without huge contract id lists duplicated in md path refs first
    arch_json = ARCHIVE_TESTS / f"{out_stem}.json"
    arch_md = ARCHIVE_TESTS / f"{out_stem}.md"
    # Also short pointer copies like prior TESTs
    arch_short_json = ARCHIVE_TESTS / f"{TEST_ID}.json"
    arch_short_md = ARCHIVE_TESTS / f"{TEST_ID}.md"

    payload["artifact_paths"] = [
        str(out_json),
        str(out_md),
        str(arch_json),
        str(arch_md),
        str(arch_short_json),
        str(arch_short_md),
    ]

    out_json.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n")
    # rebuild md with artifact paths filled
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
                "full": str(arch_json),
            },
            indent=2,
        )
        + "\n"
    )
    arch_short_md.write_text(
        f"# {TEST_ID}\n\n"
        f"PACKAGE `{PACKAGE}` verdict `{overall}`\n"
        f"invented_numbers: false\n"
        f"Full: `{arch_md}`\n"
    )

    audit_path = ARCHIVE_AUDIT / f"2026-09-11-{TEST_ID}-{PACKAGE}-examiner.md"
    audit_path.write_text(
        "# Audit pointer\n\n"
        f"- TEST: `{TEST_ID}`\n"
        f"- Package: `{PACKAGE}`\n"
        f"- Verdict: `{overall}`\n"
        f"- invented_numbers: false\n"
        f"- Trading: FORBIDDEN\n"
        f"- Artifacts: `{out_json}`\n"
        f"- Archive: `{arch_json}`\n"
        f"- DATA: DATA-PROV-PM-002 + PM-001 labels\n"
        f"- Purpose: market baseline m_t (no strategy / no model)\n"
    )
    payload["artifact_paths"].append(str(audit_path))
    # refresh json with audit path
    out_json.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n")
    arch_json.write_text(out_json.read_text())

    print(f"TEST_ID={TEST_ID}")
    print(f"overall_verdict={overall}")
    for cid in primary_order:
        c = primary_scores[cid]
        print(
            f"{cid}\tN={c['N']}\tWR={c['WR']}\tBrier={c['Brier_market']}\t"
            f"LL={c['LogLoss_market']}\tmean_m={c['mean(m_t)']}\tverdict={c['cell_verdict']}"
        )
    print(f"wrote {out_json}")
    print(f"wrote {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
