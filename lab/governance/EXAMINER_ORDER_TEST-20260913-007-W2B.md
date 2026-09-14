# EXAMINER ORDER — TEST-20260913-007 W2-B last vs mid-at-L
**From:** Conductor
**To:** Examiner
**Date (UTC):** 2026-09-13
**Package:** W2B-LAST-AT-L-INCREMENTAL vs m_L
**Feature:** DRAFT-FEAT-20260913-007
**Gate:** DRAFT-ABST-20260913-007
**Join:** DATA_VERDICT_W2B_INCUMBENT_AT_OBS (254/240; incumbent-timestamp certified; 45s lag vs decision_time is honesty, not this incumbent)
**DATA:** PM-005 Poly last + PM-003 Kalshi 1m candles for m_L + PM-001 RESOLUTION. USED_RESEARCH.
**Governor:** lift Examiner dark for this package only (`GOVERNOR_LIFT_EXAMINER_W2B_W006_2026-09-13.md`).

## Frozen map
L = Poly last obs_time
last_L = Poly 15m last (method=last; not mid)
m_L = Kalshi official 1m mid at L (completed-bar end_period_ts ≤ unix(L); NOT decision-time mid)
On ALLOW_SPEAK: p = clip(m_L + λ * clip(last_L − m_L, −w, +w), ε, 1−ε)
else p = m_L.
λ=0.20, w=0.12, ε=1e-4 frozen. Annex λ/w grid report-only. λ=0 ⇒ Δ=0 vs m_L.

## Headlines (no pool, no annex)
1. `KALSHI|15m|BTC|T-5m|mid` — incrementality vs **m_L**
2. `KALSHI|15m|ETH|T-5m|mid` — incrementality vs **m_L**

## Kill
Δ = model − m_L; negative = skill.
Both Δ < 0 required on a headline. Either Δ ≥ 0 → REDUNDANT / FAIL-INSUFFICIENT.
One-asset invert kills. N < 80 kills. Not NO_EDGE. Not Champion.
A Δ vs TEST-007 decision-time mid is **out of scope** — do not report it as this instrument.

## Forbidden
Decision-time mid as incumbent. Invented Poly mid. Last-as-mid. Map 2. CF. Sibling. CB-VEL. W2-D rem shop. Retune λ/w. Trading.

Outputs: `harness/examiner/out/TEST-20260913-007-W2B-LAST-AT-L-INCREMENTAL.{md,json}`
