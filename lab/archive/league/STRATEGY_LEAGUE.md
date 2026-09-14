# STRATEGY LEAGUE — active table
**Opened:** 2026-09-11 UTC  
**Arena:** DATA-PROV-PM-003 Kalshi 15m BTC/ETH · Clock CONDITIONAL · TEST-20260911-007  
**Benchmark:** venue mid \(m_t\) on frozen cells — not 50/50  
**Trade authorization:** NONE  
**Oracle tape:** DATA-PROV-CF-001 CLEARED. Map 2 vs mid: TEST-20260913-001 fail on frozen headline.

States: HYPOTHESIS | RESEARCH | CHALLENGER | CHAMPION | INACTIVE | RETIRED | CEMETERY  
Incumbent benchmark is **not** a Gauntlet strategy. A challenger must beat \(m_t\) on the **same six cells** (Brier / logloss Δ, sign: model − market, negative = skill).

## Incumbent — MARKET_IMPLIED

| Field | Value |
|-------|-------|
| STRATEGY_ID | **MKT-KALSHI-15M-MID** |
| NAME | Kalshi 15m mid \(m_t\) (no model) |
| STATE | **INCUMBENT_BENCHMARK** (not CHAMPION-of-strategy) |
| TEST | TEST-20260911-007 |
| DATA | DATA-PROV-PM-003 (1208; not PM-002 union) |
| Cells | `KALSHI\|15m\|{BTC,ETH}|{T-14m,T-10m,T-5m}|mid` |
| N | 604 / 604 / 604 / 604 / 569 / 545 |
| Brier_market | 0.2347 / 0.2329 / 0.1982 / 0.1982 / 0.1413 / 0.1342 |
| LogLoss_market | 0.6626 / 0.6589 / 0.5820 / 0.5796 / 0.4347 / 0.4158 |
| ECE | 0.0346 / 0.0474 / 0.0415 / 0.0229 / 0.0243 / 0.0329 |
| Model metrics | UNTESTED (this row *is* the market) |
| Trading | FORBIDDEN |

Thin T−14m bins [0.70,0.98) remain UNTESTED. Do not pool.

## Challengers

F4 closed: TEST-20260914-001 REDUNDANT / FAIL-INSUFFICIENT (N_wick BTC 12 / ETH 10 < 80; Sep-12 PM-004; lock B). No cemetery. No θ/W/λ retune.

Wave 007 closed: CB-VEL TEST-20260913-005 REDUNDANT / FAIL-INSUFFICIENT (both T-14m Δ>0; speak 604/604; Policy B). Wave 008 CLOSED: W2-D TEST-20260913-006 REDUNDANT / FAIL-INSUFFICIENT (BTC both Δ≥0; ETH ΔLogLoss≥0; rem=180). No cemetery. No retune.

Wave 005 HELD: W2-B Clock CONDITIONAL (254/240, ~45s lag ≠ same-t) — NEEDS_DATA, not a TEST, Governor Pick B. Wave 004 closed: W2-A TEST-20260913-004 REDUNDANT / FAIL-INSUFFICIENT (both T-14m Δ>0; speak 604/604; Join CONDITIONAL / Policy B). No cemetery. No retune.

Wave 006 closed: W2-B last-at-L TEST-20260913-007 REDUNDANT / FAIL-INSUFFICIENT (BTC both-Δ skill N=254; ETH invert N=240). No BTC-only rescue. No cemetery. No retune.

Wave 003 closed: W2-E TEST-20260913-003 REDUNDANT / FAIL-INSUFFICIENT (both T-5m Δ>0; speak 51 BTC / 38 ETH). Wave 002 closed: W2-C TEST-20260913-002 REDUNDANT / FAIL-INSUFFICIENT (ETH T-14m invert; BTC T-10m not a promote). 

Wave 001 closed: F1 TEST-002 REDUNDANT; F3 TEST-001 REDUNDANT. F2 attachment TEST-20260913-001 **REDUNDANT / FAIL-INSUFFICIENT** (ETH k=30 logloss; BTC k=30 and k=50 annex are not a promote). Incumbent **MKT-KALSHI-15M-MID**. No challengers. No retune. CF-001 CLEARED — oracle tape exists; incrementality failed the frozen headline.

## Entry rule
A new STRATEGY_* or FEAT_* must: (1) explicit lineage if from a dead Edge; (2) pre-register cell; (3) Examiner vs this incumbent on the same freeze; (4) UNTESTED if unmeasurable. Oracle UNTESTED does not authorize Binance substitution.
