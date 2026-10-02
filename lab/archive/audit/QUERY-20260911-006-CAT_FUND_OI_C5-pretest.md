# Pre-test search — QUERY-20260911-006

- **Requested by:** The Catalyst
- **Date (UTC):** 2026-09-11
- **Assigned EDGE_ID:** EDGE-20260911-006
- **Informal:** CAT_FUND_OI_C5
- **Proposed thesis (normalized):** Sustained funding extreme AND elevated OI at t → against crowded side at 5/10/15m with incremental skill beyond funding-only, OI-only, OHLCV, and trade-flow nested. BTC/ETH separate. [H]
- **Markets / horizons / venue:** BTC|ETH separate; 5/10/15m separate; provisional Binance USD-M [A]
- **Key features:** Cycle 5 Catalyst event/positioning; DATA family DATA-PROV-FUNDING-001 + DATA-PROV-OI-001 + DATA-PROV-001

## Exact duplicate
- no

## Semantic equivalent
- no — not a rename of CEM Tape/OHLCV kills; event-label claims with mandatory redundancy controls

## Parameter rename only
- no

## Related
- EDGE-20260910-010 (VERSIONED_CHILD); CEM-20260911-001/002 (Tape incremental FAIL — redundancy contrast, not retune); CEM-20260910-001/002/003 (OHLCV dead — event claims must not be OHLCV rewrite); EDGE-20260910-005/006 frozen L2 — out of scope

## Prior failures
- CEM-20260911-001 NO_EDGE/COST_KILLED (trade-count residual)
- CEM-20260911-002 NO_EDGE (+ ETH OHLCV-redundant large-trade)
- CEM-20260910-001/002/003 OHLCV family

## Verdict
**WARN_RELATED**

## Notes
Versioned child of EDGE-20260910-010 (KEEP AS HYPOTHESIS, body preserved). Interaction must beat funding-only sibling. Eligible pending FUNDING+OI DATA-* + Clock.
DATA-* named required/[U] — dataset files **not** invented. No L2. No 005/006 rewrite. No Cartographer rescue of dead Tape.
Parents 009/010 unchanged KEEP AS HYPOTHESIS.
