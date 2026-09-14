# DATA-PROV-PM-008 — Kalshi 15m live yes bid/ask forward capture

**Class:** DATA spec. Not a Feature. Not Examiner.
**Stamp:** 2026-09-14T01:12:05Z
**Trade:** FORBIDDEN
**Auth:** none (public `api.elections.kalshi.com`). No Trade key. No orders.

## Why
Follow-vs-fade needs Kalshi same-t mid on the live PM-006 span. Historical Poly books are BLOCKED. PM-003/004 do not cover this forward window.

## Register
- **DATA_ID:** DATA-PROV-PM-008
- **Venue:** KALSHI
- **Product:** open `KXBTC15M` / `KXETH15M`
- **Fields:** `yes_bid`, `yes_ask`, `mid` only when both sides present; `ticker`; `open_time`; `close_time`; `local_receipt_time`
- **Source:** `GET /trade-api/v2/markets?series_ticker=&status=open` (`yes_bid_dollars` / `yes_ask_dollars`)
- **Omit** missing sides — do not invent from last
- **Paths:** `data/DATA-PROV-PM-008/raw/mid/YYYY-MM-DD.jsonl`

## Forbidden
Trade API key use · orders · Examiner · treating last as mid · CF

## Ops note (2026-09-14 pulse)
Default `PM008_POLL_S=2.0` drew Kalshi HTTP 429s. Running capture uses `PM008_POLL_S=8.0`. Still public-only; no Trade key.
