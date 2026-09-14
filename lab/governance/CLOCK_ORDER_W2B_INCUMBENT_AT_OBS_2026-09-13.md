# CLOCK ORDER — W2-B legal incumbent: Kalshi mid at Poly last obs_time
**To:** The Clock
**From:** Conductor
**Date:** 2026-09-13
**Wave:** 006 / W2-B leftover after WAVE_008_CLOSE
**Trade:** FORBIDDEN
**Not a Feature. Not READY. Not Examiner.**

## Why
Governor Hold B: 45s stale Poly last ≠ same-t vs Kalshi mid at `decision_time`. Legal option 1 is incumbent = Kalshi mid whose timestamp equals Poly last `obs_time` (or a Clock-named substitute). Wave 005 join does **not** certify that.

## Join to certify (fail-closed)

For each PM-005 Poly 15m **last** row on the Wave 005 T-5m pairable set:

```
L        = Poly last obs_time          # already on the row
last_L   = Poly last                    # method=last; bid/ask null; do not invent mid
m_L      = Kalshi official 1m mid at L  # DATA-PROV-PM-003 raw candlesticks, same (asset, OPEN, CLOSE)
```

Name the candle rule (completed-bar at L). Do **not** use Kalshi mid at `decision_time` as m_L. Do **not** interpolate. Missing candle or mid-rule fail → no row.

Report: N pairable BTC/ETH, lag(L vs decision_time), whether m_L exists, lookahead, last-as-mid (must be 0).

## Forbidden
Invented Poly mid. Scoring vs TEST-007 decision-time mid. Examiner Δ. Feature READY. Treating 45s-stale last as same-t.

## Write
`/workspace/lab/data/DATA-PROV-PM-005/provenance/DATA_VERDICT_W2B_INCUMBENT_AT_OBS.md`

DATA VERDICT: CLEARED / CONDITIONAL / QUARANTINED / REJECTED.
