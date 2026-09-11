# Pre-test search — QUERY-20260911-002

- **Requested by:** The Tape Reader
- **Date (UTC):** 2026-09-11
- **Assigned EDGE_ID:** EDGE-20260911-002
- **Informal:** TR_FLOW_LRG_01
- **DATA family:** DATA-PROV-TRADES-001

## Exact duplicate
- no [V]

## Semantic equivalent
- no prior trade-flow EDGE in archive [V]. Distinct from CEM-001/002/003 (OHLCV-only failures). Distinct from EDGE-005/006 (L2-blocked; not rewritten).

## Parameter rename only
- no

## Related
- CEM-20260910-001 (001 NO_EDGE); CEM-20260910-002 (003 COST_KILLED); CEM-20260910-003 (004 NO_EDGE)
- Companion Cycle-4 trade-flow peer (other of EDGE-20260911-001/EDGE-20260911-002)
- EDGE-20260910-005/006 frozen — related microstructure intent, different data requirement

## Prior failures
- Cemetery as cited — lessons: OHLCV clones dead; cost fragility (CEM-002); placebos/controls (CEM-003)

## Verdict
CLEAR_TO_TEST

## Notes
Large-trade clustering+persistence — related companion to EDGE-20260911-001; not duplicate; not L2-005/006. Cemetery cited. Card truncated mid-ENTRY; filed with Archivist completion pending confirm.
HYPOTHESIS only. No RESEARCH TEST until DATA-PROV-TRADES-001 Clock-cleared + Conductor route.
