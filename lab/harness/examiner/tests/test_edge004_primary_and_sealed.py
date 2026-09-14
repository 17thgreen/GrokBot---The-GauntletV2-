"""EDGE-004: primary lock; sealed never opened; reverse control; cemetery cites."""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path
from unittest import mock

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data_loader import load_data_prov  # noqa: E402
from src.run_edge004 import main, primary_cell_is_locked  # noqa: E402
from src.signal_edge004 import build_eth_to_btc_reverse  # noqa: E402
from src.verdict_edge004 import evaluate_edge004, matches_or_beats_within_ci  # noqa: E402

FIXTURE = ROOT / "fixtures" / "mock_slice_layout"
CFG_PATH = ROOT / "config" / "PROV-MEAS-EDGE-004.json"


def test_locked_config_has_primary_and_cemeteries():
    cfg = json.loads(CFG_PATH.read_text())
    assert cfg["primary_cell"] is not None
    assert cfg["primary_cell_status"] == "LOCKED"
    assert primary_cell_is_locked(cfg)
    assert cfg["primary_cell"]["p"] == 0.90
    assert cfg["primary_cell"]["L"] == 288
    assert cfg["primary_cell"]["h"] == 1
    assert cfg["primary_cell"]["kappa"] == 0.50
    cites = cfg.get("cemetery_citations", [])
    assert "CEM-20260910-001" in cites
    assert "CEM-20260910-002" in cites


def test_refuse_without_primary_cell(tmp_path):
    cfg = json.loads(CFG_PATH.read_text())
    cfg["primary_cell"] = None
    cfg["primary_cell_status"] = "PENDING_STATISTICIAN_LOCK"
    cfg["package_id"] = "PROV-MEAS-EDGE-004-UNLOCKED"
    dest = ROOT / "config" / "PROV-MEAS-EDGE-004-UNLOCKED.json"
    dest.write_text(json.dumps(cfg, indent=2))
    try:
        out = tmp_path / "out"
        rc = main(
            [
                "--package",
                "PROV-MEAS-EDGE-004-UNLOCKED",
                "--data",
                str(FIXTURE),
                "--out",
                str(out),
            ]
        )
        assert rc == 0
        js = out / "STATUS_PENDING_PRIMARY_CELL_EDGE-20260910-004.json"
        assert js.exists()
        data = json.loads(js.read_text())
        assert data["MEASUREMENT"] == "BLOCKED_PENDING_PRIMARY_CELL"
        assert data["verdict"] == "UNTESTED"
        assert data["metrics"] is None
        assert data["invented_numbers"] is False
        assert "CEM-20260910-001" in data.get("cemetery_citations", [])
        assert "CEM-20260910-002" in data.get("cemetery_citations", [])
    finally:
        if dest.exists():
            dest.unlink()


def test_no_data_untested_when_locked(tmp_path):
    out = tmp_path / "out"
    rc = main(["--package", "PROV-MEAS-EDGE-004", "--out", str(out)])
    assert rc == 0
    js = out / "STATUS_UNTESTED_EDGE-20260910-004.json"
    assert js.exists()
    data = json.loads(js.read_text())
    assert data["MEASUREMENT"] == "UNTESTED"
    assert data["metrics"] is None


def test_edge004_load_never_opens_sealed(tmp_path):
    data = tmp_path / "DATA-MOCK-004"
    shutil.copytree(FIXTURE, data)
    (data / "CLOCK_VERDICT.json").write_text(
        json.dumps({"clock_verdict": "APPROVED", "DATASET_ID": "DATA-MOCK-004"})
    )
    cfg = {
        "instruments": ["BTC", "ETH"],
        "clock_verdicts_allowed": ["APPROVED", "CONDITIONAL"],
        "warmup_bars": 8,
    }
    opened: list[Path] = []
    real_read_parquet = pd.read_parquet

    def tracking_read_parquet(path, *args, **kwargs):
        p = Path(path)
        opened.append(p.resolve())
        if "sealed" in p.parts and p.suffix == ".parquet":
            raise AssertionError(f"sealed parquet opened: {p}")
        return real_read_parquet(path, *args, **kwargs)

    with mock.patch("pandas.read_parquet", side_effect=tracking_read_parquet):
        result = load_data_prov(
            data, cfg, open_holdout=False, allow_load_holdout=False
        )
    assert result.ok is True
    for p in opened:
        assert "sealed" not in p.parts


def test_reverse_matches_helper():
    assert matches_or_beats_within_ci(2.0, 3.0, 1.0, 2.5) is True  # inside CI
    assert matches_or_beats_within_ci(2.0, 5.0, 1.5, 2.5) is True  # beats
    assert matches_or_beats_within_ci(None, 1.0, 0, 1) is None
    assert matches_or_beats_within_ci(2.0, 0.5, 1.5, 2.5) is False


def test_verdict_fail_gross():
    v = evaluate_edge004(
        signal_count=500,
        distinct_utc_days=50,
        mean_gross_bps=-0.1,
        net_1x=-7.1,
        net_2x=-14.1,
        net_3x=-21.1,
        concentration_frac=0.4,
        p_grid_keep_sign_count=3,
        reverse_matches_or_beats=False,
        shuffle_matches_or_beats=False,
        gates={
            "research_signals": 200,
            "research_distinct_utc_days": 20,
            "concentration_kill_frac": 0.05,
            "grid_p_stability_min_keep_sign": 2,
        },
    )
    assert v.verdict == "FAIL"
    assert any("gross" in r for r in v.reasons)


def test_verdict_fail_reverse():
    v = evaluate_edge004(
        signal_count=500,
        distinct_utc_days=50,
        mean_gross_bps=10.0,
        net_1x=3.0,
        net_2x=-4.0,
        net_3x=-11.0,
        concentration_frac=0.4,
        p_grid_keep_sign_count=3,
        reverse_matches_or_beats=True,
        shuffle_matches_or_beats=False,
        gates={
            "research_signals": 200,
            "research_distinct_utc_days": 20,
            "concentration_kill_frac": 0.05,
            "grid_p_stability_min_keep_sign": 2,
        },
    )
    assert v.verdict == "FAIL"
    assert any("reverse" in r.lower() for r in v.reasons)
