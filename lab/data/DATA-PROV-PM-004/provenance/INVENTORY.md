# DATA-PROV-PM-004 — Inventory

**as_of_utc:** 2026-09-13T18:45:22Z
**finished_at_utc:** 2026-09-13T18:46:21Z
**cutoff:** open_time > `2026-09-11T20:15:00Z` (after PM-003 end)

## Query method

- Base: `https://api.elections.kalshi.com/trade-api/v2` (public, no key)
- `GET /markets?series_ticker={KXBTC15M|KXETH15M}&status={open|settled|closed}&limit=200` + cursor pagination
- Filter: `open_time > 2026-09-11T20:15:00Z`; dedupe by ticker across status queries
- Pace: 2s between pages; 429 backoff (1×429 on ETH settled page 2, recovered)
- No Trade API keys, no CF Benchmarks, no trades

## Counts (real API — not invented)

| metric | N |
|---|---|
| BTC (KXBTC15M) | 185 |
| ETH (KXETH15M) | 186 |
| total | 371 |
| resolved | 369 |
| still-open (status active/open) | 1 |
| closed_unsettled | 1 |
| not-yet-resolved (open + closed_unsettled) | 2 |

### status_class_counts

```json
{
  "resolved": 369,
  "closed_unsettled": 1,
  "still_open": 1
}
```

Classification: `resolved` = finalized/settled or result yes/no; `still_open` = active|open; `closed_unsettled` = closed without result.

## Open-time range

- first_open_utc: `2026-09-11T20:30:00Z`
- last_open_utc: `2026-09-13T18:45:00Z`

### Non-resolved tickers at as-of

- `KXBTC15M-26SEP131445-45` CLASS=closed_unsettled OPEN=2026-09-13T18:30:00Z CLOSE=2026-09-13T18:45:00Z STATUS_RAW=closed
- `KXETH15M-26SEP131500-00` CLASS=still_open OPEN=2026-09-13T18:45:00Z CLOSE=2026-09-13T19:00:00Z STATUS_RAW=active

## API errors

- none (hard failures)
- n429 during inventory: 1

## Binance Vision 1m (L3-002) — listability only

HTTP HEAD only (no zip download):

| symbol | date | http | content_length | listable |
|---|---|---|---|---|
| BTCUSDT | 2026-09-12 | 200 | 63357 | True |
| BTCUSDT | 2026-09-13 | 404 | None | False |
| ETHUSDT | 2026-09-12 | 200 | 63684 | True |
| ETHUSDT | 2026-09-13 | 404 | None | False |

- **2026-09-12:** listable (HTTP 200, ~63KB) for BTCUSDT and ETHUSDT — download deferred.
- **2026-09-13:** NOT listable yet (HTTP 404 both) — in-progress UTC day; same Vision lag pattern as L3-001 for Sep-11.

## Paths

- `/workspace/lab/data/DATA-PROV-PM-004/provenance/INVENTORY.json`
- `/workspace/lab/data/DATA-PROV-PM-004/provenance/INVENTORY.md`
- `/workspace/lab/data/DATA-PROV-PM-004/provenance/FETCH_SUMMARY.json`
- `/workspace/lab/data/DATA-PROV-PM-004/provenance/universe_after_cutoff.ndjson`
- `/workspace/lab/data/DATA-PROV-PM-004/provenance/inventory_pm004.py`
- `/workspace/lab/data/DATA-PROV-PM-004/raw/kalshi_markets/` (listing pages)
- `/workspace/lab/data/DATA-PROV-PM-004/raw/binance_vision_listing/listing_head.json`

## Notes

- Cutoff exclusive: open_time > 2026-09-11T20:15:00Z (PM-003 last included that open).
- BTC n=185 vs ETH n=186: at as-of, ETH had an active 18:45Z window; BTC's matching active window was not returned by status=open (only prior 18:30Z closed_unsettled).
- One 429 on KXETH15M settled page 2; recovered after backoff.
- Candle/candlestick fetch NOT started; listing pages only under raw/kalshi_markets.
- No Trade API key, no CF Benchmarks, no trades, no Clock, no Examiner.

## Not done (per order)

- No Clock-clear, no Examiner, no CF ticks, no strategy scoring, no invented numbers, no candle batch fetch yet.

