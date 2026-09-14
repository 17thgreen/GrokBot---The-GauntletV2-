# Catalyst coverage freeze proposal — Clock 2026-09-11T04:39:57Z

Issued with DATA VERDICTs: FUNDING-001 CONDITIONAL · OI-001 CONDITIONAL · LIQ-001 HISTORICAL_DATA_BLOCKED.

## FUNDING-001 usable coverage
Align to DATA-PROV-001 SEAL_LOCK open-time windows (not reshaped):
- RESEARCH 2021-01-03T04:00 → 2024-05-27T06:15
- VALIDATION 2024-05-27T06:20 → 2025-07-14T15:00
- HOLDOUT 2025-07-14T15:05 → 2026-08-31T23:55

## OI-001 / joint Catalyst
**Catalyst_COMMON_WINDOW:** 2021-12-01T00:00:00Z → 2026-08-31T23:55:00Z

**Preferred:** clip SEAL_LOCK research start to 2021-12-01T00:00 for joint BTC/ETH OI features; leave validation/holdout bounds unchanged; do not rewrite sealed OHLCV parquet.

**BTC-only OI:** full SEAL_LOCK span allowed with ETH abstention before 2021-12-01.

## LIQ-001
No historical seal coverage. Forward capture only from ~2026-09-11T04:23Z.
