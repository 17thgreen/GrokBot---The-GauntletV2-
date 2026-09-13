# EXAMINER ORDER — TEST-20260913-002 W2-C sibling mid
**From:** Conductor  
**To:** Examiner  
**Date (UTC):** 2026-09-13  
**Package:** W2C-INCREMENTAL vs MKT-KALSHI-15M-MID  
**Feature:** DRAFT-FEAT-20260913-001 (sibling same-window mid blend, λ=0.25 frozen)  
**Gate:** DRAFT-ABST-20260913-001 (speak only on headlines)  
**Join:** DATA_VERDICT_W2C_SIBLING_JOIN **CLEARED** (join only)  
**DATA:** DATA-PROV-PM-003 + PM-001 pairing. USED_RESEARCH. No PM-002. No CF. No L3. No Poly.

## Frozen map
On ABSTAIN or missing sibling: p_t = m_t.  
On ALLOW_SPEAK_HEADLINE: p_t = clip((1-0.25)*m_t + 0.25*m*_t, 1e-4, 1-1e-4)  
m*_t = opposite-asset same OPEN/CLOSE same rem mid (Clock-certified).  
No fit. No λ search. Robustness λ∈{0.15,0.25,0.35} annex only — do not pick winner. λ=0 must give Δ=0.

## Headlines (AMD-005, no pool)
1. `KALSHI|15m|ETH|T-14m|mid`
2. `KALSHI|15m|BTC|T-10m|mid`

**Annex BTC T-14m: DARK.** Do not score as speak. Do not pool.

## Kill (binding)
Sign: Δ = model − market; negative = skill.  
Skill on a headline requires **both** ΔBrier < 0 and ΔLogLoss < 0.  
Kill / REDUNDANT / FAIL-INSUFFICIENT if either Δ ≥ 0 on a headline, or one headline works and the other inverts, or N < 80.  
Not NO_EDGE. Not a Champion. Holdout closed. Trading FORBIDDEN.

## Metrics
N, Brier_model/market, ΔBrier, LogLoss_model/market, ΔLogLoss, mean(m), mean(p), mean(m*), ECE via expected_calibration_error (model vs market, same bins). Thin → UNTESTED. invented_numbers=false.

## Placebos (report, not headline switch)
Shuffle m* within cell; λ=0; wrong-window sibling.

## Forbidden
Retune λ or gate. Raw 0/1. T−1 incumbent. CF/L3. Invented numbers. Trading.

Outputs: `harness/examiner/out/TEST-20260913-002-W2C-INCREMENTAL.{md,json}`
