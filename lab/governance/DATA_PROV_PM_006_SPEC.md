# DATA-PROV-PM-006 — Polymarket live YES bid/ask forward capture

**Class:** DATA spec. Not a Feature. Not an Examiner commission.  
**Date:** 2026-09-13  
**Trade:** FORBIDDEN  
**Auth:** none (public Gamma + CLOB). No keys. No orders. No wallet.

## Why
Governor Hold W2-B: Poly last-print ≠ same-t mid. Official live book exists (`GET /book?token_id=`); historical free bid/ask for the PM-003 window is **BLOCKED** (see `data/DATA-PROV-PM-006/provenance/HISTORICAL_HUNT_BLOCKED.md`). This DATA_ID registers **live forward capture** of real best bid + best ask so mid=(bid+ask)/2 is observed, not invented.

## Register
- **DATA_ID:** DATA-PROV-PM-006
- **Venue:** POLYMARKET_GLOBAL (CLOB)
- **Product:** BTC/ETH Up/Down **15m** Up-token books (5m captured if cheap)
- **Fields (signal):** `best_bid`, `best_ask`, `mid` only when **both** sides present; `book_timestamp` (venue); `local_receipt_time`; `token_id`; `slug`; `asset`; `window_start_unix`; `window_secs`
- **Omit** missing sides — do not invent; do not fill mid from last trade or Gamma outcomePrices
- **Mode:** FORWARD_CAPTURE_ONLY for hist window; live poll of `/book`
- **Paths:** `data/DATA-PROV-PM-006/raw/book/YYYY-MM-DD.jsonl` append-only

## Forbidden
Invented mid · treating last as mid · paid Struct/Resolved/DepthFeed purchase · Kalshi orders · Examiner · READY Feature · secrets in files

## Related
- Hold: `governance/GOVERNOR_HOLD_W2B_2026-09-13.md`
- Hist BLOCKED: `data/DATA-PROV-PM-006/provenance/HISTORICAL_HUNT_BLOCKED.md`
- Template: `data/DATA-PROV-LIQ-001/provenance/FORWARD_CAPTURE.md`
