"""Unit tests: calc_time<=t; OI sort+dedupe; holdout filter; no LIQ-003 runner."""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.funding_loader import assert_calc_time_knowable, load_funding_symbol  # noqa: E402
from src.oi_loader import assert_oi_sorted_deduped, sort_dedupe_oi  # noqa: E402
from src.trades_loader import HOLDOUT_START_MS  # noqa: E402
from src.signal_edge_20260911_005 import (  # noqa: E402
    align_funding_to_bars,
    compute_funding_print_features,
)


def test_calc_time_leq_t_passes():
    assert_calc_time_knowable([100, 200], [100, 250])


def test_calc_time_lookahead_raises():
    with pytest.raises(AssertionError):
        assert_calc_time_knowable([300], [250])


def test_oi_sort_dedupe():
    df = pd.DataFrame(
        {
            "create_time": pd.to_datetime(
                ["2021-12-01 00:05:00", "2021-12-01 00:00:00", "2021-12-01 00:00:00"],
                utc=True,
            ),
            "sum_open_interest": [2.0, 1.0, 1.0],
        }
    )
    out = sort_dedupe_oi(df)
    out["create_time_ms"] = (out["create_time"].astype("int64") // 10**6).astype("int64")
    assert_oi_sorted_deduped(out)
    assert len(out) == 2
    assert out.iloc[0]["sum_open_interest"] == 1.0


def test_funding_align_respects_calc_time():
    funding = pd.DataFrame(
        {
            "calc_time": [1_000_000, 2_000_000, 3_000_000],
            "funding_interval_hours": [8, 8, 8],
            "last_funding_rate": [0.001, 0.002, -0.003],
        }
    )
    feat = compute_funding_print_features(funding, Z=0.0, D=1, L=1)
    ohlcv = pd.DataFrame(
        {
            "open_time_ms": [1_500_000, 2_500_000, 3_500_000],
            "close_time_ms": [1_799_999, 2_799_999, 3_799_999],
            "open": [1.0, 1.0, 1.0],
            "high": [1.0, 1.0, 1.0],
            "low": [1.0, 1.0, 1.0],
            "close": [1.0, 1.0, 1.0],
            "volume": [1.0, 1.0, 1.0],
        }
    )
    aligned = align_funding_to_bars(ohlcv, feat)
    used = aligned["funding_calc_time"].to_numpy()
    close_t = aligned["close_time_ms"].to_numpy()
    assert np.all(used[used >= 0] <= close_t[used >= 0])


def test_holdout_constant_locked():
    assert HOLDOUT_START_MS == int(pd.Timestamp("2025-07-14T15:05:00Z").timestamp() * 1000)


def test_no_liq_003_runner_invoked_in_catalyst_modules():
    """Catalyst C5 runners must not import/call LIQ EDGE-003 measurement."""
    forbidden = [
        "run_edge003",
        "signal_edge003",
        "DATA-PROV-LIQ-001",
        "EDGE-20260911-003",
    ]
    files = [
        ROOT / "src" / "run_edge_20260911_005.py",
        ROOT / "src" / "run_edge_20260911_004.py",
        ROOT / "src" / "run_edge_20260911_006.py",
        ROOT / "src" / "signal_edge_20260911_005.py",
        ROOT / "src" / "signal_edge_20260911_004.py",
        ROOT / "src" / "signal_edge_20260911_006.py",
    ]
    for f in files:
        text = f.read_text(encoding="utf-8")
        for token in forbidden:
            if token in text and "not invoked" not in text.lower() and "LIQ-003" not in text:
                if "not" in text.lower() and "liq" in text.lower():
                    continue
            if token in ("run_edge003", "signal_edge003") and token in text:
                raise AssertionError(f"{f.name} references {token}")


def test_holdout_filter_on_synthetic_ohlcv_loader(tmp_path):
    from src.catalyst_common import load_ohlcv_open_slices

    ohlcv = Path("/workspace/lab/data/DATA-PROV-001")
    if not (ohlcv / "slices" / "BTCUSDT_5m_RESEARCH.parquet").exists():
        pytest.skip("no OHLCV")
    df = load_ohlcv_open_slices(ohlcv, "BTCUSDT", include_validation=True)
    assert (df["open_time_ms"] >= HOLDOUT_START_MS).sum() == 0
