"""Run EDGE-20260911-004 CAT_OI_SHOCK_C5 RESEARCH (+ VALIDATION if not FAIL).

TEST-20260911-004. Holdout LOCKED. Joint OI RESEARCH window.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any, Optional

from .catalyst_common import (
    CEM_CATALYST,
    OI_RESEARCH_FIRST,
    OI_RESEARCH_LAST,
    load_ohlcv_open_slices,
    maybe_load_bar_flow,
    signal_stats,
    slice_mask,
)
from .costs import DEFAULT_COSTS, stress_schedule
from .oi_loader import load_oi_symbol, resolve_oi_clock, write_oi_manifest
from .signal_edge_20260911_004 import build_edge004_frame, ohlcv_nested_vol_div
from .signal_edge_20260911_005 import trade_flow_nested_from_flow
from .verdict_catalyst import CatalystVerdict, aggregate_btc_eth, evaluate_catalyst, matches_or_beats

HARNESS_ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = HARNESS_ROOT / "out"
CACHE_OI = HARNESS_ROOT / "cache" / "oi_001"
CACHE_TRADES = HARNESS_ROOT / "cache" / "trades_001"
ARCHIVE_TESTS = Path("/workspace/lab/archive/tests")
ARCHIVE_AUDIT = Path("/workspace/lab/archive/audit")

EDGE_ID = "EDGE-20260911-004"
TEST_ID = "TEST-20260911-004"
CEM = CEM_CATALYST
PRIMARY = dict(Z=2.5, L_oi=288, Q_lo=0.33, T_wait=2, h_bars=2, delta_exec_bars=1)
GATES = {
    "research_signals": 30,
    "research_distinct_utc_days": 10,
    "validation_signals": 15,
    "concentration_kill_frac": 0.05,
}


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--oi", default="/workspace/lab/data/DATA-PROV-OI-001")
    p.add_argument("--ohlcv", default="/workspace/lab/data/DATA-PROV-001")
    p.add_argument("--out", default=str(OUT_DIR))
    p.add_argument("--force-rebuild-cache", action="store_true")
    p.add_argument("--symbols", default="BTCUSDT,ETHUSDT")
    return p.parse_args(argv)


def evaluate_symbol(symbol: str, args: argparse.Namespace) -> dict[str, Any]:
    C = DEFAULT_COSTS.C_base
    oi = load_oi_symbol(
        Path(args.oi),
        symbol,
        cache_dir=CACHE_OI,
        force_rebuild=args.force_rebuild_cache,
        drop_holdout=True,
    )
    ohlcv = load_ohlcv_open_slices(Path(args.ohlcv), symbol, include_validation=True)

    primary = build_edge004_frame(ohlcv, oi, **PRIMARY, divergence=True)
    large_r = build_edge004_frame(ohlcv, oi, **PRIMARY, divergence=False)
    nested = ohlcv_nested_vol_div(primary, L=PRIMARY["L_oi"], Q_lo=PRIMARY["Q_lo"], T_wait=PRIMARY["T_wait"], h_bars=2)

    flow = maybe_load_bar_flow(CACHE_TRADES, symbol)
    tf_stats = None
    tf_beats = None
    if flow is not None:
        tf = trade_flow_nested_from_flow(primary, flow, h_bars=2, delta_exec_bars=1)
        tf_research = tf.loc[slice_mask(tf, "research", research_first=OI_RESEARCH_FIRST, research_last=OI_RESEARCH_LAST)]
        tf_stats = signal_stats(tf_research, C)

    research = primary.loc[slice_mask(primary, "research", research_first=OI_RESEARCH_FIRST, research_last=OI_RESEARCH_LAST)]
    research_lr = large_r.loc[slice_mask(large_r, "research", research_first=OI_RESEARCH_FIRST, research_last=OI_RESEARCH_LAST)]
    research_n = nested.loc[slice_mask(nested, "research", research_first=OI_RESEARCH_FIRST, research_last=OI_RESEARCH_LAST)]

    stats = signal_stats(research, C)
    stats_lr = signal_stats(research_lr, C)
    stats_n = signal_stats(research_n, C)

    ohlcv_beats = matches_or_beats(stats["mean_gross_bps"], stats_n["mean_gross_bps"], stats["nw_ci_low"], stats["nw_ci_high"])
    large_r_beats = matches_or_beats(stats["mean_gross_bps"], stats_lr["mean_gross_bps"], stats["nw_ci_low"], stats["nw_ci_high"])
    if tf_stats is not None:
        tf_beats = matches_or_beats(stats["mean_gross_bps"], tf_stats["mean_gross_bps"], stats["nw_ci_low"], stats["nw_ci_high"])

    nested_beats = {
        "ohlcv_nested": ohlcv_beats,
        "large_r_cohort_matches_divergence": large_r_beats,
    }
    if tf_beats is not None:
        nested_beats["trade_flow_nested"] = tf_beats

    extra = []
    if large_r_beats is True:
        extra.append("high-|ΔOI| WITH large |r| matches divergence cohort (divergence not load-bearing)")

    rob = {}
    for h_name, hb in (("h5m", 1), ("h15m", 3)):
        fr = build_edge004_frame(ohlcv, oi, Z=2.5, L_oi=288, Q_lo=0.33, T_wait=2, h_bars=hb, delta_exec_bars=1)
        rs = fr.loc[slice_mask(fr, "research", research_first=OI_RESEARCH_FIRST, research_last=OI_RESEARCH_LAST)]
        rob[h_name] = signal_stats(rs, C)

    verdict = evaluate_catalyst(
        instrument=symbol.replace("USDT", ""),
        signal_count=stats["signal_count"],
        distinct_utc_days=stats["distinct_utc_days"],
        mean_gross_bps=stats["mean_gross_bps"],
        net_1x=stats["mean_net_1x"],
        net_2x=stats["mean_net_2x"],
        net_3x=stats["mean_net_3x"],
        concentration_frac=stats["concentration_day_frac"],
        nested_beats=nested_beats,
        extra_fail_reasons=extra or None,
        gates=GATES,
        cemetery=CEM,
    )

    result: dict[str, Any] = {
        "symbol": symbol,
        "research": stats,
        "large_r_cohort": stats_lr,
        "ohlcv_nested": stats_n,
        "trade_flow_nested": tf_stats,
        "robustness_horizons": rob,
        "nested_beats": nested_beats,
        "verdict": verdict.verdict,
        "reasons": verdict.reasons,
        "validation": None,
        "validation_ran": False,
        "trigger_aggression": "sign(r) first bar |r|>5e-05 [A]; trades trigger unused",
        "C_base_tag": "[A]",
    }
    if not str(verdict.verdict).startswith("FAIL"):
        val = primary.loc[slice_mask(primary, "validation", research_first=OI_RESEARCH_FIRST, research_last=OI_RESEARCH_LAST)]
        vstats = signal_stats(val, C)
        result["validation"] = vstats
        result["validation_ran"] = True
        verdict2 = evaluate_catalyst(
            instrument=symbol.replace("USDT", ""),
            signal_count=stats["signal_count"],
            distinct_utc_days=stats["distinct_utc_days"],
            mean_gross_bps=stats["mean_gross_bps"],
            net_1x=stats["mean_net_1x"],
            net_2x=stats["mean_net_2x"],
            net_3x=stats["mean_net_3x"],
            concentration_frac=stats["concentration_day_frac"],
            nested_beats=nested_beats,
            extra_fail_reasons=extra or None,
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
        f"**Primary:** Z=2.5 L_oi=288 Q_lo=0.33 T_wait=2 Δ_exec=1×5m h=10m flush-with-trigger",
        f"**C_base:** 7.0 bps RT [A]",
        f"**Cemetery:** {';'.join(CEM)}",
        f"**VALIDATION ran:** {record.get('validation_ran')}",
        f"**Binary scoreboard:** skipped — futures mechanism only [V]",
        f"**LIQ-003:** not invoked",
        "",
        "## Kill / verdict reasons",
    ]
    for r in record.get("kill_reasons", []):
        lines.append(f"- {r}")
    lines.append("")
    lines.append("## Per-symbol research primary")
    for inst in record.get("instruments", []):
        s = inst.get("research") or {}
        lines.append(
            f"- **{inst.get('symbol')}** verdict=`{inst.get('verdict')}` "
            f"gross={s.get('mean_gross_bps')} net@1×={s.get('mean_net_1x')} "
            f"n={s.get('signal_count')}"
        )
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return json_path, md_path


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(argv)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    clock = resolve_oi_clock(Path(args.oi))
    write_oi_manifest(Path(args.oi), out_dir / "MANIFEST_OI_copy.json")
    if clock not in ("APPROVED", "CONDITIONAL"):
        record = {
            "TEST_ID": TEST_ID,
            "edge_id": EDGE_ID,
            "MEASUREMENT": "UNTESTED",
            "verdict": "UNTESTED",
            "reason": f"OI clock_verdict={clock}",
            "holdout_sealed": True,
            "invented_numbers": False,
        }
        write_artifacts(out_dir, record)
        return 2

    symbols = [s.strip() for s in args.symbols.split(",") if s.strip()]
    instruments = []
    for sym in symbols:
        print(f"[004] evaluating {sym} ...", flush=True)
        instruments.append(evaluate_symbol(sym, args))

    by = {i["symbol"]: i for i in instruments}
    btc_v = CatalystVerdict("BTC", by["BTCUSDT"]["verdict"], by["BTCUSDT"]["reasons"])
    eth_v = CatalystVerdict("ETH", by["ETHUSDT"]["verdict"], by["ETHUSDT"]["reasons"])
    lab_verdict, lab_reasons = aggregate_btc_eth(
        btc_v,
        eth_v,
        btc_gross=(by["BTCUSDT"]["research"] or {}).get("mean_gross_bps"),
        eth_gross=(by["ETHUSDT"]["research"] or {}).get("mean_gross_bps"),
    )
    record = {
        "TEST_ID": TEST_ID,
        "edge_id": EDGE_ID,
        "informal": "CAT_OI_SHOCK_C5",
        "MEASUREMENT": lab_verdict,
        "verdict": lab_verdict,
        "kill_reasons": lab_reasons,
        "instruments": instruments,
        "nested_summary": {s: i.get("nested_beats") for s, i in by.items()},
        "holdout_sealed": True,
        "invented_numbers": False,
        "validation_ran": any(i.get("validation_ran") for i in instruments),
        "C_base_bps": DEFAULT_COSTS.C_base,
        "C_tag": "[A]",
        "cost_stress": stress_schedule(),
        "clock_verdict_oi": clock,
        "splits": {
            "research": [str(OI_RESEARCH_FIRST), str(OI_RESEARCH_LAST)],
            "validation": ["2024-05-27T06:20:00Z", "2025-07-14T15:00:00Z"],
            "holdout": "LOCKED",
        },
        "primary_cell": PRIMARY,
        "cemetery": CEM,
        "binary_scoreboard": "skipped_no_Kalshi_PM_futures_mechanism_only_[V]",
        "LIQ_003_invoked": False,
        "oi_sort_dedupe": True,
        "trigger_aggression": "sign(r) |r|>5e-05 [A]",
    }
    json_path, md_path = write_artifacts(out_dir, record)
    ARCHIVE_TESTS.mkdir(parents=True, exist_ok=True)
    ARCHIVE_AUDIT.mkdir(parents=True, exist_ok=True)
    for src in (json_path, md_path):
        shutil.copy2(src, ARCHIVE_TESTS / src.name)
    (ARCHIVE_AUDIT / f"2026-09-11-{TEST_ID}-{EDGE_ID}-examiner.md").write_text(
        f"# Audit pointer\n\n- TEST: `{TEST_ID}`\n- EDGE: `{EDGE_ID}`\n"
        f"- Verdict: `{lab_verdict}`\n- holdout_sealed: true\n",
        encoding="utf-8",
    )
    (ARCHIVE_TESTS / f"{TEST_ID}.json").write_text(
        json.dumps({"TEST_ID": TEST_ID, "edge_id": EDGE_ID, "verdict": lab_verdict}, indent=2) + "\n"
    )
    (ARCHIVE_TESTS / f"{TEST_ID}.md").write_text(f"# {TEST_ID}\n\nEDGE `{EDGE_ID}` verdict `{lab_verdict}`\n")
    print(f"[004] DONE verdict={lab_verdict} -> {json_path}", flush=True)
    return 0 if not str(lab_verdict).startswith("FAIL") else 1


if __name__ == "__main__":
    sys.exit(main())
