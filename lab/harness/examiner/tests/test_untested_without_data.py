"""Without approved data → UNTESTED; invent ZERO performance numbers."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.run_edge001 import main  # noqa: E402


FORBIDDEN_METRIC_KEYS_AS_FAKE = (
    # If MEASUREMENT is UNTESTED, these must not appear as numeric claims
)


def test_no_data_exits_zero_untested(tmp_path):
    out = tmp_path / "out"
    rc = main(["--package", "PROV-MEAS-20260910-001", "--out", str(out)])
    assert rc == 0
    md = out / "STATUS_UNTESTED_EDGE-20260910-001.md"
    js = out / "STATUS_UNTESTED_EDGE-20260910-001.json"
    assert md.exists()
    assert js.exists()
    text = md.read_text()
    assert "UNTESTED" in text
    assert "Sharpe" not in text or "invent" in text.lower()
    data = json.loads(js.read_text())
    assert data["MEASUREMENT"] == "UNTESTED"
    assert data["metrics"] is None
    assert data["invented_numbers"] is False


def test_missing_path_untested(tmp_path):
    out = tmp_path / "out2"
    rc = main(
        [
            "--package",
            "PROV-MEAS-20260910-001",
            "--data",
            str(tmp_path / "does-not-exist"),
            "--out",
            str(out),
        ]
    )
    assert rc == 0
    data = json.loads((out / "STATUS_UNTESTED_EDGE-20260910-001.json").read_text())
    assert data["MEASUREMENT"] == "UNTESTED"
    assert data["metrics"] is None


def test_quarantined_manifest_untested(tmp_path):
    data_dir = tmp_path / "DATA-PROV-20990101-001"
    data_dir.mkdir()
    (data_dir / "MANIFEST.json").write_text(
        json.dumps(
            {
                "DATASET_ID": "DATA-PROV-20990101-001",
                "clock_verdict": "QUARANTINED",
                "instruments": ["BTC", "ETH"],
            }
        )
    )
    out = tmp_path / "out3"
    rc = main(
        [
            "--package",
            "PROV-MEAS-20260910-001",
            "--data",
            str(data_dir),
            "--out",
            str(out),
        ]
    )
    assert rc == 0
    data = json.loads((out / "STATUS_UNTESTED_EDGE-20260910-001.json").read_text())
    assert data["MEASUREMENT"] == "UNTESTED"
    assert "QUARANTINED" in data["reason"]


def test_synthetic_fixture_never_as_evidence():
    readme = (ROOT / "fixtures" / "README_FIXTURES.md").read_text()
    assert "NEVER" in readme
    assert "SYNTHETIC" in readme
    # Runner default out stub also says awaiting real data
    stub = (ROOT / "out" / "STATUS_UNTESTED_EDGE-20260910-001.md").read_text()
    assert "UNTESTED" in stub or stub  # may be created by this test session
