# CLOCK AUDIT REPORT — DATA-PROV-PM-003

**Audited at (UTC):** 2026-09-11T23:02:26.125965+00:00  
**Auditor:** `clock_audit_DATA-PROV-PM-003.py`  
**Parent:** DATA-PROV-PM-001  
**Sibling excluded:** DATA-PROV-PM-002 (not holdout)  
**Order:** `/workspace/lab/governance/CLOCK_REVIEW_DATA-PROV-PM-003.md`  
**Recommended verdict:** **CONDITIONAL**  
**overlap_count (PM-002 Kalshi):** `0`  

No alpha. No Examiner scores invented. No bid/ask invented. Poly not in scope.

## Executive verdict

**CONDITIONAL** — Kalshi mid m_t CLEARED at T-14m/T-10m/T-5m (exclude near-degenerate & last-fallback) on THIS 1208 remaining universe (overlap_with_PM002=0); BLOCKED: T-0 (1206/1208 near-deg), last-fallback, books, oracle, sealed holdout, union-with-PM-002-as-holdout, Poly (absent), rem=900 fabrication, PM-001 terminals as m_t. Same primary freeze pattern as PM-002 Kalshi.

## CLEARED vs BLOCKED matrix

| Cell | Status | Method | Notes |
|------|--------|--------|-------|
| `KALSHI|15m|*|T-14m|mid` | **CLEARED** | mid | n=1208. Exclude near-degenerate rows (implied_p<=0.02 or >=0.98): 0/1208 mid rows; Exclude last-fallback companions at this remaining (expect 0 on primary rem) |
| `KALSHI|15m|*|T-10m|mid` | **CLEARED** | mid | n=1208. Exclude near-degenerate rows (implied_p<=0.02 or >=0.98): 0/1208 mid rows; Exclude last-fallback companions at this remaining (expect 0 on primary rem) |
| `KALSHI|15m|*|T-5m|mid` | **CLEARED** | mid | n=1208. Exclude near-degenerate rows (implied_p<=0.02 or >=0.98): 94/1208 mid rows; Exclude last-fallback companions at this remaining (expect 0 on primary rem) |
| `KALSHI|15m|*|T-1m|mid` | **CLEARED_WITH_STRONG_CAVEAT** | mid | n=1094. Elevated near-degeneracy: 697/1094; Companion last-fallback rows at T-1m must be excluded from mid claims (114 rows) |
| `KALSHI|15m|*|T-1m|last_fallback` | **BLOCKED** | last | Last-fallback contaminates mid-based m_t claims; use only if explicitly scoring last-print (weaker). |
| `KALSHI|15m|*|T-0|last_fallback` | **BLOCKED** | last | Last-fallback contaminates mid-based m_t claims; use only if explicitly scoring last-print (weaker). |
| `KALSHI|15m|*|T-0|any` | **BLOCKED** | any | 1206/1208 near-degenerate; 1 null implied_p. Exclude from forecast cells. |
| `*|*|*|*|books_L2` | **BLOCKED** | book | Not a book archive. Candle bid/ask close != L2. |
| `*|*|*|*|independent_oracle` | **BLOCKED** | oracle | Independent CF BRTI / Chainlink TWAP UNTESTED. No Binance substitution. |
| `SEALED_HOLDOUT` | **BLOCKED** |  | Not sealed. Remaining-universe slice only; not a holdout. |
| `UNION_PM002_PLUS_PM003_AS_HOLDOUT` | **BLOCKED** |  | Do not treat 1208+120 as sealed holdout or silent research-union until ledger says RESEARCH. |
| `POLYMARKET_ANY` | **BLOCKED** |  | Poly not fetched under DATA-PROV-PM-003. Out of scope. |
| `EXACT_OPEN_T15m_rem900` | **BLOCKED** |  | No closed 1m candle at exact OPEN. Do not fabricate rem=900. Use T-14m. |
| `PM001_LAST_PRICE_DOLLARS_AS_mt` | **BLOCKED** |  | Terminal settlement fields forbidden as decision-time m_t (Clock PM-001). |
| `KALSHI_PRECUTOFF_HISTORICAL` | **BLOCKED_QUARANTINE** |  | Historical /historical/... route UNTESTED on this slice (all opens post-cutoff / live). |
| `FULL_PM001_1328_UNDER_THIS_LABEL` | **BLOCKED** |  | This label freezes the 1208 remaining only; PM-002 120 is a sibling slice, not silently included. |

### Method distinction (hard)

- **mid-based m_t** = (yes_bid + yes_ask)/2 with bid>0, ask>0, bid<=ask — Kalshi candle close only.
- **last-print-only** = last trade/print price — Kalshi last-fallback rows only on this label.
- These are **different methods**. Do not mix last-fallback into mid cells.

## Construction deltas vs PM-002 Kalshi

- PM-002 Kalshi used per-ticker GET /series/{series}/markets/{ticker}/candlesticks. PM-003 primary path uses batch GET /markets/candlesticks?market_tickers=... (span-packed under 10k candle cap); per-ticker raw also present via resume/fallback. Candle OHLC field semantics and end_period_ts alignment match PM-002.
- PM-002 Kalshi T-0 was 120/120 near-deg (rate=1.0). PM-003 T-0 is 1206/1208 near-deg (rate=0.9983) with 1 null implied_p. T-5m near-deg 94/1208 (PM-002: 15/120). T-14m/T-10m still 0 near-deg — same primary freeze.
- Method mix: mid=5330 last=709 null=1 (PM-002 Kalshi was mid=506 last=94). Primary rem 840/600/300 remain mid-only.
- Endpoint: batch /markets/candlesticks primary (+ resume per-ticker raw); PM-002 was per-ticker series route only. Same OHLC / end_period_ts semantics.

## Test results

### 1. HASH_VERIFY / counts / strata — **PASS**

- CHECKSUMS.sha256 all match: `True` (1252 entries, 0 failures)
- checkpoints.ndjson rows=6040 expected=6040 sha_match=True
- SHA256 `90e38c2f23e224def13db05924f6470a1e738778882f6b0cc17ed708b3143765`
- contract_coverage.ndjson rows=1208 expected=1208
- Strata: `{'KALSHI|BTC|15m': 604, 'KALSHI|ETH|15m': 604}` match=True (BTC=604 ETH=604)

### 2. ZERO OVERLAP with PM-002 Kalshi — **PASS**

- PM-003 venue_native_id set size: **1208**
- PM-002 Kalshi venue_native_id set size: **120**
- venue_native_id intersection size: **0**
- PM-003 contract_id set size: **1208**
- PM-002 Kalshi contract_id set size: **120**
- contract_id intersection size: **0**
- overlap_count: **0** (required 0 for non-QUARANTINE)

### 3. subseteq PM-001 Kalshi; venue=KALSHI; window=15m — **PASS**

- Every PM-003 id subseteq PM-001 Kalshi: `True` (missing=0)
- Venues: `['KALSHI']` KALSHI-only=True
- Windows: `['15m']` 15m-only=True
- PM-002+PM-003 == PM-001 Kalshi 1328: `True` (120+1208 vs 1328)
- Poly absent: `True`

### 4. decision_time / lag / formula — **PASS**

- decision_time in [OPEN, CLOSE]: 6040/6040 (outside=0)
- obs_time == decision_time: 6040/6040
- obs_lag_sec == 0: 6040/6040
- decision_time == CLOSE - remaining: 6040/6040
- Knowability: A trader knows the candle's close values only at/after the minute end. Using end_period_ts as decision_time is decision-time-aligned for that closed bar — not lookahead into a future bar. At exact OPEN there is no closed 1m candle yet.

### 5. remaining set / 5 rows/contract / no rem=900 — **PASS**

- remaining set: `[0, 60, 300, 600, 840]` expected `[0, 60, 300, 600, 840]`
- counts: `{'0': 1208, '60': 1208, '300': 1208, '600': 1208, '840': 1208}`
- fabricated rem=900: 0
- rows/contract: `{'5': 1208}` all_5=True

### 6. implied_p_method / mid validity / last-fallback — **PASS**

- Method counts: `{'mid': 5330, 'last': 709, 'None': 1}` (mid=5330 last=709 null=1)
- mid_valid: 5330/5330
- mid by remaining: `{'0': 612, '60': 1094, '300': 1208, '600': 1208, '840': 1208}`
- last-fallback by remaining: `{'0': 595, '60': 114}` (T-1m=114, T-0=595)
- Note: mid requires bid>0, ask>0, bid<=ask; else last; if last also missing -> implied_p/method null (do not invent). Primary T-14m/T-10m/T-5m are mid-only on this slice.

### 7. Near-degeneracy T-0 / T-5m / T-14m / T-10m — **PASS**

- Near-deg by remaining: `{'0': {'n': 1208, 'near_0_or_1': 1206, 'implied_p_null': 1, 'rate': 0.9983}, '60': {'n': 1208, 'near_0_or_1': 811, 'implied_p_null': 0, 'rate': 0.6714}, '300': {'n': 1208, 'near_0_or_1': 94, 'implied_p_null': 0, 'rate': 0.0778}, '600': {'n': 1208, 'near_0_or_1': 0, 'implied_p_null': 0, 'rate': 0.0}, '840': {'n': 1208, 'near_0_or_1': 0, 'implied_p_null': 0, 'rate': 0.0}}`
- T-0 near-deg: **1206** rate=0.9983
- T-5m/T-10m/T-14m near-deg counts: 94 / 0 / 0
- Delta vs PM-002: PM-002 Kalshi T-0 was 120/120 near-deg (rate=1.0). PM-003 T-0 is 1206/1208 near-deg (rate=0.9983) with 1 null implied_p. T-5m near-deg 94/1208 (PM-002: 15/120). T-14m/T-10m still 0 near-deg — same primary freeze.
- Recommendation: EXCLUDE Kalshi T-0 (remaining=0) from forecast / market-relative Examiner cells. Prefer T-14m / T-10m / T-5m mid cells; T-1m has elevated near-degeneracy and last-fallback.

### 8. Not copied from PM-001 LAST_PRICE_DOLLARS — **PASS**

- Intra equal-to-LAST_PRICE_DOLLARS rate: **0.076** (367/4832)
- T-0 equal terminal: 1207 (economic near-resolution; not field copy)
- Raw Kalshi candle spot-check OK: `True` (n=8)
- Evidence: Intra-window implied_p/last differ from PM-001 LAST_PRICE_DOLLARS for majority of rows; raw candle spot-checks match checkpoint bid/ask/last; not a terminal-field copy.

### 9. Batch vs per-ticker candle semantics — **PASS**

- Batch files: 37; per-ticker raw: 1208
- Schema keys match PM-002 per-ticker: `True`
- Same-ticker batch vs per-ticker alignment: `{'aligned_end_period': True, 'end_period_ts': 1788565560, 'price_close_equal': True, 'yes_bid_close_equal': True, 'yes_ask_close_equal': True, 'volume_fp_equal': True, 'oi_fp_equal': True}`
- ckpt endpoints batch/per-ticker: 5895/145
- Semantics: Identical: candle close keyed by end_period_ts (unix sec at minute end). Batch and per-ticker payloads expose the same candlestick object shape (price/yes_bid/yes_ask OHLC dollars + volume_fp + open_interest_fp).
- Construction delta: PM-002 Kalshi used per-ticker GET /series/{series}/markets/{ticker}/candlesticks. PM-003 primary path uses batch GET /markets/candlesticks?market_tickers=... (span-packed under 10k candle cap); per-ticker raw also present via resume/fallback. Candle OHLC field semantics and end_period_ts alignment match PM-002.

### 10. Not books / oracle / sealed / union / Poly absent — **PASS**

- Books: NOT a book archive. Kalshi candle yes_bid/yes_ask close are 1m OHLC summaries, not L2 depth snapshots. PM-001 books ABSENT stands.
- Oracle: No independent CF BRTI / Chainlink TWAP replay attached. Settlement oracle remains VENUE_DECLARED from PM-001 labels only. Binance substitution forbidden. Status=**UNTESTED**
- Sealed holdout: `False` — ['REPORT: Sibling excluded DATA-PROV-PM-002 — not holdout', 'ORDER: Forbidden treating 1208+240 as sealed holdout', 'coverage rows=1208 remaining slice of PM-001 Kalshi 1328']
- Not union-with-PM-002-as-holdout: `True` (overlap_vni=0)
- Poly paths under PM-003: `[]`; venues=['KALSHI']
- Open span: 2026-09-04T20:45:00+00:00 -> 2026-09-11T20:15:00+00:00; pre-cutoff=0; historical_ep=0; live_ep=6040

### 11. Usable coverage freeze (THIS 1208 only) — **PASS**

Do **not** silently union with PM-002 or reuse full PM-001 windows. Freeze is this 1208-slice only:

| Stratum | n | open_min (UTC) | open_max (UTC) | ckpt rows | remaining_sec |
|---------|--:|----------------|----------------|----------:|---------------|
| `KALSHI|BTC|15m` | 604 | 2026-09-04T20:45:00+00:00 | 2026-09-11T20:15:00+00:00 | 3020 | [0, 60, 300, 600, 840] |
| `KALSHI|ETH|15m` | 604 | 2026-09-04T20:45:00+00:00 | 2026-09-11T20:15:00+00:00 | 3020 | [0, 60, 300, 600, 840] |

Explicit exclusions:
- Do not union with PM-002 Kalshi 120 as one holdout
- Do not reuse full PM-001 1328 windows as if all have m_t under this label
- Poly not fetched — out of freeze
- T-0 forecast cells blocked
- last-fallback rows excluded from mid cells
- near-degenerate mid rows excluded

### Extras (duplicates / post-CLOSE) — **PASS**

- Duplicate contract x remaining: 0
- Duplicate contract x decision_time: 0
- Post-CLOSE prints: 0
- Venues: ['KALSHI']

## Examiner gate

Market-relative Examiner may proceed **only** on CLEARED cells after Conductor freezes horizon/asset/offset/method.

- **CLEARED primary (same as PM-002 Kalshi):** mid at T-14m / T-10m / T-5m on **this 1208 only** — exclude near-degenerate; exclude last-fallback.
- **CLEARED_WITH_STRONG_CAVEAT:** T-1m mid (high near-deg; exclude last-fallback companions).
- **BLOCKED:** T-0 any; last-fallback for mid claims; books; independent oracle; sealed holdout; union PM-002+PM-003 as holdout; Poly; rem=900; PM-001 LAST_PRICE_DOLLARS as m_t; pre-cutoff historical claims.

*End CLOCK_AUDIT_REPORT DATA-PROV-PM-003.*
