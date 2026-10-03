# CLOCK AUDIT — PM-004 × L3-002 JOIN

**Issued UTC:** 2026-09-13T22:05:27Z
**Order:** `/workspace/lab/governance/CLOCK_ORDER_PM004_L3002_JOIN_2026-09-13.md`
**Trade:** FORBIDDEN
**Not Feature / Not READY. F4 not commissioned. Examiner dark.**
**No alpha. No wick. No Φ(z). No PM-003 peek as fill.**

## Draft verdict: CONDITIONAL

Join works under lock B on Sep-12: 851/855 with 4 named day-start edge holes (bar_end < t needs Sep-11 prior bar not in L3-002). 0 lookahead; B_eq_t=0; lag_sec unique ['60.0']. Policy A caveat: would recover 853 with on_minute_A=853 — NOT certified; do not silent-switch. Sep-11 mid=120 and Sep-13 mid=672 are expected out-of-tape misses (L3-002 has 2026-09-12 only). last-as-mid leaks=0. L3 = external predictor NOT oracle/CF. F4 not commissioned; Examiner dark; Not Feature / Not READY.

## Certified rule (PRIMARY): **B**

```
bar_end_ms = open_time_ms + 60000   # == close_time_ms + 1 (Vision close …59999)
S_t = last L3-002 1m close where bar_end_ms < decision_time_ms
require decision_time UTC calendar day == 2026-09-12
asset: BTC→BTCUSDT, ETH→ETHUSDT
L3 role: external predictor — NOT oracle / NOT CF BRTI
```

**Why B over A:** Wave 007 Feature-style lock is `bar_end < t`. L3-001 lineage used
`close_time_ms <= t` (≈ policy A). For Vision ms, A ≡ `bar_end_ms <= t` and lands every
on-minute Kalshi `decision_time` on `bar_end == t`. Prefer certifying **B**; report **A**
as caveat count only — do not silent-switch.

## Policy A (caveat ONLY — not certified)

```
S_t_A = last L3-002 1m close where bar_end_ms <= decision_time_ms
     (= close_time_ms <= decision_time_ms on this Vision layout)
```

## Mid-only gate

| metric | N |
|--------|--:|
| checkpoints total | 1845 |
| mid (bid/ask valid) | 1647 |
| last (excluded) | 198 |
| mid rejected bid/ask | 0 |
| **last-as-mid leaks** | **0** |
| mid decision_time on-minute | 1647/1647 |

### Mid by calendar day

| day | N_mid | note |
|-----|------:|------|
| 2026-09-11 | 120 | expected out-of-tape vs L3-002 |
| 2026-09-12 | 855 | joinable day |
| 2026-09-13 | 672 | expected out-of-tape (Vision 404) |

## Coverage — Sep-12-only mid (certified universe)

**Totals B:** N_pm004_mid=855 · N_with_L3_B=851 · miss_L3=4 · lookahead=0 · B_eq_t=0
**Lag_sec_B:** {'60.0': 851}
**Totals A caveat:** N_with_L3_A=853 · miss_A=2 · on_minute_A=853 · lookahead_A=0

| asset | rem | N_pm004_mid | N_with_L3_B | miss_L3 | lookahead | N_with_L3_A (caveat) | on_minute_A |
|-------|----:|------------:|------------:|--------:|----------:|---------------------:|------------:|
| BTC | 840 | 96 | 95 | 1 | 0 | 96 | 96 |
| BTC | 600 | 96 | 96 | 0 | 0 | 96 | 96 |
| BTC | 300 | 96 | 96 | 0 | 0 | 96 | 96 |
| BTC | 60 | 96 | 96 | 0 | 0 | 96 | 96 |
| BTC | 0 | 43 | 42 | 1 | 0 | 42 | 42 |
| ETH | 840 | 96 | 95 | 1 | 0 | 96 | 96 |
| ETH | 600 | 96 | 96 | 0 | 0 | 96 | 96 |
| ETH | 300 | 96 | 96 | 0 | 0 | 96 | 96 |
| ETH | 60 | 95 | 95 | 0 | 0 | 95 | 95 |
| ETH | 0 | 45 | 44 | 1 | 0 | 44 | 44 |

### Named Sep-12 edge misses under B (4)

- `BTC` `2026-09-12T00:00:00Z` rem=0 `KXBTC15M-26SEP112000-00` — no L3-002 bar with bar_end_ms < decision_time (day-start under lock B; Sep-11 prior bar not in L3-002)
- `ETH` `2026-09-12T00:00:00Z` rem=0 `KXETH15M-26SEP112000-00` — no L3-002 bar with bar_end_ms < decision_time (day-start under lock B; Sep-11 prior bar not in L3-002)
- `BTC` `2026-09-12T00:01:00Z` rem=840 `KXBTC15M-26SEP112015-15` — no L3-002 bar with bar_end_ms < decision_time (day-start under lock B; Sep-11 prior bar not in L3-002)
- `ETH` `2026-09-12T00:01:00Z` rem=840 `KXETH15M-26SEP112015-15` — no L3-002 bar with bar_end_ms < decision_time (day-start under lock B; Sep-11 prior bar not in L3-002)

### Named Sep-12 edge misses under A caveat (2)

- `BTC` `2026-09-12T00:00:00Z` rem=0 `KXBTC15M-26SEP112000-00` — no L3-002 bar with bar_end_ms <= decision_time (exact Sep-12 00:00Z; no prior bar in tape)
- `ETH` `2026-09-12T00:00:00Z` rem=0 `KXETH15M-26SEP112000-00` — no L3-002 bar with bar_end_ms <= decision_time (exact Sep-12 00:00Z; no prior bar in tape)

## Coverage — all mid (calendar-gated)

Non-Sep-12 rows count as miss_L3 (expected out-of-tape).

**Totals B:** N=1647 · with_L3_B=851 · miss=796 · lookahead=0

| asset | rem | N_pm004_mid | N_with_L3_B | miss_L3 | lookahead | N_with_L3_A (caveat) | on_minute_A |
|-------|----:|------------:|------------:|--------:|----------:|---------------------:|------------:|
| BTC | 840 | 184 | 95 | 89 | 0 | 96 | 96 |
| BTC | 600 | 184 | 96 | 88 | 0 | 96 | 96 |
| BTC | 300 | 184 | 96 | 88 | 0 | 96 | 96 |
| BTC | 60 | 182 | 96 | 86 | 0 | 96 | 96 |
| BTC | 0 | 90 | 42 | 48 | 0 | 42 | 42 |
| ETH | 840 | 185 | 95 | 90 | 0 | 96 | 96 |
| ETH | 600 | 185 | 96 | 89 | 0 | 96 | 96 |
| ETH | 300 | 185 | 96 | 89 | 0 | 96 | 96 |
| ETH | 60 | 180 | 95 | 85 | 0 | 95 | 95 |
| ETH | 0 | 88 | 44 | 44 | 0 | 44 | 44 |

## Out-of-tape overlap (expected misses)

| slice | N_mid | certified with_L3_B |
|-------|------:|--------------------:|
| Sep-11 | 120 | 0 (before L3-002) |
| Sep-12 | 855 | 851 |
| Sep-13 | 672 | 0 (no L3-002 Sep-13) |

**Ungated Sep-13 counterfactual (NOT certified):** hit=672 miss=0 lag_sec range [60.0, 67500.0] — stale last-bar use forbidden.

## L3-002 tape

| symbol | n_bars | first_open_utc | last_bar_end_utc |
|--------|-------:|----------------|------------------|
| BTCUSDT | 1440 | 2026-09-12T00:00:00Z | 2026-09-13T00:00:00Z |
| ETHUSDT | 1440 | 2026-09-12T00:00:00Z | 2026-09-13T00:00:00Z |

## Forbidden checks

| check | result |
|-------|--------|
| last-as-mid leaks | 0 |
| lookahead under B | 0 (Sep-12) / 0 (all gated) |
| B_eq_t (must be 0 under B) | 0 |
| oracle/CF claim | false |
| wick work | false |
| F4 commission as CLEARED Feature | false |
| PM-003 peek as fill | false |

## State

Inventory for later F4 only — **F4 not commissioned**; Examiner dark; Trade FORBIDDEN.

## Artifacts

- `/workspace/lab/data/DATA-PROV-PM-004/provenance/CLOCK_AUDIT_PM004_L3002_JOIN.json`
- `/workspace/lab/data/DATA-PROV-PM-004/provenance/CLOCK_AUDIT_PM004_L3002_JOIN.md`
- `/workspace/lab/data/DATA-PROV-PM-004/provenance/DATA_VERDICT_PM004_L3002_JOIN.md`
- `/workspace/lab/data/DATA-PROV-PM-004/provenance/clock_audit_PM004_L3002_JOIN.py`
