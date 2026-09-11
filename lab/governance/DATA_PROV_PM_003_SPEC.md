# DATA-PROV-PM-003 — remaining Kalshi 15m checkpoints
**Authority:** Conductor  
**Date (UTC):** 2026-09-11  
**Parent labels:** DATA-PROV-PM-001  
**Sibling (used):** DATA-PROV-PM-002 SLICE-PM002-BOUNDED-240 = USED_RESEARCH (TEST-20260911-006). Do not call that slice holdout.

## Why
TEST-20260911-006 FAIL-INSUFFICIENT: N=51–60 cannot support named calibration. Clock remediation #4: expand same construction, then re-Clock.

## Universe
Remaining Kalshi 15m BTC/ETH from PM-001 **not** in PM-002 coverage (venue_native_id).
Expected: 604 BTC + 604 ETH = **1208**. Poly deferred (weaker last-print annex).

## Construction (identical to PM-002 Kalshi)
- Public `GET /series/{series}/markets/{ticker}/candlesticks?period_interval=1` — no keys
- Checkpoints T−14m / T−10m / T−5m / T−1m / T−0 (same remaining-sec grid)
- mid if bid>0 and ask>0 and bid≤ask else last; never PM-001 LAST_PRICE / OUTCOME_PRICES
- No invented OPEN; no post-CLOSE
- Pace for HTTP 429

## Store
`/workspace/lab/data/DATA-PROV-PM-003/`
raw/ · derived/checkpoints.ndjson · contract_coverage.ndjson · REPORT.md · SHA256 · stub `archive/datasets/DATA-PROV-PM-003.md`

## After fetch
PENDING_CLOCK. Do not Examiner until Clock. Do not mix with PM-002 as holdout. Research-union later only if ledger says RESEARCH.
