# DATA VERDICT — DATA-PROV-OI-001
**Issued by:** The Clock  
**Issued UTC:** 2026-09-11T04:39:57Z  
**Audit:** `/workspace/lab/data/DATA-PROV-OI-001/provenance/CLOCK_AUDIT_REPORT.json`

---

## DATA VERDICT: CONDITIONAL

**QUALITY_STATUS:** APPROVED_WITH_LIMITATIONS

Usable for provisional RESEARCH/VALIDATION of OI / funding×OI Catalyst edges (e.g. EDGE-20260911-004 / 006) under snapshot knowability + dedupe/sort join rules.  
**Not** venue marriage. **Not** capital. **SEAL_LOCK not reshaped.**

---

## DATA MANIFEST

| Field | Value |
|-------|-------|
| DATASET_ID | DATA-PROV-OI-001 |
| SOURCE | Binance Vision daily `metrics` UM [V] |
| VENUE | Binance USD-M — PROVISIONAL REFERENCE |
| INSTRUMENT | BTCUSDT (2021-01-01→2026-08-31); ETHUSDT (**2021-12-01→2026-08-31 only**) |
| FREQUENCY | 5m snapshot grid (imperfect — missing stamps exist) |
| TIMESTAMP_DEFINITION | `create_time` = exchange **snapshot** time UTC; aligns to OHLCV **open_time** (bucket start) [V] |
| KNOWN_LATENCY | Receipt/publish lag **[U]** |
| KNOWN_GAPS | BTC missing_stamp_total=604 (68 days); ETH=143 (10 days) — **do not fill** [V] |
| TRANSFORMATIONS | required at use: sort by create_time; dedupe identical within-file buckets (BTC early-2021) [V] |
| QUALITY_STATUS | APPROVED_WITH_LIMITATIONS |
| FILES | BTC 2069 + ETH 1735; hashes **3804/3804** [V] |

---

## HARD TESTS [V]

| Test | Result |
|------|--------|
| Inventory / HASH | PASS |
| Full parse | PASS (with flags) |
| Midnight partition dups | PASS — collision stamps=0 observed |
| Within-file dups | FLAG — BTC identical_dup_buckets=40152 (2021-01→05); conflicting=0; **dedupe required** |
| In-file order | FLAG — some days unsorted; **sort required** |
| OHLCV align | PASS — oi→open orphans=0; OHLCV bars missing OI = gap counts above |
| ETH asymmetry | PASS — 0 ETH files before 2021-12-01 |
| Receipt lag | **[U]** → CONDITIONAL |

Not QUARANTINED: gaps are documented sparse misses, not fabricated; join rules make features well-defined if Examiner abstains on missing stamps.

---

## KNOWABILITY (binding)

1. OI knowable iff `create_time ≤ decision t`.
2. OI is a **level** (last sample), not a sum — despite `sum_open_interest` name.
3. For bar open T / close decision: level at create_time=T is known before close (T < close_time).
4. **Do not** forward-fill missing stamps; abstain or skip ΔOI across gaps.
5. **Do not** invent ETH OI before 2021-12-01.

---

## Catalyst_COMMON_WINDOW (proposed — for joint BTC/ETH)

| Field | Value |
|-------|-------|
| Name | `Catalyst_COMMON_WINDOW` |
| UTC bounds | **2021-12-01T00:00:00Z → 2026-08-31T23:55:00Z** |
| open_time_ms | 1638316800000 → 1788220500000 |
| bar_count_inclusive | 499680 |
| Datasets | DATA-PROV-OI-001 ∩ DATA-PROV-001 (both symbols) |

### Preferred freeze: map existing SEAL_LOCK **clipped** (do not reshape sealed OHLCV files)

| Slice | Clipped open-time bounds (UTC) | Notes |
|-------|--------------------------------|-------|
| RESEARCH | **2021-12-01T00:00 → 2024-05-27T06:15** | Original research start truncated for ETH OI |
| VALIDATION | 2024-05-27T06:20 → 2025-07-14T15:00 | Unchanged vs SEAL_LOCK |
| HOLDOUT | 2025-07-14T15:05 → 2026-08-31T23:55 | Unchanged vs SEAL_LOCK |

### Alt (proposal only): fresh 60/20/20 on common window after warmup 624

| Slice | Bounds (UTC) |
|-------|--------------|
| RESEARCH | 2021-12-03T04:00 → 2024-10-07T20:40 |
| VALIDATION | 2024-10-07T20:45 → 2025-09-19T10:15 |
| HOLDOUT | 2025-09-19T10:20 → 2026-08-31T23:55 |

**Clock recommendation:** Prefer **SEAL_LOCK clipped** for continuity with OHLCV holdout lock. Conductor chooses; Clock forbids silent reshape of sealed OHLCV.

### Coverage classes

| Class | Bounds | Use |
|-------|--------|-----|
| btc_oi_only | 2021-01-01 → 2026-08-31 | BTC OI edges; ETH abstain |
| eth_oi_joint | 2021-12-01 → 2026-08-31 | Joint BTC/ETH OI (+ funding×OI) |
| eth_oi_absent_abstain | 2021-01-01 → 2021-11-30 | Joint edges **must abstain** |

---

## SAFE / UNSAFE

**SAFE:** snapshot OI level after sort+dedupe; ΔOI across consecutive present stamps; joint features inside Catalyst_COMMON_WINDOW.

**UNSAFE:** inventing ETH pre-2021-12; filling gaps; using unsorted/dup rows; treating receipt=create_time as proven; ratio columns unless separately registered.

---

## REQUIRED REMEDIATION

1. Implement mandatory sort+dedupe in Examiner join code (document in TEST record).
2. Gap abstention list from audit missing stamps.
3. Optional: receipt-time on live metrics feed; first-print Vision policy if zips restated.
4. Venue + forward window before capital.

---

## Examiner gate

**CLEARED** for provisional OI / funding×OI measurement inside declared coverage classes with join rules.  
Joint BTC/ETH: **Catalyst_COMMON_WINDOW** (or SEAL_LOCK clipped). ETH pre-2021-12: **BLOCKED**.
