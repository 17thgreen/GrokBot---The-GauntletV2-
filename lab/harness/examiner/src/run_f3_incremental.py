#!/usr/bin/env python3
"""TEST-20260912-001 — F3-INCREMENTAL vs MKT-KALSHI-15M-MID.

Atomic incrementality of FEAT-20260912-003 and FEAT-20260912-004
versus frozen Kalshi mid on DATA-PROV-PM-003. No MLE. No ensemble.
No PM-002. No Poly. No trading. invented_numbers=false.
"""

from __future__ import annotations

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.f3_incremental import (  # noqa: E402
    ALL_CELLS,
    ANNEX_CELLS,
    FEAT003_S0,
    FEAT003_S0_ROBUST,
    FEAT004_EPS,
    FEAT004_KAPPA,
    FEAT004_KAPPA_ROBUST,
    PLACEBO_SEED,
    PRIMARY_CELL,
    FeatRow,
    apply_feat003,
    apply_feat004,
    placebo_shuffle_s,
    placebo_signflip_delta,
    rows_for_feat003,
    rows_for_feat004,
    score_forecast,
)
from src.pm003_market_baseline import (  # noqa: E402
    EXPECTED_CHECKPOINTS_SHA256,
    KALSHI_REM_TO_LABEL,
    PRIMARY_ASSETS,
    PRIMARY_REMS,
    DataIntegrityError,
    accept_mid_row,
    assert_kalshi_only,
    assert_no_pm001_price_as_mt,
    m_t_from_checkpoint,
    primary_cell_id,
    resolve_y,
    verify_checkpoints_sha256,
)

LAB = Path("/workspace/lab")
CHECKPOINTS = LAB / "data/DATA-PROV-PM-003/derived/checkpoints.ndjson"
KALSHI_LABELS = LAB / "data/DATA-PROV-PM-001/normalized/kalshi_15m_btc_eth_resolved.ndjson"
OUT_DIR = LAB / "harness/examiner/out"
ARCHIVE_TESTS = LAB / "archive/tests"
ARCHIVE_AUDIT = LAB / "archive/audit"

TEST_ID = "TEST-20260912-001"
PACKAGE = "F3-INCREMENTAL"
INCUMBENT = "MKT-KALSHI-15M-MID"

AUTHORITY = [
    "governance/EXAMINER_ORDER_TEST-20260912-001-F3.md",
    "archive/features/FEAT-20260912-003.md",
    "archive/features/FEAT-20260912-004.md",
    "governance/FEATURE_WAVE_001_2026-09-12.md",
    "governance/BINARY_EXAMINER_SPEC.md",
    "harness/examiner/src/pm002_market_baseline.py",
    "harness/examiner/src/run_pm003_market_baseline.py",
]


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


def collect_cells(
    checkpoints: list[dict], kalshi_idx: dict
) -> tuple[dict[str, list[FeatRow]], dict[str, Any]]:
    cells: dict[str, list[FeatRow]] = {cid: [] for cid in ALL_CELLS}
    stats: dict[str, Any] = {
        "candidates": 0,
        "excluded_method_not_mid": 0,
        "excluded_near_deg": 0,
        "excluded_no_label": 0,
        "excluded_void_or_other": 0,
        "excluded_missing_bid_ask": 0,
        "mid_reconstruct_mismatch": 0,
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
        bid = r.get("yes_bid")
        ask = r.get("yes_ask")
        if bid is None or ask is None:
            stats["excluded_missing_bid_ask"] += 1
            continue
        try:
            bid_f = float(bid)
            ask_f = float(ask)
        except (TypeError, ValueError):
            stats["excluded_missing_bid_ask"] += 1
            continue
        if not math.isfinite(bid_f) or not math.isfinite(ask_f):
            stats["excluded_missing_bid_ask"] += 1
            continue
        lab = _join_label(r, kalshi_idx)
        if lab is None:
            stats["excluded_no_label"] += 1
            continue
        m_t = m_t_from_checkpoint(r)
        recon = (bid_f + ask_f) / 2.0
        if abs(recon - m_t) > 1e-9:
            stats["mid_reconstruct_mismatch"] += 1
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
        last_raw = r.get("last")
        last: float | None
        try:
            last = float(last_raw) if last_raw is not None else None
            if last is not None and not math.isfinite(last):
                last = None
        except (TypeError, ValueError):
            last = None
        s_t = ask_f - bid_f
        delta_t = (last - m_t) if last is not None else None
        cell = primary_cell_id(asset, rem)
        if cell not in cells:
            continue
        cells[cell].append(
            FeatRow(
                cell_id=cell,
                contract_id=r["contract_id"],
                asset=asset,
                checkpoint=KALSHI_REM_TO_LABEL[rem],
                time_remaining_sec=int(rem),
                decision_time=r.get("decision_time") or "",
                m_t=m_t,
                y=y,
                yes_bid=bid_f,
                yes_ask=ask_f,
                last=last,
                s_t=s_t,
                delta_t=delta_t,
            )
        )
        stats["scored"] += 1
    return cells, stats


def _fmt_num(x: Any, nd: int = 6) -> str:
    if x == "UNTESTED" or x is None:
        return "UNTESTED"
    if isinstance(x, float):
        return f"{x:.{nd}f}"
    return str(x)


def _fmt_ci(ci: Any) -> str:
    if ci == "UNTESTED" or ci is None:
        return "UNTESTED"
    if isinstance(ci, dict):
        return f"[{ci['low']:.4f}, {ci['high']:.4f}] (Wilson 95%)"
    return str(ci)


def _score_card(
    feature_id: str,
    cells: dict[str, list[FeatRow]],
    *,
    which: str,
) -> dict[str, Any]:
    primary_src = cells[PRIMARY_CELL]
    annex_src = {cid: cells[cid] for cid in ANNEX_CELLS}

    if which == "003":
        p_rows = {cid: rows_for_feat003(cells[cid]) for cid in ALL_CELLS}
        p_fn = lambda rs: apply_feat003(rs, s0=FEAT003_S0)  # noqa: E731
        map_label = f"p_t=(1-λ)m_t+λ·0.5; λ=clip(s_t/{FEAT003_S0},0,1); s_t=yes_ask-yes_bid"
        extra_drop_key = "excluded_missing_bid_ask_feature"
    elif which == "004":
        p_rows = {cid: rows_for_feat004(cells[cid]) for cid in ALL_CELLS}
        p_fn = lambda rs: apply_feat004(rs, kappa=FEAT004_KAPPA, eps=FEAT004_EPS)  # noqa: E731
        map_label = (
            f"p_t=clip(m_t+{FEAT004_KAPPA}·δ_t, {FEAT004_EPS}, 1-{FEAT004_EPS}); "
            "δ_t=last-m_t"
        )
        extra_drop_key = "excluded_missing_last_feature"
    else:
        raise ValueError(which)

    primary_rows = p_rows[PRIMARY_CELL]
    primary = score_forecast(primary_rows, p_fn(primary_rows), feature_id=feature_id, map_label=map_label)
    annex = {
        cid: score_forecast(p_rows[cid], p_fn(p_rows[cid]), feature_id=feature_id, map_label=map_label)
        for cid in ANNEX_CELLS
    }

    drops = {
        cid: len(cells[cid]) - len(p_rows[cid]) for cid in ALL_CELLS
    }

    robustness: dict[str, Any] = {"note": "annex only — not headline; no post-hoc switch"}
    if which == "003":
        rob = {}
        for s0 in FEAT003_S0_ROBUST:
            ps = apply_feat003(primary_rows, s0=s0)
            rob[f"s0={s0}"] = score_forecast(
                primary_rows, ps, feature_id=feature_id, map_label=f"robustness s0={s0}"
            )
        placebo_p = placebo_shuffle_s(primary_rows, PRIMARY_CELL)
        rob["placebo_shuffle_s_t"] = score_forecast(
            sorted(primary_rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec)),
            placebo_p,
            feature_id=feature_id,
            map_label="placebo: shuffle s_t within cell then same formula",
        )
        robustness["primary"] = rob
        robustness["placebo_seed"] = PLACEBO_SEED
    else:
        rob = {}
        for k in FEAT004_KAPPA_ROBUST:
            ps = apply_feat004(primary_rows, kappa=k, eps=FEAT004_EPS)
            rob[f"kappa={k}"] = score_forecast(
                primary_rows, ps, feature_id=feature_id, map_label=f"robustness kappa={k}"
            )
        rob["placebo_signflip_delta"] = score_forecast(
            primary_rows,
            placebo_signflip_delta(primary_rows),
            feature_id=feature_id,
            map_label="placebo: sign-flip δ_t then same formula",
        )
        robustness["primary"] = rob

    return {
        "feature_id": feature_id,
        "frozen_map": map_label,
        "mle": False,
        "ensemble": False,
        "primary_cell": PRIMARY_CELL,
        "primary": primary,
        "annex_cells": annex,
        "robustness": robustness,
        extra_drop_key: drops,
        "N_base_mid_excludes": {cid: len(cells[cid]) for cid in ALL_CELLS},
        "N_after_feature_filter": {cid: len(p_rows[cid]) for cid in ALL_CELLS},
    }


def _strip_contracts(block: dict[str, Any]) -> dict[str, Any]:
    """Markdown helper: omit long contract lists from narrative tables."""
    return block


def build_markdown(payload: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append(f"# {payload['TEST_ID']} — {payload['package']} vs {payload['incumbent']}")
    lines.append("")
    lines.append(f"**TEST_ID:** `{payload['TEST_ID']}`")
    lines.append(f"**Package:** `{payload['package']}`")
    lines.append(f"**Incumbent:** `{payload['incumbent']}` (TEST-20260911-007 mid-only)")
    lines.append("**Purpose:** atomic incrementality of two F3 frozen no-fit maps vs Kalshi mid")
    lines.append(f"**DATA:** `{payload['data']['dataset_id']}` checkpoints + PM-001 official resolution labels")
    lines.append("**Slice use:** USED_RESEARCH — not validation, not sealed holdout")
    lines.append(f"**Overall verdict:** `{payload['overall_verdict']}`")
    lines.append(f"**invented_numbers:** `{payload['invented_numbers']}`")
    lines.append("**Trading:** FORBIDDEN")
    lines.append("**MLE / ensemble 003+004:** forbidden and not run")
    lines.append("**PM-002 / Poly / L3:** not read / not scored")
    lines.append(f"**Run UTC:** `{payload['run_utc']}`")
    lines.append(f"**SHA256 verified:** `{payload['data']['sha256_verified']}`")
    lines.append("")
    lines.append("## Authority")
    for a in payload["authority"]:
        lines.append(f"- `{a}`")
    lines.append("")
    lines.append("## Filters (same as TEST-007 + feature-field drops)")
    lines.append("- venue=KALSHI, window=15m; BTC/ETH **separate** (no pool)")
    lines.append("- DATA-PROV-PM-003 1208-slice only — **no** PM-002 union")
    lines.append("- checkpoints: T-14m (840), T-10m (600), T-5m (300)")
    lines.append("- `implied_p_method == mid` only; last-fallback excluded")
    lines.append("- exclude `implied_p ≤ 0.02` or `≥ 0.98` (near-deg)")
    lines.append("- VOID/DISPUTED out of scored N")
    lines.append("- FEAT-003: missing bid/ask → drop; FEAT-004: missing last → drop")
    lines.append("- m_t = checkpoint `implied_p` (equals (yes_bid+yes_ask)/2 on mid)")
    lines.append("- **Do not** use PM-001 `LAST_PRICE_DOLLARS` / `OUTCOME_PRICES` / `EXPIRATION_VALUE`")
    lines.append("- No Poly. No L3. No Funding/OI. No in-sample refit.")
    lines.append("")
    lines.append("**Sign convention:** ΔBrier = Brier_model − Brier_market; ΔLogLoss = LogLoss_model − LogLoss_market; **negative = skill** vs mid.")
    lines.append("")
    lines.append("**Falsification (primary):** if ΔBrier≥0 **and** ΔLogLoss≥0 → `REDUNDANT / FAIL-INSUFFICIENT` (not `NO_EDGE`). Skill requires **both** Δ < 0.")
    lines.append("")
    lines.append("**Headline cell (pre-registered, no post-hoc switch):** `KALSHI|15m|BTC|T-5m|mid`")
    lines.append("Other five cells = annex, reported separately, same frozen parameters.")
    lines.append("")

    for feat_key, title, formula in (
        (
            "FEAT-20260912-003",
            "Card 1 — FEAT-20260912-003 (YES touch spread)",
            r"\(s_t=\mathrm{yes\_ask}-\mathrm{yes\_bid}\); \(\lambda=\mathrm{clip}(s_t/0.05,0,1)\); \(p_t=(1-\lambda)m_t+\lambda\cdot 0.5\)",
        ),
        (
            "FEAT-20260912-004",
            "Card 2 — FEAT-20260912-004 (last−mid disagreement)",
            r"\(\delta_t=\mathrm{last}-m_t\); \(p_t=\mathrm{clip}(m_t+1.0\cdot\delta_t,\,10^{-4},\,1-10^{-4})\)",
        ),
    ):
        card = payload["cards"][feat_key]
        prim = card["primary"]
        lines.append(f"## {title}")
        lines.append("")
        lines.append(f"**Frozen map (headline, no-fit):** {formula}")
        lines.append(f"**Primary verdict:** `{prim['cell_verdict']}`")
        lines.append(f"**Reason:** {prim['cell_reason']}")
        lines.append("")
        lines.append("### Primary headline — `KALSHI|15m|BTC|T-5m|mid`")
        lines.append("")
        lines.append(
            "| Cell | N | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | mean(m_t) | mean(p_t) | abstention | ECE | Verdict |"
        )
        lines.append("|------|--:|------------:|-------------:|-------:|--------------:|---------------:|---------:|----------:|----------:|:-----------|-----|---------|")
        lines.append(
            f"| `{PRIMARY_CELL}` | {prim['N']} | {_fmt_num(prim['Brier_model'])} | "
            f"{_fmt_num(prim['Brier_market'])} | {_fmt_num(prim['ΔBrier'])} | "
            f"{_fmt_num(prim['LogLoss_model'])} | {_fmt_num(prim['LogLoss_market'])} | "
            f"{_fmt_num(prim['ΔLogLoss'])} | {_fmt_num(prim['mean(m_t)'], 4)} | "
            f"{_fmt_num(prim['mean(p_t)'], 4)} | {prim['abstention']} | "
            f"{_fmt_num(prim['ECE'])} | `{prim['cell_verdict']}` |"
        )
        lines.append("")
        lines.append(
            f"- WR (descriptive, optional): `{_fmt_num(prim['WR'], 4)}` "
            f"N_WR={prim.get('N_WR')} CI={_fmt_ci(prim.get('CI'))}"
        )
        lines.append(f"- mean(s_t)={_fmt_num(prim.get('mean(s_t)'))}; mean(|δ_t|)={_fmt_num(prim.get('mean(|δ_t|)'))}")
        lines.append(f"- gap mean(p_t−m_t)={_fmt_num(prim['gap']['mean'] if isinstance(prim.get('gap'), dict) else 'UNTESTED')}")
        lines.append(f"- Calibration: {prim['Calibration']['note']}")
        lines.append("- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no action rule / no trading)")
        lines.append("")
        lines.append("### Annex — other five cells (same frozen map; not headline)")
        lines.append("")
        lines.append(
            "| Cell | N | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | mean(m_t) | mean(p_t) | ECE | Verdict |"
        )
        lines.append("|------|--:|------------:|-------------:|-------:|--------------:|---------------:|---------:|----------:|----------:|-----|---------|")
        for cid in ANNEX_CELLS:
            c = card["annex_cells"][cid]
            lines.append(
                f"| `{cid}` | {c['N']} | {_fmt_num(c['Brier_model'])} | "
                f"{_fmt_num(c['Brier_market'])} | {_fmt_num(c['ΔBrier'])} | "
                f"{_fmt_num(c['LogLoss_model'])} | {_fmt_num(c['LogLoss_market'])} | "
                f"{_fmt_num(c['ΔLogLoss'])} | {_fmt_num(c['mean(m_t)'], 4)} | "
                f"{_fmt_num(c['mean(p_t)'], 4)} | {_fmt_num(c['ECE'])} | `{c['cell_verdict']}` |"
            )
        lines.append("")
        lines.append("### Robustness annex (not headline; no post-hoc switch)")
        lines.append("")
        rob = card["robustness"]["primary"]
        lines.append("| Variant | N | ΔBrier | ΔLogLoss | Brier_model | LogLoss_model | Verdict |")
        lines.append("|---------|--:|-------:|---------:|------------:|--------------:|---------|")
        for k, block in rob.items():
            lines.append(
                f"| `{k}` | {block['N']} | {_fmt_num(block['ΔBrier'])} | "
                f"{_fmt_num(block['ΔLogLoss'])} | {_fmt_num(block['Brier_model'])} | "
                f"{_fmt_num(block['LogLoss_model'])} | `{block['cell_verdict']}` |"
            )
        lines.append("")

    lines.append("## Filter / join stats (shared mid universe, TEST-007 excludes)")
    lines.append("```json")
    lines.append(json.dumps(payload["filter_stats"], indent=2))
    lines.append("```")
    lines.append("")
    lines.append("## Integrity")
    lines.append("")
    lines.append(f"- checkpoints.ndjson sha256: `{payload['data']['checkpoints_sha256']}`")
    lines.append(f"- expected: `{payload['data']['checkpoints_sha256_expected']}`")
    lines.append(f"- sha256_verified: `{payload['data']['sha256_verified']}`")
    lines.append(f"- venues: `{payload['data']['venue_check']['venues']}`")
    lines.append("- PM-002 checkpoint rows: **not read / not scored**")
    lines.append("- Poly: **none**")
    lines.append("- L3 / Funding / OI: **not used**")
    lines.append("- m_t source: PM-003 `checkpoints.implied_p` (mid) — never PM-001 LAST_PRICE / OUTCOME_PRICES")
    lines.append("- No MLE; no α,β,γ; no ensemble of 003+004")
    lines.append("")
    lines.append("## Overall package verdict")
    lines.append(f"**`{payload['overall_verdict']}`** — {payload['overall_reason']}")
    lines.append("")
    lines.append("FAIL-INSUFFICIENT ≠ NO_EDGE. This is **not** a strategy PASS. No trading authorization. Holdout closed.")
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


def _package_verdict(card003: dict[str, Any], card004: dict[str, Any]) -> tuple[str, str]:
    v3 = card003["primary"]["cell_verdict"]
    v4 = card004["primary"]["cell_verdict"]
    inc3 = v3 == "INCREMENTAL_RESEARCH"
    inc4 = v4 == "INCREMENTAL_RESEARCH"
    if not inc3 and not inc4:
        return (
            "REDUNDANT / FAIL-INSUFFICIENT",
            (
                "Neither atomic F3 card improves both Brier and LogLoss vs mid "
                f"on primary {PRIMARY_CELL}. "
                f"FEAT-003={v3}; FEAT-004={v4}. "
                "REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE). "
                "USED_RESEARCH; holdout closed; no trading."
            ),
        )
    if inc3 and inc4:
        return (
            "INCREMENTAL_RESEARCH",
            (
                "Both atomic F3 cards improve Brier and LogLoss vs mid on primary "
                f"{PRIMARY_CELL} (USED_RESEARCH only). Not validation. Not trading. "
                "No ensemble of 003+004."
            ),
        )
    winner = "FEAT-20260912-003" if inc3 else "FEAT-20260912-004"
    loser = "FEAT-20260912-004" if inc3 else "FEAT-20260912-003"
    loser_v = v4 if inc3 else v3
    return (
        "MIXED_ATOMIC / FAIL-INSUFFICIENT",
        (
            f"{winner} incremental on primary (USED_RESEARCH); "
            f"{loser} {loser_v}. Package is not a strategy PASS; "
            "no ensemble; holdout closed; no trading. "
            "FAIL-INSUFFICIENT ≠ NO_EDGE for the non-incremental card."
        ),
    )


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

    kalshi_labels = _load_ndjson(KALSHI_LABELS)
    kalshi_idx = _index_labels(kalshi_labels)

    cells, filt = collect_cells(checkpoints, kalshi_idx)

    card003 = _score_card("FEAT-20260912-003", cells, which="003")
    card004 = _score_card("FEAT-20260912-004", cells, which="004")

    overall, reason = _package_verdict(card003, card004)
    run_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out_stem = f"{TEST_ID}-{PACKAGE}"
    out_json = OUT_DIR / f"{out_stem}.json"
    out_md = OUT_DIR / f"{out_stem}.md"

    payload: dict[str, Any] = {
        "TEST_ID": TEST_ID,
        "package": PACKAGE,
        "incumbent": INCUMBENT,
        "purpose": "f3_atomic_incrementality_vs_kalshi_mid",
        "strategy": None,
        "mle": False,
        "ensemble_003_004": False,
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
            "labels_kalshi": str(KALSHI_LABELS),
            "labels_poly": None,
            "m_t_source": "DATA-PROV-PM-003 derived checkpoints.implied_p (mid)",
            "forbidden_m_t": ["LAST_PRICE_DOLLARS", "OUTCOME_PRICES", "EXPIRATION_VALUE"],
            "pm002_checkpoints_read": False,
            "poly_scored": False,
            "venue_check": venue_check,
        },
        "primary_cell": PRIMARY_CELL,
        "annex_cell_order": list(ANNEX_CELLS),
        "cards": {
            "FEAT-20260912-003": card003,
            "FEAT-20260912-004": card004,
        },
        "filter_stats": {
            **{k: v for k, v in filt.items() if k != "void_bucket"},
            "void_bucket_n": len(filt["void_bucket"]),
            "void_bucket": filt["void_bucket"],
        },
        "sign_conventions": {
            "ΔBrier": "Brier_model − Brier_market; negative = skill vs mid",
            "ΔLogLoss": "LogLoss_model − LogLoss_market; negative = skill vs mid",
            "WR": "descriptive p_t>0.5⇒YES; not skill",
            "LogLoss_eps": 1e-15,
            "falsification_primary": "ΔBrier≥0 AND ΔLogLoss≥0 → REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)",
        },
        "forbidden": [
            "in-sample refit / MLE / α,β,γ",
            "ensemble of 003+004",
            "PM-002 union",
            "Poly",
            "L3",
            "Funding/OI",
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
    audit_path = ARCHIVE_AUDIT / f"2026-09-12-{TEST_ID}-{PACKAGE}-examiner.md"

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
        f"# {TEST_ID}\n\n"
        f"PACKAGE `{PACKAGE}` vs `{INCUMBENT}` verdict `{overall}`\n"
        f"invented_numbers: false\n"
        f"Trading: FORBIDDEN\n"
        f"Full: `{arch_md}`\n"
    )
    audit_path.write_text(
        "# Audit pointer\n\n"
        f"- TEST: `{TEST_ID}`\n"
        f"- Package: `{PACKAGE}` vs `{INCUMBENT}`\n"
        f"- Cards: FEAT-20260912-003, FEAT-20260912-004 (atomic; no ensemble)\n"
        f"- Verdict: `{overall}`\n"
        f"- invented_numbers: false\n"
        f"- Trading: FORBIDDEN\n"
        f"- SHA256 verified: `{digest}`\n"
        f"- PM-002: not read\n"
        f"- Poly: none\n"
        f"- MLE: none\n"
        f"- Artifacts: `{out_json}`\n"
        f"- Archive: `{arch_json}`\n"
        f"- DATA: DATA-PROV-PM-003 checkpoints + PM-001 official YES/NO/VOID labels\n"
        f"- Purpose: F3 incrementality vs mid (USED_RESEARCH; not validation)\n"
    )

    print(f"TEST_ID={TEST_ID}")
    print(f"overall_verdict={overall}")
    print(f"sha256_verified={digest}")
    for feat_id, card in payload["cards"].items():
        p = card["primary"]
        print(
            f"{feat_id}\tPRIMARY\tN={p['N']}\t"
            f"Brier_m={p['Brier_market']}\tBrier_p={p['Brier_model']}\t"
            f"dB={p['ΔBrier']}\tLL_m={p['LogLoss_market']}\tLL_p={p['LogLoss_model']}\t"
            f"dLL={p['ΔLogLoss']}\tverdict={p['cell_verdict']}"
        )
        for cid in ANNEX_CELLS:
            c = card["annex_cells"][cid]
            print(
                f"{feat_id}\tANNEX\t{cid}\tN={c['N']}\t"
                f"dB={c['ΔBrier']}\tdLL={c['ΔLogLoss']}\tverdict={c['cell_verdict']}"
            )
    print(f"wrote {out_json}")
    print(f"wrote {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
