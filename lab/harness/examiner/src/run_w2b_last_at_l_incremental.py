#!/usr/bin/env python3
"""TEST-20260913-007 — W2B-LAST-AT-L-INCREMENTAL vs m_L.

Poly last_L vs Kalshi m_L (λ=0.20, w=0.12, ε=1e-4 frozen) on
DRAFT-ABST-20260913-007 T-5m headlines only. Incumbent = m_L at Poly
obs_time L (NOT decision-time mid). Wave 005 pairable OC-twin set only
(254/240). last ≠ mid. No Map 2. No CF. No sibling. No CB-VEL. No W2-D.
No annex. invented_numbers=false. Trading FORBIDDEN.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.pm002_market_baseline import resolve_y  # noqa: E402
from src.pm003_market_baseline import (  # noqa: E402
    DataIntegrityError,
    assert_kalshi_only,
)
from src.w2b_last_at_l_incremental import (  # noqa: E402
    EPS,
    HEADLINE_BTC,
    HEADLINE_ETH,
    HEADLINES,
    LAMBDA_ROBUST,
    LAMBDA_SCORED,
    MIN_N_KILL,
    PLACEBO_SEED,
    TARGET_REM,
    W_ROBUST,
    W_SCORED,
    W2BRow,
    apply_map,
    gate_decision,
    package_verdict,
    placebo_flip_sign_b,
    placebo_lambda_zero,
    placebo_shuffle_last,
    primary_cell_id_t5m,
    score_forecast,
)

LAB = Path("/workspace/lab")
PM003_CKPT = LAB / "data/DATA-PROV-PM-003/derived/checkpoints.ndjson"
PM003_CANDLES = LAB / "data/DATA-PROV-PM-003/raw/kalshi_candles"
PM005_CKPT = LAB / "data/DATA-PROV-PM-005/derived/checkpoints.ndjson"
KALSHI_LABELS = LAB / "data/DATA-PROV-PM-001/normalized/kalshi_15m_btc_eth_resolved.ndjson"
JOIN_VERDICT = (
    LAB / "data/DATA-PROV-PM-005/provenance/DATA_VERDICT_W2B_INCUMBENT_AT_OBS.md"
)
JOIN_AUDIT_JSON = (
    LAB / "data/DATA-PROV-PM-005/provenance/CLOCK_AUDIT_W2B_INCUMBENT_AT_OBS.json"
)
OUT_DIR = LAB / "harness/examiner/out"
ARCHIVE_TESTS = LAB / "archive/tests"
ARCHIVE_AUDIT = LAB / "archive/audit"

EXPECTED_PM003_CHECKPOINTS_SHA256 = (
    "90e38c2f23e224def13db05924f6470a1e738778882f6b0cc17ed708b3143765"
)
EXPECTED_PAIRABLE = {"BTC": 254, "ETH": 240}

NEAR_DEG_LO = 0.02
NEAR_DEG_HI = 0.98

TEST_ID = "TEST-20260913-007"
PACKAGE = "W2B-LAST-AT-L-INCREMENTAL"
INCUMBENT = "m_L"  # Kalshi official 1m mid at Poly obs_time L
FEATURE_ID = "DRAFT-FEAT-20260913-007"
GATE_ID = "DRAFT-ABST-20260913-007"

AUTHORITY = [
    "governance/EXAMINER_ORDER_TEST-20260913-007-W2B.md",
    "governance/GOVERNOR_LIFT_EXAMINER_W2B_W006_2026-09-13.md",
    "archive/features/DRAFT-FEAT-20260913-007-W2B-incumbent-at-L.md",
    "archive/features/DRAFT-ABST-20260913-007-W2B-incumbent-at-L.md",
    "data/DATA-PROV-PM-005/provenance/DATA_VERDICT_W2B_INCUMBENT_AT_OBS.md",
    "governance/BINARY_EXAMINER_SPEC.md",
]

CANDLE_RULE_ID = "completed_bar_at_L_end_period_ts_le_L"


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _load_ndjson(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def _parse_ts(value: Any) -> datetime | None:
    if value is None:
        return None
    s = str(value).strip()
    if not s:
        return None
    s = s.replace(" ", "T")
    if s.endswith("+00"):
        s = s + ":00"
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(s)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _norm_ts(value: Any) -> str | None:
    dt = _parse_ts(value)
    if dt is None:
        return None
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def _unix_ts(value: Any) -> int | None:
    dt = _parse_ts(value)
    if dt is None:
        return None
    return int(dt.timestamp())


def _near_deg(ip: Any) -> bool:
    if ip is None:
        return True
    try:
        x = float(ip)
    except (TypeError, ValueError):
        return True
    return x <= NEAR_DEG_LO or x >= NEAR_DEG_HI


def _is_void(lab: dict[str, Any]) -> bool:
    st = str(lab.get("STATUS") or "").upper()
    res = str(lab.get("RESOLUTION") or "").upper()
    return st in ("VOID", "DISPUTED") or res in ("VOID", "DISPUTED")


def _parse_px(v: Any) -> float | None:
    if v is None:
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _mid_from_bid_ask(bid: float | None, ask: float | None) -> float | None:
    if bid is not None and ask is not None and bid > 0 and ask > 0 and bid <= ask:
        return round((bid + ask) / 2.0, 6)
    return None


def _oc_key(asset: str, open_time: Any, close_time: Any) -> tuple[str, str, str] | None:
    ot = _norm_ts(open_time)
    ct = _norm_ts(close_time)
    if ot is None or ct is None:
        return None
    return (asset, ot, ct)


def _index_labels(rows: list[dict[str, Any]]) -> tuple[dict[str, dict], dict[str, dict]]:
    by_cid: dict[str, dict] = {}
    by_vid: dict[str, dict] = {}
    for r in rows:
        by_cid[r["CONTRACT_ID"]] = r
        by_vid[r["VENUE_NATIVE_ID"]] = r
    return by_cid, by_vid


def _resolve_pm001(
    ckpt: dict, by_cid: dict[str, dict], by_vid: dict[str, dict]
) -> dict | None:
    m = by_cid.get(ckpt["contract_id"])
    if m is not None:
        return m
    return by_vid.get(ckpt.get("venue_native_id"))


def _load_poly_by_oc(rows: list[dict]) -> dict[tuple[str, str, str], list[dict]]:
    by_oc: dict[tuple[str, str, str], list[dict]] = {}
    for r in rows:
        if r.get("time_remaining_sec") != TARGET_REM:
            continue
        if r.get("implied_p_method") != "last":
            continue
        key = _oc_key(r["asset"], r.get("open_time"), r.get("close_time"))
        if key is None:
            continue
        by_oc.setdefault(key, []).append(r)
    return by_oc


def _pick_poly_L(
    twins: list[dict], decision_time: str
) -> tuple[dict | None, str | None, int]:
    t = _parse_ts(decision_time)
    if t is None:
        return None, "bad_decision_time", 0
    eligible: list[dict] = []
    n_la = 0
    for p in twins:
        ot = _parse_ts(p.get("obs_time"))
        if ot is None:
            continue
        if ot <= t:
            eligible.append(p)
        else:
            n_la += 1
    if not eligible:
        return None, "no_obs_time_le_t", n_la
    eligible.sort(
        key=lambda p: (
            _parse_ts(p["obs_time"]) or datetime.min.replace(tzinfo=timezone.utc),
            str(p.get("contract_id") or ""),
        )
    )
    best_obs = _parse_ts(eligible[-1]["obs_time"])
    same_obs = [p for p in eligible if _parse_ts(p["obs_time"]) == best_obs]
    same_obs.sort(key=lambda p: str(p.get("contract_id") or ""))
    return same_obs[0], None, n_la


_CANDLE_CACHE: dict[str, list[dict] | None] = {}


def _load_candles(ticker: str) -> list[dict] | None:
    if ticker in _CANDLE_CACHE:
        return _CANDLE_CACHE[ticker]
    path = PM003_CANDLES / f"{ticker}.json"
    if not path.exists():
        _CANDLE_CACHE[ticker] = None
        return None
    try:
        wrap = json.loads(path.read_text())
    except Exception:
        _CANDLE_CACHE[ticker] = None
        return None
    candles = (wrap.get("payload") or {}).get("candlesticks")
    if candles is None:
        _CANDLE_CACHE[ticker] = None
        return None
    _CANDLE_CACHE[ticker] = candles
    return candles


def m_L_from_candles(
    ticker: str, L: Any, open_time: Any, close_time: Any
) -> tuple[float | None, dict[str, Any]]:
    """Kalshi official 1m mid at L. Fail-closed. Never price.close/last as mid."""
    detail: dict[str, Any] = {
        "ticker": ticker,
        "candle_rule": CANDLE_RULE_ID,
        "L": _norm_ts(L),
        "L_unix": _unix_ts(L),
        "bar_end_period_ts": None,
        "yes_bid_close": None,
        "yes_ask_close": None,
        "m_L": None,
        "used_last_as_mid": False,
        "used_decision_time_bar": False,
        "miss_reason": None,
    }
    L_u = _unix_ts(L)
    open_u = _unix_ts(open_time)
    close_u = _unix_ts(close_time)
    if L_u is None:
        detail["miss_reason"] = "bad_L"
        return None, detail
    if open_u is None or close_u is None:
        detail["miss_reason"] = "bad_open_close"
        return None, detail
    candles = _load_candles(ticker)
    if candles is None:
        detail["miss_reason"] = "missing_candle_file"
        return None, detail
    if not candles:
        detail["miss_reason"] = "empty_candles"
        return None, detail

    completed: list[dict] = []
    for c in candles:
        end = c.get("end_period_ts")
        if end is None:
            continue
        end_i = int(end)
        if end_i <= open_u or end_i > close_u:
            continue
        if end_i <= L_u:
            completed.append(c)
    if not completed:
        detail["miss_reason"] = "no_completed_bar_at_L"
        return None, detail

    bar = max(completed, key=lambda c: int(c["end_period_ts"]))
    end_i = int(bar["end_period_ts"])
    detail["bar_end_period_ts"] = end_i
    bid = _parse_px((bar.get("yes_bid") or {}).get("close_dollars"))
    ask = _parse_px((bar.get("yes_ask") or {}).get("close_dollars"))
    detail["yes_bid_close"] = bid
    detail["yes_ask_close"] = ask
    mid = _mid_from_bid_ask(bid, ask)
    if mid is None:
        detail["miss_reason"] = "mid_rule_fail_bid_ask"
        detail["used_last_as_mid"] = False
        return None, detail
    detail["m_L"] = mid
    detail["miss_reason"] = None
    return mid, detail


def collect_pairable_rows(
    pm003_ckpts: list[dict],
    poly_by_oc: dict[tuple[str, str, str], list[dict]],
    by_cid: dict[str, dict],
    by_vid: dict[str, dict],
) -> tuple[dict[str, list[W2BRow]], dict[str, Any]]:
    cells: dict[str, list[W2BRow]] = {cid: [] for cid in HEADLINES}
    stats: dict[str, Any] = {
        "candidates": 0,
        "excluded_method_not_mid": 0,
        "excluded_near_deg": 0,
        "excluded_void_or_other": 0,
        "excluded_no_y": 0,
        "excluded_no_poly_twin": 0,
        "excluded_miss_L": 0,
        "excluded_miss_m_L": 0,
        "excluded_decision_time_bar_forbidden": 0,
        "n_lookahead_discarded": 0,
        "n_last_as_mid": 0,
        "n_used_decision_time_bar": 0,
        "n_m_L_equals_decision_mid": 0,
        "scored": 0,
        "n_speak": 0,
        "n_abstain": 0,
        "wave005_pairable": {"BTC": 0, "ETH": 0},
        "pairable_with_m_L": {"BTC": 0, "ETH": 0},
        "incumbent": "m_L",
        "decision_time_mid_used_as_incumbent": False,
        "join_verdict": "CONDITIONAL / INCUMBENT_AT_OBS_JOIN_CERTIFIED_WITH_CAVEATS",
        "candle_rule": CANDLE_RULE_ID,
        "per_cell": {
            cid: {
                "candidates": 0,
                "scored": 0,
                "speak": 0,
                "abstain": 0,
                "wave005_pairable": 0,
                "excluded_method_not_mid": 0,
                "excluded_near_deg": 0,
                "excluded_void": 0,
                "excluded_no_poly_twin": 0,
                "excluded_miss_L": 0,
                "excluded_miss_m_L": 0,
            }
            for cid in HEADLINES
        },
        "void_bucket": [],
        "CF_used": False,
        "sibling_used": False,
        "cbvel_used": False,
        "w2d_used": False,
        "map2_used": False,
        "poly_mid_invented": False,
        "last_as_mid": False,
        "decision_time_mid_as_incumbent": False,
        "004_retuned": False,
    }

    for r in pm003_ckpts:
        if r.get("venue") != "KALSHI" or r.get("window") != "15m":
            continue
        rem = r.get("time_remaining_sec")
        asset = r.get("asset")
        if rem != TARGET_REM or asset not in ("BTC", "ETH"):
            continue
        cell = primary_cell_id_t5m(asset)
        cs = stats["per_cell"][cell]
        stats["candidates"] += 1
        cs["candidates"] += 1

        if r.get("implied_p_method") != "mid":
            stats["excluded_method_not_mid"] += 1
            cs["excluded_method_not_mid"] += 1
            continue
        if r.get("implied_p") is None or _near_deg(r.get("implied_p")):
            stats["excluded_near_deg"] += 1
            cs["excluded_near_deg"] += 1
            continue

        lab = _resolve_pm001(r, by_cid, by_vid)
        if lab is None:
            stats["excluded_void_or_other"] += 1
            cs["excluded_void"] += 1
            continue
        if _is_void(lab):
            stats["excluded_void_or_other"] += 1
            cs["excluded_void"] += 1
            stats["void_bucket"].append(
                {
                    "contract_id": r.get("contract_id"),
                    "resolution": lab.get("RESOLUTION"),
                    "status": lab.get("STATUS"),
                }
            )
            continue
        y = resolve_y(lab.get("RESOLUTION"))
        if y is None:
            stats["excluded_no_y"] += 1
            cs["excluded_void"] += 1
            continue

        key = _oc_key(asset, lab.get("OPEN_TIME"), lab.get("CLOSE_TIME"))
        if key is None:
            stats["excluded_no_poly_twin"] += 1
            cs["excluded_no_poly_twin"] += 1
            continue
        twins = poly_by_oc.get(key)
        if not twins:
            stats["excluded_no_poly_twin"] += 1
            cs["excluded_no_poly_twin"] += 1
            continue

        t_iso = r["decision_time"]
        pick, miss_reason, n_la = _pick_poly_L(twins, t_iso)
        stats["n_lookahead_discarded"] += n_la
        if pick is None:
            stats["excluded_miss_L"] += 1
            cs["excluded_miss_L"] += 1
            continue
        if pick.get("implied_p_method") != "last":
            stats["excluded_miss_L"] += 1
            cs["excluded_miss_L"] += 1
            continue
        if pick.get("yes_bid") is not None or pick.get("yes_ask") is not None:
            stats["excluded_miss_L"] += 1
            cs["excluded_miss_L"] += 1
            stats["n_last_as_mid"] += 1
            continue
        last_raw = pick.get("implied_p", pick.get("last"))
        if last_raw is None:
            stats["excluded_miss_L"] += 1
            cs["excluded_miss_L"] += 1
            continue

        # Wave 005 pairable established
        stats["wave005_pairable"][asset] += 1
        cs["wave005_pairable"] += 1

        ticker = str(lab.get("VENUE_NATIVE_ID"))
        m_L, det = m_L_from_candles(
            ticker, pick["obs_time"], lab.get("OPEN_TIME"), lab.get("CLOSE_TIME")
        )
        if det.get("used_last_as_mid"):
            stats["n_last_as_mid"] += 1
            stats["last_as_mid"] = True
        if det.get("used_decision_time_bar"):
            stats["n_used_decision_time_bar"] += 1

        if m_L is None:
            stats["excluded_miss_m_L"] += 1
            cs["excluded_miss_m_L"] += 1
            continue

        bar_end = det.get("bar_end_period_ts")
        dec_u = _unix_ts(t_iso)
        L_u = _unix_ts(pick["obs_time"])
        if (
            bar_end is not None
            and dec_u is not None
            and L_u is not None
            and L_u < dec_u
            and bar_end == dec_u
        ):
            stats["excluded_decision_time_bar_forbidden"] += 1
            stats["n_used_decision_time_bar"] += 1
            stats["excluded_miss_m_L"] += 1
            cs["excluded_miss_m_L"] += 1
            continue

        stats["pairable_with_m_L"][asset] += 1

        m_dec = r.get("implied_p")
        if m_dec is not None and abs(float(m_dec) - float(m_L)) < 1e-12:
            stats["n_m_L_equals_decision_mid"] += 1

        t_dt = _parse_ts(t_iso)
        obs_dt = _parse_ts(pick["obs_time"])
        assert t_dt is not None and obs_dt is not None and L_u is not None
        lag = float((t_dt - obs_dt).total_seconds())
        last_L = float(last_raw)
        decision_ms = int(t_dt.timestamp() * 1000)

        last_ok = True
        m_L_ok = True
        mid_rule_ok = True
        gate = gate_decision(
            cell, last_ok=last_ok, m_L_ok=m_L_ok, mid_rule_ok=mid_rule_ok
        )
        speak = gate == "ALLOW_SPEAK_HEADLINE"

        if speak:
            stats["n_speak"] += 1
            cs["speak"] += 1
        else:
            stats["n_abstain"] += 1
            cs["abstain"] += 1

        cells[cell].append(
            W2BRow(
                cell_id=cell,
                contract_id=r["contract_id"],
                kalshi_ticker=ticker,
                poly_contract_id=str(pick.get("contract_id") or ""),
                asset=asset,
                checkpoint="T-5m",
                time_remaining_sec=int(rem),
                decision_time=t_iso,
                decision_time_ms=decision_ms,
                open_time=key[1],
                close_time=key[2],
                L_obs_time=str(pick.get("obs_time")),
                L_unix=int(L_u),
                last_L=last_L,
                m_L=float(m_L),
                m_L_bar_end_ts=int(bar_end) if bar_end is not None else None,
                m_L_yes_bid=det.get("yes_bid_close"),
                m_L_yes_ask=det.get("yes_ask_close"),
                m_decision_time=float(m_dec) if m_dec is not None else None,
                obs_lag_sec=lag,
                y=int(y),
                gate=gate,
                last_ok=last_ok,
                m_L_ok=m_L_ok,
                mid_rule_ok=mid_rule_ok,
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
    lines.append(
        f"# {payload['TEST_ID']} — {payload['package']} vs {payload['incumbent']}"
    )
    lines.append("")
    lines.append(f"**TEST_ID:** `{payload['TEST_ID']}`")
    lines.append(f"**Package:** `{payload['package']}`")
    lines.append(
        f"**Feature:** `{FEATURE_ID}` (Poly last_L vs Kalshi m_L, "
        f"λ={LAMBDA_SCORED} w={W_SCORED} ε={EPS} frozen)"
    )
    lines.append(
        f"**Gate:** `{GATE_ID}` (speak only when last_L and m_L exist at L)"
    )
    lines.append(
        f"**Incumbent:** `{payload['incumbent']}` "
        "(Kalshi official 1m mid at Poly obs_time L; NOT decision-time mid)"
    )
    lines.append(
        "**Purpose:** W2-B last vs mid-at-L incrementality on two T-5m headlines"
    )
    lines.append(
        "**DATA:** `DATA-PROV-PM-005` Poly last + `DATA-PROV-PM-003` Kalshi 1m candles "
        "for m_L + `DATA-PROV-PM-001` RESOLUTION"
    )
    lines.append(
        "**Join:** DATA_VERDICT_W2B_INCUMBENT_AT_OBS **CLEARED** (254/240; "
        "incumbent-timestamp certified; 45s lag vs decision_time is honesty, "
        "not this incumbent)"
    )
    lines.append("**Slice use:** USED_RESEARCH — not validation, not sealed holdout")
    lines.append(f"**Overall verdict:** `{payload['overall_verdict']}`")
    lines.append(f"**invented_numbers:** `{payload['invented_numbers']}`")
    lines.append("**Trading:** FORBIDDEN")
    lines.append(
        "**Stamp:** Join DATA_VERDICT_W2B_INCUMBENT_AT_OBS; incumbent = m_L at Poly "
        "obs_time; last ≠ mid; NOT decision-time mid; 004 not retuned; 45s lag honesty. "
        "No Map 2. No CF. No sibling. No CB-VEL. No W2-D rem shop. No invented Poly mid."
    )
    lines.append(
        "**Annex:** none (no other rem; robustness λ×w grid report-only — do not pick winner)"
    )
    lines.append(f"**Run UTC:** `{payload['run_utc']}`")
    lines.append(f"**SHA256 verified:** `{payload['data']['sha256_verified']}`")
    lines.append("")
    lines.append("## Authority")
    for a in payload["authority"]:
        lines.append(f"- `{a}`")
    lines.append("")
    lines.append("## Frozen map")
    lines.append(f"- ε = {EPS}; λ = {LAMBDA_SCORED}; w = {W_SCORED}")
    lines.append("- L = Poly last obs_time")
    lines.append("- last_L = Poly 15m last (method=last; NOT mid; no invent bid/ask)")
    lines.append(
        "- m_L = Kalshi official 1m mid at L: among candles same "
        "(asset, OPEN_TIME, CLOSE_TIME) with end_period_ts ≤ unix(L), "
        "take argmax end_period_ts; mid only if bid>0, ask>0, bid≤ask; "
        "implied_p=round((bid+ask)/2,6); method=mid; price.close/last NEVER as mid; "
        "no interpolation; NOT decision-time mid"
    )
    lines.append("- b = last_L − m_L")
    lines.append(
        "- if ABSTAIN or last_L/m_L missing or mid-rule fails: p = m_L"
    )
    lines.append(
        f"- else: p = clip(m_L + λ · clip(b, −w, +w), ε, 1−ε) "
        f"with λ={LAMBDA_SCORED}, w={W_SCORED}, ε={EPS}"
    )
    lines.append(
        f"- Robustness annex λ∈{list(LAMBDA_ROBUST)} w∈{list(W_ROBUST)} "
        "— do not pick winner. λ=0 ⇒ Δ=0 vs m_L."
    )
    lines.append(
        "- **CRITICAL:** Incumbent is m_L. Δ = model − m_L. "
        "Do NOT report Δ vs TEST-007 decision-time mid as this instrument "
        "(out of scope / UNTESTED)."
    )
    lines.append("")
    lines.append("## Filters / join")
    lines.append("- venue=KALSHI, window=15m; BTC/ETH **separate** (no pool)")
    lines.append(
        "- Wave 005 T-5m pairable OC-twin set only (rem=300 mid × Poly last OC twin) "
        "— **do NOT invent 604**"
    )
    lines.append("- Headlines only: T-5m (rem=300); **no annex**")
    lines.append(
        "- Kalshi decision-time mid used only for Wave 005 pairable hygiene "
        "(method=mid; near-deg exclude); **not** as scored incumbent"
    )
    lines.append("- VOID/DISPUTED out of scored N")
    lines.append(
        "- m_L via completed_bar_at_L_end_period_ts_le_L on PM-003 candles"
    )
    lines.append("- Missing last_L/m_L or mid-rule fail → fail-closed (row excluded or p=m_L)")
    lines.append(
        "- **NOT** decision-time mid as incumbent. **NOT** invented Poly mid. "
        "**NOT** last-as-mid. **NOT** Map 2. **NOT** CF. **NOT** sibling. "
        "**NOT** CB-VEL. **NOT** W2-D."
    )
    lines.append("")
    lines.append(
        "**Sign convention:** ΔBrier = Brier_model − Brier_m_L; "
        "ΔLogLoss = LogLoss_model − LogLoss_m_L; **negative = skill** vs m_L."
    )
    lines.append("")
    lines.append(
        "**Skill rule:** both Δ < 0 on a headline. Kill if either Δ ≥ 0, N < 80, "
        "or one headline works and the other inverts. Not NO_EDGE. Not Champion."
    )
    lines.append("")
    lines.append("## Overall reason")
    lines.append(payload["overall_reason"])
    lines.append("")
    lines.append("## Headlines (AMD-005, no pool, no annex)")
    lines.append("")
    lines.append(
        "| Cell | N | speak N | Brier_model | Brier_m_L | ΔBrier | "
        "LogLoss_model | LogLoss_m_L | ΔLogLoss | mean(m_L)_speak | "
        "mean(p)_speak | mean(last_L)_speak | speak_rate | ECE | Verdict |"
    )
    lines.append(
        "|------|--:|--------:|------------:|----------:|-------:|"
        "--------------:|------------:|---------:|---------------:|"
        "-------------:|------------------:|-----------:|-----|---------|"
    )
    for cid in HEADLINES:
        h = payload["headlines"][cid]
        lines.append(
            f"| `{cid}` | {h['N']} | {h['n_speak']} | "
            f"{_fmt_num(h['Brier_model'])} | {_fmt_num(h['Brier_market'])} | "
            f"{_fmt_num(h['ΔBrier'])} | {_fmt_num(h['LogLoss_model'])} | "
            f"{_fmt_num(h['LogLoss_market'])} | {_fmt_num(h['ΔLogLoss'])} | "
            f"{_fmt_num(h['mean(m)_speak'], 4)} | {_fmt_num(h['mean(p)_speak'], 4)} | "
            f"{_fmt_num(h['mean(last_L)_speak'], 4)} | {_fmt_num(h['speak_rate'], 4)} | "
            f"{_fmt_num(h['ECE'])} | `{h['cell_verdict']}` |"
        )
    lines.append("")

    for cid in HEADLINES:
        h = payload["headlines"][cid]
        lines.append(f"### `{cid}`")
        lines.append(
            f"- n_speak={h['n_speak']}; n_abstain={h['n_abstain']}; "
            f"fail_closed_missing={h['n_fail_closed_missing']}; "
            f"speak_rate={_fmt_num(h['speak_rate'], 4)}"
        )
        lines.append(
            f"- mean(m_L)_all={_fmt_num(h['mean(m)_all'], 4)}; "
            f"mean(p)_all={_fmt_num(h['mean(p)_all'], 4)}; "
            f"mean(last_L)_speak={_fmt_num(h['mean(last_L)_speak'], 4)}; "
            f"mean(b)_speak={_fmt_num(h['mean(b)_speak'], 4)}; "
            f"mean(obs_lag_sec)={_fmt_num(h['mean(obs_lag_sec)'], 2)}"
        )
        lines.append(f"- Reason: {h['cell_reason']}")
        cal = h.get("Calibration") or {}
        lines.append(f"- Calibration: {cal.get('note', 'UNTESTED')}")
        lines.append(f"- ECE_market (vs m_L): {_fmt_num(h.get('ECE_market'))}")
        lines.append(
            "- Δ vs decision-time mid: **UNTESTED / out of scope** (not this instrument)"
        )
        lines.append(
            "- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no trading)"
        )
        lines.append("")

    lines.append(
        "## Robustness annex (λ×w grids; not headline; do not pick winner)"
    )
    lines.append("")
    lines.append("| Cell | λ | w | N | ΔBrier | ΔLogLoss | Verdict |")
    lines.append("|------|--:|--:|--:|-------:|---------:|---------|")
    for cid in HEADLINES:
        rob = payload["robustness"][cid]
        for key, block in rob.items():
            lines.append(
                f"| `{cid}` | {block['λ']} | {block['w']} | {block['N']} | "
                f"{_fmt_num(block['ΔBrier'])} | {_fmt_num(block['ΔLogLoss'])} | "
                f"`{block['cell_verdict']}` |"
            )
    lines.append("")

    lines.append("## Placebos (report, not headline switch)")
    lines.append("")
    lines.append("| Placebo | Cell | N | ΔBrier | ΔLogLoss | Notes |")
    lines.append("|---------|------|--:|-------:|---------:|-------|")
    for pname in ("lambda_0", "shuffle_last_L", "flip_sign_b"):
        for cid in HEADLINES:
            b = payload["placebos"][pname][cid]
            lines.append(
                f"| `{pname}` | `{cid}` | {b['N']} | "
                f"{_fmt_num(b['ΔBrier'])} | {_fmt_num(b['ΔLogLoss'])} | "
                f"{b.get('placebo_note', '')} |"
            )
    lines.append("")
    lines.append(f"- placebo_seed: `{PLACEBO_SEED}`")
    lines.append("- λ=0 must give ΔBrier=0 and ΔLogLoss=0 (identity vs m_L).")
    lines.append(
        "- Swap incumbent to decision-time mid is **not** this card "
        "(held 004 / out of scope) — not scored as a placebo switch."
    )
    lines.append("")

    lines.append("## Filter / join stats")
    lines.append("```json")
    filt = {
        k: v
        for k, v in payload["filter_stats"].items()
        if k != "void_bucket"
    }
    lines.append(json.dumps(filt, indent=2, default=str))
    lines.append("```")
    lines.append("")
    lines.append("## Confirmations")
    for k, v in payload["confirmations"].items():
        lines.append(f"- `{k}`: `{v}`")
    lines.append("")
    lines.append("## Forbidden actions (not performed)")
    for f in payload["forbidden_actions"]:
        lines.append(f"- {f}")
    lines.append("")
    lines.append("## Artifact paths")
    for k, v in payload["artifact_paths"].items():
        lines.append(f"- `{k}`: `{v}`")
    lines.append("")
    lines.append("---")
    lines.append(
        f"**Sealed by Examiner** {payload['run_utc']}. "
        f"Verdict `{payload['overall_verdict']}`. "
        "Trade FORBIDDEN. USED_RESEARCH. Holdout closed. "
        "Incumbent = m_L. Δ vs decision-time mid = UNTESTED / out of scope."
    )
    lines.append("")
    return "\n".join(lines)


def _write_integrity_fail(msg: str) -> int:
    run_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out_stem = f"{TEST_ID}-{PACKAGE}"
    payload = {
        "TEST_ID": TEST_ID,
        "package": PACKAGE,
        "overall_verdict": "DATA_INTEGRITY_FAIL",
        "overall_reason": msg,
        "invented_numbers": False,
        "run_utc": run_utc,
        "error": msg,
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / f"{out_stem}.json").write_text(json.dumps(payload, indent=2) + "\n")
    (OUT_DIR / f"{out_stem}.md").write_text(
        f"# {TEST_ID} DATA_INTEGRITY_FAIL\n\n{msg}\n"
    )
    print(f"DATA_INTEGRITY_FAIL: {msg}")
    return 2


def main() -> int:
    if not JOIN_VERDICT.exists():
        return _write_integrity_fail(f"missing join verdict: {JOIN_VERDICT}")
    if not JOIN_AUDIT_JSON.exists():
        return _write_integrity_fail(f"missing join audit json: {JOIN_AUDIT_JSON}")

    digest = _sha256_file(PM003_CKPT)
    if digest != EXPECTED_PM003_CHECKPOINTS_SHA256:
        return _write_integrity_fail(
            f"PM-003 checkpoints sha256 mismatch: {digest} "
            f"expected {EXPECTED_PM003_CHECKPOINTS_SHA256}"
        )

    pm003_ckpts = _load_ndjson(PM003_CKPT)
    try:
        venue_check = assert_kalshi_only(pm003_ckpts)
    except DataIntegrityError as e:
        return _write_integrity_fail(str(e))

    pm005_ckpts = _load_ndjson(PM005_CKPT)
    labels = _load_ndjson(KALSHI_LABELS)
    by_cid, by_vid = _index_labels(labels)
    poly_by_oc = _load_poly_by_oc(pm005_ckpts)

    cells, filt = collect_pairable_rows(pm003_ckpts, poly_by_oc, by_cid, by_vid)

    # Coverage honesty vs Clock CLEARED 254/240
    for asset, expected in EXPECTED_PAIRABLE.items():
        got = filt["pairable_with_m_L"][asset]
        if got != expected:
            return _write_integrity_fail(
                f"pairable_with_m_L[{asset}]={got} ≠ Clock expected {expected}"
            )
    if filt["n_last_as_mid"] > 0 or filt["last_as_mid"]:
        return _write_integrity_fail("last-as-mid > 0 (forbidden)")
    if filt["n_used_decision_time_bar"] > 0:
        return _write_integrity_fail("decision_time bar used as m_L (forbidden)")
    if (
        filt["CF_used"]
        or filt["sibling_used"]
        or filt["cbvel_used"]
        or filt["w2d_used"]
        or filt["map2_used"]
        or filt["poly_mid_invented"]
        or filt["decision_time_mid_as_incumbent"]
        or filt["004_retuned"]
    ):
        return _write_integrity_fail("forbidden instrument path used")

    map_label = (
        f"W2B-LAST-AT-L: b=last_L-m_L; "
        f"p=clip(m_L+{LAMBDA_SCORED}*clip(b,-{W_SCORED},+{W_SCORED}),{EPS},1-{EPS}) "
        f"on ALLOW_SPEAK; else p=m_L; incumbent=m_L; last≠mid; NOT decision-time mid"
    )

    headlines: dict[str, Any] = {}
    for cid in HEADLINES:
        rows = sorted(
            cells[cid],
            key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec),
        )
        cells[cid] = rows
        if len(rows) < MIN_N_KILL:
            # still score; package_verdict / cell verdict will FAIL-INSUFFICIENT
            pass
        ps = apply_map(rows, lam=LAMBDA_SCORED, w=W_SCORED)
        headlines[cid] = score_forecast(
            rows, ps, feature_id=FEATURE_ID, map_label=map_label
        )

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

    placebos: dict[str, dict[str, Any]] = {
        "lambda_0": {},
        "shuffle_last_L": {},
        "flip_sign_b": {},
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

        ps = placebo_shuffle_last(rows, cid)
        ordered_s = sorted(
            rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec)
        )
        bs = score_forecast(
            ordered_s, ps, feature_id=FEATURE_ID, map_label="placebo shuffle last_L"
        )
        bs.pop("contract_ids_scored", None)
        bs["placebo_note"] = "last_L shuffled within cell; m_L fixed"
        placebos["shuffle_last_L"][cid] = bs

        pf = placebo_flip_sign_b(ordered)
        bf = score_forecast(
            ordered, pf, feature_id=FEATURE_ID, map_label="placebo flip sign(b)"
        )
        bf.pop("contract_ids_scored", None)
        bf["placebo_note"] = "sign of b=last_L−m_L flipped"
        placebos["flip_sign_b"][cid] = bf

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
        "purpose": "w2b_last_L_vs_m_L_at_obs_incrementality",
        "strategy": None,
        "trading": "FORBIDDEN",
        "invented_numbers": False,
        "join_verdict": "CONDITIONAL / INCUMBENT_AT_OBS_JOIN_CERTIFIED_WITH_CAVEATS",
        "overall_verdict": overall,
        "overall_reason": reason,
        "run_utc": run_utc,
        "authority": AUTHORITY,
        "frozen_map": {
            "λ": LAMBDA_SCORED,
            "w": W_SCORED,
            "ε": EPS,
            "formula": map_label,
            "L": "Poly last obs_time",
            "last_L": "Poly 15m last (method=last)",
            "m_L": "Kalshi 1m mid at L (completed_bar_at_L_end_period_ts_le_L)",
            "b": "last_L - m_L",
            "incumbent": "m_L",
            "not_decision_time_mid": True,
            "last_neq_mid": True,
            "no_phi_z": True,
            "no_sibling_blend": True,
            "no_map2": True,
            "no_annex": True,
            "no_CF": True,
            "no_CBVEL": True,
            "no_W2D": True,
            "no_004_retune": True,
            "no_invented_poly_mid": True,
        },
        "stamps": {
            "join": "DATA_VERDICT_W2B_INCUMBENT_AT_OBS",
            "incumbent": "m_L at Poly obs_time",
            "last_neq_mid": True,
            "not_decision_time_mid": True,
            "004_not_retuned": True,
            "lag_45s_honesty": True,
            "coverage_pairable": EXPECTED_PAIRABLE,
            "no_Map2": True,
            "no_CF": True,
            "no_sibling": True,
            "no_CBVEL": True,
            "no_W2D": True,
        },
        "data": {
            "dataset_ids": [
                "DATA-PROV-PM-005",
                "DATA-PROV-PM-003",
                "DATA-PROV-PM-001",
            ],
            "slice_use": "USED_RESEARCH",
            "pm003_checkpoints": str(PM003_CKPT),
            "pm003_checkpoints_sha256": digest,
            "pm003_checkpoints_sha256_expected": EXPECTED_PM003_CHECKPOINTS_SHA256,
            "sha256_verified": digest == EXPECTED_PM003_CHECKPOINTS_SHA256,
            "pm003_candles": str(PM003_CANDLES),
            "pm005_checkpoints": str(PM005_CKPT),
            "labels_kalshi": str(KALSHI_LABELS),
            "join_verdict_path": str(JOIN_VERDICT),
            "join_audit_json": str(JOIN_AUDIT_JSON),
            "m_L_source": (
                "PM-003 raw kalshi_candles completed_bar_at_L_end_period_ts_le_L; "
                "mid=(yes_bid.close+yes_ask.close)/2"
            ),
            "last_L_source": "PM-005 Poly 15m last (method=last; bid/ask null)",
            "y_source": "PM-001 RESOLUTION",
            "forbidden": [
                "decision-time mid as incumbent",
                "invented Poly mid",
                "last-as-mid",
                "Map 2",
                "CF",
                "sibling blend",
                "CB-VEL",
                "W2-D rem shop",
                "retune λ/w",
                "trading",
                "invented numbers / invent 604",
                "004 retune",
            ],
            "pm002_checkpoints_read": False,
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
            "ΔBrier": "Brier_model − Brier_m_L; negative = skill vs m_L",
            "ΔLogLoss": "LogLoss_model − LogLoss_m_L; negative = skill vs m_L",
            "falsification_primary": (
                "ΔBrier≥0 OR ΔLogLoss≥0 on a headline → "
                "REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE); "
                "one-asset invert kills; N<80 kills"
            ),
            "decision_time_mid_delta": "UNTESTED / out of scope (not this instrument)",
        },
        "confirmations": {
            "invented_numbers": False,
            "trading": False,
            "decision_time_mid_as_incumbent": False,
            "poly_mid_invented": False,
            "last_as_mid": False,
            "map2_used": False,
            "CF_used": False,
            "sibling_used": False,
            "cbvel_used": False,
            "w2d_used": False,
            "004_retuned": False,
            "join_stamped": "DATA_VERDICT_W2B_INCUMBENT_AT_OBS",
            "coverage_BTC": filt["pairable_with_m_L"]["BTC"],
            "coverage_ETH": filt["pairable_with_m_L"]["ETH"],
            "lambda0_BTC_pass": placebos["lambda_0"][HEADLINE_BTC].get(
                "lambda0_delta_zero"
            ),
            "lambda0_ETH_pass": placebos["lambda_0"][HEADLINE_ETH].get(
                "lambda0_delta_zero"
            ),
        },
        "forbidden_actions": [
            "in-sample refit",
            "retune λ/w",
            "retune gate / annex sneak",
            "decision-time mid as incumbent",
            "invented Poly mid / last-as-mid",
            "Map 2",
            "CF",
            "sibling blend",
            "CB-VEL",
            "W2-D rem shop",
            "004 retune",
            "PM-002 union",
            "invent 604 coverage",
            "trading",
        ],
        "artifact_paths": {},
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_TESTS.mkdir(parents=True, exist_ok=True)
    ARCHIVE_AUDIT.mkdir(parents=True, exist_ok=True)

    md = build_markdown(payload)
    payload["artifact_paths"] = {
        "out_json": str(out_json),
        "out_md": str(out_md),
        "archive_json": str(ARCHIVE_TESTS / f"{out_stem}.json"),
        "archive_md": str(ARCHIVE_TESTS / f"{out_stem}.md"),
        "archive_audit": str(
            ARCHIVE_AUDIT / f"2026-09-13-Examiner-{out_stem}.md"
        ),
    }
    # rebuild md with paths filled
    md = build_markdown(payload)

    out_json.write_text(json.dumps(payload, indent=2, default=str) + "\n")
    out_md.write_text(md)
    (ARCHIVE_TESTS / f"{out_stem}.json").write_text(out_json.read_text())
    (ARCHIVE_TESTS / f"{out_stem}.md").write_text(md)
    (ARCHIVE_AUDIT / f"2026-09-13-Examiner-{out_stem}.md").write_text(
        f"# Examiner pointer — {out_stem}\n\n"
        f"- out: `{out_md}`\n"
        f"- json: `{out_json}`\n"
        f"- verdict: `{overall}`\n"
        f"- run_utc: `{run_utc}`\n"
        f"- incumbent: m_L (NOT decision-time mid)\n"
        f"- coverage: BTC={filt['pairable_with_m_L']['BTC']} "
        f"ETH={filt['pairable_with_m_L']['ETH']}\n"
        f"- trade: FORBIDDEN\n"
    )

    print(f"TEST_ID={TEST_ID} PACKAGE={PACKAGE}")
    print(f"overall_verdict={overall}")
    for cid in HEADLINES:
        h = headlines[cid]
        print(
            f"  {cid}: N={h['N']} speak={h['n_speak']} "
            f"ΔBrier={h['ΔBrier']:.6f} ΔLogLoss={h['ΔLogLoss']:.6f} "
            f"verdict={h['cell_verdict']}"
        )
    print(f"wrote {out_json}")
    print(f"wrote {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
