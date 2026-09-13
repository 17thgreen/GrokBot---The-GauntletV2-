# EXAMINER ORDER — TEST-20260913-005 CB-VEL
**From:** Conductor
**To:** Examiner
**Date (UTC):** 2026-09-13
**Package:** CBVEL-INCREMENTAL vs MKT-KALSHI-15M-MID
**Feature:** DRAFT-FEAT-20260913-005
**Gate:** DRAFT-ABST-20260913-005
**Join:** DATA_VERDICT_CB001_PM003_JOIN **CONDITIONAL**
**Join policy:** **B** (`bar_end < decision_time`). See `CBVEL_ON_MINUTE_POLICY_2026-09-13.md`.
**DATA:** PM-003 + CB-001. USED_RESEARCH. No CF. No L3. No Poly last.
**Governor:** lift Examiner dark for this package only.

## Frozen map
v = (close_B − close_{B-1}) / close_{B-1} with B last CB-001 bar, bar_end < t.
On ALLOW_SPEAK: p = clip(m + 0.15 * clip(v/0.0015, -1, +1), ε, 1-ε)
else p = m.
λ=0.15, w=0.0015 frozen. Annex λ/w grid report-only — do not pick winner. λ=0 ⇒ Δ=0.
Policy A is not a headline.

## Headlines (no pool, no annex)
1. `KALSHI|15m|BTC|T-14m|mid`
2. `KALSHI|15m|ETH|T-14m|mid`

## Kill
Δ = model − market; negative = skill.
Both Δ < 0 required on a headline. Either Δ ≥ 0 → REDUNDANT / FAIL-INSUFFICIENT.
One-asset invert kills. N < 80 kills. Not NO_EDGE. Not Champion.

## Forbidden
Map 2. CF. Binance fill. Poly last. Policy A. T−1 mid. Raw 0/1. Φ(z). Sibling. Retune λ/w. Trading.

Outputs: `harness/examiner/out/TEST-20260913-005-CBVEL-INCREMENTAL.{md,json}`
