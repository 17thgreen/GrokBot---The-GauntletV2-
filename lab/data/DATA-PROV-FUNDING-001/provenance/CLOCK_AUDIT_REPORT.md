# CLOCK AUDIT REPORT — DATA-PROV-FUNDING-001

- Audited UTC: `2026-09-11T04:34:54.875418+00:00`
- Verdict: **CONDITIONAL**
- JSON: `/workspace/lab/data/DATA-PROV-FUNDING-001/provenance/CLOCK_AUDIT_REPORT.json`
- Script: `/workspace/lab/data/DATA-PROV-FUNDING-001/provenance/clock_audit_DATA-PROV-FUNDING-001.py`

## Verdict rationale
- Hard integrity tests PASS for both symbols: inventory 68/68, hashes match, schema OK, no dupes, sorted, month bounds OK, interval catalog measured, no missing settlements vs 8h grid, no NaN/negative interval, OHLCV join unmatched=0.
- Vision monthly pack publish lag vs calc_time is [U]/exact lag not established). Observable-to-trader timing for Vision-only consumers uncertain → cannot APPROVE.
- Verdict CONDITIONAL: data integrity clean, but knowability of publish/observable lag uncertain. SIGNAL must enforce calc_time<=t; forbidden premiumIndex predicted rates. Split freeze may use proposed usable coverage aligned to SEAL_LOCK without reshaping it.

## Knowability rules
- Source: `/workspace/lab/governance/DATA_PROV_CATALYST_SOURCES_2026-09-11.md` §1 DATA-PROV-FUNDING-001
- Settlement (`calc_time`): calc_time is the exchange settlement / calculation event time (ms UTC). Equivalent semantics to REST fundingTime per source map.
- Publish: Vision monthly zip appears after the calendar month closes (monthly pack). REST /fapi/v1/fundingRate is nearer real-time but geo-blocked on this host. Exact Vision publish lag after calc_time is tagged [U] in source map — NOT measured in this audit.
- Observable-to-trader: A live trader using REST/WS can observe a settlement at/after calc_time (exchange clock). A researcher using only Vision monthly packs cannot observe intra-month settlements until the monthly archive is published. Exact pack publish timestamp vs last calc_time in month: [U] unknown — not established from Vision object metadata in this audit.
- SIGNAL allowed: SIGNAL may use last_funding_rate only if calc_time <= decision t (after settlement on exchange clock).
- SIGNAL forbidden:
  - premiumIndex predicted / next-interval rate before settlement
  - lastFundingRate / nextFundingTime from premiumIndex as if settled
  - Invented mid-interval accrued funding for SIGNAL
- Vision monthly pack publish lag vs calc_time: **UNKNOWN** tag=[U] exact_lag_established=False
- Implication: Cannot establish when a Vision-only consumer could observe each print relative to calc_time. For backtests that claim live-trader parity on exchange clock, settlement rule calc_time<=t applies. For pipelines that ingest only Vision monthly packs, observability is delayed to pack publish — CONDITIONAL trigger.
- Verdict impact: Knowability of publish/observable lag uncertain → verdict must be CONDITIONAL or QUARANTINED, not APPROVED.

## Global inventory / hashes
- SHA256SUMS lines: 136 (expect 136)
- All hashes match: **True** (mismatches=0)
- derived/ empty: **True** entries=[]
- missing.txt empty-of-months: **True**

## Per-symbol hard tests

| Test | BTCUSDT | ETHUSDT |
|------|---------|---------|
| inventory | True | True |
| schema | True | True |
| duplicates_sort_bounds | True | True |
| interval_catalog | True | True |
| missing_settlements | True | True |
| impossible | True | True |
| join_ohlcv | True | True |

## BTCUSDT

- Inventory: months=68/68 missing=0 zips=68 sidecars=68 bytes=60996 range=2021-01..2026-08
- Rows: 6207 calc_time first=2021-01-01T00:00:00.002000+00:00 last=2026-08-31T16:00:00.001000+00:00
- Schema columns_ok=True dtypes={'calc_time': 'int64', 'funding_interval_hours': 'int64', 'last_funding_rate': 'float64'} nulls={'calc_time': 0, 'funding_interval_hours': 0, 'last_funding_rate': 0}
- Dup/sort/bounds: dup=0 sorted=True month_violations=0 documented_edges=0
- Interval unique values: [8]
  - regime iv=8h n=6207 2021-01-01T00:00:00.002000+00:00 → 2026-08-31T16:00:00.001000+00:00
- Missing settlements: gap_count=0 pairwise_anoms=0 classic_8h missing=0 expected=6207 actual=6207
- Impossible: nan_rates=0 neg_iv=0 absurd_outliers=0 rate_min=-0.00119172 rate_max=0.00248993
- Join OHLCV: rule=`nearest completed 5m bar with close_time_ms >= calc_time (searchsorted on sorted close_time_ms)` prints=6207 matched=6207 unmatched=0 outside_span=0 lag_ms median=299999.0 min=299952 max=299999
- Seal coverage funding span: 2021-01-01T00:00:00.002000+00:00 → 2026-08-31T16:00:00.001000+00:00
  - research: n_prints=3720 (2021-01-03T04:00:00+00:00 .. 2024-05-27T06:15:00+00:00)
  - validation: n_prints=1240 (2024-05-27T06:20:00+00:00 .. 2025-07-14T15:00:00+00:00)
  - holdout: n_prints=1240 (2025-07-14T15:05:00+00:00 .. 2026-08-31T23:55:00+00:00)
  - pre_research_context prints: 7
- Usable coverage recommendation (do NOT reshape SEAL_LOCK): Funding Vision months 2021-01..2026-08 fully cover SEAL_LOCK research/validation/holdout open-time bounds for this symbol. Propose freeze usable funding coverage to the same UTC open bounds as DATA-PROV-001 SEAL_LOCK; prints before research_open_first remain available as pre-split context only (not research-labeled).
  - proposed window print counts: {'research': 3720, 'validation': 1240, 'holdout': 1240, 'pre_research_context': 7}

## ETHUSDT

- Inventory: months=68/68 missing=0 zips=68 sidecars=68 bytes=61336 range=2021-01..2026-08
- Rows: 6207 calc_time first=2021-01-01T00:00:00.002000+00:00 last=2026-08-31T16:00:00.001000+00:00
- Schema columns_ok=True dtypes={'calc_time': 'int64', 'funding_interval_hours': 'int64', 'last_funding_rate': 'float64'} nulls={'calc_time': 0, 'funding_interval_hours': 0, 'last_funding_rate': 0}
- Dup/sort/bounds: dup=0 sorted=True month_violations=0 documented_edges=0
- Interval unique values: [8]
  - regime iv=8h n=6207 2021-01-01T00:00:00.002000+00:00 → 2026-08-31T16:00:00.001000+00:00
- Missing settlements: gap_count=0 pairwise_anoms=0 classic_8h missing=0 expected=6207 actual=6207
- Impossible: nan_rates=0 neg_iv=0 absurd_outliers=0 rate_min=-0.00356332 rate_max=0.00375
- Join OHLCV: rule=`nearest completed 5m bar with close_time_ms >= calc_time (searchsorted on sorted close_time_ms)` prints=6207 matched=6207 unmatched=0 outside_span=0 lag_ms median=299999.0 min=299952 max=299999
- Seal coverage funding span: 2021-01-01T00:00:00.002000+00:00 → 2026-08-31T16:00:00.001000+00:00
  - research: n_prints=3720 (2021-01-03T04:00:00+00:00 .. 2024-05-27T06:15:00+00:00)
  - validation: n_prints=1240 (2024-05-27T06:20:00+00:00 .. 2025-07-14T15:00:00+00:00)
  - holdout: n_prints=1240 (2025-07-14T15:05:00+00:00 .. 2026-08-31T23:55:00+00:00)
  - pre_research_context prints: 7
- Usable coverage recommendation (do NOT reshape SEAL_LOCK): Funding Vision months 2021-01..2026-08 fully cover SEAL_LOCK research/validation/holdout open-time bounds for this symbol. Propose freeze usable funding coverage to the same UTC open bounds as DATA-PROV-001 SEAL_LOCK; prints before research_open_first remain available as pre-split context only (not research-labeled).
  - proposed window print counts: {'research': 3720, 'validation': 1240, 'holdout': 1240, 'pre_research_context': 7}

## Paths
- `/workspace/lab/data/DATA-PROV-FUNDING-001`
- `/workspace/lab/data/DATA-PROV-FUNDING-001/raw`
- `/workspace/lab/data/DATA-PROV-FUNDING-001/derived`
- `/workspace/lab/data/DATA-PROV-FUNDING-001/provenance`
- `/workspace/lab/data/DATA-PROV-FUNDING-001/provenance/SHA256SUMS.txt`
- `/workspace/lab/data/DATA-PROV-FUNDING-001/provenance/DOWNLOAD_MANIFEST.md`
- `/workspace/lab/governance/DATA_PROV_CATALYST_SOURCES_2026-09-11.md`
- `/workspace/lab/data/DATA-PROV-001/sealed/SEAL_LOCK.json`
- `/workspace/lab/data/DATA-PROV-001/raw/BTCUSDT_5m_binance_um.parquet`
- `/workspace/lab/data/DATA-PROV-001/raw/ETHUSDT_5m_binance_um.parquet`
- `/workspace/lab/data/DATA-PROV-FUNDING-001/provenance/CLOCK_AUDIT_REPORT.json`
- `/workspace/lab/data/DATA-PROV-FUNDING-001/provenance/CLOCK_AUDIT_REPORT.md`
- `/workspace/lab/data/DATA-PROV-FUNDING-001/provenance/clock_audit_DATA-PROV-FUNDING-001.py`

## Success criteria
- Reports written: JSON=True MD=True
- Exit code: 0 (audit completed; verdict=CONDITIONAL)
