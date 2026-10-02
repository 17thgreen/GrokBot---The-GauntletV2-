# Pre-test search — QUERY-20260911-004

- **Requested by:** The Catalyst
- **Date (UTC):** 2026-09-11
- **Assigned EDGE_ID:** EDGE-20260911-004
- **Informal:** CAT_OI_SHOCK_C5
- **Proposed thesis (normalized):** Large |ΔOI| shock with small contemporaneous |r| (OI-price divergence) at t, then first directional aggression within T_wait → flush-direction forward 5/10/15m with incremental skill beyond OHLCV and trade-flow. BTC/ETH separate. [H]
- **Markets / horizons / venue:** BTC|ETH separate; 5/10/15m separate; provisional Binance USD-M [A]
- **Key features:** Cycle 5 Catalyst event/positioning; DATA family DATA-PROV-OI-001 (+ DATA-PROV-001; optional TRADES trigger)

## Exact duplicate
- no

## Semantic equivalent
- no — not a rename of CEM Tape/OHLCV kills; event-label claims with mandatory redundancy controls

## Parameter rename only
- no

## Related
- CEM-20260911-001/002 (Tape incremental FAIL — redundancy contrast, not retune); CEM-20260910-001/002/003 (OHLCV dead — event claims must not be OHLCV rewrite); EDGE-20260910-005/006 frozen L2 — out of scope

## Prior failures
- CEM-20260911-001 NO_EDGE/COST_KILLED (trade-count residual)
- CEM-20260911-002 NO_EDGE (+ ETH OHLCV-redundant large-trade)
- CEM-20260910-001/002/003 OHLCV family

## Verdict
**CLEAR_TO_TEST**

## Notes
New atomic; no parent EDGE. Cites cemetery for redundancy — not a retune. Eligible pending OI DATA-* + Clock.
DATA-* named required/[U] — dataset files **not** invented. No L2. No 005/006 rewrite. No Cartographer rescue of dead Tape.
Parents 009/010 unchanged KEEP AS HYPOTHESIS.
