# CARTOGRAPHER ORDER — Wave 006 / W2-B (legal incumbent)
**To:** The Cartographer
**From:** Conductor
**Date:** 2026-09-13
**Trade:** FORBIDDEN
**Slot:** `governance/WAVE_006_ORTHOGONAL_SLOT_2026-09-13.md`
**Clock:** `DATA_VERDICT_W2B_INCUMBENT_AT_OBS` **CLEARED** (incumbent-timestamp only)

Write **one new** abstention / eligibility card. Do **not** retune DRAFT-ABST-20260913-004.

## Incumbent timestamp (binding)
Incumbent = Kalshi official 1m **mid at L** (`m_L`), L = Poly last `obs_time`. Clock CLEARED 254/240.

**Not** Kalshi mid at `decision_time`. A claim that Poly last beats TEST-007 decision-time mid stays **UNTESTED**. This gate is speak-only when both `last_L` and `m_L` exist under that verdict.

## Headlines (same pair; no shop)
1. `KALSHI|15m|BTC|T-5m|mid`
2. `KALSHI|15m|ETH|T-5m|mid`

Instrument: Poly 15m **last** (not mid). last ≠ mid. Do not invent bid/ask.

## Required
- Fail-closed if last_L or m_L missing
- Name the Clock candle rule (completed-bar `end_period_ts ≤ unix(L)`)
- Name nearest dead: FEAT-20260913-006 (W2-D), FEAT-20260913-005 (CB-VEL), FEAT-20260913-001 (sibling), DRAFT-FEAT-20260913-004 (held; 45s last ≠ same-t at decision_time)
- Examiner **dark** on this card until a new Governor lift. You do not lift it.

## Forbidden
Retune 004. Decision-time mid as incumbent. Invented Poly mid. Last-as-mid. Rem shop. Map 2. Sibling blend. Orders. Examiner Δ.

If you cannot write the gate without using decision-time mid as incumbent: **DEV_FAIL**.
File a new DRAFT-ABST path (007-class).
