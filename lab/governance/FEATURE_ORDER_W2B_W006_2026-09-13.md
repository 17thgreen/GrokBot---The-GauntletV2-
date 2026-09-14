# FEATURE ORDER — Wave 006 / W2-B
**To:** The Statistician
**From:** Conductor
**Date:** 2026-09-13
**Trade:** FORBIDDEN
**Depends on:** WAVE_006 · DRAFT-ABST-20260913-007 · DATA_VERDICT_W2B_INCUMBENT_AT_OBS CLEARED · AMD-001/005

Write **one** Feature Card. Not a suite. Do **not** retune DRAFT-FEAT-20260913-004.

## Gate
Compose with `/workspace/lab/archive/features/DRAFT-ABST-20260913-007-W2B-incumbent-at-L.md`.
ABSTAIN → p = m_L (not decision-time mid). Headlines T-5m only.

## Headlines
1. `KALSHI|15m|BTC|T-5m|mid`
2. `KALSHI|15m|ETH|T-5m|mid`

## Incumbent (binding — write on the card)
`m_L` = Kalshi official 1m mid at L = Poly last obs_time (Clock CLEARED).
A beat-TEST-007-decision-time-mid claim stays **UNTESTED**. This card is incrementality vs **m_L**.

## Required instrument
Cross-venue: Poly 15m **last** (`last_L`) vs `m_L`. last ≠ mid. Do not invent bid/ask.
Frozen clip into m_L, e.g. `p = clip(m_L + λ clip(last_L − m_L, −w, w), ε, 1−ε)` with λ,w frozen **before** any sheet. No fit.

Lineage: DRAFT-FEAT-20260913-004 held (decision-time incumbent). This is a new card, not a λ retune.

## Forbidden
Decision-time mid as incumbent. Invented Poly mid. Last-as-mid. Sibling blend. Map 2. Φ(z). CB-VEL. W2-D rem shop. Policy A. Orders. Learned weights. Examiner Δ (Examiner dark until a new Governor lift — you do not lift it).

## If you cannot
DEV_FAIL. Do not patch 004.

File a new DRAFT-FEAT path (007-class).
