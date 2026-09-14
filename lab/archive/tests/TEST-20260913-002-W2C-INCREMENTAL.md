# TEST-20260913-002 — W2C-INCREMENTAL vs MKT-KALSHI-15M-MID

**TEST_ID:** `TEST-20260913-002`
**Package:** `W2C-INCREMENTAL`
**Feature:** `DRAFT-FEAT-20260913-001` (sibling same-window mid blend, λ=0.25 frozen)
**Gate:** `DRAFT-ABST-20260913-001` (speak only on ALLOW_SPEAK_HEADLINE)
**Incumbent:** `MKT-KALSHI-15M-MID` (TEST-20260911-007 mid-only)
**Purpose:** W2-C sibling-mid incrementality vs Kalshi mid on two AMD-005 headlines
**DATA:** `DATA-PROV-PM-003` checkpoints + PM-001 OPEN/CLOSE + labels
**Join:** DATA_VERDICT_W2C_SIBLING_JOIN CLEARED (join only)
**Slice use:** USED_RESEARCH — not validation, not sealed holdout
**Overall verdict:** `REDUNDANT / FAIL-INSUFFICIENT`
**invented_numbers:** `False`
**Trading:** FORBIDDEN
**PM-002 / Poly / CF / L3 / EXPIRATION_VALUE:** not used
**Annex `KALSHI|15m|BTC|T-14m|mid`:** DARK — not scored as speak
**Run UTC:** `2026-09-13T19:16:40Z`
**SHA256 verified:** `True`

## Authority
- `governance/EXAMINER_ORDER_TEST-20260913-002-W2C.md`
- `archive/features/DRAFT-FEAT-20260913-001-W2C-sibling-mid.md`
- `archive/features/DRAFT-ABST-20260913-001-W2C-bad-cal.md`
- `data/DATA-PROV-PM-003/provenance/DATA_VERDICT_W2C_SIBLING_JOIN.md`

## Frozen map
- On ABSTAIN or missing sibling: p_t = m_t
- On ALLOW_SPEAK_HEADLINE: p_t = clip((1-0.25)*m_t + 0.25*m*_t, 0.0001, 1-0.0001)
- m*_t = opposite-asset same OPEN/CLOSE same rem mid (Clock-certified)
- Scored λ=0.25 only. Robustness λ∈[0.15, 0.25, 0.35] annex — do not pick winner.
- λ=0 diagnostic must give Δ=0.

## Filters / join
- venue=KALSHI, window=15m; BTC/ETH **separate** (no pool)
- DATA-PROV-PM-003 1208-slice only — **no** PM-002 union
- `implied_p_method == mid` only; last-fallback excluded
- exclude `implied_p ≤ 0.02` or `≥ 0.98` (near-deg) on **both** sides
- VOID/DISPUTED out of scored N / sibling → missing
- Sibling key: same OPEN_TIME + CLOSE_TIME + rem; same decision_time
- Missing sibling → fail-closed p_t := m_t
- No Poly. No CF. No L3. No EXPIRATION_VALUE. No in-sample refit.

**Sign convention:** ΔBrier = Brier_model − Brier_market; ΔLogLoss = LogLoss_model − LogLoss_market; **negative = skill** vs mid.

**Skill rule:** both Δ < 0 on a headline. Kill if either Δ ≥ 0, N < 80, or one headline works and the other inverts. Not NO_EDGE. Not Champion.

## Overall reason
One headline works (KALSHI|15m|BTC|T-10m|mid) and the other fails/inverts (KALSHI|15m|ETH|T-14m|mid: ΔBrier=0.00047974441225165365, ΔLogLoss=0.0009467020672918602, N=604). Kill — no pooled rescue. REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE; not Champion). USED_RESEARCH; holdout closed; no trading.

## Headlines (AMD-005, no pool)

| Cell | N | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | mean(m) | mean(p) | mean(m*) | ECE | Verdict |
|------|--:|------------:|-------------:|-------:|--------------:|---------------:|---------:|--------:|--------:|---------:|-----|---------|
| `KALSHI|15m|ETH|T-14m|mid` | 604 | 0.233416 | 0.232936 | 0.000480 | 0.659811 | 0.658864 | 0.000947 | 0.5029 | 0.5034 | 0.5049 | 0.044845 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-10m|mid` | 604 | 0.197532 | 0.198177 | -0.000645 | 0.580089 | 0.581969 | -0.001880 | 0.5109 | 0.5088 | 0.5025 | 0.028385 | `INCREMENTAL_RESEARCH` |

### `KALSHI|15m|ETH|T-14m|mid`
- n_speak=604; fail_closed_missing_sibling=0
- Reason: ΔBrier≥0 and ΔLogLoss≥0 vs mid-only on headline; REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)
- Calibration: powered bins present; ECE on p_t (model)
- ECE_market: 0.047409
- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no trading)

### `KALSHI|15m|BTC|T-10m|mid`
- n_speak=604; fail_closed_missing_sibling=0
- Reason: both ΔBrier<0 and ΔLogLoss<0 vs mid-only on USED_RESEARCH; not validation; not sealed holdout; not trading; not Champion
- Calibration: powered bins present; ECE on p_t (model)
- ECE_market: 0.041487
- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no trading)

## Robustness annex (λ∈{0.15,0.25,0.35}; not headline; do not pick winner)

| Cell | λ | N | ΔBrier | ΔLogLoss | Verdict |
|------|--:|--:|-------:|---------:|---------|
| `KALSHI|15m|ETH|T-14m|mid` | 0.15 | 604 | 0.000236 | 0.000458 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.25 | 604 | 0.000480 | 0.000947 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.35 | 604 | 0.000793 | 0.001580 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-10m|mid` | 0.15 | 604 | -0.000574 | -0.001532 | `INCREMENTAL_RESEARCH` |
| `KALSHI|15m|BTC|T-10m|mid` | 0.25 | 604 | -0.000645 | -0.001880 | `INCREMENTAL_RESEARCH` |
| `KALSHI|15m|BTC|T-10m|mid` | 0.35 | 604 | -0.000469 | -0.001706 | `INCREMENTAL_RESEARCH` |

## Placebos (report, not headline switch)

| Placebo | Cell | N | ΔBrier | ΔLogLoss | Notes |
|---------|------|--:|-------:|---------:|-------|
| `shuffle_mstar_within_cell` | `KALSHI|15m|ETH|T-14m|mid` | 604 | 0.002488 | 0.004862 | m* shuffled within cell; m fixed |
| `shuffle_mstar_within_cell` | `KALSHI|15m|BTC|T-10m|mid` | 604 | 0.007692 | 0.017759 | m* shuffled within cell; m fixed |
| `lambda_0` | `KALSHI|15m|ETH|T-14m|mid` | 604 | 0.000000 | 0.000000 | λ=0 identity check pass=True |
| `lambda_0` | `KALSHI|15m|BTC|T-10m|mid` | 604 | 0.000000 | 0.000000 | λ=0 identity check pass=True |
| `wrong_window_sibling` | `KALSHI|15m|ETH|T-14m|mid` | 604 | 0.000813 | 0.001240 | opposite-asset same rem, different OPEN/CLOSE |
| `wrong_window_sibling` | `KALSHI|15m|BTC|T-10m|mid` | 604 | 0.002632 | 0.006446 | opposite-asset same rem, different OPEN/CLOSE |

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
  "n_fail_closed_missing_sibling": 0,
  "per_cell": {
    "KALSHI|15m|ETH|T-14m|mid": {
      "candidates": 604,
      "scored": 604,
      "speak": 604,
      "fail_closed": 0,
      "excluded_method_not_mid": 0,
      "excluded_near_deg": 0,
      "excluded_void": 0
    },
    "KALSHI|15m|BTC|T-10m|mid": {
      "candidates": 604,
      "scored": 604,
      "speak": 604,
      "fail_closed": 0,
      "excluded_method_not_mid": 0,
      "excluded_near_deg": 0,
      "excluded_void": 0
    }
  },
  "annex_dark_not_scored": "KALSHI|15m|BTC|T-14m|mid",
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
- PM-002 / Poly / CF / L3 / EXPIRATION_VALUE: **not used**
- m_t / m*: PM-003 checkpoint mid only
- No λ retune; no gate retune; no annex sneak; no pool

## Overall package verdict
**`REDUNDANT / FAIL-INSUFFICIENT`** — One headline works (KALSHI|15m|BTC|T-10m|mid) and the other fails/inverts (KALSHI|15m|ETH|T-14m|mid: ΔBrier=0.00047974441225165365, ΔLogLoss=0.0009467020672918602, N=604). Kill — no pooled rescue. REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE; not Champion). USED_RESEARCH; holdout closed; no trading.

FAIL-INSUFFICIENT ≠ NO_EDGE. This is **not** a Champion / strategy PASS. No trading authorization. Holdout closed.

## Artifacts
- `/workspace/lab/harness/examiner/out/TEST-20260913-002-W2C-INCREMENTAL.json`
- `/workspace/lab/harness/examiner/out/TEST-20260913-002-W2C-INCREMENTAL.md`
- `/workspace/lab/archive/tests/TEST-20260913-002-W2C-INCREMENTAL.json`
- `/workspace/lab/archive/tests/TEST-20260913-002-W2C-INCREMENTAL.md`
- `/workspace/lab/archive/tests/TEST-20260913-002.json`
- `/workspace/lab/archive/tests/TEST-20260913-002.md`
- `/workspace/lab/archive/audit/2026-09-13-TEST-20260913-002-W2C-INCREMENTAL-examiner.md`
