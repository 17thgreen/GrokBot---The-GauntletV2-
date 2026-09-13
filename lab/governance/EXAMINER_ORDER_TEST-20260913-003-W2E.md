# EXAMINER ORDER — TEST-20260913-003 W2-E strike vs mid
**From:** Conductor  
**To:** Examiner  
**Date (UTC):** 2026-09-13  
**Package:** W2E-INCREMENTAL vs MKT-KALSHI-15M-MID  
**Feature:** DRAFT-FEAT-20260913-002  
**Gate:** DRAFT-ABST-20260913-002  
**Join:** DATA_VERDICT_W2E_STRIKE_L3_JOIN **CONDITIONAL** (L3 ≠ oracle; K revision [A])  
**DATA:** PM-003 + PM-001 FLOOR_STRIKE + L3-001. USED_RESEARCH. No CF. No Poly.

## Frozen map
See card. Speak only on T-5m headlines when sign(S-K) disagrees with sign(m-0.5).  
p_dist = 0.5 + 0.5 clip(((S-K)/K)/0.002, -1, 1)  
p_t = clip((1-0.25)m + 0.25 p_dist, 1e-4, 1-1e-4) on disagreement; else p_t = m_t.  
δ=0.002, λ=0.25 frozen. Robustness annex only — do not pick winner. λ=0 ⇒ Δ=0.

## Headlines (no pool, no annex)
1. `KALSHI|15m|BTC|T-5m|mid`
2. `KALSHI|15m|ETH|T-5m|mid`

## Kill
Δ = model − market; negative = skill.  
Both Δ < 0 required. Either Δ ≥ 0 on a headline → REDUNDANT / FAIL-INSUFFICIENT.  
One-asset invert kills. N < 80 kills. Not NO_EDGE. Not Champion.

Stamp on report: L3 is not the oracle. CONDITIONAL join.

## Forbidden
Φ(z). Sibling blend. CF-as-oracle. VOID-at-t. Retune λ/δ. Invented numbers. Trading.

Outputs: `harness/examiner/out/TEST-20260913-003-W2E-INCREMENTAL.{md,json}`
