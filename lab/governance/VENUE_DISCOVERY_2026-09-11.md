# VENUE DISCOVERY — Short-window BTC/ETH binary crypto markets
**Date (UTC):** 2026-09-11  
**Scope:** Read-only public inventory for prediction-market mission adapters (`POLYMARKET_*`, `KALSHI`)  
**Focus:** BTC/ETH Up-Down / Above-Below / short-duration (≈5/10/15m or hourly) binary event markets  
**Method:** WebSearch + WebFetch + public HTTP APIs (no accounts, no orders, no login scrape)  
**Evidence tags:** `[V]` observed/verified · `[I]` inference · `[H]` hypothesis · `[A]` assumption · `[U]` unknown / `UNTESTED`

---

## Executive summary (adapter prioritization)

| Venue surface | Short-window BTC/ETH binaries exist now? | Best fit for 5/10/15m mission | Priority note |
|---------------|------------------------------------------|-------------------------------|---------------|
| **Polymarket Global** (`polymarket.com`) | **YES** — live **5m** and **15m** Up/Down for BTC & ETH `[V]` | Strong for **5m + 15m** | No **10m** series verified `[U]`/`[V]` absence on crypto pages |
| **Polymarket US** (`polymarket.us`) | **NO evidence** of short crypto Up/Down `[V]` search + official docs | Not usable for this product family today | Docs: sports live; politics/finance/economics “coming soon” `[V]` |
| **Kalshi** | **YES** — live **15m** Up/Down for BTC & ETH `[V]` | Strong for **15m**; **no 5m/10m series** found (404) `[V]` | Hourly Above/Below series (`KXBTCD`/`KXETHD`) exist but **0 open markets** at check `[V]` |

**Honest gaps:** Exact Kalshi dollar fee schedule PDF blocked by site checkpoint (HTML returned) — series reports `fee_type=quadratic`, `fee_multiplier=1` `[V]`; closed-form cents table **UNTESTED** from official PDF. Polymarket US crypto short-window = **not offered** based on public docs + gateway search, not merely geo-hidden `[V]`.

---

## 1. Polymarket Global (international / crypto-native)

### 1.1 Public status `[V]`
- Product: blockchain prediction markets on Polygon; distinct from Polymarket US `[V]` (`docs.polymarket.us` “Polymarket vs Polymarket US”).
- Status page: `https://status.polymarket.com/` reported systems operational at discovery time `[V]` (WebSearch/status page).
- US persons: web/UI messaging that trading on `polymarket.com` is blocked in the United States and to use `polymarket.us` `[V]` (indexed market pages / third-party mirrors). **Legal eligibility for Logan: UNTESTED / counsel `[U]`.**

### 1.2 Short-window BTC/ETH binaries — **EXIST** `[V]`

| Duration | BTC | ETH | Live at check (2026-09-11 ~04:10 UTC)? |
|----------|-----|-----|----------------------------------------|
| **~5 minutes** | Yes | Yes | **Yes** — `acceptingOrders: true` `[V]` |
| **~15 minutes** | Yes | Yes | **Yes** — `acceptingOrders: true` `[V]` |
| **~10 minutes** | Not found as slug family | Not found | Treat as **absent** for inventory `[V]` (no `*-updown-10m-*` on crypto/5M/15M pages) |
| **Hourly Up/Down** | Not found as continuous hourly slug family | Not found | **UNTESTED** as product line; only adjacent **daily** “Up or Down on September 11?” seen (Binance noon candle; closed at check) `[V]` |

**Example live titles / slugs `[V]` (Gamma API `https://gamma-api.polymarket.com/events?slug=…`):**

| Title | Slug | Window end (event `endDate`) | Outcomes |
|-------|------|------------------------------|----------|
| Bitcoin Up or Down - September 11, 12:05AM-12:10AM ET | `btc-updown-5m-1789099500` | 2026-09-11T04:10:00Z | Up / Down |
| Ethereum Up or Down - September 11, 12:05AM-12:10AM ET | `eth-updown-5m-1789099500` | 2026-09-11T04:10:00Z | Up / Down |
| Bitcoin Up or Down - September 11, 12:00AM-12:15AM ET | `btc-updown-15m-1789099200` | 2026-09-11T04:15:00Z | Up / Down |
| Ethereum Up or Down - September 11, 12:00AM-12:15AM ET | `eth-updown-15m-1789099200` | 2026-09-11T04:15:00Z | Up / Down |
| Bitcoin Up or Down - September 11, 12:15AM-12:30AM ET | `btc-updown-15m-1789100100` | 2026-09-11T04:30:00Z | Up / Down |

Also listed on UI pages (pre-open / adjacent): later 5m windows e.g. `btc-updown-5m-1789185300` (“11:55PM-12:00AM ET”) with `acceptingOrders: true` `[V]`. SOL/XRP 5m/15m slugs appear on the same crypto pages `[V]` (out of BTC/ETH focus).

**Resolution rule (verbatim gist from market description) `[V]`:**
- Resolves **Up** if Chainlink **TWAP** at end of titled range **≥** TWAP at beginning; else **Down**.
- Flat (≥) resolves **Up** per rules text `[V]`.
- Source URLs in rules:
  - BTC: `https://data.chain.link/streams/btc-usd-twap-60s-streams`
  - ETH: `https://data.chain.link/streams/eth-usd-twap-60s-streams`
- Official docs also document Chainlink TWAP consumption via Polymarket RTDS: `https://docs.polymarket.com/market-data/chainlink-twap.md` (`wss://ws-live-data.polymarket.com`) `[V]`.
- Platform-wide resolution concept uses UMA Optimistic Oracle for many markets `[V]` (`docs.polymarket.com/concepts/resolution.md`); **these crypto short windows explicitly bind Chainlink TWAP streams in the market text** `[V]`. Do not assume UMA dispute path without testing `[U]`.

### 1.3 Public API / docs `[V]`
| Surface | URL |
|---------|-----|
| Docs hub | `https://docs.polymarket.com/` |
| Docs index | `https://docs.polymarket.com/llms.txt` |
| Gamma (discover markets) | `https://gamma-api.polymarket.com` |
| CLOB (books / orders) | `https://clob.polymarket.com` |
| Data API | `https://data-api.polymarket.com` |
| RTDS | `wss://ws-live-data.polymarket.com` |
| CLOB market WS | `wss://ws-subscriptions-clob.polymarket.com/ws/market` |
| Fees doc | `https://docs.polymarket.com/trading/fees` (and `/trading/fees.md`) |

### 1.4 Historical data notes `[V]` / `[U]`
- Closed short-window events remain queryable by slug via Gamma (many historical `btc-updown-5m-*` / `15m-*`) `[V]`.
- CLOB `GET /prices-history?market={token_id}&interval=1m&fidelity=10` returned a history array for a live 15m Up token `[V]` (smoke test only — completeness / retention **UNTESTED** `[U]`).
- Full trade/order reconstruction for adapter backtests: **UNTESTED** end-to-end `[U]`.
- Gamma `public-search` returns a thin recent slice (often ~5 hits); discovery of *current* windows is more reliable via crypto category pages or known slug patterns than search alone `[V]`.

### 1.5 Fees / trading cutoff `[V]` / `[U]`
- Live 5m/15m BTC/ETH markets: `feesEnabled: true`, `feeType: crypto_fees_v2`, schedule `{exponent:1, rate:0.07, takerOnly:true, rebateRate:0.2}` `[V]`.
- Official fees doc: taker fee `fee = C × feeRate × p × (1-p)`; Crypto category rate **0.07**; makers not charged; geopolitics fee-free; fees fund maker rebates `[V]` (`docs.polymarket.com` Fees).
- At $0.50 × 100 shares, Crypto table shows **$1.75** taker fee `[V]` (docs table).
- Trading cutoff: markets showed `acceptingOrders: true` while window open / until `endDate` `[V]`. Exact last-match vs resolution race, book clear-on-start behavior: **UNTESTED** beyond field presence (`clearBookOnStart` exists on some market objects historically) `[U]`.

### 1.6 Blockers `[V]`
- None for **public read** of Gamma/CLOB history smoke / HTML crypto pages from this box.
- US trading on Global surface reportedly blocked in UI — adapter for US-resident trading may be forced to Polymarket US (which lacks this product) `[V]`/`[I]`.

---

## 2. Polymarket US (CFTC-regulated)

### 2.1 Public status `[V]`
- Separate product: fiat / USD, KYC, DCM+DCO under CFTC; not interchangeable with Global liquidity or APIs `[V]` (`docs.polymarket.us`).
- Public market data: `https://gateway.polymarket.us`  
- Authenticated trading: `https://api.polymarket.us`  
- Docs: `https://docs.polymarket.us/` · `https://docs.polymarket.us/llms.txt`  
- WS: `wss://api.polymarket.us/v1/ws/private`, `wss://api.polymarket.us/v1/ws/markets` `[V]`.

### 2.2 Short-window BTC/ETH binaries — **NOT FOUND** `[V]`
- Official “What can you trade?” lists **sports leagues only**; “Politics, culture, finance, and economics coming soon” `[V]` (`docs.polymarket.us/getting-started/what-is-polymarket-us.md`).
- Gateway search `q=bitcoin up` / `q=crypto` returned **sports** events only (MLB etc.), no crypto Up/Down `[V]` (2026-09-11).
- **Do not claim** Polymarket US offers 5m/15m BTC binaries — evidence is absence on public catalog + docs, not a longer-horizon substitute `[V]`.

### 2.3 Fees / history / cutoff
- Fee schedule for US crypto N/A (product absent) `[V]`.
- Historical crypto short-window data on US API: **N/A** `[V]`.
- Account/API key creation: **not attempted** (read-only mission) `[V]`.

### 2.4 Blockers `[V]`
- Product gap (no short crypto binaries), not a fetch blocker.
- Trading/auth requires KYC + developer portal — out of scope here `[V]`.

---

## 3. Kalshi

### 3.1 Public status `[V]`
- CFTC-regulated event exchange; exchange active at check, including shard “Crypto & Commodities” (`exchange_index: 2`) `[V]` (`GET /exchange/status`).
- Public Trade API hosts (both documented):  
  - `https://api.elections.kalshi.com/trade-api/v2`  
  - `https://external-api.kalshi.com/trade-api/v2`  
- Docs: `https://docs.kalshi.com/` · `https://docs.kalshi.com/llms.txt`  
- Legacy `trading-api.kalshi.com` redirects to elections host `[V]`.

### 3.2 Short-window BTC/ETH binaries

| Series | Title | Frequency | Open at check? | Notes |
|--------|-------|-----------|----------------|-------|
| **`KXBTC15M`** | Bitcoin price up down | `fifteen_min` | **YES** `[V]` | Live market e.g. `KXBTC15M-26SEP110015-15` — title **“BTC price up in next 15 mins?”** |
| **`KXETH15M`** | ETH 15M price up down | `fifteen_min` | **YES** `[V]` | Live market e.g. `KXETH15M-26SEP110015-15` — **“ETH price up in next 15 mins?”** |
| `KXBTC5M` / `KXETH5M` | — | — | **404 not_found** `[V]` | **No 5m series** |
| `KXBTC10M` | — | — | **404** `[V]` | **No 10m series** |
| `KXBTCD` | Bitcoin price Above/below | `hourly` | Series exists; **0 markets** returned at check `[V]` | Above/Below hourly family — **not** currently inventorying open contracts |
| `KXETHD` | Ethereum price Above/below | (sibling) | **0 markets** at check `[V]` | Same |

**Example live Kalshi contract `[V]`:**
- Ticker: `KXBTC15M-26SEP110015-15`
- Title: `BTC price up in next 15 mins?`
- `open_time`: 2026-09-11T04:00:00Z · `close_time`: 2026-09-11T04:15:00Z · `expected_expiration_time`: 2026-09-11T04:20:00Z
- `rules_primary` (gist): Yes if average of last **60 seconds** of CF Benchmarks **BRTI** before window end **≥** average of last 60 seconds of BRTI before window start.
- ETH analog uses **ETHUSDRTI** `[V]`.

**Settlement / oracle `[V]`:**
- Series `settlement_sources`: CF Benchmarks (`https://www.cfbenchmarks.com/`).
- Product metadata: final value = average of 60 RTI prices in the last minute before expiration.
- Contract terms PDF: `https://assets.kalshi.com/contract_terms/CRYPTO.pdf` — Source Agency CF Benchmarks; Last Trading Date/Time = `<time>` on `<date>` (template) `[V]`.
- Docs also describe authenticated WS CF Benchmarks feeds (`docs.kalshi.com` websockets) `[V]` — **not subscribed** here `[U]`.

### 3.3 Public API / docs `[V]`
| Item | URL / note |
|------|------------|
| Market data quickstart | `https://docs.kalshi.com/getting_started/quick_start_market_data.md` |
| Historical data | `https://docs.kalshi.com/getting_started/historical_data.md` |
| Cutoff probe | `GET /historical/cutoff` → e.g. `market_settled_ts` ≈ 2026-07-12T00:00:00Z at check `[V]` (live tier ~3 months target per docs) |
| Series | `GET /series/{ticker}` · Markets `GET /markets?series_ticker=KXBTC15M&status=open` |
| Fee schedule page | `https://kalshi.com/fee-schedule` / PDF `https://kalshi.com/docs/kalshi-fee-schedule.pdf` — **fetch returned Vercel security HTML, not PDF** `[V]` blocker |
| Series fee fields | `fee_type: quadratic`, `fee_multiplier: 1` on KXBTC15M/KXETH15M `[V]`; `GET /series/fee_changes?series_ticker=KXBTC15M` → empty array `[V]` |

### 3.4 Historical data notes `[V]` / `[U]`
- Live vs historical partition documented; older settled markets/trades via `/historical/*` `[V]`.
- Events/series remain on original endpoints even when old `[V]` (docs).
- Candlestick pull for open series requires `market_tickers` (smoke error confirmed) — **full hist pipeline UNTESTED** `[U]`.
- Rate limits: intermittent `too_many_requests` on `external-api` during burst probes `[V]`; elections host succeeded with pacing.

### 3.5 Fees / trading cutoff `[V]` / `[U]`
- Series-level: **quadratic** fees, multiplier **1** `[V]`.
- Exact published cents schedule: **UNTESTED** (official PDF blocked) `[U]`. Secondary writeups cite ≈ `0.07 × C × P × (1−P)` style curves — treat as **`[H]`/`[I]` until PDF or in-API fee quote verified**.
- Trading cutoff for 15m crypto: market `close_time` aligns with end of 15m window; settlement uses final-minute RTI average; `expected_expiration_time` was **+5m** after close on the live BTC sample `[V]`. Prefer **`close_time` as last-trade boundary** per market object `[V]`; do not invent earlier cutoffs `[U]`.
- Exchange schedule: crypto shard trading_active true; standard_hours mostly 24h with a Thursday maintenance-style gap in schedule JSON `[V]` — interpret carefully before assuming continuous `[U]`.

### 3.6 Blockers `[V]`
- Fee schedule PDF: **Vercel Security Checkpoint** (no account bypass attempted).
- Burst rate limits on public API — use backoff / elections host.
- No login scrape required for open market inventory.

---

## 4. Side-by-side (mission-relevant)

| Dimension | Polymarket Global | Polymarket US | Kalshi |
|-----------|-------------------|---------------|--------|
| **5m BTC/ETH Up-Down** | **Live** `[V]` | **None found** `[V]` | **No series** `[V]` |
| **10m** | **None found** `[V]` | None `[V]` | **No series** `[V]` |
| **15m BTC/ETH Up-Down** | **Live** `[V]` | **None found** `[V]` | **Live** (`KXBTC15M` / `KXETH15M`) `[V]` |
| **Hourly** | Continuous hourly Up-Down **not verified** `[U]`; daily Binance-style exists separately `[V]` | None `[V]` | Above/Below series `KXBTCD`/`KXETHD` exist; **no open** at check `[V]` |
| **Settlement** | Chainlink BTC/ETH **USD TWAP 60s** streams `[V]` | N/A | CF Benchmarks RTI **60×1s average** at boundaries `[V]` |
| **Public market data** | Gamma + CLOB + RTDS `[V]` | gateway.polymarket.us `[V]` | Trade API v2 (no key for market list) `[V]` |
| **US-resident trade path** | Reportedly blocked on `.com` `[V]` | Regulated US path, but **wrong product set** today `[V]` | US-regulated; crypto 15m live `[V]` |
| **Fees (short crypto)** | Taker `crypto_fees_v2` rate 0.07 `[V]` | N/A | quadratic ×1 `[V]`; $ table **UNTESTED** `[U]` |

---

## 5. Adapter prioritization (factual, not capital advice)

1. **`POLYMARKET_GLOBAL` adapter** — highest inventory match for **5m and 15m** BTC/ETH binaries; public discoverability + Chainlink TWAP docs are strong `[V]`. Confirm geo/eligibility before any execution design `[U]`.
2. **`KALSHI` adapter** — strongest **US-regulated** match for **15m only**; settlement semantics (CF Benchmarks RTI) are explicit in series + live `rules_primary` `[V]`. Do not prioritize Kalshi for **5m/10m** until a series appears `[V]`.
3. **`POLYMARKET_US` adapter** — **deprioritize** for this short-crypto mission until finance/crypto listings appear; currently sports-centric `[V]`.

**10m horizon:** neither venue currently lists a native 10m BTC/ETH Up-Down series in public inventory `[V]`. Mission cells that require native 10m contracts are **venue-blocked** unless using a different contract construction (not inventoried here) `[I]`.

---

## 6. Source checklist (reproducible)

| Check | Result |
|-------|--------|
| Gamma live slugs 5m/15m BTC/ETH | `acceptingOrders: true` `[V]` |
| Polymarket fees doc Crypto 0.07 | `[V]` |
| Polymarket US docs + gateway search | no short crypto `[V]` |
| Kalshi `GET /series/KXBTC15M`, `KXETH15M` | fifteen_min + CF Benchmarks `[V]` |
| Kalshi open markets BTC/ETH 15m | live titles/rules `[V]` |
| Kalshi `KXBTC5M`/`10M` | HTTP 404 `[V]` |
| Kalshi fee PDF | blocked (checkpoint HTML) `[V]` |
| Accounts / orders | **not created / not placed** `[V]` |

---

## 7. Explicit UNTESTED / UNKNOWN

- End-to-end authenticated order placement, fill quality, or WebSocket book latency on any venue.
- Kalshi official fee cents table (PDF blocked).
- Whether Polymarket short crypto markets use UMA challenge periods in practice vs automatic Chainlink resolution.
- Continuous Polymarket **hourly** Up-Down product line (vs daily / 5m / 15m).
- Open interest / depth sufficiency for research sizing (liquidity numbers seen in API responses but not audited) `[U]`.
- Legal permissibility of Global Polymarket trading for a specific US person.

*End of discovery report. No fabricated contracts. Inventory claims limited to observed public evidence dated 2026-09-11.*

---

## US operator constraint (2026-09-11)

**Pointer (do not reinterpret inventory above):** operable hard constraint for execution / cockpit / capital is filed at  
`governance/US_LAWFUL_VENUE_CONSTRAINT_2026-09-11.md` (`RETROACTIVE: NO`; does not rewrite `gauntlet-v2.0-alpha`).

**Adapter priority for US operators (execution path):**  
**Kalshi** (primary; CFTC-regulated; live 15m BTC/ETH Up-Down) → **Polymarket US** (watchlist when short crypto binaries exist) → **Polymarket Global** (research / oracle study only; **not** an execution venue). Binance / fapi / Vision remain Layer-3 external predictors only — never the PM trading venue.

Inventory findings in §§1–7 above are unchanged; this section only states the US-lawful execution ordering.
