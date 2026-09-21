"""CLI entrypoint for PROV-MEAS-EDGE-003 / EDGE-20260910-003.

Usage:
  python -m src.run_edge003 --package PROV-MEAS-EDGE-003 \\
      --data /path/to/DATA-PROV-001 [--open-holdout]

Without locked primary_cell → MEASUREMENT=BLOCKED_PENDING_PRIMARY_CELL / UNTESTED.
Holdout sealed/ NEVER opened unless --open-holdout + Conductor order.
Cite CEM-20260910-001 — NOT a rescue of EDGE-001.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Optional

import numpy as np
import pandas as pd

from .costs import stress_schedule
from .data_loader import SliceBundle, load_data_prov, load_package_config
from .metrics import (
    grid_w_stability,
    qlo_cliff_flag,
    slice_metrics,
    time_half_stability,
)
from .report import write_test_record, write_untested_report
from .signal_edge003 import build_trade_frame
from .splits import (
    WARMUP_BARS,
    assert_holdout_exists,
    bounds_from_presliced,
    holdout_is_sealed,
)
from .verdict import InstrumentVerdict, aggregate_lab_verdict, evaluate_instrument

HARNESS_ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = HARNESS_ROOT / "config"
OUT_DIR = HARNESS_ROOT / "out"
DEFAULT_CONDUCTOR_ORDER = HARNESS_ROOT / "config" / "CONDUCTOR_OPEN_HOLDOUT.order"

PACKAGE_ID = "PROV-MEAS-EDGE-003"
EDGE_ID = "EDGE-20260910-003"
CEM_CITATION = "CEM-20260910-001"


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Examiner harness EDGE-20260910-003")
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
    p.add_argument(
        "--test-id",
        default="TEST-20260910-002",
        help="Stable TEST id for artifacts",
    )
    return p.parse_args(argv)


def _epsilon_value(cfg: dict[str, Any], name: str) -> float:
    eps = cfg["parameter_grid"]["epsilon"]
    if name == "small":
        return float(eps["small"])
    if name in ("2x_small", "2×small", "2x"):
        return float(eps["2x_small"])
    raise KeyError(name)


def primary_cell_is_locked(cfg: dict[str, Any]) -> bool:
    pc = cfg.get("primary_cell")
    status = str(cfg.get("primary_cell_status", "")).upper()
    if pc is None:
        return False
    if status in ("PENDING_STATISTICIAN_LOCK", "PENDING", ""):
        if isinstance(pc, dict) and pc.get("locked"):
            return True
        return False
    if status == "LOCKED":
        return isinstance(pc, dict) and all(k in pc for k in ("p", "L", "h"))
    return isinstance(pc, dict) and all(k in pc for k in ("p", "L", "h"))


def write_blocked_pending_primary(
    out_dir: Path,
    *,
    package_id: str,
    edge_id: str,
    reason: str,
    data_path: Optional[str] = None,
) -> tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    record = {
        "TEST_ID": None,
        "package_id": package_id,
        "edge_id": edge_id,
        "MEASUREMENT": "BLOCKED_PENDING_PRIMARY_CELL",
        "verdict": "UNTESTED",
        "reason": reason,
        "data_path": data_path,
        "metrics": None,
        "invented_numbers": False,
        "holdout": "SEALED",
        "cemetery_citation": CEM_CITATION,
        "non_claims": [
            "No primary cell invented",
            "NOT a rescue of CEM-20260910-001",
            "No performance numbers without locked primary + approved data",
        ],
    }
    json_path = out_dir / f"STATUS_PENDING_PRIMARY_CELL_{edge_id}.json"
    md_path = out_dir / f"STATUS_PENDING_PRIMARY_CELL_{edge_id}.md"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2)
        f.write("\n")
    md = f"""# MEASUREMENT = BLOCKED_PENDING_PRIMARY_CELL — {edge_id}

**Package:** `{package_id}`
**Verdict:** UNTESTED / BLOCKED_PENDING_PRIMARY_CELL
**Cemetery citation:** {CEM_CITATION} (NOT a rescue of EDGE-001)

## Reason
{reason}

## Rules honored
- No Sharpe / return / trade-count figures invented.
- primary_cell left unlocked — Statistician lock required.
- Holdout remains SEALED.
"""
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)
    return json_path, md_path


def placebo_tests_range(
    df: pd.DataFrame,
    h: int,
    seed: int = 20260910,
) -> dict[str, Any]:
    """Placebos for high-range fade vs non-extreme contrast (Edge Card §FALSIFICATION)."""
    rng = np.random.default_rng(seed)
    work = df.copy()
    real = slice_metrics(
        work, C=0.0, h=h, slice_name="real_gross", high_col="low_range"
    )
    real_gap = real.low_high_gap_bps

    if work["range"].notna().sum() == 0:
        return {"real_gap": real_gap, "placebos": {}, "seed": seed, "note": "no range"}

    # (1) shuffled range ranks
    rv_vals = work["range"].to_numpy().copy()
    valid = np.isfinite(rv_vals)
    shuffled = rv_vals.copy()
    shuffled[valid] = rng.permutation(rv_vals[valid])
    p1 = work.copy()
    p1["range"] = shuffled
    p1["signal"] = (
        p1["range"].notna()
        & p1["Q_hi_trail"].notna()
        & (p1["range"] >= p1["Q_hi_trail"])
        & (p1["r"].abs() > 0)
    )
    p1["low_range"] = (
        p1["range"].notna()
        & p1["Q_med_trail"].notna()
        & (p1["range"] < p1["Q_med_trail"])
        & (p1["r"].abs() > 0)
    )
    m1 = slice_metrics(p1, C=0.0, h=h, slice_name="placebo_shuffled_range", high_col="low_range")

    # (2) random equal-count high-range labels
    n_hi = int(work["signal"].sum())
    eligible = work["range"].notna() & work["gross_bps"].notna() & work["r"].notna()
    eligible_idx = np.flatnonzero(eligible.to_numpy())
    p2 = work.copy()
    p2["signal"] = False
    p2["low_range"] = False
    if n_hi > 0 and eligible_idx.size >= n_hi:
        chosen = rng.choice(eligible_idx, size=n_hi, replace=False)
        p2.loc[p2.index[chosen], "signal"] = True
        n_lo = int(work["low_range"].sum())
        remain = np.setdiff1d(eligible_idx, chosen, assume_unique=False)
        if n_lo > 0 and remain.size >= n_lo:
            hchosen = rng.choice(remain, size=n_lo, replace=False)
            p2.loc[p2.index[hchosen], "low_range"] = True
    m2 = slice_metrics(p2, C=0.0, h=h, slice_name="placebo_random_bins", high_col="low_range")

    # (3) scrambled signs inside high-range bin
    p3 = work.copy()
    sig_mask = p3["signal"].to_numpy()
    g = p3["gross_bps"].to_numpy(dtype=float).copy()
    flips = rng.choice([-1.0, 1.0], size=g.size)
    g[sig_mask] = np.abs(g[sig_mask]) * flips[sig_mask]
    p3["gross_bps"] = g
    m3 = slice_metrics(p3, C=0.0, h=h, slice_name="placebo_scrambled_signs", high_col="low_range")

    def beats(real_g, placebo_g, ci_low, ci_high) -> Optional[bool]:
        if real_g is None or placebo_g is None:
            return None
        if ci_low is not None and ci_high is not None:
            if ci_low <= placebo_g <= ci_high:
                return True
        return bool(placebo_g >= real_g)

    return {
        "real_gap": real_gap,
        "real_ci": {"low": real.gap_nw_ci_low, "high": real.gap_nw_ci_high},
        "placebos": {
            "shuffled_range_ranks": {
                "gap": m1.low_high_gap_bps,
                "matches_or_beats_real": beats(
                    real_gap, m1.low_high_gap_bps, real.gap_nw_ci_low, real.gap_nw_ci_high
                ),
            },
            "random_equal_count_high_range": {
                "gap": m2.low_high_gap_bps,
                "matches_or_beats_real": beats(
                    real_gap, m2.low_high_gap_bps, real.gap_nw_ci_low, real.gap_nw_ci_high
                ),
            },
            "scrambled_signs_in_high_range": {
                "gap": m3.low_high_gap_bps,
                "matches_or_beats_real": beats(
                    real_gap, m3.low_high_gap_bps, real.gap_nw_ci_low, real.gap_nw_ci_high
                ),
            },
        },
        "seed": seed,
    }


def _sm(df: pd.DataFrame, C: float, h: int, slice_name: str):
    return slice_metrics(df, C=C, h=h, slice_name=slice_name, high_col="low_range")


def run_instrument_presliced(
    inst: str,
    bundle: SliceBundle,
    cfg: dict[str, Any],
    *,
    open_holdout: bool,
    conductor_order: Path,
    research_only: bool,
) -> tuple[InstrumentVerdict, dict[str, Any]]:
    primary = cfg["primary_cell"]
    grid = cfg["parameter_grid"]
    gates = cfg["min_gates"]
    C_base = float(cfg["costs_bps"]["C_base"])
    costs = stress_schedule(C_base)
    eps_small = _epsilon_value(cfg, "small")
    contrast_q = float(grid.get("contrast_median_q", 0.5))
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
    try:
        if bundle.holdout_file_present:
            holdout_exists = True
        else:
            assert_holdout_exists(bounds, file_present=False)
            holdout_exists = False
    except AssertionError:
        holdout_exists = bundle.holdout_file_present

    sealed = holdout_is_sealed(open_holdout, conductor_order)

    p = float(primary["p"])
    L = int(primary["L"])
    h = int(primary["h"])

    research_path = pd.concat([bundle.warmup, bundle.research], ignore_index=True)
    frame_r = build_trade_frame(
        research_path, L=L, p=p, h=h, epsilon=eps_small, contrast_q=contrast_q
    )
    research_df = frame_r.iloc[n_warmup:].copy()
    mid = n_research // 2
    half1 = research_df.iloc[:mid].copy()
    half2 = research_df.iloc[mid:].copy()

    m_research = _sm(research_df, C=costs["C_1x"], h=h, slice_name="research")
    sig_r = research_df.loc[research_df["signal"] & research_df["gross_bps"].notna()]
    gross_r = sig_r["gross_bps"]
    mean_gross = float(gross_r.mean()) if len(gross_r) else None
    net_1x = float(gross_r.mean() - costs["C_1x"]) if len(gross_r) else None
    net_2x = float(gross_r.mean() - costs["C_2x"]) if len(gross_r) else None
    net_3x = float(gross_r.mean() - costs["C_3x"]) if len(gross_r) else None

    cost_rows = {}
    for label, C in costs.items():
        sm = _sm(research_df, C=C, h=h, slice_name=f"research_{label}")
        cost_rows[label] = sm.to_dict()

    th = time_half_stability(half1, half2, h=h, C=costs["C_1x"])
    # time_half_stability uses default high_col=high_rv; our frame aliases high_rv=low_range

    placebos = placebo_tests_range(research_df, h=h, seed=seed)
    placebo_beats = any(
        bool(v.get("matches_or_beats_real"))
        for v in placebos.get("placebos", {}).values()
        if v.get("matches_or_beats_real") is not None
    )

    gap_by_p: dict[float, Optional[float]] = {}
    gap_by_L: dict[int, Optional[float]] = {}
    grid_results = []
    for p_i in grid["p"]:
        for L_i in grid["L"]:
            for h_i in grid["h"]:
                for eps_name in ("small", "2x_small"):
                    eps_v = _epsilon_value(cfg, eps_name)
                    fr = build_trade_frame(
                        research_path,
                        L=int(L_i),
                        p=float(p_i),
                        h=int(h_i),
                        epsilon=eps_v,
                        contrast_q=contrast_q,
                    )
                    rdf = fr.iloc[n_warmup:].copy()
                    sm = _sm(rdf, C=costs["C_1x"], h=int(h_i), slice_name="research")
                    cell = {
                        "p": p_i,
                        "L": L_i,
                        "h": h_i,
                        "epsilon": eps_name,
                        "metrics": sm.to_dict(),
                        "is_primary": (
                            float(p_i) == p
                            and int(L_i) == L
                            and int(h_i) == h
                            and eps_name == "small"
                        ),
                    }
                    grid_results.append(cell)
                    if (
                        int(L_i) == L
                        and int(h_i) == h
                        and eps_name == "small"
                    ):
                        gap_by_p[float(p_i)] = sm.low_high_gap_bps
                    if (
                        float(p_i) == p
                        and int(h_i) == h
                        and eps_name == "small"
                    ):
                        gap_by_L[int(L_i)] = sm.low_high_gap_bps

    # Reuse grid_w_stability on p keys (cast to int-like via 100*p for dict keys)
    gap_by_p_int = {int(round(k * 100)): v for k, v in gap_by_p.items()}
    p_stab = grid_w_stability(gap_by_p_int)
    p_stab["param"] = "p"
    p_stab["gap_by_p"] = {str(k): v for k, v in gap_by_p.items()}
    cliff = qlo_cliff_flag(gap_by_p)

    # RESEARCH-first gate: skip VALIDATION if RESEARCH would FAIL
    research_iv = evaluate_instrument(
        instrument=inst,
        research=m_research.to_dict(),
        validation=None,
        gates=gates,
        grid_w_pass=bool(p_stab["pass"]),
        qlo_cliff=cliff,
        placebo_beats=placebo_beats,
        concentration_frac=m_research.concentration_day_frac,
        net_1x=net_1x,
        net_2x=net_2x,
        net_3x=net_3x,
        gap_ci_excludes_zero_research=m_research.gap_ci_excludes_zero,
        research_only=True,
    )
    # Explicit gross≤0 kill (CEM-001 spirit)
    if mean_gross is not None and mean_gross <= 0:
        research_iv = InstrumentVerdict(
            instrument=inst,
            verdict="FAIL",
            reasons=list(research_iv.reasons)
            + [f"gross mean fade <= 0 on RESEARCH (gross={mean_gross}) — CEM-001 spirit"],
            details=research_iv.details,
        )
    elif research_iv.verdict not in ("FAIL", "FAIL-INSUFFICIENT") and (
        mean_gross is None
    ):
        pass

    research_failed = research_iv.verdict in ("FAIL", "FAIL-INSUFFICIENT")

    m_validation = None
    validation_net_1x = None
    validation_df_metrics = None
    if not research_failed and not research_only:
        val_prefix = (
            bundle.research.iloc[-warmup_bars:]
            if n_research >= warmup_bars
            else bundle.research
        )
        validation_path = pd.concat([val_prefix, bundle.validation], ignore_index=True)
        frame_v = build_trade_frame(
            validation_path, L=L, p=p, h=h, epsilon=eps_small, contrast_q=contrast_q
        )
        validation_df = frame_v.iloc[len(val_prefix) :].copy()
        m_validation = _sm(
            validation_df, C=costs["C_1x"], h=h, slice_name="validation"
        )
        val_sig = validation_df.loc[
            validation_df["signal"] & validation_df["gross_bps"].notna()
        ]
        validation_net_1x = (
            float(val_sig["gross_bps"].mean() - costs["C_1x"]) if len(val_sig) else None
        )
        validation_df_metrics = m_validation.to_dict()

    # Holdout never unless unlocked (and research not failed)
    holdout_metrics = None
    if (
        not sealed
        and holdout_exists
        and not research_only
        and not research_failed
        and bundle.holdout is not None
    ):
        h_prefix = (
            bundle.validation.iloc[-warmup_bars:]
            if n_validation >= warmup_bars
            else bundle.validation
        )
        holdout_path = pd.concat([h_prefix, bundle.holdout], ignore_index=True)
        frame_h = build_trade_frame(
            holdout_path, L=L, p=p, h=h, epsilon=eps_small, contrast_q=contrast_q
        )
        holdout_df = frame_h.iloc[len(h_prefix) :].copy()
        holdout_metrics = _sm(
            holdout_df, C=costs["C_1x"], h=h, slice_name="holdout"
        ).to_dict()

    if research_failed:
        iv = research_iv
    else:
        iv = evaluate_instrument(
            instrument=inst,
            research=m_research.to_dict(),
            validation=validation_df_metrics,
            gates=gates,
            grid_w_pass=bool(p_stab["pass"]),
            qlo_cliff=cliff,
            placebo_beats=placebo_beats,
            concentration_frac=m_research.concentration_day_frac,
            net_1x=net_1x,
            net_2x=net_2x,
            net_3x=net_3x,
            gap_ci_excludes_zero_research=m_research.gap_ci_excludes_zero,
            validation_net_1x=validation_net_1x,
            validation_gap_ci_excludes_zero=(
                m_validation.gap_ci_excludes_zero if m_validation else None
            ),
            validation_signal_count=(
                m_validation.signal_count if m_validation else 0
            ),
            research_only=research_only or m_validation is None,
        )
        if mean_gross is not None and mean_gross <= 0:
            iv = InstrumentVerdict(
                instrument=inst,
                verdict="FAIL",
                reasons=list(iv.reasons)
                + [f"gross mean fade <= 0 on RESEARCH (gross={mean_gross})"],
                details=iv.details,
            )

    summary = {
        "instrument": inst,
        "n_bars": n_warmup + n_research + n_validation + n_holdout_loaded,
        "pre_sliced": True,
        "cemetery_citation": CEM_CITATION,
        "not_rescue_of_edge001": True,
        "validation_skipped_because_research_fail": research_failed,
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
            "p": p,
            "L": L,
            "h": h,
            "epsilon": "small",
            "epsilon_value_[A]": eps_small,
            "range_definition": "(high-low)/close",
            "position": "-Sign(r_t)",
            "r_t": "log_return",
        },
        "research": m_research.to_dict(),
        "research_mean_gross_bps": mean_gross,
        "validation": validation_df_metrics,
        "holdout": holdout_metrics,
        "cost_stress_[A]": cost_rows,
        "time_half": th,
        "placebos": placebos,
        "grid_p_stability": p_stab,
        "L_neighbor_gaps": {str(k): v for k, v in gap_by_L.items()},
        "p_cliff": cliff,
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

    if not primary_cell_is_locked(cfg):
        write_blocked_pending_primary(
            out_dir,
            package_id=args.package,
            edge_id=cfg.get("edge_id", EDGE_ID),
            reason=(
                "primary_cell is null / PENDING_STATISTICIAN_LOCK — "
                "CLI refuses RESEARCH/VALIDATION measurement (UNTESTED / "
                "BLOCKED_PENDING_PRIMARY_CELL). No metrics invented."
            ),
            data_path=args.data,
        )
        print("MEASUREMENT=BLOCKED_PENDING_PRIMARY_CELL")
        print("MEASUREMENT=UNTESTED reason=primary_cell unlocked")
        return 0

    data_path = Path(args.data) if args.data else None
    conductor_order = Path(args.conductor_order)
    sealed_flag = holdout_is_sealed(bool(args.open_holdout), conductor_order)
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

    if not loaded.pre_sliced:
        write_untested_report(
            out_dir,
            package_id=args.package,
            edge_id=cfg.get("edge_id", EDGE_ID),
            reason="EDGE-003 runner requires pre-sliced SEAL_LOCK layout (DATA-PROV-001)",
            data_path=args.data,
        )
        print("MEASUREMENT=UNTESTED reason=pre_sliced_required")
        return 0

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

    headline = aggregate_lab_verdict(per_iv)
    sealed = holdout_is_sealed(bool(args.open_holdout), conductor_order)

    record = {
        "TEST_ID": args.test_id,
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
        "cemetery_citation": CEM_CITATION,
        "not_rescue_of_edge001": True,
        "signal_module": "range_expansion_snapback",
        "instruments": [
            {"instrument": iv.instrument, "verdict": iv.verdict, "reasons": iv.reasons}
            for iv in per_iv
        ],
        "metrics_summary": {
            k: {
                "research": v["research"],
                "research_mean_gross_bps": v["research_mean_gross_bps"],
                "validation": v["validation"],
                "holdout": v["holdout"],
                "grid_p_stability": v["grid_p_stability"],
                "placebos": {
                    "real_gap": v["placebos"].get("real_gap"),
                    "placebos": v["placebos"].get("placebos"),
                },
                "C_base_[A]": v["C_base_[A]"],
                "primary_cell": v["primary_cell"],
                "validation_skipped_because_research_fail": v[
                    "validation_skipped_because_research_fail"
                ],
            }
            for k, v in summaries.items()
        },
        "assumptions_[A]": {
            "C_base_bps": cfg["costs_bps"]["C_base"],
            "epsilon_small": cfg["parameter_grid"]["epsilon"]["small"],
            "epsilon_2x_small": cfg["parameter_grid"]["epsilon"]["2x_small"],
            "range_t": "(high-low)/close",
            "r_t": "log_return",
        },
        "non_claims": cfg.get("non_claims", []),
        "full_instrument_summaries": summaries,
    }
    json_path, md_path = write_test_record(out_dir, record)

    # Also write stable TEST-YYYYMMDD-NNN names
    stable_json = out_dir / f"{args.test_id}-{EDGE_ID}.json"
    stable_md = out_dir / f"{args.test_id}-{EDGE_ID}.md"
    with open(stable_json, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2, default=str)
        f.write("\n")
    stable_md.write_text(md_path.read_text(encoding="utf-8"), encoding="utf-8")

    print(f"MEASUREMENT={headline}")
    print(f"TEST_ID={args.test_id}")
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    print(f"Wrote {stable_json}")
    print(f"Wrote {stable_md}")
    print(f"cemetery_citation={CEM_CITATION}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
