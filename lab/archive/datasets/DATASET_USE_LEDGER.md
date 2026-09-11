# DATASET_USE_LEDGER (active)

**Template:** `archive/templates/DATASET_USE_LEDGER.md`  
**Status:** ACTIVE — empty (headers only) as of 2026-09-11  
**Maintainer:** Archivist  

**Hard rule:** Once a slice is used for hypothesis tuning, it cannot later be called sealed validation. See template.

---

| DATA_ID | SLICE_ID | START | END | USED_BY | PURPOSE | RESEARCH? | VALIDATION? | HOLDOUT? | FORWARD? | FIRST_OPENED | WHO_OPENED | STATUS |
|---------|----------|-------|-----|---------|---------|-----------|-------------|----------|----------|--------------|------------|--------|
| DATA-PROV-PM-002 | SLICE-PM002-BOUNDED-240 | 2026-09-04 | 2026-09-11 | Examiner | MARKET_BASELINE calibration of Kalshi mid (primary freeze) | YES | NO | NO | NO | 2026-09-11 | Conductor | OPEN_RESEARCH |
| DATA-PROV-PM-002 | SLICE-PM002-BOUNDED-240 | 2026-07-13 (approx; parent PM-001 post-cutoff) | 2026-09-11 | Conductor fetch | reconstruct decision-time \(m_t\) at remaining-time checkpoints | NO | NO | NO | NO | 2026-09-11 | Conductor | CAPTURED_PENDING_CLOCK |
