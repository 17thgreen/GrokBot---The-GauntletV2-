# DATA VERDICT — DATA-PROV-PM-001
**Issued by:** The Clock  
**Issued UTC:** 2026-09-11T20:53:10Z  
**Audit:** `/workspace/lab/data/DATA-PROV-PM-001/provenance/CLOCK_AUDIT_REPORT.json`

---

## DATA VERDICT: CONDITIONAL

**QUALITY_STATUS:** APPROVED_WITH_LIMITATIONS  
**Label-only Examiner route:** CLEARED under gates below  
**Books / mid-path / independent oracle:** **NOT APPROVED** (UNTESTED_BLOCKED)  
**Trading:** FORBIDDEN

Settlement labels are **VENUE_DECLARED [V]**; independent CF BRTI / Chainlink TWAP replay remains **UNTESTED [U]** → cannot APPROVE.

---

## DATA MANIFEST

| Field | Value |
|-------|-------|
| DATASET_ID | DATA-PROV-PM-001 |
| SOURCE | Kalshi public trade-api (elections host) + Polymarket Gamma public — **no secrets** [V] |
| VENUES | `KALSHI` · `POLYMARKET_GLOBAL` — **not equivalent**; no unlabeled pooling |
| INSTRUMENTS | Short-window BTC/ETH binaries (Kalshi 15m; Poly 5m+15m) |
| START/END | Kalshi ~2026-09-04→2026-09-11; Poly ~2026-09-08→2026-09-11 (cap) |
| FREQUENCY | Contract windows 5m / 15m |
| TIMESTAMP_DEFINITION | OPEN/CLOSE = window bounds; RESOLVE_TIME = venue settlement publish proxy |
| KNOWN_LATENCY | Settlement publish lag after CLOSE measured; label knowable at RESOLVE_TIME [V] |
| KNOWN_GAPS | Poly shorter by design; no historical books [V] |
| TRANSFORMATIONS | Normalized BINARY_CONTRACT NDJSON; provisional PROV-* IDs |
| QUALITY_STATUS | APPROVED_WITH_LIMITATIONS |
| ROWS | Kalshi 1328 + Poly 2496 = 3824; CHECKSUMS 79/79 [V] |

---

## HARD TESTS [V]

| Test | Result |
|------|--------|
| HASH_VERIFY | PASS |
| SCHEMA / unique IDs / adapters | PASS |
| RESOLUTION YES/NO only | PASS (1889/1935); Poly Up/Down map OK |
| TEMPORAL OPEN<CLOSE≤RESOLVE; window lengths | PASS (3824/3824) |
| DUPLICATES | PASS |
| CROSS-VENUE non-equivalence | PASS (pooling forbidden without strata) |
| BOOKS/PRICES completeness | PASS as absence check — books ABSENT; approve_books=False |
| ORACLE raw series attached | PASS as absence — independent replay UNTESTED |

---

## KNOWABILITY (binding)

1. **RESOLUTION** usable only if decision `t ≥ RESOLVE_TIME` (conservative). Earlier use = **LOOKAHEAD**.
2. CLOSE_TIME ≠ label publish time — settlement lag can be seconds to hours (see audit lag buckets).
3. `LAST_PRICE_DOLLARS` / `OUTCOME_PRICES` are **terminal** — not decision-time \(m_t\).
4. Oracle mapping documented; settlement source = **VENUE_DECLARED**; independent recompute **UNTESTED**.

---

## FAILURES

None that fail hard integrity of venue labels.

---

## SAFE FEATURES (CONDITIONAL label-only)

- Venue-declared YES/NO after RESOLVE_TIME
- Per-adapter strata (Kalshi vs Poly; BTC vs ETH; 5m vs 15m)
- Schedule metadata OPEN/CLOSE/WINDOW/ASSET without label leak

## UNSAFE / BLOCKED

- RESOLUTION before RESOLVE_TIME
- Terminal prices as mid paths / books
- Pooling venues without adapter strata
- Claiming independent oracle verification
- Trading / execution
- Treating sample as sealed holdout

---

## USABLE COVERAGE (freeze for label-only Examiner)

| Stratum | n | OPEN ≥ | CLOSE ≤ |
|---------|--:|--------|---------|
| KALSHI\|BTC\|15m | 664 | 2026-09-04T20:45:00Z | 2026-09-11T20:45:00Z |
| KALSHI\|ETH\|15m | 664 | 2026-09-04T20:45:00Z | 2026-09-11T20:45:00Z |
| POLYMARKET_GLOBAL\|BTC\|5m | 938 | 2026-09-08T14:30:00Z | 2026-09-11T20:40:00Z |
| POLYMARKET_GLOBAL\|ETH\|5m | 935 | 2026-09-08T14:40:00Z | 2026-09-11T20:40:00Z |
| POLYMARKET_GLOBAL\|BTC\|15m | 312 | 2026-09-08T14:30:00Z | 2026-09-11T20:30:00Z |
| POLYMARKET_GLOBAL\|ETH\|15m | 311 | 2026-09-08T14:30:00Z | 2026-09-11T20:30:00Z |

**Mid/path:** UNTESTED_BLOCKED  
**Independent oracle:** UNTESTED_BLOCKED  
Detail: `/workspace/lab/data/DATA-PROV-PM-001/provenance/USABLE_COVERAGE_DATA-PROV-PM-001.md`

---

## REQUIRED REMEDIATION (beyond CONDITIONAL)

1. Attach independently replayable CF BRTI/ETHUSDRTI + Chainlink TWAP history → separate L2 Clock
2. Optional separate DATA-* for CLOB prices-history / trades for \(m_t\)
3. Archivist non-provisional CONTRACT_IDs for any pilot freeze
4. Optional extend Poly span toward Kalshi ~7d
5. Do not promote this sample to sealed holdout without new seal protocol

---

## Examiner gate

| Route | Gate |
|-------|------|
| Label-only calibration / scoring by venue strata | **CLEARED** under CONDITIONAL |
| Mid/path microstructure | **BLOCKED** |
| Oracle-verified settlement | **BLOCKED** until L2 |
| Trading | **FORBIDDEN** |
