# CLOCK AUDIT — PM-004 Sep-12 day-start edges via L3-001

- **AUDIT_ID:** `CLOCK_AUDIT_PM004_L3_SEP11_EDGE`
- **AUDITED_AT_UTC:** 2026-09-13T22:07:39Z
- **Lock:** B (`bar_end_ms < decision_time_ms`); `bar_end_ms = open_time_ms + 60000`
- **Source:** L3-001 derived Sep-11 tape edge only — **not** PM-003 · **not** full L3-001∪L3-002 expansion · **not** Sep-13
- **Policy A:** caveat only (forbidden as rescue)

## Named rows (4/4 under B)

| asset | decision_time | rem | ticker | B_join | B bar open | B lag_ms | B_is_2359 | A_eq_t (caveat) | lookahead | last-as-mid |
|-------|---------------|----:|--------|:------:|------------|---------:|:---------:|:---------------:|:---------:|:-----------:|
| BTC | 2026-09-12T00:00:00Z | 0 | KXBTC15M-26SEP112000-00 | yes | 2026-09-11T23:58:00Z | 60000 | no | yes (23:59) | 0 | 0 |
| ETH | 2026-09-12T00:00:00Z | 0 | KXETH15M-26SEP112000-00 | yes | 2026-09-11T23:58:00Z | 60000 | no | yes (23:59) | 0 | 0 |
| BTC | 2026-09-12T00:01:00Z | 840 | KXBTC15M-26SEP112015-15 | yes | 2026-09-11T23:59:00Z | 60000 | yes | no | 0 | 0 |
| ETH | 2026-09-12T00:01:00Z | 840 | KXETH15M-26SEP112015-15 | yes | 2026-09-11T23:59:00Z | 60000 | yes | no | 0 | 0 |

**Honesty:** Under lock B, rem=0 at 00:00 cannot use the 23:59 bar (`bar_end == t`). It uses **23:58** from the same L3-001 Sep-11 tape. rem=840 at 00:01 uses **23:59** as Conductor named. Policy A would take 23:59 at 00:00 — **not** certified.

## Summary
- B_join: **4/4**
- lookahead_B: **0**
- last-as-mid: **0**
- mid_ok on all 4: **True**

## Recommended verdict
**CLEARED** (edge-only) under lock B for these four named rows.
