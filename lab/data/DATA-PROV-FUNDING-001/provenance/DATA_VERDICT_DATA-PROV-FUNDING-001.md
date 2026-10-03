# DATA VERDICT — DATA-PROV-FUNDING-001
**Issued by:** The Clock  
**Issued UTC:** 2026-09-11T04:39:57Z  
**Audit:** `/workspace/lab/data/DATA-PROV-FUNDING-001/provenance/CLOCK_AUDIT_REPORT.json`

---

## DATA VERDICT: CONDITIONAL

**QUALITY_STATUS:** APPROVED_WITH_LIMITATIONS

Usable for provisional RESEARCH/VALIDATION of funding-dependent Catalyst edges (e.g. EDGE-20260911-005 / 006) under settlement knowability rules below.  
**Not** venue marriage. **Not** capital. **Not** APPROVED (Vision pack publish lag [U]).

---

## DATA MANIFEST

| Field | Value |
|-------|-------|
| DATASET_ID | DATA-PROV-FUNDING-001 |
| SOURCE | Binance Vision monthly `fundingRate` UM [V] |
| VENUE | Binance USD-M — PROVISIONAL REFERENCE |
| INSTRUMENT | BTCUSDT, ETHUSDT |
| START | 2021-01-01T00:00:00.002Z |
| END | 2026-08-31T16:00:00.001Z |
| FREQUENCY | settlement prints (measured interval **8h only** in this span) |
| TIMESTAMP_DEFINITION | `calc_time` = exchange **settlement** event time, UTC epoch ms [V] |
| KNOWN_LATENCY | Vision monthly pack publish lag vs calc_time **[U]** |
| KNOWN_GAPS | 0 missing settlements vs classic 8h grid (6207/6207 each) [V] |
| TRANSFORMATIONS | none; derived/ empty [V] |
| QUALITY_STATUS | APPROVED_WITH_LIMITATIONS |
| ROWS | BTC=6207, ETH=6207; months 68/68; hashes 136/136 [V] |

---

## HARD TESTS [V]

| Test | Result |
|------|--------|
| Inventory / HASH | PASS |
| DUPLICATES / sort / month bounds | PASS |
| Interval catalog | PASS — unique={8}; do not assume forever |
| Missing settlements | PASS — gap=0 |
| Impossible values | PASS |
| Join to DATA-PROV-001 | PASS — rule `close_time_ms >= calc_time`; unmatched=0 |
| LOOKAHEAD / predicted funding | PASS policy — premiumIndex forbidden |
| Publish/observable lag | **[U]** → CONDITIONAL |

---

## FAILURES

None hard.

---

## KNOWABILITY (binding)

1. **Settlement:** `calc_time` is settlement clock.
2. **SIGNAL allowed:** `last_funding_rate` only if `calc_time ≤ decision t`.
3. **SIGNAL forbidden:** `premiumIndex` predicted / next-interval rate; mid-interval accrued invention.
4. **Publish:** Vision monthly pack lag exact ms **[U]** — backtests claiming Vision-ingest parity must not pretend intra-month REST observability from this corpus alone.
5. **Join:** attach print to nearest completed 5m bar with `close_time_ms ≥ calc_time`.

---

## USABLE COVERAGE DATES FOR SPLIT FREEZE

**Do not reshape OHLCV SEAL_LOCK.** Freeze funding usable coverage to the **same open-time windows** as DATA-PROV-001:

| Slice | Open-time bounds (UTC) | Funding prints/symbol |
|-------|------------------------|------------------------|
| RESEARCH | 2021-01-03T04:00 → 2024-05-27T06:15 | 3720 |
| VALIDATION | 2024-05-27T06:20 → 2025-07-14T15:00 | 1240 |
| HISTORICAL HOLDOUT | 2025-07-14T15:05 → 2026-08-31T23:55 | 1240 |
| Pre-research context | before research_open_first | 7 (context only) |

---

## SAFE / UNSAFE FEATURES

**SAFE:** settled `last_funding_rate` after `calc_time`; print-sequence windows (not wall-clock 3/day assumption beyond measured 8h regime).

**UNSAFE:** predicted funding; using unsettle rate; ignoring interval metadata if regime changes later; claiming Vision pack == live REST latency.

---

## REQUIRED REMEDIATION (upgrade path)

1. Measure Vision object publish timestamps vs last `calc_time` per month, **or** ingest REST/WS settlements with receipt-time on eligible host.
2. Re-catalog interval hours if future months ≠ 8.
3. Venue lock + forward window before capital.

---

## Examiner gate

**CLEARED** for provisional funding-edge measurement under PROV rules + settlement gate. Holdout remains LOCKED with OHLCV.
