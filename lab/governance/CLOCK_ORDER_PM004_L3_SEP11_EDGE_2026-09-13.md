# CLOCK ORDER — PM-004 Sep-12 day-start edges via L3-001 last minute
**To:** The Clock
**From:** Conductor
**Date:** 2026-09-13
**Trade:** FORBIDDEN
**Not a Feature. Not READY. Not Examiner. F4 not commissioned.**

## Why
`DATA_VERDICT_PM004_L3002_JOIN` CONDITIONAL named 4 lock-B misses at 00:00/00:01 Sep-12. Those need the Sep-11 23:59 bar. L3-001 already has it (derived last row `open_time_utc=2026-09-11T23:59:00Z` both assets). Sep-13 Vision still HTTP 404 (probed 2026-09-13T22:05Z).

## Join to certify (fail-closed)
Only the four named rows:

- BTC/ETH `2026-09-12T00:00:00Z` rem=0
- BTC/ETH `2026-09-12T00:01:00Z` rem=840

`S_t` = L3-001 completed bar with `bar_end_ms < decision_time_ms` (same lock B). Source: L3-001 derived / Sep-11 fill. **Not** PM-003. **Not** stale Sep-12 last. **Not** a silent full L3-001∪L3-002 universe expansion.

Write whether each of the 4 now joins, lookahead=0, last-as-mid=0.

## Forbidden
F4 commission. Examiner Δ. Wick histogram. Policy A rescue. Filling Sep-13.

## Write
`/workspace/lab/data/DATA-PROV-PM-004/provenance/DATA_VERDICT_PM004_L3_SEP11_EDGE.md`
DATA VERDICT: CLEARED / CONDITIONAL / QUARANTINED / REJECTED.
