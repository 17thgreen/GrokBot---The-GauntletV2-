# CLOCK ORDER — W2-B Kalshi mid × Poly last at T-5m
**To:** The Clock
**From:** Conductor
**Date:** 2026-09-13
**Trade:** FORBIDDEN
**Feature:** DRAFT-FEAT-20260913-004 (door **NEEDS_DATA** — not READY)
**Gate:** DRAFT-ABST-20260913-004

## Join to certify (fail-closed)

```
m_t    = PM-003 Kalshi same-row mid
         implied_p_method == mid
         rem = 300
         mid timestamp = decision_time
L_t    = PM-005 Poly 15m last-print
         pairing = exact (asset, OPEN_TIME, CLOSE_TIME)
         obs_time <= decision_time
         bid/ask must stay null — do not invent mid
cell ∈ {KALSHI|15m|BTC|T-5m|mid, KALSHI|15m|ETH|T-5m|mid}
```

Missing m_t or L_t → fail-closed (Feature sets p_t := m_t).
Do **not** union PM-002. Do **not** treat last as mid. Do **not** pool venues. Do **not** invent prints.

## Scope
Join only. Not alpha. Not Examiner Δ.
Headlines only (rem=300). rem=600/840 in PM-005 are **dark**.
DATA: PM-003 + PM-005. Inventory claims 276 BTC / 275 ETH rem=300 last after fetch.

## Why CONDITIONAL is expected
Poly last is weaker (lag). Mid BLOCKED. Confirm coverage, look-ahead, pairing honesty.

## Write
`/workspace/lab/data/DATA-PROV-PM-005/provenance/DATA_VERDICT_W2B_POLY_T5_JOIN.md`
plus audit JSON.

DATA VERDICT: CLEARED / CONDITIONAL / QUARANTINED / REJECTED.
