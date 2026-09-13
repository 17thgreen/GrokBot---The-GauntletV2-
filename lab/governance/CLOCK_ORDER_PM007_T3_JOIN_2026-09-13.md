# CLOCK ORDER — DATA-PROV-PM-007 rem=180 mid
**To:** The Clock
**From:** Conductor
**Date:** 2026-09-13
**Trade:** FORBIDDEN
**Wave:** 008 / W2-D
**Not a Feature. Not READY. Not Examiner.**

## Join to certify
Kalshi 15m BTC/ETH **mid** at rem=180 (T-3m) for the PM-003 window, paired on exact (asset, OPEN_TIME, CLOSE_TIME).

Claimed: 604/604 BTC, 604/604 ETH, derived from PM-003 official 1m candles at `end_period_ts = close−180`.
Do **not** trust the claim. Rebuild. Confirm bid>0, ask>0, bid≤ask, implied_p_method=mid. No last-as-mid. No invented quotes.

Headlines later: `KALSHI|15m|{BTC,ETH}|T-3m|mid`. Certify the tape first.

## Forbidden
T-1 as this cell. Union with PM-002. Poly last. Examiner Δ. Fabricating rem=180 from rem=60/300 interpolation.

## Write
`/workspace/lab/data/DATA-PROV-PM-007/provenance/DATA_VERDICT_PM007_T3_JOIN.md`
DATA VERDICT: CLEARED / CONDITIONAL / QUARANTINED / REJECTED.
