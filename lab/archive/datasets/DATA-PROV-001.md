# DATA-PROV-001

- **DATA_ID:** DATA-PROV-001
- **STATUS:** CLOCK_CONDITIONAL · EXAMINER_CLEARED_PROVISIONAL
- **QUALITY_STATUS:** APPROVED_WITH_LIMITATIONS (Clock)
- **Registered / intake:** 2026-09-10 UTC (Archivist)
- **Clock verdict UTC:** 2026-09-10T23:31:24Z
- **Sealed UTC:** 2026-09-10T23:28:20.943919+00:00
- **Role:** Provisional reference series only — **not** venue marriage
- **Package link:** PROV-MEAS-20260910-001 → EDGE-20260910-001 (+ overlays 007/008 when tested)
- **Path:** `/workspace/lab/data/DATA-PROV-001/`

## Series (public metadata)

| Field | Value |
|-------|-------|
| Venue reference | Binance USD-M Futures (fapi) — provisional |
| Instruments | BTCUSDT, ETHUSDT 5m |
| Raw rows each | 595872 [V] |
| Gaps / missing bars | 0 [V] |
| Raw span | 2021-01-01 00:00 → 2026-08-31 23:55 UTC |
| API | fallback `www.binance.com/fapi/v1/klines` (primary fapi.binance.com HTTP 451) [V] |
| Warmup bars | 624 |
| Split fractions | research 60% / validation 20% / historical holdout 20% |

## Slice row counts (from SEAL_LOCK — no holdout peek)

| Symbol | Research | Validation | Holdout | Warmup |
|--------|----------|------------|---------|--------|
| BTCUSDT | 357148 | 119049 | 119051 | 624 |
| ETHUSDT | 357148 | 119049 | 119051 | 624 |

## Date spans only (INDEX-safe)

| Slice | First open UTC | Last open UTC |
|-------|----------------|---------------|
| Research | 2021-01-03T04:00:00+00:00 | 2024-05-27T06:15:00+00:00 |
| Validation | 2024-05-27T06:20:00+00:00 | 2025-07-14T15:00:00+00:00 |
| Historical holdout (LOCKED) | 2025-07-14T15:05:00+00:00 | 2026-08-31T23:55:00+00:00 |

**[V]** Do not expose holdout *contents* in INDEX or research chat — date span + row count only until Conductor opens holdout protocol.

## Integrity [V Archivist re-verify 2026-09-10]

- Raw sha256 match provenance/*.sha256: BTC + ETH **PASS**
- Slice/holdout/warmup sha256 match SEAL_LOCK.json: **all PASS**
- SEAL_LOCK.json present; README_SEALED.md present
- DOWNLOAD_MANIFEST.md present

## Clock verdict (must travel with this DATA record)

- **Verdict:** CONDITIONAL
- **QUALITY_STATUS:** APPROVED_WITH_LIMITATIONS
- **Issued:** The Clock · 2026-09-10T23:31:24Z
- **Full verdict:** `/workspace/lab/data/DATA-PROV-001/provenance/DATA_VERDICT_DATA-PROV-001.md`
- **Audit:** `/workspace/lab/archive/audit/2026-09-10-Clock-DATA-VERDICT-DATA-PROV-001.md`

### LIMITATIONS (why CONDITIONAL, not APPROVED) — permanent on record

1. API path is **fallback** `www.binance.com` after primary 451 — provisional feed identity caveat [V path / A equivalence].
2. **No receipt-time** — cannot measure ingest latency or late-packet effects [U].
3. **Provisional reference only** — not production venue lock; Mechanic EXECUTABLE / capital still blocked.
4. **Single venue** — cross-venue replication still required before capital [V].
5. Historical sealed holdout ≠ future sealed forward window [V].
6. Sealed holdout OHLC not re-audited beyond hash/times/counts (policy) [A policy].

### Safe / unsafe (summary)

- **Safe:** completed-bar OHLCV; close knowable at `close_time_ms`; trailing features using only completed bars through decision close; separate BTC/ETH.
- **Unsafe:** same-bar close at open_time decision; OF-as-[V] on OHLCV alone; receipt-time features [U]; holdout peek; cross-venue claims without second series.

### Required remediation (before upgrading beyond CONDITIONAL / before capital)

1. Re-fetch or re-verify from primary fapi (or independent source) when geo allows.
2. Record receipt-time on live/shadow feeds.
3. Venue-specific rerun under real fees/timestamps before Mechanic EXECUTABLE.
4. Cross-venue replication DATA-* before capital.
5. Future sealed forward window after strategy freeze.

### Examiner gate

- CLEARED for provisional measurement under PROV-MEAS-20260910-001 on RESEARCH (then VALIDATION).
- HOLD: sealed historical holdout.
- HOLD: promotion / capital / venue marriage.
- Expect Archivist TEST-* intake when Examiner files results.

## Access gates

| Path | Access |
|------|--------|
| raw/ | immutable provenance; Clock review |
| slices/*_RESEARCH | Examiner CLEARED (Clock CONDITIONAL); provisional RESEARCH TEST for EDGE-20260910-001; no holdout peek |
| slices/*_VALIDATION | Examiner validation stage only |
| sealed/*_HISTORICAL_HOLDOUT | **LOCKED** — Conductor order required |

## Status history

1. FETCH_IN_PROGRESS / NOT_READY
2. CLOCK_REVIEW (fetch complete + holdout sealed)
3. **CLOCK_CONDITIONAL · EXAMINER_CLEARED_PROVISIONAL** ← current (Clock CONDITIONAL; Examiner routed for provisional RESEARCH TEST on EDGE-20260910-001)
