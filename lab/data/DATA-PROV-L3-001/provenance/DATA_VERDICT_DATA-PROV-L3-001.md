# DATA VERDICT — DATA-PROV-L3-001
**Issued by:** The Clock  
**Issued UTC:** 2026-09-12T00:15:15Z  
**Audit:** `/workspace/lab/data/DATA-PROV-L3-001/provenance/CLOCK_AUDIT_REPORT.json`

---

## DATA VERDICT: CONDITIONAL

**QUALITY_STATUS:** APPROVED_WITH_LIMITATIONS  
**Layer:** **L3 external predictor only**  
**NOT** CF BRTI / ETHUSDRTI · **NOT** Kalshi settlement oracle · **NOT** F2  
**F2:** remains **DATA-BLOCKED** (`ORACLE_RECON_CF_BRTI_2026-09-12.md`)

Integrity PASS [V]. Sep-11 Vision 404 → www.binance.com kline fill documented. Usable for CLEARED F1 uses only under the join rule below.

---

## DATA MANIFEST

| Field | Value |
|-------|-------|
| DATASET_ID | DATA-PROV-L3-001 |
| SOURCE | Binance Vision spot daily 1m zips (2026-09-04→10) + www.binance.com `/api/v3/klines` fill (2026-09-11; Vision 404; api.binance.com 451) [V] |
| VENUE | Binance **spot** (not USD-M perps) |
| INSTRUMENT | BTCUSDT, ETHUSDT |
| START | 2026-09-04T00:00:00Z |
| END | 2026-09-11T23:59:00Z |
| FREQUENCY | 1m |
| TIMESTAMP_DEFINITION | `open_time_ms` bar open; `close_time_ms` = open+59999 (Vision µs truncated `//1000`) [V] |
| KNOWN_LATENCY | Receipt-time [U]; exchange candle clock only |
| KNOWN_GAPS | 0 [V] |
| TRANSFORMATIONS | Vision µs→ms; concat API day; dtype casts; layer/label stamped |
| QUALITY_STATUS | APPROVED_WITH_LIMITATIONS |
| ROWS | 11520 × 2 [V] |

---

## HARD TESTS [V] — all PASS

HASH 20/20 · contiguity 11520×2 gaps=0 · schema close=open+59999 · Sep-10/11 boundary contiguous · Vision µs//1000 OK · OHLC sanity · NOT_oracle labels · freeze ≠ DATA-PROV-001 holdout extension · PM-003 join matched 3020/3020.

---

## KNOWABILITY — exact join to PM-003 decision_time

```
knowable_bar = argmax { bar ∈ L3 | bar.close_time_ms <= decision_time_ms }
price_at_t   = knowable_bar.close
```

On this PM-003 slice every `decision_time` lands on `:00.000Z` (3020/3020), so equivalently:

```
knowable_bar.open_time_ms = decision_time_ms - 60_000
```

(`<` vs `<=` identical here; **recommend `<=`**.)

**LOOKAHEAD / BLOCKED:** using the bar with `open_time_ms == floor_minute(decision_time)` **close** — that close is not knowable until `close_time_ms`.

---

## CLEARED F1 uses

| Use ID | Status | Rule |
|--------|--------|------|
| `F1_price_at_t_completed_1m_close` | **CLEARED** | Completed-bar close via join above; L3 external predictor only; asset-matched BTC/ETH spot |
| `F1_RV_sigma_trailing_completed_1m` | **CLEARED** | Trailing σ/RV over completed 1m bars with `close_time_ms <= decision_time_ms` (window length must be pre-registered; no look-ahead bars) |

Both CLEARED uses remain **L3** — not settlement truth, not CF BRTI.

---

## BLOCKED

| Item | Status |
|------|--------|
| Incomplete-bar close at bar open / Rule B close | **BLOCKED** (LOOKAHEAD) |
| Binance as F2 / Kalshi settlement oracle / CF BRTI substitute | **BLOCKED** |
| F2 independent CF oracle replay | **DATA-BLOCKED** (unchanged) |
| Extending DATA-PROV-001 sealed holdout with this window | **BLOCKED** |
| Examiner F1 scores invented by Clock | **FORBIDDEN** |
| UM perps under this DATA_ID | **NOT IN LABEL** |

---

## USABLE COVERAGE FREEZE

| Field | Value |
|-------|-------|
| Window | **2026-09-04T00:00:00Z → 2026-09-11T23:59:00Z** only |
| Symbols | BTCUSDT + ETHUSDT spot 1m |
| Intended join target | DATA-PROV-PM-003 Kalshi decision_times (and same-rule joins if Conductor routes) |
| Not | DATA-PROV-001 holdout extension (001 ends 2026-08-31) |

Detail: `/workspace/lab/data/DATA-PROV-L3-001/provenance/USABLE_COVERAGE_DATA-PROV-L3-001.md`

---

## Sep-11 provenance caveat (CONDITIONAL driver)

Vision daily zip for 2026-09-11 was **HTTP 404** at fetch; filled via `www.binance.com/api/v3/klines` (same schema after unit align). Pure-Vision re-fetch when published is optional remediation — not a quarantine trigger given boundary continuity [V].

---

## Examiner gate

F1 measurement may use **CLEARED** completed-bar price-at-t / trailing RV-σ only after Conductor routes. F2 remains blocked. Do not score Binance vs Kalshi settlement as oracle recon under this DATA_ID.
