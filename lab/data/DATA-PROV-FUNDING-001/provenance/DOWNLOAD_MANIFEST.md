# DATA-PROV-FUNDING-001 — Download Manifest

## Identity
- **Dataset ID:** DATA-PROV-FUNDING-001
- **Venue:** Binance USD-M perpetual futures (UM)
- **Instruments:** BTCUSDT, ETHUSDT
- **Dataset:** monthly `fundingRate` archives (settled funding prints)
- **Target range:** months **2021-01 → 2026-08** inclusive (align to OHLCV seal 2021-01-01 → 2026-08-31)
- **Completion:** FULL — 0 missing, 0 FAIL

## Source
- **Provider:** Binance Vision (`data.binance.vision`)
- **URL pattern:**
  `https://data.binance.vision/data/futures/um/monthly/fundingRate/{SYMBOL}/{SYMBOL}-fundingRate-{YYYY-MM}.zip`
- **Example:**
  `https://data.binance.vision/data/futures/um/monthly/fundingRate/BTCUSDT/BTCUSDT-fundingRate-2021-01.zip`
- **Not used:** fapi REST (`/fapi/v1/fundingRate`) — geo-blocked on this host (HTTP 451 / eligibility). Vision-only per Logan authorization 2026-09-11.

## Storage (immutable raw)
- Path: `raw/{SYMBOL}/{SYMBOL}-fundingRate-{YYYY-MM}.zip`
- Sidecar: `raw/{SYMBOL}/{SYMBOL}-fundingRate-{YYYY-MM}.zip.sha256` (hex digest only)
- Tree manifest: `provenance/SHA256SUMS.txt` (`<sha256>  raw/{SYMBOL}/...`)
- Zips not extracted into `raw/`; `derived/` empty

## Field schema (CSV inside each ZIP)
| Column | Meaning |
|--------|---------|
| `calc_time` | Settlement / calculation event time, **milliseconds since Unix epoch (UTC)** |
| `funding_interval_hours` | Interval length hours (historically 8; can vary) |
| `last_funding_rate` | Rate applied at that settlement |

Timestamp semantics: settlement knowable only if `calc_time ≤ t`; predicted/`premiumIndex` rates forbidden for SIGNAL until settlement. Cite: `DATA_PROV_CATALYST_SOURCES_2026-09-11.md` §1.

## Download window (UTC)
- Session start: **2026-09-11T04:20:25Z**
- Session complete: **2026-09-11T04:20:34Z**
- Concurrency: 8; retries: 4; validation: ZIP magic (`PK\x03\x04`) + `unzip -t`

## Inventory (facts)
| Symbol | Monthly zips | First month | Last month | Missing | Total zip bytes |
|--------|--------------|-------------|------------|---------|-----------------|
| BTCUSDT | 68 | 2021-01 | 2026-08 | **0** | 60,996 |
| ETHUSDT | 68 | 2021-01 | 2026-08 | **0** | 61,336 |

- Expected months in range: **68** per symbol (2021-01 … 2026-08).
- SHA256: **136** sidecars + **136** lines in `provenance/SHA256SUMS.txt`
- `provenance/missing.txt`: empty (0 Vision 404s; 0 unrecovered failures)
- Log: ok=135 skip=1 (pre-smoke 2021-01 BTC) miss404=0 fail=0 retries=0

## Integrity checks [V]
- All 136 zips present; ZIP magic + sampled `unzip -t` PASS
- Sidecar sha256 recompute PASS for all files
- No invented months; Vision-only

## Non-actions
- No liquidation history fetched
- No fapi calls
- No paid vendor

## Authorized by
Logan 2026-09-11 — provisional free Vision FUNDING + OI (no paid LIQ).
