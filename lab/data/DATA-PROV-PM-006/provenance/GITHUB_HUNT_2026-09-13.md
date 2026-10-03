# DATA-PROV-PM-006 — GitHub / PMXT historical bid+ask hunt

**DATA_ID:** DATA-PROV-PM-006  
**Window:** 2026-09-04 → 2026-09-11 UTC (lab PM-003)  
**Stamp:** 2026-09-13T20:35Z (box probes)  
**Target:** Polymarket Global 15m BTC/ETH Up/Down **best_bid + best_ask** (mid not invented)  
**Trade / paid vendors:** FORBIDDEN — not used.

## Verdict: **PARTIAL**

| Source | Sep 4–11 bid+ask | Notes |
|--------|------------------|-------|
| **PMXT R2 v2** (`r2v2.pmxt.dev`) | **PARTIAL** | Documented key works. Only **3 hours** in the week return 200: `2026-09-09T15/16/17`. All other probed Sep 4–11 hours **404**. Continuous dump effectively **ends 2026-08-10T00** then sparse Sep-9 fragments. |
| **GitHub hosted bytes** | **BLOCKED / miss** | No Sep 4–11 books. Only real BTC/ETH bid/ask dump is `gensx-x1/polymarket-btc-eth-updown-data` (Aug 6–18). |
| **HF Joseph3222/polymarket-orderbook** | miss | Ends **2026-08-10** (prior hunt; not re-downloaded). |
| **rocklabs-io/polymarket-dataset** | not public bytes | README points at gated R2 + academic access request — not a free GitHub dump. |
| **clarkpalmer/pmxt-data-ingestion** | scraper only | Downloader/filter for PMXT archive — hosts no Sep parquet. |
| **jprq87/polymarket-pipeline** | pipeline only | GCS/BigQuery ETL code — no public Sep orderbook releases. |

**Lab usability for PM-003 Clock join:** effectively **not gettable**. The three public Sep hours have real `best_bid`/`best_ask`, but **BTC/ETH 15m Up/Down token IDs from Gamma are absent** in probed hours `T15` (local) and `T16` (remote DuckDB filter). Almost the entire week is 404.

---

## Probe rows (documented PMXT v2 key)

Key pattern: `https://r2v2.pmxt.dev/polymarket_orderbook_YYYY-MM-DDTHH.parquet`

| URL | HTTP | Content-Length |
|-----|-----:|---------------:|
| `…/polymarket_orderbook_2026-04-17T12.parquet` (control) | **200** | 395,555,308 |
| `…/polymarket_orderbook_2026-08-10T00.parquet` (last dense day) | **200** | 361,963,136 |
| `…/polymarket_orderbook_2026-08-11T00.parquet` | **404** | — |
| `…/polymarket_orderbook_2026-09-04T00.parquet` | **404** | — |
| `…/polymarket_orderbook_2026-09-04T12.parquet` | **404** | — |
| `…/polymarket_orderbook_2026-09-07T00.parquet` | **404** | — |
| `…/polymarket_orderbook_2026-09-09T15.parquet` | **200** | 24,037,341 |
| `…/polymarket_orderbook_2026-09-09T16.parquet` | **200** | 200,873,182 |
| `…/polymarket_orderbook_2026-09-09T17.parquet` | **200** | 111,250,864 |
| `…/polymarket_orderbook_2026-09-11T20.parquet` | **404** | — |
| `https://r2.pmxt.dev/polymarket_orderbook_2026-09-04T00.parquet` (v1) | **404** | — |

Sep-9 full-hour scan: only **T15, T16, T17** are 200; T00–T14 and T18–T23 are 404.  
Other Sep 4/5/6/7/8/10/11 hours sampled at T06/T15/T16/T17/T18/T20: **all 404**.

`archive.pmxt.dev/Polymarket/v2` listing (LD+JSON in HTML) advertises the same Sep-9T15/16/17 objects plus a long Aug-10-and-earlier run — consistent with R2 HEAD results. Docs: https://archive.pmxt.dev/docs/v2-data-overview

---

## Sample inspected (one small Sep hour)

- **Path:** `/workspace/lab/data/DATA-PROV-PM-006/scratch/polymarket_orderbook_2026-09-09T15.parquet`
- **Size:** 24,037,341 bytes (~24 MB); **2,930,050** rows; received ts **2026-09-09 15:31:27Z → 15:52:55Z** (partial hour, not full :00–:59).
- **Schema (v2):** `timestamp_received`, `timestamp`, `market`, `event_type`, `asset_id`, `bids`, `asks`, `price`, `size`, `side`, **`best_bid`**, **`best_ask`**, `fee_rate_bps`, `transaction_hash`, `old_tick_size`, `new_tick_size`.
- **Event mix:** `price_change` 2,916,675 (carries best_bid/best_ask); `book` 12,372 (bids/asks JSON); `last_trade_price` 1,003.
- **BTC/ETH 15m in this hour:** **NO.** Gamma `events?slug=btc|eth-updown-15m-*` for windows overlapping 14:00–17:00Z on Sep 9 return live condition/token IDs; **0** of those `clobTokenIds` appear in the parquet `asset_id` set (36,605 distinct). Same token list vs remote `…T16.parquet` DuckDB filter: **0 hits**.
- Prior PM-005 hist YES token also absent (expected — different window).

---

## GitHub (bytes vs scrapers)

| Repo | Hosts Sep 4–11 books? | Role |
|------|----------------------|------|
| **gensx-x1/polymarket-btc-eth-updown-data** | **No** | Real SQLite ticks with `up_bid`/`up_ask`/`down_bid`/`down_ask`; coverage **2026-08-06 10:43Z → 2026-08-18 12:14Z** only; last sealed Aug 18; no releases beyond `databases/*.db.zst`. **Misses PM-003 week.** |
| clarkpalmer/pmxt-data-ingestion | No | Scripts pointing at PMXT R2 — not a data host. |
| rocklabs-io/polymarket-dataset | No public Sep JSONL on GitHub | Documents gated R2; academic access request. |
| jprq87/polymarket-pipeline | No | Cloud ETL; no orderbook releases. |

GitHub code/repo search for other Sep 2026 orderbook dumps: no additional public parquet/jsonl hosts identified for this window (other hits = bots, live watchers, trade datasets).

---

## Still missing for a Clock join (Kalshi PM-003 mids already in hand)

1. **Dense hour coverage** for 2026-09-04…11 — only three fragmented Sep-9 hours exist on public PMXT; rest 404.  
2. **BTC/ETH 15m (and 5m) rows** inside those hours — schema is right, subscription/content is not (tokens missing).  
3. **T−5m / rem=300** aligned snapshots across the full pairing window — cannot be built from 3 partial hours without inventing quotes.  
4. Forward path remains live CLOB `/book` capture under PM-006; do not treat `/prices-history` last-trade as mid; do not Examiner-score from this note.

**Bottom line:** Correcting the URL key proves PMXT v2 is real and public — but **for the PM-003 week it is not a usable historical bid+ask source** (sparse 404s + no BTC/ETH 15m in the few GETTABLE hours). GitHub does not fill the gap.
