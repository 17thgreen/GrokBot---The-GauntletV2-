"""Run EDGE-20260911-001 RESEARCH (+ VALIDATION if not FAIL). TEST-20260911-001."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any, Optional

import numpy as np
import pandas as pd

from .costs import DEFAULT_COSTS, stress_schedule
from .metrics import (
    concentration_frac,
    distinct_signal_days,
    mean_or_none,
    newey_west_mean_se,
)
from .signal_edge_20260911_001 import (
    build_edge001_frame,
    ohlcv_only_nested_signal,
)
from .trades_features import build_bar_trade_features
from .trades_loader import (
    HOLDOUT_START_MS,
    write_trades_manifest,
)
from .verdict import aggregate_lab_verdict
from .verdict_trades import evaluate_trade_flow, matches_or_beats

HARNESS_ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = HARNESS_ROOT / "out"
CACHE_DIR = HARNESS_ROOT / "cache" / "trades_001"
ARCHIVE_TESTS = Path("/workspace/lab/archive/tests")
ARCHIVE_AUDIT = Path("/workspace/lab/archive/audit")

EDGE_ID = "EDGE-20260911-001"
TEST_ID = "TEST-20260911-001"
CEM = ["CEM-20260910-001", "CEM-20260910-002", "CEM-20260910-003"]
CEM_STR = ";".join(CEM)

# Primary LOCKED
PRIMARY = dict(
    W_trade_ms=60_000,
    L=288,
    Q_star=0.80,
    N_min=20,
    delta_exec_ms=500,
    h_bars=1,
)

GATES = {
    "research_signals": 200,
    "research_distinct_utc_days": 20,
    "validation_signals": 50,
    "concentration_kill_frac": 0.05,
}

RESEARCH_OPEN_FIRST = pd.Timestamp("2021-01-03T04:00:00Z")
RESEARCH_OPEN_LAST = pd.Timestamp("2024-05-27T06:15:00Z")
VALIDATION_OPEN_FIRST = pd.Timestamp("2024-05-27T06:20:00Z")
VALIDATION_OPEN_LAST = pd.Timestamp("2025-07-14T15:00:00Z")


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--trades",
        default="/workspace/lab/data/DATA-PROV-TRADES-001",
    )
    p.add_argument(
        "--ohlcv",
        default="/workspace/lab/data/DATA-PROV-001",
    )
    p.add_argument("--out", default=str(OUT_DIR))
    p.add_argument("--force-rebuild-cache", action="store_true")
    p.add_argument("--max-days", type=int, default=None, help="Scope cut [A]")
    p.add_argument("--symbols", default="BTCUSDT,ETHUSDT")
    return p.parse_args(argv)


def _slice_mask(df: pd.DataFrame, which: str) -> pd.Series:
    ot = pd.to_datetime(df["open_time_ms"], unit="ms", utc=True)
    if which == "research":
        return (ot >= RESEARCH_OPEN_FIRST) & (ot <= RESEARCH_OPEN_LAST)
    if which == "validation":
        return (ot >= VALIDATION_OPEN_FIRST) & (ot <= VALIDATION_OPEN_LAST)
    raise ValueError(which)


def _signal_stats(df: pd.DataFrame, C: float) -> dict[str, Any]:
    sig = df.loc[df["signal"] & df["gross_bps"].notna()]
    n = int(len(sig))
    days = distinct_signal_days(df.assign(timestamp=df["timestamp"]), "signal")
    gross = sig["gross_bps"].to_numpy(dtype=float) if n else np.array([])
    mu = mean_or_none(gross)
    hit = float(np.mean(gross > 0)) if n else None
    mu_nw, se = newey_west_mean_se(gross, lag=1) if n else (None, None)
    z = 1.959963984540054
    ci_lo = (mu_nw - z * se) if (mu_nw is not None and se is not None) else None
    ci_hi = (mu_nw + z * se) if (mu_nw is not None and se is not None) else None
    conc = concentration_frac(df.assign(timestamp=df["timestamp"]), "signal")
    return {
        "signal_count": n,
        "distinct_utc_days": days,
        "mean_gross_bps": mu,
        "mean_net_1x": (mu - C) if mu is not None else None,
        "mean_net_2x": (mu - 2 * C) if mu is not None else None,
        "mean_net_3x": (mu - 3 * C) if mu is not None else None,
        "hit_rate": hit,
        "nw_ci_low": ci_lo,
        "nw_ci_high": ci_hi,
        "concentration_day_frac": conc,
    }


def _edge001_kwargs(delta_exec_ms: Optional[int] = None) -> dict:
    return dict(
        L=PRIMARY["L"],
        Q_star=PRIMARY["Q_star"],
        N_min=PRIMARY["N_min"],
        delta_exec_ms=PRIMARY["delta_exec_ms"] if delta_exec_ms is None else delta_exec_ms,
        h_bars=PRIMARY["h_bars"],
    )


def evaluate_symbol(
    symbol: str,
    bar_path: Path,
    *,
    delta_exec_ms: int = 500,
) -> dict[str, Any]:
    C = DEFAULT_COSTS.C_base
    flow = pd.read_parquet(bar_path)
    # Guard holdout
    flow = flow.loc[flow["open_time_ms"] < HOLDOUT_START_MS].reset_index(drop=True)

    primary = build_edge001_frame(flow, **_edge001_kwargs(delta_exec_ms))
    placebo = build_edge001_frame(flow, **_edge001_kwargs(delta_exec_ms), use_scrambled=True)
    # OHLCV nested uses primary frame columns
    nested = ohlcv_only_nested_signal(
        primary,
        L=PRIMARY["L"],
        Q_star=PRIMARY["Q_star"],
        delta_exec_ms=delta_exec_ms,
        h_bars=PRIMARY["h_bars"],
    )

    research = primary.loc[_slice_mask(primary, "research")].copy()
    research_p = placebo.loc[_slice_mask(placebo, "research")].copy()
    research_n = nested.loc[_slice_mask(nested, "research")].copy()

    stats = _signal_stats(research, C)
    stats_p = _signal_stats(research_p, C)
    stats_n = _signal_stats(research_n, C)

    placebo_beats = matches_or_beats(
        stats["mean_gross_bps"],
        stats_p["mean_gross_bps"],
        stats["nw_ci_low"],
        stats["nw_ci_high"],
    )
    ohlcv_redundant = matches_or_beats(
        stats["mean_gross_bps"],
        stats_n["mean_gross_bps"],
        stats["nw_ci_low"],
        stats["nw_ci_high"],
    )

    # Δ_exec sensitivity (robustness only)
    delta_sens = {}
    for d_ms in (100, 500, 1000, 5000):
        fr = build_edge001_frame(flow, **_edge001_kwargs(d_ms))
        rs = fr.loc[_slice_mask(fr, "research")].copy()
        delta_sens[str(d_ms)] = _signal_stats(rs, C)

    verdict = evaluate_trade_flow(
        instrument=symbol.replace("USDT", ""),
        signal_count=stats["signal_count"],
        distinct_utc_days=stats["distinct_utc_days"],
        mean_gross_bps=stats["mean_gross_bps"],
        net_1x=stats["mean_net_1x"],
        net_2x=stats["mean_net_2x"],
        net_3x=stats["mean_net_3x"],
        concentration_frac=stats["concentration_day_frac"],
        ohlcv_redundant=ohlcv_redundant,
        placebo_beats=placebo_beats,
        gates=GATES,
        cemetery=CEM,
    )

    result: dict[str, Any] = {
        "symbol": symbol,
        "research": stats,
        "placebo_scrambled_aggressor": stats_p,
        "ohlcv_nested": stats_n,
        "placebo_beats": placebo_beats,
        "ohlcv_redundant": ohlcv_redundant,
        "delta_exec_sensitivity": delta_sens,
        "verdict": verdict.verdict,
        "reasons": verdict.reasons,
        "validation": None,
        "validation_ran": False,
    }

    # VALIDATION only if RESEARCH not FAIL*
    if not str(verdict.verdict).startswith("FAIL"):
        val = primary.loc[_slice_mask(primary, "validation")].copy()
        vstats = _signal_stats(val, C)
        result["validation"] = vstats
        result["validation_ran"] = True
        # Re-evaluate with validation
        verdict2 = evaluate_trade_flow(
            instrument=symbol.replace("USDT", ""),
            signal_count=stats["signal_count"],
            distinct_utc_days=stats["distinct_utc_days"],
            mean_gross_bps=stats["mean_gross_bps"],
            net_1x=stats["mean_net_1x"],
            net_2x=stats["mean_net_2x"],
            net_3x=stats["mean_net_3x"],
            concentration_frac=stats["concentration_day_frac"],
            ohlcv_redundant=ohlcv_redundant,
            placebo_beats=placebo_beats,
            gates=GATES,
            validation_reached=vstats["signal_count"] >= GATES["validation_signals"],
            validation_net_1x=vstats["mean_net_1x"],
            cemetery=CEM,
        )
        result["verdict"] = verdict2.verdict
        result["reasons"] = verdict2.reasons

    return result


def write_artifacts(out_dir: Path, record: dict[str, Any]) -> tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / f"{TEST_ID}-{EDGE_ID}.json"
    md_path = out_dir / f"{TEST_ID}-{EDGE_ID}.md"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2, default=str)
        f.write("\n")

    lines = [
        f"# TEST record — {EDGE_ID}",
        "",
        f"**TEST_ID:** `{TEST_ID}`",
        f"**MEASUREMENT / verdict:** `{record.get('verdict')}`",
        f"**Holdout:** `SEALED` (holdout_sealed=true)",
        f"**invented_numbers:** False",
        f"**Δ_exec primary:** `{PRIMARY['delta_exec_ms']}ms`",
        f"**Cemetery citations:** {CEM_STR}",
        f"**VALIDATION ran:** {record.get('validation_ran')}",
        f"**L2 proxies:** false",
        "",
        "## Kill / verdict reasons",
    ]
    for iv in record.get("instruments", []):
        lines.append(f"### {iv.get('symbol')}: `{iv.get('verdict')}`")
        for r in iv.get("reasons", []):
            lines.append(f"- {r}")
        lines.append("")
        res = iv.get("research") or {}
        lines.append("#### RESEARCH primary")
        lines.append(f"- signals: {res.get('signal_count')}")
        lines.append(f"- distinct UTC days: {res.get('distinct_utc_days')}")
        lines.append(f"- mean gross bps: {res.get('mean_gross_bps')}")
        lines.append(f"- net@1×: {res.get('mean_net_1x')}")
        lines.append(f"- net@2×: {res.get('mean_net_2x')}")
        lines.append(f"- net@3×: {res.get('mean_net_3x')}")
        lines.append(f"- hit rate: {res.get('hit_rate')}")
        lines.append(
            f"- OHLCV nested gross: {(iv.get('ohlcv_nested') or {}).get('mean_gross_bps')} "
            f"(redundant={iv.get('ohlcv_redundant')})"
        )
        lines.append(
            f"- Scrambled-aggressor placebo gross: "
            f"{(iv.get('placebo_scrambled_aggressor') or {}).get('mean_gross_bps')} "
            f"(beats={iv.get('placebo_beats')})"
        )
        if iv.get("validation"):
            v = iv["validation"]
            lines.append("#### VALIDATION")
            lines.append(f"- signals: {v.get('signal_count')}")
            lines.append(f"- mean gross bps: {v.get('mean_gross_bps')}")
            lines.append(f"- net@1×: {v.get('mean_net_1x')}")
        lines.append("")
        lines.append("#### Δ_exec sensitivity (robustness)")
        lines.append("```json")
        lines.append(json.dumps(iv.get("delta_exec_sensitivity"), indent=2, default=str))
        lines.append("```")
        lines.append("")

    lines.extend(
        [
            "## Primary cell (LOCKED)",
            "```json",
            json.dumps(PRIMARY, indent=2),
            "```",
            "",
            "## Assumptions [A]",
            "- C_base = 7.0 bps RT (fees4+spread2+slip1)",
            "- Forward return: entry = next-bar open after decision close_time; "
            "exit = open of entry_idx + h_bars (Δ_exec > 0 enforced)",
            "- range_t = (high-low)/close; residual = trailing-L OLS of IMB on controls",
            "- Feature cache under cache/trades_001 derived [A]",
            "",
            "## Non-claims",
            "- Not a rescue of CEM-001/002/003 OHLCV edges",
            "- No L2 depth/spread proxy",
            "- Holdout sealed; sealed OHLCV never opened",
            "- Provisional economics ≠ venue truth",
        ]
    )
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return json_path, md_path


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(argv)
    trades_root = Path(args.trades)
    ohlcv_root = Path(args.ohlcv)
    out_dir = Path(args.out)
    write_trades_manifest(trades_root, clock_verdict="CONDITIONAL")

    raw_root = trades_root / "raw"
    symbols = [s.strip() for s in args.symbols.split(",") if s.strip()]
    instrument_results = []
    validation_any = False

    for sym in symbols:
        print(f"=== Building cache {sym} ===", flush=True)
        bar_path = build_bar_trade_features(
            symbol=sym,
            trades_raw_root=raw_root,
            ohlcv_root=ohlcv_root,
            cache_dir=CACHE_DIR,
            w_trade_ms=PRIMARY["W_trade_ms"],
            force_rebuild=args.force_rebuild_cache,
            max_days=args.max_days,
        )
        print(f"=== Evaluating {sym} ===", flush=True)
        res = evaluate_symbol(sym, bar_path, delta_exec_ms=PRIMARY["delta_exec_ms"])
        instrument_results.append(res)
        validation_any = validation_any or bool(res.get("validation_ran"))

    ivs = [
        type("IV", (), {"verdict": r["verdict"]})()  # noqa simple
        for r in instrument_results
    ]
    # aggregate manually
    order = {
        "FAIL": 0,
        "FAIL-INSUFFICIENT": 1,
        "WEAK": 2,
        "PROMISING": 3,
        "VALIDATION_PASS": 4,
        "UNTESTED": 5,
    }
    headline = min(
        (r["verdict"] for r in instrument_results),
        key=lambda v: order.get(v, 99),
    )

    record = {
        "TEST_ID": TEST_ID,
        "edge_id": EDGE_ID,
        "package_id": "PROV-MEAS-EDGE-20260911-001",
        "MEASUREMENT": headline,
        "verdict": headline,
        "holdout": "SEALED",
        "holdout_sealed": True,
        "invented_numbers": False,
        "delta_exec_ms": PRIMARY["delta_exec_ms"],
        "C_base_bps": DEFAULT_COSTS.C_base,
        "C_base_tag": "[A]",
        "cemetery_citations": CEM,
        "cemetery_citation": CEM_STR,
        "validation_ran": validation_any,
        "l2_proxy": False,
        "primary_cell": PRIMARY,
        "forward_return_assumption_[A]": (
            "entry=next_bar_open after decision close_time; "
            "exit=open[entry_idx+h]; Δ_exec>0 mandatory"
        ),
        "instruments": instrument_results,
        "stress_schedule": stress_schedule(DEFAULT_COSTS.C_base),
        "data_trades": str(trades_root),
        "data_ohlcv": str(ohlcv_root),
        "scope_cut_max_days": args.max_days,
    }
    json_path, md_path = write_artifacts(out_dir, record)

    ARCHIVE_TESTS.mkdir(parents=True, exist_ok=True)
    ARCHIVE_AUDIT.mkdir(parents=True, exist_ok=True)
    shutil.copy2(json_path, ARCHIVE_TESTS / json_path.name)
    shutil.copy2(md_path, ARCHIVE_TESTS / md_path.name)
    # stable aliases
    shutil.copy2(json_path, ARCHIVE_TESTS / f"{TEST_ID}.json")
    shutil.copy2(md_path, ARCHIVE_TESTS / f"{TEST_ID}.md")
    audit = ARCHIVE_AUDIT / "2026-09-11-TEST-20260911-001-EDGE-001-examiner.md"
    audit.write_text(
        f"# Audit pointer — {TEST_ID}\n\n"
        f"- Edge: {EDGE_ID}\n"
        f"- Verdict: {headline}\n"
        f"- Artifacts: `{json_path}` ; `{md_path}`\n"
        f"- Archive: `{ARCHIVE_TESTS / json_path.name}`\n"
        f"- Holdout sealed: true; invented_numbers: false; L2 proxy: false\n"
        f"- Cemetery: {CEM_STR}\n",
        encoding="utf-8",
    )
    print(f"Wrote {json_path} verdict={headline}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
