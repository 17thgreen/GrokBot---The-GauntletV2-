"""Run EDGE-20260911-002 RESEARCH (+ VALIDATION if not FAIL). TEST-20260911-002."""

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
from .signal_edge_20260911_001 import ohlcv_only_nested_signal
from .signal_edge_20260911_002 import build_edge002_frame
from .trades_features import build_bar_trade_features
from .trades_loader import HOLDOUT_START_MS, write_trades_manifest
from .verdict_trades import evaluate_trade_flow, matches_or_beats

HARNESS_ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = HARNESS_ROOT / "out"
CACHE_DIR = HARNESS_ROOT / "cache" / "trades_001"
ARCHIVE_TESTS = Path("/workspace/lab/archive/tests")
ARCHIVE_AUDIT = Path("/workspace/lab/archive/audit")

EDGE_ID = "EDGE-20260911-002"
TEST_ID = "TEST-20260911-002"
CEM = ["CEM-20260910-001", "CEM-20260910-002", "CEM-20260910-003"]
CEM_STR = ";".join(CEM)

PRIMARY = dict(
    p=0.95,
    W_ms=60_000,
    K=3,
    C_star=0.50,
    P_star=0.67,
    V_min=0.0,
    L_size=2000,
    L=288,
    alpha=0.50,
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
    p.add_argument("--trades", default="/workspace/lab/data/DATA-PROV-TRADES-001")
    p.add_argument("--ohlcv", default="/workspace/lab/data/DATA-PROV-001")
    p.add_argument("--out", default=str(OUT_DIR))
    p.add_argument("--force-rebuild-cache", action="store_true")
    p.add_argument("--max-days", type=int, default=None)
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


def evaluate_symbol(symbol: str, bar_path: Path) -> dict[str, Any]:
    C = DEFAULT_COSTS.C_base
    flow = pd.read_parquet(bar_path)
    flow = flow.loc[flow["open_time_ms"] < HOLDOUT_START_MS].reset_index(drop=True)

    kw = dict(
        C_star=PRIMARY["C_star"],
        P_star=PRIMARY["P_star"],
        V_min=PRIMARY["V_min"],
        alpha_single=PRIMARY["alpha"],
        delta_exec_ms=PRIMARY["delta_exec_ms"],
        h_bars=PRIMARY["h_bars"],
    )
    primary = build_edge002_frame(flow, mode="primary", **kw)
    scramble = build_edge002_frame(flow, mode="scramble_sides", **kw)
    size_shuf = build_edge002_frame(flow, mode="size_shuffle", **kw)
    kill_pers = build_edge002_frame(flow, mode="kill_pers", **kw)
    nested = ohlcv_only_nested_signal(
        primary,
        L=PRIMARY["L"],
        Q_star=0.80,
        delta_exec_ms=PRIMARY["delta_exec_ms"],
        h_bars=PRIMARY["h_bars"],
    )

    research = primary.loc[_slice_mask(primary, "research")].copy()
    stats = _signal_stats(research, C)
    stats_scr = _signal_stats(scramble.loc[_slice_mask(scramble, "research")], C)
    stats_sz = _signal_stats(size_shuf.loc[_slice_mask(size_shuf, "research")], C)
    stats_kp = _signal_stats(kill_pers.loc[_slice_mask(kill_pers, "research")], C)
    stats_n = _signal_stats(nested.loc[_slice_mask(nested, "research")], C)

    # Placebo beats if ANY of the placebos matches/beats
    p1 = matches_or_beats(
        stats["mean_gross_bps"], stats_scr["mean_gross_bps"], stats["nw_ci_low"], stats["nw_ci_high"]
    )
    p2 = matches_or_beats(
        stats["mean_gross_bps"], stats_sz["mean_gross_bps"], stats["nw_ci_low"], stats["nw_ci_high"]
    )
    # kill PERS / single-spike matches full signal → falsify
    p3 = matches_or_beats(
        stats["mean_gross_bps"], stats_kp["mean_gross_bps"], stats["nw_ci_low"], stats["nw_ci_high"]
    )
    placebo_beats = bool(p1 or p2 or p3) if None not in (p1, p2, p3) else (True if any(x is True for x in (p1, p2, p3)) else None)
    # If some placebos lack signals, treat missing as not beating
    flags = [x for x in (p1, p2, p3) if x is not None]
    placebo_beats = any(flags) if flags else None

    ohlcv_redundant = matches_or_beats(
        stats["mean_gross_bps"],
        stats_n["mean_gross_bps"],
        stats["nw_ci_low"],
        stats["nw_ci_high"],
    )

    extra = []
    if p3 is True:
        extra.append("single-spike / kill-PERS matches or beats full signal")

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
        extra_fail_reasons=extra if p3 is True else None,
        cemetery=CEM,
    )

    result: dict[str, Any] = {
        "symbol": symbol,
        "research": stats,
        "placebo_scramble_sides": stats_scr,
        "placebo_size_shuffle": stats_sz,
        "placebo_kill_pers": stats_kp,
        "ohlcv_nested": stats_n,
        "placebo_beats": placebo_beats,
        "ohlcv_redundant": ohlcv_redundant,
        "verdict": verdict.verdict,
        "reasons": verdict.reasons,
        "validation": None,
        "validation_ran": False,
        "not_L2_005_006": True,
    }

    if not str(verdict.verdict).startswith("FAIL"):
        val = primary.loc[_slice_mask(primary, "validation")].copy()
        vstats = _signal_stats(val, C)
        result["validation"] = vstats
        result["validation_ran"] = True
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
            extra_fail_reasons=extra if p3 is True else None,
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
        f"**L2 proxies / EDGE-005/006 rewrite:** false",
        "",
        "## Kill / verdict reasons",
    ]
    for iv in record.get("instruments", []):
        lines.append(f"### {iv.get('symbol')}: `{iv.get('verdict')}`")
        for r in iv.get("reasons", []):
            lines.append(f"- {r}")
        res = iv.get("research") or {}
        lines.append("#### RESEARCH primary")
        lines.append(f"- signals: {res.get('signal_count')}")
        lines.append(f"- distinct UTC days: {res.get('distinct_utc_days')}")
        lines.append(f"- mean gross bps: {res.get('mean_gross_bps')}")
        lines.append(f"- net@1×: {res.get('mean_net_1x')}")
        lines.append(f"- net@2×: {res.get('mean_net_2x')}")
        lines.append(f"- net@3×: {res.get('mean_net_3x')}")
        lines.append(
            f"- OHLCV nested gross: {(iv.get('ohlcv_nested') or {}).get('mean_gross_bps')} "
            f"(redundant={iv.get('ohlcv_redundant')})"
        )
        lines.append(
            f"- scramble sides gross: {(iv.get('placebo_scramble_sides') or {}).get('mean_gross_bps')}"
        )
        lines.append(
            f"- size shuffle gross: {(iv.get('placebo_size_shuffle') or {}).get('mean_gross_bps')}"
        )
        lines.append(
            f"- kill PERS gross: {(iv.get('placebo_kill_pers') or {}).get('mean_gross_bps')}"
        )
        if iv.get("validation"):
            v = iv["validation"]
            lines.append("#### VALIDATION")
            lines.append(f"- signals: {v.get('signal_count')}")
            lines.append(f"- mean gross: {v.get('mean_gross_bps')}")
            lines.append(f"- net@1×: {v.get('mean_net_1x')}")
        lines.append("")
    lines += [
        "## Primary cell (LOCKED)",
        "```json",
        json.dumps(PRIMARY, indent=2),
        "```",
        "",
        "## Non-claims",
        "- Not L2 EDGE-005/006 rewrite",
        "- Not rescue of CEM-001/002/003",
        "- Holdout sealed; invented_numbers=false",
    ]
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
        print(f"=== Cache {sym} ===", flush=True)
        bar_path = build_bar_trade_features(
            symbol=sym,
            trades_raw_root=raw_root,
            ohlcv_root=ohlcv_root,
            cache_dir=CACHE_DIR,
            w_trade_ms=PRIMARY["W_ms"],
            l_size=PRIMARY["L_size"],
            k_sub=PRIMARY["K"],
            p_size=PRIMARY["p"],
            force_rebuild=args.force_rebuild_cache,
            max_days=args.max_days,
        )
        print(f"=== Eval {sym} ===", flush=True)
        res = evaluate_symbol(sym, bar_path)
        instrument_results.append(res)
        validation_any = validation_any or bool(res.get("validation_ran"))

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
        "package_id": "PROV-MEAS-EDGE-20260911-002",
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
        "not_rewrite_of_EDGE_005_006": True,
        "primary_cell": PRIMARY,
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
    shutil.copy2(json_path, ARCHIVE_TESTS / f"{TEST_ID}.json")
    shutil.copy2(md_path, ARCHIVE_TESTS / f"{TEST_ID}.md")
    audit = ARCHIVE_AUDIT / "2026-09-11-TEST-20260911-002-EDGE-002-examiner.md"
    audit.write_text(
        f"# Audit pointer — {TEST_ID}\n\n"
        f"- Edge: {EDGE_ID}\n- Verdict: {headline}\n"
        f"- Artifacts: `{json_path}` ; `{md_path}`\n"
        f"- Holdout sealed: true; L2 proxy: false; not EDGE-005/006\n"
        f"- Cemetery: {CEM_STR}\n",
        encoding="utf-8",
    )
    print(f"Wrote {json_path} verdict={headline}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
