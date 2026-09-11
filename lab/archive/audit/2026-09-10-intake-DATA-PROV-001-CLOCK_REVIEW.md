# Audit — DATA-PROV-001 intake → CLOCK_REVIEW

- **UTC:** 2026-09-10
- **Actor:** The Archivist
- **Source:** The Conductor
- **Event:** DATASET_INTAKE
- **DATA_ID:** DATA-PROV-001
- **New STATUS:** CLOCK_REVIEW
- **[V]** Paths present: raw + provenance + sealed + slices
- **[V]** Hashes verified (raw vs provenance; slices/holdout/warmup vs SEAL_LOCK)
- **[V]** 595872×2 rows; 0 gaps (per DOWNLOAD_MANIFEST + Conductor)
- **[V]** API fallback www.binance.com (451 on fapi.binance.com) recorded in manifest
- **[V]** SEAL_LOCK.json sealed_utc=2026-09-10T23:28:20.943919+00:00; final 20% locked
- **[V]** INDEX updated with date spans only for holdout (no contents)
- **[V]** Examiner blocked until Clock verdict
- **[V]** Not venue marriage — provisional reference only
