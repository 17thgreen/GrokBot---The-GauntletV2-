# REPORT — DATA-PROV-PM-003 remaining Kalshi 15m checkpoints

**Date (UTC):** 2026-09-11  
**Parent:** DATA-PROV-PM-001  
**Sibling excluded:** DATA-PROV-PM-002 (VENUE_NATIVE_ID coverage) — not holdout  
**Auth:** public APIs only — **no keys**  
**Trades:** 0  
**Poly:** not fetched (deferred; Kalshi primary freeze path)  
**Examiner numbers:** none. Counts only.  
**Clock:** PENDING_CLOCK (do not Examiner until Clock)

---

## Universe

PM-001 Kalshi 15m BTC/ETH not in PM-002 coverage.

| | n |
|--|--:|
| Expected remaining | 1208 (604 BTC + 604 ETH) |
| Actual remaining listed | 1208 |
| Attempted this pass | **1208** |
| Remainder not attempted | **0** |

---

## Fetch counts

| Metric | Count |
|--------|------:|
| Attempted | 1208 |
| HTTP OK | 1208 |
| ≥1 intra-window | 1208 |
| Hit rate ≥1 intra | 1.0000 |
| Checkpoint rows | 6040 |
| HTTP 429 events (retried) | 62 |
| Batches | 37 |
| Resumed from prior raw | 52 |

### By asset

| Asset | Attempted | HTTP OK | ≥1 intra | Checkpoint rows (via 5/contract when full) |
|-------|----------:|--------:|---------:|------------------------------------------:|
| BTC | 604 | 604 | 604 | — |
| ETH | 604 | 604 | 604 | — |

Checkpoint hit table (attempted contracts × remaining-sec):

| time_remaining_sec | attempted | hit | hit_rate |
|-------------------:|----------:|----:|---------:|
| 840 | 1208 | 1208 | 1.0 |
| 600 | 1208 | 1208 | 1.0 |
| 300 | 1208 | 1208 | 1.0 |
| 60 | 1208 | 1208 | 1.0 |
| 0 | 1208 | 1208 | 1.0 |

---

## Construction (identical to PM-002 Kalshi)

- Endpoint: `GET /markets/candlesticks?market_tickers&start_ts&end_ts&period_interval=1` (batch ≤100; span-packed under 10k candle cap)
- Fallback/resume also accepts prior per-ticker single-market raw from early pacing attempts
- Checkpoints: T−14m / T−10m / T−5m / T−1m / T−0 (840 / 600 / 300 / 60 / 0)
- `implied_p` = mid if bid>0 and ask>0 and bid≤ask else last; missing = null
- Never invent OPEN; never copy PM-001 `LAST_PRICE_DOLLARS` / `OUTCOME_PRICES`; drop post-CLOSE

---

## Blockers

| ID | Status | Notes |
|----|--------|-------|
| B1 Kalshi 429 | SOFT | 62 events; all contracts recovered via retry + batch cool-down |
| B2 Batch 10k candle cap | HANDLED | Pack so n_markets × span_minutes ≤ 9000 |
| B3 T−15m exact OPEN | PARTIAL | Same as PM-002 — use T−14m |
| B4 Poly | DEFERRED | Not fetched this label |
| B5 Full remainder | COMPLETE | 0 not attempted |

**Not a blocker:** public auth. No keys used. No trading.

---

## Layout

```
/workspace/lab/data/DATA-PROV-PM-003/
  raw/kalshi_candles/{ticker}.json
  raw/kalshi_batch/batch_*.json
  derived/checkpoints.ndjson          # 6040
  derived/contract_coverage.ndjson    # 1208
  provenance/fetch_pm003.py
  provenance/FETCH_SUMMARY.json
  provenance/remaining_universe.ndjson
  REPORT.md · CHECKSUMS.sha256
```

Archive stub: `/workspace/lab/archive/datasets/DATA-PROV-PM-003.md` — **STATUS PENDING_CLOCK**

---

## Non-goals / forbidden

- No trading / no orders
- No Examiner Brier/logloss/Δ
- No Poly fetch this pass
- No treating PM-002 as holdout; no research-union until ledger says RESEARCH
- No PM-001 terminals as m_t

*End REPORT DATA-PROV-PM-003 — 2026-09-11.*
