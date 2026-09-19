"""Load DATA-PROV manifests + OHLCV (CSV or parquet slices); refuse if Clock verdict not allowed.

Supports:
- Legacy contiguous CSV under dataset root (MANIFEST paths / btc_5m.csv)
- Pre-sliced parquet layout (DATA-PROV-001 style):
    slices/{SYMBOL}_5m_WARMUP_PREFIX.parquet
    slices/{SYMBOL}_5m_RESEARCH.parquet
    slices/{SYMBOL}_5m_VALIDATION.parquet
    sealed/  — LOCKED holdout; never opened unless explicitly allowed

Clock verdict from any of: MANIFEST.json (clock_verdict), CLOCK_VERDICT.json, clock_verdict.txt.
Missing / disallowed → UNTESTED (no invented metrics).
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

import pandas as pd

ALLOWED_VERDICTS = frozenset({"APPROVED", "CONDITIONAL"})
REQUIRED_OHLCV_COLS = ("timestamp", "open", "high", "low", "close", "volume")

# BTC/ETH package keys → on-disk Binance-style symbols
INSTRUMENT_SYMBOLS: dict[str, str] = {
    "BTC": "BTCUSDT",
    "ETH": "ETHUSDT",
    "BTCUSDT": "BTCUSDT",
    "ETHUSDT": "ETHUSDT",
}

# Timestamp column aliases → canonical "timestamp"
_TIMESTAMP_ALIASES = (
    "timestamp",
    "open_time",
    "open_time_ms",
    "open_time_us",
    "time",
    "datetime",
    "date",
)


@dataclass
class SliceBundle:
    """Pre-sliced OHLCV for one instrument. Holdout left unloaded by default."""

    warmup: pd.DataFrame
    research: pd.DataFrame
    validation: pd.DataFrame
    holdout: Optional[pd.DataFrame] = None
    holdout_file_present: bool = False
    symbol: str = ""


@dataclass
class DataLoadResult:
    ok: bool
    status: str  # READY | UNTESTED
    reason: str
    manifest: Optional[dict[str, Any]] = None
    frames: Optional[dict[str, pd.DataFrame]] = None  # contiguous mode: instrument -> OHLCV
    slice_bundles: Optional[dict[str, SliceBundle]] = None  # pre-sliced mode
    research_only: bool = False
    pre_sliced: bool = False
    clock_verdict: Optional[str] = None


def load_package_config(package_id: str, config_dir: Path) -> dict[str, Any]:
    path = config_dir / f"{package_id}.json"
    if not path.exists():
        raise FileNotFoundError(f"Package config not found: {path}")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def instrument_to_symbol(inst: str) -> str:
    key = str(inst).upper()
    if key in INSTRUMENT_SYMBOLS:
        return INSTRUMENT_SYMBOLS[key]
    # already a SYMBOLUSDT-like name
    return key


def _normalize_ohlcv(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize OHLCV columns; accept open_time_ms / open_time / timestamp variants."""
    lower_map = {c.lower().strip(): c for c in df.columns}
    rename: dict[str, str] = {}

    # timestamp
    ts_src = None
    for alias in _TIMESTAMP_ALIASES:
        if alias in lower_map:
            ts_src = lower_map[alias]
            break
        if alias.upper() in df.columns:
            ts_src = alias.upper()
            break
    if ts_src is None:
        raise ValueError(
            f"OHLCV missing timestamp-like column; have {list(df.columns)}"
        )
    rename[ts_src] = "timestamp"

    for need in ("open", "high", "low", "close", "volume"):
        if need in lower_map:
            rename[lower_map[need]] = need
        elif need.upper() in df.columns:
            rename[need.upper()] = need

    out = df.rename(columns=rename)
    missing = [c for c in REQUIRED_OHLCV_COLS if c not in out.columns]
    if missing:
        raise ValueError(f"OHLCV missing columns: {missing}")
    out = out[list(REQUIRED_OHLCV_COLS)].copy()

    ts = out["timestamp"]
    if pd.api.types.is_numeric_dtype(ts):
        # Heuristic: ms since epoch if values look like milliseconds
        sample = float(ts.dropna().iloc[0]) if len(ts.dropna()) else 0.0
        unit = "ms" if sample > 1e12 else ("us" if sample > 1e15 else "s")
        if sample > 1e15:
            unit = "us"
        elif sample > 1e12:
            unit = "ms"
        else:
            unit = "s"
        out["timestamp"] = pd.to_datetime(ts, unit=unit, utc=True)
    else:
        out["timestamp"] = pd.to_datetime(ts, utc=True)

    out = out.sort_values("timestamp").drop_duplicates(subset=["timestamp"], keep="first")
    out = out.reset_index(drop=True)
    for c in ("open", "high", "low", "close", "volume"):
        out[c] = pd.to_numeric(out[c], errors="coerce")
    out = out.dropna(subset=["close"]).reset_index(drop=True)
    return out


def _read_ohlcv_file(path: Path) -> pd.DataFrame:
    suffix = path.suffix.lower()
    if suffix == ".parquet":
        raw = pd.read_parquet(path)
    elif suffix in (".csv", ".txt"):
        raw = pd.read_csv(path)
    else:
        # try parquet then csv
        try:
            raw = pd.read_parquet(path)
        except Exception:
            raw = pd.read_csv(path)
    return _normalize_ohlcv(raw)


def resolve_clock_verdict(data_dir: Path) -> tuple[Optional[str], dict[str, Any]]:
    """Return (verdict_or_None, manifest_dict).

    Sources (first hit wins for verdict string; MANIFEST body always merged if present):
      1. MANIFEST.json → clock_verdict
      2. CLOCK_VERDICT.json → clock_verdict or verdict
      3. clock_verdict.txt → raw text
    """
    manifest: dict[str, Any] = {}
    verdict: Optional[str] = None

    manifest_path = data_dir / "MANIFEST.json"
    if manifest_path.exists():
        with open(manifest_path, encoding="utf-8") as f:
            manifest = json.load(f)
        if "clock_verdict" in manifest and manifest["clock_verdict"] is not None:
            verdict = str(manifest["clock_verdict"]).strip().upper()

    if verdict is None:
        cv_json = data_dir / "CLOCK_VERDICT.json"
        if cv_json.exists():
            with open(cv_json, encoding="utf-8") as f:
                body = json.load(f)
            if isinstance(body, dict):
                raw = body.get("clock_verdict", body.get("verdict"))
                if raw is not None:
                    verdict = str(raw).strip().upper()
                # merge non-conflicting keys into manifest for downstream
                for k, v in body.items():
                    manifest.setdefault(k, v)
            else:
                verdict = str(body).strip().upper()

    if verdict is None:
        cv_txt = data_dir / "clock_verdict.txt"
        if cv_txt.exists():
            verdict = cv_txt.read_text(encoding="utf-8").strip().splitlines()[0].strip().upper()

    return verdict, manifest


def detect_slice_layout(data_dir: Path) -> bool:
    """True if slices/ contains at least one *_RESEARCH.parquet."""
    slices = data_dir / "slices"
    if not slices.is_dir():
        return False
    return any(slices.glob("*_RESEARCH.parquet"))


def _slice_paths(data_dir: Path, symbol: str) -> dict[str, Path]:
    slices = data_dir / "slices"
    sealed = data_dir / "sealed"
    return {
        "warmup": slices / f"{symbol}_5m_WARMUP_PREFIX.parquet",
        "research": slices / f"{symbol}_5m_RESEARCH.parquet",
        "validation": slices / f"{symbol}_5m_VALIDATION.parquet",
        # holdout filename per SEAL_LOCK / on-disk convention
        "holdout": sealed / f"{symbol}_5m_HISTORICAL_HOLDOUT.parquet",
    }


def load_presliced_instrument(
    data_dir: Path,
    inst: str,
    *,
    load_holdout: bool = False,
) -> SliceBundle:
    """Load warmup/research/validation parquets. Never opens sealed/ unless load_holdout."""
    symbol = instrument_to_symbol(inst)
    paths = _slice_paths(data_dir, symbol)
    for key in ("warmup", "research", "validation"):
        if not paths[key].exists():
            raise FileNotFoundError(f"Missing {key} slice for {symbol}: {paths[key]}")

    warmup = _read_ohlcv_file(paths["warmup"])
    research = _read_ohlcv_file(paths["research"])
    validation = _read_ohlcv_file(paths["validation"])

    holdout_present = paths["holdout"].exists()
    holdout_df: Optional[pd.DataFrame] = None
    if load_holdout:
        if not holdout_present:
            raise FileNotFoundError(f"Holdout requested but missing: {paths['holdout']}")
        holdout_df = _read_ohlcv_file(paths["holdout"])

    return SliceBundle(
        warmup=warmup,
        research=research,
        validation=validation,
        holdout=holdout_df,
        holdout_file_present=holdout_present,
        symbol=symbol,
    )


def load_data_prov(
    data_dir: Optional[Path],
    cfg: dict[str, Any],
    *,
    open_holdout: bool = False,
    allow_load_holdout: bool = False,
) -> DataLoadResult:
    """Load DATA-PROV directory. Returns UNTESTED without crashing if missing/quarantined.

    allow_load_holdout: caller must set True only when --open-holdout AND Conductor
    order file exists. Even then sealed/ is loaded only if allow_load_holdout.
    """
    if data_dir is None:
        return DataLoadResult(
            ok=False,
            status="UNTESTED",
            reason="No --data path provided; awaiting DATA-PROV-* attachment",
        )
    data_dir = Path(data_dir)
    if not data_dir.exists():
        return DataLoadResult(
            ok=False,
            status="UNTESTED",
            reason=f"DATA path does not exist: {data_dir}",
        )

    verdict, manifest = resolve_clock_verdict(data_dir)
    if verdict is None:
        return DataLoadResult(
            ok=False,
            status="UNTESTED",
            reason=(
                f"Clock verdict missing under {data_dir} "
                "(need MANIFEST.json clock_verdict, CLOCK_VERDICT.json, or clock_verdict.txt)"
            ),
            manifest=manifest or None,
            clock_verdict=None,
        )

    allowed = set(cfg.get("clock_verdicts_allowed", list(ALLOWED_VERDICTS)))
    if verdict not in allowed:
        return DataLoadResult(
            ok=False,
            status="UNTESTED",
            reason=(
                f"Clock verdict={verdict} not in {sorted(allowed)}; "
                "runner refuses to invent metrics"
            ),
            manifest=manifest or None,
            clock_verdict=verdict,
        )

    research_only = bool(
        verdict == "CONDITIONAL"
        and (
            manifest.get("research_only", False)
            or manifest.get("conditional_research_only", False)
            or str(manifest.get("conditional_scope", "")).upper() == "RESEARCH_ONLY"
        )
    )

    instruments = manifest.get("instruments") or cfg.get("instruments", ["BTC", "ETH"])
    load_holdout = bool(allow_load_holdout and open_holdout and not research_only)

    # --- Pre-sliced parquet layout ---
    if detect_slice_layout(data_dir):
        bundles: dict[str, SliceBundle] = {}
        for inst in instruments:
            key = str(inst).upper()
            if key in ("BTCUSDT", "ETHUSDT"):
                key = "BTC" if key.startswith("BTC") else "ETH"
            try:
                bundles[key] = load_presliced_instrument(
                    data_dir, key, load_holdout=load_holdout
                )
            except Exception as e:  # noqa: BLE001 — surface as UNTESTED
                return DataLoadResult(
                    ok=False,
                    status="UNTESTED",
                    reason=f"Failed to load slices for {key}: {e}",
                    manifest=manifest or None,
                    clock_verdict=verdict,
                )
        return DataLoadResult(
            ok=True,
            status="READY",
            reason=f"Clock {verdict}; pre-sliced loaded {sorted(bundles.keys())}",
            manifest=manifest or None,
            slice_bundles=bundles,
            research_only=research_only,
            pre_sliced=True,
            clock_verdict=verdict,
        )

    # --- Legacy contiguous CSV / path_map ---
    path_map = manifest.get("paths") or {}
    frames: dict[str, pd.DataFrame] = {}
    for inst in instruments:
        key = str(inst).upper()
        rel = path_map.get(key) or path_map.get(inst) or f"{key.lower()}_5m.csv"
        csv_path = data_dir / rel
        if not csv_path.exists():
            symbol = instrument_to_symbol(key)
            alts = [
                data_dir / f"{key.lower()}_5m.csv",
                data_dir / f"{key}_5m.csv",
                data_dir / f"{symbol}_5m.csv",
                data_dir / "slices" / f"{symbol}_5m_RESEARCH.parquet",
            ]
            csv_path = next((p for p in alts if p.exists()), csv_path)
        if not csv_path.exists():
            return DataLoadResult(
                ok=False,
                status="UNTESTED",
                reason=f"OHLCV missing for {key}: expected {rel}",
                manifest=manifest or None,
                clock_verdict=verdict,
            )
        try:
            frames[key] = _read_ohlcv_file(csv_path)
        except Exception as e:  # noqa: BLE001 — surface as UNTESTED
            return DataLoadResult(
                ok=False,
                status="UNTESTED",
                reason=f"Failed to parse OHLCV for {key}: {e}",
                manifest=manifest or None,
                clock_verdict=verdict,
            )

    return DataLoadResult(
        ok=True,
        status="READY",
        reason=f"Clock {verdict}; loaded {sorted(frames.keys())}",
        manifest=manifest or None,
        frames=frames,
        research_only=research_only,
        pre_sliced=False,
        clock_verdict=verdict,
    )
