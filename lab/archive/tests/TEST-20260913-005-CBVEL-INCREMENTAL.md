# TEST-20260913-005 — CBVEL-INCREMENTAL vs MKT-KALSHI-15M-MID

**TEST_ID:** `TEST-20260913-005`
**Package:** `CBVEL-INCREMENTAL`
**Feature:** `DRAFT-FEAT-20260913-005` (Coinbase 1m velocity clip, λ=0.15 w=0.0015 frozen)
**Gate:** `DRAFT-ABST-20260913-005` (speak only on BTC/ETH T-14m mid with Policy B CB bar)
**Incumbent:** `MKT-KALSHI-15M-MID` (TEST-20260911-007 mid-only)
**Purpose:** CB-VEL Coinbase 1m velocity incrementality on two AMD-005 headlines
**DATA:** `DATA-PROV-PM-003` + `DATA-PROV-CB-001` + PM-001 OPEN / CLOSE / RESOLUTION
**Join:** DATA_VERDICT_CB001_PM003_JOIN **CONDITIONAL** · Policy B (bar_end < decision_time) · no CF · no Poly last · no policy A
**Slice use:** USED_RESEARCH — not validation, not sealed holdout
**Overall verdict:** `REDUNDANT / FAIL-INSUFFICIENT`
**invented_numbers:** `False`
**Trading:** FORBIDDEN
**Stamp:** Join **CONDITIONAL**. Policy B (bar_end < t). No CF. No Poly last. No policy A. No Map 2. No L3. No Φ(z). No sibling blend. No Binance.
**Annex:** none (no other rem; robustness grid report-only)
**Run UTC:** `2026-09-13T20:58:16Z`
**SHA256 verified:** `True`

## Authority
- `governance/EXAMINER_ORDER_TEST-20260913-005-CBVEL.md`
- `governance/CBVEL_ON_MINUTE_POLICY_2026-09-13.md`
- `archive/features/DRAFT-FEAT-20260913-005-CBVEL.md`
- `archive/features/DRAFT-ABST-20260913-005-CBVEL.md`
- `data/DATA-PROV-CB-001/provenance/DATA_VERDICT_CB001_PM003_JOIN.md`

## Frozen map
- ε = 1e-4; w = 0.0015; λ = 0.15
- bar = last CB-001 1m candle with bar_end < decision_time  # LOCK B ONLY
- prior = immediately previous completed CB-001 1m close
- v = (bar.close − prior.close) / prior.close
- if ABSTAIN or bar/prior missing or prior.close≤0: p = m
- else: p = clip(m + λ · clip(v/w, −1, +1), ε, 1−ε) with λ=0.15, w=0.0015, ε=0.0001
- λ=0.15, w=0.0015 frozen. Robustness annex λ∈[0.1, 0.15, 0.2] / w∈[0.001, 0.0015, 0.0025] — do not pick winner. λ=0 ⇒ Δ=0.
- **Policy B ONLY.** NOT policy A (bar_end ≤ t). NOT a rescue.

## Filters / join
- venue=KALSHI, window=15m; BTC/ETH **separate** (no pool)
- DATA-PROV-PM-003 1208-slice only — **no** PM-002 union
- Headlines only: T-14m (rem=840); **no annex**
- `implied_p_method == mid` only; last-fallback excluded
- exclude `implied_p ≤ 0.02` or `≥ 0.98` (near-deg)
- VOID/DISPUTED out of scored N
- CB bar = Policy B: last DATA-PROV-CB-001 1m candle with bar_end < decision_time; prior = previous completed close
- Missing bar/prior/m or inside close-minute → fail-closed p_t := m_t
- **NOT** policy A. **NOT** CF. **NOT** Binance. **NOT** L3. **NOT** Poly last. **NOT** Map 2. **NOT** Φ(z).

**Sign convention:** ΔBrier = Brier_model − Brier_market; ΔLogLoss = LogLoss_model − LogLoss_market; **negative = skill** vs mid.

**Skill rule:** both Δ < 0 on a headline. Kill if either Δ ≥ 0, N < 80, or one headline works and the other inverts. Not NO_EDGE. Not Champion.

## Overall reason
Neither headline improves both Brier and LogLoss vs mid (BTC=REDUNDANT / FAIL-INSUFFICIENT; ETH=REDUNDANT / FAIL-INSUFFICIENT). REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE; not Champion). USED_RESEARCH; holdout closed; no trading. Join CONDITIONAL; Policy B (bar_end < t); no CF; no Poly last; no policy A.

## Headlines (AMD-005, no pool, no annex)

| Cell | N | speak N | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | mean(m)_speak | mean(p)_speak | mean(v)_speak | speak_rate | ECE | Verdict |
|------|--:|--------:|------------:|-------------:|-------:|--------------:|---------------:|---------:|-------------:|-------------:|-------------:|-----------:|-----|---------|
| `KALSHI|15m|BTC|T-14m|mid` | 604 | 604 | 0.237214 | 0.234728 | 0.002485 | 0.668622 | 0.662648 | 0.005974 | 0.5049 | 0.5046 | 0.000000 | 1.0000 | 0.036519 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 604 | 604 | 0.235788 | 0.232936 | 0.002852 | 0.665431 | 0.658864 | 0.006566 | 0.5029 | 0.5024 | 0.000001 | 1.0000 | 0.040788 | `REDUNDANT / FAIL-INSUFFICIENT` |

### `KALSHI|15m|BTC|T-14m|mid`
- n_speak=604; n_abstain=0; fail_closed_missing=0; speak_rate=1.0000
- mean(m)_all=0.5049; mean(p)_all=0.5046; mean(bar_close)=78832.569222; mean(prior_close)=78832.565364
- Reason: ΔBrier≥0 and ΔLogLoss≥0 vs mid-only on headline; REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)
- Calibration: powered bins present; ECE on p_t (model)
- ECE_market: 0.034636
- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no trading)

### `KALSHI|15m|ETH|T-14m|mid`
- n_speak=604; n_abstain=0; fail_closed_missing=0; speak_rate=1.0000
- mean(m)_all=0.5029; mean(p)_all=0.5024; mean(bar_close)=2483.077202; mean(prior_close)=2483.074288
- Reason: ΔBrier≥0 and ΔLogLoss≥0 vs mid-only on headline; REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)
- Calibration: powered bins present; ECE on p_t (model)
- ECE_market: 0.047409
- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no trading)

## Robustness annex (λ×w grids; not headline; do not pick winner)

| Cell | λ | w | N | ΔBrier | ΔLogLoss | Verdict |
|------|--:|--:|--:|-------:|---------:|---------|
| `KALSHI|15m|BTC|T-14m|mid` | 0.1 | 0.001 | 604 | 0.002351 | 0.005654 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.1 | 0.0015 | 604 | 0.001369 | 0.003241 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.1 | 0.0025 | 604 | 0.000780 | 0.001841 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.15 | 0.001 | 604 | 0.004359 | 0.010755 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.15 | 0.0015 | 604 | 0.002485 | 0.005974 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.15 | 0.0025 | 604 | 0.001339 | 0.003218 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.2 | 0.001 | 604 | 0.006921 | 0.017838 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.2 | 0.0015 | 604 | 0.003890 | 0.009564 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.2 | 0.0025 | 604 | 0.002011 | 0.004951 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.1 | 0.001 | 604 | 0.002324 | 0.005452 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.1 | 0.0015 | 604 | 0.001467 | 0.003260 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.1 | 0.0025 | 604 | 0.000663 | 0.001359 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.15 | 0.001 | 604 | 0.004706 | 0.011609 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.15 | 0.0015 | 604 | 0.002852 | 0.006566 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.15 | 0.0025 | 604 | 0.001267 | 0.002715 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.2 | 0.001 | 604 | 0.007903 | 0.021679 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.2 | 0.0015 | 604 | 0.004672 | 0.011202 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.2 | 0.0025 | 604 | 0.002053 | 0.004536 | `REDUNDANT / FAIL-INSUFFICIENT` |

## Placebos (report, not headline switch)

| Placebo | Cell | N | ΔBrier | ΔLogLoss | Notes |
|---------|------|--:|-------:|---------:|-------|
| `lambda_0` | `KALSHI|15m|BTC|T-14m|mid` | 604 | 0.000000 | 0.000000 | λ=0 identity check pass=True |
| `lambda_0` | `KALSHI|15m|ETH|T-14m|mid` | 604 | 0.000000 | 0.000000 | λ=0 identity check pass=True |
| `flip_sign_v` | `KALSHI|15m|BTC|T-14m|mid` | 604 | 0.000106 | 0.000832 | sign(v) flipped; should not beat true sign |
| `flip_sign_v` | `KALSHI|15m|ETH|T-14m|mid` | 604 | 0.001058 | 0.004006 | sign(v) flipped; should not beat true sign |
| `shuffle_v` | `KALSHI|15m|BTC|T-14m|mid` | 604 | 0.000781 | 0.001148 | v shuffled within cell; m fixed |
| `shuffle_v` | `KALSHI|15m|ETH|T-14m|mid` | 604 | 0.003711 | 0.007820 | v shuffled within cell; m fixed |

- placebo_seed: `20260913`
- λ=0 must give ΔBrier=0 and ΔLogLoss=0 (identity vs mid).

## Filter / join stats
```json
{
  "candidates": 1208,
  "excluded_method_not_mid": 0,
  "excluded_near_deg": 0,
  "excluded_void_or_other": 0,
  "excluded_no_y": 0,
  "scored": 1208,
  "n_speak": 1208,
  "n_abstain": 0,
  "n_fail_closed_missing_bar": 0,
  "n_fail_closed_missing_prior": 0,
  "n_fail_closed_locked": 0,
  "n_on_minute": 1208,
  "n_policy_A_bar_rejected": 0,
  "policy_A_used_as_headline": false,
  "policy": "B",
  "join_verdict": "CONDITIONAL",
  "per_cell": {
    "KALSHI|15m|BTC|T-14m|mid": {
      "candidates": 604,
      "scored": 604,
      "speak": 604,
      "abstain": 0,
      "fail_closed_bar": 0,
      "fail_closed_prior": 0,
      "fail_closed_locked": 0,
      "excluded_method_not_mid": 0,
      "excluded_near_deg": 0,
      "excluded_void": 0
    },
    "KALSHI|15m|ETH|T-14m|mid": {
      "candidates": 604,
      "scored": 604,
      "speak": 604,
      "abstain": 0,
      "fail_closed_bar": 0,
      "fail_closed_prior": 0,
      "fail_closed_locked": 0,
      "excluded_method_not_mid": 0,
      "excluded_near_deg": 0,
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
  "enrich": {
    "missing_coverage": 0,
    "missing_pm001": 0,
    "open_close_mismatch_vs_pm001": 0
  },
  "void_bucket_n": 0
}
```

## Integrity

- checkpoints.ndjson sha256: `90e38c2f23e224def13db05924f6470a1e738778882f6b0cc17ed708b3143765`
- expected: `90e38c2f23e224def13db05924f6470a1e738778882f6b0cc17ed708b3143765`
- sha256_verified: `True`
- venues: `{'KALSHI': 6040}`
- Join verdict: **CONDITIONAL**
- Join policy: **B** (bar_end < decision_time)
- Policy A (bar_end ≤ t): **not used** as headline / not a rescue
- CF / Binance / L3 / Poly last / Map 2 / Φ(z) / sibling: **not used**
- EXPIRATION_VALUE: **not read / not scored**
- No λ/w retune; no gate retune; no annex sneak; no pool

## Overall package verdict
**`REDUNDANT / FAIL-INSUFFICIENT`** — Neither headline improves both Brier and LogLoss vs mid (BTC=REDUNDANT / FAIL-INSUFFICIENT; ETH=REDUNDANT / FAIL-INSUFFICIENT). REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE; not Champion). USED_RESEARCH; holdout closed; no trading. Join CONDITIONAL; Policy B (bar_end < t); no CF; no Poly last; no policy A.

FAIL-INSUFFICIENT ≠ NO_EDGE. This is **not** a Champion / strategy PASS. No trading authorization. Holdout closed. Join CONDITIONAL; Policy B.

## Artifacts
- `/workspace/lab/harness/examiner/out/TEST-20260913-005-CBVEL-INCREMENTAL.json`
- `/workspace/lab/harness/examiner/out/TEST-20260913-005-CBVEL-INCREMENTAL.md`
- `/workspace/lab/archive/tests/TEST-20260913-005-CBVEL-INCREMENTAL.json`
- `/workspace/lab/archive/tests/TEST-20260913-005-CBVEL-INCREMENTAL.md`
- `/workspace/lab/archive/tests/TEST-20260913-005.json`
- `/workspace/lab/archive/tests/TEST-20260913-005.md`
- `/workspace/lab/archive/audit/2026-09-13-TEST-20260913-005-CBVEL-INCREMENTAL-examiner.md`
