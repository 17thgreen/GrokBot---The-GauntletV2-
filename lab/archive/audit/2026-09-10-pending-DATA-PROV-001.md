# Audit — pending DATA-PROV-001 intake

- **UTC:** 2026-09-10
- **Actor:** The Archivist
- **Source:** The Conductor
- **Event:** DATASET_PENDING
- **DATA_ID:** DATA-PROV-001
- **[V]** Expect: Binance USD-M BTCUSDT/ETHUSDT 5m, 2021-01-01→2026-08-31 UTC, provisional reference only
- **[V]** Expect under `/workspace/lab/data/DATA-PROV-001/`: raw immutable + sha256 + manifest
- **[V]** Scaffold exists; files not yet present
- **[V]** HARD GATE: do not open research slices until Conductor seals final 20% AND Clock verdicts
- **Linked:** PROV-MEAS-20260910-001 / EDGE-20260910-001


## RESOLVED → CLOCK_REVIEW
- Fetch complete; SEAL_LOCK present; Archivist integrity re-verify PASS.
- See audit/2026-09-10-intake-DATA-PROV-001-CLOCK_REVIEW.md
