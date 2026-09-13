# TEST-20260912-002 — F1-INCREMENTAL vs MKT-KALSHI-15M-MID

**TEST_ID:** `TEST-20260912-002`
**Package:** `F1-INCREMENTAL`
**Incumbent:** `MKT-KALSHI-15M-MID` (TEST-20260911-007 mid-only)
**Purpose:** atomic incrementality of two F1 frozen no-fit maps vs Kalshi mid
**DATA:** `DATA-PROV-PM-003` + `DATA-PROV-L3-001` + PM-001 FLOOR_STRIKE / RESOLUTION
**Slice use:** USED_RESEARCH — not validation, not sealed holdout
**Overall verdict:** `REDUNDANT / FAIL-INSUFFICIENT`
**invented_numbers:** `False`
**Trading:** FORBIDDEN
**MLE / ensemble 001+002:** forbidden and not run
**EXPIRATION_VALUE / incomplete-bar close:** NOT USED
**Run UTC:** `2026-09-12T00:19:13Z`
**SHA256 verified:** `True`

## Authority
- `governance/EXAMINER_ORDER_TEST-20260912-002-F1.md`
- `governance/L3_001_COVERAGE_FROZEN_2026-09-12.md`
- `archive/features/FEAT-20260912-001.md`
- `archive/features/FEAT-20260912-002.md`
- `data/DATA-PROV-L3-001/provenance/DATA_VERDICT_DATA-PROV-L3-001.md`
- `governance/BINARY_EXAMINER_SPEC.md`
- `harness/examiner/src/pm003_market_baseline.py`

## Filters / join (TEST-007 excludes + L3 completed-bar)
- venue=KALSHI, window=15m; BTC/ETH **separate** (no pool)
- DATA-PROV-PM-003 1208-slice only — **no** PM-002 union
- checkpoints: T-14m (840), T-10m (600), T-5m (300)
- `implied_p_method == mid` only; last-fallback excluded
- exclude `implied_p ≤ 0.02` or `≥ 0.98` (near-deg)
- VOID/DISPUTED out of scored N
- K = PM-001 `FLOOR_STRIKE` (never `EXPIRATION_VALUE`)
- S_t = L3 completed 1m close: knowable_bar = argmax{bar | close_time_ms ≤ decision_time_ms}
- On this slice: open_time_ms = decision_time_ms − 60000 (verified in stats)
- No incomplete-bar close. Binance L3 is NOT the oracle.
- FEAT-002: drop if W=60 incomplete (no frozen-σ fallback)
- m_t = checkpoint `implied_p` mid — never LAST_PRICE / OUTCOME_PRICES

**Sign convention:** ΔBrier = Brier_model − Brier_market; ΔLogLoss = LogLoss_model − LogLoss_market; **negative = skill** vs mid.

**Falsification:** if both Δ≥0 on a headline cell → `REDUNDANT / FAIL-INSUFFICIENT` (not `NO_EDGE`). Skill requires **both** Δ < 0. No BTC+ETH pool.

**Headline cells (pre-registered, separate):** `KALSHI|15m|BTC|T-5m|mid`, `KALSHI|15m|ETH|T-5m|mid`
Other four cells = annex. λ∈{0.20,0.35,0.50} robustness — do not pick winner.

## Card 1 — FEAT-20260912-001 (frozen σ digital)

**Frozen map (headline, no-fit):** \(z=\ln(S/K)/(\sigma\sqrt{\tau})\); \(p=\mathrm{clip}((1-0.35)m+0.35\Phi(z),10^{-4},1-10^{-4})\); \(\sigma_{BTC}=0.55,\sigma_{ETH}=0.70\)
**Card verdict (both headlines):** `REDUNDANT / FAIL-INSUFFICIENT`
**Reason:** no headline cell improves both ΔBrier and ΔLogLoss vs mid; REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)

### Headline cells (λ=0.35 scored)

| Cell | N | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | mean(m) | mean(p) | ECE | Verdict |
|------|--:|------------:|-------------:|-------:|--------------:|---------------:|---------:|--------:|--------:|-----|---------|
| `KALSHI|15m|BTC|T-5m|mid` | 569 | 0.144608 | 0.141266 | 0.003343 | 0.448560 | 0.434744 | 0.013816 | 0.5055 | 0.5103 | 0.061986 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 545 | 0.138267 | 0.134160 | 0.004107 | 0.434318 | 0.415843 | 0.018475 | 0.4879 | 0.4952 | 0.054311 | `REDUNDANT / FAIL-INSUFFICIENT` |

- `KALSHI|15m|BTC|T-5m|mid` WR (descriptive): `0.7926` N_WR=569 CI=[0.7574, 0.8239] (Wilson 95%); mean(S_t)=78858.036380; mean(K)=78849.331670; mean(σ)=0.550000
- `KALSHI|15m|ETH|T-5m|mid` WR (descriptive): `0.8000` N_WR=545 CI=[0.7644, 0.8314] (Wilson 95%); mean(S_t)=2482.960679; mean(K)=2482.801780; mean(σ)=0.700000
- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no action rule / no trading)

### Annex — other four cells (same frozen map; not headline)

| Cell | N | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | mean(m) | mean(p) | ECE | Verdict |
|------|--:|------------:|-------------:|-------:|--------------:|---------------:|---------:|--------:|--------:|-----|---------|
| `KALSHI|15m|BTC|T-14m|mid` | 604 | 0.235962 | 0.234728 | 0.001234 | 0.665918 | 0.662648 | 0.003270 | 0.5049 | 0.5089 | 0.044767 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 604 | 0.234605 | 0.232936 | 0.001669 | 0.662871 | 0.658864 | 0.004006 | 0.5029 | 0.5077 | 0.045203 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-10m|mid` | 604 | 0.201014 | 0.198177 | 0.002837 | 0.588420 | 0.581969 | 0.006451 | 0.5109 | 0.5134 | 0.057015 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-10m|mid` | 604 | 0.201065 | 0.198214 | 0.002851 | 0.586830 | 0.579565 | 0.007265 | 0.5025 | 0.5082 | 0.034719 | `REDUNDANT / FAIL-INSUFFICIENT` |

### Robustness annex (λ grid + placebos; do not pick winner)

**KALSHI|15m|BTC|T-5m|mid**

| Variant | N | ΔBrier | ΔLogLoss | Brier_model | LogLoss_model | Verdict |
|---------|--:|-------:|---------:|------------:|--------------:|---------|
| `λ=0.2` | 569 | 0.001135 | 0.005748 | 0.142401 | 0.440492 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `λ=0.35` | 569 | 0.003343 | 0.013816 | 0.144608 | 0.448560 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `λ=0.5` | 569 | 0.006713 | 0.024282 | 0.147978 | 0.459026 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `λ=0 (must Δ≈0)` | 569 | 0.000000 | 0.000000 | 0.141266 | 0.434744 | `REDUNDANT / FAIL-INSUFFICIENT` |

**KALSHI|15m|ETH|T-5m|mid**

| Variant | N | ΔBrier | ΔLogLoss | Brier_model | LogLoss_model | Verdict |
|---------|--:|-------:|---------:|------------:|--------------:|---------|
| `λ=0.2` | 545 | 0.001532 | 0.008379 | 0.135692 | 0.424222 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `λ=0.35` | 545 | 0.004107 | 0.018475 | 0.138267 | 0.434318 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `λ=0.5` | 545 | 0.007904 | 0.030926 | 0.142063 | 0.446769 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `λ=0 (must Δ≈0)` | 545 | 0.000000 | 0.000000 | 0.134160 | 0.415843 | `REDUNDANT / FAIL-INSUFFICIENT` |

## Card 2 — FEAT-20260912-002 (RV σ digital)

**Frozen map (headline, no-fit):** same Φ blend; \(\sigma_t=\mathrm{RMS}_{W=60}(r_i)\times\sqrt{365.25\cdot24\cdot60}\); no frozen-σ fallback
**Card verdict (both headlines):** `REDUNDANT / FAIL-INSUFFICIENT`
**Reason:** no headline cell improves both ΔBrier and ΔLogLoss vs mid; REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)

### Headline cells (λ=0.35 scored)

| Cell | N | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | mean(m) | mean(p) | ECE | Verdict |
|------|--:|------------:|-------------:|-------:|--------------:|---------------:|---------:|--------:|--------:|-----|---------|
| `KALSHI|15m|BTC|T-5m|mid` | 569 | 0.142338 | 0.141266 | 0.001072 | 0.437261 | 0.434744 | 0.002517 | 0.5055 | 0.5090 | 0.037389 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 545 | 0.135376 | 0.134160 | 0.001216 | 0.419548 | 0.415843 | 0.003705 | 0.4879 | 0.4941 | 0.020252 | `REDUNDANT / FAIL-INSUFFICIENT` |

- `KALSHI|15m|BTC|T-5m|mid` WR (descriptive): `0.7926` N_WR=569 CI=[0.7574, 0.8239] (Wilson 95%); mean(S_t)=78858.036380; mean(K)=78849.331670; mean(σ)=0.267920
- `KALSHI|15m|ETH|T-5m|mid` WR (descriptive): `0.8037` N_WR=545 CI=[0.7682, 0.8348] (Wilson 95%); mean(S_t)=2482.960679; mean(K)=2482.801780; mean(σ)=0.371452
- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no action rule / no trading)

### Annex — other four cells (same frozen map; not headline)

| Cell | N | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | mean(m) | mean(p) | ECE | Verdict |
|------|--:|------------:|-------------:|-------:|--------------:|---------------:|---------:|--------:|--------:|-----|---------|
| `KALSHI|15m|BTC|T-14m|mid` | 604 | 0.235277 | 0.234728 | 0.000548 | 0.664149 | 0.662648 | 0.001500 | 0.5049 | 0.5096 | 0.030947 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 604 | 0.234354 | 0.232936 | 0.001418 | 0.662013 | 0.658864 | 0.003149 | 0.5029 | 0.5098 | 0.041674 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-10m|mid` | 604 | 0.197668 | 0.198177 | -0.000509 | 0.580161 | 0.581969 | -0.001808 | 0.5109 | 0.5133 | 0.041735 | `INCREMENTAL_RESEARCH` |
| `KALSHI|15m|ETH|T-10m|mid` | 604 | 0.199673 | 0.198214 | 0.001459 | 0.582633 | 0.579565 | 0.003068 | 0.5025 | 0.5088 | 0.017632 | `REDUNDANT / FAIL-INSUFFICIENT` |

### Robustness annex (λ grid + placebos; do not pick winner)

**KALSHI|15m|BTC|T-5m|mid**

| Variant | N | ΔBrier | ΔLogLoss | Brier_model | LogLoss_model | Verdict |
|---------|--:|-------:|---------:|------------:|--------------:|---------|
| `λ=0.2` | 569 | 0.000266 | 0.000599 | 0.141531 | 0.435342 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `λ=0.35` | 569 | 0.001072 | 0.002517 | 0.142338 | 0.437261 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `λ=0.5` | 569 | 0.002399 | 0.005714 | 0.143664 | 0.440458 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `λ=0 (must Δ≈0)` | 569 | 0.000000 | 0.000000 | 0.141266 | 0.434744 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `placebo_shuffle_σ_t` | 569 | 0.004114 | 0.012670 | 0.145380 | 0.447413 | `REDUNDANT / FAIL-INSUFFICIENT` |

**KALSHI|15m|ETH|T-5m|mid**

| Variant | N | ΔBrier | ΔLogLoss | Brier_model | LogLoss_model | Verdict |
|---------|--:|-------:|---------:|------------:|--------------:|---------|
| `λ=0.2` | 545 | 0.000445 | 0.001477 | 0.134605 | 0.417320 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `λ=0.35` | 545 | 0.001216 | 0.003705 | 0.135376 | 0.419548 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `λ=0.5` | 545 | 0.002361 | 0.006846 | 0.136521 | 0.422690 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `λ=0 (must Δ≈0)` | 545 | 0.000000 | 0.000000 | 0.134160 | 0.415843 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `placebo_shuffle_σ_t` | 545 | 0.002002 | 0.007488 | 0.136162 | 0.423331 | `REDUNDANT / FAIL-INSUFFICIENT` |

## RV earn-keep (002 vs 001 on headlines)

| Cell | N_001 | N_002 | ΔBrier_001 | ΔBrier_002 | ΔLogLoss_001 | ΔLogLoss_002 | 002 earns keep? |
|------|------:|------:|-----------:|-----------:|-------------:|-------------:|:----------------|
| `KALSHI|15m|BTC|T-5m|mid` | 569 | 569 | 0.003343 | 0.001072 | 0.013816 | 0.002517 | **True** |
| `KALSHI|15m|ETH|T-5m|mid` | 545 | 545 | 0.004107 | 0.001216 | 0.018475 | 0.003705 | **True** |

**RV package note:** FEAT-002 has strictly better (more negative) ΔBrier and ΔLogLoss than FEAT-001 on both headline cells (same-N) — RV earns keep vs sister. Both cards still fail vs mid on headlines (both Δ≥0) → package REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE); no third card; no trading.

## Filter / join stats
```json
{
  "candidates": 3624,
  "excluded_method_not_mid": 0,
  "excluded_near_deg": 94,
  "excluded_no_label": 0,
  "excluded_void_or_other": 0,
  "excluded_missing_floor_strike": 0,
  "excluded_missing_S_t": 0,
  "excluded_join_lag_gt_90s": 0,
  "mid_reconstruct_mismatch": 0,
  "join_open_eq_decision_minus_60s": 3530,
  "join_open_ne_decision_minus_60s": 0,
  "scored_base_with_S_t": 3530,
  "expiration_value_read": false,
  "incomplete_bar_used": false,
  "void_bucket_n": 0,
  "void_bucket": []
}
```

## Integrity

- checkpoints.ndjson sha256: `90e38c2f23e224def13db05924f6470a1e738778882f6b0cc17ed708b3143765`
- expected: `90e38c2f23e224def13db05924f6470a1e738778882f6b0cc17ed708b3143765`
- sha256_verified: `True`
- venues: `{'KALSHI': 6040}`
- EXPIRATION_VALUE: **not read / not scored**
- incomplete-bar close: **not used**
- LAST_PRICE / OUTCOME_PRICES as m_t: **forbidden / not used**
- Binance L3: external predictor only — **NOT** settlement oracle
- No MLE; no ensemble of 001+002; trading FORBIDDEN
- join open==decision−60s: `3530`
- join open≠decision−60s: `0`

## Overall package verdict
**`REDUNDANT / FAIL-INSUFFICIENT`** — Neither atomic F1 card improves both Brier and LogLoss vs mid on both headline T-5m cells. FEAT-001=REDUNDANT / FAIL-INSUFFICIENT; FEAT-002=REDUNDANT / FAIL-INSUFFICIENT. RV earns keep on any headline=True. REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE). USED_RESEARCH; holdout closed; no trading.

FAIL-INSUFFICIENT ≠ NO_EDGE. This is **not** a strategy PASS. No trading authorization. Holdout closed.

## Artifacts
- `/workspace/lab/harness/examiner/out/TEST-20260912-002-F1-INCREMENTAL.json`
- `/workspace/lab/harness/examiner/out/TEST-20260912-002-F1-INCREMENTAL.md`
- `/workspace/lab/archive/tests/TEST-20260912-002-F1-INCREMENTAL.json`
- `/workspace/lab/archive/tests/TEST-20260912-002-F1-INCREMENTAL.md`
- `/workspace/lab/archive/tests/TEST-20260912-002.json`
- `/workspace/lab/archive/tests/TEST-20260912-002.md`
- `/workspace/lab/archive/audit/2026-09-12-TEST-20260912-002-F1-INCREMENTAL-examiner.md`
