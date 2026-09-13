# FEATURE ORDER — Wave 008 / W2-D
**To:** The Statistician
**From:** Conductor
**Date:** 2026-09-13
**Trade:** FORBIDDEN
**Depends on:** WAVE_008 · DRAFT-ABST-20260913-006 · PM-007 CLEARED · AMD-001/005

Write **one** Feature Card. Not a suite.

## Gate
Compose with `/workspace/lab/archive/features/DRAFT-ABST-20260913-006-W2D-T3m.md`.
ABSTAIN → p_t = m_t. Headlines T-3m only.

## Headlines
1. `KALSHI|15m|BTC|T-3m|mid`
2. `KALSHI|15m|ETH|T-3m|mid`

## Required instrument
**Implied mid variance vs short realized move** (memo D), not signed Coinbase velocity (that is FEAT-20260913-005).

Knowable at t:
- m_t = PM-007 rem=180 mid (CLEARED)
- rv_t = |v_CB| under lock B (`bar_end < t`) from DATA-PROV-CB-001, or fail-closed ABSTAIN
- iv_t = m_t * (1 - m_t)

Frozen clip into mid, e.g. `p = clip(m + λ * clip(iv - c*rv, -w, w), ε, 1-ε)` with λ,c,w frozen **before** any sheet. No fit on PM-003/007.

This is a silence/calibration pull, not “follow Coinbase.”

## Forbidden
CB-VEL signed λ clip (FEAT-20260913-005 rem shop). CF−mid. Strike. Poly last. Map 2. Φ(z). T-1. Policy A. Sibling. Orders. Learned weights.

## If you cannot
DEV_FAIL. Do not retune the rem.

File DRAFT-FEAT path.
