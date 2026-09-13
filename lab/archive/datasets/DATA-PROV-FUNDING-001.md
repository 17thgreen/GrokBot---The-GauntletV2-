# DATA-PROV-FUNDING-001

- **DATA_ID:** DATA-PROV-FUNDING-001
- **STATUS:** CONDITIONAL
- **Registered / intake:** 2026-09-11 UTC (Archivist provisional fetch)
- **Fetch complete:** 2026-09-11T04:20:34Z (manifest)
- **Manifest:** `/workspace/lab/data/DATA-PROV-FUNDING-001/provenance/DOWNLOAD_MANIFEST.md`
- **Authorized:** Logan 2026-09-11 — FUNDING + OI only (no paid LIQ history)
- **Spec / source map:** `/workspace/lab/governance/DATA_PROV_CATALYST_SOURCES_2026-09-11.md` §1
- **Path:** `/workspace/lab/data/DATA-PROV-FUNDING-001/`
- **Role:** Provisional settled funding prints — Layer-3 microstructure export for EDGE-20260911-005 / EDGE-20260911-006. Not venue marriage.

## Series (public metadata)

| Field | Value |
|-------|-------|
| Venue | Binance USD-M Futures (UM) |
| Instruments | BTCUSDT, ETHUSDT |
| Source | Binance Vision monthly `fundingRate` (free; no fapi) |
| URL pattern | `https://data.binance.vision/data/futures/um/monthly/fundingRate/{SYMBOL}/{SYMBOL}-fundingRate-{YYYY-MM}.zip` |
| Months | 2021-01 → 2026-08 inclusive (match OHLCV seal window) |
| Storage | `raw/{SYMBOL}/{SYMBOL}-fundingRate-{YYYY-MM}.zip` + `.sha256` sidecars |
| Provenance | `provenance/SHA256SUMS.txt`, `provenance/DOWNLOAD_MANIFEST.md` |

## Timestamp semantics (from source map)

| Field | Meaning | Use at decision t |
|-------|---------|-------------------|
| `calc_time` | Settlement / calculation event time (epoch **ms** UTC) | Knowable only if `settlement_ts ≤ t` |
| `funding_interval_hours` | Interval length (historically 8h; can vary) | Metadata; do not invent mid-interval accrued rate for SIGNAL |
| `last_funding_rate` | Rate applied at that settlement | Feature value after settlement |

**Forbidden for SIGNAL:** `premiumIndex` predicted / next-interval rate before settlement.

## CSV schema (Vision peek)

`calc_time,funding_interval_hours,last_funding_rate`


## Inventory [V Archivist]

| Symbol | Monthly zips | First | Last | Missing | Zip bytes |
|--------|--------------|-------|------|---------|-----------|
| BTCUSDT | 68 | 2021-01 | 2026-08 | 0 | 60,996 |
| ETHUSDT | 68 | 2021-01 | 2026-08 | 0 | 61,336 |

- SHA256SUMS lines: **136**; sidecars 68×2 [V]
- Sampled unzip -t + sidecar recompute: PASS [V]
- Source: Binance Vision monthly fundingRate UM
- `derived/`: empty
- Completion: FULL

## Access gates

| Path | Access |
|------|--------|
| raw/ | immutable provenance; awaiting Clock |
| derived/ | empty until approved transforms |
| Examiner | HOLD until Clock DATA VERDICT |

## Status history

1. FETCH_IN_PROGRESS
2. PENDING_CLOCK (fetch COMPLETE 2026-09-11T04:20:34Z; awaiting Clock)
3. **CONDITIONAL** ← current (2026-09-11T04:39:57Z) — Clock APPROVED_WITH_LIMITATIONS; Examiner CLEARED for Catalyst edges after Conductor route

## Notes for Clock

- Settlement-only rule; interval-hour regime changes must be catalogued
- Join to DATA-PROV-001 5m closes with inclusive completed-bar rule
- Volume ≪ 1 MB — not multi-GB
- fapi geo-blocked on fetch host; Vision-only path [V]

## Clock DATA VERDICT
- **Verdict:** CONDITIONAL
- **Quality:** APPROVED_WITH_LIMITATIONS
- **Issued:** 2026-09-11T04:39:57Z
- **Full verdict:** `/workspace/lab/data/DATA-PROV-FUNDING-001/provenance/DATA_VERDICT_DATA-PROV-FUNDING-001.md`
- **Archive audit:** `archive/audit/2026-09-11-Clock-DATA-VERDICT-DATA-PROV-FUNDING-001.md`
