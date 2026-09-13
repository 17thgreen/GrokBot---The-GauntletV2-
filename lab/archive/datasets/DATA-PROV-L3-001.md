# DATA-PROV-L3-001

- **DATA_ID:** DATA-PROV-L3-001
- **NAME:** Binance spot 1m BTCUSDT+ETHUSDT L3 price-at-t (PM-003 window 2026-09-04→11)
- **STATUS:** **CONDITIONAL**
- **Registered:** 2026-09-12 UTC (Feature Wave 001 · JOB B)
- **Path:** `/workspace/lab/data/DATA-PROV-L3-001/`
- **Report:** `/workspace/lab/data/DATA-PROV-L3-001/REPORT.md`
- **Role:** **Layer-3 external predictor only** — knowable exchange price-at-t for F1 structural features
- **NOT:** settlement oracle · CF BRTI / ETHUSDRTI · substitute for independent L2 replay
- **NOT a substitute for:** DATA-PROV-001 (ends 2026-08-31; different market/interval/window)
- **Auth:** Public Vision + www.binance.com klines — **no API keys**
- **Market:** Binance **spot** 1m (UM Vision available but not used this label)
- **Coverage:** BTCUSDT + ETHUSDT · 11520 bars each · 2026-09-04T00:00Z → 2026-09-11T23:59Z · 0 gaps
- **Sep-11 note:** Vision daily zip 404 at fetch → API fill (documented in REPORT)

## Access gates

| Path | Access |
|------|--------|
| raw/ | immutable public Vision zips + Sep-11 API JSON |
| derived/ | provisional L3 1m parquet/ndjson; **CONDITIONAL** (Clock) |
| Examiner | **F1 CLEARED uses only** after Conductor route; F2 blocked |
| Trading | **Forbidden** |
| Use as Kalshi oracle | **Forbidden** |

## Clock DATA VERDICT

- **Verdict:** CONDITIONAL — issued 2026-09-12T00:15:15Z
- **CLEARED:** `F1_price_at_t_completed_1m_close` · `F1_RV_sigma_trailing_completed_1m` (join: close_time_ms <= decision_time_ms)
- **BLOCKED:** incomplete-bar close; Binance as oracle/F2/CF BRTI; DATA-PROV-001 holdout extension
- **Full:** `/workspace/lab/data/DATA-PROV-L3-001/provenance/DATA_VERDICT_DATA-PROV-L3-001.md`

## Related

- Feature Wave: `/workspace/lab/governance/FEATURE_WAVE_001_2026-09-12.md` (F1 needs L3; F2 blocked on CF)
- Oracle recon (F2): `/workspace/lab/governance/ORACLE_RECON_CF_BRTI_2026-09-12.md` · **BLOCKED**
- Arena checkpoints: DATA-PROV-PM-003

## Clock join note — W2-E strike × L3 (2026-09-13T19:23:35Z)

- **Join verdict:** CONDITIONAL (join only) for DRAFT-FEAT-20260913-002
- **Coverage:** BTC T-5m 569/569 · ETH T-5m 545/545 (K+S_t)
- **Rule:** FLOOR_STRIKE + L3 completed close ≤ t (lag ≤90s); L3 NOT oracle
- **Full:** `/workspace/lab/data/DATA-PROV-L3-001/provenance/DATA_VERDICT_W2E_STRIKE_L3_JOIN.md`
