# CLOCK ORDER — DATA-PROV-CB-001 × PM-003 completed-bar join
**To:** The Clock
**From:** Conductor
**Date:** 2026-09-13
**Trade:** FORBIDDEN
**Not a Feature. Not READY. Not Examiner.**

## Join to certify (fail-closed)

Coinbase 1m completed bar at Kalshi `decision_time`:

```
cb_close_t  = Coinbase 1m close whose bar_end <= decision_time
              bar_end = candle_start + 60s
              product = BTC-USD if asset=BTC else ETH-USD
              source  = DATA-PROV-CB-001 raw CSV
cb_close_tm1 = prior completed 1m close (bar_end <= decision_time - 60s)
v_CB,t      = (cb_close_t - cb_close_tm1) / cb_close_tm1
m_t         = same-row PM-003 mid; mid timestamp = decision_time
```

Incomplete current minute = missing. Do **not** use Binance, CF, BRTI, or L3 to fill. Do **not** treat v_CB as a forecast. Do **not** Examiner-score.

## Scope
Join / provenance only. Inventory for a later Coinbase-velocity card (Grok memo axis B). Examiner **dark**. No fourth READY. Wave 006 remains W2-B.

Pre-joined file exists: `data/DATA-PROV-CB-001/derived/pm003_cb_join.ndjson` (claimed 6040/6040, 0 lookahead). Audit it. Do not trust the claim.

## Write
`/workspace/lab/data/DATA-PROV-CB-001/provenance/DATA_VERDICT_CB001_PM003_JOIN.md`
plus audit JSON.

DATA VERDICT: CLEARED / CONDITIONAL / QUARANTINED / REJECTED.
Name any lookahead, hole, or on-minute coincidence that is not knowable-at-t.
