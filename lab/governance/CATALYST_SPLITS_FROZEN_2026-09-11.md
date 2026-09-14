# Catalyst splits FROZEN — 2026-09-11

**Authority:** Conductor lock after Clock DATA VERDICTs (FUNDING-001 CONDITIONAL, OI-001 CONDITIONAL).  
**RETROACTIVE:** NO. No post-result boundary adjustment.  
**Source proposal:** `CATALYST_COVERAGE_FREEZE_PROPOSAL_2026-09-11.md`

## Joint BTC+ETH Catalyst window (OI-bearing / joint edges)

| Slice | Start (UTC) | End (UTC) |
|-------|-------------|-----------|
| RESEARCH | 2021-12-01T00:00:00Z | 2024-05-27T06:15:00Z |
| VALIDATION | 2024-05-27T06:20:00Z | 2025-07-14T15:00:00Z |
| HOLDOUT | 2025-07-14T15:05:00Z | 2026-08-31T23:55:00Z |

Notes:
- Research start clipped to ETH OI Vision availability (2021-12-01). Validation/holdout bounds match OHLCV SEAL_LOCK. Do **not** reshape sealed OHLCV parquets.
- Holdout LOCKED until Conductor opens protocol.

## Funding-only (EDGE-005) — full SEAL_LOCK open bounds

| Slice | Start (UTC) | End (UTC) |
|-------|-------------|-----------|
| RESEARCH | 2021-01-03T04:00:00Z | 2024-05-27T06:15:00Z |
| VALIDATION | 2024-05-27T06:20:00Z | 2025-07-14T15:00:00Z |
| HOLDOUT | 2025-07-14T15:05:00Z | 2026-08-31T23:55:00Z |

## Examiner gates
- SORT+DEDUPE OI before features (Clock).
- Funding SIGNAL only if `calc_time ≤ t`; no premiumIndex / predicted funding.
- Incremental controls vs OHLCV ± trade-flow; BTC/ETH and 5/10/15m separate.
- EDGE-20260911-003 HISTORICAL_DATA_BLOCKED (LIQ).
- CLEARED for provisional measurement: EDGE-20260911-004, 005, 006.
