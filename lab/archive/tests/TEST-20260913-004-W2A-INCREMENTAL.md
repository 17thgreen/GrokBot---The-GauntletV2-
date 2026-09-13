# TEST-20260913-004 — W2A-INCREMENTAL vs MKT-KALSHI-15M-MID

**TEST_ID:** `TEST-20260913-004`
**Package:** `W2A-INCREMENTAL`
**Feature:** `DRAFT-FEAT-20260913-003` (clipped CF−mid basis, λ=0.2 w=0.005 c=0.1 frozen)
**Gate:** `DRAFT-ABST-20260913-003` (speak only on BTC/ETH T-14m mid under uncertainty)
**Incumbent:** `MKT-KALSHI-15M-MID` (TEST-20260911-007 mid-only)
**Purpose:** W2-A clipped CF−mid basis incrementality on two AMD-005 headlines
**DATA:** `DATA-PROV-PM-003` + `DATA-PROV-CF-001` + PM-001 FLOOR_STRIKE / OPEN / CLOSE / RESOLUTION
**Join:** DATA_VERDICT_W2A_CF_T14_JOIN **CONDITIONAL** · Policy B (completed-second s−1) · K revision [A] · close-minute CLEARED ≠ this join
**Slice use:** USED_RESEARCH — not validation, not sealed holdout
**Overall verdict:** `REDUNDANT / FAIL-INSUFFICIENT`
**invented_numbers:** `False`
**Trading:** FORBIDDEN
**Stamp:** Join **CONDITIONAL**. Policy B (completed-second s−1). K revision [A]. close-minute CLEARED ≠ this join. No Map 2. No L3. No Poly. No Φ(z). No sibling blend. No W2-E.
**Annex:** none (no other rem; robustness grid report-only)
**Run UTC:** `2026-09-13T19:40:28Z`
**SHA256 verified:** `True`

## Authority
- `governance/EXAMINER_ORDER_TEST-20260913-004-W2A.md`
- `governance/W2A_INCOMPLETE_SECOND_POLICY_2026-09-13.md`
- `archive/features/DRAFT-FEAT-20260913-003-W2A-cf-mid-basis.md`
- `archive/features/DRAFT-ABST-20260913-003-W2A-uncertainty.md`
- `data/DATA-PROV-CF-001/provenance/DATA_VERDICT_W2A_CF_T14_JOIN.md`

## Frozen map
- d = (cf − K) / K
- q = clip(0.5 + 0.5·clip(d/w, −1, +1), ε, 1−ε) with w=0.005, ε=0.0001
- b = q − m; b_clip = clip(b, −c, +c) with c=0.1
- if ABSTAIN or missing cf/K/m or locked: p = m
- else ALLOW_SPEAK: p = clip(m + λ·b_clip, ε, 1−ε) with λ=0.2
- λ=0.2, w=0.005, c=0.1 frozen. Robustness annex λ∈[0.1, 0.2, 0.3] / c∈[0.05, 0.1, 0.15] / w∈[0.003, 0.005, 0.008] — do not pick winner. λ=0 ⇒ Δ=0.

## Filters / join
- venue=KALSHI, window=15m; BTC/ETH **separate** (no pool)
- DATA-PROV-PM-003 1208-slice only — **no** PM-002 union
- Headlines only: T-14m (rem=840); **no annex**
- `implied_p_method == mid` only; last-fallback excluded
- exclude `implied_p ≤ 0.02` or `≥ 0.98` (near-deg)
- VOID/DISPUTED out of scored N
- K = PM-001 `FLOOR_STRIKE` after OPEN (OPEN_TIME ≤ decision_time) [A]
- cf_t = Policy B: last-in-second on completed second s−1 from DATA-PROV-CF-001 hour tape (BRTI / ETHUSD_RTI); print.time ≤ decision_time_ms
- Missing cf/K/m or inside close-minute → fail-closed p_t := m_t
- **NOT** close-minute CLEARED extractor. **NOT** Join A as headline. **NOT** Binance. **NOT** L3. **NOT** Map 2. **NOT** Φ(z).

**Sign convention:** ΔBrier = Brier_model − Brier_market; ΔLogLoss = LogLoss_model − LogLoss_market; **negative = skill** vs mid.

**Skill rule:** both Δ < 0 on a headline. Kill if either Δ ≥ 0, N < 80, or one headline works and the other inverts. Not NO_EDGE. Not Champion.

## Overall reason
Neither headline improves both Brier and LogLoss vs mid (BTC=REDUNDANT / FAIL-INSUFFICIENT; ETH=REDUNDANT / FAIL-INSUFFICIENT). REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE; not Champion). USED_RESEARCH; holdout closed; no trading. Join CONDITIONAL; Policy B (completed-second s−1); K revision [A]; close-minute CLEARED ≠ this join.

## Headlines (AMD-005, no pool, no annex)

| Cell | N | speak N | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | mean(m)_speak | mean(p)_speak | mean(d)_speak | speak_rate | ECE | Verdict |
|------|--:|--------:|------------:|-------------:|-------:|--------------:|---------------:|---------:|-------------:|-------------:|-------------:|-----------:|-----|---------|
| `KALSHI|15m|BTC|T-14m|mid` | 604 | 604 | 0.235520 | 0.234728 | 0.000792 | 0.664647 | 0.662648 | 0.001999 | 0.5049 | 0.5044 | 0.000007 | 1.0000 | 0.053993 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 604 | 604 | 0.233695 | 0.232936 | 0.000759 | 0.660734 | 0.658864 | 0.001870 | 0.5029 | 0.5028 | 0.000024 | 1.0000 | 0.057104 | `REDUNDANT / FAIL-INSUFFICIENT` |

### `KALSHI|15m|BTC|T-14m|mid`
- n_speak=604; n_abstain=0; fail_closed_missing=0; speak_rate=1.0000
- mean(m)_all=0.5049; mean(p)_all=0.5044; mean(cf_t)=78837.663990; mean(K)=78837.101424
- Reason: ΔBrier≥0 and ΔLogLoss≥0 vs mid-only on headline; REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)
- Calibration: powered bins present; ECE on p_t (model)
- ECE_market: 0.034636
- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no trading)

### `KALSHI|15m|ETH|T-14m|mid`
- n_speak=604; n_abstain=0; fail_closed_missing=0; speak_rate=1.0000
- mean(m)_all=0.5029; mean(p)_all=0.5028; mean(cf_t)=2483.184868; mean(K)=2483.124652
- Reason: ΔBrier≥0 and ΔLogLoss≥0 vs mid-only on headline; REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)
- Calibration: powered bins present; ECE on p_t (model)
- ECE_market: 0.047409
- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no trading)

## Robustness annex (λ×c×w grids; not headline; do not pick winner)

See full sheet in archive; all λ/c/w cells REDUNDANT / FAIL-INSUFFICIENT on both headlines. Placebos: λ=0 identity pass; flip_sign_d / shuffle_cf report-only.

## Filter / join stats
scored=1208; n_speak=1208; fail_closed=0; policy=B; join_verdict=CONDITIONAL; L3/poly/map2/binance unused; sha256 verified.

## Integrity
Join CONDITIONAL; Policy B (completed-second s−1); K revision [A]; close-minute CLEARED ≠ this join.

## Overall package verdict
**`REDUNDANT / FAIL-INSUFFICIENT`** — Neither headline improves both Brier and LogLoss vs mid. USED_RESEARCH; holdout closed; no trading.

## Artifacts
- `/workspace/lab/archive/tests/TEST-20260913-004-W2A-INCREMENTAL.md`
- `/workspace/lab/archive/tests/TEST-20260913-004.json`
