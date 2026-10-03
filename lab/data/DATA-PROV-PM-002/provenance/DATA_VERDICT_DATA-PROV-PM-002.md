# DATA VERDICT — DATA-PROV-PM-002
**Issued by:** The Clock  
**Issued UTC:** 2026-09-11T21:27:41Z  
**Audit:** `/workspace/lab/data/DATA-PROV-PM-002/provenance/CLOCK_AUDIT_REPORT.json`  
**Parent:** DATA-PROV-PM-001 (label CONDITIONAL unchanged)

---

## DATA VERDICT: CONDITIONAL

**QUALITY_STATUS:** APPROVED_WITH_LIMITATIONS  
**Bounded slice only:** 240 contracts / 1140 checkpoints — **not** full 3824, **not** sealed holdout  
**Books:** still ABSENT · **Independent oracle:** still UNTESTED  
**Trading:** FORBIDDEN

Integrity of construction PASS [V]. Market-relative Examiner may proceed **only** on CLEARED cells below (frozen before run).

---

## DATA MANIFEST

| Field | Value |
|-------|-------|
| DATASET_ID | DATA-PROV-PM-002 |
| SOURCE | Kalshi public 1m candlesticks; Polymarket CLOB prices-history — no secrets [V] |
| VENUE | KALSHI · POLYMARKET_GLOBAL (non-equivalent; no unlabeled pool) |
| INSTRUMENT | Parent PROV-* short-window BTC/ETH binaries (stride sample) |
| START/END | Kalshi opens ~2026-09-04T23:30Z→2026-09-11T20:30Z; Poly ~2026-09-08T17:00Z→2026-09-11T20:35Z |
| SAMPLING | Declared remaining-time checkpoints; T−14m/T−4m substitute exact OPEN |
| TIMESTAMP_DEFINITION | Kalshi: candle close end_period_ts = decision_time (lag 0). Poly: last print obs_time ≤ decision_time (lag mean~43.6s, max 52s) |
| KNOWN_LATENCY | Kalshi 0s; Poly last stale vs decision_time [V] |
| TRANSFORMATIONS | mid=(bid+ask)/2 if both>0 & bid≤ask else last; never PM-001 terminal fields |
| QUALITY_STATUS | APPROVED_WITH_LIMITATIONS |
| ROWS | 1140 checkpoints; SHA256 `affbbbd0b07c765d3f7c0af5e6b23564d3973ec82f27fe7d48b84bc4ded89dc0` [V] |

---

## HARD TESTS [V] — all PASS

HASH · join ⊆ PM-001 · decision∈[OPEN,CLOSE] · not terminal-copy · Kalshi/Poly timestamp semantics · mid validity · T−0 degeneracy measured · no fabricated OPEN · not books · not oracle · post-cutoff live only · not 3824 · not sealed · no dups · no post-CLOSE · venues non-pooled.

---

## CLEARED (market-relative path)

| Cell | Method | Gate |
|------|--------|------|
| `KALSHI\|15m\|BTC\|T-14m\|mid` | mid | **CLEARED** — exclude near-deg (≤0.02/≥0.98) |
| `KALSHI\|15m\|ETH\|T-14m\|mid` | mid | **CLEARED** — same |
| `KALSHI\|15m\|BTC\|T-10m\|mid` | mid | **CLEARED** |
| `KALSHI\|15m\|ETH\|T-10m\|mid` | mid | **CLEARED** |
| `KALSHI\|15m\|BTC\|T-5m\|mid` | mid | **CLEARED** — exclude near-deg (15/120 overall at T−5m) |
| `KALSHI\|15m\|ETH\|T-5m\|mid` | mid | **CLEARED** — same |
| `KALSHI\|15m\|BTC\|T-1m\|mid` | mid | **CLEARED_WITH_STRONG_CAVEAT** — high near-deg; exclude last-fallback companions |
| `KALSHI\|15m\|ETH\|T-1m\|mid` | mid | **CLEARED_WITH_STRONG_CAVEAT** — same |

| Cell | Method | Gate |
|------|--------|------|
| `POLYMARKET_GLOBAL\|{5m,15m}\|{BTC,ETH}\|{T-14m,T-10m,T-5m,T-4m,T-3m,T-1m}\|last` | last | **CLEARED_WEAKER_LAST_PRINT** — NOT mid; lag caveat; separate strata |

**Primary freeze for Examiner (preferred):** Kalshi mid @ **T−14m / T−10m / T−5m** only, asset-split, near-deg excluded, last-fallback excluded.

**Weaker optional:** Poly last-print @ non-T−0 checkpoints — score as last-print benchmark only; never as mid.

---

## BLOCKED

| Item | Status |
|------|--------|
| `KALSHI\|15m\|*\|T-0\|any` | **BLOCKED** — 120/120 near 0/1 |
| `KALSHI\|15m\|*\|T-1m\|last_fallback` | **BLOCKED** for mid claims |
| `POLYMARKET_GLOBAL\|*\|*\|T-0\|last` | **BLOCKED** for forecast cells |
| `POLYMARKET_GLOBAL\|*\|*\|*\|mid` | **BLOCKED** — bid/ask null; no invented quotes |
| Books / L2 | **BLOCKED** — ABSENT |
| Independent oracle | **BLOCKED** — UNTESTED (no Binance substitute) |
| Full 3824 / sealed holdout | **BLOCKED** |
| Unlabeled Kalshi+Poly pool | **BLOCKED** |
| Pre-cutoff Kalshi `/historical` candle coverage | **BLOCKED_QUARANTINE** — UNTESTED |
| Exact OPEN rem=900 / 5m-rem=300 | **BLOCKED** — use T−14m/T−4m |
| PM-001 `LAST_PRICE_DOLLARS` / `OUTCOME_PRICES` as m_t | **BLOCKED** |

---

## KNOWABILITY (binding)

1. Kalshi mid at decision_time = closed 1m candle end — knowable at minute end, not earlier in that minute.
2. Poly last at decision_time is last print ≤ decision_time; typically ~20–52s stale — **last-print**, not contemporaneous mid.
3. Method mid ≠ method last — never mix in one unlabeled cell.
4. Parent PM-001 RESOLUTION still only at/after RESOLVE_TIME for labels.

---

## USABLE COVERAGE FREEZE (240 only)

Do **not** reuse full PM-001 label windows for this m_t path.

| Stratum | n | open_min → open_max (UTC) | remaining_sec present |
|---------|--:|---------------------------|------------------------|
| KALSHI\|BTC\|15m | 60 | 2026-09-04T23:30 → 2026-09-11T20:30 | 0,60,300,600,840 |
| KALSHI\|ETH\|15m | 60 | 2026-09-04T23:30 → 2026-09-11T20:30 | 0,60,300,600,840 |
| POLY\|BTC\|5m | 30 | 2026-09-08T17:05 → 2026-09-11T20:35 | 0,60,180,240 |
| POLY\|ETH\|5m | 30 | 2026-09-08T17:15 → 2026-09-11T20:35 | 0,60,180,240 |
| POLY\|BTC\|15m | 30 | 2026-09-08T17:00 → 2026-09-11T20:15 | 0,60,300,600,840 |
| POLY\|ETH\|15m | 30 | 2026-09-08T17:00 → 2026-09-11T20:15 | 0,60,300,600,840 |

Detail: `/workspace/lab/data/DATA-PROV-PM-002/provenance/USABLE_COVERAGE_DATA-PROV-PM-002.md`

---

## REQUIRED REMEDIATION

1. For mid-relative Poly: need bid/ask (book or quote) DATA-* — do not invent.
2. For T−0 / late-window cells: redesign or exclude.
3. Pre-cutoff Kalshi: exercise `/historical` route + Clock before claiming older coverage.
4. Optional expand beyond 240 with same construction + re-Clock.
5. Independent oracle L2 still separate.

---

## Examiner gate (Clock-owned)

- PM-001 market-relative route: **partially unlocked** only for CLEARED cells above after Conductor freezes horizon/asset/offset/method.
- Label-only PM-001 path unchanged.
- No Examiner scores invented by Clock.
