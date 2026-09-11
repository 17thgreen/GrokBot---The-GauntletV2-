# Pre-test search — QUERY-20260910-009

- **Requested by:** originator on card
- **Date (UTC):** 2026-09-10
- **Assigned EDGE_ID:** EDGE-20260910-009
- **Informal:** CAT_LIQ_EXHAUST
- **Thesis:** Conditional on a liquidation-notional burst in the same direction as price over a completed window ending at t, and conditional on aggressive same-direction flow decelerating by t, the forward 5/10/15m return mean-revert...

## Exact duplicate
- no [V]

## Semantic equivalent
- no duplicate of 001 [I]. Contrast/placebo vs EDGE-20260910-003 (range snapback without liq label) — related family of mean-reversion after expansion but liq label is load-bearing; not parameter rename.

## Parameter rename only
- no

## Related
- EDGE-20260910-001 orthogonal; EDGE-20260910-003 contrast/placebo (range snapback w/o liq); EDGE-20260910-005 (Tape burst fade) related microstructure/exhaustion family but liq-feed-specific

## Prior failures
- none [V]

## Verdict
CLEAR_TO_TEST

## Notes
Orthogonal to Low-RV continuation. WARN-level relatedness to range-snapback/Tape fade noted but liq label + deceleration gate make it atomic. HYPOTHESIS only.
