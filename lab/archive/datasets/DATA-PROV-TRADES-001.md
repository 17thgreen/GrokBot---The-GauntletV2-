# DATA-PROV-TRADES-001

- **DATA_ID:** DATA-PROV-TRADES-001
- **STATUS:** CLOCK_REVIEW
- **Registered:** 2026-09-11 UTC (Archivist)
- **Fetch complete:** 2026-09-11T00:42:02Z (manifest)
- **Spec:** `/workspace/lab/governance/DATA_PROV_TRADES_001_SPEC.md`
- **Manifest:** `/workspace/lab/data/DATA-PROV-TRADES-001/provenance/DOWNLOAD_MANIFEST.md`
- **Role:** Provisional reference **aggTrades** family — distinct from DATA-PROV-001 (OHLCV). Not venue marriage. Not full L2.
- **Path:** `/workspace/lab/data/DATA-PROV-TRADES-001/`

## Inventory [V Archivist]

| Symbol | Daily zips | First | Last | Missing days |
|--------|------------|-------|------|--------------|
| BTCUSDT | 2069 | 2021-01-01 | 2026-08-31 | 0 |
| ETHUSDT | 2069 | 2021-01-01 | 2026-08-31 | 0 |

- SHA256SUMS lines: 4138; sidecars 2069×2 [V counts]
- Spot-check sha256 (sample zips): PASS [V]
- Source: Binance Vision daily aggTrades UM
- `derived/`: empty
- Completion: FULL (`STOPPED_TIER=NONE_FULL`)

## Known provenance caveats (for Clock)
- Some days omit CSV header row (documented in manifest)
- 24 FAIL lines in download_log are **pre-fix** artifacts — days present after restart; not missing [V manifest]
- Full per-day row inventory not written (job aborted at finalize) — do not invent totals [V]

## Access gates

| Path | Access |
|------|--------|
| raw/ | immutable; Clock review |
| derived/ | empty until Clock + approved transforms |
| Examiner | **BLOCKED until Clock verdict** |
| EDGE-20260911-001/002 TEST | held until Clock + Conductor route |
| EDGE-005/006 | still UNMEASURABLE WITHOUT L2 (this dataset does not unblock) |

## Status history
1. FETCH_IN_PROGRESS
2. **CLOCK_REVIEW** ← current (fetch COMPLETE; Examiner blocked until Clock)
