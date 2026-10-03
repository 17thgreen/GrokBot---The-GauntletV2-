# DATA VERDICT — PM-004 Sep-12 day-start edges via L3-001

**Issued by:** The Clock
**Issued UTC:** 2026-09-13T22:07:39Z
**Authority:** `governance/CLOCK_ORDER_PM004_L3_SEP11_EDGE_2026-09-13.md` · prior `DATA_VERDICT_PM004_L3002_JOIN` CONDITIONAL
**Trade:** FORBIDDEN
**Not Feature / Not READY. F4 not commissioned. Examiner dark.**

---

## DATA VERDICT: CLEARED

**VERDICT_SCOPE:** edge_only (four named Sep-12 day-start rows)
**Certified rule:** lock **B** (`bar_end_ms < decision_time_ms`)
**Source:** L3-001 derived Sep-11 completed bars only
**NOT:** PM-003 · full L3-001∪L3-002 universe expansion · Sep-13 fill · Policy A rescue · F4 · Examiner · Feature READY

## Rationale

All four named lock-B misses from `DATA_VERDICT_PM004_L3002_JOIN` now join from L3-001 Sep-11 tape under the same B rule. Lookahead 0. Last-as-mid 0. Not a silent tape union — only these four edges.

## Coverage (exact)

| asset | decision_time | rem | B_join | B bar open (L3-001) | lag_ms | uses 23:59? |
|-------|---------------|----:|:------:|---------------------|-------:|:-----------:|
| BTC | 2026-09-12T00:00:00Z | 0 | **yes** | 2026-09-11T23:58:00Z | 60000 | no |
| ETH | 2026-09-12T00:00:00Z | 0 | **yes** | 2026-09-11T23:58:00Z | 60000 | no |
| BTC | 2026-09-12T00:01:00Z | 840 | **yes** | 2026-09-11T23:59:00Z | 60000 | **yes** |
| ETH | 2026-09-12T00:01:00Z | 840 | **yes** | 2026-09-11T23:59:00Z | 60000 | **yes** |

**Honesty [V]:** At `t=00:00`, the 23:59 bar has `bar_end == t` — **forbidden under B**. Lock B correctly selects **23:58**. At `t=00:01`, B selects **23:59** as Conductor named. Policy A on-minute at 00:00 is caveat-only — not certified.

## Combined Sep-12 note (inventory)

With this edge CLEARED + prior L3-002 CONDITIONAL Sep-12 mid under B: the four named holes close. Sep-12 mid universe becomes **855/855** joinable under B when L3-001 edge fill is allowed for these rows only. Sep-13 remains uncovered (Vision 404). Prior CONDITIONAL caveats (L3 ≠ oracle; Policy A not scored) still apply to the broader join.

## SAFE / UNSAFE

### SAFE
- Using L3-001 Sep-11 completed bars under B for these four named PM-004 mid rows only
- Keeping Policy A (23:59 at 00:00) unscored

### UNSAFE
- Treating this as a full L3-001∪L3-002 union / expanding Sep-11 PM-004 joins
- Policy A rescue at 00:00
- Filling Sep-13
- PM-003 as fill
- F4 commission / Examiner / Feature READY from this alone

## FAILURES

None on the four named edges under B.

## REQUIRED REMEDIATION

None for these edges. Downstream cards must name L3-001 edge fill explicitly when claiming Sep-12 855/855 under B.

## Clock seal

**DATA VERDICT: CLEARED** (edge-only, lock B) — sealed by The Clock 2026-09-13T22:07:39Z.
F4 not commissioned. Examiner dark. Trade FORBIDDEN.
