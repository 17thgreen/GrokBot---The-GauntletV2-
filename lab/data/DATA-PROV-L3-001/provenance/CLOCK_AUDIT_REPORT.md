# CLOCK AUDIT REPORT — DATA-PROV-L3-001

- Audited UTC: `2026-09-12T00:14:37.670937+00:00`
- Auditor: `Clock`
- Order: `/workspace/lab/governance/CLOCK_REVIEW_DATA-PROV-L3-001.md`
- Recommended verdict: **CONDITIONAL**
- All integrity tests pass: **True**
- JSON: `/workspace/lab/data/DATA-PROV-L3-001/provenance/CLOCK_AUDIT_REPORT.json`

## Role (binding)

| Field | Value |
|-------|-------|
| Layer | **L3** external predictor |
| Market | Binance **spot** 1m BTCUSDT + ETHUSDT |
| Window | 2026-09-04T00:00Z → 2026-09-11T23:59Z (11520 bars/symbol) |
| **NOT** | CF BRTI / ETHUSDRTI / Kalshi settlement oracle |
| F2 | **DATA-BLOCKED** (see ORACLE_RECON_CF_BRTI_2026-09-12) |
| Examiner scores | **none** (this audit) |

## Hard tests

| # | Test | Pass |
|---|------|:----:|
| 1 | HASH_VERIFY + contiguity (11520×2, gaps=0, dups=0, sorted) | True |
| 2 | Schema (OHLCV + close=open+59999 + layer/label) | True |
| 3 | Sep-11 source split (Vision 04–10 / API 11; boundary) | True |
| 4 | Timestamp units Vision µs→ms truncation | True |
| 5 | KNOWABILITY join to PM-003 decision_time | True |
| 6 | Spot ≠ CF BRTI / NOT_oracle / F2 BLOCKED | True |
| 7 | Coverage freeze ≠ DATA-PROV-001 holdout extension | True |
| 8 | OHLC sanity | True |

## 1. HASH_VERIFY + contiguity

- CHECKSUMS entries: 20; all match: **True**
- Raw inventory: vision zips=14/14, api json=2/2
- **BTCUSDT**: rows=11520 (expect 11520), first=2026-09-04T00:00:00Z, last=2026-09-11T23:59:00Z, gaps_Δ≠60s=0, dups=0, sorted=True, pass=True
- **ETHUSDT**: rows=11520 (expect 11520), first=2026-09-04T00:00:00Z, last=2026-09-11T23:59:00Z, gaps_Δ≠60s=0, dups=0, sorted=True, pass=True

## 2. Schema

- **BTCUSDT**: close_time==open+59999 mismatch=0; layer_all_L3=True; label_NOT_oracle=True; market_spot=True; pass=True
- **ETHUSDT**: close_time==open+59999 mismatch=0; layer_all_L3=True; label_NOT_oracle=True; market_spot=True; pass=True
- Convention: `open_time_ms + 59999 (Binance 1m kline close)`

## 3. Sep-11 source split

- Vision days: ['2026-09-04', '2026-09-05', '2026-09-06', '2026-09-07', '2026-09-08', '2026-09-09', '2026-09-10'] (all 1440: True)
- API fill day: 2026-09-11 (1440: True)
- Boundary Sep-10→11: last=2026-09-10T23:59:00Z → first=2026-09-11T00:00:00Z; gap_ms=60000 (expect 60000); contiguous=True
- Path note: Vision daily zip 2026-09-11 HTTP 404 at fetch; filled via https://www.binance.com/api/v3/klines (api.binance.com HTTP 451 from host)

## 4. Timestamp units

- Convention: Vision CSV microseconds truncated with integer //1000 (not round) to match API ms; close remains …999
- BTC Vision spot-check all match: True; API first-bar match: True
- ETH Vision spot-check all match: True; API first-bar match: True
- Example: Vision open_us=1788480000000000 //1000 → 1788480000000 = derived 1788480000000; close_us=1788480059999999 → 1788480059999

## 5. KNOWABILITY join to PM-003

- Unique `decision_time` values: **3020**
- Range: 2026-09-04T20:46:00Z → 2026-09-11T20:30:00Z
- Land on `:00` seconds: **3020/3020** (fraction=1.0)
- Align to L3 `open_time_ms` grid (floor==decision): True
- Rule A strict `<` (close_time_ms < t): matched=3020, missing=0
- Rule A inclusive `<=` (close_time_ms <= t): matched=3020, missing=0
- `<` vs `<=` identical selection on this PM-003 slice: **True**
- Rule B open-at-t bar present: 3020/3020 (close NOT knowable — BLOCKED for close features)
- Equiv prior open (`decision_time_ms - 60000`) in grid: 3020/3020

### Exact join formula (binding for CLEARED F1)

```
knowable_bar = argmax { bar in L3 | bar.close_time_ms <= decision_time_ms }; price_at_t = knowable_bar.close; equiv_when_decision_on_minute_boundary: open_time_ms = floor_minute_ms(decision_time_ms) - 60_000 (= decision_time_ms - 60_000 when decision_time is :00.000).
```

- Recommended comparison: `close_time_ms <= decision_time_ms`
- Rationale: Binance 1m close_time_ms = open_time_ms + 59999. PM-003 decision_times all land on :00.000Z (minute boundary). At those instants, close_time_ms < t and close_time_ms <= t select the identical prior bar (prior close is always :59.999). Prefer <= so a decision exactly at close_time (if ever) still sees that bar as completed. Strict < is equally safe for this PM-003 slice and matches REPORT.md sketch.
- Rule B close blocked: Bar with open_time_ms == floor_minute_ms(decision_time_ms) has known open at t but UNKNOWN close until close_time_ms — using that bar's close at decision_time is LOOKAHEAD / BLOCKED.

### Samples

- decision_time=`2026-09-04T20:46:00Z` → completed prior open=`2026-09-04T20:45:00Z` (close_ms=1788554759999); open-at-t=`2026-09-04T20:46:00Z` (close knowable=False)
- decision_time=`2026-09-08T07:46:00Z` → completed prior open=`2026-09-08T07:45:00Z` (close_ms=1788853559999); open-at-t=`2026-09-08T07:46:00Z` (close knowable=False)
- decision_time=`2026-09-11T20:30:00Z` → completed prior open=`2026-09-11T20:29:00Z` (close_ms=1789158599999); open-at-t=`2026-09-11T20:30:00Z` (close knowable=False)

## 6. Spot ≠ CF BRTI

- Oracleish columns found: none
- Manifest NOT_oracle / NOT_CF_BRTI_substitute / NOT_settlement_oracle: {'NOT_oracle': True, 'NOT_CF_BRTI_substitute': True, 'NOT_settlement_oracle': True, 'layer': 'L3', 'role': 'external_predictor_price_at_t', 'forbidden_as_feature': ['PM-001 EXPIRATION_VALUE', 'terminal last-as-oracle', 'Binance-as-Kalshi-settlement-oracle']}
- F2 remains DATA-BLOCKED: **True** (`/workspace/lab/governance/ORACLE_RECON_CF_BRTI_2026-09-12.md`)
- Do **not** bless Binance as CF BRTI / Kalshi settlement oracle.

## 7. Coverage freeze

- L3 freeze: 2026-09-04T00:00:00Z → 2026-09-11T23:59:00Z (day-inclusive end 2026-09-11)
- DATA-PROV-001 holdout last open: 2026-08-31T23:55:00Z
- Extends DATA-PROV-001 holdout? **False**
- Note: DATA-PROV-L3-001 coverage is 2026-09-04→11 only. DATA-PROV-001 sealed holdout ends 2026-08-31T23:55:00Z (5m). This dataset does NOT extend or reopen that holdout; it is a separate L3 label for the PM-003 Feature Wave window.

## 8. OHLC sanity

- **BTCUSDT**: high<max(o,c)=0, low>min(o,c)=0, nonpos_price=0, neg_vol=0, pass=True
- **ETHUSDT**: high<max(o,c)=0, low>min(o,c)=0, nonpos_price=0, neg_vol=0, pass=True

## Verdict

**CONDITIONAL**

All integrity tests PASS. CONDITIONAL (not APPROVED) because: (1) role is L3 external predictor with explicit NOT_oracle constraints; (2) Sep-11 is API fill via www.binance.com (api.binance.com 451) not Vision zip; (3) F2/CF BRTI remains DATA-BLOCKED — Binance must not be promoted to settlement oracle; (4) knowability requires completed-bar join discipline.

### CLEARED F1 uses

- **CLEARED**: `F1_price_at_t_completed_1m_close`
  - join: price_at_t = L3.close where close_time_ms <= decision_time_ms (last completed 1m bar before/at t); equiv on PM-003 :00 boundaries: open_time_ms = decision_time_ms - 60_000
  - caveat: L3 external predictor only — not settlement oracle
  - caveat: Freeze = 2026-09-04→11 only
  - caveat: Do not use incomplete bar close at bar open
- **CLEARED**: `F1_RV_sigma_trailing_completed_1m`
  - join: RV/σ over trailing completed 1m bars with close_time_ms <= decision_time_ms (window ends at last completed bar before t); no bars with open_time_ms >= decision_time_ms
  - caveat: Trailing window must end strictly on completed bars
  - caveat: Same L3 / NOT_oracle constraints

### BLOCKED

- **BLOCKED**: `incomplete_bar_close_at_bar_open` — Using close of bar with open_time_ms == floor_minute(decision_time) at decision_time is LOOKAHEAD — close not knowable until close_time_ms
- **BLOCKED**: `Binance_as_F2_oracle_or_settlement` — Binance spot is L3 predictor only; Kalshi settlement oracle is CF BRTI / ETHUSDRTI
- **BLOCKED**: `claim_CF_BRTI_substitute` — Explicitly forbidden; ORACLE_RECON confirms F2 DATA-BLOCKED
- **BLOCKED**: `DATA_PROV_001_holdout_extension` — L3 freeze is 2026-09-04→11 only; does not extend DATA-PROV-001 holdout (ends 2026-08-31)
- **BLOCKED**: `Examiner_F1_scores_in_this_audit` — Clock integrity audit only — no Examiner numbers / no alpha
- **BLOCKED**: `F2_independent_oracle_replay` — F2 remains DATA-BLOCKED pending licensed CF/Kalshi path (ORACLE_RECON_CF_BRTI_2026-09-12)

## Policy

- No alpha / no Examiner F1 scores in this audit.
- No Binance-as-Kalshi-oracle claim.
- No DATA-PROV-001 holdout reopen/extension.
- No secrets / no purchase / no trading.

*End CLOCK_AUDIT_REPORT DATA-PROV-L3-001.*
