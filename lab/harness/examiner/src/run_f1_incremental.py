#!/usr/bin/env python3
"""TEST-20260912-002 — F1-INCREMENTAL vs MKT-KALSHI-15M-MID.

Atomic incrementality of FEAT-20260912-001 and FEAT-20260912-002
versus frozen Kalshi mid on DATA-PROV-PM-003 + L3-001. No MLE.
No ensemble. No trading. invented_numbers=false.
Never EXPIRATION_VALUE. Never incomplete-bar close.
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

from src.f1_incremental import (  # noqa: E402
    ALL_CELLS,
    ANNEX_CELLS,
    ANN_FACTOR,
    EPS_P,
    HEADLINE_CELLS,
    LAMBDA_ROBUST,
    LAMBDA_SCORED,
    PLACEBO_SEED,
    S_MAX_LAG_MS,
    SIGMA_FROZEN,
    W_RV,
    FeatRow,
    apply_feat001,
    apply_feat002,
    placebo_shuffle_sigma_rv,
    rows_for_feat001,
    rows_for_feat002,
    rv_earns_keep,
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
L3_BTC = LAB / "data/DATA-PROV-L3-001/derived/BTCUSDT_1m_spot_2026-09-04_2026-09-11.parquet"
L3_ETH = LAB / "data/DATA-PROV-L3-001/derived/ETHUSDT_1m_spot_2026-09-04_2026-09-11.parquet"
OUT_DIR = LAB / "harness/examiner/out"
ARCHIVE_TESTS = LAB / "archive/tests"
ARCHIVE_AUDIT = LAB / "archive/audit"

TEST_ID = "TEST-20260912-002"
PACKAGE = "F1-INCREMENTAL"
INCUMBENT = "MKT-KALSHI-15M-MID"

AUTHORITY = [
    "governance/EXAMINER_ORDER_TEST-20260912-002-F1.md",
    "governance/L3_001_COVERAGE_FROZEN_2026-09-12.md",
    "archive/features/FEAT-20260912-001.md",
    "archive/features/FEAT-20260912-002.md",
    "data/DATA-PROV-L3-001/provenance/DATA_VERDICT_DATA-PROV-L3-001.md",
    "governance/BINARY_EXAMINER_SPEC.md",
    "harness/examiner/src/pm003_market_baseline.py",
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


def _parse_decision_ms(decision_time: str) -> int:
    """Parse ISO Z timestamp to epoch ms."""
    dt = datetime.fromisoformat(decision_time.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)


class L3Book:
    """Completed-bar L3 join + trailing RV (no incomplete bar)."""

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
        # Precompute log returns between consecutive completed bars.
        with np.errstate(divide="ignore", invalid="ignore"):
            self.log_ret = np.empty(len(self.closes), dtype=np.float64)
            self.log_ret[0] = np.nan
            self.log_ret[1:] = np.log(self.closes[1:] / self.closes[:-1])
        # Trailing RMS of last W returns ending at each bar index i (inclusive),
        # annualized. Requires indices i-W+1 .. i all valid returns → need i >= W.
        self.sigma_at = np.full(len(self.closes), np.nan, dtype=np.float64)
        if len(self.closes) > W_RV:
            # squared returns; index i uses returns at i-W+1 .. i (W returns)
            sq = self.log_ret ** 2
            # cumulative sum of sq with nan→0 for prefix, then check finite count
            finite = np.isfinite(sq).astype(np.float64)
            sq0 = np.where(np.isfinite(sq), sq, 0.0)
            csum_sq = np.cumsum(sq0)
            csum_n = np.cumsum(finite)
            for i in range(W_RV, len(self.closes)):
                # returns indices (i-W+1) .. i inclusive = W returns
                # but return at j uses closes[j]/closes[j-1], so j>=1
                lo = i - W_RV + 1
                n = csum_n[i] - (csum_n[lo - 1] if lo > 0 else 0.0)
                if n < W_RV:
                    continue
                ssq = csum_sq[i] - (csum_sq[lo - 1] if lo > 0 else 0.0)
                rms = math.sqrt(ssq / W_RV)
                if rms > 0 and math.isfinite(rms):
                    self.sigma_at[i] = rms * ANN_FACTOR

    def knowable_idx(self, decision_time_ms: int) -> Optional[int]:
        """argmax { bar | close_time_ms <= decision_time_ms }."""
        # searchsorted right → first index with close_ms > decision → idx-1
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
        # Binding slice identity: open_time_ms == decision_time_ms - 60000
        join_ok = open_ms == decision_time_ms - 60_000
        # Guard: never use incomplete bar (open == floor minute of decision)
        if open_ms == (decision_time_ms // 60_000) * 60_000:
            # That would be the bar that opens AT decision — incomplete at t
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
            "sigma_rv": (
                float(self.sigma_at[j]) if math.isfinite(self.sigma_at[j]) else None
            ),
        }


def collect_cells(
    checkpoints: list[dict],
    kalshi_idx: dict,
    books: dict[str, L3Book],
) -> tuple[dict[str, list[FeatRow]], dict[str, Any]]:
    cells: dict[str, list[FeatRow]] = {cid: [] for cid in ALL_CELLS}
    stats: dict[str, Any] = {
        "candidates": 0,
        "excluded_method_not_mid": 0,
        "excluded_near_deg": 0,
        "excluded_no_label": 0,
        "excluded_void_or_other": 0,
        "excluded_missing_floor_strike": 0,
        "excluded_missing_S_t": 0,
        "excluded_join_lag_gt_90s": 0,
        "mid_reconstruct_mismatch": 0,
        "join_open_eq_decision_minus_60s": 0,
        "join_open_ne_decision_minus_60s": 0,
        "scored_base_with_S_t": 0,
        "expiration_value_read": False,
        "incomplete_bar_used": False,
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
        # NEVER use EXPIRATION_VALUE — only FLOOR_STRIKE + RESOLUTION
        k_raw = lab.get("FLOOR_STRIKE")
        if k_raw is None:
            stats["excluded_missing_floor_strike"] += 1
            continue
        try:
            k = float(k_raw)
        except (TypeError, ValueError):
            stats["excluded_missing_floor_strike"] += 1
            continue
        if not math.isfinite(k) or k <= 0:
            stats["excluded_missing_floor_strike"] += 1
            continue
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
        m_t = m_t_from_checkpoint(r)
        bid = r.get("yes_bid")
        ask = r.get("yes_ask")
        if bid is not None and ask is not None:
            try:
                recon = (float(bid) + float(ask)) / 2.0
                if abs(recon - m_t) > 1e-9:
                    stats["mid_reconstruct_mismatch"] += 1
            except (TypeError, ValueError):
                pass
        dt = r.get("decision_time") or ""
        decision_ms = _parse_decision_ms(dt)
        join = books[asset].price_at_t(decision_ms)
        if join is None:
            # distinguish lag vs no bar
            j = books[asset].knowable_idx(decision_ms)
            if j is None:
                stats["excluded_missing_S_t"] += 1
            else:
                stats["excluded_join_lag_gt_90s"] += 1
            continue
        if join["join_ok_open_eq_decision_minus_60s"]:
            stats["join_open_eq_decision_minus_60s"] += 1
        else:
            stats["join_open_ne_decision_minus_60s"] += 1
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
                decision_time=dt,
                decision_time_ms=decision_ms,
                m_t=m_t,
                y=y,
                k=k,
                s_t=join["s_t"],
                bar_open_time_ms=join["open_time_ms"],
                bar_close_time_ms=join["close_time_ms"],
                sigma_frozen=SIGMA_FROZEN[asset],
                sigma_rv=join["sigma_rv"],
                join_ok_open_eq_decision_minus_60s=join[
                    "join_ok_open_eq_decision_minus_60s"
                ],
            )
        )
        stats["scored_base_with_S_t"] += 1
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
    if which == "001":
        p_rows = {cid: rows_for_feat001(cells[cid]) for cid in ALL_CELLS}
        p_fn = lambda rs, lam=LAMBDA_SCORED: apply_feat001(rs, lam=lam)  # noqa: E731
        map_label = (
            f"p=clip((1-{LAMBDA_SCORED})m+{LAMBDA_SCORED}*Φ(ln(S/K)/(σ√τ)),{EPS_P},1-{EPS_P}); "
            f"σ_BTC={SIGMA_FROZEN['BTC']} σ_ETH={SIGMA_FROZEN['ETH']}"
        )
        drop_key = "excluded_missing_feat001"
    elif which == "002":
        p_rows = {cid: rows_for_feat002(cells[cid]) for cid in ALL_CELLS}
        p_fn = lambda rs, lam=LAMBDA_SCORED: apply_feat002(rs, lam=lam)  # noqa: E731
        map_label = (
            f"same Φ blend λ={LAMBDA_SCORED}; σ_t=RMS W={W_RV} completed 1m log-returns "
            f"bar_end≤t annualized *sqrt(365.25*24*60); no frozen-σ fallback"
        )
        drop_key = "excluded_missing_feat002_W_incomplete"
    else:
        raise ValueError(which)

    headlines = {
        cid: score_forecast(
            p_rows[cid], p_fn(p_rows[cid]), feature_id=feature_id, map_label=map_label
        )
        for cid in HEADLINE_CELLS
    }
    annex = {
        cid: score_forecast(
            p_rows[cid], p_fn(p_rows[cid]), feature_id=feature_id, map_label=map_label
        )
        for cid in ANNEX_CELLS
    }

    drops = {cid: len(cells[cid]) - len(p_rows[cid]) for cid in ALL_CELLS}

    # λ robustness on each headline cell (annex only — do not pick winner)
    robustness: dict[str, Any] = {
        "note": "λ grid annex only — not headline; do not pick winner by Δ on this slice",
        "headline_cells": {},
    }
    for cid in HEADLINE_CELLS:
        rob: dict[str, Any] = {}
        rs = p_rows[cid]
        for lam in LAMBDA_ROBUST:
            ps = p_fn(rs, lam)
            rob[f"λ={lam}"] = score_forecast(
                rs, ps, feature_id=feature_id, map_label=f"robustness λ={lam}"
            )
        # λ=0 must give Δ≈0
        ps0 = p_fn(rs, 0.0)
        rob["λ=0 (must Δ≈0)"] = score_forecast(
            rs, ps0, feature_id=feature_id, map_label="placebo/ablation λ=0 ≡ mid"
        )
        if which == "002" and rs:
            ordered = sorted(
                rs, key=lambda r: (r.contract_id, r.decision_time, r.time_remaining_sec)
            )
            rob["placebo_shuffle_σ_t"] = score_forecast(
                ordered,
                placebo_shuffle_sigma_rv(rs, cid),
                feature_id=feature_id,
                map_label="placebo: shuffle σ_t leaving (S,K,τ) fixed",
            )
        robustness["headline_cells"][cid] = rob
    robustness["placebo_seed"] = PLACEBO_SEED

    # Card-level verdict from BOTH headlines (separate, no pool)
    h_verdicts = [headlines[cid]["cell_verdict"] for cid in HEADLINE_CELLS]
    n_inc = sum(1 for v in h_verdicts if v == "INCREMENTAL_RESEARCH")
    if n_inc == len(HEADLINE_CELLS):
        card_verdict = "INCREMENTAL_RESEARCH"
        card_reason = (
            "both headline cells improve Brier and LogLoss vs mid (USED_RESEARCH only)"
        )
    elif n_inc == 0:
        card_verdict = "REDUNDANT / FAIL-INSUFFICIENT"
        card_reason = (
            "no headline cell improves both ΔBrier and ΔLogLoss vs mid; "
            "REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)"
        )
    else:
        card_verdict = "MIXED_ATOMIC / FAIL-INSUFFICIENT"
        card_reason = (
            "only one of BTC/ETH T-5m headlines incremental; no pooled rescue; "
            "FAIL-INSUFFICIENT ≠ NO_EDGE"
        )

    return {
        "feature_id": feature_id,
        "frozen_map": map_label,
        "mle": False,
        "ensemble": False,
        "headline_cells": headlines,
        "annex_cells": annex,
        "robustness": robustness,
        "card_verdict": card_verdict,
        "card_reason": card_reason,
        drop_key: drops,
        "N_base_with_S_t": {cid: len(cells[cid]) for cid in ALL_CELLS},
        "N_after_feature_filter": {cid: len(p_rows[cid]) for cid in ALL_CELLS},
        "_rows": p_rows,  # internal for RV comparison; stripped before write
    }


def build_markdown(payload: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append(f"# {payload['TEST_ID']} — {payload['package']} vs {payload['incumbent']}")
    lines.append("")
    lines.append(f"**TEST_ID:** `{payload['TEST_ID']}`")
    lines.append(f"**Package:** `{payload['package']}`")
    lines.append(f"**Incumbent:** `{payload['incumbent']}` (TEST-20260911-007 mid-only)")
    lines.append("**Purpose:** atomic incrementality of two F1 frozen no-fit maps vs Kalshi mid")
    lines.append(
        f"**DATA:** `{payload['data']['dataset_id']}` + `{payload['data']['l3_dataset_id']}` "
        "+ PM-001 FLOOR_STRIKE / RESOLUTION"
    )
    lines.append("**Slice use:** USED_RESEARCH — not validation, not sealed holdout")
    lines.append(f"**Overall verdict:** `{payload['overall_verdict']}`")
    lines.append(f"**invented_numbers:** `{payload['invented_numbers']}`")
    lines.append("**Trading:** FORBIDDEN")
    lines.append("**MLE / ensemble 001+002:** forbidden and not run")
    lines.append("**EXPIRATION_VALUE / incomplete-bar close:** NOT USED")
    lines.append(f"**Run UTC:** `{payload['run_utc']}`")
    lines.append(f"**SHA256 verified:** `{payload['data']['sha256_verified']}`")
    lines.append("")
    lines.append("## Authority")
    for a in payload["authority"]:
        lines.append(f"- `{a}`")
    lines.append("")
    lines.append("## Filters / join (TEST-007 excludes + L3 completed-bar)")
    lines.append("- venue=KALSHI, window=15m; BTC/ETH **separate** (no pool)")
    lines.append("- DATA-PROV-PM-003 1208-slice only — **no** PM-002 union")
    lines.append("- checkpoints: T-14m (840), T-10m (600), T-5m (300)")
    lines.append("- `implied_p_method == mid` only; last-fallback excluded")
    lines.append("- exclude `implied_p ≤ 0.02` or `≥ 0.98` (near-deg)")
    lines.append("- VOID/DISPUTED out of scored N")
    lines.append("- K = PM-001 `FLOOR_STRIKE` (never `EXPIRATION_VALUE`)")
    lines.append(
        "- S_t = L3 completed 1m close: knowable_bar = argmax{bar | close_time_ms ≤ decision_time_ms}"
    )
    lines.append("- On this slice: open_time_ms = decision_time_ms − 60000 (verified in stats)")
    lines.append("- No incomplete-bar close. Binance L3 is NOT the oracle.")
    lines.append("- FEAT-002: drop if W=60 incomplete (no frozen-σ fallback)")
    lines.append("- m_t = checkpoint `implied_p` mid — never LAST_PRICE / OUTCOME_PRICES")
    lines.append("")
    lines.append(
        "**Sign convention:** ΔBrier = Brier_model − Brier_market; "
        "ΔLogLoss = LogLoss_model − LogLoss_market; **negative = skill** vs mid."
    )
    lines.append("")
    lines.append(
        "**Falsification:** if both Δ≥0 on a headline cell → `REDUNDANT / FAIL-INSUFFICIENT` "
        "(not `NO_EDGE`). Skill requires **both** Δ < 0. No BTC+ETH pool."
    )
    lines.append("")
    lines.append(
        "**Headline cells (pre-registered, separate):** "
        + ", ".join(f"`{c}`" for c in HEADLINE_CELLS)
    )
    lines.append("Other four cells = annex. λ∈{0.20,0.35,0.50} robustness — do not pick winner.")
    lines.append("")

    for feat_key, title, formula in (
        (
            "FEAT-20260912-001",
            "Card 1 — FEAT-20260912-001 (frozen σ digital)",
            r"\(z=\ln(S/K)/(\sigma\sqrt{\tau})\); \(p=\mathrm{clip}((1-0.35)m+0.35\Phi(z),10^{-4},1-10^{-4})\); \(\sigma_{BTC}=0.55,\sigma_{ETH}=0.70\)",
        ),
        (
            "FEAT-20260912-002",
            "Card 2 — FEAT-20260912-002 (RV σ digital)",
            r"same Φ blend; \(\sigma_t=\mathrm{RMS}_{W=60}(r_i)\times\sqrt{365.25\cdot24\cdot60}\); no frozen-σ fallback",
        ),
    ):
        card = payload["cards"][feat_key]
        lines.append(f"## {title}")
        lines.append("")
        lines.append(f"**Frozen map (headline, no-fit):** {formula}")
        lines.append(f"**Card verdict (both headlines):** `{card['card_verdict']}`")
        lines.append(f"**Reason:** {card['card_reason']}")
        lines.append("")
        lines.append("### Headline cells (λ=0.35 scored)")
        lines.append("")
        lines.append(
            "| Cell | N | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | mean(m) | mean(p) | ECE | Verdict |"
        )
        lines.append(
            "|------|--:|------------:|-------------:|-------:|--------------:|---------------:|---------:|--------:|--------:|-----|---------|"
        )
        for cid in HEADLINE_CELLS:
            prim = card["headline_cells"][cid]
            lines.append(
                f"| `{cid}` | {prim['N']} | {_fmt_num(prim['Brier_model'])} | "
                f"{_fmt_num(prim['Brier_market'])} | {_fmt_num(prim['ΔBrier'])} | "
                f"{_fmt_num(prim['LogLoss_model'])} | {_fmt_num(prim['LogLoss_market'])} | "
                f"{_fmt_num(prim['ΔLogLoss'])} | {_fmt_num(prim['mean(m_t)'], 4)} | "
                f"{_fmt_num(prim['mean(p_t)'], 4)} | {_fmt_num(prim['ECE'])} | "
                f"`{prim['cell_verdict']}` |"
            )
        lines.append("")
        for cid in HEADLINE_CELLS:
            prim = card["headline_cells"][cid]
            lines.append(
                f"- `{cid}` WR (descriptive): `{_fmt_num(prim['WR'], 4)}` "
                f"N_WR={prim.get('N_WR')} CI={_fmt_ci(prim.get('CI'))}; "
                f"mean(S_t)={_fmt_num(prim.get('mean(S_t)'))}; "
                f"mean(K)={_fmt_num(prim.get('mean(K)'))}; "
                f"mean(σ)={_fmt_num(prim.get('mean(σ_rv)') if feat_key.endswith('002') else prim.get('mean(σ_frozen)'))}"
            )
        lines.append("- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no action rule / no trading)")
        lines.append("")
        lines.append("### Annex — other four cells (same frozen map; not headline)")
        lines.append("")
        lines.append(
            "| Cell | N | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | mean(m) | mean(p) | ECE | Verdict |"
        )
        lines.append(
            "|------|--:|------------:|-------------:|-------:|--------------:|---------------:|---------:|--------:|--------:|-----|---------|"
        )
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
        lines.append("### Robustness annex (λ grid + placebos; do not pick winner)")
        lines.append("")
        for cid in HEADLINE_CELLS:
            lines.append(f"**{cid}**")
            lines.append("")
            lines.append("| Variant | N | ΔBrier | ΔLogLoss | Brier_model | LogLoss_model | Verdict |")
            lines.append("|---------|--:|-------:|---------:|------------:|--------------:|---------|")
            rob = card["robustness"]["headline_cells"][cid]
            for k, block in rob.items():
                lines.append(
                    f"| `{k}` | {block['N']} | {_fmt_num(block['ΔBrier'])} | "
                    f"{_fmt_num(block['ΔLogLoss'])} | {_fmt_num(block['Brier_model'])} | "
                    f"{_fmt_num(block['LogLoss_model'])} | `{block['cell_verdict']}` |"
                )
            lines.append("")

    lines.append("## RV earn-keep (002 vs 001 on headlines)")
    lines.append("")
    lines.append("| Cell | N_001 | N_002 | ΔBrier_001 | ΔBrier_002 | ΔLogLoss_001 | ΔLogLoss_002 | 002 earns keep? |")
    lines.append("|------|------:|------:|-----------:|-----------:|-------------:|-------------:|:----------------|")
    for cid in HEADLINE_CELLS:
        ek = payload["rv_vs_frozen"][cid]
        lines.append(
            f"| `{cid}` | {ek['N_001']} | {ek['N_002']} | "
            f"{_fmt_num(ek['ΔBrier_001'])} | {_fmt_num(ek['ΔBrier_002'])} | "
            f"{_fmt_num(ek['ΔLogLoss_001'])} | {_fmt_num(ek['ΔLogLoss_002'])} | "
            f"**{ek['earns_keep']}** |"
        )
    lines.append("")
    lines.append(f"**RV package note:** {payload['rv_vs_frozen']['package_note']}")
    lines.append("")

    lines.append("## Filter / join stats")
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
    lines.append("- EXPIRATION_VALUE: **not read / not scored**")
    lines.append("- incomplete-bar close: **not used**")
    lines.append("- LAST_PRICE / OUTCOME_PRICES as m_t: **forbidden / not used**")
    lines.append("- Binance L3: external predictor only — **NOT** settlement oracle")
    lines.append("- No MLE; no ensemble of 001+002; trading FORBIDDEN")
    lines.append(f"- join open==decision−60s: `{payload['filter_stats']['join_open_eq_decision_minus_60s']}`")
    lines.append(f"- join open≠decision−60s: `{payload['filter_stats']['join_open_ne_decision_minus_60s']}`")
    lines.append("")
    lines.append("## Overall package verdict")
    lines.append(f"**`{payload['overall_verdict']}`** — {payload['overall_reason']}")
    lines.append("")
    lines.append(
        "FAIL-INSUFFICIENT ≠ NO_EDGE. This is **not** a strategy PASS. "
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
        f"# {TEST_ID} — DATA_INTEGRITY_FAIL\n\n{reason}\n\n"
        "invented_numbers: false\nTrading: FORBIDDEN\n"
    )
    (ARCHIVE_TESTS / f"{out_stem}.json").write_text(out_json.read_text())
    (ARCHIVE_TESTS / f"{out_stem}.md").write_text(out_md.read_text())
    print(f"DATA_INTEGRITY_FAIL: {reason}", file=sys.stderr)
    return 2


def _package_verdict(card001: dict[str, Any], card002: dict[str, Any], rv_block: dict[str, Any]) -> tuple[str, str]:
    v1 = card001["card_verdict"]
    v2 = card002["card_verdict"]
    inc1 = v1 == "INCREMENTAL_RESEARCH"
    inc2 = v2 == "INCREMENTAL_RESEARCH"
    any_earn = any(
        rv_block[cid]["earns_keep"] for cid in HEADLINE_CELLS if cid in rv_block
    )
    if not inc1 and not inc2:
        return (
            "REDUNDANT / FAIL-INSUFFICIENT",
            (
                "Neither atomic F1 card improves both Brier and LogLoss vs mid "
                f"on both headline T-5m cells. FEAT-001={v1}; FEAT-002={v2}. "
                f"RV earns keep on any headline={any_earn}. "
                "REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE). "
                "USED_RESEARCH; holdout closed; no trading."
            ),
        )
    if inc1 and inc2:
        return (
            "INCREMENTAL_RESEARCH",
            (
                "Both atomic F1 cards improve Brier and LogLoss vs mid on both "
                "headline cells (USED_RESEARCH only). Not validation. Not trading. "
                f"RV earns keep any headline={any_earn}. No ensemble of 001+002."
            ),
        )
    winner = "FEAT-20260912-001" if inc1 else "FEAT-20260912-002"
    loser = "FEAT-20260912-002" if inc1 else "FEAT-20260912-001"
    loser_v = v2 if inc1 else v1
    return (
        "MIXED_ATOMIC / FAIL-INSUFFICIENT",
        (
            f"{winner} incremental on headlines (USED_RESEARCH); "
            f"{loser} {loser_v}. RV earns keep any={any_earn}. "
            "Package is not a strategy PASS; no ensemble; holdout closed; no trading. "
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

    books = {
        "BTC": L3Book(L3_BTC, "BTC"),
        "ETH": L3Book(L3_ETH, "ETH"),
    }

    cells, filt = collect_cells(checkpoints, kalshi_idx, books)

    # Hard integrity: on this slice every join should satisfy open = decision-60s
    if filt["join_open_ne_decision_minus_60s"] != 0:
        return _write_integrity_fail(
            f"join identity failed: {filt['join_open_ne_decision_minus_60s']} rows "
            "with open_time_ms != decision_time_ms - 60000"
        )
    if filt["expiration_value_read"] or filt["incomplete_bar_used"]:
        return _write_integrity_fail("forbidden field / incomplete bar used")

    card001 = _score_card("FEAT-20260912-001", cells, which="001")
    card002 = _score_card("FEAT-20260912-002", cells, which="002")

    # RV vs frozen comparison on headlines (same cell; N may differ if W drops)
    rv_vs: dict[str, Any] = {}
    for cid in HEADLINE_CELLS:
        h1 = card001["headline_cells"][cid]
        h2 = card002["headline_cells"][cid]
        # Prefer same-N comparison on intersection of 002 rows (002 ⊆ 001 typically)
        rows2 = card002["_rows"][cid]
        rows1_by_key = {
            (r.contract_id, r.decision_time, r.time_remaining_sec): r
            for r in card001["_rows"][cid]
        }
        inter = [
            rows1_by_key[(r.contract_id, r.decision_time, r.time_remaining_sec)]
            for r in rows2
            if (r.contract_id, r.decision_time, r.time_remaining_sec) in rows1_by_key
        ]
        if inter and len(inter) == len(rows2):
            s1 = score_forecast(
                inter,
                apply_feat001(inter),
                feature_id="FEAT-20260912-001",
                map_label="same-N vs 002",
            )
            s2 = score_forecast(
                rows2,
                apply_feat002(rows2),
                feature_id="FEAT-20260912-002",
                map_label="same-N vs 001",
            )
            ek = rv_earns_keep(s2["ΔBrier"], s2["ΔLogLoss"], s1["ΔBrier"], s1["ΔLogLoss"])
            rv_vs[cid] = {
                **ek,
                "N_001": h1["N"],
                "N_002": h2["N"],
                "N_same": len(inter),
                "same_N_comparison": True,
                "ΔBrier_001_full": h1["ΔBrier"],
                "ΔLogLoss_001_full": h1["ΔLogLoss"],
            }
        else:
            ek = rv_earns_keep(
                h2["ΔBrier"] if h2["N"] else 0.0,
                h2["ΔLogLoss"] if h2["N"] else 0.0,
                h1["ΔBrier"] if h1["N"] else 0.0,
                h1["ΔLogLoss"] if h1["N"] else 0.0,
            )
            rv_vs[cid] = {
                **ek,
                "N_001": h1["N"],
                "N_002": h2["N"],
                "N_same": 0,
                "same_N_comparison": False,
            }

    any_earn = any(rv_vs[cid]["earns_keep"] for cid in HEADLINE_CELLS)
    both_earn = all(rv_vs[cid]["earns_keep"] for cid in HEADLINE_CELLS)
    if both_earn:
        rv_vs["package_note"] = (
            "FEAT-002 has strictly better (more negative) ΔBrier and ΔLogLoss than "
            "FEAT-001 on both headline cells (same-N) — RV earns keep vs sister. "
            "Sister comparison ≠ skill vs mid; see overall_verdict for mid falsification."
        )
    elif any_earn:
        rv_vs["package_note"] = (
            "FEAT-002 beats FEAT-001 on only one headline — mixed; no pooled rescue; "
            "RV does not fully earn keep vs sister."
        )
    else:
        rv_vs["package_note"] = (
            "FEAT-002 does not beat FEAT-001 on Δ on either headline (same-N) — "
            "RV term REDUNDANT vs sister (do not open a third card)."
        )

    overall, reason = _package_verdict(card001, card002, rv_vs)
    run_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out_stem = f"{TEST_ID}-{PACKAGE}"
    out_json = OUT_DIR / f"{out_stem}.json"
    out_md = OUT_DIR / f"{out_stem}.md"

    # Strip internal row caches before serialize
    for card in (card001, card002):
        card.pop("_rows", None)

    payload: dict[str, Any] = {
        "TEST_ID": TEST_ID,
        "package": PACKAGE,
        "incumbent": INCUMBENT,
        "purpose": "f1_atomic_incrementality_vs_kalshi_mid",
        "strategy": None,
        "mle": False,
        "ensemble_001_002": False,
        "trading": "FORBIDDEN",
        "invented_numbers": False,
        "overall_verdict": overall,
        "overall_reason": reason,
        "run_utc": run_utc,
        "authority": AUTHORITY,
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
            "K_source": "DATA-PROV-PM-001 FLOOR_STRIKE",
            "S_t_source": "DATA-PROV-L3-001 completed 1m close (close_time_ms<=decision_time_ms)",
            "forbidden": [
                "EXPIRATION_VALUE",
                "LAST_PRICE_DOLLARS as m_t",
                "OUTCOME_PRICES as m_t",
                "incomplete-bar close",
                "Binance as oracle",
            ],
            "pm002_checkpoints_read": False,
            "poly_scored": False,
            "venue_check": venue_check,
        },
        "headline_cells": list(HEADLINE_CELLS),
        "annex_cell_order": list(ANNEX_CELLS),
        "cards": {
            "FEAT-20260912-001": card001,
            "FEAT-20260912-002": card002,
        },
        "rv_vs_frozen": rv_vs,
        "filter_stats": {
            **{k: v for k, v in filt.items() if k != "void_bucket"},
            "void_bucket_n": len(filt["void_bucket"]),
            "void_bucket": filt["void_bucket"],
        },
        "sign_conventions": {
            "ΔBrier": "Brier_model − Brier_market; negative = skill vs mid",
            "ΔLogLoss": "LogLoss_model − LogLoss_market; negative = skill vs mid",
            "WR": "descriptive p_t>0.5⇒YES; not skill",
            "falsification_primary": (
                "ΔBrier≥0 AND ΔLogLoss≥0 on a headline cell → "
                "REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)"
            ),
        },
        "confirmations": {
            "EXPIRATION_VALUE_used": False,
            "incomplete_bar_used": False,
            "invented_numbers": False,
            "trading": False,
            "mle": False,
            "ensemble_001_002": False,
            "join_rule": "argmax{bar|close_time_ms<=decision_time_ms}",
            "join_open_eq_decision_minus_60s_all": filt["join_open_ne_decision_minus_60s"]
            == 0,
        },
        "forbidden_actions": [
            "in-sample refit / MLE",
            "ensemble of 001+002",
            "PM-002 union",
            "Poly",
            "EXPIRATION_VALUE",
            "incomplete-bar close",
            "Binance as oracle",
            "trading",
            "invented numbers",
            "pick λ winner from robustness grid",
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
                "EXPIRATION_VALUE_used": False,
                "incomplete_bar_used": False,
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
        f"EXPIRATION_VALUE: not used\n"
        f"incomplete-bar: not used\n"
        f"Full: `{arch_md}`\n"
    )
    audit_path.write_text(
        "# Audit pointer\n\n"
        f"- TEST: `{TEST_ID}`\n"
        f"- Package: `{PACKAGE}` vs `{INCUMBENT}`\n"
        f"- Cards: FEAT-20260912-001, FEAT-20260912-002 (atomic; no ensemble)\n"
        f"- Verdict: `{overall}`\n"
        f"- invented_numbers: false\n"
        f"- Trading: FORBIDDEN\n"
        f"- EXPIRATION_VALUE: not used\n"
        f"- incomplete-bar close: not used\n"
        f"- SHA256 verified: `{digest}`\n"
        f"- L3: DATA-PROV-L3-001 completed-bar join only\n"
        f"- PM-002: not read\n"
        f"- Poly: none\n"
        f"- MLE: none\n"
        f"- Artifacts: `{out_json}`\n"
        f"- Archive: `{arch_json}`\n"
        f"- DATA: PM-003 + PM-001 FLOOR_STRIKE/RESOLUTION + L3-001\n"
        f"- Purpose: F1 incrementality vs mid (USED_RESEARCH; not validation)\n"
    )

    print(f"TEST_ID={TEST_ID}")
    print(f"overall_verdict={overall}")
    print(f"sha256_verified={digest}")
    print(
        f"join_ok={filt['join_open_eq_decision_minus_60s']} "
        f"join_bad={filt['join_open_ne_decision_minus_60s']}"
    )
    for feat_id, card in payload["cards"].items():
        print(f"{feat_id}\tCARD\t{card['card_verdict']}")
        for cid in HEADLINE_CELLS:
            p = card["headline_cells"][cid]
            print(
                f"{feat_id}\tHEADLINE\t{cid}\tN={p['N']}\t"
                f"dB={p['ΔBrier']}\tdLL={p['ΔLogLoss']}\tverdict={p['cell_verdict']}"
            )
        for cid in ANNEX_CELLS:
            c = card["annex_cells"][cid]
            print(
                f"{feat_id}\tANNEX\t{cid}\tN={c['N']}\t"
                f"dB={c['ΔBrier']}\tdLL={c['ΔLogLoss']}\tverdict={c['cell_verdict']}"
            )
    for cid in HEADLINE_CELLS:
        ek = rv_vs[cid]
        print(
            f"RV_vs_001\t{cid}\tearns_keep={ek['earns_keep']}\t"
            f"dB001={ek['ΔBrier_001']}\tdB002={ek['ΔBrier_002']}"
        )
    print(f"wrote {out_json}")
    print(f"wrote {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
