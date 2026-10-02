#!/usr/bin/env python3
"""TEST-20260913-003 — W2E-INCREMENTAL vs MKT-KALSHI-15M-MID.

Strike-distance vs mid disagreement pull (λ=0.25, δ=0.002 frozen)
on DRAFT-ABST-20260913-002 T-5m headlines only. No annex. No Φ(z).
No sibling blend. No CF. No Poly. No EXPIRATION_VALUE. L3 ≠ oracle.
invented_numbers=false. Trading FORBIDDEN.
"""

from __future__ import annotations

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import numpy as np
import pyarrow.parquet as pq

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
from src.w2e_incremental import (  # noqa: E402
    DELTA_ROBUST,
    DELTA_SCORED,
    EPS,
    HEADLINE_BTC,
    HEADLINE_ETH,
    HEADLINES,
    LAMBDA_ROBUST,
    LAMBDA_SCORED,
    MIN_N_KILL,
    PLACEBO_SEED,
    S_MAX_LAG_MS,
    W2ERow,
    apply_map,
    gate_decision,
    is_agree,
    package_verdict,
    placebo_flip_sign_d,
    placebo_lambda_zero,
    placebo_shuffle_s,
    score_forecast,
    signed_distance,
)

LAB = Path("/workspace/lab")
CHECKPOINTS = LAB / "data/DATA-PROV-PM-003/derived/checkpoints.ndjson"
COVERAGE = LAB / "data/DATA-PROV-PM-003/derived/contract_coverage.ndjson"
KALSHI_LABELS = LAB / "data/DATA-PROV-PM-001/normalized/kalshi_15m_btc_eth_resolved.ndjson"
L3_BTC = LAB / "data/DATA-PROV-L3-001/derived/BTCUSDT_1m_spot_2026-09-04_2026-09-11.parquet"
L3_ETH = LAB / "data/DATA-PROV-L3-001/derived/ETHUSDT_1m_spot_2026-09-04_2026-09-11.parquet"
OUT_DIR = LAB / "harness/examiner/out"
ARCHIVE_TESTS = LAB / "archive/tests"
ARCHIVE_AUDIT = LAB / "archive/audit"

TEST_ID = "TEST-20260913-003"
PACKAGE = "W2E-INCREMENTAL"
INCUMBENT = "MKT-KALSHI-15M-MID"
FEATURE_ID = "DRAFT-FEAT-20260913-002"
GATE_ID = "DRAFT-ABST-20260913-002"

AUTHORITY = [
    "governance/EXAMINER_ORDER_TEST-20260913-003-W2E.md",
    "archive/features/DRAFT-FEAT-20260913-002-W2E-strike-vs-mid.md",
    "archive/features/DRAFT-ABST-20260913-002-W2E-rules-strike.md",
    "data/DATA-PROV-L3-001/provenance/DATA_VERDICT_W2E_STRIKE_L3_JOIN.md",
]

TARGET_REM = 300  # T-5m only; no annex


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


class L3Book:
    """Completed-bar L3 join (F1 reuse). L3 ≠ oracle."""

    def __init__(self, path: Path, asset: str):
        table = pq.read_table(
            path,
            columns=["open_time_ms", "close_time_ms", "close"],
        )
        open_ms = np.asarray(table.column("open_time_ms").to_numpy(), dtype=np.int64)
        close_ms = np.asarray(table.column("close_time_ms").to_numpy(), dtype=np.int64)
        closes = np.asarray(table.column("close").to_numpy(), dtype=np.float64)
        order = np.argsort(close_ms, kind="mergesort")
        self.asset = asset
        self.open_ms = open_ms[order]
        self.close_ms = close_ms[order]
        self.closes = closes[order]

    def knowable_idx(self, decision_time_ms: int) -> Optional[int]:
        j = int(np.searchsorted(self.close_ms, decision_time_ms, side="right") - 1)
        if j < 0:
            return None
        return j

    def price_at_t(self, decision_time_ms: int) -> Optional[dict[str, Any]]:
        j = self.knowable_idx(decision_time_ms)
        if j is None:
            return None
        lag = decision_time_ms - int(self.close_ms[j])
        if lag < 0:
            raise RuntimeError("lookahead: close_time_ms > decision_time_ms")
        if lag > S_MAX_LAG_MS:
            return None
        open_ms = int(self.open_ms[j])
        join_ok = open_ms == decision_time_ms - 60_000
        if open_ms == (decision_time_ms // 60_000) * 60_000:
            raise RuntimeError(
                "BLOCKED incomplete-bar join attempted "
                f"(open_ms={open_ms}, decision_ms={decision_time_ms})"
            )
        return {
            "idx": j,
            "s_t": float(self.closes[j]),
            "open_time_ms": open_ms,
            "close_time_ms": int(self.close_ms[j]),
            "lag_ms": int(lag),
            "join_ok_open_eq_decision_minus_60s": join_ok,
        }


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
        er["_label"] = lab
        enriched.append(er)
    return enriched, stats


def collect_headline_rows(
    enriched: list[dict],
    books: dict[str, L3Book],
) -> tuple[dict[str, list[W2ERow]], dict[str, Any]]:
    cells: dict[str, list[W2ERow]] = {cid: [] for cid in HEADLINES}
    stats: dict[str, Any] = {
        "candidates": 0,
        "excluded_method_not_mid": 0,
        "excluded_near_deg": 0,
        "excluded_void_or_other": 0,
        "excluded_no_y": 0,
        "scored": 0,
        "n_speak": 0,
        "n_agree": 0,
        "n_fail_closed_missing_K": 0,
        "n_fail_closed_missing_S": 0,
        "n_fail_closed_K_not_knowable": 0,
        "join_open_eq_decision_minus_60s": 0,
        "join_open_ne_decision_minus_60s": 0,
        "expiration_value_read": False,
        "incomplete_bar_used": False,
        "per_cell": {
            cid: {
                "candidates": 0,
                "scored": 0,
                "speak": 0,
                "agree": 0,
                "fail_closed_K": 0,
                "fail_closed_S": 0,
                "excluded_method_not_mid": 0,
                "excluded_near_deg": 0,
                "excluded_void": 0,
            }
            for cid in HEADLINES
        },
        "void_bucket": [],
        "L3_is_oracle": False,
        "join_verdict": "CONDITIONAL",
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

        # S_t L3 completed bar
        join = books[asset].price_at_t(decision_ms)
        s_t: Optional[float] = None
        bar_open: Optional[int] = None
        bar_close: Optional[int] = None
        lag_ms: Optional[int] = None
        s_ok = False
        if join is None:
            stats["n_fail_closed_missing_S"] += 1
            cs["fail_closed_S"] += 1
        else:
            s_t = join["s_t"]
            bar_open = join["open_time_ms"]
            bar_close = join["close_time_ms"]
            lag_ms = join["lag_ms"]
            s_ok = True
            if join["join_ok_open_eq_decision_minus_60s"]:
                stats["join_open_eq_decision_minus_60s"] += 1
            else:
                stats["join_open_ne_decision_minus_60s"] += 1

        gate = gate_decision(cell, k_knowable=k_knowable and s_ok)
        # Feature: ALLOW only when K knowable; missing S also fail-closed → treat as ABSTAIN
        if not (k_knowable and s_ok):
            gate = "ABSTAIN"

        d: Optional[float] = None
        agree: Optional[bool] = None
        speak = False
        if gate == "ALLOW_SPEAK_HEADLINE" and k is not None and s_t is not None:
            d = signed_distance(s_t, k)
            if d is not None:
                agree = is_agree(d, m_t)
                speak = not agree
                if agree:
                    stats["n_agree"] += 1
                    cs["agree"] += 1
                else:
                    stats["n_speak"] += 1
                    cs["speak"] += 1

        cells[cell].append(
            W2ERow(
                cell_id=cell,
                contract_id=r["contract_id"],
                asset=asset,
                checkpoint=KALSHI_REM_TO_LABEL[int(rem)],
                time_remaining_sec=int(rem),
                decision_time=dt,
                decision_time_ms=decision_ms,
                open_time=str(open_time),
                m_t=m_t,
                y=y,
                k=k if k_knowable else None,
                s_t=s_t if s_ok else None,
                d=d,
                bar_open_time_ms=bar_open,
                bar_close_time_ms=bar_close,
                lag_ms=lag_ms,
                gate=gate,
                k_knowable=k_knowable,
                s_ok=s_ok,
                agree=agree,
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
        f"**Feature:** `{FEATURE_ID}` (FLOOR_STRIKE signed distance vs mid, "
        f"λ={LAMBDA_SCORED} δ={DELTA_SCORED} frozen; disagreement pull)"
    )
    lines.append(
        f"**Gate:** `{GATE_ID}` (speak only on BTC/ETH T-5m mid when FLOOR_STRIKE knowable)"
    )
    lines.append(f"**Incumbent:** `{payload['incumbent']}` (TEST-20260911-007 mid-only)")
    lines.append(
        "**Purpose:** W2-E strike-distance vs mid incrementality on two AMD-005 headlines"
    )
    lines.append(
        f"**DATA:** `{payload['data']['dataset_id']}` + `{payload['data']['l3_dataset_id']}` "
        "+ PM-001 FLOOR_STRIKE / RESOLUTION"
    )
    lines.append(
        "**Join:** DATA_VERDICT_W2E_STRIKE_L3_JOIN **CONDITIONAL** "
        "(L3 ≠ oracle; K revision [A])"
    )
    lines.append("**Slice use:** USED_RESEARCH — not validation, not sealed holdout")
    lines.append(f"**Overall verdict:** `{payload['overall_verdict']}`")
    lines.append(f"**invented_numbers:** `{payload['invented_numbers']}`")
    lines.append("**Trading:** FORBIDDEN")
    lines.append(
        "**Stamp:** L3 is **not** the CF/Kalshi settlement oracle. CONDITIONAL join. "
        "No CF. No Poly. No EXPIRATION_VALUE. No Φ(z). No sibling blend."
    )
    lines.append("**Annex:** none (no W2-C cells; no other rem)")
    lines.append(f"**Run UTC:** `{payload['run_utc']}`")
    lines.append(f"**SHA256 verified:** `{payload['data']['sha256_verified']}`")
    lines.append("")
    lines.append("## Authority")
    for a in payload["authority"]:
        lines.append(f"- `{a}`")
    lines.append("")
    lines.append("## Frozen map")
    lines.append("- d = (S − K) / K")
    lines.append(
        f"- p_dist = 0.5 + 0.5·clip(d/δ, −1, 1) with δ={DELTA_SCORED}; "
        f"clip to [{EPS}, 1−{EPS}]"
    )
    lines.append("- agree = (d==0) or (m==0.5) or sign(d)==sign(m−0.5)")
    lines.append("- if ABSTAIN or missing K/S: p = m")
    lines.append("- elif agree: p = m")
    lines.append(
        f"- else: p = clip((1−{LAMBDA_SCORED})·m + {LAMBDA_SCORED}·p_dist, {EPS}, 1−{EPS})"
    )
    lines.append(
        f"- λ={LAMBDA_SCORED}, δ={DELTA_SCORED} frozen. "
        f"Robustness annex λ∈{list(LAMBDA_ROBUST)} / δ∈{list(DELTA_ROBUST)} — "
        "do not pick winner. λ=0 ⇒ Δ=0."
    )
    lines.append("")
    lines.append("## Filters / join")
    lines.append("- venue=KALSHI, window=15m; BTC/ETH **separate** (no pool)")
    lines.append("- DATA-PROV-PM-003 1208-slice only — **no** PM-002 union")
    lines.append("- Headlines only: T-5m (rem=300); **no annex**")
    lines.append("- `implied_p_method == mid` only; last-fallback excluded")
    lines.append("- exclude `implied_p ≤ 0.02` or `≥ 0.98` (near-deg)")
    lines.append("- VOID/DISPUTED out of scored N")
    lines.append("- K = PM-001 `FLOOR_STRIKE` after OPEN (OPEN_TIME ≤ decision_time)")
    lines.append(
        "- S_t = L3 completed 1m close: argmax{bar | close_time_ms ≤ decision_time_ms}; "
        "lag ≤ 90s"
    )
    lines.append("- Missing K or S_t → fail-closed p_t := m_t")
    lines.append("- **L3 ≠ oracle.** No CF. No Poly. No EXPIRATION_VALUE. No Φ(z).")
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
            f"- n_speak={c['n_speak']}; n_agree={c['n_agree']}; "
            f"fail_closed_missing_KS={c['n_fail_closed_missing_KS']}; "
            f"speak_rate={_fmt_num(c.get('speak_rate'), 4)}"
        )
        lines.append(
            f"- mean(m)_all={_fmt_num(c.get('mean(m)_all'), 4)}; "
            f"mean(p)_all={_fmt_num(c.get('mean(p)_all'), 4)}; "
            f"mean(S_t)={_fmt_num(c.get('mean(S_t)'))}; mean(K)={_fmt_num(c.get('mean(K)'))}"
        )
        lines.append(f"- Reason: {c['cell_reason']}")
        lines.append(f"- Calibration: {c['Calibration']['note']}")
        lines.append(f"- ECE_market: {_fmt_num(c.get('ECE_market'))}")
        lines.append("- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no trading)")
        lines.append("")

    lines.append(
        "## Robustness annex (λ×δ grids; not headline; do not pick winner)"
    )
    lines.append("")
    lines.append("| Cell | λ | δ | N | ΔBrier | ΔLogLoss | Verdict |")
    lines.append("|------|--:|--:|--:|-------:|---------:|---------|")
    for cid in HEADLINES:
        for key, block in payload["robustness"][cid].items():
            lines.append(
                f"| `{cid}` | {block.get('λ', key)} | {block.get('δ', '')} | "
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
    lines.append("- **L3 ≠ oracle** (Binance spot proxy only; not CF BRTI / Kalshi settlement)")
    lines.append("- Join verdict: **CONDITIONAL**")
    lines.append("- EXPIRATION_VALUE: **not read / not scored**")
    lines.append("- incomplete-bar close: **not used**")
    lines.append("- Φ(z) / sibling blend / CF / Poly: **not used**")
    lines.append("- No λ/δ retune; no gate retune; no annex sneak; no pool")
    lines.append(
        f"- join open==decision−60s: "
        f"`{payload['filter_stats']['join_open_eq_decision_minus_60s']}`"
    )
    lines.append(
        f"- join open≠decision−60s: "
        f"`{payload['filter_stats']['join_open_ne_decision_minus_60s']}`"
    )
    lines.append("")
    lines.append("## Overall package verdict")
    lines.append(f"**`{payload['overall_verdict']}`** — {payload['overall_reason']}")
    lines.append("")
    lines.append(
        "FAIL-INSUFFICIENT ≠ NO_EDGE. This is **not** a Champion / strategy PASS. "
        "No trading authorization. Holdout closed. L3 ≠ oracle."
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
        "L3_is_oracle": False,
        "join_verdict": "CONDITIONAL",
        "run_utc": run_utc,
        "authority": AUTHORITY,
    }
    out_json = OUT_DIR / f"{out_stem}.json"
    out_md = OUT_DIR / f"{out_stem}.md"
    out_json.write_text(json.dumps(payload, indent=2) + "\n")
    out_md.write_text(
        f"# {TEST_ID} — DATA_INTEGRITY_FAIL\n\n{reason}\n\n"
        "invented_numbers: false\nTrading: FORBIDDEN\nL3 ≠ oracle\n"
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

    books = {
        "BTC": L3Book(L3_BTC, "BTC"),
        "ETH": L3Book(L3_ETH, "ETH"),
    }

    enriched, enrich_stats = enrich_checkpoints(checkpoints, coverage, kalshi_idx)
    cells, filt = collect_headline_rows(enriched, books)
    filt["enrich"] = enrich_stats

    if filt["join_open_ne_decision_minus_60s"] != 0:
        return _write_integrity_fail(
            f"join identity failed: {filt['join_open_ne_decision_minus_60s']} rows "
            "with open_time_ms != decision_time_ms - 60000"
        )
    if filt["expiration_value_read"] or filt["incomplete_bar_used"]:
        return _write_integrity_fail("forbidden field / incomplete bar used")

    map_label = (
        f"disagreement pull: d=(S-K)/K; p_dist=0.5+0.5*clip(d/{DELTA_SCORED},-1,1); "
        f"agree→p=m; else p=clip((1-{LAMBDA_SCORED})m+{LAMBDA_SCORED}*p_dist,{EPS},1-{EPS})"
    )

    headlines: dict[str, Any] = {}
    for cid in HEADLINES:
        rows = cells[cid]
        ps = apply_map(rows, lam=LAMBDA_SCORED, delta=DELTA_SCORED)
        headlines[cid] = score_forecast(
            rows, ps, feature_id=FEATURE_ID, map_label=map_label
        )

    # Robustness: λ × δ grid (annex only)
    robustness: dict[str, dict[str, Any]] = {}
    for cid in HEADLINES:
        rows = cells[cid]
        rob: dict[str, Any] = {}
        for lam in LAMBDA_ROBUST:
            for delta in DELTA_ROBUST:
                key = f"λ={lam}|δ={delta}"
                ps = apply_map(rows, lam=lam, delta=delta)
                block = score_forecast(
                    rows,
                    ps,
                    feature_id=FEATURE_ID,
                    map_label=f"robustness {key}",
                )
                block["λ"] = lam
                block["δ"] = delta
                # strip heavy contract lists from annex
                block.pop("contract_ids_scored", None)
                rob[key] = block
        robustness[cid] = rob

    # Placebos
    placebos: dict[str, dict[str, Any]] = {
        "lambda_0": {},
        "flip_sign_d": {},
        "shuffle_S": {},
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
        placebos["lambda_0"][cid] = b0

        pf = placebo_flip_sign_d(rows, cid)
        # placebo_flip returns on ordered; re-score on ordered
        ordered_f = sorted(
            rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec)
        )
        bf = score_forecast(
            ordered_f, pf, feature_id=FEATURE_ID, map_label="placebo flip sign(d)"
        )
        bf.pop("contract_ids_scored", None)
        bf["placebo_note"] = "sign(d) flipped; should not beat true sign"
        placebos["flip_sign_d"][cid] = bf

        ps = placebo_shuffle_s(rows, cid)
        ordered_s = sorted(
            rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec)
        )
        bs = score_forecast(
            ordered_s, ps, feature_id=FEATURE_ID, map_label="placebo shuffle S"
        )
        bs.pop("contract_ids_scored", None)
        bs["placebo_note"] = "S_t shuffled within cell; K,m fixed"
        placebos["shuffle_S"][cid] = bs

    overall, reason = package_verdict(headlines)
    run_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out_stem = f"{TEST_ID}-{PACKAGE}"
    out_json = OUT_DIR / f"{out_stem}.json"
    out_md = OUT_DIR / f"{out_stem}.md"

    payload: dict[str, Any] = {
        "TEST_ID": TEST_ID,
        "package": PACKAGE,
        "feature_id": FEATURE_ID,
        "gate_id": GATE_ID,
        "incumbent": INCUMBENT,
        "purpose": "w2e_strike_distance_vs_mid_incrementality",
        "strategy": None,
        "trading": "FORBIDDEN",
        "invented_numbers": False,
        "L3_is_oracle": False,
        "join_verdict": "CONDITIONAL",
        "overall_verdict": overall,
        "overall_reason": reason,
        "run_utc": run_utc,
        "authority": AUTHORITY,
        "frozen_map": {
            "λ": LAMBDA_SCORED,
            "δ": DELTA_SCORED,
            "ε": EPS,
            "formula": map_label,
            "no_phi_z": True,
            "no_sibling_blend": True,
            "no_annex": True,
        },
        "data": {
            "dataset_id": "DATA-PROV-PM-003",
            "l3_dataset_id": "DATA-PROV-L3-001",
            "slice_use": "USED_RESEARCH",
            "checkpoints": str(CHECKPOINTS),
            "checkpoints_sha256": digest,
            "checkpoints_sha256_expected": EXPECTED_CHECKPOINTS_SHA256,
            "sha256_verified": digest == EXPECTED_CHECKPOINTS_SHA256,
            "labels_kalshi": str(KALSHI_LABELS),
            "l3_btc": str(L3_BTC),
            "l3_eth": str(L3_ETH),
            "m_t_source": "DATA-PROV-PM-003 derived checkpoints.implied_p (mid)",
            "K_source": "DATA-PROV-PM-001 FLOOR_STRIKE (OPEN_TIME<=decision_time)",
            "S_t_source": (
                "DATA-PROV-L3-001 completed 1m close "
                "(close_time_ms<=decision_time_ms; lag<=90s)"
            ),
            "L3_is_oracle": False,
            "join_verdict": "CONDITIONAL",
            "forbidden": [
                "EXPIRATION_VALUE",
                "CF-as-oracle",
                "Binance L3 as oracle",
                "Φ(z)",
                "sibling blend",
                "Poly",
                "incomplete-bar close",
                "last-fallback-as-mid",
            ],
            "pm002_checkpoints_read": False,
            "poly_scored": False,
            "cf_used": False,
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
            "incomplete_bar_used": False,
            "invented_numbers": False,
            "trading": False,
            "phi_z_used": False,
            "sibling_blend_used": False,
            "cf_used": False,
            "poly_used": False,
            "L3_is_oracle": False,
            "join_rule": "argmax{bar|close_time_ms<=decision_time_ms}; lag<=90s",
            "join_open_eq_decision_minus_60s_all": filt[
                "join_open_ne_decision_minus_60s"
            ]
            == 0,
            "join_verdict": "CONDITIONAL",
        },
        "forbidden_actions": [
            "in-sample refit",
            "retune λ/δ",
            "retune gate / annex sneak",
            "PM-002 union",
            "Poly",
            "CF-as-oracle",
            "EXPIRATION_VALUE",
            "incomplete-bar close",
            "Binance as oracle",
            "Φ(z)",
            "sibling blend",
            "trading",
            "invented numbers",
            "pick λ/δ winner from robustness grid",
            "BTC+ETH pool",
        ],
        "artifact_paths": [],
    }

    # Strip heavy contract id lists from primary for size (keep N small enough)
    for cid in HEADLINES:
        headlines[cid].pop("contract_ids_scored", None)

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
                "L3_is_oracle": False,
                "join_verdict": "CONDITIONAL",
                "EXPIRATION_VALUE_used": False,
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
        f"L3 ≠ oracle; CONDITIONAL join\n"
        f"EXPIRATION_VALUE: not used\n"
        f"Φ(z)/sibling: not used\n"
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
        f"- L3 ≠ oracle; join CONDITIONAL\n"
        f"- EXPIRATION_VALUE: not used\n"
        f"- Φ(z): not used\n"
        f"- sibling blend: not used\n"
        f"- CF / Poly: not used\n"
        f"- SHA256 verified: `{digest}`\n"
        f"- L3: DATA-PROV-L3-001 completed-bar join only (F1 reuse)\n"
        f"- Headlines: `{HEADLINE_BTC}`, `{HEADLINE_ETH}`\n"
        f"- Artifacts: `{out_json}`\n"
        f"- Archive: `{arch_json}`\n"
        f"- DATA: PM-003 + PM-001 FLOOR_STRIKE/RESOLUTION + L3-001\n"
        f"- Purpose: W2-E strike vs mid incrementality (USED_RESEARCH; not validation)\n"
    )

    print(f"TEST_ID={TEST_ID}")
    print(f"overall_verdict={overall}")
    print(f"sha256_verified={digest}")
    print(
        f"join_ok={filt['join_open_eq_decision_minus_60s']} "
        f"join_bad={filt['join_open_ne_decision_minus_60s']}"
    )
    for cid in HEADLINES:
        p = headlines[cid]
        print(
            f"HEADLINE\t{cid}\tN={p['N']}\tspeak={p['n_speak']}\t"
            f"dB={p['ΔBrier']}\tdLL={p['ΔLogLoss']}\tverdict={p['cell_verdict']}"
        )
    print(f"wrote {out_json}")
    print(f"wrote {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
