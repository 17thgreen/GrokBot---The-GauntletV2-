# REPORT — DATA-PROV-PM-002 decision-time checkpoint m_t

**Date (UTC):** 2026-09-11  
**Parent:** DATA-PROV-PM-001 (Clock CONDITIONAL; labels only; books/mids ABSENT)  
**Auth:** public APIs only — **no keys** `[V]`  
**Trades:** 0 `[V]`  
**Examiner numbers:** none invented. Counts only.

---

## 0. Verdict for Track B next bottleneck

**Intra-window reconstruction is FEASIBLE on both co-primary venues.**  
This is **not** a terminal-only BLOCKER. Do **not** use PM-001 `LAST_PRICE_DOLLARS` / `OUTCOME_PRICES` as \(m_t\) — those remain forbidden (Clock). This dataset attaches **new** public candlestick / prices-history observations inside `[OPEN, CLOSE]`.

Clock verdict on PM-002: **not issued** (PENDING_CLOCK). This report does not claim Examiner clearance.

---

## 1. Prototype (20 Kalshi + 20 Polymarket) `[V]`

| Venue | Attempted | HTTP OK | ≥1 intra-window price | Hit rate | Mean intra points | Checkpoint rows |
|-------|----------:|--------:|----------------------:|---------:|------------------:|----------------:|
| Kalshi 15m | 20 | 18 | 18 | 0.90 | 13.5 | 90 |
| Polymarket Global 5m+15m | 20 | 20 | 20 | 1.00 | 10.0 | 90 |

Kalshi's 2 proto misses were **HTTP 429** after 8 retries, **not** empty history. Recovered later (see §3).

Both endpoints return **intra-window** series:

- Kalshi `GET /series/{series}/markets/{ticker}/candlesticks?period_interval=1` → typically **15** one-minute candles with `yes_bid` / `yes_ask` / `price` OHLC in dollars.
- Polymarket `GET https://clob.polymarket.com/prices-history?market={yes_token}&startTs&endTs&fidelity=1` → typically **5** (5m) or **15** (15m) last-price points `{t,p}`.

---

## 2. Bounded extend (not all 3824)

Stride sample of PM-001: **120 Kalshi** (60 BTC + 60 ETH 15m) + **120 Polymarket** (30 × BTC/ETH × 5m/15m) = **240 contracts**.

After 429 retry of 4 Kalshi tickers (3s pacing; all 200 + 15 candles):

| Venue | Attempted | ≥1 intra-window | Hit rate | Checkpoint rows |
|-------|----------:|----------------:|---------:|----------------:|
| Kalshi | 120 | **120** | **1.00** | 600 (5 / contract) |
| Polymarket Global | 120 | **120** | **1.00** | 540 (4 on 5m, 5 on 15m) |
| **Combined** | **240** | **240** | **1.00** | **1140** |

Strata (all ge1 = attempted):

| Stratum | n |
|---------|--:|
| KALSHI\|BTC\|15m | 60 |
| KALSHI\|ETH\|15m | 60 |
| POLYMARKET_GLOBAL\|BTC\|5m | 30 |
| POLYMARKET_GLOBAL\|ETH\|5m | 30 |
| POLYMARKET_GLOBAL\|BTC\|15m | 30 |
| POLYMARKET_GLOBAL\|ETH\|15m | 30 |

---

## 3. Which checkpoints are possible

Declared remaining-time grid (seconds before CLOSE). Exact OPEN (T−15m / T−5m remaining 900 / 300 on the nose) has **no closed 1m candle** — first Kalshi candle ends at OPEN+60s ⇒ **T−14m (840s)** / **T−4m (240s)**. Not invented.

| Checkpoint | 15m | 5m | Kalshi hit | Poly hit | Notes |
|------------|-----|----|-----------:|---------:|-------|
| T−14m (840s) | yes | — | 120/120 | 60/60 | First closed minute. Kalshi **mid** on all 120. |
| T−10m (600s) | yes | — | 120/120 | 60/60 | Kalshi mid 120/120. |
| T−5m (300s) | yes | 15m only | 120/120 | 60/60 | Kalshi mid 120/120; 15/120 Kalshi already near 0/1. |
| T−4m (240s) | — | yes | — | 60/60 | 5m first closed-ish minute. |
| T−3m (180s) | — | yes | — | 60/60 | |
| T−1m (60s) | yes | yes | 120/120 | 120/120 | Kalshi 84/120 near 0/1; 22 fall back to last (bid=0). |
| T−0 / CLOSE | yes | yes | 120/120 | 120/120 | Trade cutoff. Kalshi **120/120 near 0/1**. Often economically resolved. |

Poly last-print lag vs declared `decision_time`: mean ~43s, max 52s, **0** with lag >60s `[V]`. `yes_bid` / `yes_ask` = **null `[U]`** on all 540 Poly rows (endpoint does not return a book).

`implied_p` construction (explicit, not Examiner-scored):

- Kalshi: mid = (yes_bid.close + yes_ask.close)/2 **only if** both > 0 and bid ≤ ask; else last. After merge: **506 mid + 94 last**.
- Poly: `implied_p` = last print `p`. Bid/ask `[U]`.
- Never copied from PM-001 `LAST_PRICE_DOLLARS` or `OUTCOME_PRICES`.
- Post-CLOSE prints dropped (Poly can emit t > CLOSE; those are not \(m_t\)).

---

## 4. Blockers (honest)

| ID | Status | Impact |
|----|--------|--------|
| **Hard: APIs only return terminal prices** | **NOT OBSERVED** on this live-tier slice | Intra-window path exists `[V]` |
| B1 Kalshi 429 | **SOFT** `[V]` | 4/120 first-pass misses; recovered with pacing. Bulk-all-3824 will need slower client or batch-by-day (batch endpoint 10k-candle cap). |
| B2 T−15m / T−5m exact OPEN | **PARTIAL** `[V]` | No closed 1m candle at OPEN. Use T−14m / T−4m or accept missing. Do not back-fill from prior contract. |
| B3 T−0 degeneracy | **QUALITY** `[V]` | Kalshi CLOSE candle is intra-window but 120/120 near 0/1. Not a fake of settlement last-price field — still a poor forecast checkpoint. Prefer T−14m / T−10m / T−5m for market-relative Examiner. |
| B4 Poly bid/ask | **ABSENT `[U]`** | prices-history is last only. Not a book. |
| B5 Historical books | **Still ABSENT** | Candle bid/ask **close** ≠ L2 book archive. Clock PM-001 books ABSENT stands. |
| B6 Independent oracle | **Still UNTESTED** | Out of scope here. |
| B7 Pre-cutoff Kalshi (`/historical/…`) | **UNTESTED on this slice** | PM-001 sample is post ~2026-07-13 cutoff; live candlestick route used. Dual-route coded but not exercised. |
| B8 Full 3824 | **NOT FETCHED** | Bounded 240 by design. No evidence the other 3584 lack history; also no claim they have it. |
| B9 Archivist IDs | Provisional `PROV-*` still | Same as PM-001. |

**Not a blocker:** public auth. No keys used.

---

## 5. Schema (checkpoint row)

`derived/checkpoints.ndjson` — one row per contract × hit checkpoint.

Required: `contract_id`, `venue`, `decision_time`, `time_remaining_sec`, `yes_bid`, `yes_ask`, `last`, `implied_p`, `source_endpoint`.  
Missing → JSON `null` (`[U]`). Extra honesty fields: `implied_p_method`, `obs_time`, `obs_lag_sec`, `asset`, `window`, `http`.

`derived/contract_coverage.ndjson` — one row per attempted contract (hit-rate source).

---

## 6. Layout

```
/workspace/lab/data/DATA-PROV-PM-002/
  raw/kalshi_candles/{ticker}.json     # wrapped meta+payload
  raw/poly_prices/{slug}.json
  derived/checkpoints.ndjson           # 1140
  derived/contract_coverage.ndjson     # 240
  provenance/fetch_pm002.py
  provenance/FETCH_SUMMARY.json
  provenance/PHASE1_PROTOTYPE.json
  REPORT.md · README.md · MANIFEST.json · CHECKSUMS.sha256
```

Pointer: `/workspace/lab/data/DATA-PROV-PM-001/derived/checkpoints/README.md` → this dataset (PM-001 stay label-only).

---

## 7. Non-goals / forbidden

- No trading / no orders.
- No Examiner Brier/logloss/Δ invented.
- No pooling Kalshi with Poly as one market.
- No treating this slice as sealed holdout.
- No claiming independent CF BRTI / Chainlink TWAP replay.

*End REPORT DATA-PROV-PM-002 — 2026-09-11.*
