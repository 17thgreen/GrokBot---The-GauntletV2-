"""Load DATA-PROV-OI-001 Vision metrics zips.

REQUIRED: sort by create_time + dedupe identical within-file buckets before features.
Knowability: create_time <= decision t. Do not forward-fill gaps.
ETH OI absent before 2021-12-01 — do not invent.
Holdout: filter create_time_ms >= HOLDOUT_START_MS.
"""

from __future__ import annotations

import json
import zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

from .trades_loader import HOLDOUT_START_MS

ETH_OI_START_MS = int(pd.Timestamp("2021-12-01T00:00:00Z").timestamp() * 1000)


def write_oi_manifest(data_dir: Path, out_path: Path) -> Path:
    data_dir = Path(data_dir)
    manifest_path = data_dir / "MANIFEST.json"
    if not manifest_path.exists():
        body = {
            "DATASET_ID": "DATA-PROV-OI-001",
            "clock_verdict": "CONDITIONAL",
            "quality_status": "APPROVED_WITH_LIMITATIONS",
            "instruments": ["BTC", "ETH"],
            "transformations_required": ["sort_by_create_time", "dedupe_identical_buckets"],
            "comment": "Auto-written by oi_loader; Clock CONDITIONAL.",
        }
        manifest_path.write_text(json.dumps(body, indent=2) + "\n", encoding="utf-8")
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(manifest_path.read_text(encoding="utf-8"), encoding="utf-8")
    return manifest_path


def resolve_oi_clock(data_dir: Path) -> str:
    manifest = data_dir / "MANIFEST.json"
    if manifest.exists():
        body = json.loads(manifest.read_text(encoding="utf-8"))
        v = body.get("clock_verdict")
        if v:
            return str(v).strip().upper()
    verdict_md = data_dir / "provenance" / "DATA_VERDICT_DATA-PROV-OI-001.md"
    if verdict_md.exists() and "CONDITIONAL" in verdict_md.read_text(encoding="utf-8"):
        return "CONDITIONAL"
    return "MISSING"


def _parse_create_time(series: pd.Series) -> pd.Series:
    if pd.api.types.is_numeric_dtype(series):
        sample = float(series.dropna().iloc[0]) if series.dropna().size else 0.0
        unit = "ms" if sample > 1e12 else "s"
        return pd.to_datetime(series, unit=unit, utc=True)
    return pd.to_datetime(series, utc=True)


def _read_oi_zip(path: Path) -> pd.DataFrame:
    with zipfile.ZipFile(path) as zf:
        names = [n for n in zf.namelist() if n.endswith(".csv")]
        if not names:
            return pd.DataFrame()
        with zf.open(names[0]) as fh:
            df = pd.read_csv(fh)
    if df.empty:
        return df
    lower = {c.lower().strip(): c for c in df.columns}
    ct_col = lower.get("create_time") or ("create_time" if "create_time" in df.columns else None)
    oi_col = lower.get("sum_open_interest") or (
        "sum_open_interest" if "sum_open_interest" in df.columns else None
    )
    if ct_col is None or oi_col is None:
        raise ValueError(f"{path} missing create_time/sum_open_interest; have {list(df.columns)}")
    out = pd.DataFrame(
        {
            "create_time": _parse_create_time(df[ct_col]),
            "sum_open_interest": pd.to_numeric(df[oi_col], errors="coerce"),
        }
    )
    out = out.dropna(subset=["create_time", "sum_open_interest"])
    # Within-file SORT + DEDUPE identical buckets (Clock FLAG)
    out = out.sort_values("create_time")
    out = out.drop_duplicates(subset=["create_time"], keep="first")
    return out.reset_index(drop=True)


def sort_dedupe_oi(df: pd.DataFrame) -> pd.DataFrame:
    """Mandatory global sort + dedupe by create_time (keep first)."""
    out = df.sort_values("create_time").drop_duplicates(subset=["create_time"], keep="first")
    return out.reset_index(drop=True)


def load_oi_symbol(
    data_dir: Path,
    symbol: str,
    *,
    cache_dir: Optional[Path] = None,
    force_rebuild: bool = False,
    drop_holdout: bool = True,
    max_workers: int = 8,
) -> pd.DataFrame:
    """Load metrics zips; SORT+DEDUPE; expose create_time_ms + oi level."""
    data_dir = Path(data_dir)
    raw = data_dir / "raw" / symbol
    if not raw.is_dir():
        raise FileNotFoundError(f"OI raw dir missing: {raw}")

    cache_path = None
    if cache_dir is not None:
        cache_dir = Path(cache_dir)
        cache_dir.mkdir(parents=True, exist_ok=True)
        cache_path = cache_dir / f"{symbol}_oi.parquet"

    if cache_path is not None and cache_path.exists() and not force_rebuild:
        df = pd.read_parquet(cache_path)
    else:
        zips = sorted(raw.glob(f"{symbol}-metrics-*.zip"))
        if not zips:
            raise FileNotFoundError(f"No OI metrics zips under {raw}")
        frames: list[pd.DataFrame] = []
        with ThreadPoolExecutor(max_workers=max_workers) as ex:
            for part in ex.map(_read_oi_zip, zips):
                if part is not None and len(part):
                    frames.append(part)
        if not frames:
            raise FileNotFoundError(f"OI parse produced empty frame for {symbol}")
        df = sort_dedupe_oi(pd.concat(frames, ignore_index=True))
        df["create_time_ms"] = (
            df["create_time"].astype("int64") // 10**6
        ).astype("int64")
        df = df[["create_time", "create_time_ms", "sum_open_interest"]]
        if cache_path is not None:
            df.to_parquet(cache_path, index=False)

    if "create_time_ms" not in df.columns:
        df = df.copy()
        df["create_time_ms"] = (
            pd.to_datetime(df["create_time"], utc=True).astype("int64") // 10**6
        ).astype("int64")

    if symbol.startswith("ETH"):
        df = df.loc[df["create_time_ms"] >= ETH_OI_START_MS].reset_index(drop=True)

    if drop_holdout:
        df = df.loc[df["create_time_ms"] < HOLDOUT_START_MS].reset_index(drop=True)

    # Final safety sort+dedupe
    df = sort_dedupe_oi(df)
    if "create_time_ms" not in df.columns:
        df["create_time_ms"] = (
            pd.to_datetime(df["create_time"], utc=True).astype("int64") // 10**6
        ).astype("int64")
    return df.reset_index(drop=True)


def assert_oi_sorted_deduped(df: pd.DataFrame) -> None:
    ct = df["create_time_ms"].to_numpy() if "create_time_ms" in df.columns else None
    if ct is None:
        ct = (pd.to_datetime(df["create_time"], utc=True).astype("int64") // 10**6).to_numpy()
    if len(ct) and np.any(ct[1:] < ct[:-1]):
        raise AssertionError("OI create_time not sorted ascending")
    if len(ct) and np.any(ct[1:] == ct[:-1]):
        raise AssertionError("OI create_time has duplicates after dedupe")
