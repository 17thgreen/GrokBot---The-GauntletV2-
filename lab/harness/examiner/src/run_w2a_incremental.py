#!/usr/bin/env python3
"""TEST-20260913-004 — W2A-INCREMENTAL vs MKT-KALSHI-15M-MID.

Clipped CF−mid basis (λ=0.20, w=0.005, c=0.10 frozen) on
DRAFT-ABST-20260913-003 T-14m headlines only. Policy B CF hour-tape join.
No Map 2. No Φ(z). No sibling blend. No L3. No Poly. No annex.
No close-minute extractor. invented_numbers=false. Trading FORBIDDEN.
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
from src.w2a_incremental import (  # noqa: E402
    ASSET_TO_INDEX,
    C_ROBUST,
    C_SCORED,
    EPS,
    HEADLINE_BTC,
    HEADLINE_ETH,
    HEADLINES,
    LAMBDA_ROBUST,
    LAMBDA_SCORED,
    MIN_N_KILL,
    PLACEBO_SEED,
    W_ROBUST,
    W_SCORED,
    W2ARow,
    apply_map,
    gate_decision,
    package_verdict,
    placebo_flip_sign_d,
    placebo_lambda_zero,
    placebo_shuffle_cf,
    score_forecast,
    signed_distance,
)

LAB = Path("/workspace/lab")
CHECKPOINTS = LAB / "data/DATA-PROV-PM-003/derived/checkpoints.ndjson"
COVERAGE = LAB / "data/DATA-PROV-PM-003/derived/contract_coverage.ndjson"
KALSHI_LABELS = LAB / "data/DATA-PROV-PM-001/normalized/kalshi_15m_btc_eth_resolved.ndjson"
CF_RAW = LAB / "data/DATA-PROV-CF-001/raw"
OUT_DIR = LAB / "harness/examiner/out"
ARCHIVE_TESTS = LAB / "archive/tests"
ARCHIVE_AUDIT = LAB / "archive/audit"

TEST_ID = "TEST-20260913-004"
PACKAGE = "W2A-INCREMENTAL"
INCUMBENT = "MKT-KALSHI-15M-MID"
FEATURE_ID = "DRAFT-FEAT-20260913-003"
GATE_ID = "DRAFT-ABST-20260913-003"

AUTHORITY = [
    "governance/EXAMINER_ORDER_TEST-20260913-004-W2A.md",
    "governance/W2A_INCOMPLETE_SECOND_POLICY_2026-09-13.md",
    "archive/features/DRAFT-FEAT-20260913-003-W2A-cf-mid-basis.md",
    "archive/features/DRAFT-ABST-20260913-003-W2A-uncertainty.md",
    "data/DATA-PROV-CF-001/provenance/DATA_VERDICT_W2A_CF_T14_JOIN.md",
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


def _is_void(lab: dict[str, Any]) -> bool:
    st = str(lab.get("STATUS") or "").upper()
    res = str(lab.get("RESOLUTION") or "").upper()
    return st in ("VOID", "DISPUTED") or res in ("VOID", "DISPUTED")


def _hour_key_from_unix_s(unix_s: int) -> str:
    return datetime.fromtimestamp((unix_s // 3600) * 3600, tz=timezone.utc).strftime(
        "%Y-%m-%dT%H"
    )


def load_hour_prints_for_seconds(
    index: str, needed_secs: set[int]
) -> tuple[dict[int, list[tuple[int, float]]], list[str], list[str]]:
    prints_by_sec: dict[int, list[tuple[int, float]]] = defaultdict(list)
    hours = sorted({_hour_key_from_unix_s(s) for s in needed_secs})
    loaded: list[str] = []
    missing: list[str] = []
    for h in hours:
        path = CF_RAW / f"{index}_HOUR_{h}.json"
        if not path.exists():
            missing.append(h)
            continue
        payload = json.loads(path.read_text())["data"]["payload"]
        loaded.append(h)
        hour_secs = {s for s in needed_secs if _hour_key_from_unix_s(s) == h}
        for x in payload:
            sec = int(x["time"]) // 1000
            if sec not in hour_secs:
                continue
            prints_by_sec[sec].append((int(x["time"]), float(x["value"])))
    return dict(prints_by_sec), loaded, missing


def last_in_second_le(
    prints_by_sec: dict[int, list[tuple[int, float]]], sec: int, t_ms: int
) -> tuple[int, float] | None:
    cands = [(tm, v) for tm, v in prints_by_sec.get(sec, []) if tm <= t_ms]
    if not cands:
        return None
    return max(cands, key=lambda x: x[0])


def policy_b_cf(
    prints_by_sec: dict[int, list[tuple[int, float]]],
    decision_time_ms: int,
) -> tuple[Optional[float], Optional[int], Optional[int], bool]:
    """Policy B completed-second join (locked).

    s = floor(decision_time_ms / 1000)
    cf_t = last-in-second on (s-1) when on-second; else last-in-second on s.
    require print exists AND timestamp_ms <= decision_time_ms
    require (s-1) completed: s*1000 <= decision_time_ms (always true for on-second)
    """
    s = decision_time_ms // 1000
    # Completed-second safe: if t%1000==0 use s-1; else A (current s)
    if decision_time_ms % 1000 == 0:
        # require completed: s*1000 <= decision_time_ms (equality on boundary)
        if s * 1000 > decision_time_ms:
            return None, None, None, False
        s_b = s - 1
    else:
        s_b = s
    hit = last_in_second_le(prints_by_sec, s_b, decision_time_ms)
    if hit is None:
        return None, None, None, False
    cf_ms, cf_val = hit
    if cf_ms > decision_time_ms:
        return None, None, None, False
    lag = int(decision_time_ms - cf_ms)
    return float(cf_val), int(cf_ms), lag, True


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
) -> tuple[dict[str, list[W2ARow]], dict[str, Any]]:
    cells: dict[str, list[W2ARow]] = {cid: [] for cid in HEADLINES}
    stats: dict[str, Any] = {
        "candidates": 0,
        "excluded_method_not_mid": 0,
        "excluded_near_deg": 0,
        "excluded_void_or_other": 0,
        "excluded_no_y": 0,
        "scored": 0,
        "n_speak": 0,
        "n_abstain": 0,
        "n_fail_closed_missing_K": 0,
        "n_fail_closed_missing_cf": 0,
        "n_fail_closed_K_not_knowable": 0,
        "n_fail_closed_locked": 0,
        "n_on_second": 0,
        "close_minute_extractor_used": False,
        "join_A_used_as_headline": False,
        "policy": "B",
        "join_verdict": "CONDITIONAL",
        "per_cell": {
            cid: {
                "candidates": 0,
                "scored": 0,
                "speak": 0,
                "abstain": 0,
                "fail_closed_K": 0,
                "fail_closed_cf": 0,
                "fail_closed_locked": 0,
                "excluded_method_not_mid": 0,
                "excluded_near_deg": 0,
                "excluded_void": 0,
            }
            for cid in HEADLINES
        },
        "void_bucket": [],
        "cf_hours_loaded": {"BTC": [], "ETH": []},
        "cf_hours_missing": {"BTC": [], "ETH": []},
        "L3_used": False,
        "poly_used": False,
        "map2_used": False,
        "binance_used": False,
    }

    # Pre-filter candidates and collect needed seconds per asset
    candidates_by_asset: dict[str, list[dict]] = {"BTC": [], "ETH": []}
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
        candidates_by_asset[asset].append(r)

    # Load CF hour tapes for needed seconds (s and s-1)
    prints: dict[str, dict[int, list[tuple[int, float]]]] = {}
    for asset, rows in candidates_by_asset.items():
        needed: set[int] = set()
        for r in rows:
            t_ms = _parse_decision_ms(r.get("decision_time") or "")
            s = t_ms // 1000
            needed.add(s)
            needed.add(s - 1)
        index = ASSET_TO_INDEX[asset]
        pbs, loaded, missing = load_hour_prints_for_seconds(index, needed)
        prints[asset] = pbs
        stats["cf_hours_loaded"][asset] = loaded
        stats["cf_hours_missing"][asset] = missing

    for asset, rows in candidates_by_asset.items():
        for r in rows:
            rem = int(r["time_remaining_sec"])
            cell = primary_cell_id(asset, rem)
            cs = stats["per_cell"][cell]
            m_t = float(m_t_from_checkpoint(r))
            dt = r.get("decision_time") or ""
            decision_ms = _parse_decision_ms(dt)
            if decision_ms % 1000 == 0:
                stats["n_on_second"] += 1

            # K = FLOOR_STRIKE; knowable iff present AND OPEN_TIME <= decision_time
            k: Optional[float] = None
            k_raw = r.get("FLOOR_STRIKE")
            k_present = False
            if k_raw is not None:
                try:
                    k_f = float(k_raw)
                    if math.isfinite(k_f) and k_f > 0:
                        k = k_f
                        k_present = True
                except (TypeError, ValueError):
                    k = None
                    k_present = False

            open_time = r.get("OPEN_TIME") or r.get("open_time") or ""
            close_time = r.get("CLOSE_TIME") or r.get("close_time") or ""
            k_knowable = False
            if k_present and open_time:
                try:
                    open_ms = _parse_decision_ms(open_time)
                    k_knowable = open_ms <= decision_ms
                except Exception:
                    k_knowable = False
            if not k_present:
                stats["n_fail_closed_missing_K"] += 1
                cs["fail_closed_K"] += 1
            elif not k_knowable:
                stats["n_fail_closed_K_not_knowable"] += 1
                cs["fail_closed_K"] += 1

            # close-window lock check
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

            # Policy B CF join
            cf_t, cf_ms, lag_ms, cf_ok = policy_b_cf(prints[asset], decision_ms)
            if not cf_ok:
                stats["n_fail_closed_missing_cf"] += 1
                cs["fail_closed_cf"] += 1

            mid_ok = True  # already filtered
            k_ok = k_knowable and k is not None
            gate = gate_decision(
                cell,
                mid_ok=mid_ok,
                cf_ok=cf_ok,
                k_ok=k_ok,
                not_locked=not_locked,
            )
            speak = gate == "ALLOW_SPEAK_HEADLINE"
            d: Optional[float] = None
            if speak and k is not None and cf_t is not None:
                d = signed_distance(cf_t, k)

            if speak:
                stats["n_speak"] += 1
                cs["speak"] += 1
            else:
                stats["n_abstain"] += 1
                cs["abstain"] += 1

            cells[cell].append(
                W2ARow(
                    cell_id=cell,
                    contract_id=r["contract_id"],
                    asset=asset,
                    checkpoint=KALSHI_REM_TO_LABEL[rem],
                    time_remaining_sec=rem,
                    decision_time=dt,
                    decision_time_ms=decision_ms,
                    open_time=str(open_time),
                    close_time=str(close_time),
                    m_t=m_t,
                    y=int(resolve_y(r.get("RESOLUTION"))),
                    k=k if k_ok else None,
                    cf_t=cf_t if cf_ok else None,
                    cf_print_time_ms=cf_ms if cf_ok else None,
                    cf_lag_ms=lag_ms if cf_ok else None,
                    d=d,
                    gate=gate,
                    k_ok=k_ok,
                    cf_ok=cf_ok,
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
        f"**Feature:** `{FEATURE_ID}` (clipped CF−mid basis, "
        f"λ={LAMBDA_SCORED} w={W_SCORED} c={C_SCORED} frozen)"
    )
    lines.append(
        f"**Gate:** `{GATE_ID}` (speak only on BTC/ETH T-14m mid under uncertainty)"
    )
    lines.append(f"**Incumbent:** `{payload['incumbent']}` (TEST-20260911-007 mid-only)")
    lines.append(
        "**Purpose:** W2-A clipped CF−mid basis incrementality on two AMD-005 headlines"
    )
    lines.append(
        f"**DATA:** `{payload['data']['dataset_id']}` + `{payload['data']['cf_dataset_id']}` "
        "+ PM-001 FLOOR_STRIKE / OPEN / CLOSE / RESOLUTION"
    )
    lines.append(
        "**Join:** DATA_VERDICT_W2A_CF_T14_JOIN **CONDITIONAL** "
        "· Policy B (completed-second s−1) · K revision [A] · "
        "close-minute CLEARED ≠ this join"
    )
    lines.append("**Slice use:** USED_RESEARCH — not validation, not sealed holdout")
    lines.append(f"**Overall verdict:** `{payload['overall_verdict']}`")
    lines.append(f"**invented_numbers:** `{payload['invented_numbers']}`")
    lines.append("**Trading:** FORBIDDEN")
    lines.append(
        "**Stamp:** Join **CONDITIONAL**. Policy B (completed-second s−1). "
        "K revision [A]. close-minute CLEARED ≠ this join. "
        "No Map 2. No L3. No Poly. No Φ(z). No sibling blend. No W2-E."
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
    lines.append("- d = (cf − K) / K")
    lines.append(
        f"- q = clip(0.5 + 0.5·clip(d/w, −1, +1), ε, 1−ε) with w={W_SCORED}, ε={EPS}"
    )
    lines.append(f"- b = q − m; b_clip = clip(b, −c, +c) with c={C_SCORED}")
    lines.append("- if ABSTAIN or missing cf/K/m or locked: p = m")
    lines.append(
        f"- else ALLOW_SPEAK: p = clip(m + λ·b_clip, ε, 1−ε) with λ={LAMBDA_SCORED}"
    )
    lines.append(
        f"- λ={LAMBDA_SCORED}, w={W_SCORED}, c={C_SCORED} frozen. "
        f"Robustness annex λ∈{list(LAMBDA_ROBUST)} / c∈{list(C_ROBUST)} / "
        f"w∈{list(W_ROBUST)} — do not pick winner. λ=0 ⇒ Δ=0."
    )
    lines.append("")
    lines.append("## Filters / join")
    lines.append("- venue=KALSHI, window=15m; BTC/ETH **separate** (no pool)")
    lines.append("- DATA-PROV-PM-003 1208-slice only — **no** PM-002 union")
    lines.append("- Headlines only: T-14m (rem=840); **no annex**")
    lines.append("- `implied_p_method == mid` only; last-fallback excluded")
    lines.append("- exclude `implied_p ≤ 0.02` or `≥ 0.98` (near-deg)")
    lines.append("- VOID/DISPUTED out of scored N")
    lines.append("- K = PM-001 `FLOOR_STRIKE` after OPEN (OPEN_TIME ≤ decision_time) [A]")
    lines.append(
        "- cf_t = Policy B: last-in-second on completed second s−1 from "
        "DATA-PROV-CF-001 hour tape (BRTI / ETHUSD_RTI); print.time ≤ decision_time_ms"
    )
    lines.append("- Missing cf/K/m or inside close-minute → fail-closed p_t := m_t")
    lines.append(
        "- **NOT** close-minute CLEARED extractor. **NOT** Join A as headline. "
        "**NOT** Binance. **NOT** L3. **NOT** Map 2. **NOT** Φ(z)."
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
        "mean(d)_speak | speak_rate | ECE | Verdict |"
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
            f"{_fmt_num(c.get('mean(p)_speak'), 4)} | {_fmt_num(c.get('mean(d)_speak'))} | "
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
            f"mean(cf_t)={_fmt_num(c.get('mean(cf_t)'))}; mean(K)={_fmt_num(c.get('mean(K)'))}"
        )
        lines.append(f"- Reason: {c['cell_reason']}")
        lines.append(f"- Calibration: {c['Calibration']['note']}")
        lines.append(f"- ECE_market: {_fmt_num(c.get('ECE_market'))}")
        lines.append("- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no trading)")
        lines.append("")

    lines.append(
        "## Robustness annex (λ×c×w grids; not headline; do not pick winner)"
    )
    lines.append("")
    lines.append("| Cell | λ | c | w | N | ΔBrier | ΔLogLoss | Verdict |")
    lines.append("|------|--:|--:|--:|--:|-------:|---------:|---------|")
    for cid in HEADLINES:
        for key, block in payload["robustness"][cid].items():
            lines.append(
                f"| `{cid}` | {block.get('λ', '')} | {block.get('c', '')} | "
                f"{block.get('w', '')} | {block['N']} | {_fmt_num(block['ΔBrier'])} | "
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
    lines.append("- Join policy: **B** (completed-second s−1)")
    lines.append("- K revision: **[A]** (static dump; no revision feed)")
    lines.append("- close-minute CLEARED extractor: **not used** (≠ this join)")
    lines.append("- Join A as headline: **not used**")
    lines.append("- Map 2 / Φ(z) / sibling blend / W2-E / L3 / Poly / Binance: **not used**")
    lines.append("- EXPIRATION_VALUE: **not read / not scored**")
    lines.append("- No λ/w/c retune; no gate retune; no annex sneak; no pool")
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
        "Join CONDITIONAL; Policy B; K revision [A]; "
        "close-minute CLEARED ≠ this join\n"
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
    cells, filt = collect_headline_rows(enriched)
    filt["enrich"] = enrich_stats

    if filt["close_minute_extractor_used"] or filt["join_A_used_as_headline"]:
        return _write_integrity_fail("forbidden close-minute / Join A used as headline")
    if filt["L3_used"] or filt["poly_used"] or filt["map2_used"] or filt["binance_used"]:
        return _write_integrity_fail("forbidden L3/Poly/Map2/Binance used")

    map_label = (
        f"clipped CF-mid basis: d=(cf-K)/K; q=clip(0.5+0.5*clip(d/{W_SCORED},-1,1),{EPS},1-{EPS}); "
        f"b_clip=clip(q-m,-{C_SCORED},{C_SCORED}); "
        f"p=clip(m+{LAMBDA_SCORED}*b_clip,{EPS},1-{EPS}) on ALLOW_SPEAK; else p=m; Policy B"
    )

    headlines: dict[str, Any] = {}
    for cid in HEADLINES:
        rows = sorted(
            cells[cid],
            key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec),
        )
        cells[cid] = rows
        ps = apply_map(rows, lam=LAMBDA_SCORED, w=W_SCORED, c=C_SCORED)
        headlines[cid] = score_forecast(
            rows, ps, feature_id=FEATURE_ID, map_label=map_label
        )

    # Robustness: λ × c × w grid (annex only — do not pick winner)
    robustness: dict[str, dict[str, Any]] = {}
    for cid in HEADLINES:
        rows = cells[cid]
        rob: dict[str, Any] = {}
        for lam in LAMBDA_ROBUST:
            for c in C_ROBUST:
                for w in W_ROBUST:
                    key = f"λ={lam}|c={c}|w={w}"
                    ps = apply_map(rows, lam=lam, w=w, c=c)
                    block = score_forecast(
                        rows,
                        ps,
                        feature_id=FEATURE_ID,
                        map_label=f"robustness {key}",
                    )
                    block["λ"] = lam
                    block["c"] = c
                    block["w"] = w
                    block.pop("contract_ids_scored", None)
                    rob[key] = block
        robustness[cid] = rob

    # Placebos
    placebos: dict[str, dict[str, Any]] = {
        "lambda_0": {},
        "flip_sign_d": {},
        "shuffle_cf": {},
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

        pf = placebo_flip_sign_d(rows, cid)
        ordered_f = sorted(
            rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec)
        )
        bf = score_forecast(
            ordered_f, pf, feature_id=FEATURE_ID, map_label="placebo flip sign(d)"
        )
        bf.pop("contract_ids_scored", None)
        bf["placebo_note"] = "sign(d) flipped; should not beat true sign"
        placebos["flip_sign_d"][cid] = bf

        ps = placebo_shuffle_cf(rows, cid)
        ordered_s = sorted(
            rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec)
        )
        bs = score_forecast(
            ordered_s, ps, feature_id=FEATURE_ID, map_label="placebo shuffle cf"
        )
        bs.pop("contract_ids_scored", None)
        bs["placebo_note"] = "cf_t shuffled within cell; K,m fixed"
        placebos["shuffle_cf"][cid] = bs

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
        "purpose": "w2a_clipped_cf_mid_basis_incrementality",
        "strategy": None,
        "trading": "FORBIDDEN",
        "invented_numbers": False,
        "join_verdict": "CONDITIONAL",
        "join_policy": "B",
        "K_revision": "[A]",
        "close_minute_CLEARED_ne_this_join": True,
        "overall_verdict": overall,
        "overall_reason": reason,
        "run_utc": run_utc,
        "authority": AUTHORITY,
        "frozen_map": {
            "λ": LAMBDA_SCORED,
            "w": W_SCORED,
            "c": C_SCORED,
            "ε": EPS,
            "formula": map_label,
            "no_phi_z": True,
            "no_sibling_blend": True,
            "no_map2": True,
            "no_annex": True,
            "no_L3": True,
            "policy_B_only": True,
        },
        "stamps": {
            "join": "CONDITIONAL",
            "policy": "B (completed-second s−1)",
            "K_revision": "[A]",
            "close_minute_CLEARED_ne_this_join": True,
        },
        "data": {
            "dataset_id": "DATA-PROV-PM-003",
            "cf_dataset_id": "DATA-PROV-CF-001",
            "slice_use": "USED_RESEARCH",
            "checkpoints": str(CHECKPOINTS),
            "checkpoints_sha256": digest,
            "checkpoints_sha256_expected": EXPECTED_CHECKPOINTS_SHA256,
            "sha256_verified": digest == EXPECTED_CHECKPOINTS_SHA256,
            "labels_kalshi": str(KALSHI_LABELS),
            "cf_raw": str(CF_RAW),
            "m_t_source": "DATA-PROV-PM-003 derived checkpoints.implied_p (mid)",
            "K_source": "DATA-PROV-PM-001 FLOOR_STRIKE (OPEN_TIME<=decision_time) [A]",
            "cf_t_source": (
                "DATA-PROV-CF-001 hour tape Policy B: last-in-second on completed "
                "second s−1 (BRTI/ETHUSD_RTI); print.time<=decision_time_ms"
            ),
            "join_verdict": "CONDITIONAL",
            "join_policy": "B",
            "forbidden": [
                "close-minute CLEARED extractor",
                "Join A as headline",
                "Map 2",
                "Φ(z)",
                "sibling blend",
                "W2-E",
                "L3",
                "Poly",
                "Binance",
                "EXPIRATION_VALUE",
                "T−1 mid",
                "raw 0/1",
                "retune λ/w/c",
            ],
            "pm002_checkpoints_read": False,
            "poly_scored": False,
            "l3_used": False,
            "close_minute_used": False,
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
            "close_minute_extractor_used": False,
            "join_A_used_as_headline": False,
            "invented_numbers": False,
            "trading": False,
            "phi_z_used": False,
            "sibling_blend_used": False,
            "map2_used": False,
            "L3_used": False,
            "poly_used": False,
            "binance_used": False,
            "w2e_used": False,
            "join_policy": "B",
            "join_verdict": "CONDITIONAL",
            "K_revision": "[A]",
            "close_minute_CLEARED_ne_this_join": True,
        },
        "forbidden_actions": [
            "in-sample refit",
            "retune λ/w/c",
            "retune gate / annex sneak",
            "PM-002 union",
            "Poly",
            "L3",
            "Map 2",
            "Φ(z)",
            "sibling blend",
            "W2-E",
            "close-minute extractor",
            "Join A as headline",
            "Binance",
            "EXPIRATION_VALUE",
            "T−1 mid",
            "raw 0/1",
            "trading",
            "invented numbers",
            "pick λ/w/c winner from robustness grid",
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
                "K_revision": "[A]",
                "close_minute_CLEARED_ne_this_join": True,
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
        f"Join CONDITIONAL; Policy B (completed-second s−1); K revision [A]\n"
        f"close-minute CLEARED ≠ this join\n"
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
        f"- Join: CONDITIONAL · Policy B (completed-second s−1)\n"
        f"- K revision: [A]\n"
        f"- close-minute CLEARED ≠ this join\n"
        f"- Map 2 / Φ(z) / sibling / W2-E / L3 / Poly: not used\n"
        f"- SHA256 verified: `{digest}`\n"
        f"- Headlines: `{HEADLINE_BTC}`, `{HEADLINE_ETH}`\n"
        f"- Artifacts: `{out_json}`\n"
        f"- Archive: `{arch_json}`\n"
        f"- DATA: PM-003 + PM-001 FLOOR_STRIKE/OPEN/CLOSE + CF-001 hour tape Policy B\n"
        f"- Purpose: W2-A clipped CF−mid basis incrementality (USED_RESEARCH; not validation)\n"
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
