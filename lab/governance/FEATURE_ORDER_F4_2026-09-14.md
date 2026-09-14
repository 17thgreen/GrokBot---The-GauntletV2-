# FEATURE ORDER — Wave 009 / F4
**To:** The Statistician
**From:** Conductor
**Date:** 2026-09-14
**Trade:** FORBIDDEN
**Depends on:** WAVE_009 · DRAFT-ABST-20260914-008 · GOVERNOR_SIGN_F4 · AMD-001/005

Write **one** Feature Card. Not a suite. Compose DRAFT-FEAT-20260912-006 onto the new gate. Do **not** retune θ/W/λ.

## Gate
Compose with `/workspace/lab/archive/features/DRAFT-ABST-20260914-008-F4-wick.md`.
ABSTAIN / missing lookback → p = m. Off-wick → p = m (Feature silence). Headlines T-5m only.

## Headlines
1. `KALSHI|15m|BTC|T-5m|mid`
2. `KALSHI|15m|ETH|T-5m|mid`

## Tape
Sep-12 PM-004 mid × L3-002 lock B + named L3-001 edges. No PM-003. L3 ≠ oracle.

## Frozen instrument (already on disk — do not search)
θ=1.5, W=5, λ=0.35, ε=1e-4.
Wick := |ln(S_t/S_{t-W})| > θ · σ̂_t · √(W / (365.25·24·60))
On wick: p = clip((1-λ)m + λ Φ(z), ε, 1-ε) with z from the draft structural map (L3 S_t, FLOOR_STRIKE, same σ̂).
Off wick / ABSTAIN: p = m.
N_wick < 80 on a headline kills. One-asset invert kills.

## Forbidden
θ/W/λ fit. Wick histogram before freeze (already frozen). PM-003 peek. F1-always-speak. Cheap-binary wick. |m − p_struct| wick. W2-B. Map 2. T-14m. Orders. Examiner Δ from this filing.

## If you cannot
DEV_FAIL. Do not invent a new θ.

File a new DRAFT-FEAT path (008-class / 20260914).
