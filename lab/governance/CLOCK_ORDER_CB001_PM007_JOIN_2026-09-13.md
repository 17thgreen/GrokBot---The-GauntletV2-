# CLOCK ORDER — DATA-PROV-CB-001 × PM-007 rem=180 completed-bar join
**To:** The Clock
**From:** Conductor
**Date:** 2026-09-13
**Wave:** 008 / W2-D
**Trade:** FORBIDDEN
**Not a Feature. Not READY. Not Examiner.**

## Why this join
CB-001 × PM-003 was CONDITIONAL at rem 840/600/300/60/0. That verdict **does not** cover rem=180. DRAFT-FEAT-20260913-006 uses Coinbase 1m under lock B at T-3m. Certify that join before any Examiner sheet.

## Join to certify (fail-closed)

Feature lock is **B** (`bar_end < decision_time`) — same as Wave 007 / `CBVEL_ON_MINUTE_POLICY_2026-09-13.md`.

```
decision_time = CLOSE_TIME − 180s          # PM-007 same row
product       = BTC-USD if asset=BTC else ETH-USD
bar           = last CB-001 1m candle with bar_end < decision_time
prior         = immediately previous completed CB-001 1m
v_CB,t        = (bar.close − prior.close) / prior.close
m_t           = PM-007 same-row mid; method=mid only
```

Also report SPEC / policy A (`bar_end <= t`) as a **caveat count only**. Do **not** score A. Do **not** silently switch.

Incomplete current minute = missing. Do **not** use Binance, CF, BRTI, or L3 to fill. Do **not** treat v_CB as a forecast. Do **not** Examiner-score. Do **not** invent coverage from the PM-003 join.

## Claim (do not trust)
`data/DATA-PROV-CB-001/derived/pm007_cb_join.ndjson`
plus `pm007_cb_join_coverage.json`. Rebuild from CB-001 raw CSV + PM-007 checkpoints.

## Scope
Join / provenance only. Inventory for DRAFT-FEAT-20260913-006. No fourth READY. W2-B stays HELD.

## Write
`/workspace/lab/data/DATA-PROV-CB-001/provenance/DATA_VERDICT_CB001_PM007_JOIN.md`
plus audit JSON.

DATA VERDICT: CLEARED / CONDITIONAL / QUARANTINED / REJECTED.
Name lookahead, holes, and any on-minute coincidence at rem=180. Coverage under **B** is the Feature lock.
