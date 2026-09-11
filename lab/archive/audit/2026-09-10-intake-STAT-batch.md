# Audit — Statistician Cycle 0 intake

- **UTC:** 2026-09-10
- **Actor:** The Archivist
- **Event:** EDGE_INTAKE_BATCH
- **Originator:** The Statistician (via Conductor)

## Informal ↔ canonical map

| Informal | EDGE_ID | Role | Pre-test verdict |
|----------|---------|------|------------------|
| STAT_003A | EDGE-20260910-001 | PRIMARY | CLEAR_TO_TEST |
| STAT_001 | EDGE-20260910-002 | RESERVE | WARN_RELATED |
| STAT_002 | EDGE-20260910-003 | RESERVE | CLEAR_TO_TEST |
| STAT_004 | EDGE-20260910-004 | RESERVE | CLEAR_TO_TEST |

## Lab-wide blockers (unchanged)
- market-data path [U]
- venue [U]
- cost model [U]
- sealed holdout [U]

**[V]** No RESEARCH TEST routing performed.
**[V]** Cemetery still empty of failures; WARN_RELATED is intra-batch (STAT_001 ↔ STAT_003A).
