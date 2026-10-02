#!/usr/bin/env python3
"""TEST-20260913-005 — CBVEL-INCREMENTAL vs MKT-KALSHI-15M-MID.

Coinbase 1m velocity clip (λ=0.15, w=0.0015 frozen) on
DRAFT-ABST-20260913-005 T-14m headlines only. Policy B (bar_end < t).
No CF. No Map 2. No Φ(z). No Poly last. No Policy A. No annex.
invented_numbers=false. Trading FORBIDDEN.
"""

from __future__ import annotations

import csv
import json
import math
import sys
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
from src.cbvel_incremental import (  # noqa: E402
    ASSET_TO_PRODUCT,
    CBVELRow,
    EPS,
    GRAN,
    HEADLINE_BTC,
    HEADLINE_ETH,
    HEADLINES,
    LAMBDA_ROBUST,
    LAMBDA_SCORED,
    MIN_N_KILL,
    PLACEBO_SEED,
    W_ROBUST,
    W_SCORED,
    apply_map,
    gate_decision,
    last_completed_start_policy_b,
    package_verdict,
    placebo_flip_sign_v,
    placebo_lambda_zero,
    placebo_shuffle_v,
    score_forecast,
    velocity_from_closes,
)

LAB = Path("/workspace/lab")
CHECKPOINTS = LAB / "data/DATA-PROV-PM-003/derived/checkpoints.ndjson"
COVERAGE = LAB / "data/DATA-PROV-PM-003/derived/contract_coverage.ndjson"
KALSHI_LABELS = LAB / "data/DATA-PROV-PM-001/normalized/kalshi_15m_btc_eth_resolved.ndjson"
CB_RAW = LAB / "data/DATA-PROV-CB-001/raw"
OUT_DIR = LAB / "harness/examiner/out"
ARCHIVE_TESTS = LAB / "archive/tests"
ARCHIVE_AUDIT = LAB / "archive/audit"

TEST_ID = "TEST-20260913-005"
PACKAGE = "CBVEL-INCREMENTAL"
INCUMBENT = "MKT-KALSHI-15M-MID"
FEATURE_ID = "DRAFT-FEAT-20260913-005"
GATE_ID = "DRAFT-ABST-20260913-005"

AUTHORITY = [
    "governance/EXAMINER_ORDER_TEST-20260913-005-CBVEL.md",
    "governance/CBVEL_ON_MINUTE_POLICY_2026-09-13.md",
    "archive/features/DRAFT-FEAT-20260913-005-CBVEL.md",
    "archive/features/DRAFT-ABST-20260913-005-CBVEL.md",
    "data/DATA-PROV-CB-001/provenance/DATA_VERDICT_CB001_PM003_JOIN.md",
]

TARGET_REM = 840  # T-14m only; no annex


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


def _parse_decision_ms(decision_time: str) -> int:
    dt = datetime.fromisoformat(decision_time.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)


def _parse_decision_s(decision_time: str) -> int:
    return _parse_decision_ms(decision_time) // 1000


def _is_void(lab: dict[str, Any]) -> bool:
    st = str(lab.get("STATUS") or "").upper()
    res = str(lab.get("RESOLUTION") or "").upper()
    return st in ("VOID", "DISPUTED") or res in ("VOID", "DISPUTED")


def load_cb_candles(product: str) -> dict[int, dict[str, Any]]:
    path = CB_RAW / f"{product}_1m.csv"
    out: dict[int, dict[str, Any]] = {}
    with path.open() as f:
        for row in csv.DictReader(f):
            ts = int(row["time"])
            out[ts] = {
                "time": ts,
                "close": float(row["close"]),
                "open": float(row["open"]),
                "low": float(row["low"]),
                "high": float(row["high"]),
                "volume": float(row["volume"]),
                "time_iso": row["time_iso"],
                "bar_end_iso": row["bar_end_iso"],
            }
    return out


def policy_b_bar(
    book: dict[int, dict[str, Any]], decision_s: int
) -> tuple[
    Optional[int],
    Optional[int],
    Optional[float],
    Optional[float],
    Optional[float],
    bool,
    bool,
]:
    """Policy B only: bar_end < decision_time. NOT policy A.

    Returns (bar_start, bar_end, bar_close, prior_close, v, bar_ok, prior_ok).
    """
    start = last_completed_start_policy_b(decision_s)
    bar_end = start + GRAN
    if bar_end >= decision_s:
        # safety: must never select bar ending at/after t under B
        return None, None, None, None, None, False, False
    c_bar = book.get(start)
    c_prior = book.get(start - GRAN)
    if c_bar is None:
        return start, bar_end, None, None, None, False, False
    bar_close = float(c_bar["close"])
    if c_prior is None:
        return start, bar_end, bar_close, None, None, True, False
    prior_close = float(c_prior["close"])
    if prior_close <= 0 or not math.isfinite(prior_close):
        return start, bar_end, bar_close, prior_close, None, True, False
    v = velocity_from_closes(bar_close, prior_close)
    return start, bar_end, bar_close, prior_close, v, True, v is not None


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
        er["FLOOR_STRIKE"] = lab.get("FLOOR_STRIKE")
        er["OPEN_TIME"] = lab.get("OPEN_TIME")
        er["CLOSE_TIME"] = lab.get("CLOSE_TIME")
        er["_label"] = lab
        enriched.append(er)
    return enriched, stats


def collect_headline_rows(
    enriched: list[dict],
    candles: dict[str, dict[int, dict[str, Any]]],
) -> tuple[dict[str, list[CBVELRow]], dict[str, Any]]:
    cells: dict[str, list[CBVELRow]] = {cid: [] for cid in HEADLINES}
    stats: dict[str, Any] = {
        "candidates": 0,
        "excluded_method_not_mid": 0,
        "excluded_near_deg": 0,
        "excluded_void_or_other": 0,
        "excluded_no_y": 0,
        "scored": 0,
        "n_speak": 0,
        "n_abstain": 0,
        "n_fail_closed_missing_bar": 0,
        "n_fail_closed_missing_prior": 0,
        "n_fail_closed_locked": 0,
        "n_on_minute": 0,
        "n_policy_A_bar_rejected": 0,
        "policy_A_used_as_headline": False,
        "policy": "B",
        "join_verdict": "CONDITIONAL",
        "per_cell": {
            cid: {
                "candidates": 0,
                "scored": 0,
                "speak": 0,
                "abstain": 0,
                "fail_closed_bar": 0,
                "fail_closed_prior": 0,
                "fail_closed_locked": 0,
                "excluded_method_not_mid": 0,
                "excluded_near_deg": 0,
                "excluded_void": 0,
            }
            for cid in HEADLINES
        },
        "void_bucket": [],
        "cb_bars_loaded": {
            "BTC-USD": len(candles.get("BTC-USD", {})),
            "ETH-USD": len(candles.get("ETH-USD", {})),
        },
        "CF_used": False,
        "L3_used": False,
        "poly_used": False,
        "map2_used": False,
        "binance_used": False,
        "policy_A_used": False,
    }

    for r in enriched:
        rem = r.get("time_remaining_sec")
        asset = r.get("asset")
        if rem != TARGET_REM or asset not in ("BTC", "ETH"):
            continue
        cell = primary_cell_id(asset, rem)
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
        dt = r.get("decision_time") or ""
        decision_ms = _parse_decision_ms(dt)
        decision_s = decision_ms // 1000
        if decision_ms % 60_000 == 0:
            stats["n_on_minute"] += 1

        open_time = r.get("OPEN_TIME") or r.get("open_time") or ""
        close_time = r.get("CLOSE_TIME") or r.get("close_time") or ""

        # close-window / Map 2 lock check
        not_locked = True
        if close_time:
            try:
                close_ms = _parse_decision_ms(close_time)
                close_start_ms = close_ms - 60_000
                if decision_ms >= close_start_ms:
                    not_locked = False
                    stats["n_fail_closed_locked"] += 1
                    cs["fail_closed_locked"] += 1
            except Exception:
                not_locked = False
                stats["n_fail_closed_locked"] += 1
                cs["fail_closed_locked"] += 1
        else:
            not_locked = False
            stats["n_fail_closed_locked"] += 1
            cs["fail_closed_locked"] += 1

        product = ASSET_TO_PRODUCT[asset]
        (
            bar_start,
            bar_end,
            bar_close,
            prior_close,
            v,
            bar_ok,
            prior_ok,
        ) = policy_b_bar(candles[product], decision_s)

        # Explicitly reject Policy A (bar_end == decision_time) as headline path
        if bar_end is not None and bar_end == decision_s:
            stats["n_policy_A_bar_rejected"] += 1
            bar_ok = False
            prior_ok = False
            v = None

        if not bar_ok:
            stats["n_fail_closed_missing_bar"] += 1
            cs["fail_closed_bar"] += 1
        elif not prior_ok:
            stats["n_fail_closed_missing_prior"] += 1
            cs["fail_closed_prior"] += 1

        mid_ok = True  # already filtered
        gate = gate_decision(
            cell,
            mid_ok=mid_ok,
            bar_ok=bar_ok,
            prior_ok=prior_ok,
            not_locked=not_locked,
        )
        speak = gate == "ALLOW_SPEAK_HEADLINE" and v is not None

        if speak:
            stats["n_speak"] += 1
            cs["speak"] += 1
        else:
            stats["n_abstain"] += 1
            cs["abstain"] += 1

        cells[cell].append(
            CBVELRow(
                cell_id=cell,
                contract_id=r["contract_id"],
                asset=asset,
                checkpoint=KALSHI_REM_TO_LABEL[int(rem)],
                time_remaining_sec=int(rem),
                decision_time=dt,
                decision_time_ms=decision_ms,
                open_time=str(open_time),
                close_time=str(close_time),
                m_t=m_t,
                y=int(y),
                bar_start_s=bar_start if bar_ok else None,
                bar_end_s=bar_end if bar_ok else None,
                bar_close=bar_close if bar_ok else None,
                prior_close=prior_close if prior_ok else None,
                v=v if speak else (v if (bar_ok and prior_ok) else None),
                gate=gate,
                bar_ok=bar_ok,
                prior_ok=prior_ok,
                not_locked=not_locked,
                speak=speak,
            )
        )
        stats["scored"] += 1
        cs["scored"] += 1

    return cells, stats


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
    lines.append(
        f"**Feature:** `{FEATURE_ID}` (Coinbase 1m velocity clip, "
        f"λ={LAMBDA_SCORED} w={W_SCORED} frozen)"
    )
    lines.append(
        f"**Gate:** `{GATE_ID}` (speak only on BTC/ETH T-14m mid with Policy B CB bar)"
    )
    lines.append(f"**Incumbent:** `{payload['incumbent']}` (TEST-20260911-007 mid-only)")
    lines.append(
        "**Purpose:** CB-VEL Coinbase 1m velocity incrementality on two AMD-005 headlines"
    )
    lines.append(
        f"**DATA:** `{payload['data']['dataset_id']}` + `{payload['data']['cb_dataset_id']}` "
        "+ PM-001 OPEN / CLOSE / RESOLUTION"
    )
    lines.append(
        "**Join:** DATA_VERDICT_CB001_PM003_JOIN **CONDITIONAL** "
        "· Policy B (bar_end < decision_time) · no CF · no Poly last · no policy A"
    )
    lines.append("**Slice use:** USED_RESEARCH — not validation, not sealed holdout")
    lines.append(f"**Overall verdict:** `{payload['overall_verdict']}`")
    lines.append(f"**invented_numbers:** `{payload['invented_numbers']}`")
    lines.append("**Trading:** FORBIDDEN")
    lines.append(
        "**Stamp:** Join **CONDITIONAL**. Policy B (bar_end < t). "
        "No CF. No Poly last. No policy A. "
        "No Map 2. No L3. No Φ(z). No sibling blend. No Binance."
    )
    lines.append("**Annex:** none (no other rem; robustness grid report-only)")
    lines.append(f"**Run UTC:** `{payload['run_utc']}`")
    lines.append(f"**SHA256 verified:** `{payload['data']['sha256_verified']}`")
    lines.append("")
    lines.append("## Authority")
    for a in payload["authority"]:
        lines.append(f"- `{a}`")
    lines.append("")
    lines.append("## Frozen map")
    lines.append("- ε = 1e-4; w = 0.0015; λ = 0.15")
    lines.append(
        "- bar = last CB-001 1m candle with bar_end < decision_time  # LOCK B ONLY"
    )
    lines.append("- prior = immediately previous completed CB-001 1m close")
    lines.append("- v = (bar.close − prior.close) / prior.close")
    lines.append(
        "- if ABSTAIN or bar/prior missing or prior.close≤0: p = m"
    )
    lines.append(
        f"- else: p = clip(m + λ · clip(v/w, −1, +1), ε, 1−ε) "
        f"with λ={LAMBDA_SCORED}, w={W_SCORED}, ε={EPS}"
    )
    lines.append(
        f"- λ={LAMBDA_SCORED}, w={W_SCORED} frozen. "
        f"Robustness annex λ∈{list(LAMBDA_ROBUST)} / w∈{list(W_ROBUST)} "
        "— do not pick winner. λ=0 ⇒ Δ=0."
    )
    lines.append("- **Policy B ONLY.** NOT policy A (bar_end ≤ t). NOT a rescue.")
    lines.append("")
    lines.append("## Filters / join")
    lines.append("- venue=KALSHI, window=15m; BTC/ETH **separate** (no pool)")
    lines.append("- DATA-PROV-PM-003 1208-slice only — **no** PM-002 union")
    lines.append("- Headlines only: T-14m (rem=840); **no annex**")
    lines.append("- `implied_p_method == mid` only; last-fallback excluded")
    lines.append("- exclude `implied_p ≤ 0.02` or `≥ 0.98` (near-deg)")
    lines.append("- VOID/DISPUTED out of scored N")
    lines.append(
        "- CB bar = Policy B: last DATA-PROV-CB-001 1m candle with "
        "bar_end < decision_time; prior = previous completed close"
    )
    lines.append("- Missing bar/prior/m or inside close-minute → fail-closed p_t := m_t")
    lines.append(
        "- **NOT** policy A. **NOT** CF. **NOT** Binance. **NOT** L3. "
        "**NOT** Poly last. **NOT** Map 2. **NOT** Φ(z)."
    )
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
    lines.append("## Overall reason")
    lines.append(payload["overall_reason"])
    lines.append("")
    lines.append("## Headlines (AMD-005, no pool, no annex)")
    lines.append("")
    lines.append(
        "| Cell | N | speak N | Brier_model | Brier_market | ΔBrier | "
        "LogLoss_model | LogLoss_market | ΔLogLoss | mean(m)_speak | mean(p)_speak | "
        "mean(v)_speak | speak_rate | ECE | Verdict |"
    )
    lines.append(
        "|------|--:|--------:|------------:|-------------:|-------:|"
        "--------------:|---------------:|---------:|-------------:|-------------:|"
        "-------------:|-----------:|-----|---------|"
    )
    for cid in HEADLINES:
        c = payload["headlines"][cid]
        lines.append(
            f"| `{cid}` | {c['N']} | {c['n_speak']} | {_fmt_num(c['Brier_model'])} | "
            f"{_fmt_num(c['Brier_market'])} | {_fmt_num(c['ΔBrier'])} | "
            f"{_fmt_num(c['LogLoss_model'])} | {_fmt_num(c['LogLoss_market'])} | "
            f"{_fmt_num(c['ΔLogLoss'])} | {_fmt_num(c.get('mean(m)_speak'), 4)} | "
            f"{_fmt_num(c.get('mean(p)_speak'), 4)} | {_fmt_num(c.get('mean(v)_speak'))} | "
            f"{_fmt_num(c.get('speak_rate'), 4)} | {_fmt_num(c['ECE'])} | "
            f"`{c['cell_verdict']}` |"
        )
    lines.append("")
    for cid in HEADLINES:
        c = payload["headlines"][cid]
        lines.append(f"### `{cid}`")
        lines.append(
            f"- n_speak={c['n_speak']}; n_abstain={c['n_abstain']}; "
            f"fail_closed_missing={c['n_fail_closed_missing']}; "
            f"speak_rate={_fmt_num(c.get('speak_rate'), 4)}"
        )
        lines.append(
            f"- mean(m)_all={_fmt_num(c.get('mean(m)_all'), 4)}; "
            f"mean(p)_all={_fmt_num(c.get('mean(p)_all'), 4)}; "
            f"mean(bar_close)={_fmt_num(c.get('mean(bar_close)'))}; "
            f"mean(prior_close)={_fmt_num(c.get('mean(prior_close)'))}"
        )
        lines.append(f"- Reason: {c['cell_reason']}")
        lines.append(f"- Calibration: {c['Calibration']['note']}")
        lines.append(f"- ECE_market: {_fmt_num(c.get('ECE_market'))}")
        lines.append("- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no trading)")
        lines.append("")

    lines.append(
        "## Robustness annex (λ×w grids; not headline; do not pick winner)"
    )
    lines.append("")
    lines.append("| Cell | λ | w | N | ΔBrier | ΔLogLoss | Verdict |")
    lines.append("|------|--:|--:|--:|-------:|---------:|---------|")
    for cid in HEADLINES:
        for _key, block in payload["robustness"][cid].items():
            lines.append(
                f"| `{cid}` | {block.get('λ', '')} | {block.get('w', '')} | "
                f"{block['N']} | {_fmt_num(block['ΔBrier'])} | "
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
    lines.append("- λ=0 must give ΔBrier=0 and ΔLogLoss=0 (identity vs mid).")
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
    lines.append("- Join verdict: **CONDITIONAL**")
    lines.append("- Join policy: **B** (bar_end < decision_time)")
    lines.append("- Policy A (bar_end ≤ t): **not used** as headline / not a rescue")
    lines.append("- CF / Binance / L3 / Poly last / Map 2 / Φ(z) / sibling: **not used**")
    lines.append("- EXPIRATION_VALUE: **not read / not scored**")
    lines.append("- No λ/w retune; no gate retune; no annex sneak; no pool")
    lines.append("")
    lines.append("## Overall package verdict")
    lines.append(f"**`{payload['overall_verdict']}`** — {payload['overall_reason']}")
    lines.append("")
    lines.append(
        "FAIL-INSUFFICIENT ≠ NO_EDGE. This is **not** a Champion / strategy PASS. "
        "No trading authorization. Holdout closed. Join CONDITIONAL; Policy B."
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
        "join_verdict": "CONDITIONAL",
        "join_policy": "B",
        "run_utc": run_utc,
        "authority": AUTHORITY,
    }
    out_json = OUT_DIR / f"{out_stem}.json"
    out_md = OUT_DIR / f"{out_stem}.md"
    out_json.write_text(json.dumps(payload, indent=2) + "\n")
    out_md.write_text(
        f"# {TEST_ID} — DATA_INTEGRITY_FAIL\n\n{reason}\n\n"
        "invented_numbers: false\nTrading: FORBIDDEN\n"
        "Join CONDITIONAL; Policy B (bar_end < t); no CF; no Poly last; no policy A\n"
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

    candles = {
        "BTC-USD": load_cb_candles("BTC-USD"),
        "ETH-USD": load_cb_candles("ETH-USD"),
    }
    if not candles["BTC-USD"] or not candles["ETH-USD"]:
        return _write_integrity_fail("CB-001 raw candles missing for BTC-USD or ETH-USD")

    enriched, enrich_stats = enrich_checkpoints(checkpoints, coverage, kalshi_idx)
    cells, filt = collect_headline_rows(enriched, candles)
    filt["enrich"] = enrich_stats

    if filt["policy_A_used"] or filt["policy_A_used_as_headline"]:
        return _write_integrity_fail("forbidden Policy A used as headline")
    if (
        filt["CF_used"]
        or filt["L3_used"]
        or filt["poly_used"]
        or filt["map2_used"]
        or filt["binance_used"]
    ):
        return _write_integrity_fail("forbidden CF/L3/Poly/Map2/Binance used")

    map_label = (
        f"CB-VEL: v=(bar.close-prior.close)/prior.close; "
        f"p=clip(m+{LAMBDA_SCORED}*clip(v/{W_SCORED},-1,1),{EPS},1-{EPS}) "
        f"on ALLOW_SPEAK Policy B (bar_end<t); else p=m"
    )

    headlines: dict[str, Any] = {}
    for cid in HEADLINES:
        rows = sorted(
            cells[cid],
            key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec),
        )
        cells[cid] = rows
        # Ensure speak rows have v set for scoring
        fixed: list[CBVELRow] = []
        for r in rows:
            if r.speak and r.v is None and r.bar_close is not None and r.prior_close is not None:
                vv = velocity_from_closes(r.bar_close, r.prior_close)
                r = CBVELRow(**{**r.__dict__, "v": vv})
            fixed.append(r)
        cells[cid] = fixed
        rows = fixed
        ps = apply_map(rows, lam=LAMBDA_SCORED, w=W_SCORED)
        headlines[cid] = score_forecast(
            rows, ps, feature_id=FEATURE_ID, map_label=map_label
        )

    # Robustness: λ × w grid (annex only — do not pick winner)
    robustness: dict[str, dict[str, Any]] = {}
    for cid in HEADLINES:
        rows = cells[cid]
        rob: dict[str, Any] = {}
        for lam in LAMBDA_ROBUST:
            for w in W_ROBUST:
                key = f"λ={lam}|w={w}"
                ps = apply_map(rows, lam=lam, w=w)
                block = score_forecast(
                    rows,
                    ps,
                    feature_id=FEATURE_ID,
                    map_label=f"robustness {key}",
                )
                block["λ"] = lam
                block["w"] = w
                block.pop("contract_ids_scored", None)
                rob[key] = block
        robustness[cid] = rob

    # Placebos
    placebos: dict[str, dict[str, Any]] = {
        "lambda_0": {},
        "flip_sign_v": {},
        "shuffle_v": {},
    }
    for cid in HEADLINES:
        rows = cells[cid]
        ordered = sorted(
            rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec)
        )

        p0 = placebo_lambda_zero(ordered)
        b0 = score_forecast(
            ordered, p0, feature_id=FEATURE_ID, map_label="placebo λ=0"
        )
        b0.pop("contract_ids_scored", None)
        ok0 = (
            isinstance(b0["ΔBrier"], float)
            and isinstance(b0["ΔLogLoss"], float)
            and abs(b0["ΔBrier"]) < 1e-15
            and abs(b0["ΔLogLoss"]) < 1e-15
        )
        b0["placebo_note"] = f"λ=0 identity check pass={ok0}"
        b0["lambda0_delta_zero"] = ok0
        placebos["lambda_0"][cid] = b0

        pf = placebo_flip_sign_v(rows, cid)
        ordered_f = sorted(
            rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec)
        )
        bf = score_forecast(
            ordered_f, pf, feature_id=FEATURE_ID, map_label="placebo flip sign(v)"
        )
        bf.pop("contract_ids_scored", None)
        bf["placebo_note"] = "sign(v) flipped; should not beat true sign"
        placebos["flip_sign_v"][cid] = bf

        ps = placebo_shuffle_v(rows, cid)
        ordered_s = sorted(
            rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec)
        )
        bs = score_forecast(
            ordered_s, ps, feature_id=FEATURE_ID, map_label="placebo shuffle v"
        )
        bs.pop("contract_ids_scored", None)
        bs["placebo_note"] = "v shuffled within cell; m fixed"
        placebos["shuffle_v"][cid] = bs

    overall, reason = package_verdict(headlines)
    run_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out_stem = f"{TEST_ID}-{PACKAGE}"
    out_json = OUT_DIR / f"{out_stem}.json"
    out_md = OUT_DIR / f"{out_stem}.md"

    for cid in HEADLINES:
        headlines[cid].pop("contract_ids_scored", None)

    payload: dict[str, Any] = {
        "TEST_ID": TEST_ID,
        "package": PACKAGE,
        "feature_id": FEATURE_ID,
        "gate_id": GATE_ID,
        "incumbent": INCUMBENT,
        "purpose": "cbvel_coinbase_1m_velocity_incrementality",
        "strategy": None,
        "trading": "FORBIDDEN",
        "invented_numbers": False,
        "join_verdict": "CONDITIONAL",
        "join_policy": "B",
        "overall_verdict": overall,
        "overall_reason": reason,
        "run_utc": run_utc,
        "authority": AUTHORITY,
        "frozen_map": {
            "λ": LAMBDA_SCORED,
            "w": W_SCORED,
            "ε": EPS,
            "formula": map_label,
            "no_phi_z": True,
            "no_sibling_blend": True,
            "no_map2": True,
            "no_annex": True,
            "no_CF": True,
            "no_L3": True,
            "no_poly_last": True,
            "no_binance": True,
            "policy_B_only": True,
            "policy_A_forbidden": True,
        },
        "stamps": {
            "join": "CONDITIONAL",
            "policy": "B (bar_end < decision_time)",
            "no_CF": True,
            "no_Poly_last": True,
            "no_policy_A": True,
        },
        "data": {
            "dataset_id": "DATA-PROV-PM-003",
            "cb_dataset_id": "DATA-PROV-CB-001",
            "slice_use": "USED_RESEARCH",
            "checkpoints": str(CHECKPOINTS),
            "checkpoints_sha256": digest,
            "checkpoints_sha256_expected": EXPECTED_CHECKPOINTS_SHA256,
            "sha256_verified": digest == EXPECTED_CHECKPOINTS_SHA256,
            "labels_kalshi": str(KALSHI_LABELS),
            "cb_raw": str(CB_RAW),
            "m_t_source": "DATA-PROV-PM-003 derived checkpoints.implied_p (mid)",
            "v_source": (
                "DATA-PROV-CB-001 1m candles Policy B: last bar with "
                "bar_end < decision_time; v=(close_B-close_{B-1})/close_{B-1}"
            ),
            "join_verdict": "CONDITIONAL",
            "join_policy": "B",
            "forbidden": [
                "Policy A (bar_end <= t) as headline",
                "Map 2",
                "Φ(z)",
                "sibling blend",
                "CF",
                "L3",
                "Poly last",
                "Binance",
                "EXPIRATION_VALUE",
                "T−1 mid",
                "raw 0/1",
                "retune λ/w",
            ],
            "pm002_checkpoints_read": False,
            "poly_scored": False,
            "l3_used": False,
            "cf_used": False,
            "binance_used": False,
            "policy_A_used": False,
            "venue_check": venue_check,
        },
        "headline_cells": list(HEADLINES),
        "headlines": headlines,
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
            "falsification_primary": (
                "ΔBrier≥0 OR ΔLogLoss≥0 on a headline → "
                "REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE); "
                "one-asset invert kills; N<80 kills"
            ),
        },
        "confirmations": {
            "EXPIRATION_VALUE_used": False,
            "policy_A_used_as_headline": False,
            "invented_numbers": False,
            "trading": False,
            "phi_z_used": False,
            "sibling_blend_used": False,
            "map2_used": False,
            "L3_used": False,
            "poly_used": False,
            "binance_used": False,
            "CF_used": False,
            "join_policy": "B",
            "join_verdict": "CONDITIONAL",
        },
        "forbidden_actions": [
            "in-sample refit",
            "retune λ/w",
            "retune gate / annex sneak",
            "PM-002 union",
            "Poly last",
            "L3",
            "CF",
            "Map 2",
            "Φ(z)",
            "sibling blend",
            "Policy A as headline",
            "Binance",
            "EXPIRATION_VALUE",
            "T−1 mid",
            "raw 0/1",
            "trading",
            "invented numbers",
            "pick λ/w winner from robustness grid",
            "BTC+ETH pool",
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
                "join_verdict": "CONDITIONAL",
                "join_policy": "B",
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
        f"Join CONDITIONAL; Policy B (bar_end < t); no CF; no Poly last; no policy A\n"
        f"Full: `{arch_md}`\n"
    )
    audit_path.write_text(
        "# Audit pointer\n\n"
        f"- TEST: `{TEST_ID}`\n"
        f"- Package: `{PACKAGE}` vs `{INCUMBENT}`\n"
        f"- Feature: `{FEATURE_ID}`\n"
        f"- Gate: `{GATE_ID}`\n"
        f"- Verdict: `{overall}`\n"
        f"- invented_numbers: false\n"
        f"- Trading: FORBIDDEN\n"
        f"- Join: CONDITIONAL · Policy B (bar_end < decision_time)\n"
        f"- no CF; no Poly last; no policy A\n"
        f"- Map 2 / Φ(z) / sibling / L3 / Binance: not used\n"
        f"- SHA256 verified: `{digest}`\n"
        f"- Headlines: `{HEADLINE_BTC}`, `{HEADLINE_ETH}`\n"
        f"- Artifacts: `{out_json}`\n"
        f"- Archive: `{arch_json}`\n"
        f"- DATA: PM-003 + PM-001 OPEN/CLOSE + CB-001 1m Policy B\n"
        f"- Purpose: CB-VEL Coinbase 1m velocity incrementality (USED_RESEARCH; not validation)\n"
    )

    print(f"TEST_ID={TEST_ID}")
    print(f"overall_verdict={overall}")
    print(f"sha256_verified={digest}")
    print(f"n_speak={filt['n_speak']} n_abstain={filt['n_abstain']}")
    for cid in HEADLINES:
        p = headlines[cid]
        print(
            f"HEADLINE\t{cid}\tN={p['N']}\tspeak={p['n_speak']}\t"
            f"speak_rate={p['speak_rate']}\t"
            f"dB={p['ΔBrier']}\tdLL={p['ΔLogLoss']}\tverdict={p['cell_verdict']}"
        )
    for cid in HEADLINES:
        z = placebos["lambda_0"][cid]
        print(
            f"PLACEBO_λ0\t{cid}\tdB={z['ΔBrier']}\tdLL={z['ΔLogLoss']}\tok={z['lambda0_delta_zero']}"
        )
    print(f"wrote {out_json}")
    print(f"wrote {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
