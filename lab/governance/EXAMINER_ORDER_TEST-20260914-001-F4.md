# EXAMINER ORDER — TEST-20260914-001 F4 wick-gate
**From:** Conductor
**To:** Examiner
**Date (UTC):** 2026-09-14
**Package:** F4-WICK-INCREMENTAL vs MKT-KALSHI-15M-MID
**Feature:** DRAFT-FEAT-20260914-008
**Gate:** DRAFT-ABST-20260914-008
**Join:** PM-004 × L3-002 lock B + L3-001 Sep-11 edges (Sep-12 855/855)
**DATA:** PM-004 mid + L3-002/L3-001 + PM-001 FLOOR_STRIKE / RESOLUTION. USED_RESEARCH. No PM-003. No CF oracle.
**Governor:** SIGN F4 (`GOVERNOR_SIGN_F4_WICK_2026-09-14.md`).

## Frozen map
θ=1.5 W=5 λ=0.35 ε=1e-4 Wσ=60. Lock B.
On ALLOW + wick: p = clip((1-λ)m + λ Φ(z), ε, 1-ε)
else p = m.
No θ/W search. Annex λ grid report-only. λ=0 ⇒ Δ=0.

## Headlines (no pool)
1. `KALSHI|15m|BTC|T-5m|mid`
2. `KALSHI|15m|ETH|T-5m|mid`

## Kill
Δ = model − market; negative = skill.
Both Δ < 0 required on a headline. Either Δ ≥ 0 → REDUNDANT / FAIL-INSUFFICIENT.
N_wick < 80 on a headline kills. One-asset invert kills. Not NO_EDGE. Not Champion.
Skill on the full cell (off-wick Δ=0 by construction). Report N_wick as annex, not a leaderboard.

## Forbidden
PM-003. θ/W retune. F1-always-speak. Cheap-binary wick. CF-as-oracle. T-14m. W2-B. Trading.

Outputs: `harness/examiner/out/TEST-20260914-001-F4-WICK-INCREMENTAL.{md,json}`
