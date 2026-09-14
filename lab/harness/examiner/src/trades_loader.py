"""Stream Binance Vision UM aggTrades for DATA-PROV-TRADES-001.

Knowability: features at decision t use only trades with transact_time <= t.
Holdout: filter transact_time >= HOLDOUT_START_MS out of every analysis.
Aggressor: is_buyer_maker True -> SELL aggressor; False -> BUY aggressor.
"""

from __future__ import annotations

import io
import json
import zipfile
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Iterator, Optional

import numpy as np
import pandas as pd

# SEAL_LOCK holdout open_time first = 2025-07-14T15:05:00Z
# Decision close_time for that bar = open + 299999ms; we forbid ALL events
# with transact_time >= holdout open_time (conservative; matches Examiner order).
HOLDOUT_START_MS = int(
    datetime(2025, 7, 14, 15, 5, 0, tzinfo=timezone.utc).timestamp() * 1000
)
RESEARCH_OPEN_FIRST_MS = int(
    datetime(2021, 1, 3, 4, 0, 0, tzinfo=timezone.utc).timestamp() * 1000
)
VALIDATION_OPEN_LAST_MS = int(
    datetime(2025, 7, 14, 15, 0, 0, tzinfo=timezone.utc).timestamp() * 1000
)
BAR_MS = 300_000
CLOSE_OFFSET_MS = 299_999  # open_time + 299999 = close_time

AGG_COLS = [
    "agg_trade_id",
    "price",
    "quantity",
    "first_trade_id",
    "last_trade_id",
    "transact_time",
    "is_buyer_maker",
]


@dataclass(frozen=True)
class SealBounds:
    holdout_start_ms: int = HOLDOUT_START_MS
    research_open_first_ms: int = RESEARCH_OPEN_FIRST_MS
    validation_open_last_ms: int = VALIDATION_OPEN_LAST_MS


DEFAULT_SEALS = SealBounds()


def aggressor_side(is_buyer_maker) -> np.ndarray:
    """Return +1 BUY / -1 SELL aggressor from is_buyer_maker.

    True (buyer is maker) => aggressor SELL => -1
    False => aggressor BUY => +1
    """
    arr = np.asarray(is_buyer_maker)
    if arr.dtype == object or arr.dtype.kind in ("U", "S", "b"):
        # bool or string
        if arr.dtype == bool or arr.dtype.kind == "b":
            buy_maker = arr.astype(bool)
        else:
            s = pd.Series(arr).astype(str).str.lower()
            buy_maker = s.isin(["true", "1", "t", "yes"]).to_numpy()
    else:
        buy_maker = arr.astype(bool)
    side = np.where(buy_maker, -1, 1).astype(np.int8)
    return side


def close_time_from_open(open_time_ms: np.ndarray | int) -> np.ndarray | int:
    return open_time_ms + CLOSE_OFFSET_MS


def filter_pre_holdout(transact_time_ms: np.ndarray, holdout_start_ms: int = HOLDOUT_START_MS) -> np.ndarray:
    """Boolean mask: True where trade is allowed (strictly before holdout start)."""
    return np.asarray(transact_time_ms, dtype=np.int64) < int(holdout_start_ms)


def day_zip_path(raw_root: Path, symbol: str, day: date) -> Path:
    return raw_root / symbol / f"{day.isoformat()}.zip"


def iter_days(start: date, end: date) -> Iterator[date]:
    d = start
    while d <= end:
        yield d
        d += timedelta(days=1)


def _has_header(first_line: str) -> bool:
    low = first_line.lower()
    return "agg_trade_id" in low or "transact_time" in low


def read_day_aggtrades(
    zip_path: Path,
    *,
    holdout_start_ms: int = HOLDOUT_START_MS,
    columns: Optional[list[str]] = None,
) -> pd.DataFrame:
    """Read one daily Vision aggTrades zip; drop holdout-time rows.

    Returns columns: transact_time (int64 ms), price, quantity, is_buyer_maker (bool), side (+1/-1)
    Empty frame if file missing.
    """
    if not zip_path.exists():
        return pd.DataFrame(
            columns=["transact_time", "price", "quantity", "is_buyer_maker", "side"]
        )
    with zipfile.ZipFile(zip_path) as zf:
        names = [n for n in zf.namelist() if n.endswith(".csv")]
        if not names:
            raise ValueError(f"No CSV in {zip_path}")
        raw = zf.read(names[0])
    # Detect header
    head = raw[:200].decode("utf-8", errors="replace").split("\n", 1)[0]
    header = 0 if _has_header(head) else None
    usecols = [1, 2, 5, 6]  # price, quantity, transact_time, is_buyer_maker
    df = pd.read_csv(
        io.BytesIO(raw),
        header=header,
        names=AGG_COLS if header is None else None,
        usecols=usecols if header is None else ["price", "quantity", "transact_time", "is_buyer_maker"],
        dtype={
            "price": "float64",
            "quantity": "float64",
            "transact_time": "int64",
        },
        low_memory=False,
    )
    if header is not None:
        # ensure names
        df = df.rename(columns={c: c for c in df.columns})
        need = {"price", "quantity", "transact_time", "is_buyer_maker"}
        missing = need - set(df.columns)
        if missing:
            raise ValueError(f"Missing cols in {zip_path}: {missing}")
    # Normalize is_buyer_maker to bool
    ibm = df["is_buyer_maker"]
    if ibm.dtype != bool:
        if pd.api.types.is_numeric_dtype(ibm):
            df["is_buyer_maker"] = ibm.astype(int).astype(bool)
        else:
            df["is_buyer_maker"] = (
                ibm.astype(str).str.lower().isin(["true", "1", "t", "yes"])
            )
    df["transact_time"] = pd.to_numeric(df["transact_time"], errors="coerce").astype("int64")
    mask = filter_pre_holdout(df["transact_time"].to_numpy(), holdout_start_ms)
    df = df.loc[mask, ["transact_time", "price", "quantity", "is_buyer_maker"]].copy()
    df["side"] = aggressor_side(df["is_buyer_maker"].to_numpy())
    df = df.sort_values("transact_time").reset_index(drop=True)
    return df


def load_ohlcv_slices_no_holdout(
    ohlcv_root: Path,
    symbol: str,
) -> pd.DataFrame:
    """Load WARMUP+RESEARCH+VALIDATION only — never sealed holdout parquet."""
    slices = ohlcv_root / "slices"
    parts = []
    for tag in ("WARMUP_PREFIX", "RESEARCH", "VALIDATION"):
        p = slices / f"{symbol}_5m_{tag}.parquet"
        if not p.exists():
            raise FileNotFoundError(p)
        parts.append(pd.read_parquet(p))
    df = pd.concat(parts, ignore_index=True)
    df = df.sort_values("open_time_ms").drop_duplicates("open_time_ms").reset_index(drop=True)
    # Guard: no bar with open_time >= holdout start
    if (df["open_time_ms"] >= HOLDOUT_START_MS).any():
        df = df.loc[df["open_time_ms"] < HOLDOUT_START_MS].reset_index(drop=True)
    df["close_time_ms"] = df["open_time_ms"] + CLOSE_OFFSET_MS
    return df


def assert_no_holdout_trades(transact_time_ms: np.ndarray, holdout_start_ms: int = HOLDOUT_START_MS) -> None:
    if np.any(np.asarray(transact_time_ms) >= holdout_start_ms):
        raise AssertionError("Holdout-period trades present in analysis frame")


def write_trades_manifest(dataset_root: Path, clock_verdict: str = "CONDITIONAL") -> Path:
    """Write MANIFEST.json for DATA-PROV-TRADES-001."""
    manifest = {
        "DATASET_ID": "DATA-PROV-TRADES-001",
        "clock_verdict": clock_verdict,
        "QUALITY_STATUS": "APPROVED_WITH_LIMITATIONS",
        "source": "Binance Vision daily UM aggTrades",
        "symbols": ["BTCUSDT", "ETHUSDT"],
        "timestamp_definition": "transact_time exchange event ms UTC",
        "aggressor_semantics": {
            "is_buyer_maker_true": "SELL",
            "is_buyer_maker_false": "BUY",
        },
        "seal_alignment": "timestamp-aligned to DATA-PROV-001 SEAL_LOCK",
        "holdout_start_utc": "2025-07-14T15:05:00Z",
        "holdout_start_ms": HOLDOUT_START_MS,
        "research_open_first_utc": "2021-01-03T04:00:00Z",
        "validation_open_last_utc": "2025-07-14T15:00:00Z",
        "distinct_from": "DATA-PROV-001",
        "l2_proxy": False,
        "evidence_tag": "[V] Clock CONDITIONAL 2026-09-11",
        "derived_cache_tag": "[A]",
    }
    path = dataset_root / "MANIFEST.json"
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return path
