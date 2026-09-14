"""Write TEST record JSON + Markdown. Never invent performance numbers."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def write_untested_report(
    out_dir: Path,
    *,
    package_id: str,
    edge_id: str,
    reason: str,
    data_path: Optional[str] = None,
) -> tuple[Path, Path]:
    """MEASUREMENT=UNTESTED — zero fabricated metrics."""
    out_dir.mkdir(parents=True, exist_ok=True)
    record = {
        "TEST_ID": None,
        "package_id": package_id,
        "edge_id": edge_id,
        "MEASUREMENT": "UNTESTED",
        "verdict": "UNTESTED",
        "reason": reason,
        "data_path": data_path,
        "metrics": None,
        "invented_numbers": False,
        "holdout": "SEALED",
        "generated_utc": _utc_now(),
        "non_claims": [
            "OHLCV test does NOT validate OF mechanism",
            "No performance numbers invented without approved DATA-PROV",
        ],
    }
    json_path = out_dir / f"STATUS_UNTESTED_{edge_id}.json"
    md_path = out_dir / f"STATUS_UNTESTED_{edge_id}.md"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2)
        f.write("\n")
    md = f"""# MEASUREMENT = UNTESTED — {edge_id}

**Package:** `{package_id}`  
**Generated (UTC):** {_utc_now()}  
**Verdict:** UNTESTED

## Reason
{reason}

## Rules honored
- No Sharpe / return / trade-count figures invented.
- Holdout remains SEALED.
- Awaiting DATA-PROV-* with Clock verdict APPROVED or CONDITIONAL.

## Data path
`{data_path or "(none)"}`

## Non-claims
- OHLCV conditional-return test does **not** validate the order-flow (OF) mechanism story.
- Provisional economics remain **[A]** assumptions until venue lock.
"""
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)
    return json_path, md_path


def write_test_record(
    out_dir: Path,
    record: dict[str, Any],
) -> tuple[Path, Path]:
    """Persist full TEST JSON + human MD. Caller supplies only code-measured fields."""
    out_dir.mkdir(parents=True, exist_ok=True)
    edge_id = record.get("edge_id", "EDGE-UNKNOWN")
    stamp = _utc_now().replace(":", "").replace("-", "")[:15]
    measurement = record.get("MEASUREMENT") or record.get("verdict", "UNKNOWN")
    json_path = out_dir / f"TEST_{edge_id}_{measurement}_{stamp}.json"
    md_path = out_dir / f"TEST_{edge_id}_{measurement}_{stamp}.md"
    record = dict(record)
    record.setdefault("generated_utc", _utc_now())
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2, default=str)
        f.write("\n")

    lines = [
        f"# TEST record — {edge_id}",
        "",
        f"**MEASUREMENT / verdict:** `{measurement}`",
        f"**Package:** `{record.get('package_id')}`",
        f"**Generated (UTC):** {record.get('generated_utc')}",
        f"**Holdout:** `{record.get('holdout', 'SEALED')}`",
        "",
        "## Per-instrument verdicts",
    ]
    for iv in record.get("instruments", []):
        lines.append(f"### {iv.get('instrument')}")
        lines.append(f"- Verdict: `{iv.get('verdict')}`")
        for r in iv.get("reasons", []):
            lines.append(f"- {r}")
        lines.append("")
    lines.append("## Notes")
    lines.append("- All metrics from executed code only.")
    lines.append("- Evidence tag on C_base=7bps and ε thresholds: **[A]**.")
    lines.append("- OF mechanism is **NOT** validated by this OHLCV harness.")
    if record.get("metrics_summary"):
        lines.append("")
        lines.append("## Metrics summary (code-measured)")
        lines.append("```json")
        lines.append(json.dumps(record["metrics_summary"], indent=2, default=str))
        lines.append("```")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return json_path, md_path
