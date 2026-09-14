# DATA-PROV-PM-009 — PolyOrderbooks Starter L2 (bounded history)

**Class:** DATA spec. Not a Feature. Not Examiner.
**Stamp:** 2026-09-14T03:50Z
**Trade:** FORBIDDEN
**Auth:** Starter API key on disk (`/home/box/.secrets/POLYORDERBOOKS_API_KEY`). Do not paste. Do not commit.

## Why
Follow-vs-fade needs historical Poly L2 / TOB for book velocity. Official CLOB history for Sep 4–11 remains BLOCKED.
Starter key is live. Live probe 2026-09-14T03:46Z:

- Sep 4–11 books: **HTTP 403** — "History window exceeds your starter plan (max 3 days). Earliest allowed start_ts is 2026-09-11T03:46:02Z."
- Sep 12 16:00Z `btc-updown-15m` books: **HTTP 200**, full L2 ladders at 1s (`bids`/`asks` as `[price, size]`).
- `GET /v1/usage`: plan=starter, 1s allowed, max_history_days=3, 60/min, 1,000/day.

Sep 12 is the PM-004 / F4 week. It ages off this 3-day window ~2026-09-15T03:46Z. Pull now. Do not wait for $19.

## Register
- **DATA_ID:** DATA-PROV-PM-009
- **Vendor:** PolyOrderbooks archive (not live CLOB)
- **Product:** `btc-updown-15m-*` / `eth-updown-15m-*`
- **Resolution this pull:** `1m` (last book in each minute). 1s would burn the daily cap (~5 pages × 192 markets).
- **Window:** closed 15m markets with start_ts ≥ earliest Starter bound, through last fully closed window.
- **Fields kept:** `t`, Yes/No `bids`/`asks` ladders. Derive TOB mid only when both sides exist. Do not invent from last.
- **Paths:** `data/DATA-PROV-PM-009/raw/books/{slug}.json`

## Caps
- 60 req/min, 1,000/day. Sleep ≥1.1s. Stop if 429.
- Do not upgrade. Do not burn Backtest AI credit from this job.

## Forbidden
Trade · Examiner Δ from this tape alone · treat vendor P&L as a gate · commit the key · paid checkout
