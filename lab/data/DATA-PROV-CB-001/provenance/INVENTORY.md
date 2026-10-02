# DATA-PROV-CB-001 — Inventory

**Class:** DATA inventory. Not a Feature. Not READY. Not Examiner.  
**Stamp:** 2026-09-13T20:45:29Z (fetch) / 2026-09-13 (join)  
**Trade:** FORBIDDEN  
**Auth:** public Coinbase Exchange API — no key. User-Agent: `GrokLab-DATA-PROV-CB-001/1.0`  
**Verdict for this window:** **GETTABLE**

## Source & window

| Field | Value |
|-------|-------|
| Endpoint | `GET https://api.exchange.coinbase.com/products/{BTC-USD\|ETH-USD}/candles?granularity=60&start=&end=` |
| Granularity | 60s (1m bars) |
| Window | `2026-09-04T20:00:00Z` → `2026-09-11T20:59:00Z` (inclusive bar starts) |
| Page size | ≤300 candles/request; 34 pages/product |
| Extra fetch | 1 prior bar (`19:59Z`) + trailing buffer for join velocity / edge |

## HTTP & raw tape

| Product | HTTP status counts | Requests | Bars in window | Expected | Missing in window | CSV rows (incl. buffers) | Path |
|---------|-------------------:|---------:|---------------:|---------:|------------------:|-------------------------:|------|
| BTC-USD | 200×34 | 34 | **10140** | 10140 | **0** | 10142 | `raw/BTC-USD_1m.csv` |
| ETH-USD | 200×34 | 34 | **10140** | 10140 | **0** | 10142 | `raw/ETH-USD_1m.csv` |

- Non-200 / 429 / auth blockers: **0** (no retries needed).  
- Holes in 1m grid inside window: **none**.  
- See `provenance/FETCH_SUMMARY.json`.

## GitHub hunt (as-needed first hunt)

See `provenance/GITHUB_HUNT.md`.

- Hosted dump covering this window: **NOT FOUND** (HF adjacent dump ends ~2025-12 — miss).  
- Scrapers/libs found: yes (cbhist, coinbase-advanced-py, etc.) — not substitute bytes.  
- Code search: HTTP 401 without auth; HTML search 429.  
- **Clock not cleared by GitHub.** Official API used as primary and succeeded → GETTABLE.

## Completed-bar policy (enforced)

- Coinbase `time` = bar **start**. Bar end = start + 60s.  
- Usable at `decision_time` iff `bar_end <= decision_time`.  
- Incomplete current minute = **missing** (not used).  
- `v_CB,t = (close_t - close_{t-1m}) / close_{t-1m}` only when both completed bars exist.  
- No Binance / CF / BRTI fill. No invented closes.

## Join to PM-003

Upstream: `/workspace/lab/data/DATA-PROV-PM-003/derived/checkpoints.ndjson` (Clock-cleared Kalshi 15m sheet).  
Join output: `derived/pm003_cb_join.ndjson` (6040 rows). Coverage JSON: `derived/pm003_cb_join_coverage.json`.

| Metric | Count |
|--------|------:|
| PM-003 rows | 6040 |
| With `decision_time` | 6040 |
| Join rows | 6040 |
| `cb_bar_end_iso == decision_time` (on-minute) | 6040 |
| Lookahead (`bar_end > decision_time`) | **0** |

### Coverage by asset

| Asset | N | close_ok | velocity_ok | close cov | velocity cov |
|-------|--:|---------:|------------:|----------:|-------------:|
| BTC | 3020 | 3020 | 3020 | 1.000 | 1.000 |
| ETH | 3020 | 3020 | 3020 | 1.000 | 1.000 |

### Coverage by asset × rem

| Asset | rem | N | close_ok | velocity_ok | missing_close | missing_prior |
|-------|-----|--:|---------:|------------:|--------------:|--------------:|
| BTC | T-14m | 604 | 604 | 604 | 0 | 0 |
| BTC | T-10m | 604 | 604 | 604 | 0 | 0 |
| BTC | T-5m | 604 | 604 | 604 | 0 | 0 |
| BTC | T-1m | 604 | 604 | 604 | 0 | 0 |
| BTC | T-0 | 604 | 604 | 604 | 0 | 0 |
| ETH | T-14m | 604 | 604 | 604 | 0 | 0 |
| ETH | T-10m | 604 | 604 | 604 | 0 | 0 |
| ETH | T-5m | 604 | 604 | 604 | 0 | 0 |
| ETH | T-1m | 604 | 604 | 604 | 0 | 0 |
| ETH | T-0 | 604 | 604 | 604 | 0 | 0 |

**Velocity knowable at t (completed bars only):** YES for all 6040 PM-003 decision rows in this join.

Kalshi mid side-note (incumbent, not CB): PM-003 `implied_p_method` on join rows = mid 5330 / last 709 / null 1. CB closes attached regardless; mid quality is upstream PM-003, not this tape.

## GETTABLE / PARTIAL / BLOCKED

| Label | Status | Reason |
|-------|--------|--------|
| Coinbase 1m BTC-USD window tape | **GETTABLE** | 10140/10140, HTTP 200 only |
| Coinbase 1m ETH-USD window tape | **GETTABLE** | 10140/10140, HTTP 200 only |
| PM-003 inventory join (close + prior + v_CB) | **GETTABLE** | 6040/6040 velocity_ok; 0 holes; completed-bar only |
| GitHub hosted dump substitute | NOT FOUND | scrapers only; does not block |

**Overall window verdict: GETTABLE.**

## Paths

```
/workspace/lab/data/DATA-PROV-CB-001/
  provenance/SPEC.md
  provenance/GITHUB_HUNT.md
  provenance/INVENTORY.md          ← this file
  provenance/FETCH_SUMMARY.json
  provenance/fetch_cb001.py
  provenance/join_pm003_cb.py
  raw/BTC-USD_1m.csv
  raw/ETH-USD_1m.csv
  derived/pm003_cb_join.ndjson
  derived/pm003_cb_join_coverage.json
```

No Examiner packet. No `p_t`. No READY. No trades.
