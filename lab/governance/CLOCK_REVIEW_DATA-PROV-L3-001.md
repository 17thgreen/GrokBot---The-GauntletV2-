# CLOCK REVIEW ORDER — DATA-PROV-L3-001
**From:** Conductor  
**To:** Clock  
**Date (UTC):** 2026-09-12  
**DATA_ID:** DATA-PROV-L3-001  
**Role:** L3 external predictor only — **not** CF BRTI oracle

Issue DATA VERDICT: APPROVED / CONDITIONAL / QUARANTINED / REJECTED.

## Claims
Binance **spot** 1m BTCUSDT+ETHUSDT, 2026-09-04T00:00Z→2026-09-11T23:59Z, 11520 bars each, 0 gaps. Public Vision + Sep-11 www.binance.com API fill (Vision 404 that day). No keys.

Paths: `/workspace/lab/data/DATA-PROV-L3-001/` · REPORT.md · `archive/datasets/DATA-PROV-L3-001.md`

## Required questions
1. TIMESTAMP / knowability at Kalshi decision_time (candle open vs close vs PM-003 checkpoint)
2. Sep-11 API-fill vs Vision — same schema, any revision/gap risk
3. Spot vs CF BRTI — confirm this is **not** oracle and must not be used as F2
4. Join rule to PM-003 checkpoints (which 1m bar is knowable at t)
5. Usable freeze = this window only; do not extend DATA-PROV-001 holdout
6. If CONDITIONAL: which F1 uses are CLEARED (price-at-t, RV-σ) vs blocked

## Forbidden
Treating this as settlement oracle. Examiner F1 scores. Opening holdout. Purchase.
