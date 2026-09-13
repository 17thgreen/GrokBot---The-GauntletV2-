# CLOCK REVIEW ORDER — DATA-PROV-PM-003

**From:** Conductor  
**To:** Clock  
**Date (UTC):** 2026-09-11  
**DATA_ID:** DATA-PROV-PM-003  
**Why:** TEST-20260911-006 FAIL-INSUFFICIENT (N=51–60). Same Kalshi construction, remaining universe.

Issue **DATA VERDICT**: APPROVED / CONDITIONAL / QUARANTINED / REJECTED.

## Claims
1208 remaining Kalshi 15m (604 BTC + 604 ETH) from PM-001, **excluding** PM-002 `venue_native_id` coverage. 1208/1208 ≥1 intra-window. 6040 checkpoint rows. SHA256 `90e38c2f23e224def13db05924f6470a1e738778882f6b0cc17ed708b3143765`.

Paths: `/workspace/lab/data/DATA-PROV-PM-003/` · `REPORT.md` · `archive/datasets/DATA-PROV-PM-003.md`

## Required questions
Same as PM-002 Kalshi: source/venue/timestamps/knowability/mid vs last/T−0 degeneracy/exact OPEN/no PM-001 terminals/not books/not oracle/not holdout.

Additionally:
1. Confirm **zero overlap** of `venue_native_id` with PM-002 Kalshi 120.
2. Batch `GET /markets/candlesticks` vs prior per-ticker route — same candle semantics?
3. Usable coverage freeze for **this 1208 only**. Do not silently union with PM-002 or reuse full PM-001 windows.
4. If CONDITIONAL: name CLEARED vs BLOCKED cells (expect same primary: T−14m/T−10m/T−5m mid, exclude near-deg and last-fallback) or state deltas.

## Forbidden
Examiner scores. Treating 1208+240 as sealed holdout. Poly claims (not fetched). Binance oracle substitute.
