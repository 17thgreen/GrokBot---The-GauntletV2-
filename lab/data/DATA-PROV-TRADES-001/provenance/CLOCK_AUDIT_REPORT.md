# CLOCK AUDIT REPORT — DATA-PROV-TRADES-001

- Audited UTC: `2026-09-11T00:58:26.693535+00:00`
- Overall verdict: **APPROVED**
- JSON: `/workspace/lab/data/DATA-PROV-TRADES-001/provenance/CLOCK_AUDIT_REPORT.json`
- Script: `/workspace/lab/data/DATA-PROV-TRADES-001/provenance/clock_audit_DATA-PROV-TRADES-001.py`

## Scope
- Dataset: Binance Vision UM daily aggTrades zips (BTCUSDT, ETHUSDT)
- Range: 2021-01-01 → 2026-08-31 UTC
- Did NOT merge OHLCV, invent full-history row totals, create slices, or compute PnL
- Did NOT proxy L2 depth/spread

## Confirmed event-time semantics
- `transact_time`: exchange event time, milliseconds since Unix epoch (UTC)
- Vision column order: agg_trade_id, price, quantity, first_trade_id, last_trade_id, transact_time, is_buyer_maker
- Some days omit CSV header (handled: parse as 7-col Vision order)
- Aggressor: `is_buyer_maker==true` → aggressor SELL; `false` → aggressor BUY

## Pass/fail by section

| Section | Pass | Notes |
|---------|------|-------|
| A Inventory/calendar | True | zips/sidecars per symbol; SHA256SUMS; derived; recovery 24 |
| B HASH_VERIFY | True | 4138/4138 both-match; fails=0; full=True |
| C Deep sample CSV | True | n=33; header_safe=True |
| D Cross-day continuity | True | 6 pairs |
| E OHLCV 5m alignment | True | sample days; compatible_all=True |
| F Lookahead/knowability | True | rules documented; EDGE-005/006 UNMEASURABLE WITHOUT L2 |
| G Seal alignment feasibility | True | timestamp-align preferred; no slices created |

## A — Inventory exact counts

- **BTCUSDT**: zips=2069, sidecars=2069, first=2021-01-01, last=2026-08-31, missing_days=0, pass=True
- **ETHUSDT**: zips=2069, sidecars=2069, first=2021-01-01, last=2026-08-31, missing_days=0, pass=True
- SHA256SUMS lines: 4138 (expect 4138)
- derived/ empty: True
- missing_days.txt date rows: [] (empty_of_dates=True)
- BTCUSDT 2024-01-01..01-24 recovery: 24/24 exist

## B — HASH_VERIFY

- total_zips=4138, sidecar_matches=4138, sums_matches=4138, both=4138
- fail_count=0, elapsed_sec=29.73, workers=6
- full_verify_completed=True

## C — Deep sample CSV audits

- Stratified seed=42 days: ['2021-11-22', '2021-12-21', '2022-04-11', '2022-08-08', '2023-05-17', '2023-07-20', '2024-05-11', '2024-09-08', '2025-01-01', '2025-08-24', '2026-07-13', '2026-08-29']

| Symbol | Date | Rows | Header | Dup agg | ID↑ | Time↺ | Gaps | Out-of-day | Agg SELL/BUY | Pass |
|--------|------|------|--------|---------|-----|-------|------|------------|--------------|------|
| BTCUSDT | 2021-01-01 | 885732 | True | 0 | True | 0 | 0 | 0 | 447386/438346 | True |
| BTCUSDT | 2021-11-22 | 2062432 | False | 0 | True | 0 | 0 | 0 | 1041229/1021203 | True |
| BTCUSDT | 2021-12-21 | 1876367 | False | 0 | True | 0 | 0 | 0 | 937792/938575 | True |
| BTCUSDT | 2022-04-11 | 1843670 | False | 0 | True | 0 | 0 | 0 | 933051/910619 | True |
| BTCUSDT | 2022-06-15 | 6146703 | False | 0 | True | 0 | 0 | 0 | 3089669/3057034 | True |
| BTCUSDT | 2022-08-08 | 1430125 | False | 0 | True | 0 | 0 | 0 | 717450/712675 | True |
| BTCUSDT | 2023-05-17 | 1265796 | True | 0 | True | 0 | 0 | 0 | 633141/632655 | True |
| BTCUSDT | 2023-07-20 | 1040049 | True | 0 | True | 0 | 0 | 0 | 514800/525249 | True |
| BTCUSDT | 2024-01-01 | 761222 | True | 0 | True | 0 | 0 | 0 | 376837/384385 | True |
| BTCUSDT | 2024-01-02 | 1677641 | True | 0 | True | 0 | 0 | 0 | 851006/826635 | True |
| BTCUSDT | 2024-01-03 | 2295158 | True | 0 | True | 0 | 0 | 0 | 1165726/1129432 | True |
| BTCUSDT | 2024-05-11 | 683102 | True | 0 | True | 0 | 0 | 0 | 335262/347840 | True |
| BTCUSDT | 2024-09-08 | 835850 | True | 0 | True | 0 | 0 | 0 | 419898/415952 | True |
| BTCUSDT | 2025-01-01 | 726611 | True | 0 | True | 0 | 0 | 0 | 361496/365115 | True |
| BTCUSDT | 2025-08-24 | 1172176 | True | 0 | True | 0 | 0 | 0 | 592569/579607 | True |
| BTCUSDT | 2026-07-13 | 1432145 | True | 0 | True | 0 | 0 | 0 | 712863/719282 | True |
| BTCUSDT | 2026-08-29 | 444895 | True | 0 | True | 0 | 0 | 0 | 220553/224342 | True |
| BTCUSDT | 2026-08-31 | 1353859 | True | 0 | True | 0 | 0 | 0 | 679219/674640 | True |
| ETHUSDT | 2021-01-01 | 437250 | False | 0 | True | 0 | 0 | 0 | 224893/212357 | True |
| ETHUSDT | 2021-11-22 | 1393037 | False | 0 | True | 0 | 0 | 0 | 702661/690376 | True |
| ETHUSDT | 2021-12-21 | 1087800 | False | 0 | True | 0 | 0 | 0 | 543344/544456 | True |
| ETHUSDT | 2022-04-11 | 1298709 | False | 0 | True | 0 | 0 | 0 | 660977/637732 | True |
| ETHUSDT | 2022-06-15 | 5317519 | False | 0 | True | 0 | 0 | 0 | 2667726/2649793 | True |
| ETHUSDT | 2022-08-08 | 1661373 | False | 0 | True | 0 | 0 | 0 | 822255/839118 | True |
| ETHUSDT | 2023-05-17 | 807546 | True | 0 | True | 0 | 0 | 0 | 407505/400041 | True |
| ETHUSDT | 2023-07-20 | 699123 | True | 0 | True | 0 | 0 | 0 | 347749/351374 | True |
| ETHUSDT | 2024-05-11 | 603304 | True | 0 | True | 0 | 0 | 0 | 286447/316857 | True |
| ETHUSDT | 2024-09-08 | 715681 | True | 0 | True | 0 | 0 | 0 | 350353/365328 | True |
| ETHUSDT | 2025-01-01 | 816837 | True | 0 | True | 0 | 0 | 0 | 395135/421702 | True |
| ETHUSDT | 2025-08-24 | 2880376 | True | 0 | True | 0 | 0 | 0 | 1451121/1429255 | True |
| ETHUSDT | 2026-07-13 | 1269320 | True | 0 | True | 0 | 0 | 0 | 635319/634001 | True |
| ETHUSDT | 2026-08-29 | 340277 | True | 0 | True | 0 | 0 | 0 | 165130/175147 | True |
| ETHUSDT | 2026-08-31 | 1250468 | True | 0 | True | 0 | 0 | 0 | 625666/624802 | True |

### Header quirk checks

- ETHUSDT 2021-01-01: expected_header=False, observed=False, handled_safely=True
- BTCUSDT 2022-06-15: expected_header=False, observed=False, handled_safely=True
- ETHUSDT 2022-06-15: expected_header=False, observed=False, handled_safely=True
- BTCUSDT 2021-01-01: expected_header=True, observed=True, handled_safely=True

## D — Cross-day continuity

- BTCUSDT 2024-01-01→2024-01-02: id_inc=True gap_missing=0 time_ok=True pass=True
- BTCUSDT 2022-06-14→2022-06-15: id_inc=True gap_missing=0 time_ok=True pass=True
- BTCUSDT 2026-08-30→2026-08-31: id_inc=True gap_missing=0 time_ok=True pass=True
- ETHUSDT 2024-01-01→2024-01-02: id_inc=True gap_missing=0 time_ok=True pass=True
- ETHUSDT 2022-06-14→2022-06-15: id_inc=True gap_missing=0 time_ok=True pass=True
- ETHUSDT 2026-08-30→2026-08-31: id_inc=True gap_missing=0 time_ok=True pass=True

## E — Alignment to DATA-PROV-001 5m bars

- BTCUSDT 2021-01-01: ohlcv_bars=288 empty_bars=0 trades=885732 outside_day=0 outside_ohlcv_opens=0 med_|last-close|/close=0.0 compatible=True pass=True
- BTCUSDT 2022-06-15: ohlcv_bars=288 empty_bars=0 trades=6146703 outside_day=0 outside_ohlcv_opens=0 med_|last-close|/close=0.0 compatible=True pass=True
- BTCUSDT 2024-01-01: ohlcv_bars=288 empty_bars=0 trades=761222 outside_day=0 outside_ohlcv_opens=0 med_|last-close|/close=0.0 compatible=True pass=True
- BTCUSDT 2026-08-31: ohlcv_bars=288 empty_bars=0 trades=1353859 outside_day=0 outside_ohlcv_opens=0 med_|last-close|/close=0.0 compatible=True pass=True
- ETHUSDT 2021-01-01: ohlcv_bars=288 empty_bars=0 trades=437250 outside_day=0 outside_ohlcv_opens=0 med_|last-close|/close=0.0 compatible=True pass=True
- ETHUSDT 2022-06-15: ohlcv_bars=288 empty_bars=0 trades=5317519 outside_day=0 outside_ohlcv_opens=0 med_|last-close|/close=0.0 compatible=True pass=True
- ETHUSDT 2024-01-01: ohlcv_bars=288 empty_bars=0 trades=504953 outside_day=0 outside_ohlcv_opens=0 med_|last-close|/close=0.0 compatible=True pass=True
- ETHUSDT 2026-08-31: ohlcv_bars=288 empty_bars=0 trades=1250468 outside_day=0 outside_ohlcv_opens=0 med_|last-close|/close=0.0 compatible=True pass=True

## F — Lookahead / knowability

- A trade at transact_time T is knowable only after T (and after receipt — receipt time [U] unavailable in this dataset).
- Features for a decision at 5m bar close C may only use trades with transact_time <= C.
- Binance 5m close_time_ms ≈ open_time_ms + 299999; decision-at-close must wait until close_time.
- Cannot use future trades within an incomplete bar (trades with transact_time > current decision time).
- No receipt/local ingest timestamps in Vision aggTrades archives — exchange event-time only.
- EDGE-005/006: **UNMEASURABLE_WITHOUT_L2** — aggTrades provide aggressor side and size of executed aggregates only; they do not provide order-book depth troughs, bid/ask sizes, or spread path. EDGE-005/006 remain unmeasurable from this dataset alone.

## G — Seal alignment feasibility (metadata only)

- Trades calendar: {'first': '2021-01-01', 'last': '2026-08-31', 'days_per_symbol': 2069}
- OHLCV SEAL bounds (BTCUSDT): {'research_open_first_utc': '2021-01-03T04:00:00+00:00', 'research_open_last_utc': '2024-05-27T06:15:00+00:00', 'validation_open_last_utc': '2025-07-14T15:00:00+00:00', 'holdout_open_first_utc': '2025-07-14T15:05:00+00:00', 'holdout_open_last_utc': '2026-08-31T23:55:00+00:00'}
- can_day_aligned_splits=True
- can_timestamp_aligned_splits=True
- slices_created=False
- Recommendation (day): Possible but blunt: map research to calendar dates whose UTC day intersects research open_time range; bars on 2024-05-27 span both research (through 06:15) and validation (from 06:20) — day-align would leak across slice boundary on that calendar day.
- Recommendation (timestamp): PREFERRED: for a decision at bar close C, include trades with transact_time <= C and only bars belonging to the target SEAL slice. Research: open_time in [research_open_first, research_open_last]; same for validation/holdout. Do NOT create slices in this audit.
- Boundary days: {'research_validation': '2024-05-27 — split intra-day at 06:15 vs 06:20 open', 'validation_holdout': '2025-07-14 — split intra-day at 15:00 vs 15:05 open'}

## Verdict detail

- **APPROVED**
- hard_fail: []
- conditional_triggers: ['F: receipt-time [U] unavailable — knowability bounded by exchange transact_time only', 'F: EDGE-005/006 UNMEASURABLE WITHOUT L2 — trades do not provide depth/spread', 'G: prefer timestamp-aligned SEAL cuts; day-align leaks on 2024-05-27 and 2025-07-14 boundary days']
- quarantine_triggers: []

## Known limitations

- Receipt/local ingest timestamps not present in Vision archives ([U] unknown).
- Full per-day row inventory across all 4138 zips was NOT computed in this audit (samples only).
- ID gaps in agg_trade_id may reflect exchange-side non-publication; reported as counts where sampled.
- EDGE-005/006 unmeasurable without L2.
- No strategy PnL; no research slices created.

## Policy

- Raw zips remain immutable; derived/ left empty.
- Do not claim APPROVED if header handling unsafe or hashes fail.

