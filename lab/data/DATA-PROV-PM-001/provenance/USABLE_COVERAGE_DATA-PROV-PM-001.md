# USABLE COVERAGE — DATA-PROV-PM-001
**Clock:** 2026-09-11T20:53:10Z  
**Verdict:** CONDITIONAL — label-only

## Freeze rule
Evaluate strata separately. Use RESOLUTION only at/after RESOLVE_TIME. No venue pooling without adapter tags. No books/mid. No independent oracle claim.

## Strata windows
(see DATA_VERDICT table)

## Explicitly not covered
- Historical order books
- Decision-time mid paths
- Independent CF/Chainlink replay
- Pre-cutoff Kalshi deep hist (smoke only in raw/)
- Sealed holdout protocol
