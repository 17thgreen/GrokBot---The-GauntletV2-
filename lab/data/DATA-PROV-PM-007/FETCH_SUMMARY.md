# FETCH_SUMMARY — DATA-PROV-PM-007

**DATA_ID:** DATA-PROV-PM-007  
**Wave:** WAVE_008 / W2-D  
**Cell:** rem=180 (T-3m) Kalshi 15m mid  
**Verdict:** **GETTABLE**  
**Derived_at_utc:** 2026-09-13T21:01:44Z  
**Pair_to:** DATA-PROV-PM-003  
**Trade:** FORBIDDEN · **Not Feature · Not Examiner · No p_t · No READY**

## Method

1. GitHub/HF hunt for Sep 4–11 Kalshi rem=180 dumps → **miss** (see `GITHUB_HUNT.md`).
2. Re-extract rem=180 from DATA-PROV-PM-003 official Kalshi 1m candlesticks (`end_period_ts == CLOSE_TIME_unix - 180`).
3. Mid-only gate (no last-as-mid).
4. Live public API probes for HTTP evidence.

Machine-readable twin: `provenance/FETCH_SUMMARY.json`.

## Counts

| Metric | N |
|--------|--:|
| Universe (PM-003 window) | 1208 |
| BTC rem=180 mid rows | **604** |
| ETH rem=180 mid rows | **604** |
| Coverage vs PM-003 | **604/604 BTC · 604/604 ETH** (100%) |
| Missing pair keys | 0 |

### by_asset

```json
{
  "BTC": {
    "n_attempted": 604,
    "n_http_ok": 604,
    "n_candle_rem180": 604,
    "n_mid_ok": 604
  },
  "ETH": {
    "n_attempted": 604,
    "n_http_ok": 604,
    "n_candle_rem180": 604,
    "n_mid_ok": 604
  }
}
```

## Live HTTP evidence

```json
{
  "n_probes": 4,
  "n_http_200": 2,
  "n_http_429": 2,
  "n_rem180_confirmed": 2
}
```

Confirmed rem=180 + mid on live `GET .../candlesticks?period_interval=1`:

- `KXBTC15M-26SEP041700-00` → HTTP **200**, rem180 present, mid=0.575
- `KXETH15M-26SEP041700-00` → HTTP **200**, rem180 present, mid=0.185

Additional probes returned HTTP **429** (`too_many_requests`) — soft rate-limit evidence; not a data hole (PM-003 raw already complete).

## Paths

- `derived/checkpoints.ndjson`
- `derived/contract_coverage.ndjson`
- `raw/kalshi_live_probe/`
- `provenance/FETCH_SUMMARY.json`
- `provenance/live_probes.json`
- `provenance/extract_pm007.py`
- Source candles: `/workspace/lab/data/DATA-PROV-PM-003/raw/kalshi_candles/`

## Not done (out of scope)

Clock join · Cartographer · Feature · Examiner · Poly · trades.

*End FETCH_SUMMARY DATA-PROV-PM-007.*
