"""Load DATA-PROV-FUNDING-001 Vision fundingRate zips.

Knowability: SIGNAL may use last_funding_rate only if calc_time <= decision t.
Forbidden: premiumIndex / predicted funding.
Holdout: filter calc_time >= HOLDOUT_START_MS out of analysis frames.
"""

from __future__ import annotations

import json
import zipfile
from pathlib import Path
from typing import Any, Optional

import pandas as pd

from .trades_loader import HOLDOUT_START_MS

FUNDING_COLS = ("calc_time", "funding_interval_hours", "last_funding_rate")


def write_funding_manifest(data_dir: Path, out_path: Path) -> Path:
    """Ensure MANIFEST.json exists with clock_verdict=CONDITIONAL if missing."""
    data_dir = Path(data_dir)
    manifest_path = data_dir / "MANIFEST.json"
    if not manifest_path.exists():
        body = {
            "DATASET_ID": "DATA-PROV-FUNDING-001",
            "clock_verdict": "CONDITIONAL",
            "quality_status": "APPROVED_WITH_LIMITATIONS",
            "instruments": ["BTC", "ETH"],
            "comment": "Auto-written by funding_loader; Clock CONDITIONAL.",
        }
        manifest_path.write_text(json.dumps(body, indent=2) + "\n", encoding="utf-8")
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(manifest_path.read_text(encoding="utf-8"), encoding="utf-8")
    return manifest_path


def resolve_funding_clock(data_dir: Path) -> str:
    manifest = data_dir / "MANIFEST.json"
    if manifest.exists():
        body = json.loads(manifest.read_text(encoding="utf-8"))
        v = body.get("clock_verdict")
        if v:
            return str(v).strip().upper()
    verdict_md = data_dir / "provenance" / "DATA_VERDICT_DATA-PROV-FUNDING-001.md"
    if verdict_md.exists():
        text = verdict_md.read_text(encoding="utf-8")
        if "CONDITIONAL" in text:
            return "CONDITIONAL"
    return "MISSING"


def _read_funding_zip(path: Path) -> pd.DataFrame:
    with zipfile.ZipFile(path) as zf:
        names = [n for n in zf.namelist() if n.endswith(".csv")]
        if not names:
            raise ValueError(f"No CSV in {path}")
        with zf.open(names[0]) as fh:
            df = pd.read_csv(fh)
    lower = {c.lower().strip(): c for c in df.columns}
    rename = {}
    for need in FUNDING_COLS:
        if need in lower:
            rename[lower[need]] = need
        elif need in df.columns:
            rename[need] = need
    df = df.rename(columns=rename)
    missing = [c for c in FUNDING_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"{path} missing cols {missing}; have {list(df.columns)}")
    out = df[list(FUNDING_COLS)].copy()
    out["calc_time"] = pd.to_numeric(out["calc_time"], errors="coerce").astype("int64")
    out["funding_interval_hours"] = pd.to_numeric(
        out["funding_interval_hours"], errors="coerce"
    )
    out["last_funding_rate"] = pd.to_numeric(out["last_funding_rate"], errors="coerce")
    return out.dropna(subset=["calc_time", "last_funding_rate"])


def load_funding_symbol(
    data_dir: Path,
    symbol: str,
    *,
    cache_dir: Optional[Path] = None,
    force_rebuild: bool = False,
    drop_holdout: bool = True,
) -> pd.DataFrame:
    """Load all monthly fundingRate zips for symbol; sort + dedupe by calc_time."""
    data_dir = Path(data_dir)
    raw = data_dir / "raw" / symbol
    if not raw.is_dir():
        raise FileNotFoundError(f"Funding raw dir missing: {raw}")

    cache_path = None
    if cache_dir is not None:
        cache_dir = Path(cache_dir)
        cache_dir.mkdir(parents=True, exist_ok=True)
        cache_path = cache_dir / f"{symbol}_funding.parquet"

    if cache_path is not None and cache_path.exists() and not force_rebuild:
        df = pd.read_parquet(cache_path)
    else:
        frames = []
        for zp in sorted(raw.glob(f"{symbol}-fundingRate-*.zip")):
            frames.append(_read_funding_zip(zp))
        if not frames:
            raise FileNotFoundError(f"No funding zips under {raw}")
        df = pd.concat(frames, ignore_index=True)
        df = df.sort_values("calc_time").drop_duplicates(subset=["calc_time"], keep="first")
        df = df.reset_index(drop=True)
        if cache_path is not None:
            df.to_parquet(cache_path, index=False)

    if drop_holdout:
        df = df.loc[df["calc_time"] < HOLDOUT_START_MS].reset_index(drop=True)
    return df


def assert_calc_time_knowable(calc_times: Any, decision_t: Any) -> None:
    """Raise if any funding calc_time used exceeds decision t."""
    import numpy as np

    ct = np.asarray(calc_times, dtype=np.int64)
    dt = np.asarray(decision_t, dtype=np.int64)
    if ct.size == 0:
        return
    if dt.ndim == 0:
        if np.any(ct > int(dt)):
            raise AssertionError("funding calc_time > decision t (lookahead)")
        return
    if ct.shape != dt.shape:
        # pairwise max check: all calc <= corresponding decision
        if len(ct) != len(dt):
            raise AssertionError("calc_time/decision length mismatch")
    if np.any(ct > dt):
        raise AssertionError("funding calc_time > decision t (lookahead)")
