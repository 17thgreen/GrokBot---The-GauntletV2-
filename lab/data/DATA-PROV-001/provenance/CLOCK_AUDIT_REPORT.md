# CLOCK AUDIT REPORT — DATA-PROV-001

- Audited UTC: `2026-09-10T23:30:39.551349+00:00`
- Overall pass: **True**
- JSON: `/workspace/lab/data/DATA-PROV-001/provenance/CLOCK_AUDIT_REPORT.json`

## Confirmed timestamp definition
- open_time_ms: candle start (open time) from Binance fapi klines API, UTC epoch milliseconds
- close_time_ms: candle close time from API; expected open_time_ms + 299999 for 5m bars

## Known limitations
- API primary fapi.binance.com returned HTTP 451 (restricted location); fallback www.binance.com/fapi/v1/klines used (same path/schema).
- No receipt-time / local ingest timestamp recorded — only exchange open_time_ms / close_time_ms.
- Provisional reference clock: exchange candle clock only; no cross-venue clock comparison (single venue).
- Sealed holdout OHLC integrity not re-checked in this audit (policy); hash+times+counts only.

## Hard tests

| Test | BTC | ETH | Pass |
|------|-----|-----|------|
| HASH_VERIFY | True | True | True |
| DUPLICATES | True | True | True |
| MISSINGNESS | True | True | True |
| IMPOSSIBLE_SEQUENCING | True | True | True |
| LOOKAHEAD_LATE_INFORMATION | True | True | True |
| SPLIT_SEALING | True | True | True |
| SAMPLE_ADEQUACY | True | True | True |
| MISALIGNMENT | within=True | within=True; BTC==ETH=True | True |
| CROSS_VENUE_CLOCK_ERROR | n/a single venue | BTC/ETH identical=True | True |

## Exact counts (both symbols)

### BTCUSDT
- raw=595872, warmup=624, research=357148, validation=119049, holdout=119051
- HASH_VERIFY pass=True
  - raw: match=True sha256=799f379f8a3d3228179b5a17987cbd31a2195b5fc545784a1f0d857b7593a713
  - research: match=True sha256=29d8a016723a3ae880f79a176f4c19a8f7695843ea9792b87be79204d34485a5
  - validation: match=True sha256=3397049626801bd1f550ff092050076076f444a0dcc8da5fdf4864286c6aa5aa
  - warmup: match=True sha256=75b6d45f85da2aeddb8b12486d95e498ced44a608e74282fb65067a820b19a3b
  - holdout: match=True sha256=e858531c4a6b5282232ca3cec3b313041a27cb648c40f3cb8223426cb274c835
- DUPLICATES: raw_dup=0, sorted_raw=True
- MISSINGNESS raw: missing=0, off_epoch_grid=0, close_plus_299999=True, close_mismatch=0
- IMPOSSIBLE_SEQUENCING raw total_violation_events=0
- OUTLIERS (R+V diagnostic): count=16 (|log(c/o)|>0.05), fraction=3.35995396863063e-05
- SAMPLE_ADEQUACY: span_days=2068.9965, warmup_meets_min=True
- sealed times only: rows=119051, min=2025-07-14T15:05:00+00:00, max=2026-08-31T23:55:00+00:00

### ETHUSDT
- raw=595872, warmup=624, research=357148, validation=119049, holdout=119051
- HASH_VERIFY pass=True
  - raw: match=True sha256=d7781563e7665adce5db69cda3ea7b650daee3acdbf3c0814b062248ed9e8cf2
  - research: match=True sha256=96bcc1680589d2221c378d1cf498b0963186b534e596ce7ccfd6002503082c29
  - validation: match=True sha256=8590b4872eb2364ffe57ad60dc07a880c5db103f1d762108eaa790ebb8ceb4d7
  - warmup: match=True sha256=fd1bd1c71496b1770daa854c60ddc0ab878e6aacf1de5ac0859864b33de88c93
  - holdout: match=True sha256=d95005724ef1071152139ac64aaba816ec3598f214c9361f1a08e74defb438be
- DUPLICATES: raw_dup=0, sorted_raw=True
- MISSINGNESS raw: missing=0, off_epoch_grid=0, close_plus_299999=True, close_mismatch=0
- IMPOSSIBLE_SEQUENCING raw total_violation_events=0
- OUTLIERS (R+V diagnostic): count=32 (|log(c/o)|>0.05), fraction=6.71990793726126e-05
- SAMPLE_ADEQUACY: span_days=2068.9965, warmup_meets_min=True
- sealed times only: rows=119051, min=2025-07-14T15:05:00+00:00, max=2026-08-31T23:55:00+00:00

## LOOKAHEAD rule
Bar t close is only knowable at close_time_ms (exchange event). A feature that uses bar t close for a decision at open_time_ms of bar t is LOOKAHEAD. EDGE-001-style trailing RV/quantile using only completed bars through t is OK IF the decision is at close of t (after close_time_ms).
- derived/ empty: True

## CONDITIONAL / QUARANTINE
- CONDITIONAL: BTCUSDT: 16 RESEARCH+VALIDATION bars with |log(close/open)| > 0.05 (diagnostic; not hard fail)
- CONDITIONAL: ETHUSDT: 32 RESEARCH+VALIDATION bars with |log(close/open)| > 0.05 (diagnostic; not hard fail)
- CONDITIONAL: CROSS-VENUE: N/A single venue; API 451 fallback to www.binance.com — document as known limitation
- QUARANTINE: none

## Policy notes
- Sealed holdout prices were not printed or used for research.
- No strategy PnL computed.
