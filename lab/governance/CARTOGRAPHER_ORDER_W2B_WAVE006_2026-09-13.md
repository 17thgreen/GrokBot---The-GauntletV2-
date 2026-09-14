# CARTOGRAPHER ORDER — Wave 006 / W2-B (incumbent-at-obs)
**To:** The Cartographer
**From:** Conductor
**Date:** 2026-09-13
**Trade:** FORBIDDEN
**Slot:** `governance/WAVE_006_ORTHOGONAL_SLOT_2026-09-13.md`
**Clock:** `DATA_VERDICT_W2B_INCUMBENT_AT_OBS.md` = **CONDITIONAL** (254 BTC / 240 ETH m_L)

Write **one** abstention / eligibility card for Wave 006 W2-B. No Feature formula. No Examiner. No trade.

## Axis
Cross-venue disagreement **with the lag written**. Incumbent is **not** Kalshi mid at decision_time for a Poly last stamped at L≈decision_time−45s.

## Binding incumbent timestamp (Clock option 1)
- L = Poly last `obs_time`
- last_L = Poly last (method=last; bid/ask null; do not invent mid)
- m_L = Kalshi 1m mid at L via `completed_bar_at_L_end_period_ts_le_L` (Clock CONDITIONAL)
- Claim “beats Kalshi mid at decision_time” using L without naming this substitute → **UNTESTED / DEV_FAIL**

## Headlines (binding; no pool; no annex)
1. `KALSHI|15m|BTC|T-5m|mid@L`
2. `KALSHI|15m|ETH|T-5m|mid@L`

## Required on the card
- Knowable at L. Fail-closed if m_L or last_L missing.
- Name lag (~45s median L vs decision_time).
- Name nearest dead/held: DRAFT-FEAT-20260913-004 (held; 45s last ≠ same-t), FEAT-20260913-001, FEAT-005.
- Lineage: DRAFT-FEAT-20260913-004 held, **not retuned**.

## Forbidden
Unlabeled pool · invent Poly mid · treat last as same-t mid · score vs TEST-007 decision_time mid without naming L · Map 2 · λ/c shop · rem annex · orders · Examiner route from this card alone.

If the gate cannot name a legal incumbent timestamp: **DEV_FAIL** this slot.
File `/workspace/lab/archive/features/DRAFT-ABST-…` and point Conductor at the path.
