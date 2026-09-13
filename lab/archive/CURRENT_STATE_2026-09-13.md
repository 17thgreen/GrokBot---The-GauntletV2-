# Current state — 2026-09-13 (persisted for GitHub review)

**Not a strategy.** **Not a stamp.** Reconstructs what a reviewer of `main` could not see at `754c73f`.

| Item | State |
|------|--------|
| Incumbent | `MKT-KALSHI-15M-MID` · TEST-20260911-007 `BASELINE_MEASURED` |
| F1 | TEST-20260912-002 `REDUNDANT / FAIL-INSUFFICIENT` · cards INACTIVE |
| F3 | TEST-20260912-001 `REDUNDANT / FAIL-INSUFFICIENT` · cards INACTIVE |
| DATA-PROV-CF-001 | **CLEARED** 2026-09-13T17:53:52Z · 1208/1208 close minutes 60/60 · raw ticks **not** in this repo |
| F2 / FEAT-005 | TEST-20260913-001 **REDUNDANT / FAIL-INSUFFICIENT** (ETH k=30 ΔLogLoss +0.324) · INACTIVE |
| Holdout | closed |
| Trade | FORBIDDEN |

## Honest label on F2 (Astra 2026-09-13)

Headline compared Map 2 at CLOSE-k=30 to **T−1m** Kalshi mid. T−0 mid was **BLOCKED** (near-degenerate). This is incrementality vs an *older* market price, not same-\(t\) \(m_t\). The mapping is hard 0/1. The kill is “this mapping failed,” not “settlement-window information has no value.” No retune after the sheet.

## What is not in git

- CF hour JSON / 1Hz ndjson (local only; entitled tape)
- Large per-row Examiner JSON for TEST-007 / F1 / F3 (headline tables are in the `.md` packets)
- Keys, PEM, Kalshi credentials

## Packets in this persist

- `archive/tests/TEST-20260911-007-PM003-MARKET-BASELINE.md`
- `archive/tests/TEST-20260912-001-F3-INCREMENTAL.md`
- `archive/tests/TEST-20260912-002-F1-INCREMENTAL.md`
- `archive/tests/TEST-20260913-001-F2-INCREMENTAL.{md,json}`
- `archive/datasets/DATA-PROV-CF-001.md` (CLEARED)
- `data/DATA-PROV-CF-001/provenance/DATA_VERDICT_DATA-PROV-CF-001.md`
- `data/DATA-PROV-CF-001/REPORT.md`
