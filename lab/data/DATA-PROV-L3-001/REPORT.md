# REPORT — DATA-PROV-L3-001 Binance spot 1m L3 price-at-t (PM-003 window)

**Date (UTC):** 2026-09-12  
**DATA_ID:** DATA-PROV-L3-001  
**Wave:** Feature Wave 001 · JOB B (F1 measurement support)  
**Auth:** public only — **no keys**  
**Trades:** 0  
**Examiner numbers:** none  
**Clock:** **PENDING_CLOCK** (do not Examiner until Clock)  

---

## Label (binding)

| Field | Value |
|-------|-------|
| Layer | **L3** external predictor |
| Role | `price-at-t` for F1 structural features (oracle-distance / time / vol) |
| **NOT** | Kalshi settlement oracle |
| **NOT** | CF Benchmarks BRTI / ETHUSDRTI substitute |
| **NOT** | Independent L2 oracle replay |
| Forbidden features | PM-001 `EXPIRATION_VALUE` / terminal last as decision-time input |

Binance is **not** treated as the Kalshi settlement oracle. Settlement remains CF BRTI / ETHUSDRTI (see `ORACLE_RECON_CF_BRTI_2026-09-12.md` — F2 BLOCKED).

---

## Market declared

| Choice | Value |
|--------|-------|
| Market | **Binance spot** (`data/spot/daily/klines`) |
| Why | UTC minute `open_time` aligns cleanly to Kalshi `decision_time` checkpoints; spot is closer in kind to CF RTI inputs than USD-M perps |
| Alternatives checked | UM futures Vision daily zips also HTTP 200 for 2026-09-04→10 — **not** stored this label |
| Interval | **1m** |
| Symbols | BTCUSDT, ETHUSDT |

---

## Coverage

| Symbol | Rows | First open UTC | Last open UTC | Gaps (Δ≠60s) | Complete |
|--------|-----:|----------------|---------------|-------------:|:--------:|
| BTCUSDT | 11520 | 2026-09-04T00:00:00Z | 2026-09-11T23:59:00Z | 0 | YES |
| ETHUSDT | 11520 | 2026-09-04T00:00:00Z | 2026-09-11T23:59:00Z | 0 | YES |

Expected = 8 × 1440 = 11520 per symbol. Covers PM-003 opens **2026-09-04→11** (DATA-PROV-001 OHLCV ends 2026-08-31 and does **not** cover this window).

---

## Sources

| Days | Source | Auth |
|------|--------|------|
| 2026-09-04 … 2026-09-10 | Binance Vision daily zip `…/spot/daily/klines/{SYM}/1m/{SYM}-1m-{date}.zip` | none |
| 2026-09-11 | Vision daily zip **HTTP 404** at fetch (not yet published) → fill via `https://www.binance.com/api/v3/klines` | none |
| — | `api.binance.com` / `fapi.binance.com` | HTTP **451** from this host (same pattern as DATA-PROV-001) |

**Timestamp note:** Vision CSV times are **microseconds**; API fill is **milliseconds**. Derived files truncate Vision µs→ms (`//1000`). See `provenance/VISION_TIMESTAMP_NOTE.md`.

---

## Layout

```
/workspace/lab/data/DATA-PROV-L3-001/
  raw/vision_spot_1m/*.zip          # 14 zips (2 sym × 7 days)
  raw/api_fill_sep11/*.json         # 2 JSON kline arrays (Sep 11)
  derived/{SYM}_1m_spot_2026-09-04_2026-09-11.parquet
  derived/{SYM}_1m_spot_2026-09-04_2026-09-11.ndjson
  provenance/fetch_l3_vision.py
  provenance/download_log.txt
  provenance/VISION_TIMESTAMP_NOTE.md
  MANIFEST.json
  CHECKSUMS.sha256
  REPORT.md
```

Each derived row carries `layer=L3` and `label=external_predictor_NOT_oracle_NOT_CF_BRTI`.

---

## Integrity

- SHA256 of raw + derived listed in `CHECKSUMS.sha256`
- Contiguity audit: 0 missing minutes both symbols `[V]`
- No secrets; no purchase; no trading

---

## Blockers / caveats

| ID | Status | Notes |
|----|--------|-------|
| L3-B1 Vision Sep-11 lag | HANDLED | API fill same calendar day; re-fetch Vision zip when published for pure-Vision provenance if Clock requires |
| L3-B2 Host 451 on api.binance.com | HANDLED | www.binance.com public path used (documented) |
| L3-B3 Not CF oracle | BY DESIGN | F2 remains BLOCKED; do not promote L3 → L2 |
| L3-B4 Knowability | PENDING_CLOCK | Close knowable at `close_time_ms`; open-at-decision uses prior completed bar — Clock to confirm |

---

## Knowability sketch (for Clock — not a verdict)

- At decision time \(t\), safe L3 inputs are bars with `close_time_ms < t` (completed).
- Same-bar close at bar-open decision = unsafe (same limitation class as DATA-PROV-001).
- Align to PM-003 checkpoints by `open_time_ms` / `close_time_ms` on the 1m grid.

---

## Non-goals confirmed

- No Examiner scores  
- No trading  
- No PM-001 `expiration_value` as feature  
- No Binance-as-Kalshi-oracle claim  

*End REPORT DATA-PROV-L3-001 — JOB B.*
