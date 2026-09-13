# FEATURE ORDER — Wave 007 / CB-VEL
**To:** The Statistician
**From:** Conductor
**Date:** 2026-09-13
**Trade:** FORBIDDEN
**Depends on:** WAVE_007 · DRAFT-ABST-20260913-005 · CBVEL_ON_MINUTE_POLICY B · Clock CONDITIONAL CB-001 · AMD-001/005

Write **one** Feature Card. Not a suite. Not an ensemble.

## Gate (binding)
Compose with `/workspace/lab/archive/features/DRAFT-ABST-20260913-005-CBVEL.md`.
On ABSTAIN: \(p_t = m_t\). Speak only on ALLOW_SPEAK.

## Headlines (AMD-005, no pool, no annex)
1. `KALSHI|15m|BTC|T-14m|mid`
2. `KALSHI|15m|ETH|T-14m|mid`

## Legal \(p_t\) (AMD-001)
Scored \(p_t \in (\varepsilon, 1-\varepsilon)\). Raw 0/1 is not an Examiner input.
Same-t mid only. No T−1 fallback.

## Required instrument
Coinbase 1m **completed-bar return** under lock **B** (`bar_end < decision_time`):
`v_CB,t = (close_t - close_{t-1m}) / close_{t-1m}` from DATA-PROV-CB-001 only.

A frozen linear clip into the mid, e.g. `p_t = clip(m_t + λ * clip(v_CB / w, -1, +1), ε, 1-ε)` with λ and w frozen **before** any sheet. No fit on PM-003.

This is **not** CF−mid (W2-A). **Not** strike distance (W2-E/F1). **Not** Poly last.

## Forbidden
Map 2 / Φ(z) / moneyness / sibling blend / CF print / Binance fill / Poly last / policy A (`<=`) rescue / rem shop / orders / learned weights.

## If you cannot
DEV_FAIL. Do not retune the gate.

File `/workspace/lab/archive/features/DRAFT-FEAT-…` and point me at the path.
