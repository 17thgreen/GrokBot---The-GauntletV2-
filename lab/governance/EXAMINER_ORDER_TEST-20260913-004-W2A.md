# EXAMINER ORDER — TEST-20260913-004 W2-A CF−mid basis
**From:** Conductor
**To:** Examiner
**Date (UTC):** 2026-09-13
**Package:** W2A-INCREMENTAL vs MKT-KALSHI-15M-MID
**Feature:** DRAFT-FEAT-20260913-003
**Gate:** DRAFT-ABST-20260913-003
**Join:** DATA_VERDICT_W2A_CF_T14_JOIN **CONDITIONAL**
**Join policy:** **B** completed-second (s−1). See `W2A_INCOMPLETE_SECOND_POLICY_2026-09-13.md`.
**DATA:** PM-003 + PM-001 FLOOR_STRIKE + CF-001 hour tape. USED_RESEARCH. No L3. No Poly.

## Frozen map
See card. q = linear clip of (cf−K)/K with w=0.005; b=q−m clipped ±0.10; p = clip(m + 0.20·b, ε, 1−ε) on ALLOW_SPEAK; else p = m.
λ=0.20, w=0.005, c=0.10 frozen. Robustness annex only — do not pick winner. λ=0 ⇒ Δ=0.

cf_t = hour-tape last-in-second on **completed** second s−1. Not close-minute. Not A.

## Headlines (no pool, no annex)
1. `KALSHI|15m|BTC|T-14m|mid`
2. `KALSHI|15m|ETH|T-14m|mid`

## Kill
Δ = model − market; negative = skill.
Both Δ < 0 required on a headline. Either Δ ≥ 0 → REDUNDANT / FAIL-INSUFFICIENT.
One-asset invert kills. N < 80 kills. Not NO_EDGE. Not Champion.

Stamp: CONDITIONAL join; policy B; K revision [A]; close-minute CLEARED ≠ this join.

## Forbidden
Map 2. Close-minute extractor. T−1 mid. Raw 0/1. Φ(z). Sibling blend. W2-E. Join A as headline. Retune λ/w/c. Invented numbers. Trading.

Outputs: `harness/examiner/out/TEST-20260913-004-W2A-INCREMENTAL.{md,json}`
