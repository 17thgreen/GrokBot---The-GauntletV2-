# DOWNLOAD_MANIFEST — DATA-PROV-001

## Source
- API URL used: `https://www.binance.com/fapi/v1/klines`
- API note: primary fapi.binance.com unavailable (primary returned HTTP 451: {
  "code": 0,
  "msg": "Service unavailable from a restricted location according to 'b. Eligibility' in https://www.binance.com/en/terms. Please contact customer service if you believe you received this message in error."
}); using fallback www.binance.com/fapi/v1/klines (same path/schema)
- API primary (requested): `https://fapi.binance.com/fapi/v1/klines`
- API fallback: `https://www.binance.com/fapi/v1/klines`
- Venue: Binance USD-M Futures (fapi)
- Endpoint: GET /fapi/v1/klines
- Params used: symbol, interval=5m, startTime, endTime, limit=1500
- Pagination: advance startTime to last open time + 1 interval (5m = 300000 ms)

## Requested range
- startTime: 1609459200000 (2021-01-01 00:00:00 UTC)
- endTime: 1788220799000 (2026-08-31 23:59:59 UTC)
- Interval: 5m
- Instruments: BTCUSDT, ETHUSDT (USD-M perpetual)

## Timestamp definition
- open_time_ms: candle start (open time) from API, UTC epoch milliseconds
- close_time_ms: candle close time from API (typically open + 5m - 1ms)
- No timezone conversion beyond UTC interpretation of epoch ms

## Transforms
- dtype casts only: open_time_ms/close_time_ms/trades -> int64; OHLC/volumes -> float64
- No interpolation, no gap filling, no resampling
- Duplicate open_time_ms: if any, logged then first occurrence kept (see anomalies)

## Download window (wall clock UTC)
- download_start_utc: 2026-09-10T23:20:05Z
- download_end_utc: 2026-09-10T23:27:20Z

## Column schema (raw API order, renamed)
- [0] open_time_ms
- [1] open
- [2] high
- [3] low
- [4] close
- [5] volume
- [6] close_time_ms
- [7] quote_volume
- [8] trades
- [9] taker_buy_base
- [10] taker_buy_quote
- [11] ignore

## BTCUSDT

- file: `/workspace/lab/data/DATA-PROV-001/raw/BTCUSDT_5m_binance_um.parquet`
- size_bytes: 38029058
- sha256: `799f379f8a3d3228179b5a17987cbd31a2195b5fc545784a1f0d857b7593a713`
- rows: 595872
- pages_fetched: 398
- first_open_time: 1609459200000 (2021-01-01 00:00:00 UTC)
- last_open_time: 1788220500000 (2026-08-31 23:55:00 UTC)
- requested_first_open: 2021-01-01 00:00:00 UTC
- requested_last_open: 2026-08-31 23:55:00 UTC
- range_shortfall_start: False
- range_shortfall_end: False
- missing_bar_count (within first..last actual): 0
- gap_range_count: 0
- extra_offgrid_count: 0
- duplicates_logged: 0
- anomalies: none
- api_failures: none
- gap_ranges: none

## ETHUSDT

- file: `/workspace/lab/data/DATA-PROV-001/raw/ETHUSDT_5m_binance_um.parquet`
- size_bytes: 37643152
- sha256: `d7781563e7665adce5db69cda3ea7b650daee3acdbf3c0814b062248ed9e8cf2`
- rows: 595872
- pages_fetched: 398
- first_open_time: 1609459200000 (2021-01-01 00:00:00 UTC)
- last_open_time: 1788220500000 (2026-08-31 23:55:00 UTC)
- requested_first_open: 2021-01-01 00:00:00 UTC
- requested_last_open: 2026-08-31 23:55:00 UTC
- range_shortfall_start: False
- range_shortfall_end: False
- missing_bar_count (within first..last actual): 0
- gap_range_count: 0
- extra_offgrid_count: 0
- duplicates_logged: 0
- anomalies: none
- api_failures: none
- gap_ranges: none

## Hard rules compliance
- Raw files written once to raw/
- Gaps not filled; missing bars counted and listed
- SHA256 written to provenance/*_5m.sha256
- derived/ left empty (no research slices)

