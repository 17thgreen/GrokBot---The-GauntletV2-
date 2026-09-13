# DATA-PROV-PM-005 — Polymarket Global 15m last-print (W2-B substrate)

**Class:** DATA spec. Not a Feature. Not an Examiner commission.
**Date:** 2026-09-13
**Trade:** FORBIDDEN
**Auth:** none (public CLOB prices-history / gamma). No keys. No books invented.

## Why
W2-B needs a same-t Poly print next to PM-003 Kalshi 15m mid. PM-002 Poly 15m last is Clock-tagged `CLEARED_WEAKER_LAST_PRINT` but n≈30/asset and must not be silently unioned with PM-003.

## Register
- Venue: POLYMARKET_GLOBAL
- Product: BTC/ETH Up/Down **15m** only (not 5m this spec)
- Checkpoints: rem ∈ {300} headline; {600, 840} captured if cheap, **dark** (no annex shop)
- Method: last print with obs_time ≤ decision_time. **Not mid.** Bid/ask null → do not invent quotes.
- Universe: resolved contracts whose OPEN overlaps PM-003 Kalshi 15m opens (2026-09-04T20:15Z → 2026-09-11T20:15Z) as far as public history allows
- Pairing key: asset + window length + closest OPEN/CLOSE to the Kalshi contract; Clock names the legal match rule

## Forbidden
Invented mid · T−0 last as forecast · pooling with Kalshi · Trade API · CF · orders

## Next
Inventory first (what PM-001 raw already has). Fetch remainder. Clock join vs PM-003 T-5m mid. Coverage target: enough for N≥80 per headline after TEST-007 excludes, or write UNTESTED / FAIL-INSUFFICIENT honestly.
