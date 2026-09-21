"""CLI entrypoint for PROV-MEAS-20260910-001 / EDGE-20260910-001.

Usage:
  python -m src.run_edge001 --package PROV-MEAS-20260910-001 \\
      --data /path/to/DATA-PROV-... [--open-holdout]

Without --data or with missing/quarantined data → exit 0, MEASUREMENT=UNTESTED.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any, Optional

import pandas as pd

from . import EDGE_ID, PACKAGE_ID
from .costs import stress_schedule
from .data_loader import SliceBundle, load_data_prov, load_package_config
from .metrics import (
    grid_w_stability,
    placebo_tests,
    qlo_cliff_flag,
    slice_metrics,
    time_half_stability,
)
from .report import write_test_record, write_untested_report
from .signal_edge001 import build_trade_frame
from .splits import (
    WARMUP_BARS,
    assert_holdout_exists,
    bounds_from_presliced,
    compute_split_bounds,
    holdout_is_sealed,
    apply_slice,
)
from .verdict import InstrumentVerdict, aggregate_lab_verdict, evaluate_instrument

HARNESS_ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = HARNESS_ROOT / "config"
OUT_DIR = HARNESS_ROOT / "out"
DEFAULT_CONDUCTOR_ORDER = HARNESS_ROOT / "config" / "CONDUCTOR_OPEN_HOLDOUT.order"


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Examiner harness EDGE-20260910-001")
    p.add_argument("--package", default=PACKAGE_ID, help="Package ID")
    p.add_argument("--data", default=None, help="Path to DATA-PROV-* directory")
    p.add_argument(
        "--open-holdout",
        action="store_true",
        help="Evaluate holdout only if Conductor order file also exists",
    )
    p.add_argument(
        "--conductor-order",
        default=str(DEFAULT_CONDUCTOR_ORDER),
        help="Path to Conductor holdout-open order file",
    )
    p.add_argument("--out", default=str(OUT_DIR), help="Output directory")
    return p.parse_args(argv)


def _epsilon_value(cfg: dict[str, Any], name: str) -> float:
    eps = cfg["parameter_grid"]["epsilon"]
    if name == "small":
        return float(eps["small"])
    if name in ("2x_small", "2×small", "2x"):
        return float(eps["2x_small"])
    raise KeyError(name)


def run_instrument_presliced(
    inst: str,
    bundle: SliceBundle,
    cfg: dict[str, Any],
    *,
    open_holdout: bool,
    conductor_order: Path,
    research_only: bool,
) -> tuple[InstrumentVerdict, dict[str, Any]]:
    """Pipeline using on-disk SEAL_LOCK slices — do not re-split the full series."""
    primary = cfg["primary_cell"]
    grid = cfg["parameter_grid"]
    gates = cfg["min_gates"]
    C_base = float(cfg["costs_bps"]["C_base"])
    costs = stress_schedule(C_base)
    eps_small = _epsilon_value(cfg, "small")
    Q_hi = float(primary.get("Q_hi_default", 0.80))
    seed = int(cfg["stats"]["placebo_seed"])
    warmup_bars = int(cfg.get("warmup_bars", WARMUP_BARS))

    n_warmup = len(bundle.warmup)
    n_research = len(bundle.research)
    n_validation = len(bundle.validation)
    n_holdout_loaded = len(bundle.holdout) if bundle.holdout is not None else 0

    bounds = bounds_from_presliced(
        n_warmup=n_warmup,
        n_research=n_research,
        n_validation=n_validation,
        n_holdout=n_holdout_loaded if bundle.holdout is not None else 0,
    )
    # Assert sealed holdout *file* exists without reading it when not loaded
    try:
        if bundle.holdout_file_present:
            holdout_exists = True
        else:
            assert_holdout_exists(bounds, file_present=False)
            holdout_exists = False
    except AssertionError:
        holdout_exists = bundle.holdout_file_present

    sealed = holdout_is_sealed(open_holdout, conductor_order)

    W = int(primary["W"])
    Q_lo = float(primary["Q_lo"])
    L = int(primary["L"])
    h = int(primary["h"])

    # Research path: WARMUP_PREFIX + RESEARCH for feature continuity
    research_path = pd.concat([bundle.warmup, bundle.research], ignore_index=True)
    frame_r = build_trade_frame(
        research_path, W=W, L=L, Q_lo=Q_lo, h=h, epsilon=eps_small, Q_hi=Q_hi
    )
    # Metrics only on RESEARCH portion (after warmup prefix)
    research_df = frame_r.iloc[n_warmup:].copy()
    mid = n_research // 2
    half1 = research_df.iloc[:mid].copy()
    half2 = research_df.iloc[mid:].copy()

    m_research = slice_metrics(research_df, C=costs["C_1x"], h=h, slice_name="research")
    sig_r = research_df.loc[research_df["signal"] & research_df["gross_bps"].notna()]
    gross_r = sig_r["gross_bps"]
    net_1x = float(gross_r.mean() - costs["C_1x"]) if len(gross_r) else None
    net_2x = float(gross_r.mean() - costs["C_2x"]) if len(gross_r) else None
    net_3x = float(gross_r.mean() - costs["C_3x"]) if len(gross_r) else None

    # Validation: prepend last warmup_bars of research for feature continuity
    # (does not use sealed/; research is permitted on the research path)
    val_prefix = bundle.research.iloc[-warmup_bars:] if n_research >= warmup_bars else bundle.research
    validation_path = pd.concat([val_prefix, bundle.validation], ignore_index=True)
    frame_v = build_trade_frame(
        validation_path, W=W, L=L, Q_lo=Q_lo, h=h, epsilon=eps_small, Q_hi=Q_hi
    )
    validation_df = frame_v.iloc[len(val_prefix) :].copy()
    m_validation = slice_metrics(
        validation_df, C=costs["C_1x"], h=h, slice_name="validation"
    )
    val_sig = validation_df.loc[
        validation_df["signal"] & validation_df["gross_bps"].notna()
    ]
    validation_net_1x = (
        float(val_sig["gross_bps"].mean() - costs["C_1x"]) if len(val_sig) else None
    )

    cost_rows = {}
    for label, C in costs.items():
        sm = slice_metrics(research_df, C=C, h=h, slice_name=f"research_{label}")
        cost_rows[label] = sm.to_dict()

    th = time_half_stability(half1, half2, h=h, C=costs["C_1x"])

    placebos = placebo_tests(research_df, h=h, seed=seed)
    placebo_beats = any(
        bool(v.get("matches_or_beats_real"))
        for v in placebos.get("placebos", {}).values()
        if v.get("matches_or_beats_real") is not None
    )

    gap_by_W: dict[int, Optional[float]] = {}
    gap_by_qlo: dict[float, Optional[float]] = {}
    grid_results = []
    for W_i in grid["W"]:
        for Q_i in grid["Q_lo"]:
            for L_i in grid["L"]:
                for h_i in grid["h"]:
                    for eps_name in ("small", "2x_small"):
                        eps_v = _epsilon_value(cfg, eps_name)
                        fr = build_trade_frame(
                            research_path,
                            W=int(W_i),
                            L=int(L_i),
                            Q_lo=float(Q_i),
                            h=int(h_i),
                            epsilon=eps_v,
                            Q_hi=Q_hi,
                        )
                        rdf = fr.iloc[n_warmup:].copy()
                        sm = slice_metrics(
                            rdf, C=costs["C_1x"], h=int(h_i), slice_name="research"
                        )
                        cell = {
                            "W": W_i,
                            "Q_lo": Q_i,
                            "L": L_i,
                            "h": h_i,
                            "epsilon": eps_name,
                            "metrics": sm.to_dict(),
                            "is_primary": (
                                W_i == W
                                and Q_i == Q_lo
                                and L_i == L
                                and h_i == h
                                and eps_name == "small"
                            ),
                        }
                        grid_results.append(cell)
                        if (
                            Q_i == Q_lo
                            and L_i == L
                            and h_i == h
                            and eps_name == "small"
                        ):
                            gap_by_W[int(W_i)] = sm.low_high_gap_bps
                        if (
                            W_i == W
                            and L_i == L
                            and h_i == h
                            and eps_name == "small"
                        ):
                            gap_by_qlo[float(Q_i)] = sm.low_high_gap_bps

    w_stab = grid_w_stability(gap_by_W)
    cliff = qlo_cliff_flag(gap_by_qlo)

    holdout_metrics = None
    if (
        not sealed
        and holdout_exists
        and not research_only
        and bundle.holdout is not None
    ):
        # Warmup continuity from end of validation (still not inventing splits)
        h_prefix = (
            bundle.validation.iloc[-warmup_bars:]
            if n_validation >= warmup_bars
            else bundle.validation
        )
        holdout_path = pd.concat([h_prefix, bundle.holdout], ignore_index=True)
        frame_h = build_trade_frame(
            holdout_path, W=W, L=L, Q_lo=Q_lo, h=h, epsilon=eps_small, Q_hi=Q_hi
        )
        holdout_df = frame_h.iloc[len(h_prefix) :].copy()
        holdout_metrics = slice_metrics(
            holdout_df, C=costs["C_1x"], h=h, slice_name="holdout"
        ).to_dict()

    iv = evaluate_instrument(
        instrument=inst,
        research=m_research.to_dict(),
        validation=m_validation.to_dict(),
        gates=gates,
        grid_w_pass=bool(w_stab["pass"]),
        qlo_cliff=cliff,
        placebo_beats=placebo_beats,
        concentration_frac=m_research.concentration_day_frac,
        net_1x=net_1x,
        net_2x=net_2x,
        net_3x=net_3x,
        gap_ci_excludes_zero_research=m_research.gap_ci_excludes_zero,
        validation_net_1x=validation_net_1x,
        validation_gap_ci_excludes_zero=m_validation.gap_ci_excludes_zero,
        validation_signal_count=m_validation.signal_count,
        research_only=research_only,
    )

    summary = {
        "instrument": inst,
        "n_bars": n_warmup + n_research + n_validation + n_holdout_loaded,
        "pre_sliced": True,
        "splits": {
            "warmup_end": bounds.warmup_end,
            "research": [bounds.research_start, bounds.research_end],
            "validation": [bounds.validation_start, bounds.validation_end],
            "holdout": [bounds.holdout_start, bounds.holdout_end],
            "holdout_sealed": sealed,
            "holdout_exists": holdout_exists,
            "holdout_loaded": bundle.holdout is not None,
            "source": "SEAL_LOCK_slices",
            "n_warmup": n_warmup,
            "n_research": n_research,
            "n_validation": n_validation,
        },
        "primary_cell": {
            "W": W,
            "Q_lo": Q_lo,
            "L": L,
            "h": h,
            "epsilon": "small",
            "epsilon_value_[A]": eps_small,
        },
        "research": m_research.to_dict(),
        "validation": m_validation.to_dict(),
        "holdout": holdout_metrics,
        "cost_stress_[A]": cost_rows,
        "time_half": th,
        "placebos": placebos,
        "grid_w_stability": w_stab,
        "qlo_cliff": cliff,
        "grid_cell_count": len(grid_results),
        "grid_results": grid_results,
        "C_base_[A]": C_base,
    }
    return iv, summary


def run_instrument(
    inst: str,
    df,
    cfg: dict[str, Any],
    *,
    open_holdout: bool,
    conductor_order: Path,
    research_only: bool,
) -> tuple[InstrumentVerdict, dict[str, Any]]:
    """Full pipeline for one instrument (contiguous series). Metrics from code only."""
    primary = cfg["primary_cell"]
    grid = cfg["parameter_grid"]
    gates = cfg["min_gates"]
    C_base = float(cfg["costs_bps"]["C_base"])
    costs = stress_schedule(C_base)
    eps_small = _epsilon_value(cfg, "small")
    Q_hi = float(primary.get("Q_hi_default", 0.80))
    seed = int(cfg["stats"]["placebo_seed"])

    n = len(df)
    bounds = compute_split_bounds(
        n,
        warmup=int(cfg.get("warmup_bars", WARMUP_BARS)),
        research_frac=float(cfg["splits"]["research_frac"]),
        validation_frac=float(cfg["splits"]["validation_frac"]),
        holdout_frac=float(cfg["splits"]["holdout_frac"]),
    )
    try:
        assert_holdout_exists(bounds)
        holdout_exists = True
    except AssertionError:
        holdout_exists = False

    sealed = holdout_is_sealed(open_holdout, conductor_order)

    # Primary cell frame
    W = int(primary["W"])
    Q_lo = float(primary["Q_lo"])
    L = int(primary["L"])
    h = int(primary["h"])
    frame = build_trade_frame(df, W=W, L=L, Q_lo=Q_lo, h=h, epsilon=eps_small, Q_hi=Q_hi)

    research_df = apply_slice(frame, bounds, "research")
    validation_df = apply_slice(frame, bounds, "validation")
    half1 = apply_slice(frame, bounds, "research_half1")
    half2 = apply_slice(frame, bounds, "research_half2")

    m_research = slice_metrics(research_df, C=costs["C_1x"], h=h, slice_name="research")
    # nets at stress
    sig_r = research_df.loc[research_df["signal"] & research_df["gross_bps"].notna()]
    gross_r = sig_r["gross_bps"]
    net_1x = float(gross_r.mean() - costs["C_1x"]) if len(gross_r) else None
    net_2x = float(gross_r.mean() - costs["C_2x"]) if len(gross_r) else None
    net_3x = float(gross_r.mean() - costs["C_3x"]) if len(gross_r) else None

    m_validation = slice_metrics(
        validation_df, C=costs["C_1x"], h=h, slice_name="validation"
    )
    val_sig = validation_df.loc[
        validation_df["signal"] & validation_df["gross_bps"].notna()
    ]
    validation_net_1x = (
        float(val_sig["gross_bps"].mean() - costs["C_1x"]) if len(val_sig) else None
    )

    # Cost stress rows (reported)
    cost_rows = {}
    for label, C in costs.items():
        sm = slice_metrics(research_df, C=C, h=h, slice_name=f"research_{label}")
        cost_rows[label] = sm.to_dict()

    # Time-half
    th = time_half_stability(half1, half2, h=h, C=costs["C_1x"])

    # Placebos on RESEARCH
    placebos = placebo_tests(research_df, h=h, seed=seed)
    placebo_beats = any(
        bool(v.get("matches_or_beats_real"))
        for v in placebos.get("placebos", {}).values()
        if v.get("matches_or_beats_real") is not None
    )

    # Parameter grid — all cells; headline stays primary
    gap_by_W: dict[int, Optional[float]] = {}
    gap_by_qlo: dict[float, Optional[float]] = {}
    grid_results = []
    for W_i in grid["W"]:
        for Q_i in grid["Q_lo"]:
            for L_i in grid["L"]:
                for h_i in grid["h"]:
                    for eps_name in ("small", "2x_small"):
                        eps_v = _epsilon_value(cfg, eps_name)
                        fr = build_trade_frame(
                            df,
                            W=int(W_i),
                            L=int(L_i),
                            Q_lo=float(Q_i),
                            h=int(h_i),
                            epsilon=eps_v,
                            Q_hi=Q_hi,
                        )
                        rdf = apply_slice(fr, bounds, "research")
                        sm = slice_metrics(
                            rdf, C=costs["C_1x"], h=int(h_i), slice_name="research"
                        )
                        cell = {
                            "W": W_i,
                            "Q_lo": Q_i,
                            "L": L_i,
                            "h": h_i,
                            "epsilon": eps_name,
                            "metrics": sm.to_dict(),
                            "is_primary": (
                                W_i == W
                                and Q_i == Q_lo
                                and L_i == L
                                and h_i == h
                                and eps_name == "small"
                            ),
                        }
                        grid_results.append(cell)
                        # W stability at primary-like Q_lo,L,h,eps
                        if (
                            Q_i == Q_lo
                            and L_i == L
                            and h_i == h
                            and eps_name == "small"
                        ):
                            gap_by_W[int(W_i)] = sm.low_high_gap_bps
                        if (
                            W_i == W
                            and L_i == L
                            and h_i == h
                            and eps_name == "small"
                        ):
                            gap_by_qlo[float(Q_i)] = sm.low_high_gap_bps

    w_stab = grid_w_stability(gap_by_W)
    cliff = qlo_cliff_flag(gap_by_qlo)

    # Holdout: sealed by default
    holdout_metrics = None
    if not sealed and holdout_exists and not research_only:
        holdout_df = apply_slice(frame, bounds, "holdout")
        holdout_metrics = slice_metrics(
            holdout_df, C=costs["C_1x"], h=h, slice_name="holdout"
        ).to_dict()

    iv = evaluate_instrument(
        instrument=inst,
        research=m_research.to_dict(),
        validation=m_validation.to_dict(),
        gates=gates,
        grid_w_pass=bool(w_stab["pass"]),
        qlo_cliff=cliff,
        placebo_beats=placebo_beats,
        concentration_frac=m_research.concentration_day_frac,
        net_1x=net_1x,
        net_2x=net_2x,
        net_3x=net_3x,
        gap_ci_excludes_zero_research=m_research.gap_ci_excludes_zero,
        validation_net_1x=validation_net_1x,
        validation_gap_ci_excludes_zero=m_validation.gap_ci_excludes_zero,
        validation_signal_count=m_validation.signal_count,
        research_only=research_only,
    )

    summary = {
        "instrument": inst,
        "n_bars": n,
        "pre_sliced": False,
        "splits": {
            "warmup_end": bounds.warmup_end,
            "research": [bounds.research_start, bounds.research_end],
            "validation": [bounds.validation_start, bounds.validation_end],
            "holdout": [bounds.holdout_start, bounds.holdout_end],
            "holdout_sealed": sealed,
            "holdout_exists": holdout_exists,
        },
        "primary_cell": {
            "W": W,
            "Q_lo": Q_lo,
            "L": L,
            "h": h,
            "epsilon": "small",
            "epsilon_value_[A]": eps_small,
        },
        "research": m_research.to_dict(),
        "validation": m_validation.to_dict(),
        "holdout": holdout_metrics,
        "cost_stress_[A]": cost_rows,
        "time_half": th,
        "placebos": placebos,
        "grid_w_stability": w_stab,
        "qlo_cliff": cliff,
        "grid_cell_count": len(grid_results),
        "grid_results": grid_results,
        "C_base_[A]": C_base,
    }
    return iv, summary


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(argv)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        cfg = load_package_config(args.package, CONFIG_DIR)
    except FileNotFoundError as e:
        write_untested_report(
            out_dir,
            package_id=args.package,
            edge_id=EDGE_ID,
            reason=str(e),
            data_path=args.data,
        )
        print(f"MEASUREMENT=UNTESTED reason={e}")
        return 0

    data_path = Path(args.data) if args.data else None
    conductor_order = Path(args.conductor_order)
    sealed_flag = holdout_is_sealed(bool(args.open_holdout), conductor_order)
    # Only allow sealed/ parquet load when BOTH open-holdout AND conductor order
    allow_load_holdout = (not sealed_flag) and bool(args.open_holdout)

    loaded = load_data_prov(
        data_path,
        cfg,
        open_holdout=bool(args.open_holdout),
        allow_load_holdout=allow_load_holdout,
    )
    if not loaded.ok:
        write_untested_report(
            out_dir,
            package_id=args.package,
            edge_id=cfg.get("edge_id", EDGE_ID),
            reason=loaded.reason,
            data_path=args.data,
        )
        print(f"MEASUREMENT=UNTESTED reason={loaded.reason}")
        return 0

    per_iv: list[InstrumentVerdict] = []
    summaries: dict[str, Any] = {}

    if loaded.pre_sliced:
        assert loaded.slice_bundles is not None
        for inst in sorted(loaded.slice_bundles.keys()):
            iv, summary = run_instrument_presliced(
                inst,
                loaded.slice_bundles[inst],
                cfg,
                open_holdout=bool(args.open_holdout),
                conductor_order=conductor_order,
                research_only=loaded.research_only,
            )
            per_iv.append(iv)
            summaries[inst] = summary
    else:
        assert loaded.frames is not None
        for inst in sorted(loaded.frames.keys()):
            iv, summary = run_instrument(
                inst,
                loaded.frames[inst],
                cfg,
                open_holdout=bool(args.open_holdout),
                conductor_order=conductor_order,
                research_only=loaded.research_only,
            )
            per_iv.append(iv)
            summaries[inst] = summary

    headline = aggregate_lab_verdict(per_iv)
    sealed = holdout_is_sealed(bool(args.open_holdout), conductor_order)

    record = {
        "package_id": args.package,
        "edge_id": cfg.get("edge_id", EDGE_ID),
        "MEASUREMENT": headline,
        "verdict": headline,
        "data_path": str(data_path),
        "dataset_id": (loaded.manifest or {}).get("DATASET_ID"),
        "clock_verdict": loaded.clock_verdict
        or (loaded.manifest or {}).get("clock_verdict"),
        "research_only": loaded.research_only,
        "pre_sliced": loaded.pre_sliced,
        "holdout": "SEALED" if sealed else "OPEN",
        "invented_numbers": False,
        "instruments": [
            {"instrument": iv.instrument, "verdict": iv.verdict, "reasons": iv.reasons}
            for iv in per_iv
        ],
        "metrics_summary": {
            k: {
                "research": v["research"],
                "validation": v["validation"],
                "holdout": v["holdout"],
                "grid_w_stability": v["grid_w_stability"],
                "placebos": {
                    "real_gap": v["placebos"].get("real_gap"),
                    "placebos": v["placebos"].get("placebos"),
                },
                "C_base_[A]": v["C_base_[A]"],
                "primary_cell": v["primary_cell"],
            }
            for k, v in summaries.items()
        },
        "full_summaries_path_hint": "see companion JSON keys under metrics if archived",
        "assumptions_[A]": {
            "C_base_bps": cfg["costs_bps"]["C_base"],
            "epsilon_small": cfg["parameter_grid"]["epsilon"]["small"],
            "epsilon_2x_small": cfg["parameter_grid"]["epsilon"]["2x_small"],
        },
        "non_claims": cfg.get("non_claims", []),
        # Keep full grid in JSON for audit (large but required)
        "full_instrument_summaries": summaries,
    }
    json_path, md_path = write_test_record(out_dir, record)
    print(f"MEASUREMENT={headline}")
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
