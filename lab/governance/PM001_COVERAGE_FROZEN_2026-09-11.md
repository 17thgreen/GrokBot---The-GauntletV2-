# DATA-PROV-PM-001 coverage FROZEN — 2026-09-11

**Clock verdict:** CONDITIONAL (APPROVED_WITH_LIMITATIONS).  
**RETROACTIVE:** NO.

## Allowed use
- Label-only research by **venue × asset × horizon** strata.
- RESOLUTION knowable only at/after RESOLVE_TIME (else LOOKAHEAD).
- Settlement = VENUE_DECLARED; independent oracle replay UNTESTED.

## Forbidden until new DATA-* / Clock
- Treat LAST_PRICE / terminal OUTCOME_PRICES as decision-time m_t
- Historical books / mid-path
- Independent CF BRTI / Chainlink TWAP recompute as ground truth
- Unlabeled pooling across venues
- Trading / sealed-holdout claim / Strategy League

## Usable windows [V] Clock
| Venue | Strata | OPEN ≥ | CLOSE ≤ | N |
|-------|--------|--------|---------|---|
| KALSHI | BTC 15m | 2026-09-04T20:45Z | 2026-09-11T20:45Z | 664 |
| KALSHI | ETH 15m | 2026-09-04T20:45Z | 2026-09-11T20:45Z | 664 |
| POLYMARKET_GLOBAL | BTC+ETH 5m+15m | ~2026-09-08T14:30Z | ~2026-09-11T20:40Z | 2496 (5m-heavy) |

Source: `data/DATA-PROV-PM-001/provenance/USABLE_COVERAGE_DATA-PROV-PM-001.md`
