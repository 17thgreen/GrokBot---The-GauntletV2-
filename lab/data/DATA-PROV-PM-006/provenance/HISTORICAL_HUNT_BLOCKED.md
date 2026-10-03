# DATA-PROV-PM-006 — Historical bid/ask hunt (BLOCKED)

**DATA_ID:** DATA-PROV-PM-006  
**Window sought:** 2026-09-04 → 2026-09-11 UTC (PM-003 / PM-005 pairing window)  
**Target:** Polymarket YES best bid + best ask snapshots with timestamps (so mid=(bid+ask)/2 is not invented) for BTC/ETH 15m Up/Down  
**Stamp:** 2026-09-13T20:25Z (box probes)  
**Verdict:** **BLOCKED** — no free public source returns historical bid+ask for this window.  
**Trade / auth:** FORBIDDEN / none. Paid vendors not used.

## Method

Real HTTP probes from this box. No invented quotes. Last-trade (`/prices-history`) is **not** treated as mid.

Reference historical YES token (PM-005 raw):  
`11862021886282096742243011293088924092955028730250907544249148111484298656607`  
slug `btc-updown-15m-1788877800`.

Unix window: `startTs=1788480000` (2026-09-04T00:00Z) → `endTs=1789171140` (2026-09-11T23:59Z).

## Probe log (exact)

| Endpoint | Params / note | HTTP | Body summary |
|----------|---------------|-----:|--------------|
| `GET https://clob.polymarket.com/orderbook-history` | `asset_id=<hist YES>&startTs=1788480000&endTs=1789171140&limit=10` | **200** | `{"count":0,"data":[]}` — empty for PM-003 window |
| `GET https://clob.polymarket.com/orderbook-history` | `token_id=<hist YES>&…` | **400** | `either market or asset_id must be provided` |
| `GET https://clob.polymarket.com/orderbook-history` | `market=<hist YES>&…` | **400** | same |
| `GET https://clob.polymarket.com/orderbook-history` | live current YES token + live window | **200** | `{"count":0,"data":[]}` — endpoint alive but produces no snapshots |
| `GET https://clob.polymarket.com/book?token_id=<hist YES>` | resolved market | **404** | `No orderbook exists for the requested token id` |
| `GET https://clob.polymarket.com/midpoint?token_id=<hist YES>` | | **404** | same |
| `GET https://clob.polymarket.com/spread?token_id=<hist YES>` | | **404** | same |
| `GET https://clob.polymarket.com/book-history?token_id=…` | | **404** | nginx HTML |
| `GET https://clob.polymarket.com/timeseries?token_id=…` | | **404** | nginx HTML |
| `GET https://clob.polymarket.com/books?token_id=…` | | **400** | `Invalid payload` |
| `GET https://clob.polymarket.com/prices-history?market=<hist YES>&startTs=…&endTs=…&fidelity=1` | | **200** | history of `{t,p}` **last trade only** — not bid/ask |
| `GET https://clob.polymarket.com/last-trade-price?token_id=<hist YES>` | | **200** | last trade price only |
| `GET https://data-api.polymarket.com/trades?asset=<hist YES>&limit=3` | | **200** | returns **unrelated live** trades (asset filter ignored / wrong) — trades, not books |
| `GET https://data-api.polymarket.com/trades?market=<hist YES>` | | **200** | `[]` |
| `GET https://data-api.polymarket.com/orderbook` | | **404** | `page not found` |
| `GET https://data-api.polymarket.com/books` | | **404** | `page not found` |
| `GET https://data-api.polymarket.com/book?token_id=…` | | **404** | earlier probe |
| `GET https://gamma-api.polymarket.com/markets?clob_token_ids=<hist YES>` | | **200** | `[]` (closed markets not returned by default) |
| `GET https://r2.pmxt.dev/` and `/2026-09-04/` | OSS mirror cited by HF readme | **404** | Cloudflare Not Found |
| `GET https://r2v2.pmxt.dev/` and `/2026-09-04.parquet` | | **404** | same |
| `GET https://r2v2.pmxt.dev/orderbook/2026-09-04.parquet` | | **404** | same |
| `GET https://api.pmxt.dev/` | | **404** | Cannot GET / |
| `GET https://huggingface.co/api/datasets/Joseph3222/polymarket-orderbook` | free CC-BY parquet | **200** | dataset exists |
| HF tree `orderbook_1min/` | recursive list | **200** | **328** day partitions; **last day = 2026-08-10**; **0** paths containing `2026-09` |
| HF tree `orderbook/` | | **200** | same cutoff: `date=2026-08-10` last |

## What live APIs prove (control)

Same box, current BTC 15m Up token:  
`GET /book?token_id=<live>` → **200** with non-empty `bids`/`asks` and `timestamp`.  
`GET /midpoint?token_id=<live>` → **200** `{"mid":"…"}`.  
So live book is gettable; historical book for resolved 15m tokens is not.

## Conclusion

| Path | Result for Sep 4–11 2026 bid+ask |
|------|----------------------------------|
| Official CLOB `/orderbook-history` | Empty (`count:0`) — decommissioned ingestion |
| Official CLOB `/book` | Live only; hist token **404** |
| Official `/prices-history` | Last trade ≠ bid/ask |
| data-api.polymarket.com | Trades / no book hist |
| pmxt R2 free mirror | **404** for Sep |
| HF Joseph3222/polymarket-orderbook | Free but **ends 2026-08-10** — misses PM-003 window |
| Paid Struct/Resolved/DepthFeed/etc. | **FORBIDDEN** by order — not probed for purchase |

**HISTORICAL bid+ask for the PM-003 window is NOT GETTABLE on free public paths probed above.**  
Forward path only: live capture under this DATA_ID (see `FORWARD_CAPTURE.md`).

## Forbidden interpretations (explicit)

- Do **not** treat `/prices-history` last as mid.  
- Do **not** invent bid/ask from outcomePrices / Gamma.  
- Do **not** backfill from HF Aug data and label it Sep.  
- Do **not** Examiner-score or READY a Feature from this note.
