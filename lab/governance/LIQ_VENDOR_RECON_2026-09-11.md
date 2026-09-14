# LIQ vendor reconnaissance — paid liquidation-history backfill (NO PURCHASE)
**Document:** `LIQ_VENDOR_RECON_2026-09-11.md`  
**Date (UTC):** 2026-09-11  
**Actor:** Grok Bot (executor) for Logan M  
**Scope:** Lightweight **paid** liquidation-history vendor recon **ONLY**. Purpose: if forward LIQ evidence becomes promising, identify the **cheapest trustworthy backfill path** for DATA-PROV-LIQ-001 / EDGE-20260911-003 Clock review.  
**Status:** RESEARCH NOTE — **no purchase, no account created, no API key requested**.  
**Related:** `DATA_PROV_CATALYST_SOURCES_2026-09-11.md` §3, `archive/audit/2026-09-11-Governor-authorize-FUNDING-OI-fetch-LIQ-forward.md` (paid LIQ hist **not** authorized).

Evidence tags: **[V]** verified this session (docs fetch / public pages); **[C]** cited public docs; **[O]** operator/lab assumption; **[P]** prior lab artifact; **[U]** unknown / paywalled / not verified here.

---

## Context (lab)
- Free Binance Vision **UM** `liquidationSnapshot` is **empty**; live WS `!forceOrder@arr` is **forward-only** [P][V].
- Seal reference (OHLCV): **2021-01-01 → 2026-08-31** UTC [P].
- Cards require **actual venue liquidation events**, not wick inference [P].
- Governor: paid LIQ history **not authorized** as of 2026-09-11; this note is **recon only** [P].

---

## Name check
| Name in brief | Verified? | Note |
|---------------|-----------|------|
| **Tardis.dev** | Yes [V] | Tick archive; explicit `liquidations` / `forceOrder` |
| **Kaiko** | Yes [V] | `liquidation.v1/trades` + token-level volumes |
| **CoinAPI** | Yes [V] | Metrics v1 liquidation fields (venue-native; no synthetic cross-venue event feed) |
| **Amberdata** | Yes [V] | `/markets/futures/liquidations/{instrument}` historical |
| **Laevitas** | Yes [V] | Historical derivs liquidation endpoints (largely USD-aggregated bars) |
| **Coin Metrics** | Yes [V] | `/timeseries/market-liquidations` event schema |
| **CryptoTick** | **Not found** as a programmable LIQ-history vendor [V] | CryptoTicker.io charts exist; market-wide aggregation called commercial — **not** treated as a candidate archive |

---

## Ranking for Clock-fit cheap trustworthy backfill (opinion, tagged [O])
| Rank | Vendor | Why |
|------|--------|-----|
| 1 | **Tardis.dev** | Event-level WS capture; Binance UM `forceOrder` since **2020-01-07**; CSV + API; **public list prices**; transparent Binance 1s aggregation limit [V][C] |
| 2 | **Coin Metrics** | Harmonized event schema + excellent methodology (order vs trade, side convention, known gaps); Pro quote **[U]** [V][C] |
| 3 | **Amberdata** | Event-level futures liquidations; REST; sales/on-demand pricing **[U]** [V][C] |
| 4 | **Kaiko** | Tick liquidation events + USD aggregates; add-on to L1/L2 packs; enterprise sales **[U]** [V][C] |
| 5 | **CoinAPI** | Lowest **public** entry ($79+/mo); liquidation via **Metrics** not a unified event dump — weaker Clock audit story [V][C] |
| 6 | **Laevitas** | Convenient USD long/short bars; **aggregated** — poor fit if Clock demands per-event force-order lineage [V][C] |

**Cheapest trustworthy path (conditional on forward LIQ promising):** start quote/order form for **Tardis Perpetuals or Derivatives** Solo/Pro with billing interval that covers seal start (**≥4y history** → yearly Solo/Pro, or Business yearly for full depth) [C][O]. Do **not** buy until Logan re-authorizes [P].

---

## Summary matrix

| VENDOR | COVERAGE | VENUES (liq-relevant) | BTC/ETH | START DATE (notable) | EVENT GRANULARITY | RAW VS AGGREGATED | TIMESTAMP SEMANTICS | HISTORICAL DEPTH | API/DOWNLOAD | LICENSING | COST | KNOWN LIMITATIONS | QUALITY/REPUTATION | FIT FOR CLOCK REVIEW |
|--------|----------|----------------------|---------|----------------------|-------------------|-------------------|---------------------|------------------|--------------|-----------|------|-------------------|--------------------|----------------------|
| **Tardis.dev** | Derivs WS tick archive incl. liquidations | Binance UM/CM, Bybit, OKX, BitMEX, Deribit, Kraken Futs, Bitget, Gate, HTX, Hyperliquid, … (Perpetuals/Derivatives plans) [C] | Yes (e.g. BTCUSDT/ETHUSDT on `binance-futures`) [V] | Binance `forceOrder` **2020-01-07**; Bybit/OKX liq CSV often **~2020-12-18** [V][C] | Event rows; Binance = latest per symbol per **1000ms** window [V] | Normalized CSV **+** exchange-native replay [V] | `timestamp` = exchange µs (fallback local); `local_timestamp` = capture µs [V] | Multi-year; Business yearly = all avail. since ~2019-03-30 majority; Solo/Pro yearly = **4y** fixed start [V] | HTTP replay, tardis-machine, **daily CSV.gz** [V] | Subscription ToS; Academic/Solo/Pro/Business [C] | **Public list** on tardis.dev: plan tiers roughly **$350–$3,500/mo** by plan×tier; liq not sold alone [C]. Exact checkout for Perpetuals Solo yearly: confirm form **[U]** | Inherits exchange feed limits (Binance 1s aggregate); no one-off date-range purchase [V][C] | Strong among quants; transparent incidents [C][O] | **Best** default for seal-aligned event backfill [O] |
| **Coin Metrics** | Futures market liquidations | Binance, Bitfinex, BitMEX, Bybit, Deribit, dYdX, Huobi, Kraken, OKEx [V] | Yes (`binance-BTCUSDT-future` etc.) [V] | Per-market; see coverage explorer **[U exact start per market]** [C] | One obs per liq **order** or **trade** (`type`) [V] | Harmonized events; separate Liquidation Metrics for 5m/1h/1d [V] | `time` = exchange event (or receive on some venues); `database_time` = store time [V] | Deep where collected; outages often **unfillable** (no exchange hist) [V] | REST `/timeseries/market-liquidations` + WS stream [V] | Community (limited) vs Pro/Enterprise [C] | Pro/Enterprise **[U]** (sales). Community free non-commercial — confirm whether full LIQ hist is included **[U]** [C] | Binance post-2021-04-27 = ≤1 update/s aggregate; known gaps 2021; amount units venue-native [V] | Institutional; methodology gold-standard [C][O] | **Excellent** if Pro quote ≤ Tardis for needed window [O] |
| **Amberdata** | Futures (+ options) liquidations | Multi-CEX via `exchange=` (e.g. binance); coverage table by dataset [V][C] | BTCUSDT examples in docs [V] | Blog/coverage cites Binance liq from **~2020-05-15**, Bybit **~2021-10-05** [C] — reconfirm before buy **[U]** | Event-level historical rows (price, volume, side, positionType) [V] | Event endpoint + separate analytics aggregates [V] | `exchangeTimestamp` (+ optional ns); formats ms/iso/hr [V] | Query max span **731 days**/request; page via cursor [V] | REST `x-api-key`; trial/on-demand/enterprise key types [V] | Subscription-tier market/exchange scoping [V] | Trial UAT; On-Demand UAO / Enterprise UAK — **list $ [U]** [V] | BitMEX volume = contracts not base; must use multiplier [V] | Established market-data vendor [C][O] | **Good** event path; cost opaque [O] |
| **Kaiko** | Derivative liquidation **events** + token-level volumes | Cefi deriv markets (codes e.g. `bbit`); see Kaiko coverage [V][C] | ETH-USDT / BTC instruments via instrument codes [V] | Access range example shows early bound ~2023-07 in sample payload — **do not treat as global start**; confirm coverage **[U]** [V] | Tick events: amount, price, `position_side`, `trade_id` [V] | Events **and** interval USD volumes [V] | Exchange or collection ts (ms; docs show large ints) [V] | Historical via `start_time`/`end_time` + continuation [V] | REST `X-Api-Key`; regional hosts [V] | Add-on to L1/L2 / ticker packs; sales-led [V] | **[U]** enterprise / package quote | Add-on gating; sales onboarding (no self-serve key) [C] | Top-tier institutional brand [C][O] | **Strong** quality; likely **not cheapest** [O] |
| **CoinAPI** | Venue-native liquidation **metrics** | Selected deriv venues (BinanceFTS, BitMEX, OKEX, KrakenFTS, Deribit, …) [C] | Via symbol/exchange metrics [C] | Metric availability varies; deep hist possible but **not** one unified LIQ tape [C] | Metric samples (PRICE/QTY/SIDE/TIME…) not a single event schema [C] | Explicitly **no** synthetic cross-exchange liquidation event feed [C] | Per metric / exchange conventions [C][U] | Historical Metrics v1 REST [C] | REST/WS Market Data API [C] | Standard API ToS [C] | **Public:** Startup **$79**/mo, Streamer **$249**, Pro **$599** (+ usage) [V] | Must assemble events from metrics; coverage uneven; credits burn on deep pulls [C][O] | Broad MD vendor; LIQ is secondary surface [C][O] | **Cheap entry, weak Clock event provenance** unless schema proven [O] |
| **Laevitas** | Derivs liquidation history by market/symbol or currency | DERIBIT, BINANCE, BITFINEX, BITMEX, BYBIT, HUOBI, KRAKEN, OKX (+ AGGREGATED) [V] | Yes [V] | Not published as a single global start in fetched docs **[U]** [V] | Docs examples return **`date`, `usd_amount`, `side`** — bar/aggregate oriented [V] | Primarily **aggregated USD** long/short; granularity query param [V] | `date` epoch ms in examples [V] | Historical API with pagination (max limit 144/page) [V] | REST API v1/v2; key / subscription [C] | Commercial API [C] | **[U]** (subscription; some x402 mentions elsewhere **[U]**) | Not tick force-order dump; page limits; weak for cascade microstructure [V][O] | Popular analytics UI/API [C][O] | **Poor** if Clock requires raw venue events [O] |

---

## Per-vendor detail

### 1) Tardis.dev
| Field | Detail | Tag |
|-------|--------|-----|
| COVERAGE | Historical WS-derived market data including **liquidations** / Binance **forceOrder** | [V] |
| VENUES | Broad perp set under Perpetuals/Derivatives plans (Binance USDS-M, Bybit, OKX, BitMEX, Deribit, … Hyperliquid, Lighter, …) | [C] |
| BTC/ETH | Yes — e.g. `binance-futures` BTCUSDT/ETHUSDT | [V] |
| START DATE | Binance UM `forceOrder` **since 2020-01-07**; liq CSV datasets commonly from **2020-12-18** on Bybit/OKX swap | [V] |
| EVENT GRANULARITY | One CSV row per captured liquidation message; **Binance publishes ≤1 forceOrder update per symbol per 1000ms** (latest in window) | [V] |
| RAW VS AGGREGATED | Normalized `liquidations` CSV **and** native replay (`forceOrder` channel) | [V] |
| TIMESTAMP SEMANTICS | Exchange `timestamp` (µs) + `local_timestamp` capture; Clock should prefer exchange event time, audit lag via local | [V][O] |
| HISTORICAL DEPTH | Yearly Business = all available; Yearly Solo/Pro/Academic = **4 years** fixed start; Quarterly = 12m; Monthly = 4m | [V] |
| API/DOWNLOAD | CSV daily gz; HTTP `/data-feeds`; tardis-machine (Pro/Business) | [V] |
| LICENSING | Paid subscription; no one-off custom exports | [V] |
| COST | Public homepage list prices by plan×tier ~**$350–$3,500/mo**; Perpetuals/Derivatives/Spot/Options differ [C]. **No liq-only SKU** [C]. Exact seal-window checkout total **[U]** until order-form quote | |
| KNOWN LIMITATIONS | Subscription-only; inherits venue aggregation; early Binance collection quality notes pre-2020-05-14 on other channels | [V] |
| QUALITY/REPUTATION | Widely used by quant shops; public incident/coverage pages | [C][O] |
| FIT FOR CLOCK REVIEW | **Primary candidate** — event lineage + seal depth + transparent Binance semantics | [O] |

### 2) Coin Metrics
| Field | Detail | Tag |
|-------|--------|-----|
| COVERAGE | Market liquidations (forced closes on futures) | [V] |
| VENUES | 9 exchanges listed in methodology (Binance … OKEx) | [V] |
| BTC/ETH | Yes | [V] |
| START DATE | Per-market coverage explorer — not re-fetched exhaustively here | [C][U] |
| EVENT GRANULARITY | Event-driven; `type` = `order` \| `trade` | [V] |
| RAW VS AGGREGATED | Harmonized events; optional aggregated Liquidation Metrics | [V] |
| TIMESTAMP SEMANTICS | `time` exchange (or receive); `database_time` persistence | [V] |
| HISTORICAL DEPTH | Collector depth; gaps often permanent | [V] |
| API/DOWNLOAD | HTTP + WS | [V] |
| LICENSING | Community vs Pro | [C] |
| COST | Pro/Enterprise **[U]** | |
| KNOWN LIMITATIONS | Binance aggregation post-2021-04-27; documented 2021 undercounts; side/units caveats | [V] |
| QUALITY/REPUTATION | High — published methodology matches Clock concerns | [C][O] |
| FIT FOR CLOCK REVIEW | **Strong alternate** if quote competitive | [O] |

### 3) Amberdata
| Field | Detail | Tag |
|-------|--------|-----|
| COVERAGE | Futures liquidations historical; options liq; analytics aggregates | [V] |
| VENUES | Parameterized `exchange` (docs default binance); multi-CEX coverage tables | [V][C] |
| BTC/ETH | Yes (BTCUSDT examples) | [V] |
| START DATE | Cited ~2020-05-15 Binance / ~2021-10-05 Bybit for liquidations — **verify on buy** | [C][U] |
| EVENT GRANULARITY | Per-event rows (side, positionType, price, volume) | [V] |
| RAW VS AGGREGATED | Both (event + analytics total) | [V] |
| TIMESTAMP SEMANTICS | `exchangeTimestamp` | [V] |
| HISTORICAL DEPTH | Multi-year claimed; **≤2y per request** | [V] |
| API/DOWNLOAD | REST + cursor pagination | [V] |
| LICENSING | Trial / on-demand exchange-scoped / enterprise | [V] |
| COST | **[U]** | |
| KNOWN LIMITATIONS | Exchange scoping on cheaper tiers; BitMEX contract volume quirk | [V] |
| QUALITY/REPUTATION | Established | [C][O] |
| FIT FOR CLOCK REVIEW | Good if quote ≤ Tardis and start dates cover seal | [O] |

### 4) Kaiko
| Field | Detail | Tag |
|-------|--------|-----|
| COVERAGE | Derivative liquidation events; token-level liquidation volumes | [V] |
| VENUES | Kaiko cefi derivative exchange codes | [C] |
| BTC/ETH | Yes | [V] |
| START DATE | Confirm per instrument — sample access_range ≠ proof of full seal | [V][U] |
| EVENT GRANULARITY | Tick events with USD conversions | [V] |
| RAW VS AGGREGATED | Both | [V] |
| TIMESTAMP SEMANTICS | Exchange or collection timestamp | [V] |
| HISTORICAL DEPTH | Queryable historically under package access | [V] |
| API/DOWNLOAD | REST + pagination tokens | [V] |
| LICENSING | Add-on to L1/L2 packages; sales-provisioned keys | [V][C] |
| COST | **[U]** | |
| KNOWN LIMITATIONS | Likely package bundling cost; sales cycle | [C][O] |
| QUALITY/REPUTATION | Institutional standard | [C][O] |
| FIT FOR CLOCK REVIEW | High quality; expect higher $ than Tardis Solo | [O] |

### 5) CoinAPI
| Field | Detail | Tag |
|-------|--------|-----|
| COVERAGE | Liquidation-related **Metrics v1** by exchange | [C] |
| VENUES | Subset of derivatives exchanges | [C] |
| BTC/ETH | Supported where metrics exist | [C] |
| START DATE | Varies **[U]** | |
| EVENT GRANULARITY | Metric time series — not advertised as unified LIQ event dump | [C] |
| RAW VS AGGREGATED | Venue-native metrics; vendor refuses synthetic cross-venue event feed | [C] |
| TIMESTAMP SEMANTICS | Metric-dependent **[U]** | |
| HISTORICAL DEPTH | Via Metrics history endpoints | [C] |
| API/DOWNLOAD | REST / WS Market Data API | [C] |
| LICENSING | Self-serve plans | [V] |
| COST | Startup **$79**, Streamer **$249**, Pro **$599** /mo (+ overage) [V] | |
| KNOWN LIMITATIONS | Reconstruction burden; may fail Clock “actual events” bar without careful schema map | [O] |
| QUALITY/REPUTATION | Solid MD API; LIQ not flagship | [C][O] |
| FIT FOR CLOCK REVIEW | **Only if** metrics reconstruct to auditable force-order events — else reject | [O] |

### 6) Laevitas
| Field | Detail | Tag |
|-------|--------|-----|
| COVERAGE | Historical liquidations by symbol / by currency | [V] |
| VENUES | Major CEX list + AGGREGATED | [V] |
| BTC/ETH | Yes | [V] |
| START DATE | **[U]** | |
| EVENT GRANULARITY | Example payloads are **USD amount + side + date** | [V] |
| RAW VS AGGREGATED | Aggregated | [V] |
| TIMESTAMP SEMANTICS | Bar `date` | [V] |
| HISTORICAL DEPTH | API historical; page size capped | [V] |
| API/DOWNLOAD | REST | [V] |
| LICENSING | Paid API | [C] |
| COST | **[U]** | |
| KNOWN LIMITATIONS | Not raw forceOrder tape | [V] |
| QUALITY/REPUTATION | Analytics-oriented | [C][O] |
| FIT FOR CLOCK REVIEW | **Low** for DATA-PROV-LIQ-001 event standard | [O] |

---

## Clock review checklist (if a vendor is later purchased)
1. Source = venue force-order / liquidation feed lineage (not wick inference) [P]
2. Document exchange aggregation (esp. **Binance ≤1/s**) as known undercount, not silent completeness [V][P]
3. Prefer exchange event time; store vendor receive/local separately [P]
4. Side convention locked (Tardis CSV: `buy` = short liq, `sell` = long liq) [V] — confirm vs Binance forceOrder before SIGNAL [C][U until frozen]
5. Hash purchased dump; license/redistribution constraints on dataset card [P]
6. Holdout only where prints exist; do not invent pre-coverage zeros [P]

---

## Explicit non-actions this note
- No purchase / checkout / trial signup / API key request [V]
- No bulk download of paid datasets
- No EDGE or DATA card registration changes
- No contradiction of Governor “forward LIQ only / no paid hist” authorization [P]

## Sources consulted (non-exhaustive)
- https://docs.tardis.dev/… (liquidations schema, billing, binance-futures `forceOrder`) [V]
- https://tardis.dev/ (public list pricing tables) [V]
- https://docs.kaiko.com/…/derivative-liquidation-events [V]
- https://docs.amberdata.io/http/market/futures-liquidations [V]
- https://www.coinapi.io/blog/crypto-liquidation-data + pricing page [V]
- https://gitbook-docs.coinmetrics.io/…/market-liquidations [V]
- https://docs.laevitas.ch/derivs/historical [V]
- Lab: `DATA_PROV_CATALYST_SOURCES_2026-09-11.md`, Governor LIQ-forward audit [P]

---

**Bottom line:** For a future Logan-approved seal-aligned LIQ backfill, **Tardis.dev** is the leading cheapest-trustworthy candidate (public pricing, event CSV, Binance UM from 2020-01-07 with documented 1s aggregation). **Coin Metrics** is the quality alternate if Pro quote competes. **CoinAPI** is cheapest public entry but weaker event provenance. **Kaiko/Amberdata** are solid but price-opaque. **Laevitas** is analytics/agg — poor Clock event fit. **CryptoTick** not verified as an archive vendor.
