# Current state — 2026-09-13 (persisted for GitHub review)

**Not a strategy.** **Not a stamp.** Reconstructs what a reviewer of `main` could not see at `754c73f`.

| Item | State |
|------|--------|
| Incumbent | `MKT-KALSHI-15M-MID` · TEST-20260911-007 `BASELINE_MEASURED` |
| F1 | TEST-20260912-002 `REDUNDANT / FAIL-INSUFFICIENT` · cards INACTIVE |
| F3 | TEST-20260912-001 `REDUNDANT / FAIL-INSUFFICIENT` · cards INACTIVE |
| DATA-PROV-CF-001 | **CLEARED** 2026-09-13T17:53:52Z · 1208/1208 close minutes 60/60 · raw ticks **not** in this repo |
| F2 / FEAT-005 | TEST-20260913-001 **REDUNDANT / FAIL-INSUFFICIENT** (ETH k=30 ΔLogLoss +0.324) · INACTIVE |
| Holdout | closed |
| Trade | FORBIDDEN |

## Honest label on F2 (Astra 2026-09-13)

Headline compared Map 2 at CLOSE-k=30 to **T−1m** Kalshi mid. T−0 mid was **BLOCKED** (near-degenerate). This is incrementality vs an *older* market price, not same-\(t\) \(m_t\). The mapping is hard 0/1. The kill is “this mapping failed,” not “settlement-window information has no value.” No retune after the sheet.

## What is not in git

- CF hour JSON / 1Hz ndjson (local only; entitled tape)
- Large per-row Examiner JSON for TEST-007 / F1 / F3 (headline tables are in the `.md` packets)
- Keys, PEM, Kalshi credentials

## Packets in this persist

- `archive/tests/TEST-20260911-007-PM003-MARKET-BASELINE.md`
- `archive/tests/TEST-20260912-001-F3-INCREMENTAL.md`
- `archive/tests/TEST-20260912-002-F1-INCREMENTAL.md`
- `archive/tests/TEST-20260913-001-F2-INCREMENTAL.{md,json}`
- `archive/datasets/DATA-PROV-CF-001.md` (CLEARED)
- `data/DATA-PROV-CF-001/provenance/DATA_VERDICT_DATA-PROV-CF-001.md`
- `data/DATA-PROV-CF-001/REPORT.md`

## W2-C (updated 2026-09-13T19:17:54Z)

| Item | State |
|------|--------|
| Feature | `FEAT-20260913-001` (promoted from DRAFT-FEAT-20260913-001) |
| Gate | DRAFT-ABST-20260913-001 |
| TEST-20260913-002 | **REDUNDANT / FAIL-INSUFFICIENT** — one headline incremental, other inverts; package kill |
| STATUS | INACTIVE · no cemetery · no retune · trade FORBIDDEN |
| Artifacts | `archive/tests/TEST-20260913-002-W2C-INCREMENTAL.{md,json}` |

## W2-E (updated 2026-09-13T19:28:51Z)

| Item | State |
|------|--------|
| Feature | `FEAT-20260913-002` (promoted from DRAFT-FEAT-20260913-002) |
| Gate | DRAFT-ABST-20260913-002 |
| TEST-20260913-003 | **REDUNDANT / FAIL-INSUFFICIENT** — both T-5m headlines Δ>0 vs mid |
| Stamp | L3 ≠ oracle · CONDITIONAL join |
| STATUS | INACTIVE · no cemetery · no retune · trade FORBIDDEN |
| Artifacts | `archive/tests/TEST-20260913-003-W2E-INCREMENTAL.{md,json}` |

## Front-door sync (2026-09-13T19:30:19Z) — AMD-003

| Item | State |
|------|--------|
| Wave 003 | **CLOSED** on TEST-20260913-003 W2-E REDUNDANT / FAIL-INSUFFICIENT |
| FEAT-20260913-002 | INACTIVE · **no cemetery** (same as W2-C) |
| Wave 004 | axis **W2-A** declared — `governance/WAVE_004_ORTHOGONAL_SLOT_2026-09-13.md` |
| Incumbent | MKT-KALSHI-15M-MID · trade FORBIDDEN · holdout closed |
| League | `archive/league/STRATEGY_LEAGUE.md` — no challengers |

## W2-A / Wave 004 (updated 2026-09-13T19:42:19Z)

| Item | State |
|------|--------|
| Feature | `FEAT-20260913-003` (promoted from DRAFT-FEAT-20260913-003) |
| Gate | DRAFT-ABST-20260913-003 |
| TEST-20260913-004 | **REDUNDANT / FAIL-INSUFFICIENT** — both T-14m Δ>0 vs mid |
| Join | CONDITIONAL · Policy B · K revision [A] · close-minute CLEARED ≠ this join |
| Wave 004 | **CLOSED** · no cemetery · trade FORBIDDEN |
| Artifacts | `archive/tests/TEST-20260913-004-W2A-INCREMENTAL.{md,json}` |

## Wave 005 (updated 2026-09-13T19:43:08Z) — AMD-003

| Item | State |
|------|--------|
| Wave 004 | CLOSED on TEST-20260913-004 · FEAT-20260913-003 INACTIVE · no cemetery |
| Wave 005 | axis **W2-B** declared · **NEEDS_DATA** · `governance/WAVE_005_ORTHOGONAL_SLOT_2026-09-13.md` |
| Capacity | no 4th READY this cycle without Governor |
| Trade | FORBIDDEN · holdout closed |

## POST_KILL pointer (2026-09-13T19:43:24Z)
`governance/POST_KILL_ATTENTION_2026-09-13.md` stamped after TEST-20260913-004. Leftover = **W2-B** (Wave 005 NEEDS_DATA). Not pending. No 4th READY. No cemetery.

## W2-B HOLD (Governor Pick B, 2026-09-13)

| Item | State |
|------|--------|
| Feature | DRAFT-FEAT-20260913-004 **NEEDS_DATA** |
| Join | DATA_VERDICT_W2B_POLY_T5_JOIN **CONDITIONAL** — 254/240 pairable; lag ~45s |
| TEST | **none** — Examiner dark; not a fourth READY |
| Next | Wave 006 declared (`WAVE_006_ORTHOGONAL_SLOT_2026-09-13.md`) — no notebook yet |

## CB-VEL (updated 2026-09-13T20:58:16Z)
TEST-20260913-005 REDUNDANT / FAIL-INSUFFICIENT. FEAT-20260913-005 INACTIVE. Wave 007 closed. Wave 008 W2-D rem=180 declared NEEDS_DATA. Mid incumbent. No retune. Poly last still unsored.

## Wave 008 close (2026-09-13T21:51:30Z)

| Item | State |
|------|--------|
| Feature | `FEAT-20260913-006` (promoted from DRAFT-FEAT-20260913-006) |
| TEST-20260913-006 | **REDUNDANT / FAIL-INSUFFICIENT** |
| Wave 008 | **CLOSED** · no cemetery |
| Wave 006 W2-B | still HELD |
| Artifacts | `archive/tests/TEST-20260913-006-W2D-IVRV-INCREMENTAL.{md,json}` |

## W2-B incumbent-at-obs Clock (updated 2026-09-13T22:00:54Z)

| Item | State |
|------|--------|
| Order | `CLOCK_ORDER_W2B_INCUMBENT_AT_OBS_2026-09-13.md` |
| Verdict | **CONDITIONAL** · join_only_incumbent_at_obs |
| Coverage | BTC 254/254 m_L · ETH 240/240 m_L · miss_m_L=0 |
| Lag | median ~45s L vs decision_time (unchanged) |
| Candle | `completed_bar_at_L_end_period_ts_le_L` · decision_time bar as m_L = 0 · last-as-mid = 0 |
| Door | NEEDS_DATA · Examiner dark on Poly last |
| Artifacts | `data/DATA-PROV-PM-005/provenance/DATA_VERDICT_W2B_INCUMBENT_AT_OBS.md` |

Next physical: Cartographer Wave 006 eligibility with lag + incumbent-at-obs (m_L) on the card. Not Examiner. No λ/c/w retune. Captures LIQ + PM-006 live.

## F4 leftover data (2026-09-13T22:05Z)
PM-004 × L3-002 Clock **CONDITIONAL** lock B: Sep-12 851/855 mid×L3; 4 named midnight edges. Sep-13 Vision still 404. F4 not commissioned. Examiner dark. Edge-close via L3-001 Sep-11 23:59 ordered (not PM-003 peek).

Sep-12 midnight edges **CLEARED** 4/4 (`DATA_VERDICT_PM004_L3_SEP11_EDGE`). Combined Sep-12 mid×L3 **855/855** under B. F4 still unsigned.


## W2-B / Wave 006 (updated 2026-09-13T23:38:44Z)
TEST-20260913-007 REDUNDANT / FAIL-INSUFFICIENT (one-asset invert). FEAT-20260913-007 INACTIVE. Wave 006 closed.
BTC T-5m N=254 ΔBrier=−0.000690 ΔLogLoss=−0.001818 PROMISING. ETH N=240 ΔBrier=+0.000330 ΔLogLoss=+0.000057 kill.
No BTC-only. No λ retune. Mid incumbent. F4 Sep-12 855/855 unsigned next leftover.


## F4 kill / Wave 009 close (2026-09-14T01:12:05Z)
TEST-20260914-001 REDUNDANT / FAIL-INSUFFICIENT. N_wick BTC 12 / ETH 10 < 80. No cemetery. No θ/W/λ retune. Mid incumbent.
Next: follow-vs-fade NEEDS_DATA (PM-006 38 closed 15m; PM-008 Kalshi live mid kicked). Squeeze extract filed, not a wave.
