# TEST-20260913-006 — W2D-IVRV-INCREMENTAL vs MKT-KALSHI-15M-MID

**TEST_ID:** `TEST-20260913-006`
**Package:** `W2D-IVRV-INCREMENTAL`
**Feature:** `DRAFT-FEAT-20260913-006` (iv vs |CB 1m|, λ=0.25 c=80.0 w=0.08 frozen)
**Gate:** `DRAFT-ABST-20260913-006` (speak only on BTC/ETH T-3m mid with Policy B CB bar)
**Incumbent:** `MKT-KALSHI-15M-MID` (same-t rem=180 mid)
**Purpose:** W2-D implied-variance vs |Coinbase 1m| incrementality on two headlines
**DATA:** `DATA-PROV-PM-007` + `DATA-PROV-CB-001` + PM-001 OPEN / CLOSE / RESOLUTION
**Join (mid):** DATA_VERDICT_PM007_T3_JOIN **CLEARED** · **Join (CB):** DATA_VERDICT_CB001_PM007_JOIN **CLEARED** under lock **B** · no CF · no Poly last · Policy A not scored
**Slice use:** USED_RESEARCH — not validation, not sealed holdout
**Overall verdict:** `REDUNDANT / FAIL-INSUFFICIENT`
**invented_numbers:** `False`
**Trading:** FORBIDDEN
**Stamp:** Mid join **CLEARED**; CB join **CLEARED** under lock B; Policy A not scored; sign of v discarded; not FEAT-005; no rem shop. No CF. No Poly last. No Map 2. No L3. No Φ(z). No sibling blend. No Binance.
**Annex:** none (no other rem; robustness λ×c×w grid report-only)
**Run UTC:** `2026-09-13T21:50:00Z`
**SHA256 verified:** `True`

## Authority
- `governance/EXAMINER_ORDER_TEST-20260913-006-W2D.md`
- `governance/GOVERNOR_LIFT_EXAMINER_W2D_2026-09-13.md`
- `archive/features/DRAFT-FEAT-20260913-006-W2D-iv-rv.md`
- `archive/features/DRAFT-ABST-20260913-006-W2D-T3m.md`
- `data/DATA-PROV-PM-007/provenance/DATA_VERDICT_PM007_T3_JOIN.md`
- `data/DATA-PROV-CB-001/provenance/DATA_VERDICT_CB001_PM007_JOIN.md`
- `governance/BINARY_EXAMINER_SPEC.md`

## Frozen map
- ε = 0.0001; λ = 0.25; c = 80.0; w = 0.08
- iv = m · (1 − m)
- bar = last CB-001 1m candle with bar_end < decision_time  # LOCK B ONLY
- prior = immediately previous completed CB-001 1m close
- v = (bar.close − prior.close) / prior.close; rv = |v|  # SIGN DISCARDED
- resid = iv − c · rv
- if ABSTAIN or missing m/bar/prior or prior.close≤0: p = m
- else: p = clip(m + λ · clip(resid, −w, +w), ε, 1−ε) with λ=0.25, c=80.0, w=0.08, ε=0.0001
- Robustness annex λ∈[0.15, 0.25, 0.4] c∈[50.0, 80.0, 120.0] w∈[0.05, 0.08, 0.12] — do not pick winner. λ=0 ⇒ Δ=0.
- **Policy B ONLY.** NOT policy A (bar_end ≤ t). NOT FEAT-005 (signed v).

## Filters / join
- venue=KALSHI, window=15m; BTC/ETH **separate** (no pool)
- DATA-PROV-PM-007 rem=180 mid only — **no** PM-002 union; **no** rem shop
- Headlines only: T-3m (rem=180); **no annex**
- `implied_p_method == mid` only; last-fallback excluded
- exclude `implied_p ≤ 0.02` or `≥ 0.98` (near-deg; TEST-007 hygiene)
- VOID/DISPUTED out of scored N
- CB bar = Policy B: last DATA-PROV-CB-001 1m candle with bar_end < decision_time; prior = previous completed close; rv = |v|
- Missing bar/prior/m or inside close-minute → fail-closed p_t := m_t
- **NOT** policy A. **NOT** signed CB-VEL. **NOT** CF. **NOT** Binance. **NOT** L3. **NOT** Poly last. **NOT** Map 2. **NOT** Φ(z).

**Sign convention:** ΔBrier = Brier_model − Brier_market; ΔLogLoss = LogLoss_model − LogLoss_market; **negative = skill** vs mid.

**Skill rule:** both Δ < 0 on a headline. Kill if either Δ ≥ 0, N < 80, or one headline works and the other inverts. Not NO_EDGE. Not Champion.

## Overall reason
Neither headline improves both Brier and LogLoss vs mid (BTC=REDUNDANT / FAIL-INSUFFICIENT; ETH=REDUNDANT / FAIL-INSUFFICIENT). REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE; not Champion). USED_RESEARCH; holdout closed; no trading. Mid join CLEARED; CB join CLEARED under lock B; Policy A not scored; sign of v discarded; not FEAT-005; no rem shop.

## Headlines (AMD-005, no pool, no annex)

| Cell | N | speak N | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | mean(m)_speak | mean(p)_speak | mean(rv)_speak | speak_rate | ECE | Verdict |
|------|--:|--------:|------------:|-------------:|-------:|--------------:|---------------:|---------:|-------------:|-------------:|--------------:|-----------:|-----|---------|
| `KALSHI|15m|BTC|T-3m|mid` | 471 | 471 | 0.145017 | 0.144105 | 0.000912 | 0.438200 | 0.435030 | 0.003169 | 0.4961 | 0.5105 | 0.000246 | 1.0000 | 0.042637 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 440 | 440 | 0.116436 | 0.116546 | -0.000110 | 0.377897 | 0.377614 | 0.000283 | 0.4932 | 0.5064 | 0.000335 | 1.0000 | 0.019191 | `REDUNDANT / FAIL-INSUFFICIENT` |

### `KALSHI|15m|BTC|T-3m|mid`
- n_speak=471; n_abstain=0; fail_closed_missing=0; speak_rate=1.0000
- mean(m)_all=0.4961; mean(p)_all=0.5105; mean(iv)_speak=0.128032; mean(bar_close)=78894.352505; mean(prior_close)=78893.313015
- Reason: ΔBrier≥0 and ΔLogLoss≥0 vs mid-only on headline; REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)
- Calibration: powered bins present; ECE on p_t (model)
- ECE_market: 0.038337
- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no trading)

### `KALSHI|15m|ETH|T-3m|mid`
- n_speak=440; n_abstain=0; fail_closed_missing=0; speak_rate=1.0000
- mean(m)_all=0.4932; mean(p)_all=0.5064; mean(iv)_speak=0.121398; mean(bar_close)=2481.583023; mean(prior_close)=2481.542659
- Reason: does not improve both Brier and LogLoss vs mid-only (ΔBrier=-0.00011038, ΔLogLoss=0.00028281); REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)
- Calibration: powered bins present; ECE on p_t (model)
- ECE_market: 0.013999
- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no trading)

## Robustness annex (λ×c×w grids; not headline; do not pick winner)

| Cell | λ | c | w | N | ΔBrier | ΔLogLoss | Verdict |
|------|--:|--:|--:|--:|-------:|---------:|---------|
| `KALSHI|15m|BTC|T-3m|mid` | 0.15 | 50.0 | 0.05 | 471 | 0.000306 | 0.001251 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.15 | 50.0 | 0.08 | 471 | 0.000485 | 0.001791 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.15 | 50.0 | 0.12 | 471 | 0.000726 | 0.002456 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.15 | 80.0 | 0.05 | 471 | 0.000290 | 0.001084 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.15 | 80.0 | 0.08 | 471 | 0.000482 | 0.001657 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.15 | 80.0 | 0.12 | 471 | 0.000714 | 0.002269 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.15 | 120.0 | 0.05 | 471 | 0.000308 | 0.000997 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.15 | 120.0 | 0.08 | 471 | 0.000487 | 0.001513 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.15 | 120.0 | 0.12 | 471 | 0.000708 | 0.002081 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.25 | 50.0 | 0.05 | 471 | 0.000561 | 0.002328 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.25 | 50.0 | 0.08 | 471 | 0.000920 | 0.003436 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.25 | 50.0 | 0.12 | 471 | 0.001424 | 0.004897 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.25 | 80.0 | 0.05 | 471 | 0.000533 | 0.002013 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.25 | 80.0 | 0.08 | 471 | 0.000912 | 0.003169 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.25 | 80.0 | 0.12 | 471 | 0.001397 | 0.004520 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.25 | 120.0 | 0.05 | 471 | 0.000561 | 0.001845 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.25 | 120.0 | 0.08 | 471 | 0.000917 | 0.002898 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.25 | 120.0 | 0.12 | 471 | 0.001380 | 0.004143 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.4 | 50.0 | 0.05 | 471 | 0.001019 | 0.004334 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.4 | 50.0 | 0.08 | 471 | 0.001742 | 0.006624 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.4 | 50.0 | 0.12 | 471 | 0.002794 | 0.009847 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.4 | 80.0 | 0.05 | 471 | 0.000971 | 0.003736 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.4 | 80.0 | 0.08 | 471 | 0.001718 | 0.006085 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.4 | 80.0 | 0.12 | 471 | 0.002732 | 0.009071 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.4 | 120.0 | 0.05 | 471 | 0.001013 | 0.003404 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.4 | 120.0 | 0.08 | 471 | 0.001717 | 0.005581 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-3m|mid` | 0.4 | 120.0 | 0.12 | 471 | 0.002685 | 0.008316 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.15 | 50.0 | 0.05 | 440 | -0.000092 | -0.000123 | `PROMISING` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.15 | 50.0 | 0.08 | 440 | -0.000130 | -0.000120 | `PROMISING` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.15 | 50.0 | 0.12 | 440 | -0.000175 | -0.000173 | `PROMISING` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.15 | 80.0 | 0.05 | 440 | -0.000093 | -0.000053 | `PROMISING` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.15 | 80.0 | 0.08 | 440 | -0.000127 | -0.000047 | `PROMISING` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.15 | 80.0 | 0.12 | 440 | -0.000155 | -0.000040 | `PROMISING` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.15 | 120.0 | 0.05 | 440 | -0.000070 | 0.000181 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.15 | 120.0 | 0.08 | 440 | -0.000103 | 0.000146 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.15 | 120.0 | 0.12 | 440 | -0.000136 | 0.000155 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.25 | 50.0 | 0.05 | 440 | -0.000105 | -0.000006 | `PROMISING` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.25 | 50.0 | 0.08 | 440 | -0.000111 | 0.000198 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.25 | 50.0 | 0.12 | 440 | -0.000090 | 0.000380 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.25 | 80.0 | 0.05 | 440 | -0.000109 | 0.000089 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.25 | 80.0 | 0.08 | 440 | -0.000110 | 0.000283 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.25 | 80.0 | 0.12 | 440 | -0.000068 | 0.000545 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.25 | 120.0 | 0.05 | 440 | -0.000071 | 0.000487 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.25 | 120.0 | 0.08 | 440 | -0.000071 | 0.000616 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.25 | 120.0 | 0.12 | 440 | -0.000045 | 0.000853 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.4 | 50.0 | 0.05 | 440 | -0.000052 | 0.000478 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.4 | 50.0 | 0.08 | 440 | 0.000077 | 0.001303 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.4 | 50.0 | 0.12 | 440 | 0.000338 | 0.002274 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.4 | 80.0 | 0.05 | 440 | -0.000063 | 0.000575 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.4 | 80.0 | 0.08 | 440 | 0.000067 | 0.001343 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.4 | 80.0 | 0.12 | 440 | 0.000349 | 0.002391 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.4 | 120.0 | 0.05 | 440 | -0.000003 | 0.001224 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.4 | 120.0 | 0.08 | 440 | 0.000125 | 0.001910 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-3m|mid` | 0.4 | 120.0 | 0.12 | 440 | 0.000363 | 0.002847 | `REDUNDANT / FAIL-INSUFFICIENT` |

## Placebos (report, not headline switch)

| Placebo | Cell | N | ΔBrier | ΔLogLoss | Notes |
|---------|------|--:|-------:|---------:|-------|
| `lambda_0` | `KALSHI|15m|BTC|T-3m|mid` | 471 | 0.000000 | 0.000000 | λ=0 identity check pass=True |
| `lambda_0` | `KALSHI|15m|ETH|T-3m|mid` | 440 | 0.000000 | 0.000000 | λ=0 identity check pass=True |
| `shuffle_rv` | `KALSHI|15m|BTC|T-3m|mid` | 471 | 0.000860 | 0.003485 | rv shuffled within cell; m fixed; sign already discarded |
| `shuffle_rv` | `KALSHI|15m|ETH|T-3m|mid` | 440 | -0.000025 | 0.000798 | rv shuffled within cell; m fixed; sign already discarded |

- placebo_seed: `20260913`
- λ=0 must give ΔBrier=0 and ΔLogLoss=0 (identity vs mid).
- Signed v (FEAT-005) is **not** this card — not scored as a placebo switch.

## Filter / join stats
```json
{
  "candidates": 1208,
  "excluded_method_not_mid": 0,
  "excluded_near_deg": 297,
  "excluded_void_or_other": 0,
  "excluded_no_y": 0,
  "scored": 911,
  "n_speak": 911,
  "n_abstain": 0,
  "n_fail_closed_missing_bar": 0,
  "n_fail_closed_missing_prior": 0,
  "n_fail_closed_locked": 0,
  "n_on_minute": 911,
  "n_policy_A_bar_rejected": 0,
  "policy_A_used_as_headline": false,
  "policy": "B",
  "mid_join_verdict": "CLEARED",
  "cb_join_verdict": "CLEARED",
  "per_cell": {
    "KALSHI|15m|BTC|T-3m|mid": {
      "candidates": 604,
      "scored": 471,
      "speak": 471,
      "abstain": 0,
      "fail_closed_bar": 0,
      "fail_closed_prior": 0,
      "fail_closed_locked": 0,
      "excluded_method_not_mid": 0,
      "excluded_near_deg": 133,
      "excluded_void": 0
    },
    "KALSHI|15m|ETH|T-3m|mid": {
      "candidates": 604,
      "scored": 440,
      "speak": 440,
      "abstain": 0,
      "fail_closed_bar": 0,
      "fail_closed_prior": 0,
      "fail_closed_locked": 0,
      "excluded_method_not_mid": 0,
      "excluded_near_deg": 164,
      "excluded_void": 0
    }
  },
  "cb_bars_loaded": {
    "BTC-USD": 10142,
    "ETH-USD": 10142
  },
  "CF_used": false,
  "L3_used": false,
  "poly_used": false,
  "map2_used": false,
  "binance_used": false,
  "policy_A_used": false,
  "signed_v_used_in_map": false,
  "feat005_map_used": false,
  "enrich": {
    "missing_coverage": 0,
    "missing_pm001": 0,
    "open_close_mismatch_vs_pm001": 0
  },
  "void_bucket_n": 0
}
```

## Integrity

- checkpoints.ndjson sha256: `65d5757e184c4c8371c16b48bfef994eaa3e6181f3a1da2d641b4cce89463aa0`
- expected: `65d5757e184c4c8371c16b48bfef994eaa3e6181f3a1da2d641b4cce89463aa0`
- sha256_verified: `True`
- venues: `{'KALSHI': 1208}`
- Mid join verdict: **CLEARED**
- CB join verdict: **CLEARED** under lock **B**
- Join policy: **B** (bar_end < decision_time)
- Policy A (bar_end ≤ t): **not used** as headline / not a rescue
- Sign of v: **discarded** (rv = |v|); not FEAT-005
- CF / Binance / L3 / Poly last / Map 2 / Φ(z) / sibling: **not used**
- EXPIRATION_VALUE: **not read / not scored**
- No λ/c/w retune; no gate retune; no annex sneak; no pool; no rem shop

## Overall package verdict
**`REDUNDANT / FAIL-INSUFFICIENT`** — Neither headline improves both Brier and LogLoss vs mid (BTC=REDUNDANT / FAIL-INSUFFICIENT; ETH=REDUNDANT / FAIL-INSUFFICIENT). REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE; not Champion). USED_RESEARCH; holdout closed; no trading. Mid join CLEARED; CB join CLEARED under lock B; Policy A not scored; sign of v discarded; not FEAT-005; no rem shop.

FAIL-INSUFFICIENT ≠ NO_EDGE. This is **not** a Champion / strategy PASS. No trading authorization. Holdout closed. Mid CLEARED; CB CLEARED lock B.

## Artifacts
- `/workspace/lab/harness/examiner/out/TEST-20260913-006-W2D-IVRV-INCREMENTAL.json`
- `/workspace/lab/harness/examiner/out/TEST-20260913-006-W2D-IVRV-INCREMENTAL.md`
- `/workspace/lab/archive/tests/TEST-20260913-006-W2D-IVRV-INCREMENTAL.json`
- `/workspace/lab/archive/tests/TEST-20260913-006-W2D-IVRV-INCREMENTAL.md`
- `/workspace/lab/archive/tests/TEST-20260913-006.json`
- `/workspace/lab/archive/tests/TEST-20260913-006.md`
- `/workspace/lab/archive/audit/2026-09-13-TEST-20260913-006-W2D-IVRV-INCREMENTAL-examiner.md`
