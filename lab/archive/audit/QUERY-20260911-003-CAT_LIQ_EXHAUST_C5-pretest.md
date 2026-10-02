# Pre-test search — QUERY-20260911-003

- **Requested by:** The Catalyst
- **Date (UTC):** 2026-09-11
- **Assigned EDGE_ID:** EDGE-20260911-003
- **Informal:** CAT_LIQ_EXHAUST_C5
- **Proposed thesis (normalized):** Actual liq-notional burst (venue events) + same-dir impulse + Decel → fade (−d) at 5/10/15m separately with incremental skill beyond matched OHLCV and ordinary trade-flow (CEM-20260911-001/002). BTC/ETH separate. [H]
- **Markets / horizons / venue:** BTC|ETH separate; 5/10/15m separate; provisional Binance USD-M [A]
- **Key features:** Cycle 5 Catalyst event/positioning; DATA family DATA-PROV-LIQ-001 (+ DATA-PROV-001; optional TRADES-001 Decel only)

## Exact duplicate
- no

## Semantic equivalent
- no — not a rename of CEM Tape/OHLCV kills; event-label claims with mandatory redundancy controls

## Parameter rename only
- no

## Related
- EDGE-20260910-009 (VERSIONED_CHILD); CEM-20260911-001/002 (Tape incremental FAIL — redundancy contrast, not retune); CEM-20260910-001/002/003 (OHLCV dead — event claims must not be OHLCV rewrite); EDGE-20260910-005/006 frozen L2 — out of scope

## Prior failures
- CEM-20260911-001 NO_EDGE/COST_KILLED (trade-count residual)
- CEM-20260911-002 NO_EDGE (+ ETH OHLCV-redundant large-trade)
- CEM-20260910-001/002/003 OHLCV family

## Verdict
**WARN_RELATED**

## Notes
Versioned child of EDGE-20260910-009 (KEEP AS HYPOTHESIS, body preserved). Not duplicate of CEM Tape/OHLCV — distinct DATA-PROV-LIQ-001 event labels + redundancy controls. Eligible pending LIQ DATA-* + Clock.
DATA-* named required/[U] — dataset files **not** invented. No L2. No 005/006 rewrite. No Cartographer rescue of dead Tape.
Parents 009/010 unchanged KEEP AS HYPOTHESIS.
