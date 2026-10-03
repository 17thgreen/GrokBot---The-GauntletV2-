# DATA-PROV-PM-004 — REPORT

**fetched_at_utc:** 2026-09-13T18:48:36Z
**finished_at_utc:** 2026-09-13T19:06:59Z
**partial:** False
**stop_reason:** complete

## Scope

- Kalshi 15m BTC/ETH (`KXBTC15M`/`KXETH15M`), `open_time > 2026-09-11T20:15Z`
- Resolved only (369). Skipped still-open + closed_unsettled.
- Public `GET /markets/candlesticks` batch. No Trade API key. No CF. No trades.
- Checkpoints: `[840, 600, 300, 60, 0]` (T-14m … T-0)

## Candle fetch counts

| metric | N |
|---|---|
| universe_resolved | 369 |
| contracts_attempted | 369 |
| http_ok | 369 |
| ge1_intra | 369 |
| checkpoint_rows | 1845 |
| remainder_not_attempted | 0 |
| n_429 | 25 |
| n_batches | 11 |
| n_resumed | 0 |

### by_asset

```json
{
  "BTC": {
    "n_attempted": 184,
    "n_http_ok": 184,
    "n_ge1_intra": 184,
    "hit_rate_ge1_intra": 1.0,
    "mean_intra_points": 15.0,
    "mean_checkpoints_hit": 5.0
  },
  "ETH": {
    "n_attempted": 185,
    "n_http_ok": 185,
    "n_ge1_intra": 185,
    "hit_rate_ge1_intra": 1.0,
    "mean_intra_points": 15.0,
    "mean_checkpoints_hit": 5.0
  }
}
```

### checkpoint_hit_table

```json
[
  {
    "time_remaining_sec": 840,
    "attempted": 369,
    "hit": 369,
    "hit_rate": 1.0
  },
  {
    "time_remaining_sec": 600,
    "attempted": 369,
    "hit": 369,
    "hit_rate": 1.0
  },
  {
    "time_remaining_sec": 300,
    "attempted": 369,
    "hit": 369,
    "hit_rate": 1.0
  },
  {
    "time_remaining_sec": 60,
    "attempted": 369,
    "hit": 369,
    "hit_rate": 1.0
  },
  {
    "time_remaining_sec": 0,
    "attempted": 369,
    "hit": 369,
    "hit_rate": 1.0
  }
]
```

## Paths

- `derived/checkpoints.ndjson`
- `derived/contract_coverage.ndjson`
- `raw/kalshi_candles/`
- `raw/kalshi_batch/`
- `provenance/FETCH_SUMMARY.json`
- `provenance/progress.jsonl`
- `provenance/resolved_universe.ndjson`

## Not done

- No Clock-clear, no Examiner, no CF ticks, no strategy scoring, no trades.

