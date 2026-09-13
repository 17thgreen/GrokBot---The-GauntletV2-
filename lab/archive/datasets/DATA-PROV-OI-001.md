# DATA-PROV-OI-001

- **DATA_ID:** DATA-PROV-OI-001
- **STATUS:** CONDITIONAL
- **Registered / intake:** 2026-09-11 UTC (Archivist provisional fetch)
- **Fetch complete:** 2026-09-11T04:23:20Z (manifest)
- **Manifest:** `/workspace/lab/data/DATA-PROV-OI-001/provenance/DOWNLOAD_MANIFEST.md`
- **Authorized:** Logan 2026-09-11 — FUNDING + OI only (no paid LIQ history)
- **Spec / source map:** `/workspace/lab/governance/DATA_PROV_CATALYST_SOURCES_2026-09-11.md` §2
- **Path:** `/workspace/lab/data/DATA-PROV-OI-001/`
- **Role:** Provisional open-interest / metrics snapshots — Layer-3 for EDGE-20260911-004 / EDGE-20260911-006. Not venue marriage.

## Series (public metadata)

| Field | Value |
|-------|-------|
| Venue | Binance USD-M Futures (UM) |
| Instruments | BTCUSDT, ETHUSDT |
| Source | Binance Vision daily `metrics` (free; no fapi) |
| URL pattern | `https://data.binance.vision/data/futures/um/daily/metrics/{SYMBOL}/{SYMBOL}-metrics-{YYYY-MM-DD}.zip` |
| BTC range | 2021-01-01 → 2026-08-31 (match OHLCV seal) |
| ETH range | **2021-12-01 → 2026-08-31 only** (Vision metrics earliest for ETHUSDT) |
| ETH short seal | **Intentional gap 2021-01-01 → 2021-11-30** vs DATA-PROV-001 OHLCV seal — do **not** invent / forward-fill; document abstention |
| Storage | `raw/{SYMBOL}/{SYMBOL}-metrics-{YYYY-MM-DD}.zip` + `.sha256` sidecars |
| Provenance | `provenance/SHA256SUMS.txt`, `provenance/DOWNLOAD_MANIFEST.md` |
| Expected volume | ~tens of MB compressed (not multi-GB) |

## Timestamp semantics (from source map)

| Field | Meaning | Use at decision t |
|-------|---------|-------------------|
| `create_time` | Exchange observation / snapshot time (`YYYY-MM-DD HH:MM:SS`, 5m steps) | OI knowable iff `snapshot_ts ≤ t` |
| Day-file partition | File for day D may include a row stamped into D+1 | Midnight double-write — take latest-by-timestamp per bucket |

**Not** trade-event time; **not** funding settlement time. OI is a **level** (last sample in bar), not a sum.

## CSV schema (Vision peek)

`create_time,symbol,sum_open_interest,sum_open_interest_value,count_toptrader_long_short_ratio,sum_toptrader_long_short_ratio,count_long_short_ratio,sum_taker_long_short_vol_ratio`

Units: `sum_open_interest` = contracts/base qty; `sum_open_interest_value` = notional. Extra ratio columns not required for EDGE-004/006 SIGNAL unless separately registered.

## ETH coverage asymmetry (binding)

- BTC OI covers full OHLCV seal window.
- ETH OI joint seal with DATA-PROV-001 starts **≥ 2021-12-01**.
- Edge abstention required where ETH OI absent (2021-01-01 → 2021-11-30).


## Inventory [V Archivist]

| Symbol | Daily zips | First | Last | Missing in range | Zip bytes |
|--------|------------|-------|------|------------------|-----------|
| BTCUSDT | 2069 | 2021-01-01 | 2026-08-31 | 0 | 23,861,538 |
| ETHUSDT | 1735 | 2021-12-01 | 2026-08-31 | 0 | 20,459,807 |

- Combined zip bytes: **44,321,345** (~42.3 MiB)
- SHA256SUMS lines: **3804**; sidecars 2069+1735 [V]
- Sampled unzip -t + sidecar recompute: PASS [V]
- ETH intentional gap vs OHLCV seal: **334 days** 2021-01-01→2021-11-30 (not fetched, not invented)
- `derived/`: empty
- Completion: FULL within documented ranges

## Access gates

| Path | Access |
|------|--------|
| raw/ | immutable provenance; awaiting Clock |
| derived/ | empty until approved transforms |
| Examiner | HOLD until Clock DATA VERDICT |

## Status history

1. FETCH_IN_PROGRESS
2. PENDING_CLOCK (fetch COMPLETE 2026-09-11T04:23:20Z; awaiting Clock)
3. **CONDITIONAL** ← current (2026-09-11T04:39:57Z) — Clock APPROVED_WITH_LIMITATIONS; Examiner CLEARED for Catalyst edges after Conductor route

## Notes for Clock

- Snapshot time ≤ t; no look-ahead restatement without quarantine
- 5m grid completeness / midnight partition duplicates
- BTC vs ETH coverage asymmetry must remain explicit
- Forbidden: inferred OI from price or volume; inventing pre-2021-12 ETH days
- fapi geo-blocked on fetch host; Vision-only path [V]

## Clock DATA VERDICT
- **Verdict:** CONDITIONAL
- **Quality:** APPROVED_WITH_LIMITATIONS
- **Issued:** 2026-09-11T04:39:57Z
- **Full verdict:** `/workspace/lab/data/DATA-PROV-OI-001/provenance/DATA_VERDICT_DATA-PROV-OI-001.md`
- **Archive audit:** `archive/audit/2026-09-11-Clock-DATA-VERDICT-DATA-PROV-OI-001.md`
