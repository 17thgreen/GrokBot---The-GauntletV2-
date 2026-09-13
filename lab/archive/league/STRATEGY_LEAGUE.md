# STRATEGY LEAGUE — active table
**Opened:** 2026-09-11 UTC  
**Arena:** DATA-PROV-PM-003 Kalshi 15m BTC/ETH · TEST-20260911-007  
**Benchmark:** venue mid \(m_t\)  
**Trade authorization:** NONE  
**Oracle tape:** DATA-PROV-CF-001 CLEARED. Map 2 vs T−1m mid: TEST-20260913-001 fail on frozen headline.

## Incumbent — MARKET_IMPLIED

| Field | Value |
|-------|-------|
| STRATEGY_ID | **MKT-KALSHI-15M-MID** |
| STATE | **INCUMBENT_BENCHMARK** |
| TEST | TEST-20260911-007 |
| DATA | DATA-PROV-PM-003 (1208) |
| Cells | `KALSHI\|15m\|{BTC,ETH}\|{T-14m,T-10m,T-5m}\|mid` |
| N | 604 / 604 / 604 / 604 / 569 / 545 |
| Brier_market | 0.2347 / 0.2329 / 0.1982 / 0.1982 / 0.1413 / 0.1342 |
| LogLoss_market | 0.6626 / 0.6589 / 0.5820 / 0.5796 / 0.4347 / 0.4158 |
| ECE | 0.0346 / 0.0474 / 0.0415 / 0.0229 / 0.0243 / 0.0329 |
| Trading | FORBIDDEN |

## Challengers

Wave 001: F1 TEST-002 REDUNDANT; F3 TEST-001 REDUNDANT. F2 TEST-20260913-001 **REDUNDANT / FAIL-INSUFFICIENT**. No challengers. No retune.
