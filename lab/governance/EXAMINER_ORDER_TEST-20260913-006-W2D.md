# EXAMINER ORDER — TEST-20260913-006 W2-D iv-vs-rv
**From:** Conductor
**To:** Examiner
**Date (UTC):** 2026-09-13
**Package:** W2D-IVRV-INCREMENTAL vs MKT-KALSHI-15M-MID
**Feature:** DRAFT-FEAT-20260913-006
**Gate:** DRAFT-ABST-20260913-006
**Join (mid):** DATA_VERDICT_PM007_T3_JOIN **CLEARED**
**Join (CB):** DATA_VERDICT_CB001_PM007_JOIN **CLEARED** under lock **B**
**Join policy:** **B** (`bar_end < decision_time`). Policy A is caveat-count only — not a headline.
**DATA:** PM-007 rem=180 mid + CB-001 + PM-001 OPEN / CLOSE / RESOLUTION. USED_RESEARCH. No CF. No L3. No Poly last.
**Governor:** lift Examiner dark for this package only (`GOVERNOR_LIFT_EXAMINER_W2D_2026-09-13.md`).

## Frozen map
iv = m * (1 − m)
rv = |v_CB| with v_CB = (close_B − close_{B-1}) / close_{B-1}
B = last CB-001 bar, bar_end < t
On ALLOW_SPEAK: p = clip(m + λ * clip(iv − c·rv, −w, +w), ε, 1−ε)
else p = m.
λ=0.25, c=80, w=0.08, ε=1e-4 frozen. Annex λ/c/w grid report-only — do not pick winner. λ=0 ⇒ Δ=0.
Sign of v discarded. Not FEAT-20260913-005. Policy A is not a headline.

## Headlines (no pool, no annex)
1. `KALSHI|15m|BTC|T-3m|mid` (rem=180)
2. `KALSHI|15m|ETH|T-3m|mid` (rem=180)

## Kill
Δ = model − market; negative = skill.
Both Δ < 0 required on a headline. Either Δ ≥ 0 → REDUNDANT / FAIL-INSUFFICIENT.
One-asset invert kills. N < 80 kills. Not NO_EDGE. Not Champion.

## Forbidden
Map 2. CF. Binance fill. Poly last. Policy A. T−1 mid. Raw 0/1. Φ(z). Sibling. Signed CB-VEL. Retune λ/c/w. Rem shop. Trading.

Outputs: `harness/examiner/out/TEST-20260913-006-W2D-IVRV-INCREMENTAL.{md,json}`
