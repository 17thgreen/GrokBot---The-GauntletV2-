# EXAMINER ORDER — TEST-20260912-001 F3 incrementality
**From:** Conductor  
**To:** Examiner  
**Date (UTC):** 2026-09-12  
**Package:** F3-INCREMENTAL vs MKT-KALSHI-15M-MID  
**DATA:** DATA-PROV-PM-003 only (USED_RESEARCH). No PM-002. No L3. No Poly.

## Cards (atomic — two sub-packages or two clearly labeled sections)

| ID | Feature | Frozen map |
|----|---------|------------|
| FEAT-20260912-003 | s_t = yes_ask − yes_bid | p_t=(1−λ_t)m_t + λ_t·0.5, λ_t=clip(s_t/0.05, 0, 1) |
| FEAT-20260912-004 | δ_t = last − m_t | p_t=clip(m_t + 1.0·δ_t, 1e-4, 1−1e-4) |

No MLE. No α,β,γ fit. Do not ensemble 003+004 this TEST.

## Cells
Primary headline: `KALSHI|15m|BTC|T-5m|mid`  
Annex (separate): the other five of the six. Same near-deg / last-fallback excludes as TEST-007.

## Metrics
For each card × cell: N, Brier_model, Brier_market, ΔBrier (model−market; negative=skill), LogLoss_model, LogLoss_market, ΔLogLoss, mean(m_t), mean(p_t), abstention if any (default none). ECE UNTESTED if bins thin. WR descriptive optional.
If ΔBrier≥0 and ΔLogLoss≥0 on primary → REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE).

## Forbidden
In-sample refit. Union holdout. Funding/OI. Invented numbers. Trading.

Outputs: `harness/examiner/out/TEST-20260912-001-F3-INCREMENTAL.{md,json}` invented_numbers=false.
