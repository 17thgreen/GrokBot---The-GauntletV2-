# Audit — Tape Reader Cycle 4 resubmit confirm

- **UTC:** 2026-09-11
- **Actor:** The Archivist
- **Event:** CARD_UPGRADE_EXISTING_IDS
- **[V]** Conductor/Tape “not in registry / still 10 edges” was stale — archive has 12 edges including EDGE-20260911-001/EDGE-20260911-002
- **[V]** TR_FLOW_CNT_01 → EDGE-20260911-001 CLEAR_TO_TEST (QUERY-20260911-001) — card upgraded from full resubmit
- **[V]** TR_FLOW_LRG_01 → EDGE-20260911-002 CLEAR_TO_TEST (QUERY-20260911-002) — resubmit truncated again at SIGNAL; no new ID; await complete tail
- **[V]** EDGE-005/006 frozen unchanged
