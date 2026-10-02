"""CLI entrypoint for PROV-MEAS-EDGE-004 / EDGE-20260910-004.

Usage:
  python -m src.run_edge004 --package PROV-MEAS-EDGE-004 \\
      --data /path/to/DATA-PROV-001 [--open-holdout]

Cross-asset BTC lead → ETH response. VALIDATION only if RESEARCH does not FAIL.
Holdout sealed unless --open-holdout + Conductor order.
Cite CEM-20260910-001 and CEM-20260910-002 — NOT a rescue of either.
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
    concentration_frac,
    distinct_signal_days,
    grid_w_stability,
    mean_or_none,
    newey_west_mean_se,
)
from .report import write_test_record, write_untested_report
from .signal_edge004 import (
    build_btc_to_eth,
    build_eth_to_btc_reverse,
    timestamp_shuffle_btc,
)
from .splits import (
    WARMUP_BARS,
    assert_holdout_exists,
    bounds_from_presliced,
    holdout_is_sealed,
)
from .verdict import InstrumentVerdict, aggregate_lab_verdict
from .verdict_edge004 import evaluate_edge004, matches_or_beats_within_ci

HARNESS_ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = HARNESS_ROOT / "config"
OUT_DIR = HARNESS_ROOT / "out"
DEFAULT_CONDUCTOR_ORDER = HARNESS_ROOT / "config" / "CONDUCTOR_OPEN_HOLDOUT.order"

PACKAGE_ID = "PROV-MEAS-EDGE-004"
EDGE_ID = "EDGE-20260910-004"
CEM_CITATIONS = ["CEM-20260910-001", "CEM-20260910-002"]
CEM_CITATION_STR = "CEM-20260910-001;CEM-20260910-002"


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Examiner harness EDGE-20260910-004")
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
        default="TEST-20260910-003",
        help="Stable TEST id for artifacts",
    )
    return p.parse_args(argv)


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
        return isinstance(pc, dict) and all(k in pc for k in ("p", "L", "h", "kappa"))
    return isinstance(pc, dict) and all(k in pc for k in ("p", "L", "h", "kappa"))


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
        "cemetery_citations": CEM_CITATIONS,
        "cemetery_citation": CEM_CITATION_STR,
        "non_claims": [
            "No primary cell invented",
            "NOT a rescue of CEM-20260910-001 or CEM-20260910-002",
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
**Cemetery citations:** {CEM_CITATION_STR} (NOT a rescue of EDGE-001 or EDGE-003)

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


def _concat_warmup_slice(warmup: pd.DataFrame, slice_df: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([warmup, slice_df], ignore_index=True)


def _signal_stats(frame: pd.DataFrame, C: float, h: int) -> dict[str, Any]:
    sig = frame.loc[frame["signal"] & frame["gross_bps"].notna()]
    gross = sig["gross_bps"].to_numpy(dtype=float)
    mean_g = mean_or_none(gross)
    mean_n = None if mean_g is None else float(mean_g - C)
    mu, se = newey_west_mean_se(gross, lag=h) if gross.size else (None, None)
    z = 1.959963984540054
    ci_low = None if mu is None or se is None else float(mu - z * se)
    ci_high = None if mu is None or se is None else float(mu + z * se)
    hit = None if gross.size == 0 else float(np.mean(gross > 0))
    return {
        "signal_count": int(len(sig)),
        "distinct_utc_days": distinct_signal_days(frame, "signal"),
        "mean_gross_bps": mean_g,
        "mean_net_bps": mean_n,
        "hit_rate": hit,
        "nw_mean": mu,
        "nw_se": se,
        "nw_ci_low": ci_low,
        "nw_ci_high": ci_high,
        "concentration_day_frac": concentration_frac(frame, "signal"),
        "notes": f"NW lag=h={h}; C={C}",
    }


def _pair_paths(
    btc_bundle: SliceBundle,
    eth_bundle: SliceBundle,
    *,
    which: str,
    warmup_bars: int,
) -> tuple[pd.DataFrame, pd.DataFrame, int]:
    """Return (btc_path, eth_path, n_prefix) for research or validation.

    Research: warmup + research; prefix length = len(warmup).
    Validation: last warmup_bars of research as prefix + validation.
    """
    if which == "research":
        btc = _concat_warmup_slice(btc_bundle.warmup, btc_bundle.research)
        eth = _concat_warmup_slice(eth_bundle.warmup, eth_bundle.research)
        return btc, eth, len(btc_bundle.warmup)
    if which == "validation":
        n_r = len(btc_bundle.research)
        b_pref = (
            btc_bundle.research.iloc[-warmup_bars:]
            if n_r >= warmup_bars
            else btc_bundle.research
        )
        e_pref = (
            eth_bundle.research.iloc[-warmup_bars:]
            if len(eth_bundle.research) >= warmup_bars
            else eth_bundle.research
        )
        btc = _concat_warmup_slice(b_pref, btc_bundle.validation)
        eth = _concat_warmup_slice(e_pref, eth_bundle.validation)
        return btc, eth, len(b_pref)
    raise ValueError(which)


def run_cross_asset_presliced(
    btc_bundle: SliceBundle,
    eth_bundle: SliceBundle,
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
    seed = int(cfg["stats"]["placebo_seed"])
    warmup_bars = int(cfg.get("warmup_bars", WARMUP_BARS))

    n_warmup = len(btc_bundle.warmup)
    n_research = len(btc_bundle.research)
    n_validation = len(btc_bundle.validation)
    n_holdout_loaded = len(btc_bundle.holdout) if btc_bundle.holdout is not None else 0

    bounds = bounds_from_presliced(
        n_warmup=n_warmup,
        n_research=n_research,
        n_validation=n_validation,
        n_holdout=n_holdout_loaded if btc_bundle.holdout is not None else 0,
    )
    try:
        if btc_bundle.holdout_file_present:
            holdout_exists = True
        else:
            assert_holdout_exists(bounds, file_present=False)
            holdout_exists = False
    except AssertionError:
        holdout_exists = btc_bundle.holdout_file_present

    sealed = holdout_is_sealed(open_holdout, conductor_order)

    p = float(primary["p"])
    L = int(primary["L"])
    h = int(primary["h"])
    kappa = float(primary["kappa"])

    btc_path, eth_path, n_prefix = _pair_paths(
        btc_bundle, eth_bundle, which="research", warmup_bars=warmup_bars
    )

    # --- Primary BTC→ETH ---
    frame_full = build_btc_to_eth(
        btc_path, eth_path, L=L, p=p, h=h, kappa=kappa, apply_kappa=True
    )
    # Drop warmup-aligned prefix by timestamp count on aligned frame:
    # Use first n_prefix *aligned* bars approx via original warmup length on lead timestamps.
    # Safer: mark bars whose timestamp is in warmup set.
    warmup_ts = set(
        pd.to_datetime(btc_bundle.warmup["timestamp"], utc=True).tolist()
    )
    # Also include eth warmup timestamps (same expected)
    warmup_ts |= set(
        pd.to_datetime(eth_bundle.warmup["timestamp"], utc=True).tolist()
    )
    ts_all = pd.to_datetime(frame_full["timestamp"], utc=True)
    research_mask = ~ts_all.isin(warmup_ts)
    research_df = frame_full.loc[research_mask].copy()

    m_research = _signal_stats(research_df, C=costs["C_1x"], h=h)
    mean_gross = m_research["mean_gross_bps"]
    net_1x = m_research["mean_net_bps"]
    # stress nets from same gross
    gross_arr = research_df.loc[
        research_df["signal"] & research_df["gross_bps"].notna(), "gross_bps"
    ].to_numpy(dtype=float)
    net_2x = float(np.mean(gross_arr) - costs["C_2x"]) if gross_arr.size else None
    net_3x = float(np.mean(gross_arr) - costs["C_3x"]) if gross_arr.size else None

    cost_rows: dict[str, Any] = {}
    for label, C in costs.items():
        cost_rows[label] = _signal_stats(research_df, C=C, h=h)

    # --- Reverse control ETH→BTC ---
    rev_full = build_eth_to_btc_reverse(
        btc_path, eth_path, L=L, p=p, h=h, kappa=kappa
    )
    rev_df = rev_full.loc[
        ~pd.to_datetime(rev_full["timestamp"], utc=True).isin(warmup_ts)
    ].copy()
    m_rev = _signal_stats(rev_df, C=costs["C_1x"], h=h)
    reverse_matches = matches_or_beats_within_ci(
        mean_gross,
        m_rev["mean_gross_bps"],
        m_research["nw_ci_low"],
        m_research["nw_ci_high"],
    )

    # --- Timestamp shuffle ---
    sh_full = timestamp_shuffle_btc(
        btc_path, eth_path, L=L, p=p, h=h, kappa=kappa, seed=seed
    )
    sh_df = sh_full.loc[
        ~pd.to_datetime(sh_full["timestamp"], utc=True).isin(warmup_ts)
    ].copy()
    m_sh = _signal_stats(sh_df, C=costs["C_1x"], h=h)
    shuffle_matches = matches_or_beats_within_ci(
        mean_gross,
        m_sh["mean_gross_bps"],
        m_research["nw_ci_low"],
        m_research["nw_ci_high"],
    )

    # --- kappa ablation (diagnostic only) ---
    abl_full = build_btc_to_eth(
        btc_path, eth_path, L=L, p=p, h=h, kappa=kappa, apply_kappa=False
    )
    abl_df = abl_full.loc[
        ~pd.to_datetime(abl_full["timestamp"], utc=True).isin(warmup_ts)
    ].copy()
    m_abl = _signal_stats(abl_df, C=costs["C_1x"], h=h)

    # --- p-grid stability (L,h,kappa fixed at primary) ---
    gap_by_p_int: dict[int, Optional[float]] = {}
    gross_by_p: dict[str, Optional[float]] = {}
    grid_results: list[dict[str, Any]] = []
    for p_i in grid["p"]:
        for L_i in grid["L"]:
            for h_i in grid["h"]:
                for k_i in grid["kappa"]:
                    fr = build_btc_to_eth(
                        btc_path,
                        eth_path,
                        L=int(L_i),
                        p=float(p_i),
                        h=int(h_i),
                        kappa=float(k_i),
                        apply_kappa=True,
                    )
                    rdf = fr.loc[
                        ~pd.to_datetime(fr["timestamp"], utc=True).isin(warmup_ts)
                    ].copy()
                    sm = _signal_stats(rdf, C=costs["C_1x"], h=int(h_i))
                    is_primary = (
                        float(p_i) == p
                        and int(L_i) == L
                        and int(h_i) == h
                        and float(k_i) == kappa
                    )
                    grid_results.append(
                        {
                            "p": p_i,
                            "L": L_i,
                            "h": h_i,
                            "kappa": k_i,
                            "metrics": sm,
                            "is_primary": is_primary,
                        }
                    )
                    if int(L_i) == L and int(h_i) == h and float(k_i) == kappa:
                        gap_by_p_int[int(round(float(p_i) * 100))] = sm[
                            "mean_gross_bps"
                        ]
                        gross_by_p[str(p_i)] = sm["mean_gross_bps"]

    p_stab = grid_w_stability(gap_by_p_int)
    p_stab["param"] = "p"
    p_stab["gross_by_p"] = gross_by_p

    # RESEARCH-first verdict
    research_v = evaluate_edge004(
        instrument="BTC_ETH",
        signal_count=m_research["signal_count"],
        distinct_utc_days=m_research["distinct_utc_days"],
        mean_gross_bps=mean_gross,
        net_1x=net_1x,
        net_2x=net_2x,
        net_3x=net_3x,
        concentration_frac=m_research["concentration_day_frac"],
        p_grid_keep_sign_count=int(p_stab["keep_sign_count"]),
        p_grid_n=len(grid["p"]),
        reverse_matches_or_beats=reverse_matches,
        shuffle_matches_or_beats=shuffle_matches,
        gates={**gates, "grid_p_stability_min_keep_sign": int(
            cfg["stats"].get("grid_p_stability_min_keep_sign", 2)
        )},
        validation_reached=False,
        research_only=True,
    )
    research_failed = research_v.verdict in ("FAIL", "FAIL-INSUFFICIENT")

    # --- VALIDATION only if RESEARCH not FAIL ---
    m_validation = None
    validation_net_1x = None
    validation_ran = False
    if not research_failed and not research_only:
        validation_ran = True
        vb, ve, _ = _pair_paths(
            btc_bundle, eth_bundle, which="validation", warmup_bars=warmup_bars
        )
        # Prefix timestamps = those in the prefix portion of vb
        # Use research timestamps as the "already seen" set for cutting prefix:
        # bars whose timestamp is NOT in validation slice timestamps
        val_ts = set(
            pd.to_datetime(btc_bundle.validation["timestamp"], utc=True).tolist()
        )
        val_ts |= set(
            pd.to_datetime(eth_bundle.validation["timestamp"], utc=True).tolist()
        )
        vf = build_btc_to_eth(vb, ve, L=L, p=p, h=h, kappa=kappa, apply_kappa=True)
        validation_df = vf.loc[
            pd.to_datetime(vf["timestamp"], utc=True).isin(val_ts)
        ].copy()
        m_validation = _signal_stats(validation_df, C=costs["C_1x"], h=h)
        validation_net_1x = m_validation["mean_net_bps"]

    # Holdout never unless unlocked (and research not failed)
    holdout_metrics = None
    if (
        not sealed
        and holdout_exists
        and not research_only
        and not research_failed
        and btc_bundle.holdout is not None
        and eth_bundle.holdout is not None
    ):
        # Deliberately not implementing holdout eval path in provisional RESEARCH —
        # sealed remains closed by default. If unlocked later, extend carefully.
        holdout_metrics = {
            "note": "holdout unlock path reserved; not evaluated in this provisional run"
        }

    if research_failed:
        iv = research_v.to_instrument_verdict()
    else:
        final_v = evaluate_edge004(
            instrument="BTC_ETH",
            signal_count=m_research["signal_count"],
            distinct_utc_days=m_research["distinct_utc_days"],
            mean_gross_bps=mean_gross,
            net_1x=net_1x,
            net_2x=net_2x,
            net_3x=net_3x,
            concentration_frac=m_research["concentration_day_frac"],
            p_grid_keep_sign_count=int(p_stab["keep_sign_count"]),
            p_grid_n=len(grid["p"]),
            reverse_matches_or_beats=reverse_matches,
            shuffle_matches_or_beats=shuffle_matches,
            gates={**gates, "grid_p_stability_min_keep_sign": int(
                cfg["stats"].get("grid_p_stability_min_keep_sign", 2)
            )},
            validation_reached=validation_ran and m_validation is not None,
            validation_net_1x=validation_net_1x,
            research_only=research_only or not validation_ran,
        )
        iv = final_v.to_instrument_verdict()

    summary = {
        "instrument": "BTC_ETH",
        "claim": "BTC_lead_ETH_trade",
        "n_bars_btc_research": n_research,
        "n_bars_eth_research": len(eth_bundle.research),
        "n_aligned_research": int(len(research_df)),
        "pre_sliced": True,
        "cemetery_citations": CEM_CITATIONS,
        "cemetery_citation": CEM_CITATION_STR,
        "not_rescue_of_edge001": True,
        "not_rescue_of_edge003": True,
        "validation_ran": validation_ran,
        "validation_skipped_because_research_fail": research_failed,
        "splits": {
            "warmup_end": bounds.warmup_end,
            "research": [bounds.research_start, bounds.research_end],
            "validation": [bounds.validation_start, bounds.validation_end],
            "holdout": [bounds.holdout_start, bounds.holdout_end],
            "holdout_sealed": sealed,
            "holdout_exists": holdout_exists,
            "holdout_loaded": btc_bundle.holdout is not None,
            "source": "SEAL_LOCK_slices",
            "n_warmup": n_warmup,
            "n_research": n_research,
            "n_validation": n_validation,
        },
        "primary_cell": {
            "p": p,
            "L": L,
            "h": h,
            "kappa": kappa,
            "position": "Sign(r_BTC_t) on ETH",
            "r_t": "log_return",
            "alignment": "inner_join_on_timestamp",
        },
        "research": m_research,
        "research_mean_gross_bps": mean_gross,
        "research_net_1x": net_1x,
        "research_net_2x": net_2x,
        "research_net_3x": net_3x,
        "validation": m_validation,
        "holdout": holdout_metrics,
        "cost_stress_[A]": cost_rows,
        "controls": {
            "reverse_ETH_to_BTC": {
                **m_rev,
                "matches_or_beats_primary": reverse_matches,
            },
            "timestamp_shuffle_BTC_vs_ETH": {
                **m_sh,
                "matches_or_beats_primary": shuffle_matches,
                "seed": seed,
            },
            "kappa_ablation_diagnostic": {
                **m_abl,
                "note": "diagnostic only — not alternate headline",
            },
        },
        "grid_p_stability": p_stab,
        "grid_cell_count": len(grid_results),
        "grid_results": grid_results,
        "C_base_[A]": C_base,
        "n_prefix_used": n_prefix,
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

    if not loaded.pre_sliced:
        write_untested_report(
            out_dir,
            package_id=args.package,
            edge_id=cfg.get("edge_id", EDGE_ID),
            reason="EDGE-004 runner requires pre-sliced SEAL_LOCK layout (DATA-PROV-001)",
            data_path=args.data,
        )
        print("MEASUREMENT=UNTESTED reason=pre_sliced_required")
        return 0

    assert loaded.slice_bundles is not None
    if "BTC" not in loaded.slice_bundles or "ETH" not in loaded.slice_bundles:
        write_untested_report(
            out_dir,
            package_id=args.package,
            edge_id=cfg.get("edge_id", EDGE_ID),
            reason="EDGE-004 requires both BTC and ETH slice bundles",
            data_path=args.data,
        )
        print("MEASUREMENT=UNTESTED reason=missing_BTC_or_ETH")
        return 0

    iv, summary = run_cross_asset_presliced(
        loaded.slice_bundles["BTC"],
        loaded.slice_bundles["ETH"],
        cfg,
        open_holdout=bool(args.open_holdout),
        conductor_order=conductor_order,
        research_only=loaded.research_only,
    )
    headline = aggregate_lab_verdict([iv])
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
        "cemetery_citations": CEM_CITATIONS,
        "cemetery_citation": CEM_CITATION_STR,
        "not_rescue_of_edge001": True,
        "not_rescue_of_edge003": True,
        "signal_module": "btc_lead_eth_response",
        "instruments": [
            {"instrument": iv.instrument, "verdict": iv.verdict, "reasons": iv.reasons}
        ],
        "metrics_summary": {
            "BTC_ETH": {
                "research": summary["research"],
                "research_mean_gross_bps": summary["research_mean_gross_bps"],
                "research_net_1x": summary["research_net_1x"],
                "research_net_2x": summary["research_net_2x"],
                "research_net_3x": summary["research_net_3x"],
                "validation": summary["validation"],
                "holdout": summary["holdout"],
                "controls": summary["controls"],
                "grid_p_stability": summary["grid_p_stability"],
                "C_base_[A]": summary["C_base_[A]"],
                "primary_cell": summary["primary_cell"],
                "validation_ran": summary["validation_ran"],
                "validation_skipped_because_research_fail": summary[
                    "validation_skipped_because_research_fail"
                ],
                "n_aligned_research": summary["n_aligned_research"],
            }
        },
        "assumptions_[A]": {
            "C_base_bps": cfg["costs_bps"]["C_base"],
            "r_t": "log_return",
            "kappa": primary_cell_kappa(cfg),
            "alignment": "inner_join_timestamp",
        },
        "non_claims": cfg.get("non_claims", []),
        "full_instrument_summaries": {"BTC_ETH": summary},
    }
    json_path, md_path = write_test_record(out_dir, record)

    stable_json = out_dir / f"{args.test_id}-{EDGE_ID}.json"
    stable_md = out_dir / f"{args.test_id}-{EDGE_ID}.md"
    with open(stable_json, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2, default=str)
        f.write("\n")
    # Richer markdown for archive
    rich_md = _rich_markdown(record, summary, headline)
    stable_md.write_text(rich_md, encoding="utf-8")
    # Also overwrite timestamped md with rich version
    md_path.write_text(rich_md, encoding="utf-8")

    print(f"MEASUREMENT={headline}")
    print(f"TEST_ID={args.test_id}")
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    print(f"Wrote {stable_json}")
    print(f"Wrote {stable_md}")
    print(f"cemetery_citations={CEM_CITATION_STR}")
    print(f"validation_ran={summary['validation_ran']}")
    return 0


def primary_cell_kappa(cfg: dict[str, Any]) -> float:
    return float(cfg["primary_cell"]["kappa"])


def _rich_markdown(record: dict[str, Any], summary: dict[str, Any], headline: str) -> str:
    r = summary["research"]
    ctrl = summary["controls"]
    lines = [
        f"# TEST record — {record.get('edge_id')}",
        "",
        f"**TEST_ID:** `{record.get('TEST_ID')}`",
        f"**MEASUREMENT / verdict:** `{headline}`",
        f"**Package:** `{record.get('package_id')}`",
        f"**Cemetery citations:** {CEM_CITATION_STR}",
        f"**Holdout:** `{record.get('holdout', 'SEALED')}`",
        f"**invented_numbers:** {record.get('invented_numbers')}",
        f"**VALIDATION ran:** {summary.get('validation_ran')}",
        "",
        "## Kill / verdict reasons",
    ]
    for iv in record.get("instruments", []):
        lines.append(f"### {iv.get('instrument')}: `{iv.get('verdict')}`")
        for reason in iv.get("reasons", []):
            lines.append(f"- {reason}")
        lines.append("")
    lines += [
        "## RESEARCH primary (BTC→ETH)",
        f"- n (signals): {r.get('signal_count')}",
        f"- distinct UTC days: {r.get('distinct_utc_days')}",
        f"- day concentration frac: {r.get('concentration_day_frac')}",
        f"- mean gross bps: {r.get('mean_gross_bps')}",
        f"- net@1×: {summary.get('research_net_1x')}",
        f"- net@2×: {summary.get('research_net_2x')}",
        f"- net@3×: {summary.get('research_net_3x')}",
        f"- hit rate: {r.get('hit_rate')}",
        f"- NW CI: [{r.get('nw_ci_low')}, {r.get('nw_ci_high')}]",
        f"- n_aligned_research bars: {summary.get('n_aligned_research')}",
        "",
        "## Controls",
        f"- Reverse ETH→BTC gross: {ctrl['reverse_ETH_to_BTC'].get('mean_gross_bps')} "
        f"(matches/beats={ctrl['reverse_ETH_to_BTC'].get('matches_or_beats_primary')})",
        f"- Timestamp shuffle gross: {ctrl['timestamp_shuffle_BTC_vs_ETH'].get('mean_gross_bps')} "
        f"(matches/beats={ctrl['timestamp_shuffle_BTC_vs_ETH'].get('matches_or_beats_primary')})",
        f"- κ ablation (diagnostic) gross: {ctrl['kappa_ablation_diagnostic'].get('mean_gross_bps')}",
        "",
        "## p-grid stability",
        f"```json\n{json.dumps(summary.get('grid_p_stability'), indent=2, default=str)}\n```",
        "",
        "## Primary cell",
        f"```json\n{json.dumps(summary.get('primary_cell'), indent=2)}\n```",
        "",
        "## Non-claims",
    ]
    for nc in record.get("non_claims", []):
        lines.append(f"- {nc}")
    lines.append("")
    lines.append("## Notes")
    lines.append("- All metrics from executed code only.")
    lines.append("- C_base=7.0 bps [A].")
    lines.append("- Cross-asset lead/lag — NOT a rescue of CEM-001 or CEM-002.")
    lines.append("- Sealed holdout never opened.")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    sys.exit(main())
