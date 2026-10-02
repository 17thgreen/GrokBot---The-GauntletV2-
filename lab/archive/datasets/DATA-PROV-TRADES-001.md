# DATA-PROV-TRADES-001

- **DATA_ID:** DATA-PROV-TRADES-001
- **STATUS:** CONDITIONAL
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
| raw/ | immutable; Clock CONDITIONAL |
| derived/ | empty until approved transforms |
| Examiner | **CLEARED for trade-flow-only** after Conductor route (001 then 002 commissioned) |
| EDGE-20260911-001 | IN_TEST — provisional RESEARCH TEST commissioned |
| EDGE-20260911-002 | HYPOTHESIS — next after 001; CLEARED for trade-flow TEST |
| EDGE-005/006 | still UNMEASURABLE WITHOUT L2 (this dataset does not unblock) |
| Seal | timestamp-aligned to OHLCV SEAL_LOCK (not calendar-day) |

## Status history
1. FETCH_IN_PROGRESS
2. CLOCK_REVIEW (fetch COMPLETE)
3. **CONDITIONAL** ← current (2026-09-11T00:59:35Z) — Clock DATA VERDICT: APPROVED_WITH_LIMITATIONS; trade-flow edges cleared; EDGE-005/006 still blocked; timestamp-aligned seals preferred

## Clock DATA VERDICT

- **Verdict:** CONDITIONAL
- **Quality:** APPROVED_WITH_LIMITATIONS
- **Failures:** none (hard inventory/hash; sampled integrity)
- **Safe features:** aggressor-signed aggTrades with transact_time <= decision; completed-interval trade-flow features
- **Unsafe features:** L2 proxies (005/006); lookahead trades; receipt-time claims; day-aligned seal leaks on boundary days
- **Required remediation:** optional full-zip content inventory; receipt-time on live feeds; L2 before 005/006; timestamp-aligned seals; forward window + cross-venue before capital
- **Full verdict:** `/workspace/lab/data/DATA-PROV-TRADES-001/provenance/DATA_VERDICT_DATA-PROV-TRADES-001.md`
- **Audit:** `/workspace/lab/archive/audit/2026-09-11-Clock-DATA-VERDICT-DATA-PROV-TRADES-001.md`
