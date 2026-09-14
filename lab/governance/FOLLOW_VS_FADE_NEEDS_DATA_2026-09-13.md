# Follow-vs-fade — NEEDS_DATA inventory (not a TEST)
**Stamp:** 2026-09-14T21:53Z (hourly pulse)
**Kernel:** memo extract §4 (`KERNEL_EXTRACT_GROK_OSS_MEMO_2026-09-13.md`)
**Trade:** FORBIDDEN. Not READY. Not commissioned.

## Present
| Piece | State |
|-------|--------|
| Live Poly bid/ask | DATA-PROV-PM-006 **running** pid 1391180 · failures=0 · kept≈244.2k |
| Closed 15m windows with both sides | **204** (102 BTC / 102 ETH) |
| Closed 5m windows | (not re-counted this pulse; 15m is the join unit) |
| Capture span | 2026-09-13T20:26Z → live (forward only) |
| Kalshi live mid | DATA-PROV-PM-008 **running** pid 1565519 · poll_s=8.0 · raw≈16.2k · intermittent 429; still writing |
| CB 1m live | DATA-PROV-CB-002 **running** pid 1565525 · kept_bars≈2404 · failures=0 |
| Triple-tape overlap closed 15m / asset (since CB-002 ~01:51Z; align start≥02:00Z) | **79** ≪ 80 |
| CB 1m historical | DATA-PROV-CB-001 (Sep 4–11; **not** this live span) |
| Starter L2 hist | DATA-PROV-PM-009 **718/718** on disk (through 21:30Z start; pulse incr **4** @2026-09-14T21:53Z) |
| LIQ forward | DATA-PROV-LIQ-001 connected pid 360571 · kept≈6880 (passive) |

## Missing for a Clock-joinable switcher
| Hole | Status |
|------|--------|
| Same-t historical Poly **book velocity** on Sep 4–11 research week | BLOCKED (Starter 403 beyond 3 days; GitHub hunt empty) |
| N≥80 closed 15m / asset **on triple-tape overlap** | **accumulating** (79 now; raw live both-side 102/102) |
| Pre-registered A thresholds before peek | Not written |

## Why not Clock / Examiner yet
Triple-tape overlap 79/asset. Headline kill is N<80. Do not score a thin live morning. Do not treat live windows as validation. PM-009 fills Starter-window L2 only — not a free Sep 4–11 dump.

## Next physical
1. Keep PM-006 / PM-008 / CB-002 running.
2. Hourly PM-009 skip-existing catch-up while Starter 3-day window holds (Sep-12 ages off ~2026-09-15T03:46Z; already on disk).
3. Join spec already on disk — Clock only after N plausible **and** all three live tapes cover the same closed windows.
4. Do **not** reopen CB-VEL (FAIL-005) as a standalone card.
5. Squeeze / compression remains intake-only until follow-vs-fade is blocked or signed.

## Forbidden
Examiner score · invent mid from last · treat live windows as validation · F4 θ retune · hire Bot for this hole · mix CB-002 into CB-001 · burn PolyOrderbooks AI credit · paid upgrade from this file

## 2026-09-14T03:52Z PolyOrderbooks Starter
- Sep 4–11 hist books still BLOCKED (403, 3-day cap).
- DATA-PROV-PM-009 pulled 1m L2 for closed 15m BTC/ETH from 2026-09-11T04:00Z (includes Sep-12 PM-004 week).

## 2026-09-14T13:58Z pulse
- Captures healthy. Incremental PM-009 kicked (80 missing after morning DONE). No seat wake. No Examiner. No Clock order. Trade FORBIDDEN.

## 2026-09-14T15:03Z pulse
- Captures healthy. Prior PM-009 incremental DONE @14:04Z (80). New catch-up DONE @15:03Z (**10** ok / 654 skip / 0 fail; 664 on disk through 14:45Z). Triple-tape **53**/asset ≪80. No seat wake. No Examiner. No Clock. No F4 retune. Trade FORBIDDEN. Quiet to Logan.

## 2026-09-14T16:19Z pulse
- Captures healthy: LIQ (pid 360571, connected, kept≈6102) + PM-006 (pid 1391180, failures=0, kept≈203.0k, closed 15m both-side **160**=80/80) + PM-008 (pid 1565519, poll_s=8.0, kept≈11.7k, failures=72) + CB-002 (pid 1565525, kept_bars≈1732, failures=0).
- PM-009 catch-up DONE @16:18Z (ok=10 skip=664 fail=0; **674** on disk through 16:00Z).
- Triple-tape overlap **57**/asset ≪80 — follow-vs-fade still NEEDS_DATA.
- No seat wake. No Examiner. No Clock. No F4 retune. Trade FORBIDDEN. Quiet to Logan (nothing needs him).

## 2026-09-14T17:07Z pulse
- Captures healthy: LIQ (pid 360571, connected, kept≈6241) + PM-006 (pid 1391180, failures=0, kept≈209.3k, closed 15m both-side **166**=83/83) + PM-008 (pid 1565519, poll_s=8.0, raw≈14.3k, status failures=74, still writing through 429s) + CB-002 (pid 1565525, kept_bars≈1832, failures=0).
- PM-009 catch-up DONE @17:07Z (ok=6 skip=674 fail=0; **680** on disk through 17:00Z).
- Triple-tape overlap **61**/asset ≪80 — follow-vs-fade still NEEDS_DATA.
- No seat wake. No Examiner. No Clock. No F4 retune. Trade FORBIDDEN. Quiet to Logan (nothing needs him).

## 2026-09-14T18:06Z pulse
- Captures healthy: LIQ (pid 360571, connected, kept≈6293) + PM-006 (pid 1391180, failures=0, kept≈216.6k, closed 15m both-side **174**=87/87) + PM-008 (pid 1565519, poll_s=8.0, raw≈15.1k, status failures=78, still writing through 429s) + CB-002 (pid 1565525, kept_bars≈1948, failures=0).
- PM-009 catch-up DONE @18:05Z (ok=8 skip=680 fail=0; **688/688** on disk through 17:45Z start).
- Triple-tape overlap **64**/asset ≪80 — follow-vs-fade still NEEDS_DATA.
- No seat wake. No Examiner. No Clock. No F4 retune. Trade FORBIDDEN. Quiet to Logan (nothing needs him).

## 2026-09-14T18:57Z pulse
- Captures healthy: LIQ (pid 360571, connected, kept≈6446) + PM-006 (pid 1391180, failures=0, kept≈223.3k, closed 15m both-side **180**=90/90) + PM-008 (pid 1565519, poll_s=8.0, raw≈15.8k, status failures=97, still writing through 429s) + CB-002 (pid 1565525, kept_bars≈2054, failures=0).
- PM-009 catch-up DONE @2026-09-14T18:57Z (ok=6 skip=688 fail=0; **694/694** on disk through 18:30Z start).
- Triple-tape overlap **67**/asset ≪80 — follow-vs-fade still NEEDS_DATA.
- No seat wake. No Examiner. No Clock. No F4 retune. Trade FORBIDDEN. Quiet to Logan (nothing needs him).

## 2026-09-14T19:55Z pulse
- Captures healthy: LIQ (pid 360571, connected, kept≈6495) + PM-006 (pid 1391180, failures=0, kept≈230.1k, closed 15m both-side **188**=94/94) + PM-008 (pid 1565519, poll_s=8.0, raw≈16.6k, status failures=86, still writing through 429s) + CB-002 (pid 1565525, kept_bars≈2166, failures=0).
- PM-009 catch-up DONE @2026-09-14T19:54Z (ok=8 skip=694 fail=0; **702/702** on disk through 19:30Z start).
- Triple-tape overlap **71**/asset ≪80 — follow-vs-fade still NEEDS_DATA.
- No seat wake. No Examiner. No Clock. No F4 retune. Trade FORBIDDEN. Quiet to Logan (nothing needs him).

## 2026-09-14T21:22Z pulse
- Captures healthy: LIQ (pid 360571, connected, kept≈6865) + PM-006 (pid 1391180, failures=0, kept≈240.3k, closed 15m both-side **200**=100/100) + PM-008 (pid 1565519, poll_s=8.0, raw≈17.7k, intermittent 429, still writing) + CB-002 (pid 1565525, kept_bars≈2340, failures=0).
- PM-009 catch-up DONE @2026-09-14T21:22Z (ok=10 skip=704 fail=0; **714/714** on disk through 21:00Z start).
- Triple-tape overlap **77**/asset ≪80 (~45 min to N=80 at current cadence) — follow-vs-fade still NEEDS_DATA.
- No seat wake. No Examiner. No Clock. No F4 retune. Trade FORBIDDEN. Quiet to Logan (nothing needs him).

## 2026-09-14T21:53Z pulse
- Captures healthy: LIQ (pid 360571, connected, kept≈6880) + PM-006 (pid 1391180, failures=0, kept≈244.2k, closed 15m both-side **204**=102/102) + PM-008 (pid 1565519, poll_s=8.0, raw≈16.2k, intermittent 429, still writing) + CB-002 (pid 1565525, kept_bars≈2404, failures=0).
- PM-009 catch-up DONE @2026-09-14T21:53Z (ok=4 skip=714 fail=0; **718/718** on disk through 21:30Z start).
- Triple-tape overlap **79**/asset ≪80 (~one closed 15m window to gate) — follow-vs-fade still NEEDS_DATA.
- No seat wake. No Examiner. No Clock. No F4 retune. Trade FORBIDDEN. Quiet to Logan (nothing needs him).

