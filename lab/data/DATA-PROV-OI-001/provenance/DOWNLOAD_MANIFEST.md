# DATA-PROV-OI-001 — Download Manifest

## Identity
- **Dataset ID:** DATA-PROV-OI-001
- **Venue:** Binance USD-M perpetual futures (UM)
- **Instruments:** BTCUSDT, ETHUSDT
- **Dataset:** daily `metrics` archives (5m open interest + ratios)
- **BTC target range:** 2021-01-01 → 2026-08-31 UTC (inclusive) — match OHLCV seal
- **ETH target range:** 2021-12-01 → 2026-08-31 UTC (inclusive) — Vision earliest for ETHUSDT metrics
- **Completion:** FULL within documented ranges — 0 unexpected missing days, 0 FAIL

## Source
- **Provider:** Binance Vision (`data.binance.vision`)
- **URL pattern:**
  `https://data.binance.vision/data/futures/um/daily/metrics/{SYMBOL}/{SYMBOL}-metrics-{YYYY-MM-DD}.zip`
- **Example:**
  `https://data.binance.vision/data/futures/um/daily/metrics/BTCUSDT/BTCUSDT-metrics-2021-01-01.zip`
- **Not used:** fapi REST (`/futures/data/openInterestHist` etc.) — geo-blocked on this host; ~30d retention anyway. Vision-only per Logan authorization 2026-09-11.
- **Not fetched:** liquidation history (explicitly out of scope)

## Storage (immutable raw)
- Path: `raw/{SYMBOL}/{SYMBOL}-metrics-{YYYY-MM-DD}.zip`
- Sidecar: `raw/{SYMBOL}/{SYMBOL}-metrics-{YYYY-MM-DD}.zip.sha256` (hex digest only)
- Tree manifest: `provenance/SHA256SUMS.txt` (`<sha256>  raw/{SYMBOL}/...`)
- Zips not extracted into `raw/`; `derived/` empty

## Field schema (CSV inside each ZIP)
| Column | Meaning |
|--------|---------|
| `create_time` | Snapshot / observation time `YYYY-MM-DD HH:MM:SS` at **5-minute** steps (UTC) |
| `symbol` | Instrument |
| `sum_open_interest` | Open interest (contracts / base qty) |
| `sum_open_interest_value` | Open interest notional |
| `count_toptrader_long_short_ratio` | Top-trader count L/S ratio (not required for EDGE-004/006 SIGNAL unless registered) |
| `sum_toptrader_long_short_ratio` | Top-trader sum L/S ratio |
| `count_long_short_ratio` | Global count L/S ratio |
| `sum_taker_long_short_vol_ratio` | Taker L/S volume ratio |

Timestamp semantics: OI knowable iff `create_time ≤ t`; level (not sum); midnight partition may double-write — take latest-by-timestamp per bucket. Cite: `DATA_PROV_CATALYST_SOURCES_2026-09-11.md` §2.

## Download window (UTC)
- Session start: **2026-09-11T04:20:25Z**
- Session complete: **2026-09-11T04:23:20Z**
- Concurrency: 12 workers; retries: 4 with backoff; validation: ZIP magic (`PK\x03\x04`) + `unzip -t`

## Inventory (facts)
| Symbol | Daily zips | First | Last | Missing in range | Total zip bytes |
|--------|------------|-------|------|------------------|-----------------|
| BTCUSDT | 2069 | 2021-01-01 | 2026-08-31 | **0** | 23,861,538 (~22.76 MiB) |
| ETHUSDT | 1735 | 2021-12-01 | 2026-08-31 | **0** | 20,459,807 (~19.51 MiB) |

- Expected BTC calendar days: **2069**
- Expected ETH calendar days: **1735**
- Combined zip bytes: **44,321,345** (~42.3 MiB) — tens of MB, not multi-GB
- SHA256: **3804** sidecars + **3804** lines in `provenance/SHA256SUMS.txt`
- `provenance/missing_days.txt`: empty (0 Vision 404s in requested ranges; 0 unrecovered failures)
- Log: ok=3804 skip=0 miss404=0 fail=0 retries=0

## ETH intentional gap vs OHLCV seal (NOT missing-in-range)
- DATA-PROV-001 OHLCV seal: 2021-01-01 → 2026-08-31
- ETH Vision metrics earliest: **2021-12-01** (HEAD of 2021-11-30 = 404; confirmed)
- **334 days** 2021-01-01 → 2021-11-30: **not fetched, not invented**
- Zero ETH files dated before 2021-12-01 on disk
- Joint BTC+ETH OI/OHLCV seal for edges starts ≥ 2021-12-01; abstain where ETH OI absent

## Integrity checks [V]
- Calendar completeness PASS for both symbols in their documented ranges
- Sampled ZIP magic + `unzip -t` + sidecar recompute PASS (endpoint + mid + last each symbol)
- Schema header matches source-map peek
- No extras outside requested ranges

## Non-actions
- No liquidation history fetched
- No fapi calls
- No paid vendor
- No invented ETH pre-2021-12 days

## Authorized by
Logan 2026-09-11 — provisional free Vision FUNDING + OI (no paid LIQ).
