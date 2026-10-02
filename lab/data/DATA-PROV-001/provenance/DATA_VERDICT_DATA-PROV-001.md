# DATA VERDICT — DATA-PROV-001
**Issued by:** The Clock (Data Integrity Sentinel)  
**Issued UTC:** 2026-09-10T23:31:24Z  
**Audit report:** `/workspace/lab/data/DATA-PROV-001/provenance/CLOCK_AUDIT_REPORT.json`  
**Package ceiling:** PROV-MEAS-20260910-001 — provisional RESEARCH/VALIDATION only

---

## DATA VERDICT: CONDITIONAL

**QUALITY_STATUS:** APPROVED_WITH_LIMITATIONS

Usable for provisional RESEARCH TEST / VALIDATION of EDGE-20260910-001 **price-series narrow claim** on this OHLCV series.  
**Not** a venue marriage. **Not** capital-greenlight. Historical holdout remains LOCKED. Future sealed forward window + cross-venue replication still mandatory before capital.

Examiner may proceed on `slices/*_RESEARCH` (then VALIDATION under package rules) after this verdict. Sealed holdout stays closed until Conductor opens holdout protocol.

---

## DATA MANIFEST

| Field | Value |
|-------|-------|
| DATASET_ID | DATA-PROV-001 |
| SOURCE | Binance USD-M klines via `https://www.binance.com/fapi/v1/klines` (fallback; primary `fapi.binance.com` HTTP 451) [V] |
| VENUE | Binance USD-M Futures — **PROVISIONAL REFERENCE only** |
| INSTRUMENT | BTCUSDT, ETHUSDT perpetual |
| START | 2021-01-01 00:00:00 UTC |
| END | 2026-08-31 23:55:00 UTC |
| FREQUENCY | 5m |
| TIMESTAMP_DEFINITION | `open_time_ms` = exchange candle open (UTC epoch ms); `close_time_ms` = open + 299999 ms [V] |
| KNOWN_LATENCY | **[U]** — no receipt-time / ingest latency recorded |
| KNOWN_GAPS | 0 missing bars; 0 off-grid; 0 duplicates (both symbols) [V] |
| TRANSFORMATIONS | dtype casts only; no interpolation/gap-fill/resample [V] |
| QUALITY_STATUS | APPROVED_WITH_LIMITATIONS |
| RAW_ROWS | 595872 each [V] |
| SPLITS | warmup 624 → research 357148 / validation 119049 / holdout 119051 (60/20/20 post-warmup) [V] |

---

## HARD TESTS [V]

| Test | Result |
|------|--------|
| LOOKAHEAD (structural) | PASS — `derived/` empty; close knowable only at `close_time_ms` |
| MISALIGNMENT | PASS — slice concat == raw; BTC/ETH timestamps identical; continuous 300000 ms steps |
| DUPLICATES | PASS — 0 |
| MISSINGNESS | PASS — 0 gaps; close_time == open+299999 |
| IMPOSSIBLE SEQUENCING | PASS — 0 OHLC violations on raw/warmup/research/validation (sealed OHLC not re-inspected by policy) |
| LATE INFORMATION | PASS for documented close-at-decision rule; receipt-time **[U]** |
| CROSS-VENUE CLOCK ERROR | N/A single venue; BTC/ETH clocks identical PASS |
| HASH_VERIFY | PASS — all raw + slices + sealed match expected sha256 |
| SPLIT_SEALING | PASS — recomputed partitions match SEAL_LOCK |

Diagnostic (not hard fail): RESEARCH+VALIDATION bars with \|log(c/o)\|>0.05 — BTC 16, ETH 32.

---

## FAILURES

None that fail hard tests.

---

## LIMITATIONS (why CONDITIONAL, not APPROVED)

1. API path is **fallback** `www.binance.com` after primary 451 — same schema claimed; treat as provisional feed identity caveat [V path / A equivalence].
2. **No receipt-time** — cannot measure ingest latency or late-packet effects [U].
3. **Provisional reference only** — not production venue lock; Mechanic EXECUTABLE / capital still blocked.
4. **Single venue** — cross-venue replication still required before capital (constitutional add) [V].
5. Historical sealed holdout ≠ future sealed forward window [V].
6. Sealed holdout OHLC not re-audited beyond hash/times/counts (policy) [A policy].

---

## SAFE FEATURES (for EDGE-001 narrow claim)

- Completed-bar OHLCV indexed by `open_time_ms`
- Features using bar **t close only at/after `close_time_ms`** (decision at candle close)
- Trailing windows / quantiles using only bars with `close_time_ms` ≤ decision time
- Separate BTC / ETH pipelines on this aligned grid
- Volume columns present (unused by 001 v0)

---

## UNSAFE FEATURES

- Using bar **t close** at decision time = `open_time_ms` of bar t → **LOOKAHEAD**
- Treating taker_buy_* / OF imbalance as verified mechanism evidence → stays **[H]** on OHLCV alone
- Any latency / receipt-time feature → **[U]** / block until instrumented
- Cross-venue lead-lag on this series alone → **[U]** / need second DATA-*
- Optimizing against sealed historical holdout → **holdout contamination** / hard veto
- Claiming venue-executable economics from provisional 7 bps stack → economics remain **[A]**

---

## REQUIRED REMEDIATION (before upgrading beyond CONDITIONAL / before capital)

1. Re-fetch or re-verify from primary fapi endpoint (or second independent source) and compare hashes/timeline when geo allows.
2. Record receipt-time alongside exchange time for live/shadow feeds.
3. Venue-specific rerun under real fees/timestamps before Mechanic EXECUTABLE.
4. Cross-venue replication DATA-* before capital.
5. Future sealed forward window after strategy freeze (historical holdout alone insufficient).

---

## Examiner gate

**CLEARED for provisional measurement** under PROV-MEAS-20260910-001 on RESEARCH (then VALIDATION).  
**HOLD:** sealed historical holdout. **HOLD:** promotion / capital / venue marriage.
