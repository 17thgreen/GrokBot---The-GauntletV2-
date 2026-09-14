"""EDGE-003: refuse without primary; sealed never opened; reuse fixtures."""

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
from src.run_edge003 import main, primary_cell_is_locked  # noqa: E402

FIXTURE = ROOT / "fixtures" / "mock_slice_layout"
CFG_PATH = ROOT / "config" / "PROV-MEAS-EDGE-003.json"


def test_locked_config_has_primary():
    cfg = json.loads(CFG_PATH.read_text())
    assert cfg["primary_cell"] is not None
    assert cfg["primary_cell_status"] == "LOCKED"
    assert primary_cell_is_locked(cfg)
    assert cfg["primary_cell"]["p"] == 0.95
    assert cfg["primary_cell"]["L"] == 288
    assert cfg["primary_cell"]["h"] == 1
    assert "CEM-20260910-001" in cfg.get("cemetery_citation", "")


def test_refuse_without_primary_cell(tmp_path):
    cfg = json.loads(CFG_PATH.read_text())
    cfg["primary_cell"] = None
    cfg["primary_cell_status"] = "PENDING_STATISTICIAN_LOCK"
    cfg["package_id"] = "PROV-MEAS-EDGE-003-UNLOCKED"
    unlocked = tmp_path / "PROV-MEAS-EDGE-003-UNLOCKED.json"
    dest = ROOT / "config" / "PROV-MEAS-EDGE-003-UNLOCKED.json"
    dest.write_text(json.dumps(cfg, indent=2))
    try:
        out = tmp_path / "out"
        rc = main(
            [
                "--package",
                "PROV-MEAS-EDGE-003-UNLOCKED",
                "--data",
                str(FIXTURE),
                "--out",
                str(out),
            ]
        )
        assert rc == 0
        js = out / "STATUS_PENDING_PRIMARY_CELL_EDGE-20260910-003.json"
        assert js.exists()
        data = json.loads(js.read_text())
        assert data["MEASUREMENT"] == "BLOCKED_PENDING_PRIMARY_CELL"
        assert data["verdict"] == "UNTESTED"
        assert data["metrics"] is None
        assert data["invented_numbers"] is False
    finally:
        if dest.exists():
            dest.unlink()


def test_no_data_untested_when_locked(tmp_path):
    out = tmp_path / "out"
    rc = main(["--package", "PROV-MEAS-EDGE-003", "--out", str(out)])
    assert rc == 0
    js = out / "STATUS_UNTESTED_EDGE-20260910-003.json"
    assert js.exists()
    data = json.loads(js.read_text())
    assert data["MEASUREMENT"] == "UNTESTED"
    assert data["metrics"] is None


def test_edge003_load_never_opens_sealed(tmp_path):
    data = tmp_path / "DATA-MOCK-003"
    shutil.copytree(FIXTURE, data)
    (data / "CLOCK_VERDICT.json").write_text(
        json.dumps({"clock_verdict": "APPROVED", "DATASET_ID": "DATA-MOCK-003"})
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


def test_fixture_reuse_labeled_synthetic():
    label = (ROOT / "fixtures" / "README_FIXTURES.md").read_text()
    assert "SYNTHETIC" in label
    assert "NEVER" in label
