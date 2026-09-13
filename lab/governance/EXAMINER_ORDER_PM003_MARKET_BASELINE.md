# EXAMINER ORDER — PM-003 market baseline
**From:** Conductor  
**To:** Examiner  
**TEST_ID (assigned):** TEST-20260911-007  
**Package:** PM003-MARKET-BASELINE  
**Purpose:** venue calibration of \(m_t\) on the 1208-slice — **not** a strategy  
**DATA:** DATA-PROV-PM-003 (Clock CONDITIONAL) joined to PM-001 official resolution  
**Freeze:** `governance/PM003_COVERAGE_FROZEN_2026-09-11.md`

## Primary cells only
`KALSHI|15m|{BTC,ETH}|{T-14m,T-10m,T-5m}|mid`
Exclude near-deg and last-fallback. Asset × checkpoint **separate**. **Do not** include PM-002 rows.

## Join
- Checkpoints: `/workspace/lab/data/DATA-PROV-PM-003/derived/checkpoints.ndjson` SHA256 `90e38c2f23e224def13db05924f6470a1e738778882f6b0cc17ed708b3143765`
- Labels: PM-001 official YES/NO/VOID only
- Never PM-001 LAST_PRICE / OUTCOME_PRICES as \(m_t\)

## Metrics (no model)
MEASURE: N, descriptive mid>0.5 WR + Wilson CI if powered, calibration of \(m_t\) vs y, Brier_market, LogLoss_market, mean(\(m_t\)).
UNTESTED: Brier_model, LogLoss_model, Δ, gap, EV, abstention, costs.
Same pre-registered bins as TEST-006. Thin bin → UNTESTED, not pooled. ECE only if ≥2 bins with n≥20 and/or N≥100.
FAIL-INSUFFICIENT ≠ NO_EDGE.

## Annex
T−1m mid optional after primary. No Poly (not in this dataset).

## Forbidden
Invented numbers. Union with PM-002. T−0. Strategy search. Trading. Changing freeze after peek.

Outputs: `harness/examiner/out/TEST-20260911-007-PM003-MARKET-BASELINE.{md,json}` + archive copies. invented_numbers=false.
