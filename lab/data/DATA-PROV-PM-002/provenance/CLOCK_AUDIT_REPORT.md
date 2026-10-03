# CLOCK AUDIT REPORT — DATA-PROV-PM-002

**Audited at (UTC):** 2026-09-11T21:26:42.900998+00:00  
**Auditor:** `clock_audit_DATA-PROV-PM-002.py`  
**Parent:** DATA-PROV-PM-001  
**Order:** `/workspace/lab/governance/CLOCK_REVIEW_DATA-PROV-PM-002.md`  
**Recommended verdict:** **CONDITIONAL**  

No alpha. No Examiner scores invented. No bid/ask invented.

## Executive verdict

**CONDITIONAL** — Kalshi mid m_t CLEARED at T-14m/T-10m/T-5m (exclude near-degenerate & last-fallback); Poly last-only CLEARED as WEAKER last-print benchmark with lag caveat; BLOCKED: T-0 Kalshi forecast cells, Poly mid, books, oracle, full 3824, sealed holdout, unlabeled pool, pre-cutoff historical.

## CLEARED vs BLOCKED matrix

| Cell | Status | Method | Notes |
|------|--------|--------|-------|
| `KALSHI|15m|*|T-14m|mid` | **CLEARED** | mid | n=120. Exclude near-degenerate rows (implied_p<=0.02 or >=0.98): 0/120 mid rows; Candle close knowable at minute end (= decision_time) |
| `KALSHI|15m|*|T-10m|mid` | **CLEARED** | mid | n=120. Exclude near-degenerate rows (implied_p<=0.02 or >=0.98): 0/120 mid rows; Candle close knowable at minute end (= decision_time) |
| `KALSHI|15m|*|T-5m|mid` | **CLEARED** | mid | n=120. Exclude near-degenerate rows (implied_p<=0.02 or >=0.98): 15/120 mid rows; Candle close knowable at minute end (= decision_time) |
| `KALSHI|15m|*|T-1m|mid` | **CLEARED_WITH_STRONG_CAVEAT** | mid | n=98. Elevated near-degeneracy: 62/98; Companion last-fallback rows at T-1m must be excluded from mid claims (22 rows) |
| `POLYMARKET_GLOBAL|*|*|T-14m|last` | **CLEARED_WEAKER_LAST_PRINT** | last | n=60. bid/ask all null — NOT mid; cannot support mid-relative scoring; obs_lag_sec mean~43.557s max=52.0s — stale last vs decision_time |
| `POLYMARKET_GLOBAL|*|*|T-10m|last` | **CLEARED_WEAKER_LAST_PRINT** | last | n=60. bid/ask all null — NOT mid; cannot support mid-relative scoring; obs_lag_sec mean~43.557s max=52.0s — stale last vs decision_time |
| `POLYMARKET_GLOBAL|*|*|T-5m|last` | **CLEARED_WEAKER_LAST_PRINT** | last | n=60. bid/ask all null — NOT mid; cannot support mid-relative scoring; obs_lag_sec mean~43.557s max=52.0s — stale last vs decision_time |
| `POLYMARKET_GLOBAL|*|*|T-4m|last` | **CLEARED_WEAKER_LAST_PRINT** | last | n=60. bid/ask all null — NOT mid; cannot support mid-relative scoring; obs_lag_sec mean~43.557s max=52.0s — stale last vs decision_time |
| `POLYMARKET_GLOBAL|*|*|T-3m|last` | **CLEARED_WEAKER_LAST_PRINT** | last | n=60. bid/ask all null — NOT mid; cannot support mid-relative scoring; obs_lag_sec mean~43.557s max=52.0s — stale last vs decision_time |
| `POLYMARKET_GLOBAL|*|*|T-1m|last` | **CLEARED_WEAKER_LAST_PRINT** | last | n=120. bid/ask all null — NOT mid; cannot support mid-relative scoring; obs_lag_sec mean~43.557s max=52.0s — stale last vs decision_time |
| `KALSHI|15m|*|T-1m|last_fallback` | **BLOCKED** | last | Last-fallback contaminates mid-based m_t claims; use only if explicitly scoring last-print (weaker). |
| `KALSHI|15m|*|T-0|any` | **BLOCKED** | any | 120/120 near-degenerate (implied_p near 0/1). Exclude from forecast cells. |
| `POLYMARKET_GLOBAL|*|*|T-0|last` | **BLOCKED** | last | T-0 last-print often economically resolved; poor forecast checkpoint. Prefer earlier remaining. |
| `POLYMARKET_GLOBAL|*|*|*|mid` | **BLOCKED** | mid | Poly bid/ask all null; mid impossible without inventing quotes. |
| `*|*|*|*|books_L2` | **BLOCKED** | book | Not a book archive. Candle bid/ask close ≠ L2. |
| `*|*|*|*|independent_oracle` | **BLOCKED** | oracle | Independent CF BRTI / Chainlink TWAP UNTESTED. No Binance substitution. |
| `FULL_3824` | **BLOCKED** |  | Only 240-contract bounded slice fetched. Do not treat as full parent. |
| `SEALED_HOLDOUT` | **BLOCKED** |  | Not sealed. Provisional PROV-* sample only. |
| `UNLABELED_VENUE_POOL` | **BLOCKED** |  | Never pool Kalshi with Polymarket as one market. |
| `KALSHI_PRECUTOFF_HISTORICAL` | **BLOCKED_QUARANTINE** |  | Historical /historical/... route UNTESTED on this slice. Quarantine older coverage claims. |
| `EXACT_OPEN_T15m_T5m` | **BLOCKED** |  | No closed 1m candle at exact OPEN. Do not fabricate rem=900 / 5m-rem=300. Use T-14m/T-4m. |
| `PM001_LAST_PRICE_OR_OUTCOME_PRICES_AS_mt` | **BLOCKED** |  | Terminal settlement fields forbidden as decision-time m_t (Clock PM-001). |

### Method distinction (hard)

- **mid-based m_t** = (yes_bid + yes_ask)/2 with bid>0, ask>0, bid≤ask — Kalshi candle close only.
- **last-print-only** = last trade/print price — Poly entire surface; Kalshi last-fallback rows.
- These are **different methods**. Do not score Poly last as if it were mid. Do not mix last-fallback into mid cells.

## Test results (12 Conductor questions + extras)

### 1. HASH_VERIFY / counts / strata — **PASS**

- CHECKSUMS.sha256 all match: `True` (253 entries, 0 failures)
- checkpoints.ndjson rows=1140 expected=1140 sha_match=True
- SHA256 `affbbbd0b07c765d3f7c0af5e6b23564d3973ec82f27fe7d48b84bc4ded89dc0`
- contract_coverage.ndjson rows=240 expected=240
- Strata: `{'KALSHI|BTC|15m': 60, 'KALSHI|ETH|15m': 60, 'POLYMARKET_GLOBAL|BTC|15m': 30, 'POLYMARKET_GLOBAL|BTC|5m': 30, 'POLYMARKET_GLOBAL|ETH|15m': 30, 'POLYMARKET_GLOBAL|ETH|5m': 30}` match=True
- Venue ckpt counts: `{'KALSHI': 600, 'POLYMARKET_GLOBAL': 540}`

### 2. Join integrity — **PASS**

- Every PM-002 contract_id ⊆ PM-001: `True` (missing=0)
- venue/asset/window mismatches: 0/0/0
- decision_time ∈ [OPEN, CLOSE]: 1140/1140 (outside=0)
- coverage OPEN/CLOSE match parent: 240/240

### 3. NO copy from PM-001 LAST_PRICE / OUTCOME_PRICES — **PASS**

- Kalshi intra equal-to-LAST_PRICE_DOLLARS rate: **0.0854** (41/480)
- Kalshi T-0 equal terminal: 120 (economic near-resolution; not field copy)
- Poly intra equal-to-OUTCOME_PRICES[0] rate: **0.0**
- Raw Kalshi candle spot-check OK: `True` (n=8)
- Raw Poly history spot-check OK: `True` (n=8)
- Evidence: checkpoint bid/ask/last match raw candle/history payloads; intra-window values are not the terminal-only pattern.

### 4. Kalshi timestamp semantics — **PASS**

- obs_time == decision_time: 600/600
- obs_lag_sec == 0: 600/600
- decision_time == CLOSE − remaining: 600/600
- Knowability: A trader knows the candle's close values only at/after the minute end. Using end_period_ts as decision_time is therefore decision-time-aligned for that closed bar — not lookahead into a future bar. At exact OPEN there is no closed 1m candle yet.

### 5. Poly timestamp / lag — **PASS**

- lag_sec: n=540 min=20.0 median=45.0 mean=43.557 p90=47.0 max=52.0 n_gt_60=0
- Report claim mean~43s consistent: `True`
- obs_time after decision_time: 0
- Knowability: Last-print is knowable at obs_time; at decision_time the trader would have seen that print if they observed the CLOB stream continuously up to decision_time. Lag means m_t is a stale last, not a contemporaneous mid. Mean lag ~43s as claimed.

### 6. implied_p_method / mid validity / last fallback — **PASS**

- Method counts: `{'KALSHI|last': 94, 'KALSHI|mid': 506, 'POLYMARKET_GLOBAL|last': 540}`
- Kalshi mid=506 last=94; mid_valid=506; claim 506/94 match=`True`
- Kalshi last-fallback by remaining: `{'0': 72, '60': 22}` (T-1m=22)
- Poly all last-only: `True`; bid_null=540 ask_null=540

### 7. T-0 Kalshi degeneracy — **PASS**

- Kalshi T-0 rows: 120; near-degenerate (≤0.02 or ≥0.98): **120**
- Near-deg by remaining: `{'0': {'n': 120, 'near_0_or_1': 120, 'rate': 1.0}, '60': {'n': 120, 'near_0_or_1': 84, 'rate': 0.7}, '300': {'n': 120, 'near_0_or_1': 15, 'rate': 0.125}, '600': {'n': 120, 'near_0_or_1': 0, 'rate': 0.0}, '840': {'n': 120, 'near_0_or_1': 0, 'rate': 0.0}}`
- Recommendation: EXCLUDE Kalshi T-0 (remaining=0) from forecast / market-relative Examiner cells. Prefer T-14m / T-10m / T-5m mid cells; T-1m has elevated near-degeneracy and last-fallback.

### 8. Exact OPEN missing / no fabricated 900/300 — **PASS**

- remaining counts: `{'0': 240, '60': 240, '180': 60, '240': 60, '300': 180, '600': 180, '840': 180}`
- Kalshi rem=900 fabricated: 0; rem=840 T-14m: 120
- Poly 5m rem=300 exact OPEN: 0; rem=240 T-4m: 60
- Note: Exact OPEN (T-15m rem=900 / T-5m rem=300 for 5m windows) has no closed 1m candle. Dataset correctly uses T-14m (840) and T-4m (240). rem=300 on Kalshi 15m is T-5m mid-window, not exact OPEN.

### 9. Not a book archive — **PASS**

- NOT a book archive. Poly bid/ask all null [U]. Kalshi candle yes_bid/yes_ask close are 1m OHLC summaries, not L2 depth snapshots. PM-001 books ABSENT stands.

### 10. No independent oracle — **PASS**

- No independent CF BRTI / Chainlink TWAP replay attached. Settlement oracle remains VENUE_DECLARED from PM-001 labels only. Independent-oracle UNTESTED stands; Binance substitution forbidden.
- Status: **UNTESTED**

### 11. Pre-cutoff historical route — **PASS**

- Kalshi open span: 2026-09-04T23:30:00+00:00 → 2026-09-11T20:30:00+00:00 (cutoff 2026-07-13T00:00:00+00:00)
- Pre-cutoff contracts: 0; historical-routed raw: 0; live endpoints: 600
- All PM-002 Kalshi rows are post-cutoff / live candlestick route. Historical /historical/... route remains UNTESTED → quarantine any claim of older (pre-~2026-07-13) Kalshi candle coverage. Dual-route code exists in fetch_pm002.py but was not exercised on this slice.

### 12. Not full 3824 / not sealed holdout — **PASS**

- n_contracts=240 parent_n=3824 is_full_3824=False is_sealed_holdout=False
- MANIFEST NOTES: Bounded slice — not all 3824
- README: Not sealed. PENDING_CLOCK
- REPORT B8: Full 3824 NOT FETCHED
- coverage rows=240 << 3824

### Extras (duplicates / uniqueness / post-CLOSE / non-pooling) — **PASS**

- Duplicate contract×remaining: 0
- Duplicate contract×decision_time: 0
- Post-CLOSE prints: 0
- Venues: ['KALSHI', 'POLYMARKET_GLOBAL']; non-pooling OK: `True`

## Usable coverage freeze (240 only)

Do **not** silently reuse full PM-001 label windows. Freeze is this 240-slice only:

| Stratum | n | open_min (UTC) | open_max (UTC) | ckpt rows | remaining_sec |
|---------|--:|----------------|----------------|----------:|---------------|
| `KALSHI|BTC|15m` | 60 | 2026-09-04T23:30:00+00:00 | 2026-09-11T20:30:00+00:00 | 300 | [0, 60, 300, 600, 840] |
| `KALSHI|ETH|15m` | 60 | 2026-09-04T23:30:00+00:00 | 2026-09-11T20:30:00+00:00 | 300 | [0, 60, 300, 600, 840] |
| `POLYMARKET_GLOBAL|BTC|5m` | 30 | 2026-09-08T17:05:00+00:00 | 2026-09-11T20:35:00+00:00 | 120 | [0, 60, 180, 240] |
| `POLYMARKET_GLOBAL|ETH|5m` | 30 | 2026-09-08T17:15:00+00:00 | 2026-09-11T20:35:00+00:00 | 120 | [0, 60, 180, 240] |
| `POLYMARKET_GLOBAL|BTC|15m` | 30 | 2026-09-08T17:00:00+00:00 | 2026-09-11T20:15:00+00:00 | 150 | [0, 60, 300, 600, 840] |
| `POLYMARKET_GLOBAL|ETH|15m` | 30 | 2026-09-08T17:00:00+00:00 | 2026-09-11T20:15:00+00:00 | 150 | [0, 60, 300, 600, 840] |

## Examiner gate

PM-001 market-relative Examiner remains **BLOCKED** except for the CLEARED cells above, which must be frozen (horizon, asset, decision offset, method) before Examiner runs.

- CLEARED primary: Kalshi **mid** at T-14m / T-10m / T-5m (exclude near-degenerate; exclude last-fallback rows).
- CLEARED weaker: Poly **last-print** at non-T-0 checkpoints with lag caveat — not mid-relative.
- Still BLOCKED: T-0 Kalshi; Poly mid; books; independent oracle; full 3824; sealed holdout; unlabeled venue pool; PM-001 terminal prices as m_t.

*End CLOCK_AUDIT_REPORT DATA-PROV-PM-002.*
