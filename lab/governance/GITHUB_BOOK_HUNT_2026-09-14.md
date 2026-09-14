# GitHub / HF book-tape hunt — FREE Polymarket / Kalshi BTC·ETH 5m·15m L2 / bid-ask dumps

**Stamp:** 2026-09-14 (box probes; `gh` unauthenticated — used raw GitHub, jsDelivr, Hugging Face API, and direct parquet pulls)  
**Goal:** Clock-joinable book tape for follow-vs-fade vs Kalshi mid (see `JOIN_SPEC_FOLLOW_VS_FADE_2026-09-14.md`).  
**Window of interest:** research week **2026-09-04 → 2026-09-11** (and live-forward if that is all that exists).  
**Trade:** FORBIDDEN. Not Examiner. Do not invent coverage. DepthFeed / paid full archives: **do not buy**.

## Already known (carried forward; re-checked where noted)

| Item | State |
|------|--------|
| `gensx-x1/polymarket-btc-eth-updown-data` | Real TOB bid/ask dump; **2026-08-06 → 2026-08-18** only — not Sep week |
| DATA-PROV-PM-006 historical hunt | **BLOCKED** for Sep 4–11 on official CLOB + prior free mirrors (`data/DATA-PROV-PM-006/provenance/HISTORICAL_HUNT_BLOCKED.md`, `GITHUB_HUNT_2026-09-13.md`) |
| DepthFeed | **PAID** full-depth archive (Jan 2026+); client repos only — **do not buy** |
| PMXT `r2v2.pmxt.dev` | Prior hunt: dense ends ~2026-08-10; Sep week almost all 404; only Sep-9 T15/T16/T17 GETTABLE and **no** BTC/ETH 15m tokens in those hours |

## Verdict (this hunt)

**No free public dump found that covers Polymarket or Kalshi BTC/ETH 5m or 15m order-book / L2 / bid-ask for 2026-09-04 → 2026-09-11.**

Free survivors exist for **other** windows (Aug and earlier) or are **wrong product** / **scraper-only** / **empty** / **paid teaser**. Forward path remains live capture (PM-006 / PM-008).

---

## Survivors with hosted FREE bytes (product-relevant)

### 1. `gensx-x1/polymarket-btc-eth-updown-data` (GitHub)

| | |
|--|--|
| **Repo** | https://github.com/gensx-x1/polymarket-btc-eth-updown-data |
| **Date range** | **2026-08-06 10:43:07Z → 2026-08-18 12:14:59Z** (README + five sealed `databases/*.db.zst`; last sealed 2026-08-18) |
| **Fields** | **Top-of-book** only: `up_bid`/`up_ask`/`up_bid_sz`/`up_ask_sz`, same for `down_*`, plus `up_mid`/`down_mid`, `ts_ms`, `slug` (`btc-updown-15m-…` / `5m`), window helpers. **Not** full L2. |
| **Sep 2026?** | **No** — Aug only; no Sep files in `databases/`. Live-forward: collector claimed to roll at 200 MB, but **no post-Aug-18 sealed file** observed on GitHub. |
| **License** | No `LICENSE` file; README: as-is, research/educational. Free download (donations solicited). |
| **Usability** | Real clockable Poly TOB for Aug — **wrong week** for PM-003 / Sep research join. |

### 2. `polyorderbooks/polymarket-crypto-updown-orderbooks-l2` (HF + Zenodo)

| | |
|--|--|
| **Repo / dataset** | https://huggingface.co/datasets/polyorderbooks/polymarket-crypto-updown-orderbooks-l2 · DOI https://doi.org/10.5281/zenodo.22084114 |
| **Date range** | **2026-08-21 → 2026-08-24 UTC** (verified on `updown_15m.parquet`: `captured_at` min/max; Zenodo text agrees). |
| **Fields** | **Full L2** ladders (`bid_prices`/`bid_sizes`/`ask_prices`/`ask_sizes`) + `best_bid`/`best_ask`, `market_slug` (`btc-updown-15m-…`, `eth-…`, 5m/15m/4h), `captured_at`, `seconds_to_close`, winner. 1-second style capture with reconcile. |
| **Sep 2026?** | **No.** |
| **License** | **CC BY 4.0** |
| **Note** | Wider continuous coverage is marketed via paid/API (`polyorderbooks.com`) — free research release is this Aug 21–24 slice only. |

### 3. `polyorderbooks/polymarket-crypto-5min-orderbooks` (HF)

| | |
|--|--|
| **Dataset** | https://huggingface.co/datasets/polyorderbooks/polymarket-crypto-5min-orderbooks |
| **Date range** | **2026-08-20 10:45:00Z – 10:59:59Z** only (15 complete 5m markets). |
| **Fields** | Full L2 `bids`/`asks` + `best_bid`/`best_ask`; BTC/ETH among seven assets. |
| **Sep 2026?** | **No.** |
| **License** | **CC BY 4.0** |

### 4. `gregyoung14/openmarket` + HF `gregyoung14/openmarket-btc-polymarket`

| | |
|--|--|
| **Repo / dataset** | https://github.com/gregyoung14/openmarket · https://huggingface.co/datasets/gregyoung14/openmarket-btc-polymarket |
| **Date range** | Observed event span **2026-02-12 → 2026-05-15** (54 Polymarket days); snapshot publication through **2026-07-01**; **archival shutdown** at tag `v0.5.2` — no new collection. |
| **Fields** | `polymarket_ticks_ms`: **top-of-book** `best_bid` / `best_ask` (ms); paired Binance. Sample `market_meta` shows `btc-updown-15m-*` slugs. **BTC-focused**; not a Kalshi tape. |
| **Sep 2026?** | **No** (frozen; ends May / Jul archive). |
| **License** | **Apache-2.0** (code) · dataset card **apache-2.0** |

### 5. `Joseph3222/polymarket-orderbook` (HF; pmxt mirror)

| | |
|--|--|
| **Dataset** | https://huggingface.co/datasets/Joseph3222/polymarket-orderbook |
| **Date range** | **2026-02-22 → 2026-08-10** (tree last partition `date=2026-08-10`; Aug-10 partial). Gap 2026-06-12→06-17. |
| **Fields** | Raw CLOB events (`book` / `price_change` / …) → reconstructable **full L2**; plus `orderbook_1min` full-depth rollup. All markets (filter to updown by `asset_id` / Gamma). |
| **Sep 2026?** | **No** — **0** `2026-09-*` partitions (reconfirmed this hunt). |
| **License** | **CC BY 4.0** (credits pmxt). |

### 6. `kartikbathla/polymarket-crypto-up-down-5min-15min-market-orderbook-l2-data` (HF sample)

| | |
|--|--|
| **Dataset** | https://huggingface.co/datasets/kartikbathla/polymarket-crypto-up-down-5min-15min-market-orderbook-l2-data |
| **Date range** | Sample day **2026-07-17** only (btc/eth/… 5m+15m). |
| **Fields** | Episodes NDJSON + **top-10** parquet L2 + trades. |
| **Sep 2026?** | **No.** Month-scale = commercial contact. |
| **License** | `other` (sample; commercial for more). |

---

## Near-misses / non-survivors (checked)

| Source | Why not a Sep BTC/ETH 5m·15m free book tape |
|--------|---------------------------------------------|
| **`DineshKumar8399/polymarket-orderbook-dataset`** (HF + GH release `data-2026-09-13`) | Free **CC BY 4.0**; partitions **`dt=2026-09-04` … `09-13` exist** and Sep-04 parquet pulled OK (`bid`/`ask`/`mid` TOB ~2-min sweep). **But** `markets.parquet`: **0** slugs matching `updown` / `btc-updown` / `eth-updown`. Crypto category = **57** long-dated `cpc-btc-*` price markets only. **Wrong product** for this join. |
| **`krish301/polymarket-raw-15m`** (HF) | Card claims L2 JSONL from 2026-06-04; **dataset empty** (~8.7 kB, “currently empty”). Unusable. MIT claimed. |
| **`rocklabs-io/polymarket-dataset`** | Documents Jan/Feb 2026–present full CLOB JSONL on **gated R2**; “free for students/academic” **by request** — **no public GitHub bytes**. Custom research license (no redistribution). |
| **`mdowis/Kalshi_orderbook_streamer`** | Scripts + Actions for KXBTC15M/KXETH15M snapshot+delta JSONL. **No `data/` in repo** (jsDelivr tree = scripts only). README: when R2 set, **skips git commits** — historical tape is **private bucket**, not a public dump. |
| **`lerchen3/kalshi-orderbook-alpha`** (HF) | Live Kalshi book alpha feed; tree shows **2026-07-19** files only in this probe; top-200 volume universe — **not** a documented KXBTC15M Sep archive. |
| **`bennett-tan/kalshi-btc-15m`** (HF) | Large free set — **trade prints** (`yes_price`/`no_price`/`trade_id`), **not** order-book snapshots. Features sibling has `ofi` derived fields — still not L2 tape. |
| **`sneddy/polymarket_research`**, **`Caiooooo/polymarket-l2-collector`**, **`holypolyfoundation/KDE`**, **`Conn-Ho/polymarket-btc-tracker`**, **`suitedaces/polyterminal`** | Collectors / live tools; **no** published historical Sep BTC/ETH book dumps. |
| **`LuciferForge` / `manja316` polymarket-historical-data** | GitHub points to **paid** Gumroad / API; author warns orderbook table is mostly thin placeholders. Free HF samples ≠ dense BTC/ETH 15m L2 for Sep. |
| **`vcorp-dev/kalshi-price-data`**, **`V-Corp/polymarket-orderbook-depth-sample`** | DepthFeed client + **free sample** (BTC L2, generated 2026-08-07). Full archive = **paid DepthFeed** — **FORBIDDEN to buy** for this hunt. |
| **`astrnvk/polymarket-orderbook-data-preview`** | Free preview Jun 26–29 TOB + Jun-21 30m L2 sample; full = **paid** storefront. CC BY-NC 4.0 on preview. |
| **`Coyevans/polymarket-kalshi-scoresync-orderbook-sample`** | Sports score-sync teaser; not crypto 5m/15m. |
| **OFI × polymarket GitHub query** | Hits are live bots / research code / trade-derived features — **no** additional free Sep book dump identified. |

---

## Queries executed (representative)

GitHub/web/HF: `polymarket orderbook snapshot btc 15m`, `kalshi orderbook historical btc 15m github`, `polymarket clob book jsonl`, `"btc-updown-15m" orderbook`, `OFI polymarket github`, HF `polymarket orderbook` / `kalshi orderbook` / `kalshi btc 15m`.  
Direct pulls: gensx README + DB filenames; Dinesh `markets.parquet` + `quotes/dt=2026-09-04`; polyorderbooks `updown_15m.parquet`; OpenMarket `market_meta.parquet`; Joseph tree last day; Kalshi streamer jsDelivr tree.

`gh search` unavailable (not logged in / no `GH_TOKEN`).

---

## Bottom line for follow-vs-fade

| Need | Free hist for Sep 4–11? |
|------|-------------------------|
| Polymarket BTC/ETH **15m/5m** bid-ask or L2 | **No** survivor |
| Kalshi BTC/ETH **15m** book / mid hist | **No** public dump (streamer = forward DIY; DepthFeed = paid) |
| Closest free Poly book tapes | gensx **Aug 6–18 TOB**; polyorderbooks **Aug 21–24 L2**; Joseph/pmxt **→ Aug 10 L2**; OpenMarket **→ May 15 TOB BTC** |

**Do not** backfill Sep week from Aug dumps. **Do not** treat Dinesh Sep partitions as updown coverage. **Do not** Examiner-score from this memo. Keep **PM-006** (Poly live book) and **PM-008** (Kalshi live mid) as the physical path for a same-t join.
