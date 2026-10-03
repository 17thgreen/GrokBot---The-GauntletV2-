# CLOCK AUDIT REPORT — DATA-PROV-OI-001

- Audited UTC: `2026-09-11T04:39:19.475913+00:00`
- Overall verdict: **CONDITIONAL**
- JSON: `/workspace/lab/data/DATA-PROV-OI-001/provenance/CLOCK_AUDIT_REPORT.json`
- Script: `/workspace/lab/data/DATA-PROV-OI-001/provenance/clock_audit_DATA-PROV-OI-001.py`

## Scope
- Dataset: Binance Vision UM daily metrics zips (5m OI + ratios)
- BTC: 2021-01-01 → 2026-08-31 (2069 days)
- ETH: 2021-12-01 → 2026-08-31 (1735 days); intentional gap 2021-01-01..2021-11-30
- No alpha. No invented ETH history. No inferred OI from price.
- Does NOT reshape DATA-PROV-001 SEAL_LOCK

## Confirmed timestamp semantics
- `create_time`: exchange observation/snapshot time `YYYY-MM-DD HH:MM:SS` UTC at 5m steps
- Knowability: OI knowable iff `create_time <= decision t`
- OI is a **level** (last sample in bar), not a sum — despite column name `sum_open_interest`
- Stamp↔OHLCV convention: **bucket_start_open_time** (create_time aligns with OHLCV `open_time_ms` / bucket start)
- Receipt/publish lag: **UNCERTAIN [U]** (Vision zip first-print not in-archive)

## Pass/fail by section

| Section | Pass | Notes |
|---------|------|-------|
| A Inventory/calendar | True | BTC 2069/2069; ETH 1735/1735; SHA256SUMS 3804 |
| B HASH_VERIFY | True | 3804/3804 both-match; fails=0; full=True |
| C Full parse all days | True | days=3804; elapsed=2.355s |
| D Snapshot vs receipt | True | receipt [U]; knowability rule documented |
| E OHLCV 5m alignment | True | bucket-start convention; no orphan OI stamps |
| F ETH asymmetry | True | ETH pre-2021-12 files=0 |
| G Common window proposal | True | Catalyst_COMMON_WINDOW explicit |

## A — Inventory

- **BTCUSDT**: zips=2069, sidecars=2069, first=2021-01-01, last=2026-08-31, missing=0, pass=True
- **ETHUSDT**: zips=1735, sidecars=1735, first=2021-12-01, last=2026-08-31, missing=0, pass=True
- SHA256SUMS lines: 3804 (expect 3804)
- derived/ empty: True
- missing_days.txt empty: True
- ETH intentional gap: 2021-01-01 → 2021-11-30 (334 days)

## B — HASH_VERIFY (full)

- total_zips=3804, sidecar_matches=3804, sums_matches=3804, both=3804
- fail_count=0, elapsed_sec=0.328, workers=6
- full_verify_completed=True

## C — Full parse (all days, both symbols)

### BTCUSDT
- days_audited=2069, hard_pass=True, pass=True
- total_rows=635420, unique_create_times=595268
- within_file_dup days=141, identical_dup_buckets=40152, conflicting=0
- missing_stamp_total=604 (frac=0.00101364), days_with_missing=68, grid_severe=False
- midnight_collision_pairs=0, midnight_collision_stamps=0
- nan_oi=0, neg_oi=0, off_grid=0, foreign=0
- days_not_ascending=107
- join_rule within-file: SORT by create_time ascending, then keep latest-by-file-order per create_time bucket (early-2021 identical double-writes; conflicting=0 → keep-any equivalent). Some later days are unsorted in-file — sort required.
- join_rule midnight: if create_time appears in adjacent day files, keep latest-by-timestamp per bucket (day D+1 row wins only if values differ; else identical). Observed collision stamps tallied below.

Missing stamps sample (first days):
- 2021-01-20: count=17 sample=['2021-01-20 00:50:00', '2021-01-20 00:55:00', '2021-01-20 01:00:00', '2021-01-20 01:05:00', '2021-01-20 01:10:00', '2021-01-20 01:15:00', '2021-01-20 01:20:00', '2021-01-20 01:25:00', '2021-01-20 01:30:00', '2021-01-20 01:35:00', '2021-01-20 01:40:00', '2021-01-20 01:45:00']
- 2021-02-05: count=9 sample=['2021-02-05 00:35:00', '2021-02-05 00:40:00', '2021-02-05 00:45:00', '2021-02-05 00:50:00', '2021-02-05 00:55:00', '2021-02-05 01:00:00', '2021-02-05 01:05:00', '2021-02-05 01:10:00', '2021-02-05 01:15:00']
- 2021-02-07: count=1 sample=['2021-02-07 01:45:00']
- 2021-02-10: count=1 sample=['2021-02-10 01:00:00']
- 2021-02-11: count=12 sample=['2021-02-11 01:10:00', '2021-02-11 03:30:00', '2021-02-11 12:40:00', '2021-02-11 13:10:00', '2021-02-11 13:35:00', '2021-02-11 13:45:00', '2021-02-11 14:20:00', '2021-02-11 14:35:00', '2021-02-11 14:45:00', '2021-02-11 15:15:00', '2021-02-11 15:45:00', '2021-02-11 15:50:00']
- 2021-02-15: count=3 sample=['2021-02-15 01:10:00', '2021-02-15 02:20:00', '2021-02-15 02:25:00']
- 2021-02-16: count=1 sample=['2021-02-16 01:45:00']
- 2021-02-18: count=1 sample=['2021-02-18 00:05:00']
- 2021-02-19: count=70 sample=['2021-02-19 00:35:00', '2021-02-19 00:40:00', '2021-02-19 00:45:00', '2021-02-19 00:50:00', '2021-02-19 00:55:00', '2021-02-19 01:00:00', '2021-02-19 01:05:00', '2021-02-19 01:10:00', '2021-02-19 01:15:00', '2021-02-19 01:20:00', '2021-02-19 01:25:00', '2021-02-19 01:30:00']
- 2021-02-20: count=16 sample=['2021-02-20 00:00:00', '2021-02-20 00:05:00', '2021-02-20 00:10:00', '2021-02-20 00:15:00', '2021-02-20 00:20:00', '2021-02-20 00:25:00', '2021-02-20 00:30:00', '2021-02-20 00:35:00', '2021-02-20 00:40:00', '2021-02-20 00:45:00', '2021-02-20 00:50:00', '2021-02-20 00:55:00']
- 2021-02-24: count=1 sample=['2021-02-24 00:30:00']
- 2021-02-28: count=1 sample=['2021-02-28 00:30:00']
- 2021-03-05: count=1 sample=['2021-03-05 00:30:00']
- 2021-03-10: count=1 sample=['2021-03-10 00:05:00']
- 2021-03-12: count=1 sample=['2021-03-12 00:05:00']

### ETHUSDT
- days_audited=1735, hard_pass=True, pass=True
- total_rows=499537, unique_create_times=499537
- within_file_dup days=0, identical_dup_buckets=0, conflicting=0
- missing_stamp_total=143 (frac=0.00028618), days_with_missing=10, grid_severe=False
- midnight_collision_pairs=0, midnight_collision_stamps=0
- nan_oi=0, neg_oi=0, off_grid=0, foreign=0
- days_not_ascending=111
- join_rule within-file: SORT by create_time ascending, then keep latest-by-file-order per create_time bucket (early-2021 identical double-writes; conflicting=0 → keep-any equivalent). Some later days are unsorted in-file — sort required.
- join_rule midnight: if create_time appears in adjacent day files, keep latest-by-timestamp per bucket (day D+1 row wins only if values differ; else identical). Observed collision stamps tallied below.

Missing stamps sample (first days):
- 2021-12-04: count=3 sample=['2021-12-04 05:00:00', '2021-12-04 05:25:00', '2021-12-04 05:30:00']
- 2021-12-15: count=1 sample=['2021-12-15 19:05:00']
- 2021-12-24: count=1 sample=['2021-12-24 15:05:00']
- 2021-12-29: count=1 sample=['2021-12-29 23:25:00']
- 2021-12-31: count=1 sample=['2021-12-31 16:05:00']
- 2023-09-12: count=3 sample=['2023-09-12 08:40:00', '2023-09-12 08:45:00', '2023-09-12 08:50:00']
- 2024-02-16: count=125 sample=['2024-02-16 13:35:00', '2024-02-16 13:40:00', '2024-02-16 13:45:00', '2024-02-16 13:50:00', '2024-02-16 13:55:00', '2024-02-16 14:00:00', '2024-02-16 14:05:00', '2024-02-16 14:10:00', '2024-02-16 14:15:00', '2024-02-16 14:20:00', '2024-02-16 14:25:00', '2024-02-16 14:30:00']
- 2024-10-28: count=2 sample=['2024-10-28 16:25:00', '2024-10-28 16:30:00']
- 2025-08-29: count=3 sample=['2025-08-29 06:20:00', '2025-08-29 06:25:00', '2025-08-29 06:30:00']
- 2026-08-12: count=3 sample=['2026-08-12 11:45:00', '2026-08-12 11:50:00', '2026-08-12 11:55:00']

- within_file_dup_only_day_count=119 (2021-01-01 → 2021-05-20)

## D — Snapshot vs receipt

- Knowability: `OI knowable at decision t iff create_time <= t (snapshot_ts ≤ t)`
- OI aggregation: OI is a LEVEL (last sample in bar), not a sum across trades. Column name sum_open_interest is Binance Vision naming for the OI level.
- Receipt: UNCERTAIN [U]
- Note: Vision daily zip first-print / CDN publish time is not recorded in-archive. Zip internal CSV mtimes reflect packaging, not exchange snapshot receipt. Cannot prove zero publish lag beyond create_time itself from this corpus alone.

## E — OHLCV 5m alignment

- Aggregate rule: Join OI to OHLCV on create_time_ms == open_time_ms (bucket-start convention). OI level for bar open T is the row at create_time=T; do not sum OI. ΔOI features: diff of levels across bars after dedupe.

### BTCUSDT
- convention=bucket_start_open_time
- oi_unique=595268, ohlcv_bars=595872
- oi→open matches=595268, oi with no OHLCV open=0
- ohlcv opens in OI range with no OI=604
- note: create_time stamps fall on the same 5m grid as OHLCV open_time_ms (bucket start). Treat as snapshot time at bar open; for bar [T, T+5m) the level at create_time=T is the OI sample at open. Knowability at decision t requires create_time <= t. For features at bar close, create_time=T is known (T < close).

### ETHUSDT
- convention=bucket_start_open_time
- oi_unique=499537, ohlcv_bars=595872
- oi→open matches=499537, oi with no OHLCV open=0
- ohlcv opens in OI range with no OI=143
- note: create_time stamps fall on the same 5m grid as OHLCV open_time_ms (bucket start). Treat as snapshot time at bar open; for bar [T, T+5m) the level at create_time=T is the OI sample at open. Knowability at decision t requires create_time <= t. For features at bar close, create_time=T is known (T < close).

## F — ETH coverage asymmetry

- BTC full seal range: True (2021-01-01 → 2026-08-31)
- ETH files before 2021-12-01: 0
- ETH range: 2021-12-01 → 2026-08-31
- intentional_gap_days=334
- no_invented_eth=True

## G — Catalyst_COMMON_WINDOW (proposal)

- **Name:** `Catalyst_COMMON_WINDOW`
- **UTC bounds:** `2021-12-01T00:00:00+00:00` → `2026-08-31T23:55:00+00:00`
- **open_time_ms:** 1638316800000 → 1788220500000
- **bar_count_inclusive:** 499680
- datasets: ['DATA-PROV-OI-001', 'DATA-PROV-001']

### Map onto existing SEAL_LOCK (clipped, not reshaped)

- **research**: original `2021-01-03T04:00:00+00:00` → `2024-05-27T06:15:00+00:00`; clipped `2021-12-01T00:00:00+00:00` → `2024-05-27T06:15:00+00:00`; empty=False; bars_approx=261580
- **validation**: original `2024-05-27T06:20:00+00:00` → `2025-07-14T15:00:00+00:00`; clipped `2024-05-27T06:20:00+00:00` → `2025-07-14T15:00:00+00:00`; empty=False; bars_approx=119049
- **historical_holdout**: original `2025-07-14T15:05:00+00:00` → `2026-08-31T23:55:00+00:00`; clipped `2025-07-14T15:05:00+00:00` → `2026-08-31T23:55:00+00:00`; empty=False; bars_approx=119051

### Alt fresh 60/20/20 on common window (proposal only)

- post_warmup_bars=499056
- research: `2021-12-03T04:00:00+00:00` → `2024-10-07T20:40:00+00:00` (299433 bars)
- validation: `2024-10-07T20:45:00+00:00` → `2025-09-19T10:15:00+00:00` (99811 bars)
- holdout: `2025-09-19T10:20:00+00:00` → `2026-08-31T23:55:00+00:00` (99812 bars)

### Usable coverage for split freeze

- **btc_oi_only**: `2021-01-01T00:00:00+00:00` → `2026-08-31T23:55:00+00:00` — BTC OI + BTC OHLCV; ETH abstain
- **eth_oi_joint**: `2021-12-01T00:00:00+00:00` → `2026-08-31T23:55:00+00:00` — BTC OI + ETH OI + both OHLCV
- **eth_oi_absent_abstain**: `2021-01-01T00:00:00+00:00` → `2021-11-30T23:55:00+00:00` — No ETH Vision metrics; joint edges must abstain

- Recommendation: Prefer map_existing_SEAL_LOCK_clipped for continuity with OHLCV holdout lock; use Catalyst_COMMON_WINDOW bounds as hard gate for joint BTC/ETH OI features. Do not reshape sealed OHLCV slices.

## Verdict

- **CONDITIONAL**
- Flags: ['BTCUSDT_grid_imperfect', 'BTCUSDT_missing_5m_stamps', 'BTCUSDT_within_file_dups_need_dedupe_rule', 'BTCUSDT_within_file_order_needs_sort', 'ETHUSDT_grid_imperfect', 'ETHUSDT_missing_5m_stamps', 'ETHUSDT_within_file_order_needs_sort', 'receipt_publish_lag_uncertain']
- Section pass: {'A': True, 'B': True, 'C': True, 'D': True, 'E': True, 'F': True, 'G': True}
- Rationale: CONDITIONAL if receipt/publish lag uncertain or midnight/within-file dups need careful join rule; QUARANTINE if 5m grid broken badly; APPROVED only if all hard checks pass and no conditional flags.

