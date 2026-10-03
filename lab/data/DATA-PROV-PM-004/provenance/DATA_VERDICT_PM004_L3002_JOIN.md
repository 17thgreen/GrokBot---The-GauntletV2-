# DATA VERDICT — PM-004 × L3-002 JOIN

**Issued by:** The Clock
**Issued UTC:** 2026-09-13T22:05:54Z
**Authority:** `/workspace/lab/governance/CLOCK_ORDER_PM004_L3002_JOIN_2026-09-13.md`
**Trade:** FORBIDDEN
**Not Feature / Not READY. F4 not commissioned. Examiner dark.**

---

## DATA VERDICT: CONDITIONAL

**VERDICT_SCOPE:** join_only
**Certified rule:** **B** (`bar_end_ms < decision_time_ms`)
**Policy A:** (`bar_end_ms <= decision_time_ms` / `close_time_ms <= t`) — caveat count ONLY; not certified
**bar_end_ms:** `open_time_ms + 60000` (== `close_time_ms + 1`; Vision close …59999)
**Layer:** PM-004 Kalshi 15m mid checkpoints × L3-002 Binance Vision 1m (BTCUSDT/ETHUSDT) **2026-09-12 only**
**L3 role:** external predictor — **NOT** settlement oracle / **NOT** CF BRTI
**THIS JOIN:** completed-bar L3 close at decision_time under lock B (calendar-gated to Sep-12)
**NOT:** Feature · READY · alpha · Examiner · F4 wick-gate · Φ(z) · wick histogram · PM-003 fill · invented quotes

## Rationale

Join works under lock B on Sep-12: 851/855 with 4 named day-start edge holes (bar_end < t needs Sep-11 prior bar not in L3-002). 0 lookahead; B_eq_t=0; lag_sec unique ['60.0']. Policy A caveat: would recover 853 with on_minute_A=853 — NOT certified; do not silent-switch. Sep-11 mid=120 and Sep-13 mid=672 are expected out-of-tape misses (L3-002 has 2026-09-12 only). last-as-mid leaks=0. L3 = external predictor NOT oracle/CF. F4 not commissioned; Examiner dark; Not Feature / Not READY.

## Coverage under lock B — Sep-12 mid

| asset | rem | N_pm004_mid | N_with_L3_B | miss_L3 | lookahead |
|-------|----:|------------:|------------:|--------:|----------:|
| BTC | 840 | 96 | 95 | 1 | 0 |
| BTC | 600 | 96 | 96 | 0 | 0 |
| BTC | 300 | 96 | 96 | 0 | 0 |
| BTC | 60 | 96 | 96 | 0 | 0 |
| BTC | 0 | 43 | 42 | 1 | 0 |
| ETH | 840 | 96 | 95 | 1 | 0 |
| ETH | 600 | 96 | 96 | 0 | 0 |
| ETH | 300 | 96 | 96 | 0 | 0 |
| ETH | 60 | 95 | 95 | 0 | 0 |
| ETH | 0 | 45 | 44 | 1 | 0 |

**Sep-12 totals:** 851/855 under B · miss=4 · lookahead=0 · B_eq_t=0
**Lag_sec_B unique:** ['60.0'] (expect 60s on on-minute t under B)

### Named Sep-12 edge misses (B)

- `BTC` `2026-09-12T00:00:00Z` rem=0 `KXBTC15M-26SEP112000-00`
- `ETH` `2026-09-12T00:00:00Z` rem=0 `KXETH15M-26SEP112000-00`
- `BTC` `2026-09-12T00:01:00Z` rem=840 `KXBTC15M-26SEP112015-15`
- `ETH` `2026-09-12T00:01:00Z` rem=840 `KXETH15M-26SEP112015-15`

## Out-of-tape (expected)

| day | N_mid | certified join |
|-----|------:|----------------|
| 2026-09-11 | 120 | expected miss (before L3-002) |
| 2026-09-12 | 855 | 851/855 under B |
| 2026-09-13 | 672 | expected miss (L3-002 has no Sep-13; Vision 404 at inventory) |

Ungated Sep-13 stale-hit of last Sep-12 bar is **NOT certified** (counterfactual hit=672, lag up to 67500.0s).

## Policy A caveat (NOT certified)

| measure | Sep-12 count |
|---------|-------------:|
| N_with_L3_A | 853 |
| miss_L3_A | 2 |
| on_minute_A (bar_end == t) | 853 |
| lookahead_A | 0 |

Do **not** silent-switch from B to A. On-minute coincidence under A is the same knowability class previously caveat'd on CB×PM-003.

## Mid-only / forbidden

| check | value |
|-------|------:|
| mid (valid bid/ask) | 1647 |
| last excluded | 198 |
| last-as-mid leaks | **0** |
| lookahead B (Sep-12) | **0** |
| oracle/CF claim | false |
| wick / F4 commission / Examiner Δ | false |

## SAFE / UNSAFE

### SAFE (under this verdict, lock B)

- Using L3-002 completed-bar closes with `bar_end_ms < decision_time_ms` on Sep-12 mid rows only.
- Naming Sep-11/Sep-13 holes as expected out-of-tape.
- Counting Policy A on-minute as caveat only.
- Inventory for a later signed F4 order — **F4 not commissioned here**.

### UNSAFE

- Feature-scoring Policy A or silent-switching B→A.
- Treating Binance L3 as CF BRTI / Kalshi settlement oracle.
- Filling Sep-13 (or Sep-11) with stale Sep-12 last bar / PM-003 peek.
- last-as-mid; incomplete-bar close; wick histogram; Examiner Δ; trade.
- Declaring Feature / READY / F4 CLEARED from this join alone.

## REQUIRED REMEDIATION

1. Accept named Sep-12 day-start edge misses under lock B (4 rows at 00:00/00:01), or extend L3 tape with Sep-11 last minutes if those contracts must join — **not** by peeking PM-003 for fill.
2. Keep Policy A on-minute as caveat-count only; do not Feature-score A.
3. Sep-13 Vision daily zip when HTTP 200 — separate L3 provenance + Clock join.
4. F4 remains uncommissioned until a signed Governor/Feature order.

## Blockers

- (none that REJECT; see caveats above)

## State

**Inventory for later F4 only — F4 not commissioned; Examiner dark; Trade FORBIDDEN.**

## Artifacts

- `/workspace/lab/data/DATA-PROV-PM-004/provenance/clock_audit_PM004_L3002_JOIN.py`
- `/workspace/lab/data/DATA-PROV-PM-004/provenance/CLOCK_AUDIT_PM004_L3002_JOIN.json`
- `/workspace/lab/data/DATA-PROV-PM-004/provenance/CLOCK_AUDIT_PM004_L3002_JOIN.md`
- `/workspace/lab/data/DATA-PROV-PM-004/provenance/DATA_VERDICT_PM004_L3002_JOIN.md`

---

## Clock seal

**DATA VERDICT: CONDITIONAL** (join only, lock B) — sealed by The Clock 2026-09-13T22:05:54Z.  
Sep-12: 851/855 mid×L3; 4 named day-start holes. Sep-13 uncovered (no L3-002).  
L3 = external predictor, not oracle. F4 not commissioned. Examiner dark. Trade FORBIDDEN.
