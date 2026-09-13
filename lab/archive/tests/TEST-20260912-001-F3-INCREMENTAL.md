# TEST-20260912-001 — F3-INCREMENTAL vs MKT-KALSHI-15M-MID

**TEST_ID:** `TEST-20260912-001`
**Package:** `F3-INCREMENTAL`
**Incumbent:** `MKT-KALSHI-15M-MID` (TEST-20260911-007 mid-only)
**Purpose:** atomic incrementality of two F3 frozen no-fit maps vs Kalshi mid
**DATA:** `DATA-PROV-PM-003` checkpoints + PM-001 official resolution labels
**Slice use:** USED_RESEARCH — not validation, not sealed holdout
**Overall verdict:** `REDUNDANT / FAIL-INSUFFICIENT`
**invented_numbers:** `False`
**Trading:** FORBIDDEN
**MLE / ensemble 003+004:** forbidden and not run
**PM-002 / Poly / L3:** not read / not scored
**Run UTC:** `2026-09-12T00:14:22Z`
**SHA256 verified:** `True`

## Authority
- `governance/EXAMINER_ORDER_TEST-20260912-001-F3.md`
- `archive/features/FEAT-20260912-003.md`
- `archive/features/FEAT-20260912-004.md`
- `governance/FEATURE_WAVE_001_2026-09-12.md`
- `governance/BINARY_EXAMINER_SPEC.md`
- `harness/examiner/src/pm002_market_baseline.py`
- `harness/examiner/src/run_pm003_market_baseline.py`

## Filters (same as TEST-007 + feature-field drops)
- venue=KALSHI, window=15m; BTC/ETH **separate** (no pool)
- DATA-PROV-PM-003 1208-slice only — **no** PM-002 union
- checkpoints: T-14m (840), T-10m (600), T-5m (300)
- `implied_p_method == mid` only; last-fallback excluded
- exclude `implied_p ≤ 0.02` or `≥ 0.98` (near-deg)
- VOID/DISPUTED out of scored N
- FEAT-003: missing bid/ask → drop; FEAT-004: missing last → drop
- m_t = checkpoint `implied_p` (equals (yes_bid+yes_ask)/2 on mid)
- **Do not** use PM-001 `LAST_PRICE_DOLLARS` / `OUTCOME_PRICES` / `EXPIRATION_VALUE`
- No Poly. No L3. No Funding/OI. No in-sample refit.

**Sign convention:** ΔBrier = Brier_model − Brier_market; ΔLogLoss = LogLoss_model − LogLoss_market; **negative = skill** vs mid.

**Falsification (primary):** if ΔBrier≥0 **and** ΔLogLoss≥0 → `REDUNDANT / FAIL-INSUFFICIENT` (not `NO_EDGE`). Skill requires **both** Δ < 0.

**Headline cell (pre-registered, no post-hoc switch):** `KALSHI|15m|BTC|T-5m|mid`
Other five cells = annex, reported separately, same frozen parameters.

## Card 1 — FEAT-20260912-003 (YES touch spread)

**Frozen map (headline, no-fit):** \(s_t=\mathrm{yes\_ask}-\mathrm{yes\_bid}\); \(\lambda=\mathrm{clip}(s_t/0.05,0,1)\); \(p_t=(1-\lambda)m_t+\lambda\cdot 0.5\)
**Primary verdict:** `REDUNDANT / FAIL-INSUFFICIENT`
**Reason:** ΔBrier≥0 and ΔLogLoss≥0 vs mid-only on primary/cell; REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)

### Primary headline — `KALSHI|15m|BTC|T-5m|mid`

| Cell | N | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | mean(m_t) | mean(p_t) | abstention | ECE | Verdict |
|------|--:|------------:|-------------:|-------:|--------------:|---------------:|---------:|----------:|----------:|:-----------|-----|---------|
| `KALSHI|15m|BTC|T-5m|mid` | 569 | 0.142594 | 0.141266 | 0.001328 | 0.439402 | 0.434744 | 0.004658 | 0.5055 | 0.5069 | none | 0.039247 | `REDUNDANT / FAIL-INSUFFICIENT` |

- WR (descriptive, optional): `0.7944` N_WR=569 CI=[0.7592, 0.8256] (Wilson 95%)
- mean(s_t)=0.007209; mean(|δ_t|)=0.003938
- gap mean(p_t−m_t)=0.001406
- Calibration: powered bins present; ECE on p_t
- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no action rule / no trading)

### Annex — other five cells (same frozen map; not headline)

| Cell | N | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | mean(m_t) | mean(p_t) | ECE | Verdict |
|------|--:|------------:|-------------:|-------:|--------------:|---------------:|---------:|----------:|----------:|-----|---------|
| `KALSHI|15m|BTC|T-14m|mid` | 604 | 0.236139 | 0.234728 | 0.001410 | 0.665196 | 0.662648 | 0.002548 | 0.5049 | 0.5041 | 0.062278 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 604 | 0.234652 | 0.232936 | 0.001716 | 0.661983 | 0.658864 | 0.003119 | 0.5029 | 0.5026 | 0.069967 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-10m|mid` | 604 | 0.201528 | 0.198177 | 0.003351 | 0.590656 | 0.581969 | 0.008687 | 0.5109 | 0.5086 | 0.058274 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-10m|mid` | 604 | 0.201154 | 0.198214 | 0.002940 | 0.587486 | 0.579565 | 0.007921 | 0.5025 | 0.5023 | 0.043330 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 545 | 0.137330 | 0.134160 | 0.003170 | 0.427723 | 0.415843 | 0.011880 | 0.4879 | 0.4898 | 0.051971 | `REDUNDANT / FAIL-INSUFFICIENT` |

### Robustness annex (not headline; no post-hoc switch)

| Variant | N | ΔBrier | ΔLogLoss | Brier_model | LogLoss_model | Verdict |
|---------|--:|-------:|---------:|------------:|--------------:|---------|
| `s0=0.02` | 569 | 0.009807 | 0.026900 | 0.151072 | 0.461644 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `s0=0.1` | 569 | 0.000232 | 0.001048 | 0.141497 | 0.435792 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `placebo_shuffle_s_t` | 569 | 0.003566 | 0.017177 | 0.144831 | 0.451920 | `REDUNDANT / FAIL-INSUFFICIENT` |

## Card 2 — FEAT-20260912-004 (last−mid disagreement)

**Frozen map (headline, no-fit):** \(\delta_t=\mathrm{last}-m_t\); \(p_t=\mathrm{clip}(m_t+1.0\cdot\delta_t,\,10^{-4},\,1-10^{-4})\)
**Primary verdict:** `REDUNDANT / FAIL-INSUFFICIENT`
**Reason:** ΔBrier≥0 and ΔLogLoss≥0 vs mid-only on primary/cell; REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)

### Primary headline — `KALSHI|15m|BTC|T-5m|mid`

| Cell | N | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | mean(m_t) | mean(p_t) | abstention | ECE | Verdict |
|------|--:|------------:|-------------:|-------:|--------------:|---------------:|---------:|----------:|----------:|:-----------|-----|---------|
| `KALSHI|15m|BTC|T-5m|mid` | 569 | 0.141630 | 0.141266 | 0.000364 | 0.435779 | 0.434744 | 0.001035 | 0.5055 | 0.5054 | none | 0.026619 | `REDUNDANT / FAIL-INSUFFICIENT` |

- WR (descriptive, optional): `0.7965` N_WR=565 CI=[0.7613, 0.8276] (Wilson 95%)
- mean(s_t)=0.007209; mean(|δ_t|)=0.003938
- gap mean(p_t−m_t)=-0.000116
- Calibration: powered bins present; ECE on p_t
- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no action rule / no trading)

### Annex — other five cells (same frozen map; not headline)

| Cell | N | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | mean(m_t) | mean(p_t) | ECE | Verdict |
|------|--:|------------:|-------------:|-------:|--------------:|---------------:|---------:|----------:|----------:|-----|---------|
| `KALSHI|15m|BTC|T-14m|mid` | 604 | 0.234760 | 0.234728 | 0.000032 | 0.662719 | 0.662648 | 0.000071 | 0.5049 | 0.5053 | 0.038179 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 604 | 0.233172 | 0.232936 | 0.000236 | 0.659378 | 0.658864 | 0.000514 | 0.5029 | 0.5032 | 0.050927 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-10m|mid` | 604 | 0.198763 | 0.198177 | 0.000586 | 0.583149 | 0.581969 | 0.001180 | 0.5109 | 0.5110 | 0.040743 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-10m|mid` | 604 | 0.198531 | 0.198214 | 0.000317 | 0.580325 | 0.579565 | 0.000760 | 0.5025 | 0.5029 | 0.029101 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 545 | 0.133937 | 0.134160 | -0.000223 | 0.415341 | 0.415843 | -0.000502 | 0.4879 | 0.4883 | 0.029222 | `INCREMENTAL_RESEARCH` |

### Robustness annex (not headline; no post-hoc switch)

| Variant | N | ΔBrier | ΔLogLoss | Brier_model | LogLoss_model | Verdict |
|---------|--:|-------:|---------:|------------:|--------------:|---------|
| `kappa=0.5` | 569 | 0.000171 | 0.000497 | 0.141437 | 0.435241 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `kappa=2.0` | 569 | 0.000815 | 0.002240 | 0.142080 | 0.436984 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `placebo_signflip_delta` | 569 | -0.000278 | -0.000861 | 0.140987 | 0.433882 | `INCREMENTAL_RESEARCH` |

## Filter / join stats (shared mid universe, TEST-007 excludes)
```json
{
  "candidates": 3624,
  "excluded_method_not_mid": 0,
  "excluded_near_deg": 94,
  "excluded_no_label": 0,
  "excluded_void_or_other": 0,
  "excluded_missing_bid_ask": 0,
  "mid_reconstruct_mismatch": 0,
  "scored": 3530,
  "void_bucket_n": 0,
  "void_bucket": []
}
```

## Integrity

- checkpoints.ndjson sha256: `90e38c2f23e224def13db05924f6470a1e738778882f6b0cc17ed708b3143765`
- expected: `90e38c2f23e224def13db05924f6470a1e738778882f6b0cc17ed708b3143765`
- sha256_verified: `True`
- venues: `{'KALSHI': 6040}`
- PM-002 checkpoint rows: **not read / not scored**
- Poly: **none**
- L3 / Funding / OI: **not used**
- m_t source: PM-003 `checkpoints.implied_p` (mid) — never PM-001 LAST_PRICE / OUTCOME_PRICES
- No MLE; no α,β,γ; no ensemble of 003+004

## Overall package verdict
**`REDUNDANT / FAIL-INSUFFICIENT`** — Neither atomic F3 card improves both Brier and LogLoss vs mid on primary KALSHI|15m|BTC|T-5m|mid. FEAT-003=REDUNDANT / FAIL-INSUFFICIENT; FEAT-004=REDUNDANT / FAIL-INSUFFICIENT. REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE). USED_RESEARCH; holdout closed; no trading.

FAIL-INSUFFICIENT ≠ NO_EDGE. This is **not** a strategy PASS. No trading authorization. Holdout closed.

## Artifacts
- `/workspace/lab/harness/examiner/out/TEST-20260912-001-F3-INCREMENTAL.json`
- `/workspace/lab/harness/examiner/out/TEST-20260912-001-F3-INCREMENTAL.md`
- `/workspace/lab/archive/tests/TEST-20260912-001-F3-INCREMENTAL.json`
- `/workspace/lab/archive/tests/TEST-20260912-001-F3-INCREMENTAL.md`
- `/workspace/lab/archive/tests/TEST-20260912-001.json`
- `/workspace/lab/archive/tests/TEST-20260912-001.md`
- `/workspace/lab/archive/audit/2026-09-12-TEST-20260912-001-F3-INCREMENTAL-examiner.md`
