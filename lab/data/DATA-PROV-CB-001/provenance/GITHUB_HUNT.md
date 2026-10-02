# DATA-PROV-CB-001 — GitHub hunt (as-needed first hunt for missing tapes)

**Stamp:** 2026-09-13  
**Need:** Coinbase BTC-USD / ETH-USD **1-minute** historical candles covering `2026-09-04T20:00Z` → `2026-09-11T20:59Z`.  
**Rule:** Distinguish **hosted bytes** (downloadable dump covering the window) vs **scrapers** (code that calls the live API). A GitHub hit does **not** Clock-clear. Official Exchange API fetch still required when working.

## Probes executed

| Probe | Tool | Result |
|-------|------|--------|
| `GET /search/repositories?q=coinbase+candles+BTC-USD+1m` | GitHub REST (unauth) | HTTP 200, `total_count=0` |
| `GET /search/repositories?q=coinbase+historical+candles+granularity` | GitHub REST | HTTP 200, `total_count=0` |
| Broader repo qs (`coinbase 1m BTC ETH candles`, `ohlcv 1-minute`, `BTC-USD historical csv`, `gdax candles historical`, `exchange candles dataset`, `minute bars BTC-USD`) | GitHub REST | HTTP 200, all `total_count=0` |
| `topic:coinbase candles` | GitHub REST | HTTP 200, **6 repos** — all scrapers/libs (see below) |
| `GET /search/code?q=BTC-USD+candles+granularity+60…` | GitHub REST | HTTP **401** Requires authentication |
| `GET /search/code?q=api.exchange.coinbase.com+products+candles…` | GitHub REST | HTTP **401** Requires authentication |
| `github.com/search?q=…&type=repositories` HTML | curl | HTTP **429** rate limited |
| Web search `site:github.com Coinbase BTC-USD 1-minute OHLCV … 2026` | external index | scrapers/SDKs only; no Sept-2026 dump |
| Hugging Face `tensorlink-dev/coinbase-1m-btc-eth-sol-paxg` (adjacent, not GitHub) | web | **hosted parquet**, coverage **2024-12-01 → 2025-12-01** — **does not cover 2026-09** |

`gh` CLI present but **not logged in**; code search therefore unavailable without user auth. Repo search + topic search + web index used instead.

## Hits (classified)

### Hosted bytes covering our window

**None found** on GitHub (or adjacent HF dump) for `2026-09-04`–`2026-09-11`.

| Candidate | Class | Coverage vs window | Notes |
|-----------|-------|--------------------|-------|
| *(none on GitHub)* | — | — | — |
| HF `tensorlink-dev/coinbase-1m-btc-eth-sol-paxg` (and Mindbyte-89 mirror) | hosted parquet (non-GitHub) | ends ~2025-12-01 — **MISS** our 2026-09 window | Not used; not Clock-clearing |

### Scrapers / libraries (not dumps)

| Repo | Class | Notes |
|------|-------|-------|
| `silktown-software/coinbase-historic-candlestick-scraper` | scraper | Coinbase Pro public API collector |
| `8W9aG/cbhist` | scraper/lib | pages Exchange candles (300/req); no shipped tape |
| `marianogappa/crypto-candles` | library/CLI | multi-venue iterator |
| `EtWnn/CryptoPrice` | library | multi-source history |
| `Ohkthx/coeus` | collector | candle collection + TA |
| `NullCharacter0/CoinBase-API-CandleStick-OHLC` | tutorial/scraper | Advanced Trade v3 candles → pandas |
| `anssip/spot-server` | live streamer | realtime Coinbase candles |
| `coinbase/coinbase-advanced-py` | official SDK | `get_candles` client — not a dump |
| `ta4j/ta4j` example `CoinbaseHttpBarSeriesDataSource` | scraper example | paginates Advanced Trade |
| `Efixdata/exeria-charts` adapter-coinbase | adapter | REST + WS; no archive bytes |

## Verdict for hunt

- **Hosted dump for window:** NOT FOUND  
- **Scrapers abundant:** YES (would re-hit the same public API we already call)  
- **Implication:** Do not treat GitHub as a substitute tape for this window. Proceed with official `api.exchange.coinbase.com` paged fetch (completed successfully — see `FETCH_SUMMARY.json` / `INVENTORY.md`).

**Clock:** not cleared by this hunt (no usable hosted bytes for the window).
