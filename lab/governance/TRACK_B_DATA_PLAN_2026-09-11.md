# TRACK B DATA PLAN — Historical resolved short-window BTC/ETH binaries
**Document:** `TRACK_B_DATA_PLAN_2026-09-11.md`  
**Date (UTC):** 2026-09-11  
**Track:** B — historical contract capture (L1 PM + L2 oracle mapping)  
**Scope:** Kalshi `KXBTC15M` / `KXETH15M` (15m); Polymarket Global 5m + 15m BTC/ETH Up/Down  
**Authority context:** `PREDICTION_MARKET_MISSION_2026-09-11.md` · `VENUE_DISCOVERY_2026-09-11.md` · `US_LAWFUL_VENUE_CONSTRAINT_2026-09-11.md` (Kalshi + Polymarket Global **co-primary** for lab planning `[A]` Governor)  
**Evidence tags:** `[V]` observed · `[I]` inference · `[H]` hypothesis · `[A]` assumption · `[U]` unknown  
**Non-goals:** trading · UI · inventing API keys · browser login workarounds for private APIs

---

## 0. Executive result (this deliverable)

| Item | Result |
|------|--------|
| Free public historical path? | **YES** for both co-primary venues `[V]` |
| Auth / API key required for metadata + resolution labels? | **NO** `[V]` |
| Provisional sample | **Fetched** → `/workspace/lab/data/DATA-PROV-PM-001/` (~38 MB; 3824 contracts) |
| Dataset stub | `/workspace/lab/archive/datasets/DATA-PROV-PM-001.md` · **STATUS PENDING_CLOCK** |
| Blockers for Governor | Soft only (rate limits, retention partitions, fee PDF, L2 oracle raw feeds, book history completeness) — **no hard auth blocker** for resolved-contract reconstruction |

---

## 1. Kalshi — 15m BTC/ETH (`KXBTC15M` / `KXETH15M`)

### 1.1 Endpoints `[V]`

| Purpose | Method / URL | Auth |
|---------|--------------|------|
| Series metadata | `GET https://api.elections.kalshi.com/trade-api/v2/series/{ticker}` | **None** (public market data) |
| Live / recent markets | `GET …/markets?series_ticker=KXBTC15M&status=settled&limit=100&cursor=` | **None** |
| Historical cutoff | `GET …/historical/cutoff` | **None** |
| Settled older than cutoff | `GET …/historical/markets?series_ticker=KXBTC15M&limit=&cursor=` | **None** |
| Single market | `GET …/markets/{ticker}` or `…/historical/markets/{ticker}` | **None** |
| Candlesticks (live tier) | `GET …/markets/{ticker}/candlesticks` | **None** (params UNTESTED fully) |
| Candlesticks (hist tier) | `GET …/historical/markets/{ticker}/candlesticks` | **None** |
| Public trades | `GET …/markets/trades` (+ hist `/historical/trades`) | **None** for public trade tape |
| Orderbook (live) | `GET …/markets/{ticker}/orderbook` | **None** (live book only; not historical books) |
| Portfolio / orders / fills | `/portfolio/*` | **API key + RSA-PSS** — **out of scope**; not needed for resolved-contract ground truth |

**Alternate public host:** `https://external-api.kalshi.com/trade-api/v2` (docs). Elections host used for this sample (lower 429 rate in practice) `[V]`.

**Docs:** `https://docs.kalshi.com/getting_started/historical_data.md` · `quick_start_market_data.md` · `llms.txt`.

### 1.2 Auth needs

- **Resolved contract metadata + `result`:** no secrets `[V]`.
- **Trading / private fills / authenticated WS CF feeds:** keys required — **STOP** for those paths; do not invent keys `[A]` Track B rule.

### 1.3 Historical availability `[V]`

| Tier | Boundary (observed 2026-09-11) | Access |
|------|--------------------------------|--------|
| Live / recent settled | Markets with `settlement_ts` **≥** `market_settled_ts` | `GET /markets?status=settled` |
| Historical archive | **Before** cutoff | `GET /historical/markets` |
| Cutoff observed | `market_settled_ts` ≈ **2026-07-13T00:00:00Z** (also trades/orders/positions cutoffs same day) `[V]` | Refresh via `/historical/cutoff` before backfills |
| Live-window target | ~3 months per docs `[V]` docs | Cutoff advances |

**Series existence:** `KXBTC15M` / `KXETH15M` = `fifteen_min`. `KXBTC5M` / `10M` = **404** (no 5m/10m) `[V]` Venue Discovery.

**Provisional sample coverage:** ~7d settled (`2026-09-04` → `2026-09-11`): **664 BTC + 664 ETH** finalized with `result` ∈ {yes,no} `[V]`.

**Pre-cutoff smoke:** `/historical/markets?series_ticker=KXBTC15M&limit=5` returned July-12-settled tickers (e.g. `KXBTC15M-26JUL121945-45`) `[V]` — checkpoint reconstruction **feasible** across the partition.

### 1.4 Oracle mapping (L2) `[V]` / `[U]`

| Field | Value |
|-------|-------|
| Provider | **CF Benchmarks** (`settlement_sources`) |
| Index | BTC: **BRTI**; ETH: **ETHUSDRTI** |
| Method | Simple average of **60×1s** RTI prints in the last minute **before window start** vs **before window end**; Yes if end ≥ start (`rules_primary` on live/settled markets) |
| API fields useful for labels | `result`, `floor_strike` (start ref), `expiration_value` (end ref), `settlement_ts`, `rules_primary` |
| Raw RTI history for independent recompute | **UNTESTED** free public path `[U]`; Kalshi docs mention **authenticated** WS CF feeds — treat independent oracle replay as **optional L2** / possible BLOCKER if required |
| Contract terms PDF | `https://assets.kalshi.com/contract_terms/CRYPTO.pdf` `[V]` discovery |

### 1.5 Checkpoint reconstruction feasibility

| Artifact | Feasibility | Notes |
|----------|-------------|-------|
| BINARY_CONTRACT registration (rules, times, resolution) | **HIGH** `[V]` | Public settled markets include `result` + timestamps |
| Decision-time \(m_t\) from last/mid | **PARTIAL** `[I]` | `last_price_dollars` on settled object is terminal; full path needs trades/candles |
| Trade prints | **FEASIBLE** public `/markets/trades` + `/historical/trades` with pacing `[V]` docs; bulk UNTESTED `[U]` |
| Full L2 book history | **LOW / blocked** `[I]` | Public API exposes **live** orderbook, not historical books |
| Candlestick path | **FEASIBLE** with live vs hist routing by cutoff `[V]` docs; fidelity UNTESTED `[U]` |

---

## 2. Polymarket Global — 5m + 15m BTC/ETH Up/Down

### 2.1 Endpoints `[V]`

| Purpose | Method / URL | Auth |
|---------|--------------|------|
| Event by slug | `GET https://gamma-api.polymarket.com/events?slug={slug}` or `/events/slug/{slug}` | **None** |
| Closed discovery | `GET …/events?title_search=Bitcoin%20Up%20or%20Down&closed=true&limit=&offset=&order=endDate&ascending=false` | **None** |
| Keyset pagination | `GET …/events/keyset?closed=true&limit=&after_cursor=` | **None** |
| Markets list | `GET …/markets` / `/markets/keyset` | **None** |
| CLOB price history | `GET https://clob.polymarket.com/prices-history?market={token_id}&interval=1m&fidelity=10` | **None** (smoke 200 `[V]`) |
| CLOB book / mid | CLOB REST public market endpoints | **None** for public book; trading needs wallet auth |
| Data API | `https://data-api.polymarket.com` (trades/activity) | Public claimed; **429 / CF 1015** observed on burst `[V]` — pace or treat as soft blocker |
| RTDS Chainlink TWAP | `wss://ws-live-data.polymarket.com` | Public stream for **live** TWAP; historical TWAP archive **UNTESTED** `[U]` |
| Resolution docs | `https://docs.polymarket.com/concepts/resolution.md` · `market-data/chainlink-twap.md` | — |

**Slug pattern `[V]`:** `{btc|eth}-updown-{5m|15m}-{unix_utc_window_start}`  
Example: `btc-updown-5m-1789099500` = start `2026-09-11T04:05:00Z` (5m window).

### 2.2 Auth needs

- **Closed event metadata + outcomePrices / umaResolutionStatus:** no secrets `[V]`.
- **Order placement / private positions:** wallet / session — **out of scope**; STOP if required.
- **Do not** use browser login workarounds for paid/private surfaces.

### 2.3 Historical availability `[V]` / `[U]`

| Path | Result |
|------|--------|
| Gamma by known slug | Closed short-window events remain queryable; `closed=true`, `outcomePrices` e.g. `["1","0"]`, `umaResolutionStatus=resolved` `[V]` |
| `title_search` + `closed=true` | Works for “Bitcoin/Ethereum Up or Down”; paginate `offset` `[V]` |
| Blind `closed=true` without filter | Returns unrelated long-horizon events — **not** useful alone `[V]` |
| Retention depth | Closed 5m/15m slugs exist historically; **full multi-month completeness UNTESTED** `[U]` |
| CLOB `prices-history` | Returns history array without auth `[V]` smoke; retention/completeness for expired tokens **UNTESTED** `[U]` |

**Provisional sample:** **2496** resolved Global events (~3d dense 5m-heavy under row cap): BTC 1250 / ETH 1246; windows 5m=1873 / 15m=623; all with RESOLUTION YES/NO `[V]`.

### 2.4 Oracle mapping (L2) `[V]` / `[U]`

| Field | Value |
|-------|-------|
| Provider | **Chainlink** BTC/ETH **USD TWAP 60s** streams |
| URLs in rules | `https://data.chain.link/streams/btc-usd-twap-60s-streams` · `eth-usd-twap-60s-streams` |
| Method | Up if TWAP at **end** of titled range **≥** TWAP at **beginning**; flat → Up |
| Platform resolution | Many markets use UMA Optimistic Oracle generally; short crypto rules **explicitly bind Chainlink TWAP** `[V]`; dispute path practice **UNTESTED** `[U]` |
| Live TWAP | Polymarket RTDS `[V]` docs |
| Historical TWAP for independent recompute | **UNTESTED** free archive `[U]` — label reconstruction from Gamma `outcomePrices` does **not** require it |

### 2.5 Checkpoint reconstruction feasibility

| Artifact | Feasibility | Notes |
|----------|-------------|-------|
| BINARY_CONTRACT + resolution label | **HIGH** `[V]` | Map Up→YES, Down→NO |
| Deterministic slug enumeration | **HIGH** `[V]` | Generate unix starts every 300s / 900s |
| \(m_t\) path | **PARTIAL→HIGH** `[I]` | CLOB prices-history + public trades if Data API stable |
| Full historical books | **UNTESTED / likely limited** `[U]` | Live CLOB books ≠ archive |
| Oracle independent audit | **UNTESTED** `[U]` | Needs Chainlink TWAP history |

---

## 3. Schema alignment (BINARY_CONTRACT)

Template: `archive/templates/BINARY_CONTRACT.md`.

| Template field | Kalshi source | Polymarket Global source |
|----------------|---------------|--------------------------|
| `VENUE_ADAPTER` | `KALSHI` | `POLYMARKET_GLOBAL` |
| `VENUE_NATIVE_ID` | `ticker` | event `slug` |
| `TITLE` / `QUESTION` | `title` | `title` / market `question` |
| `OUTCOMES` | YES/NO (venue yes/no) | YES/NO ← Up/Down |
| `STATUS` | `finalized` → RESOLVED | closed + resolved prices → RESOLVED |
| `RESOLUTION` | `result` yes/no | winning outcome from `outcomePrices` |
| `RESOLUTION_SOURCE` | CF Benchmarks RTI | Chainlink TWAP 60s URL |
| `OPEN_TIME` / `CLOSE_TIME` | `open_time` / `close_time` | `eventStartTime` / `endDate` |
| `RESOLVE_TIME` | `settlement_ts` | `closedTime` |
| `TICK_SIZE` | cents grid `[A]` verify | `orderPriceMinTickSize` |
| `FEE_SCHEDULE_REF` | series `fee_type=quadratic`, multiplier 1; PDF **UNTESTED** | `feeType=crypto_fees_v2` rate 0.07 `[V]` discovery |
| `PROVENANCE` | DATA-PROV-PM-001 | DATA-PROV-PM-001 |

Provisional IDs use `PROV-KALSHI-*` / `PROV-POLYGLOBAL-*` pending Archivist assign.

---

## 4. Provisional fetch executed (no secrets)

| Item | Value |
|------|-------|
| Path | `/workspace/lab/data/DATA-PROV-PM-001/` |
| Layout | `raw/` · `normalized/` · `provenance/` · `MANIFEST.json` · `CHECKSUMS.sha256` |
| Normalized | `kalshi_15m_btc_eth_resolved.ndjson` (1328) · `polymarket_global_5m_15m_btc_eth_resolved.ndjson` (2496) · `binary_contracts_provisional.ndjson` (3824) |
| Combined SHA256 | `431f7bd1f3d5d7b96b1419c2cdd3f200c05a91086f0983a738897c7243e1f027` |
| Bytes | ~38 MB total (raw ~23 MB + normalized ~16 MB) — **not** multi-GB |
| Auth used | **None** |
| Trades placed | **None** |

---

## 5. Blockers for Human Governor `[V]` / `[U]`

### 5.1 Hard blockers for *this* Track B goal (resolved-contract sample)
**None.** Free public paths sufficient for L1 contract + resolution labels on both co-primary venues `[V]`.

### 5.2 Soft / partial blockers (escalate if mission requires)

| ID | Blocker | Impact | Suggested Governor action |
|----|---------|--------|---------------------------|
| B1 | Kalshi / Polymarket **rate limits** (429; Data API CF 1015) `[V]` | Slows bulk backfill | Pace, elections host, backoff; optional higher-tier key **only if** Governor provisions secrets vault |
| B2 | Kalshi **live vs historical partition** (cutoff ~2026-07-13) `[V]` | Must dual-route queries | Implement cutoff-aware client (documented) |
| B3 | Kalshi **fee schedule PDF** Vercel checkpoint `[V]` discovery | Exact cents table UNTESTED | Accept quadratic×1 from API or fetch PDF via approved channel |
| B4 | **No Kalshi 5m/10m** series `[V]` | Cannot native-capture 5m on Kalshi | Use Polymarket Global for 5m; Kalshi 15m only |
| B5 | Polymarket **historical TWAP archive** UNTESTED `[U]` | Blocks independent L2 recompute | Accept venue resolution labels **or** commission Chainlink history source |
| B6 | **Historical order books** generally unavailable `[I]`/`[U]` | Limits microstructure backtests | Restrict early strategies to trades/candles/last; forward-capture books if needed |
| B7 | CLOB / Data API **retention completeness** UNTESTED `[U]` | \(m_t\) path risk on deep history | Spot-check ages; forward-capture mid/last |
| B8 | US eligibility of Global trading `[U]` counsel | Execution path ≠ research capture | Constraint file already separates planning assumption vs counsel; capture allowed under co-primary `[A]` |

### 5.3 Explicit non-blockers
- No API key required for Gamma closed events or Kalshi settled/historical markets `[V]`.
- Polymarket US product gap is **N/A** for this short-crypto family (watchlist only) `[V]`.

---

## 6. Recommended next steps (not executed here)

1. Clock review of `DATA-PROV-PM-001` (knowability, resolution revision policy, Up↔YES map).  
2. Archivist assign real `CONTRACT_ID`s for a pilot basket.  
3. Optional: extend Poly sample to full 7–30d via slug enumeration (deterministic) with pacing.  
4. Optional: attach CLOB `prices-history` samples for \(m_t\) harness — still public.  
5. Do **not** trade; do **not** build UI.

---

## 7. Source checklist (reproducible)

| Check | Result | Tag |
|-------|--------|-----|
| Kalshi `/historical/cutoff` | 200; ~2026-07-13 | `[V]` |
| Kalshi settled `KXETH15M`/`KXBTC15M` | 200; `result` present | `[V]` |
| Kalshi `/historical/markets` smoke | 200; Jul-12 tickers | `[V]` |
| Gamma closed slug / title_search | 200; resolved prices | `[V]` |
| CLOB prices-history | 200; history array | `[V]` |
| Data API trades burst | 429 / CF 1015 | `[V]` soft |
| API keys created | **No** | `[V]` |
| Orders placed | **No** | `[V]` |

*End TRACK B DATA PLAN — 2026-09-11. Claims limited to public evidence + provisional sample on disk.*
