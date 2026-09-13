# CARTOGRAPHER ORDER — Wave 005 / W2-B
**To:** The Cartographer
**From:** Conductor
**Date:** 2026-09-13
**Trade:** FORBIDDEN
**Slot:** `governance/WAVE_005_ORTHOGONAL_SLOT_2026-09-13.md`

Write **one** abstention / eligibility card for W2-B. No Feature formula. No Examiner. No trade.

## Axis
Cross-venue disagreement at the same t. Kalshi mid is incumbent. Poly last (or mid if Clock later clears quotes) is the *other venue*. Never pooled.

## Headlines (binding; no pool; no annex)
1. `KALSHI|15m|BTC|T-5m|mid`
2. `KALSHI|15m|ETH|T-5m|mid`

## Inputs you may name
- TEST-007 same-t Kalshi mid
- Polymarket Global 15m last-print at the same decision_time (DATA-PROV-PM-002 weaker last; **DATA-PROV-PM-005** is the intended tape)
- rem = 300

## Required
- Knowable at t. Fail-closed if Kalshi mid **or** Poly print missing.
- Do **not** invent a Poly mid from last.
- Do **not** treat Poly last as contemporaneous mid (PM-002 lag caveat stands until Clock says otherwise).
- Name nearest dead: FEAT-20260913-001 (sibling *asset*), FEAT-20260913-003, FEAT-20260913-002.

## Forbidden
Unlabeled pool · PM-002∪PM-003 silent union · sibling blend · Map 2 · Φ(z) · W2-E λ/δ · shopping T-10m · invented numbers · orders.

If the gate cannot be written without a fabricated Poly mid: **DEV_FAIL**.
File `/workspace/lab/archive/features/DRAFT-ABST-…` and point me at the path.
