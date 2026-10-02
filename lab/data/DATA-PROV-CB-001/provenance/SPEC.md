# DATA-PROV-CB-001 — Coinbase Exchange 1m candle tape (BTC-USD / ETH-USD)

**Class:** DATA inventory. Not a Feature. Not READY. Not Examiner.
**Trade:** FORBIDDEN. No orders. No invented quotes.
**Auth:** public Coinbase Exchange API only — **no key**.
**Stamp:** 2026-09-13

## Source

| Field | Value |
|-------|-------|
| Venue | Coinbase Exchange (public REST) |
| Endpoint | `GET https://api.exchange.coinbase.com/products/{PRODUCT}/candles` |
| Products | `BTC-USD`, `ETH-USD` |
| Granularity | `60` (1-minute bars) |
| User-Agent | required (`GrokLab-DATA-PROV-CB-001/1.0`) |
| Page size | max ~300 candles / request — page the window |
| Candle schema | `[time, low, high, open, close, volume]` — `time` = bar **start** unix seconds |

## Window

| Bound | ISO (UTC) |
|-------|-----------|
| Start | `2026-09-04T20:00:00Z` |
| End   | `2026-09-11T20:59:00Z` |

Inclusive 1m grid: bar starts from `2026-09-04T20:00:00Z` through `2026-09-11T20:59:00Z` (expected ~10140 bars / product if dense).

## Join target (inventory only)

Upstream: **DATA-PROV-PM-003** Clock-cleared Kalshi 15m checkpoints
(`/workspace/lab/data/DATA-PROV-PM-003/derived/checkpoints.ndjson`).

Fields used: `decision_time`, `asset` (BTC→BTC-USD, ETH→ETH-USD), `time_remaining_sec` / rem labels (T-14m / T-10m / T-5m / T-1m / T-0), `implied_p` as Kalshi mid `m_t`.

### Completed-bar policy (fail-closed)

- Coinbase bar `[t_start, t_start+60)` is **completed** only when `t_start + 60 <= decision_time`.
- Attach last completed close at or before `decision_time`, plus prior 1m close, plus simple return  
  `v_CB,t = (close_t - close_{t-1m}) / close_{t-1m}`.
- Incomplete current minute = **missing**. Do not use partial-minute close.
- Do **not** fill gaps with Binance, CF/BRTI, or invented prints.
- Velocity is knowable at `t` only when both completed bars exist.

## Kernel note (NOT scored tonight)

Incumbent is Kalshi mid `m_t`. Candidate velocity is Coinbase 1m simple return at the same `decision_time`. Not Binance last. Not F1 strike distance. No `p_t`. No Examiner packet.

## Layout

```
DATA-PROV-CB-001/
  provenance/SPEC.md
  provenance/GITHUB_HUNT.md
  provenance/INVENTORY.md
  provenance/FETCH_SUMMARY.json
  raw/BTC-USD_1m.csv  (or parquet)
  raw/ETH-USD_1m.csv
  derived/pm003_cb_join.ndjson
```

## GitHub hunt

As-needed first hunt for missing tapes: search GitHub (repos + code) for hosted Coinbase 1m dumps covering this window. Distinguish **hosted bytes** vs **scrapers**. A GitHub hit does **not** Clock-clear. Official Exchange API fetch still required when working. See `GITHUB_HUNT.md`.
