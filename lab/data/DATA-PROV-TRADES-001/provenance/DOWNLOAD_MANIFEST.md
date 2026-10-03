# DATA-PROV-TRADES-001 — Download Manifest

## Identity
- **Dataset ID:** DATA-PROV-TRADES-001
- **Venue:** Binance USD-M perpetual futures (UM)
- **Instruments:** BTCUSDT, ETHUSDT
- **Dataset:** daily `aggTrades` archives
- **Target range:** 2021-01-01 → 2026-08-31 UTC (inclusive)
- **Completion:** FULL — `STOPPED_TIER=NONE_FULL` (P1→P2→P3 all completed)

## Source
- **Provider:** Binance Vision (`data.binance.vision`)
- **URL pattern:**
  `https://data.binance.vision/data/futures/um/daily/aggTrades/{SYMBOL}/{SYMBOL}-aggTrades-YYYY-MM-DD.zip`
- **Example:**
  `https://data.binance.vision/data/futures/um/daily/aggTrades/BTCUSDT/BTCUSDT-aggTrades-2024-01-01.zip`

## Storage choice (immutable raw)
- Keep **official Vision daily ZIP** as immutable raw.
- Path: `raw/{SYMBOL}/YYYY-MM-DD.zip`
- Sidecar: `raw/{SYMBOL}/YYYY-MM-DD.zip.sha256` (hex digest only)
- Tree manifest: `provenance/SHA256SUMS.txt` (`<sha256>  raw/{SYMBOL}/YYYY-MM-DD.zip`)
- Zips are **not** extracted into `raw/` (hashed-friendly, space-efficient).
- `derived/` left empty (no transforms, no OHLCV merge, no backtests).

## Field schema (CSV inside each ZIP)
Vision CSV columns (header present on most files; **some days omit the header row** — observed e.g. `ETHUSDT/2021-01-01.zip`, `BTCUSDT/2022-06-15.zip`, `ETHUSDT/2022-06-15.zip`):

| Column | Meaning |
|--------|---------|
| `agg_trade_id` | Aggregate trade ID |
| `price` | Price |
| `quantity` | Quantity |
| `first_trade_id` | First trade ID in aggregate |
| `last_trade_id` | Last trade ID in aggregate |
| `transact_time` | Event time, **milliseconds since Unix epoch (UTC)** |
| `is_buyer_maker` | `true`/`false` |

Note: Vision uses `transact_time`, not `timestamp`.

## Download window (UTC)
- Session start (log): **2026-09-11T00:05:36Z**
- Pipeline fix + P1 restart: **2026-09-11T00:09:39Z**
- Session complete: **2026-09-11T00:42:02Z**
- Concurrency: 6; retries: 4 on transient errors; min free disk guard: 15 GB

## Inventory (facts)
| Symbol | Daily zips | Date first | Date last | Missing days | Total zip bytes |
|--------|------------|------------|-----------|--------------|-----------------|
| BTCUSDT | 2069 | 2021-01-01 | 2026-08-31 | **0** | 41,572,620,842 (~38.72 GiB) |
| ETHUSDT | 2069 | 2021-01-01 | 2026-08-31 | **0** | 40,519,215,191 (~37.74 GiB) |

- Expected calendar days in range: **2069** per symbol (no extras).
- SHA256: **4138** sidecars + **4138** lines in `provenance/SHA256SUMS.txt` (1:1 with zips; spot-checks matched).

## First / last timestamps (from endpoint day files)
| Symbol | Day | Data rows (that day) | First `transact_time` | Last `transact_time` |
|--------|-----|----------------------|-----------------------|----------------------|
| BTCUSDT | 2021-01-01 | 885,732 | 2021-01-01T00:00:00.001Z | 2021-01-01T23:59:59.660Z |
| BTCUSDT | 2026-08-31 | 1,353,859 | 2026-08-31T00:00:00.001Z | 2026-08-31T23:59:59.466Z |
| ETHUSDT | 2021-01-01 | 437,250 | 2021-01-01T00:00:00.004Z | 2021-01-01T23:59:59.697Z |
| ETHUSDT | 2026-08-31 | 1,250,468 | 2026-08-31T00:00:00.002Z | 2026-08-31T23:59:59.994Z |

### Additional sampled day row counts (not full history)
| Symbol | Day | Data rows | Header present |
|--------|-----|-----------|----------------|
| BTCUSDT | 2022-06-15 | 6,146,703 | False |
| BTCUSDT | 2024-01-01 | 761,222 | True |
| BTCUSDT | 2024-06-15 | 372,184 | True |
| ETHUSDT | 2022-06-15 | 5,317,519 | False |
| ETHUSDT | 2024-01-01 | 504,953 | True |
| ETHUSDT | 2024-06-15 | 681,756 | True |

Full per-day row inventory was **not** written (row-count job aborted at finalize). Endpoint + sample counts above are measured from zips; do not invent totals.

## Missing-day / FAIL reconciliation
- `provenance/missing_days.txt`: **no missing date rows** (0 Vision 404s; 0 unrecovered failures).
- `download_log.txt` contains **24 `FAIL` lines**, all `BTCUSDT` dates in **2024-01-01 … 2024-01-24** (subset).
- Cause: initial `dl_one.sh` validated downloads with the `file` binary, which is **not installed** on this box. HTTP 200 ZIP bodies were rejected → RETRY ×4 → FAIL, and partials deleted.
- Fix (2026-09-11T00:09:39Z): validate with ZIP magic (`PK\x03\x04`) + `unzip -t`; restart P1.
- After fix: **0 FAIL**, **0 MISS_404**. All 24 previously FAILed days are present as `raw/BTCUSDT/YYYY-MM-DD.zip` with SHA256 sidecars.
- **Do not treat the 24 FAIL log lines as missing data.**

## Priority tiers executed
1. P1 2024-01-01 → 2026-08-31 (both) — complete (974 days × 2)
2. P2 2022-01-01 → 2023-12-31 (both) — complete
3. P3 2021-01-01 → 2021-12-31 (both) — complete

## Disk (at session complete / finalize)
- At complete: ~36G free (leave ≥15G satisfied)
- Raw tree ~77G compressed zips
- No raw deletions after successful download (pre-fix failed attempts never landed final zips)

## Paths
```
/workspace/lab/data/DATA-PROV-TRADES-001/
  raw/BTCUSDT/YYYY-MM-DD.zip (+ .sha256)
  raw/ETHUSDT/YYYY-MM-DD.zip (+ .sha256)
  provenance/DOWNLOAD_MANIFEST.md
  provenance/download_log.txt
  provenance/missing_days.txt
  provenance/SHA256SUMS.txt
  provenance/dl_one.sh
  derived/   (empty)
```

## Non-goals (honored)
- No merge with OHLCV DATA-PROV-001
- No backtests
- No silent gap/dupe repair
- No invented trades or missing days
