# DATASET_USE_LEDGER (active)

**Template:** `archive/templates/DATASET_USE_LEDGER.md`  
**Maintainer:** Archivist  

**Hard rule:** Once a slice is used for hypothesis tuning, it cannot later be called sealed validation.

---

| DATA_ID | SLICE_ID | START | END | USED_BY | PURPOSE | RESEARCH? | VALIDATION? | HOLDOUT? | FORWARD? | FIRST_OPENED | WHO_OPENED | STATUS |
|---------|----------|-------|-----|---------|---------|-----------|-------------|----------|----------|--------------|------------|--------|
| DATA-PROV-CF-001 | SLICE-CF001-PM003-CLOSE-1208 | 2026-09-04 | 2026-09-11 | Examiner TEST-20260913-001 | F2 Map 2 incrementality vs T−1m mid | YES | NO | NO | NO | 2026-09-13 | Conductor | USED_RESEARCH — not holdout |
| DATA-PROV-PM-003 | SLICE-PM003-KALSHI-REMAIN-1208 | 2026-09-04 | 2026-09-11 | Examiner TEST-20260911-007 | MARKET_BASELINE (used) | YES | NO | NO | NO | 2026-09-11 | Conductor | USED_RESEARCH — not holdout |
| DATA-PROV-PM-003 | SLICE-PM003-KALSHI-REMAIN-1208 | 2026-09-04 | 2026-09-11 | Conductor fetch | reconstruct remaining Kalshi 15m m_t | NO | NO | NO | NO | 2026-09-11 | Conductor | CAPTURED_PENDING_CLOCK |
| DATA-PROV-PM-002 | SLICE-PM002-BOUNDED-240 | 2026-09-04 | 2026-09-11 | Examiner TEST-20260911-006 | MARKET_BASELINE (used) | YES | NO | NO | NO | 2026-09-11 | Conductor | USED_RESEARCH — not holdout |
