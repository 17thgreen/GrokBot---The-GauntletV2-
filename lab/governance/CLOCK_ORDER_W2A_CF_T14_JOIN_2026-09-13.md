# CLOCK ORDER — W2-A CF hour-tape join at T-14m
**To:** The Clock
**From:** Conductor
**Date:** 2026-09-13
**Trade:** FORBIDDEN
**Feature:** DRAFT-FEAT-20260913-003
**Gate:** DRAFT-ABST-20260913-003

## Join to certify (fail-closed)

```
cf_t = last-in-second CF print
       index = BRTI if BTC else ETHUSD_RTI
       source = DATA-PROV-CF-001 HOUR tape
       unix second = floor(decision_time_ms / 1000)
       require print exists AND timestamp_ms <= decision_time_ms
K    = PM-001 FLOOR_STRIKE
       require present AND OPEN_TIME <= decision_time
m_t  = same-row PM-003 mid; mid timestamp = decision_time
cell ∈ {KALSHI|15m|BTC|T-14m|mid, KALSHI|15m|ETH|T-14m|mid}
       rem = 840
```

Missing cf_t or K or m_t → fail-closed (Feature will set p_t := m_t). Do **not** substitute T−1 mid. Do **not** use the close-minute CLEARED extractor. Do **not** use Binance. Do **not** use EXPIRATION_VALUE. Do **not** use incomplete current second.

## Scope
Join only. Not alpha. Not Examiner Δ.
Headlines only (no annex, no T-10m/T-5m).
DATA: PM-003 + PM-001 + CF-001 hour archive. No new fetch unless you must name a hole.

## Why this is not the F2 CLEARED path
CF-001 CLEARED uses = close-minute 1Hz + pre_close_last. This join is last-in-second at T-14m (840s remaining) from the **hour** tape.

## Write
`/workspace/lab/data/DATA-PROV-CF-001/provenance/DATA_VERDICT_W2A_CF_T14_JOIN.md`
plus audit JSON.

DATA VERDICT: CLEARED / CONDITIONAL / QUARANTINED / REJECTED.
If hour-tape holes at those seconds: say so with coverage counts. Do not invent prints.
