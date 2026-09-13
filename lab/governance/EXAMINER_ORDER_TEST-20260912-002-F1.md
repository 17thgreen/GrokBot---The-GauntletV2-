# EXAMINER ORDER — TEST-20260912-002 F1 incrementality
**From:** Conductor  
**To:** Examiner  
**DATA:** DATA-PROV-PM-003 + DATA-PROV-L3-001 (Clock CONDITIONAL) + PM-001 FLOOR_STRIKE / resolution  
**Join:** `governance/L3_001_COVERAGE_FROZEN_2026-09-12.md`

## Cards (atomic)

| ID | Map |
|----|-----|
| FEAT-20260912-001 | p_t=clip((1-0.35)m_t+0.35 Φ(ln(S_t/K)/(σ√τ)), 1e-4, 1-1e-4); σ_BTC=0.55 σ_ETH=0.70 |
| FEAT-20260912-002 | same with σ_t = RMS of W=60 completed 1m log returns, bar_end≤t; no frozen-σ fallback |

S_t = completed L3 1m close with close_time_ms ≤ decision_time_ms. K=FLOOR_STRIKE. τ=time_remaining_sec/(365.25·24·3600). No EXPIRATION_VALUE. No MLE. No 001+002 ensemble.

## Cells
Headline (separate): `KALSHI|15m|{BTC,ETH}|T-5m|mid`  
Annex only: other four; λ grid {0.20,0.35,0.50} robustness — do not pick winner.

## Metrics
N, Brier/LL model vs market, Δ (model−market; negative=skill). Placebos on 002 as carded. If both Δ≥0 on a headline cell → REDUNDANT / FAIL-INSUFFICIENT not NO_EDGE.

## Forbidden
Lookahead incomplete bar. Binance-as-oracle. Holdout. Trading. Invented numbers.

Outputs: `harness/examiner/out/TEST-20260912-002-F1-INCREMENTAL.{md,json}`
