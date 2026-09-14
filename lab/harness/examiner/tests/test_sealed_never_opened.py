"""Pre-sliced layout: sealed/ parquet must never be opened by default."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest import mock

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data_loader import (  # noqa: E402
    detect_slice_layout,
    load_data_prov,
    load_presliced_instrument,
    resolve_clock_verdict,
)
from src.splits import bounds_from_presliced, research_time_halves  # noqa: E402

FIXTURE = ROOT / "fixtures" / "mock_slice_layout"
CFG = {
    "instruments": ["BTC", "ETH"],
    "clock_verdicts_allowed": ["APPROVED", "CONDITIONAL"],
    "warmup_bars": 8,
}


def test_fixture_is_slice_layout():
    assert detect_slice_layout(FIXTURE)


def test_resolve_clock_missing_on_fixture():
    verdict, _ = resolve_clock_verdict(FIXTURE)
    assert verdict is None


def test_load_without_verdict_untested_and_skips_sealed():
    opened: list[str] = []
    real_read_parquet = pd.read_parquet

    def tracking_read_parquet(path, *args, **kwargs):
        opened.append(str(path))
        return real_read_parquet(path, *args, **kwargs)

    with mock.patch("pandas.read_parquet", side_effect=tracking_read_parquet):
        result = load_data_prov(FIXTURE, CFG)
    assert result.ok is False
    assert result.status == "UNTESTED"
    assert "Clock verdict missing" in result.reason
    # Must not open any parquet (including sealed) when verdict missing
    assert opened == []


def test_presliced_load_never_opens_sealed_by_default(tmp_path):
    # Copy fixture layout and add APPROVED clock verdict
    import shutil

    data = tmp_path / "DATA-MOCK-001"
    shutil.copytree(FIXTURE, data)
    (data / "CLOCK_VERDICT.json").write_text(
        json.dumps({"clock_verdict": "APPROVED", "DATASET_ID": "DATA-MOCK-001"})
    )

    opened: list[Path] = []
    real_read_parquet = pd.read_parquet

    def tracking_read_parquet(path, *args, **kwargs):
        p = Path(path)
        opened.append(p.resolve())
        # Fail loud if sealed holdout parquet is touched
        if "sealed" in p.parts and p.suffix == ".parquet":
            raise AssertionError(f"sealed parquet opened: {p}")
        return real_read_parquet(path, *args, **kwargs)

    with mock.patch("pandas.read_parquet", side_effect=tracking_read_parquet):
        result = load_data_prov(
            data, CFG, open_holdout=False, allow_load_holdout=False
        )

    assert result.ok is True
    assert result.pre_sliced is True
    assert result.slice_bundles is not None
    assert set(result.slice_bundles.keys()) == {"BTC", "ETH"}
    for bund in result.slice_bundles.values():
        assert bund.holdout is None
        assert bund.holdout_file_present is True
        assert len(bund.warmup) == 8
        assert len(bund.research) == 20
        assert len(bund.validation) == 10

    for p in opened:
        assert "sealed" not in p.parts, f"opened under sealed/: {p}"

    # Sentinel text file also must not have been read
    sentinel = data / "sealed" / "DO_NOT_OPEN.txt"
    assert sentinel.exists()


def test_load_presliced_instrument_default_skips_holdout():
    opened: list[str] = []
    real_read_parquet = pd.read_parquet

    def tracking_read_parquet(path, *args, **kwargs):
        opened.append(str(path))
        p = Path(path)
        if "sealed" in p.parts and p.suffix == ".parquet":
            raise AssertionError(f"sealed parquet opened: {p}")
        return real_read_parquet(path, *args, **kwargs)

    with mock.patch("pandas.read_parquet", side_effect=tracking_read_parquet):
        bund = load_presliced_instrument(FIXTURE, "BTC", load_holdout=False)
    assert bund.holdout is None
    assert bund.symbol == "BTCUSDT"
    assert all("sealed" not in x for x in opened)


def test_bounds_from_presliced_no_resplit():
    b = bounds_from_presliced(n_warmup=8, n_research=20, n_validation=10, n_holdout=0)
    assert b.pre_sliced is True
    assert b.warmup_end == 8
    assert b.research_end - b.research_start == 20
    assert b.validation_end - b.validation_start == 10
    h1, h2 = research_time_halves(20)
    assert h1 + h2 == 20
    assert h1 == 10


def test_btc_eth_symbol_mapping(tmp_path):
    import shutil

    data = tmp_path / "DATA-MOCK-002"
    shutil.copytree(FIXTURE, data)
    (data / "clock_verdict.txt").write_text("APPROVED\n")
    result = load_data_prov(data, CFG)
    assert result.ok
    assert "BTC" in result.slice_bundles
    assert result.slice_bundles["BTC"].symbol == "BTCUSDT"
    assert result.slice_bundles["ETH"].symbol == "ETHUSDT"
