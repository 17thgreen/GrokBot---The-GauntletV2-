# DATA-PROV Catalyst sources — provisional registration research
**Document:** `DATA_PROV_CATALYST_SOURCES_2026-09-11.md`  
**Date (UTC):** 2026-09-11  
**Scope:** Read-only source map for provisional registration of **DATA-PROV-LIQ-001**, **DATA-PROV-OI-001**, **DATA-PROV-FUNDING-001** on Binance **USD-M** `BTCUSDT` + `ETHUSDT` to unblock Cycle 5 Catalyst Edges **EDGE-20260911-003…006**.  
**Status:** RESEARCH NOTE — **no multi-GB fetch**; **not** Clock VERDICT; **not** Examiner-ready.  
**Related:** `DATA_PROV_CATALYST_001_SPEC.md`, `CYCLE_5_RESEARCH_ORDERS.md`, `catalyst/cycle5/INTAKE-CAT-C5-20260911.md`, `catalyst/cycle5/EVAL_ENDPOINTS-C5.md`.

## Mission-layer note (binding context)
These series are **Layer-3 external predictors** under `PREDICTION_MARKET_MISSION_2026-09-11.md` §7 (crypto microstructure exports / positioning stress) when reused for PM forecasts.  
They are **not** prediction-market **Layer-1** (venue contract/order/resolution adapters). Cycle 5 futures mechanism tests remain primary for EDGE-003…006; binary P(resolve) scoring is additive per `EVAL_ENDPOINTS-C5.md`.

OHLCV seal window reference (DATA-PROV-001): **2021-01-01 00:00 → 2026-08-31 23:55 UTC** [V].

Evidence tags: **[V]** verified this session (Vision HEAD/S3 list / tiny CSV peek); **[C]** cited public docs/issues; **[O]** operator/lab assumption; **[P]** prior lab artifact; **[U]** unknown / not verified here.

---

## Shared venue / access facts
| Fact | Detail | Tag |
|------|--------|-----|
| Archive host | `https://data.binance.vision/` (S3: `s3-ap-northeast-1.amazonaws.com/data.binance.vision`) | [V][C] |
| REST base (USD-M) | `https://fapi.binance.com` | [C] |
| WS base (USD-M) | `wss://fstream.binance.com` | [C] |
| This box → fapi | Geo eligibility block (`code:0` restricted-location / HTTP 451 on probes) | [V] |
| This box → Vision | Reachable; listings + object HEAD work | [V] |
| Provisional preference | Prefer **Vision archives** for historical backfill; do not assume fapi reachable from every agent host | [O] |

Official developers.binance.com market-data pages were JS/bot-gated from WebFetch this session [V]. Endpoint names below are taken from Binance public mirrors / connector docs + live Vision peeks — **not fabricated**. Where REST path strings were not re-verified against the live OpenAPI HTML, tagged **[C]**.

---

## 1. DATA-PROV-FUNDING-001 (settled funding)

### Unlocks
EDGE-20260911-005 (funding-only), EDGE-20260911-006 (funding × OI); parent EDGE-20260910-010 lineage.

### Public endpoints / Vision archives
| Source | URL / path | Auth | Role |
|--------|------------|------|------|
| **Vision monthly (preferred historical)** | `https://data.binance.vision/data/futures/um/monthly/fundingRate/{SYMBOL}/{SYMBOL}-fundingRate-{YYYY-MM}.zip` | none | Settlement prints archive [V] |
| Listing UI | `https://data.binance.vision/?prefix=data/futures/um/monthly/fundingRate/BTCUSDT/` (same for ETHUSDT) | none | Browse [V] |
| REST history | `GET /fapi/v1/fundingRate?symbol=&startTime=&endTime=&limit=` (limit typically ≤1000) | none (MARKET_DATA) | Live/tail + pagination [C]; **geo-blocked on this box** [V] |
| REST mark / predicted | `GET /fapi/v1/premiumIndex?symbol=` → fields such as `lastFundingRate`, `nextFundingTime` | none | **Not** a settled-history substitute; leakage surface [C] |
| Funding info | `GET /fapi/v1/fundingInfo` (interval changes) | none | Metadata for interval hours [C][U exact field set] |

**Vision CSV schema (peeked):** header `calc_time,funding_interval_hours,last_funding_rate` — `calc_time` epoch **ms** [V] (sample `BTCUSDT-fundingRate-2021-01.zip`, ~1 KB).

### Timestamp semantics
| Field | Meaning | Use at decision t |
|-------|---------|-------------------|
| `calc_time` / REST `fundingTime` | **Settlement / calculation event time** of the funding print | Knowable only if `settlement_ts ≤ t` [P][C] |
| `funding_interval_hours` | Interval length (historically 8h; can vary) | Metadata; do not invent mid-interval “accrued” rate for SIGNAL [V][C] |
| `last_funding_rate` | Rate applied at that settlement | Feature value after settlement [V] |
| `premiumIndex.lastFundingRate` / predicted next | Live / next-interval estimate | **Forbidden** for SIGNAL until that interval settles [P] |

Publish lag after `calc_time` on Vision: archives appear after period close (monthly pack; REST nearer real-time) — treat REST vs Vision as same settlement clock if values match; document any Vision file delay separately [C][U exact REST-vs-Vision lag].

### Knowability risks
1. **Funding settlement leak:** using the rate of the **not-yet-settled** interval (or `premiumIndex` “current” rate) at t before settlement → hard FAIL for Clock [P].
2. **Interval regime change:** `funding_interval_hours` ≠ 8 in places — z-score / “D consecutive prints” windows must use print sequence, not assume 3/day [V][C].
3. **Join to 5m bars:** settlement timestamps are sparse; align with inclusive rule on completed 5m closes from DATA-PROV-001 [P].

### Historical coverage without paid vendor
| Symbol | Vision zip span | Approx size (all months on Vision) | Tag |
|--------|-----------------|--------------------------------------|-----|
| BTCUSDT | **2020-01 → 2026-08** (80 monthly zips) | ~0.07 MB total zips | [V] |
| ETHUSDT | **2020-01 → 2026-08** (80 monthly zips) | ~0.07 MB total zips | [V] |

REST deep history: pagination possible in principle [C]; **not relied on** here because fapi blocked on this host [V]. No paid vendor required for full seal-aligned funding history via Vision [V].

### Recommended provisional fetch scope
- **Symbols:** BTCUSDT, ETHUSDT  
- **Range:** **2021-01-01 → 2026-08-31** (match OHLCV seal; Vision months 2021-01 … 2026-08) [V][P]  
- **Source:** Vision monthly fundingRate only for v0  
- **Volume:** ≪ 1 MB — **not** multi-GB  

### What Clock must audit
- Settlement-only rule: no future / predicted funding in features  
- `calc_time` timezone = exchange ms UTC; monotonic per symbol  
- Interval-hour changes catalogued; no silent 8h assumption  
- Duplicates / missing settlements vs expected schedule (allow documented gaps)  
- Join integrity to DATA-PROV-001 5m closes; seal proposal align to SEAL_LOCK where coverage allows  
- Source identity: Vision path + CHECKSUM when fetched  

---

## 2. DATA-PROV-OI-001 (open interest)

### Unlocks
EDGE-20260911-004 (OI shock); EDGE-20260911-006 (funding × OI).

### Public endpoints / Vision archives
| Source | URL / path | Auth | Role |
|--------|------------|------|------|
| **Vision daily metrics (preferred historical)** | `https://data.binance.vision/data/futures/um/daily/metrics/{SYMBOL}/{SYMBOL}-metrics-{YYYY-MM-DD}.zip` | none | 5m OI + ratios [V] |
| Listing UI | `https://data.binance.vision/?prefix=data/futures/um/daily/metrics/BTCUSDT/` | none | Browse [V] |
| REST current | `GET /fapi/v1/openInterest?symbol=` | none | Point-in-time only [C] |
| REST hist stats | `GET /futures/data/openInterestHist?symbol=&period=&limit=&startTime=&endTime=` (`period` ∈ {5m,15m,30m,1h,2h,4h,6h,12h,1d}) | none | Short rolling window — commonly cited **~30 days** retention [C]; **not** multi-year [C]; geo-blocked here [V] |

**Vision CSV schema (peeked):**  
`create_time,symbol,sum_open_interest,sum_open_interest_value,count_toptrader_long_short_ratio,sum_toptrader_long_short_ratio,count_long_short_ratio,sum_taker_long_short_vol_ratio`  
with `create_time` as `YYYY-MM-DD HH:MM:SS` at **5-minute** steps [V] (sample `BTCUSDT-metrics-2023-01-01.zip`).

Units: `sum_open_interest` = contracts/base qty; `sum_open_interest_value` = notional [C][V]. Declare units on dataset card.

### Timestamp semantics
| Field | Meaning | Use at decision t |
|-------|---------|-------------------|
| `create_time` | Exchange **observation / snapshot time** of the metrics row | OI knowable iff snapshot_ts ≤ t [P] |
| REST `openInterestHist.timestamp` | Bucket timestamp for aggregated hist | Same rule; confirm ms vs s on fetch [C][U] |
| Day-file partition | File for day D can include a row stamped just into D+1 | Midnight double-write risk — take latest-by-timestamp per bucket, not last-writer [C] |

**Not** trade-event time; **not** funding settlement time. OI is a **level** (last sample in bar), not a sum [C].

### Knowability risks
1. **OI lag / coarse clock:** native 5m Vision cadence — shocks inside a 5m bin only visible at bin stamp; do not pretend sub-5m knowability from this source [V].  
2. **REST hist truncation:** building “history” from `/openInterestHist` alone invents a false deep book after ~30d [C].  
3. **Revision / restatement:** if a day zip is re-uploaded (known past metrics gap repair, e.g. 2023-09-18 incident [C]), Clock needs first-print vs restated policy.  
4. **ETH coverage shortfall vs OHLCV seal** (below) — do not silently pad or forward-fill into 2021 [O].  
5. Extra ratio columns are **not** required for EDGE-004/006 SIGNAL; exclude unless separately registered [O].

### Historical coverage without paid vendor
| Symbol | Vision metrics earliest → latest listed | Approx zip bytes on Vision | Tag |
|--------|-----------------------------------------|----------------------------|-----|
| BTCUSDT | **2020-09-01 → 2026-09-09** (2200 daily zips; ~25.5 MB) | covers full OHLCV seal | [V] |
| ETHUSDT | **2021-12-01 → 2026-09-09** (1744 daily zips; ~20.6 MB) | **missing 2021-01-01→2021-11-30** vs seal | [V] |

Paid vendors (e.g. Tardis `derivative_ticker` / openInterest from ~2020-05) exist for denser/longer OI [C] — **not required** for BTC seal-aligned 5m Vision OI; **optional** if Logan wants ETH pre-2021-12 or sub-5m [C][U pricing].

### Recommended provisional fetch scope
| Symbol | Provisional range | Rationale |
|--------|-------------------|-----------|
| BTCUSDT | **2021-01-01 → 2026-08-31** | Match OHLCV seal [V][P] |
| ETHUSDT | **2021-12-01 → 2026-08-31** | Honest shorter; Vision start [V] |

- **Source:** Vision `daily/metrics` only for v0  
- **Volume:** order **~40–55 MB** compressed for both symbols over seal-ish window — **not** multi-GB [V]  
- Document ETH start ≠ BTC/OHLCV start on dataset card and Edge abstention rules  

### What Clock must audit
- Snapshot time ≤ t; no look-ahead restatement without quarantine  
- 5m grid completeness / gap list; midnight partition duplicates  
- Units explicit; BTC vs ETH coverage asymmetry  
- Alignment rule to 5m OHLCV closes for ΔOI / divergence features  
- Forbidden: inferred OI from price or volume  
- Seal proposal: joint holdout only where **both** OI and OHLCV exist (ETH joint seal starts ≥ 2021-12-01) [O]

---

## 3. DATA-PROV-LIQ-001 (venue liquidations)

### Unlocks
EDGE-20260911-003 (liq exhaust / fade); parent EDGE-20260910-009. Cards require **actual venue liquidation events**, **not** wick inference [P].

### Public endpoints / Vision archives
| Source | URL / path | Status for USD-M BTCUSDT/ETHUSDT | Tag |
|--------|------------|----------------------------------|-----|
| Vision UM liquidationSnapshot | `data/futures/um/daily/liquidationSnapshot/` (and monthly) | **Empty** — S3 `KeyCount=0`; sample object HEADs 404 | [V] |
| Binance staff | Issue #361: “this data is no longer provided”; #420: UM historical snapshots removed / unrestored as of 2025-08 commentary | Confirms discontinuation | [C] |
| Vision CM liquidationSnapshot | `data/futures/cm/daily/liquidationSnapshot/{SYMBOL}/` | **Exists** but **COIN-M** (e.g. `BTCUSD_PERP`), not USD-M `BTCUSDT`; sample span ~2023-06-25→2024-10-14 for BTCUSD_PERP | [V] — **wrong product family** for this registration |
| WS all-market | `wss://fstream.binance.com/ws/!forceOrder@arr` | Live liquidation stream; **no historical replay** | [C] |
| WS per-symbol | `<symbol>@forceOrder` | Live only | [C] |
| REST user force orders | `GET /fapi/v1/forceOrders` (USER_DATA — **own account** only) | Not market-wide history | [C] |
| REST market-wide historical forceOrders / allForceOrders | Often cited historically; community reports **451 / removed / docs stale** | **Not usable** as free deep history from this research host | [C][V geo] |

**CM snapshot CSV schema (wrong market; for contrast only):**  
`time,side,order_type,time_in_force,original_quantity,price,average_price,order_status,last_fill_quantity,accumulated_fill_quantity` [V].

### Timestamp semantics (when a real feed exists)
| Field | Meaning | Use at decision t |
|-------|---------|-------------------|
| Exchange event `time` / `E`/`T` on forceOrder stream | Liquidation **order event time** | Burst windows may include only events with event_ts ≤ t [P][C] |
| Ingest/receive time | Local capture clock | Audit only; do not substitute for event time in SIGNAL [P] |
| Inferred “liq” from OHLCV wicks | **Not** venue force-order | **Forbidden** if card claims actual liq [P] |

### Knowability risks
1. **Inference vs forceOrders:** labeling wick/volume spikes as liquidations falsifies EDGE-003 mechanism and fails Clock [P].  
2. **No free UM historical archive:** cannot backtest 2021→2026 actual liqs from Vision [V].  
3. **Live WS only:** forward capture starts at collector go-live; survivorship / outage gaps [O].  
4. **CM proxy temptation:** COIN-M `BTCUSD_PERP` liq ≠ USD-M `BTCUSDT` liq — do not cross-wire without explicit VERSION + Logan venue lock [O][V].  
5. **Paid vendor** (e.g. Tardis forceOrder archives cited from ~2020-01-07 [C]): cost + licensing — **Logan approval** before purchase [O].

### Historical coverage without paid vendor
| Path | UM BTCUSDT/ETHUSDT deep history | Tag |
|------|----------------------------------|-----|
| Vision UM liquidationSnapshot | **None (empty)** | [V] |
| Free REST market-wide hist | **Not established / unavailable** from this host | [C][V] |
| Free WS | Forward-only from capture start | [C] |
| Honest provisional history length | **Empty** until paid archive or live collector accumulates | [V][O] |

### Recommended provisional fetch scope
**Do not claim seal-aligned LIQ history.** Options for Archivist/Clock:

| Option | Scope | Cost | Notes |
|--------|-------|------|-------|
| **A. Register DATA-BLOCKED / empty raw** | Card stub + provenance of negative Vision result | $0 | EDGE-003 stays DATA-BLOCKED for historical RESEARCH TEST [O] |
| **B. Live WS capture forward** | `!forceOrder@arr` filtered to BTCUSDT/ETHUSDT from go-live → … | $0 infra (bandwidth small) | Honest short range; not 2021–2026 [C][O] |
| **C. Paid historical vendor** | Vendor UM forceOrder for seal window | **Paid — needs Logan approval** | Only path to seal-aligned EDGE-003 test known here [C][U vendor quote] |

**Forbidden under provisional registration:** wick-inferred liq labeled as DATA-PROV-LIQ-001; CM snapshot silently renamed to UM [P][O].

### What Clock must audit
- Source = actual force-order / liquidationSnapshot lineage (or explicit QUARANTINE if empty)  
- Event time vs receive time; ordering; duplicate event IDs  
- Side semantics (BUY force order ≈ long liq vs short — confirm against stream docs before SIGNAL lock) [C][U until stream schema frozen]  
- No wick inference; no CM→UM aliasing  
- Coverage honesty vs DATA-PROV-001 seal; holdout only where liq prints exist  
- If vendor: license, redistribution, and hash of purchased dump  

---

## Cross-cutting provisional registration matrix

| DATA_ID | Free historical for seal window? | Recommended v0 scope | Approx free volume | Blocks which EDGE |
|---------|----------------------------------|----------------------|--------------------|-------------------|
| DATA-PROV-FUNDING-001 | **Yes** (Vision) | 2021-01→2026-08 BTC+ETH | ≪1 MB | 005, 006 |
| DATA-PROV-OI-001 | **Partial** — BTC yes; ETH from **2021-12-01** | BTC 2021-01→2026-08; ETH 2021-12→2026-08 | ~40–55 MB | 004, 006 |
| DATA-PROV-LIQ-001 | **No** free UM history | Empty / live-forward / or paid | $0 or paid | **003** (and any liq-gated child) |

EDGE-20260911-004/005/006 can proceed toward Clock on **FUNDING+OI** alone once fetched+audited; EDGE-20260911-003 remains blocked on actual LIQ history unless Logan approves paid backfill or accepts forward-only power limits [O][P].

---

## Safe provisional fetch — feasibility without Logan cost approval

| Action | Feasible without cost approval? | Rationale |
|--------|----------------------------------|-----------|
| Vision **fundingRate** BTC+ETH (2021-01…2026-08) | **YES** | Public, free, ≪1 MB [V] |
| Vision **metrics** OI BTC (2021-01…2026-08) + ETH (2021-12…2026-08) | **YES** | Public, free, ~tens of MB (not multi-GB) [V] |
| Vision / free REST **UM liquidations** historical seal window | **NO** | Archive empty; no free deep hist verified [V][C] |
| Paid liq/OI denser vendor | **NO without Logan** | Cash/license [O] |
| fapi REST from **this** box | **Not currently** | Geo eligibility block [V] — use Vision or an eligible egress host |

**Bottom line:** A **safe provisional fetch** of **FUNDING-001 + OI-001** from Binance Vision is **feasible without Logan cost approval** (bandwidth/storage trivial). **LIQ-001 historical** is **not** safely/fetchably free for USD-M BTCUSDT+ETHUSDT; register honestly as empty/blocked or seek Logan approval for paid history / accept live-forward-only.

---

## Explicit non-actions this note
- No bulk download of metrics/funding beyond tiny schema peeks (~15 KB) [V]  
- No paid vendor calls; no account API keys  
- No EDGE-003…006 body edits; no Clock VERDICT issued here  

## Sources consulted (non-exhaustive)
- Vision S3 listings + HEAD/tiny ZIP peeks (2026-09-11) [V]  
- `github.com/binance/binance-public-data` issues #211, #276, #361, #420 [C]  
- Binance connector WS stream catalog (`!forceOrder@arr`, `<symbol>@forceOrder`) [C]  
- binance-skills-hub `futures-usds.md` market-data endpoint table [C]  
- Lab: `DATA_PROV_CATALYST_001_SPEC.md`, Cycle 5 intake/orders, DATA-PROV-001 seal span [P]  

*End research note.*
