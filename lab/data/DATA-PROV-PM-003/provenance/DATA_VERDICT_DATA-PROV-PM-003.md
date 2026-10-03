# DATA VERDICT — DATA-PROV-PM-003
**Issued by:** The Clock  
**Issued UTC:** 2026-09-11T23:03:13Z  
**Audit:** `/workspace/lab/data/DATA-PROV-PM-003/provenance/CLOCK_AUDIT_REPORT.json`  
**Parent:** DATA-PROV-PM-001 · **Sibling excluded:** DATA-PROV-PM-002 (not holdout)

---

## DATA VERDICT: CONDITIONAL

**QUALITY_STATUS:** APPROVED_WITH_LIMITATIONS  
**Universe:** remaining Kalshi 15m only — **1208 contracts / 6040 rows**  
**overlap_count vs PM-002:** **0** [V]  
**Not** sealed holdout · **Not** union with PM-002 · **Not** Poly · **Not** books · **Not** independent oracle

Same primary mid freeze pattern as PM-002 Kalshi, applied to **this 1208 only**.

---

## DATA MANIFEST

| Field | Value |
|-------|-------|
| DATASET_ID | DATA-PROV-PM-003 |
| SOURCE | Kalshi public batch `GET /markets/candlesticks` (+ resume per-ticker) — no secrets [V] |
| VENUE | KALSHI only |
| INSTRUMENT | BTC/ETH 15m binaries from PM-001 minus PM-002 coverage |
| START/END | opens ~2026-09-04T20:45Z → 2026-09-11T20:15Z |
| SAMPLING | rem ∈ {0,60,300,600,840}; T−14m substitutes exact OPEN |
| TIMESTAMP_DEFINITION | candle close end = decision_time; obs_lag=0 [V] |
| TRANSFORMATIONS | mid if bid>0 & ask>0 & bid≤ask else last; never PM-001 terminals |
| QUALITY_STATUS | APPROVED_WITH_LIMITATIONS |
| ROWS | 6040; SHA256 `90e38c2f23e224def13db05924f6470a1e738778882f6b0cc17ed708b3143765` [V] |

---

## HARD TESTS [V]

| Test | Result |
|------|--------|
| HASH / counts / strata 604+604 | PASS |
| Zero overlap PM-002 (vni ∩ = 0, cid ∩ = 0) | PASS |
| ⊆ PM-001 Kalshi; PM-002+PM-003=1328 | PASS |
| Temporal / lag / rem set / 5 rows | PASS |
| Mid validity; last-fallback only T−1m/T−0 | PASS |
| T−0 near-deg 1206/1208 (+1 null ip) | PASS (measured → BLOCK T−0) |
| Not terminal-copy; raw candle OK | PASS |
| Batch ≡ per-ticker OHLC semantics | PASS |
| Not books/oracle/sealed/Poly/union-holdout | PASS |

---

## CLEARED (THIS 1208 only)

| Cell | Status |
|------|--------|
| `KALSHI\|15m\|BTC\|T-14m\|mid` | **CLEARED** — exclude near-deg (0 at T−14m) |
| `KALSHI\|15m\|ETH\|T-14m\|mid` | **CLEARED** |
| `KALSHI\|15m\|BTC\|T-10m\|mid` | **CLEARED** — near-deg 0 |
| `KALSHI\|15m\|ETH\|T-10m\|mid` | **CLEARED** |
| `KALSHI\|15m\|BTC\|T-5m\|mid` | **CLEARED** — exclude near-deg (94/1208 overall at T−5m) |
| `KALSHI\|15m\|ETH\|T-5m\|mid` | **CLEARED** — same |
| `KALSHI\|15m\|{BTC,ETH}\|T-1m\|mid` | **CLEARED_WITH_STRONG_CAVEAT** — high near-deg; exclude 114 last-fallback |

**Primary Examiner freeze (preferred):** T−14m / T−10m / T−5m mid, asset-split, near-deg & last-fallback excluded.

---

## BLOCKED

| Item | Status |
|------|--------|
| T−0 any | **BLOCKED** (1206/1208 near-deg + 1 null) |
| T−1m / T−0 last-fallback for mid claims | **BLOCKED** |
| Books / L2 | **BLOCKED** |
| Independent oracle | **BLOCKED** |
| Sealed holdout | **BLOCKED** |
| Union PM-002 + PM-003 as holdout | **BLOCKED** |
| Poly under this label | **BLOCKED** (not fetched) |
| Exact OPEN rem=900 | **BLOCKED** |
| PM-001 terminals as m_t | **BLOCKED** |
| Pre-cutoff historical | **BLOCKED_QUARANTINE** |
| Silent include of PM-002 120 under this label | **BLOCKED** |

---

## Construction deltas vs PM-002 Kalshi [V]

1. Primary fetch = **batch** `/markets/candlesticks` (PM-002 was per-ticker series route); OHLC/`end_period_ts` semantics match.
2. T−0 near-deg rate 0.9983 (not exactly 1.0); T−5m near-deg 94/1208 vs PM-002 15/120 — still exclude near-deg; primary freeze unchanged.

---

## USABLE COVERAGE FREEZE

**This 1208 only.** Do not reuse full PM-001 windows; do not union with PM-002 as holdout.

| Stratum | n | open_min → open_max (UTC) |
|---------|--:|---------------------------|
| KALSHI\|BTC\|15m | 604 | 2026-09-04T20:45 → 2026-09-11T20:15 |
| KALSHI\|ETH\|15m | 604 | 2026-09-04T20:45 → 2026-09-11T20:15 |

Detail: `/workspace/lab/data/DATA-PROV-PM-003/provenance/USABLE_COVERAGE_DATA-PROV-PM-003.md`

---

## Examiner gate

Conductor may route market-baseline cells on CLEARED primary mid checkpoints for **PM-003 1208** after freeze. PM-002 USED_RESEARCH 240 remains a separate slice — not this label's holdout.
