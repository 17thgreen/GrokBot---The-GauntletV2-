# EXAMINER ORDER — PM-002 market baseline
**From:** Conductor  
**To:** Examiner (hard authority)  
**Date (UTC):** 2026-09-11  
**TEST purpose:** venue calibration of \(m_t\) — not a strategy  
**DATA:** DATA-PROV-PM-002 (Clock CONDITIONAL) joined to DATA-PROV-PM-001 resolution labels  
**Freeze:** `governance/PM002_COVERAGE_FROZEN_2026-09-11.md` — locked before this run

## Question
When the Kalshi mid says ~55 / 60 / 70 / 80%, how often does YES resolve?

This is the **market baseline**. Every later Gauntlet \(p_t\) must beat this on the same cells.

## Primary cells (only)

`KALSHI|15m|{BTC,ETH}|{T-14m,T-10m,T-5m}|mid`

Exclude: implied_p ≤0.02 or ≥0.98; `implied_p_method != mid` (no last-fallback). Asset and checkpoint **separate**.

## Join
- Checkpoints: `/workspace/lab/data/DATA-PROV-PM-002/derived/checkpoints.ndjson`
- Labels: DATA-PROV-PM-001 resolved contracts (official YES/NO/VOID)
- Join on native/parent contract id. VOID/DISPUTED out of scored N or separate void bucket.
- Do **not** use PM-001 `LAST_PRICE_DOLLARS` / `OUTCOME_PRICES` as \(m_t\).

## Required metrics (`BINARY_EXAMINER_SPEC.md`)

This package has **no model**. Honest:

| Metric | This package |
|--------|----------------|
| N | MEASURE (declare: scored decision-events per cell) |
| WR | MEASURE only as descriptive "mid>0.5 ⇒ YES" — not a skill claim |
| CI | MEASURE on WR / bin rates if N allows; else UNTESTED |
| Brier_model / LogLoss_model | **UNTESTED** |
| Calibration | MEASURE of \(m_t\) vs y (reliability table + ECE if N allows) |
| Brier_market / LogLoss_market | MEASURE |
| Δ vs market / gap / EV / abstention / cost sensitivity | **UNTESTED** |
| mean(\(m_t\)) | MEASURE |

Bins (pre-registered): [0.02,0.50), [0.50,0.55), [0.55,0.60), [0.60,0.70), [0.70,0.80), [0.80,0.90), [0.90,0.98). If a bin has too few points for a named rate+CI → `UNTESTED` for that bin, do not pool bins to invent a curve.

If cell N is too small for a powered calibration claim: package `FAIL-INSUFFICIENT` or metric-level `UNTESTED` — **not** `NO_EDGE`.

## Annex (after primary, same TEST or clearly labeled annex)
Poly last-print non-T−0, strata separate. Score as last-print benchmark only. Kalshi T−1m mid caveat annex optional.

## Forbidden
Invented numbers. Pooled Kalshi+Poly. T−0. Books-as-present. Binance oracle substitute. Strategy search. Trading. Treating 240 as 3824 or holdout. Changing freeze after peeking.

## Outputs
TEST markdown + JSON with every required key present (`UNTESTED` allowed; key absence forbidden). Persist under harness/examiner/out/. Invented_numbers=false.
