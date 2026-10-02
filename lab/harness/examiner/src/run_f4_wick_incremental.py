#!/usr/bin/env python3
"""TEST-20260914-001 — F4-WICK-INCREMENTAL vs MKT-KALSHI-15M-MID.

Wick-gated structural Φ(z) blend (θ=1.5 W=5 λ=0.35 frozen) on
DRAFT-FEAT-20260914-008 × DRAFT-ABST-20260914-008 T-5m headlines only.
Sep-12 PM-004 mid × L3-002 lock B + L3-001 Sep-11 edges (855/855).
No PM-003. No θ/W search. L3 ≠ oracle. invented_numbers=false. Trading FORBIDDEN.
"""

from __future__ import annotations

import csv
import hashlib
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

from src.f1_incremental import p_struct_digital, tau_years  # noqa: E402
from src.f4_wick_incremental import (  # noqa: E402
    ANN_FACTOR,
    EPS,
    F4Row,
    HEADLINE_BTC,
    HEADLINE_ETH,
    HEADLINES,
    LAMBDA_ROBUST,
    LAMBDA_SCORED,
    MIN_N_WICK_KILL,
    PLACEBO_SEED,
    THETA,
    W_SIGMA,
    W_WICK,
    apply_map,
    gate_decision,
    is_wick,
    package_verdict,
    placebo_lambda_zero,
    placebo_reverse_gate,
    placebo_shuffle_wick,
    placebo_sign_flip_ps,
    score_forecast,
)
from src.pm002_market_baseline import (  # noqa: E402
    KALSHI_REM_TO_LABEL,
    accept_mid_row,
    m_t_from_checkpoint,
    primary_cell_id,
    resolve_y,
)

LAB = Path("/workspace/lab")
CHECKPOINTS = LAB / "data/DATA-PROV-PM-004/derived/checkpoints.ndjson"
COVERAGE = LAB / "data/DATA-PROV-PM-004/derived/contract_coverage.ndjson"
MARKETS_DIR = LAB / "data/DATA-PROV-PM-004/raw/kalshi_markets"
RESOLVED = LAB / "data/DATA-PROV-PM-004/provenance/resolved_universe.ndjson"
L3_002_BTC = LAB / "data/DATA-PROV-L3-002/derived/BTCUSDT-1m-2026-09-12.csv"
L3_002_ETH = LAB / "data/DATA-PROV-L3-002/derived/ETHUSDT-1m-2026-09-12.csv"
L3_001_BTC = LAB / "data/DATA-PROV-L3-001/derived/BTCUSDT_1m_spot_2026-09-04_2026-09-11.parquet"
L3_001_ETH = LAB / "data/DATA-PROV-L3-001/derived/ETHUSDT_1m_spot_2026-09-04_2026-09-11.parquet"
OUT_DIR = LAB / "harness/examiner/out"
ARCHIVE_TESTS = LAB / "archive/tests"
ARCHIVE_AUDIT = LAB / "archive/audit"

TEST_ID = "TEST-20260914-001"
PACKAGE = "F4-WICK-INCREMENTAL"
INCUMBENT = "MKT-KALSHI-15M-MID"
FEATURE_ID = "DRAFT-FEAT-20260914-008"
GATE_ID = "DRAFT-ABST-20260914-008"
TARGET_REM = 300  # T-5m only
TAPE_DAY = "2026-09-12"

AUTHORITY = [
    "governance/EXAMINER_ORDER_TEST-20260914-001-F4.md",
    "governance/GOVERNOR_SIGN_F4_WICK_2026-09-14.md",
    "archive/features/DRAFT-FEAT-20260914-008-F4-wick.md",
    "archive/features/DRAFT-ABST-20260914-008-F4-wick.md",
    "archive/features/DRAFT-FEAT-20260912-006.md",
    "data/DATA-PROV-PM-004/provenance/DATA_VERDICT_PM004_L3002_JOIN.md",
    "data/DATA-PROV-PM-004/provenance/DATA_VERDICT_PM004_L3_SEP11_EDGE.md",
    "governance/BINARY_EXAMINER_SPEC.md",
]

# Named Sep-12 day-start edge contracts (Clock CLEARED via L3-001 under lock B).
# T-5m universe does not include rem=0/840 edges; still name for stamp honesty.
NAMED_EDGE_KEYS = {
    ("BTC", "2026-09-12T00:00:00Z"),
    ("ETH", "2026-09-12T00:00:00Z"),
    ("BTC", "2026-09-12T00:01:00Z"),
    ("ETH", "2026-09-12T00:01:00Z"),
}


def _sha256(path: Path) -> str:
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


def _parse_decision_ms(decision_time: str) -> int:
    dt = datetime.fromisoformat(decision_time.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)


def load_market_labels() -> dict[str, dict[str, Any]]:
    """FLOOR_STRIKE + RESULT from PM-004 settled markets (Sep-12 not in PM-001)."""
    out: dict[str, dict[str, Any]] = {}
    for p in sorted(MARKETS_DIR.glob("*settled*.json")):
        d = json.load(p.open())
        markets = d.get("payload", {}).get("markets") or d.get("markets") or []
        for m in markets:
            t = m.get("ticker")
            if not t:
                continue
            out[t] = {
                "VENUE_NATIVE_ID": t,
                "FLOOR_STRIKE": m.get("floor_strike"),
                "RESULT": m.get("result"),
                "STATUS": m.get("status"),
                "OPEN_TIME": m.get("open_time"),
                "CLOSE_TIME": m.get("close_time"),
                "RESOLUTION": (
                    str(m.get("result") or "").upper()
                    if m.get("result") in ("yes", "no", "YES", "NO")
                    else None
                ),
            }
            if out[t]["RESOLUTION"] == "YES" or out[t]["RESOLUTION"] == "NO":
                pass
            elif m.get("result") in ("yes", "YES"):
                out[t]["RESOLUTION"] = "YES"
            elif m.get("result") in ("no", "NO"):
                out[t]["RESOLUTION"] = "NO"
    # Overlay resolved_universe CLASS/RESULT if present
    if RESOLVED.exists():
        for r in _load_ndjson(RESOLVED):
            nid = r.get("VENUE_NATIVE_ID")
            if not nid:
                continue
            base = out.setdefault(nid, {"VENUE_NATIVE_ID": nid})
            if r.get("RESULT"):
                res = str(r["RESULT"]).upper()
                if res in ("YES", "NO"):
                    base["RESOLUTION"] = res
            if r.get("OPEN_TIME"):
                base["OPEN_TIME"] = r["OPEN_TIME"]
            if r.get("CLOSE_TIME"):
                base["CLOSE_TIME"] = r["CLOSE_TIME"]
            if r.get("CONTRACT_ID"):
                base["CONTRACT_ID"] = r["CONTRACT_ID"]
    return out


class L3Book:
    """Merged L3-001 (Sep-11 lookback/edges) + L3-002 (Sep-12) under lock B.

    bar_end_ms = open_time_ms + 60000 (== close_time_ms + 1 for Vision).
    Lock B: last bar with bar_end_ms < decision_time_ms.
    """

    def __init__(self, asset: str):
        self.asset = asset
        rows: list[dict[str, Any]] = []
        pq_path = L3_001_BTC if asset == "BTC" else L3_001_ETH
        csv_path = L3_002_BTC if asset == "BTC" else L3_002_ETH

        table = pq.read_table(pq_path, columns=["open_time_ms", "close_time_ms", "close"])
        open_ms = np.asarray(table.column("open_time_ms").to_numpy(), dtype=np.int64)
        close_ms = np.asarray(table.column("close_time_ms").to_numpy(), dtype=np.int64)
        closes = np.asarray(table.column("close").to_numpy(), dtype=np.float64)
        for i in range(len(open_ms)):
            ot = int(open_ms[i])
            ct = int(close_ms[i])
            be = ot + 60_000
            # Honesty: Vision/L3-001 close …59999 ⇒ bar_end = close+1
            if be != ct + 1 and abs(be - (ct + 1)) > 1:
                # tolerate exact equality variants
                be = ct + 1 if ct % 1000 == 999 else ot + 60_000
            rows.append(
                {
                    "open_time_ms": ot,
                    "close_time_ms": ct,
                    "bar_end_ms": be,
                    "close": float(closes[i]),
                    "source": "L3-001",
                }
            )

        with csv_path.open() as f:
            for r in csv.DictReader(f):
                ot = int(r["open_time_ms"])
                ct = int(r["close_time_ms"])
                be = ot + 60_000
                rows.append(
                    {
                        "open_time_ms": ot,
                        "close_time_ms": ct,
                        "bar_end_ms": be,
                        "close": float(r["close"]),
                        "source": "L3-002",
                    }
                )

        # Deduplicate by open_time_ms preferring L3-002 on overlap
        by_ot: dict[int, dict[str, Any]] = {}
        for r in rows:
            ot = r["open_time_ms"]
            if ot in by_ot and by_ot[ot]["source"] == "L3-002":
                continue
            if ot in by_ot and r["source"] == "L3-001":
                continue
            by_ot[ot] = r
        ordered = [by_ot[k] for k in sorted(by_ot)]
        self.open_ms = np.asarray([r["open_time_ms"] for r in ordered], dtype=np.int64)
        self.close_ms = np.asarray([r["close_time_ms"] for r in ordered], dtype=np.int64)
        self.bar_end_ms = np.asarray([r["bar_end_ms"] for r in ordered], dtype=np.int64)
        self.closes = np.asarray([r["close"] for r in ordered], dtype=np.float64)
        self.source = [r["source"] for r in ordered]

        with np.errstate(divide="ignore", invalid="ignore"):
            self.log_ret = np.empty(len(self.closes), dtype=np.float64)
            self.log_ret[0] = np.nan
            self.log_ret[1:] = np.log(self.closes[1:] / self.closes[:-1])

        self.sigma_at = np.full(len(self.closes), np.nan, dtype=np.float64)
        if len(self.closes) > W_SIGMA:
            sq = self.log_ret ** 2
            finite = np.isfinite(sq).astype(np.float64)
            sq0 = np.where(np.isfinite(sq), sq, 0.0)
            csum_sq = np.cumsum(sq0)
            csum_n = np.cumsum(finite)
            for i in range(W_SIGMA, len(self.closes)):
                lo = i - W_SIGMA + 1
                n = csum_n[i] - (csum_n[lo - 1] if lo > 0 else 0.0)
                if n < W_SIGMA:
                    continue
                ssq = csum_sq[i] - (csum_sq[lo - 1] if lo > 0 else 0.0)
                rms = math.sqrt(ssq / W_SIGMA)
                if rms > 0 and math.isfinite(rms):
                    self.sigma_at[i] = rms * ANN_FACTOR

    def lock_b_idx(self, decision_time_ms: int) -> Optional[int]:
        """Last bar with bar_end_ms < decision_time_ms."""
        j = int(np.searchsorted(self.bar_end_ms, decision_time_ms, side="left") - 1)
        if j < 0:
            return None
        if not (int(self.bar_end_ms[j]) < decision_time_ms):
            return None
        return j

    def lookback(self, decision_time_ms: int) -> Optional[dict[str, Any]]:
        j = self.lock_b_idx(decision_time_ms)
        if j is None:
            return None
        if j < W_WICK:
            return None  # incomplete W=5 chain
        if not math.isfinite(self.sigma_at[j]) or self.sigma_at[j] <= 0:
            return None  # incomplete Wσ
        s_t = float(self.closes[j])
        s_tW = float(self.closes[j - W_WICK])
        if s_t <= 0 or s_tW <= 0 or not math.isfinite(s_t) or not math.isfinite(s_tW):
            return None
        # Contiguity check: W completed steps back must be spaced 1m
        expected_ot = int(self.open_ms[j]) - W_WICK * 60_000
        if int(self.open_ms[j - W_WICK]) != expected_ot:
            return None
        return {
            "idx": j,
            "s_t": s_t,
            "s_tW": s_tW,
            "sigma_hat": float(self.sigma_at[j]),
            "bar_end_ms": int(self.bar_end_ms[j]),
            "bar_open_ms": int(self.open_ms[j]),
            "source": self.source[j],
            "lag_ms": int(decision_time_ms - int(self.bar_end_ms[j])),
        }


def build_rows(
    checkpoints: list[dict],
    coverage: dict[str, dict],
    labels: dict[str, dict],
    books: dict[str, L3Book],
) -> tuple[dict[str, list[F4Row]], dict[str, Any]]:
    cells: dict[str, list[F4Row]] = {c: [] for c in HEADLINES}
    stats: dict[str, Any] = {
        "candidates": 0,
        "excluded_not_sep12": 0,
        "excluded_not_t5m": 0,
        "excluded_method_not_mid": 0,
        "excluded_near_deg": 0,
        "excluded_void_or_other": 0,
        "excluded_no_y": 0,
        "excluded_no_label": 0,
        "excluded_no_k": 0,
        "excluded_wrong_venue": 0,
        "scored": 0,
        "n_speak": 0,
        "n_abstain": 0,
        "n_off_wick": 0,
        "n_allow": 0,
        "n_l3_001_source": 0,
        "n_l3_002_source": 0,
        "lookahead": 0,
        "policy": "B",
        "join_verdict": "CONDITIONAL+EDGE_CLEARED",
        "coverage_named": "855/855",
        "per_cell": {
            c: {
                "candidates": 0,
                "scored": 0,
                "speak": 0,
                "abstain": 0,
                "off_wick": 0,
                "excluded_method_not_mid": 0,
                "excluded_near_deg": 0,
                "excluded_void": 0,
                "excluded_no_y": 0,
            }
            for c in HEADLINES
        },
        "pm003_used": False,
        "theta_w_search": False,
        "policy_A_used": False,
    }

    for r in checkpoints:
        if r.get("venue") != "KALSHI" or r.get("window") != "15m":
            stats["excluded_wrong_venue"] += 1
            continue
        asset = r.get("asset")
        rem = r.get("time_remaining_sec")
        dt = r.get("decision_time") or ""
        if not dt.startswith(TAPE_DAY):
            stats["excluded_not_sep12"] += 1
            continue
        if rem != TARGET_REM:
            stats["excluded_not_t5m"] += 1
            continue
        if asset not in ("BTC", "ETH"):
            continue

        cell_id = primary_cell_id(asset, int(rem))
        if cell_id not in HEADLINES:
            continue
        cs = stats["per_cell"][cell_id]
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

        nid = r.get("venue_native_id") or ""
        lab = labels.get(nid)
        if lab is None:
            stats["excluded_no_label"] += 1
            continue
        res = lab.get("RESOLUTION")
        st = str(lab.get("STATUS") or "").upper()
        if st in ("VOID", "DISPUTED") or (res and str(res).upper() in ("VOID", "DISPUTED")):
            stats["excluded_void_or_other"] += 1
            cs["excluded_void"] += 1
            continue
        y = resolve_y(res)
        if y is None:
            stats["excluded_no_y"] += 1
            cs["excluded_no_y"] += 1
            continue

        k_raw = lab.get("FLOOR_STRIKE")
        try:
            k = float(k_raw) if k_raw is not None else None
        except (TypeError, ValueError):
            k = None
        if k is None or not math.isfinite(k) or k <= 0:
            stats["excluded_no_k"] += 1
            continue

        cov = coverage.get(r["contract_id"], {})
        open_time = lab.get("OPEN_TIME") or cov.get("open_time") or ""
        close_time = lab.get("CLOSE_TIME") or cov.get("close_time") or ""
        # K knowable after OPEN
        if open_time and dt < open_time:
            stats["excluded_no_k"] += 1
            continue

        m_t = m_t_from_checkpoint(r)
        decision_ms = _parse_decision_ms(dt)
        book = books[asset]
        lb = book.lookback(decision_ms)

        lookback_ok = False
        s_t = s_tW = sigma_hat = z = p_s = None
        wick = False
        bar_end_ms = bar_open_ms = None
        l3_source = "missing"
        if lb is not None:
            if lb["bar_end_ms"] >= decision_ms:
                stats["lookahead"] += 1
                raise RuntimeError(
                    f"lookahead lock B violation: bar_end={lb['bar_end_ms']} t={decision_ms}"
                )
            s_t = lb["s_t"]
            s_tW = lb["s_tW"]
            sigma_hat = lb["sigma_hat"]
            bar_end_ms = lb["bar_end_ms"]
            bar_open_ms = lb["bar_open_ms"]
            l3_source = lb["source"]
            tau = tau_years(int(rem))
            p_s = p_struct_digital(s_t, k, sigma_hat, tau)
            if p_s is not None:
                z = math.log(s_t / k) / (sigma_hat * math.sqrt(tau))
                wick = is_wick(s_t, s_tW, sigma_hat)
                lookback_ok = True

        mid_ok = True
        gate = gate_decision(cell_id, mid_ok=mid_ok, lookback_ok=lookback_ok)
        speak = gate == "ALLOW_SPEAK_HEADLINE" and lookback_ok and wick

        row = F4Row(
            cell_id=cell_id,
            contract_id=r["contract_id"],
            asset=asset,
            checkpoint=KALSHI_REM_TO_LABEL[int(rem)],
            time_remaining_sec=int(rem),
            decision_time=dt,
            decision_time_ms=decision_ms,
            open_time=open_time,
            close_time=close_time,
            m_t=float(m_t),
            y=int(y),
            k=k,
            s_t=s_t,
            s_tW=s_tW,
            sigma_hat=sigma_hat,
            z=z,
            p_s=p_s,
            wick=wick,
            lookback_ok=lookback_ok,
            gate=gate,
            bar_end_ms=bar_end_ms,
            bar_open_ms=bar_open_ms,
            l3_source=l3_source,
            speak=speak,
        )
        cells[cell_id].append(row)
        stats["scored"] += 1
        cs["scored"] += 1
        if speak:
            stats["n_speak"] += 1
            cs["speak"] += 1
        if gate == "ABSTAIN":
            stats["n_abstain"] += 1
            cs["abstain"] += 1
        elif lookback_ok and not wick:
            stats["n_off_wick"] += 1
            cs["off_wick"] += 1
        if gate == "ALLOW_SPEAK_HEADLINE":
            stats["n_allow"] += 1
        if l3_source == "L3-001":
            stats["n_l3_001_source"] += 1
        elif l3_source == "L3-002":
            stats["n_l3_002_source"] += 1

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
        f"**Feature:** `{FEATURE_ID}` (wick-gated structural Φ(z) blend, "
        f"θ={THETA} W={W_WICK} λ={LAMBDA_SCORED} frozen)"
    )
    lines.append(
        f"**Gate:** `{GATE_ID}` (speak-eligible only on BTC/ETH T-5m mid with W=5 lock-B lookback)"
    )
    lines.append(f"**Incumbent:** `{payload['incumbent']}` (same-t PM-004 mid)")
    lines.append(
        "**Purpose:** F4 wick-gate incrementality of structural Φ(z) blend vs Kalshi mid "
        "on two AMD-005 headlines (full cell; off-wick Δ=0 by construction)"
    )
    lines.append(
        "**DATA:** `DATA-PROV-PM-004` + `DATA-PROV-L3-002` lock B + `DATA-PROV-L3-001` "
        "Sep-11 edges/lookback + PM-004 settled FLOOR_STRIKE/RESULT (Sep-12; PM-001 ends Sep-11)"
    )
    lines.append(
        "**Join:** DATA_VERDICT_PM004_L3002_JOIN **CONDITIONAL** + "
        "DATA_VERDICT_PM004_L3_SEP11_EDGE **CLEARED** · lock B (bar_end < decision_time) · "
        "named 855/855 · L3 ≠ oracle · no PM-003 · no CF"
    )
    lines.append("**Slice use:** USED_RESEARCH — not validation, not sealed holdout")
    lines.append(f"**Overall verdict:** `{payload['overall_verdict']}`")
    lines.append(f"**invented_numbers:** `{payload['invented_numbers']}`")
    lines.append("**Trading:** FORBIDDEN")
    lines.append(
        "**Stamp:** Sep-12 PM-004; lock B; L3 ≠ oracle; no PM-003; θ/W frozen no search; "
        "Governor SIGN F4."
    )
    lines.append(
        "**Annex:** N_wick + wick-subset Δ + λ grid report-only (not a leaderboard)"
    )
    lines.append(f"**Run UTC:** `{payload['run_utc']}`")
    lines.append(f"**SHA256 recorded:** `{payload['data']['sha256_recorded']}`")
    lines.append("")
    lines.append("## Authority")
    for a in payload["authority"]:
        lines.append(f"- `{a}`")
    lines.append("")
    lines.append("## Frozen map")
    lines.append(f"- ε={EPS}; θ={THETA}; W={W_WICK}; λ={LAMBDA_SCORED}; Wσ={W_SIGMA}")
    lines.append("- Lock B only: bar usable iff bar_end_ms < decision_time_ms")
    lines.append("- m = PM-004 same-row mid (Sep-12 only; method=mid)")
    lines.append("- S_t = close of last L3 bar with bar_end < t")
    lines.append("- S_tW = close W completed steps back in same lock-B chain")
    lines.append(
        "- σhat = RMS(log returns of prior Wσ completed lock-B bars) "
        "* sqrt(365.25*24*60)"
    )
    lines.append("- τ = time_remaining_sec / (365.25*24*3600); K = FLOOR_STRIKE")
    lines.append("- z = ln(S_t/K) / (σhat * sqrt(τ)); p_s = Φ(z)")
    lines.append(
        "- wick = abs(ln(S_t/S_tW)) > θ * σhat * sqrt(W/(365.25*24*60))"
    )
    lines.append("- if ABSTAIN or m missing or not lookback_ok: p = m")
    lines.append("- elif not wick: p = m   # Feature silence; Δ=0 by construction")
    lines.append(f"- else: p = clip((1-λ)*m + λ*p_s, ε, 1-ε) with λ={LAMBDA_SCORED}")
    lines.append(
        f"- Robustness annex λ∈{list(LAMBDA_ROBUST)} report-only — NO θ/W grid. λ=0 ⇒ Δ=0."
    )
    lines.append("")
    lines.append("## Filters / join")
    lines.append("- venue=KALSHI, window=15m; BTC/ETH **separate** (no pool)")
    lines.append("- Sep-12 PM-004 mid only — **no** PM-003 · **no** Sep-13 · **no** PM-002 union")
    lines.append("- Headlines only: T-5m (rem=300); **no** T-14m · **no** T-10m speak")
    lines.append("- `implied_p_method == mid` only; last-fallback excluded")
    lines.append("- exclude `implied_p ≤ 0.02` or `≥ 0.98` (near-deg)")
    lines.append("- VOID/DISPUTED out of scored N")
    lines.append(
        "- L3 = L3-002 Sep-12 + L3-001 Sep-11 bars for lookback/edges under lock B; "
        "L3 ≠ CF settlement oracle"
    )
    lines.append("- Missing W=5 chain or incomplete Wσ → ABSTAIN (p:=m), not “no wick”")
    lines.append("- **NOT** policy A. **NOT** PM-003. **NOT** F1-always-speak. **NOT** W2-B.")
    lines.append("")
    lines.append(
        "**Sign convention:** ΔBrier = Brier_model − Brier_market; "
        "ΔLogLoss = LogLoss_model − LogLoss_market; **negative = skill** vs mid."
    )
    lines.append("")
    lines.append(
        f"**Skill rule:** both Δ < 0 on full cell. Kill if either Δ ≥ 0, "
        f"N_wick < {MIN_N_WICK_KILL}, or one headline works and the other inverts. "
        "Not NO_EDGE. Not Champion. N_wick / wick-subset Δ = annex only."
    )
    lines.append("")
    lines.append("## Overall reason")
    lines.append(payload["overall_reason"])
    lines.append("")
    lines.append("## Headlines (AMD-005, no pool, no annex speak)")
    lines.append("")
    lines.append(
        "| Cell | N | N_wick | speak | Brier_model | Brier_market | ΔBrier | "
        "LogLoss_model | LogLoss_market | ΔLogLoss | mean(m) | mean(p) | ECE | Verdict |"
    )
    lines.append(
        "|------|--:|-------:|------:|------------:|-------------:|-------:|"
        "--------------:|---------------:|---------:|--------:|--------:|-----|---------|"
    )
    for cid in HEADLINES:
        c = payload["headlines"][cid]
        lines.append(
            f"| `{cid}` | {c['N']} | {c['N_wick']} | {c['n_speak']} | "
            f"{_fmt_num(c['Brier_model'])} | {_fmt_num(c['Brier_market'])} | "
            f"{_fmt_num(c['ΔBrier'])} | {_fmt_num(c['LogLoss_model'])} | "
            f"{_fmt_num(c['LogLoss_market'])} | {_fmt_num(c['ΔLogLoss'])} | "
            f"{_fmt_num(c.get('mean(m)'), 4)} | {_fmt_num(c.get('mean(p)'), 4)} | "
            f"{_fmt_num(c['ECE'])} | `{c['cell_verdict']}` |"
        )
    lines.append("")
    for cid in HEADLINES:
        c = payload["headlines"][cid]
        lines.append(f"### `{cid}`")
        lines.append(
            f"- N={c['N']}; N_wick={c['N_wick']}; n_speak={c['n_speak']}; "
            f"n_allow={c['n_allow']}; n_off_wick={c['n_off_wick']}; "
            f"n_abstain={c['n_abstain']}; speak_rate={_fmt_num(c.get('speak_rate'), 4)}"
        )
        lines.append(
            f"- mean(m)_all={_fmt_num(c.get('mean(m)_all'), 4)}; "
            f"mean(p)_all={_fmt_num(c.get('mean(p)_all'), 4)}; "
            f"mean(m)_speak={_fmt_num(c.get('mean(m)_speak'), 4)}; "
            f"mean(p)_speak={_fmt_num(c.get('mean(p)_speak'), 4)}"
        )
        lines.append(
            f"- mean(S_t)={_fmt_num(c.get('mean(S_t)'))}; "
            f"mean(K)={_fmt_num(c.get('mean(K)'))}; "
            f"mean(σhat)={_fmt_num(c.get('mean(σhat)'))}; "
            f"mean(p_s)_speak={_fmt_num(c.get('mean(p_s)_speak'))}"
        )
        lines.append(f"- Reason: {c['cell_reason']}")
        lines.append(f"- Calibration: {c['Calibration']['note']}")
        lines.append(f"- ECE_market: {_fmt_num(c.get('ECE_market'))}")
        wa = c.get("wick_subset_annex") or {}
        lines.append(
            f"- Wick-subset annex (not leaderboard): N_wick={wa.get('N_wick')}; "
            f"ΔBrier={_fmt_num(wa.get('ΔBrier'))}; ΔLogLoss={_fmt_num(wa.get('ΔLogLoss'))}"
        )
        lines.append("- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no trading)")
        lines.append("")

    lines.append("## Robustness annex (λ grid; not headline; do not pick winner)")
    lines.append("")
    lines.append("| Cell | λ | N | N_wick | ΔBrier | ΔLogLoss | Verdict |")
    lines.append("|------|--:|--:|-------:|-------:|---------:|---------|")
    for cid in HEADLINES:
        for _key, block in payload["robustness"][cid].items():
            lines.append(
                f"| `{cid}` | {block.get('λ', '')} | {block['N']} | "
                f"{block.get('N_wick', '')} | {_fmt_num(block['ΔBrier'])} | "
                f"{_fmt_num(block['ΔLogLoss'])} | `{block['cell_verdict']}` |"
            )
    lines.append("")

    lines.append("## Placebos (report, not headline switch)")
    lines.append("")
    lines.append("| Placebo | Cell | N | N_wick_effective | ΔBrier | ΔLogLoss | Notes |")
    lines.append("|---------|------|--:|-----------------:|-------:|---------:|-------|")
    for name, by_cell in payload["placebos"].items():
        for cid in HEADLINES:
            block = by_cell[cid]
            note = block.get("placebo_note", "")
            lines.append(
                f"| `{name}` | `{cid}` | {block['N']} | "
                f"{block.get('N_wick', '')} | {_fmt_num(block['ΔBrier'])} | "
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
    lines.append(f"- L3-002 BTC csv sha256: `{payload['data']['l3_002_btc_sha256']}`")
    lines.append(f"- L3-002 ETH csv sha256: `{payload['data']['l3_002_eth_sha256']}`")
    lines.append(f"- sha256_recorded: `{payload['data']['sha256_recorded']}`")
    lines.append(f"- venues: `{payload['data']['venue_check']['venues']}`")
    lines.append("- Join verdict: **CONDITIONAL** (L3-002) + **CLEARED** (L3-001 edges)")
    lines.append("- Join policy: **B** (bar_end < decision_time)")
    lines.append("- Policy A (bar_end ≤ t): **not used**")
    lines.append("- PM-003: **not used**")
    lines.append("- CF / EXPIRATION_VALUE / incomplete-bar / F1-always-speak / W2-B: **not used**")
    lines.append("- L3 = external predictor ≠ settlement oracle")
    lines.append("- No θ/W/λ retune; no gate retune; no pool; no T-14m")
    lines.append("")
    lines.append("## Overall package verdict")
    lines.append(f"**`{payload['overall_verdict']}`** — {payload['overall_reason']}")
    lines.append("")
    lines.append(
        "FAIL-INSUFFICIENT ≠ NO_EDGE. This is **not** a Champion / strategy PASS. "
        "No trading authorization. Holdout closed. Stamp: Sep-12 PM-004; lock B; "
        "L3 ≠ oracle; no PM-003; θ/W frozen; Governor SIGN F4."
    )
    lines.append("")
    lines.append("## Artifacts")
    for p in payload["artifact_paths"]:
        lines.append(f"- `{p}`")
    lines.append("")
    lines.append("## Blockers")
    blockers = payload.get("blockers") or []
    if not blockers:
        lines.append("- (none beyond package verdict)")
    else:
        for b in blockers:
            lines.append(f"- {b}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    run_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_TESTS.mkdir(parents=True, exist_ok=True)
    ARCHIVE_AUDIT.mkdir(parents=True, exist_ok=True)

    cp_sha = _sha256(CHECKPOINTS)
    btc_sha = _sha256(L3_002_BTC)
    eth_sha = _sha256(L3_002_ETH)

    checkpoints = _load_ndjson(CHECKPOINTS)
    coverage_rows = _load_ndjson(COVERAGE)
    coverage = {c["contract_id"]: c for c in coverage_rows}
    labels = load_market_labels()
    books = {"BTC": L3Book("BTC"), "ETH": L3Book("ETH")}

    cells, stats = build_rows(checkpoints, coverage, labels, books)

    headlines: dict[str, dict[str, Any]] = {}
    robustness: dict[str, dict[str, Any]] = {}
    placebos: dict[str, dict[str, Any]] = {
        "lambda_0": {},
        "shuffle_wick": {},
        "reverse_gate": {},
        "sign_flip_ps": {},
    }

    for cid in HEADLINES:
        rows = cells[cid]
        p = apply_map(rows, lam=LAMBDA_SCORED)
        block = score_forecast(
            rows, p, feature_id=FEATURE_ID, map_label=f"λ={LAMBDA_SCORED}_wick_gate"
        )
        headlines[cid] = block

        rob: dict[str, Any] = {}
        for lam in LAMBDA_ROBUST:
            pr = apply_map(rows, lam=lam)
            br = score_forecast(
                rows, pr, feature_id=FEATURE_ID, map_label=f"λ={lam}_robust"
            )
            br["λ"] = lam
            rob[f"λ={lam}"] = br
        robustness[cid] = rob

        p0 = placebo_lambda_zero(rows)
        b0 = score_forecast(rows, p0, feature_id=FEATURE_ID, map_label="placebo_λ=0")
        b0["placebo_note"] = (
            f"λ=0 identity check pass={abs(float(b0['ΔBrier'])) < 1e-15 and abs(float(b0['ΔLogLoss'])) < 1e-15}"
            if b0["ΔBrier"] != "UNTESTED"
            else "λ=0 identity"
        )
        placebos["lambda_0"][cid] = b0

        # placebos that reorder rows must re-score aligned ordered lists
        ordered = sorted(
            rows, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec)
        )
        ps = placebo_shuffle_wick(rows, cid)
        bs = score_forecast(
            ordered, ps, feature_id=FEATURE_ID, map_label="placebo_shuffle_wick"
        )
        bs["placebo_note"] = "wick labels shuffled within ALLOW rows; m fixed"
        placebos["shuffle_wick"][cid] = bs

        pr = placebo_reverse_gate(rows)
        brv = score_forecast(
            rows, pr, feature_id=FEATURE_ID, map_label="placebo_reverse_gate"
        )
        brv["placebo_note"] = "blend only when NO wick (reverse gate)"
        placebos["reverse_gate"][cid] = brv

        pf = placebo_sign_flip_ps(rows)
        bf = score_forecast(
            rows, pf, feature_id=FEATURE_ID, map_label="placebo_sign_flip_ps"
        )
        bf["placebo_note"] = "p_s → 1−p_s on wick rows"
        placebos["sign_flip_ps"][cid] = bf

    overall, reason = package_verdict(headlines)

    blockers = []
    for cid in HEADLINES:
        b = headlines[cid]
        if b.get("N_wick", 0) < MIN_N_WICK_KILL:
            blockers.append(f"{cid}: N_wick={b.get('N_wick')} < {MIN_N_WICK_KILL}")
        if b.get("ΔBrier") != "UNTESTED" and (
            float(b["ΔBrier"]) >= 0 or float(b["ΔLogLoss"]) >= 0
        ):
            blockers.append(
                f"{cid}: skill fail ΔBrier={b['ΔBrier']} ΔLogLoss={b['ΔLogLoss']}"
            )

    out_stem = f"{TEST_ID}-{PACKAGE}"
    out_json = OUT_DIR / f"{out_stem}.json"
    out_md = OUT_DIR / f"{out_stem}.md"
    artifact_paths = [
        str(out_md),
        str(out_json),
        str(ARCHIVE_TESTS / f"{out_stem}.md"),
        str(ARCHIVE_TESTS / f"{out_stem}.json"),
    ]

    venues = sorted({r.get("venue") for r in checkpoints if r.get("venue")})
    payload: dict[str, Any] = {
        "TEST_ID": TEST_ID,
        "package": PACKAGE,
        "feature_id": FEATURE_ID,
        "gate_id": GATE_ID,
        "incumbent": INCUMBENT,
        "overall_verdict": overall,
        "overall_reason": reason,
        "invented_numbers": False,
        "trading": "FORBIDDEN",
        "run_utc": run_utc,
        "authority": AUTHORITY,
        "frozen_map": {
            "ε": EPS,
            "θ": THETA,
            "W": W_WICK,
            "λ": LAMBDA_SCORED,
            "Wσ": W_SIGMA,
            "lock": "B",
            "bar_end_rule": "bar_end_ms < decision_time_ms",
        },
        "stamps": {
            "tape": "Sep-12 PM-004",
            "lock": "B",
            "L3_ne_oracle": True,
            "no_PM003": True,
            "theta_W_frozen_no_search": True,
            "governor_sign": "GOVERNOR_SIGN_F4_WICK_2026-09-14.md",
            "coverage_named": "855/855",
        },
        "headlines": headlines,
        "robustness": robustness,
        "placebos": placebos,
        "filter_stats": stats,
        "blockers": blockers,
        "data": {
            "dataset_id": "DATA-PROV-PM-004",
            "l3_dataset_id": "DATA-PROV-L3-002",
            "l3_edge_dataset_id": "DATA-PROV-L3-001",
            "checkpoints_path": str(CHECKPOINTS),
            "checkpoints_sha256": cp_sha,
            "l3_002_btc_sha256": btc_sha,
            "l3_002_eth_sha256": eth_sha,
            "sha256_recorded": True,
            "venue_check": {"venues": venues, "kalshi_only": venues == ["KALSHI"]},
            "K_source": "PM-004 raw settled markets floor_strike (Sep-12; PM-001 tape ends Sep-11)",
            "y_source": "PM-004 settled result / resolved_universe RESULT",
            "EXPIRATION_VALUE_used": False,
            "PM003_used": False,
        },
        "artifact_paths": artifact_paths,
        "placebo_seed": PLACEBO_SEED,
        "named_edge_keys": [list(x) for x in sorted(NAMED_EDGE_KEYS)],
    }

    md = build_markdown(payload)
    out_json.write_text(json.dumps(payload, indent=2, default=str) + "\n")
    out_md.write_text(md)
    (ARCHIVE_TESTS / f"{out_stem}.json").write_text(out_json.read_text())
    (ARCHIVE_TESTS / f"{out_stem}.md").write_text(out_md.read_text())

    # Brief audit stamp
    audit = ARCHIVE_AUDIT / f"2026-09-14-Examiner-{TEST_ID}-F4-WICK.md"
    audit.write_text(
        f"# Audit — {TEST_ID} F4-WICK-INCREMENTAL\n\n"
        f"- **UTC:** {run_utc}\n"
        f"- **Verdict:** {overall}\n"
        f"- **Artifacts:** `{out_md}`, `{out_json}`\n"
        f"- **Stamp:** Sep-12 PM-004; lock B; L3 ≠ oracle; no PM-003; θ/W frozen; Governor SIGN F4.\n"
        f"- **invented_numbers:** false\n"
        f"- **Trading:** FORBIDDEN\n"
    )

    print(f"Wrote {out_md}")
    print(f"Wrote {out_json}")
    print(f"Overall: {overall}")
    for cid in HEADLINES:
        h = headlines[cid]
        print(
            f"  {cid}: N={h['N']} N_wick={h['N_wick']} "
            f"ΔBrier={h['ΔBrier']} ΔLogLoss={h['ΔLogLoss']} → {h['cell_verdict']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
