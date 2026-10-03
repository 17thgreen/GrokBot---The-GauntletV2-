# INVENTORY — DATA-PROV-PM-007

**DATA_ID:** DATA-PROV-PM-007  
**Verdict:** **GETTABLE**  
**Derived_at_utc:** 2026-09-13T21:01:44Z  
**Trade:** FORBIDDEN

## Layout

```
/workspace/lab/data/DATA-PROV-PM-007/
  SPEC.md
  INVENTORY.md
  GITHUB_HUNT.md
  FETCH_SUMMARY.md
  derived/
    checkpoints.ndjson          # rem=180 mid rows only
    contract_coverage.ndjson    # per-contract rem=180 status
  raw/
    kalshi_live_probe/          # live official API probe payloads (HTTP evidence)
  provenance/
    FETCH_SUMMARY.json
    live_probes.json
    extract_pm007.py
```

**Candle bytes reused (not copied):**  
`/workspace/lab/data/DATA-PROV-PM-003/raw/kalshi_candles/` (1208 tickers, official Kalshi, HTTP 200 in meta).

## Counts vs PM-003

| Metric | N |
|--------|--:|
| PM-003 BTC windows | 604 |
| PM-003 ETH windows | 604 |
| PM-007 BTC rem=180 mid | **604** |
| PM-007 ETH rem=180 mid | **604** |
| Checkpoint rows | 1208 |
| Missing vs PM-003 pair keys | 0 |
| Extra vs PM-003 | 0 |
| Coverage mid_ok | 1208 / 1208 |

## Mid rule (enforced)

- Emit row only when `yes_bid.close_dollars > 0` AND `yes_ask.close_dollars > 0` AND `bid <= ask`
- `implied_p = round((bid+ask)/2, 6)`, `implied_p_method = "mid"`
- `last` retained on row for audit only — **never** used as mid
- No invented OPEN / no copy of PM-001 terminals

## Checkpoint schema (derived)

Same family as PM-003 plus `open_time` / `close_time` for explicit pairing:

`contract_id, venue, venue_native_id, asset, window, open_time, close_time, decision_time, time_remaining_sec=180, yes_bid, yes_ask, last, implied_p, implied_p_method, obs_time, obs_lag_sec, source_endpoint, http, volume_fp, open_interest_fp, parent_dataset=DATA-PROV-PM-003, source_raw, fetched_at_utc, derived_at_utc`

## HTTP evidence (live probes)

See `provenance/live_probes.json` and `raw/kalshi_live_probe/`.

| Ticker | HTTP | rem180 | mid |
|--------|-----:|:------:|----:|
| `KXETH15M-26SEP111630-30` | 429 | — | — |
| `KXBTC15M-26SEP111630-30` | 429 | — | — |
| `KXBTC15M-26SEP041700-00` | 200 | yes | 0.575 |
| `KXETH15M-26SEP041700-00` | 200 | yes | 0.185 |

PM-003 per-ticker raw meta also records **HTTP 200** for all 1208 candlestick fetches used as primary source.

## Status flags

- Not Feature / Not Examiner / No `p_t` / No READY / No Clock-clear in this label
