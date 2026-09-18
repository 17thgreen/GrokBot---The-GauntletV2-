# TEST-20260913-007 — W2B-LAST-AT-L-INCREMENTAL vs m_L

**TEST_ID:** `TEST-20260913-007`
**Package:** `W2B-LAST-AT-L-INCREMENTAL`
**Feature:** `DRAFT-FEAT-20260913-007` (Poly last_L vs Kalshi m_L, λ=0.2 w=0.12 ε=0.0001 frozen)
**Gate:** `DRAFT-ABST-20260913-007` (speak only when last_L and m_L exist at L)
**Incumbent:** `m_L` (Kalshi official 1m mid at Poly obs_time L; NOT decision-time mid)
**Purpose:** W2-B last vs mid-at-L incrementality on two T-5m headlines
**DATA:** `DATA-PROV-PM-005` Poly last + `DATA-PROV-PM-003` Kalshi 1m candles for m_L + `DATA-PROV-PM-001` RESOLUTION
**Join:** DATA_VERDICT_W2B_INCUMBENT_AT_OBS **CLEARED** (254/240; incumbent-timestamp certified; 45s lag vs decision_time is honesty, not this incumbent)
**Slice use:** USED_RESEARCH — not validation, not sealed holdout
**Overall verdict:** `REDUNDANT / FAIL-INSUFFICIENT`
**invented_numbers:** `False`
**Trading:** FORBIDDEN
**Stamp:** Join DATA_VERDICT_W2B_INCUMBENT_AT_OBS; incumbent = m_L at Poly obs_time; last ≠ mid; NOT decision-time mid; 004 not retuned; 45s lag honesty. No Map 2. No CF. No sibling. No CB-VEL. No W2-D rem shop. No invented Poly mid.
**Annex:** none (no other rem; robustness λ×w grid report-only — do not pick winner)
**Run UTC:** `2026-09-13T23:38:44Z`
**SHA256 verified:** `True`

## Authority
- `governance/EXAMINER_ORDER_TEST-20260913-007-W2B.md`
- `governance/GOVERNOR_LIFT_EXAMINER_W2B_W006_2026-09-13.md`
- `archive/features/DRAFT-FEAT-20260913-007-W2B-incumbent-at-L.md`
- `archive/features/DRAFT-ABST-20260913-007-W2B-incumbent-at-L.md`
- `data/DATA-PROV-PM-005/provenance/DATA_VERDICT_W2B_INCUMBENT_AT_OBS.md`
- `governance/BINARY_EXAMINER_SPEC.md`

## Frozen map
- ε = 0.0001; λ = 0.2; w = 0.12
- L = Poly last obs_time
- last_L = Poly 15m last (method=last; NOT mid; no invent bid/ask)
- m_L = Kalshi official 1m mid at L: among candles same (asset, OPEN_TIME, CLOSE_TIME) with end_period_ts ≤ unix(L), take argmax end_period_ts; mid only if bid>0, ask>0, bid≤ask; implied_p=round((bid+ask)/2,6); method=mid; price.close/last NEVER as mid; no interpolation; NOT decision-time mid
- b = last_L − m_L
- if ABSTAIN or last_L/m_L missing or mid-rule fails: p = m_L
- else: p = clip(m_L + λ · clip(b, −w, +w), ε, 1−ε) with λ=0.2, w=0.12, ε=0.0001
- Robustness annex λ∈[0.1, 0.2, 0.3] w∈[0.08, 0.12, 0.16] — do not pick winner. λ=0 ⇒ Δ=0 vs m_L.
- **CRITICAL:** Incumbent is m_L. Δ = model − m_L. Do NOT report Δ vs TEST-007 decision-time mid as this instrument (out of scope / UNTESTED).

## Filters / join
- venue=KALSHI, window=15m; BTC/ETH **separate** (no pool)
- Wave 005 T-5m pairable OC-twin set only (rem=300 mid × Poly last OC twin) — **do NOT invent 604**
- Headlines only: T-5m (rem=300); **no annex**
- Kalshi decision-time mid used only for Wave 005 pairable hygiene (method=mid; near-deg exclude); **not** as scored incumbent
- VOID/DISPUTED out of scored N
- m_L via completed_bar_at_L_end_period_ts_le_L on PM-003 candles
- Missing last_L/m_L or mid-rule fail → fail-closed (row excluded or p=m_L)
- **NOT** decision-time mid as incumbent. **NOT** invented Poly mid. **NOT** last-as-mid. **NOT** Map 2. **NOT** CF. **NOT** sibling. **NOT** CB-VEL. **NOT** W2-D.

**Sign convention:** ΔBrier = Brier_model − Brier_m_L; ΔLogLoss = LogLoss_model − LogLoss_m_L; **negative = skill** vs m_L.

**Skill rule:** both Δ < 0 on a headline. Kill if either Δ ≥ 0, N < 80, or one headline works and the other inverts. Not NO_EDGE. Not Champion.

## Overall reason
One headline works (KALSHI|15m|BTC|T-5m|mid) and the other fails/inverts (KALSHI|15m|ETH|T-5m|mid: ΔBrier=0.00032967829166666296, ΔLogLoss=5.667467872116916e-05, N=240). Kill — no pooled rescue. REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE; not Champion). USED_RESEARCH; holdout closed; no trading. Join DATA_VERDICT_W2B_INCUMBENT_AT_OBS; incumbent = m_L at Poly obs_time; last ≠ mid; NOT decision-time mid; 004 not retuned; 45s lag honesty.

## Headlines (AMD-005, no pool, no annex)

| Cell | N | speak N | Brier_model | Brier_m_L | ΔBrier | LogLoss_model | LogLoss_m_L | ΔLogLoss | mean(m_L)_speak | mean(p)_speak | mean(last_L)_speak | speak_rate | ECE | Verdict |
|------|--:|--------:|------------:|----------:|-------:|--------------:|------------:|---------:|---------------:|-------------:|------------------:|-----------:|-----|---------|
| `KALSHI|15m|BTC|T-5m|mid` | 254 | 254 | 0.156074 | 0.156763 | -0.000690 | 0.472849 | 0.474667 | -0.001818 | 0.5100 | 0.5095 | 0.5075 | 1.0000 | 0.017271 | `PROMISING` |
| `KALSHI|15m|ETH|T-5m|mid` | 240 | 240 | 0.148469 | 0.148140 | 0.000330 | 0.467085 | 0.467028 | 0.000057 | 0.4779 | 0.4776 | 0.4776 | 1.0000 | 0.029180 | `REDUNDANT / FAIL-INSUFFICIENT` |

### `KALSHI|15m|BTC|T-5m|mid`
- n_speak=254; n_abstain=0; fail_closed_missing=0; speak_rate=1.0000
- mean(m_L)_all=0.5100; mean(p)_all=0.5095; mean(last_L)_speak=0.5075; mean(b)_speak=-0.0025; mean(obs_lag_sec)=44.20
- Reason: both ΔBrier<0 and ΔLogLoss<0 vs m_L on USED_RESEARCH; not validation; not sealed holdout; not trading; not Champion; NOT vs decision-time mid
- Calibration: powered bins present; ECE on p_t (model)
- ECE_market (vs m_L): 0.018549
- Δ vs decision-time mid: **UNTESTED / out of scope** (not this instrument)
- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no trading)

### `KALSHI|15m|ETH|T-5m|mid`
- n_speak=240; n_abstain=0; fail_closed_missing=0; speak_rate=1.0000
- mean(m_L)_all=0.4779; mean(p)_all=0.4776; mean(last_L)_speak=0.4776; mean(b)_speak=-0.0003; mean(obs_lag_sec)=44.18
- Reason: ΔBrier≥0 and ΔLogLoss≥0 vs m_L on headline; REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)
- Calibration: powered bins present; ECE on p_t (model)
- ECE_market (vs m_L): 0.030285
- Δ vs decision-time mid: **UNTESTED / out of scope** (not this instrument)
- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no trading)

## Robustness annex (λ×w grids; not headline; do not pick winner)

| Cell | λ | w | N | ΔBrier | ΔLogLoss | Verdict |
|------|--:|--:|--:|-------:|---------:|---------|
| `KALSHI|15m|BTC|T-5m|mid` | 0.1 | 0.08 | 254 | -0.000327 | -0.000884 | `PROMISING` |
| `KALSHI|15m|BTC|T-5m|mid` | 0.1 | 0.12 | 254 | -0.000356 | -0.000943 | `PROMISING` |
| `KALSHI|15m|BTC|T-5m|mid` | 0.1 | 0.16 | 254 | -0.000405 | -0.001050 | `PROMISING` |
| `KALSHI|15m|BTC|T-5m|mid` | 0.2 | 0.08 | 254 | -0.000635 | -0.001712 | `PROMISING` |
| `KALSHI|15m|BTC|T-5m|mid` | 0.2 | 0.12 | 254 | -0.000690 | -0.001818 | `PROMISING` |
| `KALSHI|15m|BTC|T-5m|mid` | 0.2 | 0.16 | 254 | -0.000783 | -0.002021 | `PROMISING` |
| `KALSHI|15m|BTC|T-5m|mid` | 0.3 | 0.08 | 254 | -0.000926 | -0.002485 | `PROMISING` |
| `KALSHI|15m|BTC|T-5m|mid` | 0.3 | 0.12 | 254 | -0.001000 | -0.002628 | `PROMISING` |
| `KALSHI|15m|BTC|T-5m|mid` | 0.3 | 0.16 | 254 | -0.001134 | -0.002917 | `PROMISING` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.1 | 0.08 | 240 | 0.000124 | -0.000090 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.1 | 0.12 | 240 | 0.000152 | -0.000017 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.1 | 0.16 | 240 | 0.000150 | -0.000010 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.2 | 0.08 | 240 | 0.000268 | -0.000098 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.2 | 0.12 | 240 | 0.000330 | 0.000057 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.2 | 0.16 | 240 | 0.000326 | 0.000073 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.3 | 0.08 | 240 | 0.000432 | -0.000028 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.3 | 0.12 | 240 | 0.000532 | 0.000218 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.3 | 0.16 | 240 | 0.000529 | 0.000245 | `REDUNDANT / FAIL-INSUFFICIENT` |

## Placebos (report, not headline switch)

| Placebo | Cell | N | ΔBrier | ΔLogLoss | Notes |
|---------|------|--:|-------:|---------:|-------|
| `lambda_0` | `KALSHI|15m|BTC|T-5m|mid` | 254 | 0.000000 | 0.000000 | λ=0 identity check pass=True |
| `lambda_0` | `KALSHI|15m|ETH|T-5m|mid` | 240 | 0.000000 | 0.000000 | λ=0 identity check pass=True |
| `shuffle_last_L` | `KALSHI|15m|BTC|T-5m|mid` | 254 | 0.000780 | 0.004122 | last_L shuffled within cell; m_L fixed |
| `shuffle_last_L` | `KALSHI|15m|ETH|T-5m|mid` | 240 | 0.000101 | -0.001603 | last_L shuffled within cell; m_L fixed |
| `flip_sign_b` | `KALSHI|15m|BTC|T-5m|mid` | 254 | 0.000781 | 0.002100 | sign of b=last_L−m_L flipped |
| `flip_sign_b` | `KALSHI|15m|ETH|T-5m|mid` | 240 | -0.000230 | 0.000325 | sign of b=last_L−m_L flipped |

- placebo_seed: `20260913`
- λ=0 must give ΔBrier=0 and ΔLogLoss=0 (identity vs m_L).
- Swap incumbent to decision-time mid is **not** this card (held 004 / out of scope) — not scored as a placebo switch.

## Filter / join stats
```json
{
  "candidates": 1208,
  "excluded_method_not_mid": 0,
  "excluded_near_deg": 94,
  "excluded_void_or_other": 0,
  "excluded_no_y": 0,
  "excluded_no_poly_twin": 620,
  "excluded_miss_L": 0,
  "excluded_miss_m_L": 0,
  "excluded_decision_time_bar_forbidden": 0,
  "n_lookahead_discarded": 0,
  "n_last_as_mid": 0,
  "n_used_decision_time_bar": 0,
  "n_m_L_equals_decision_mid": 16,
  "scored": 494,
  "n_speak": 494,
  "n_abstain": 0,
  "wave005_pairable": {
    "BTC": 254,
    "ETH": 240
  },
  "pairable_with_m_L": {
    "BTC": 254,
    "ETH": 240
  },
  "incumbent": "m_L",
  "decision_time_mid_used_as_incumbent": false,
  "join_verdict": "CONDITIONAL / INCUMBENT_AT_OBS_JOIN_CERTIFIED_WITH_CAVEATS",
  "candle_rule": "completed_bar_at_L_end_period_ts_le_L",
  "per_cell": {
    "KALSHI|15m|BTC|T-5m|mid": {
      "candidates": 604,
      "scored": 254,
      "speak": 254,
      "abstain": 0,
      "wave005_pairable": 254,
      "excluded_method_not_mid": 0,
      "excluded_near_deg": 35,
      "excluded_void": 0,
      "excluded_no_poly_twin": 315,
      "excluded_miss_L": 0,
      "excluded_miss_m_L": 0
    },
    "KALSHI|15m|ETH|T-5m|mid": {
      "candidates": 604,
      "scored": 240,
      "speak": 240,
      "abstain": 0,
      "wave005_pairable": 240,
      "excluded_method_not_mid": 0,
      "excluded_near_deg": 59,
      "excluded_void": 0,
      "excluded_no_poly_twin": 305,
      "excluded_miss_L": 0,
      "excluded_miss_m_L": 0
    }
  },
  "CF_used": false,
  "sibling_used": false,
  "cbvel_used": false,
  "w2d_used": false,
  "map2_used": false,
  "poly_mid_invented": false,
  "last_as_mid": false,
  "decision_time_mid_as_incumbent": false,
  "004_retuned": false,
  "void_bucket_n": 0
}
```

## Confirmations
- `invented_numbers`: `False`
- `trading`: `False`
- `decision_time_mid_as_incumbent`: `False`
- `poly_mid_invented`: `False`
- `last_as_mid`: `False`
- `map2_used`: `False`
- `CF_used`: `False`
- `sibling_used`: `False`
- `cbvel_used`: `False`
- `w2d_used`: `False`
- `004_retuned`: `False`
- `join_stamped`: `DATA_VERDICT_W2B_INCUMBENT_AT_OBS`
- `coverage_BTC`: `254`
- `coverage_ETH`: `240`
- `lambda0_BTC_pass`: `True`
- `lambda0_ETH_pass`: `True`

## Forbidden actions (not performed)
- in-sample refit
- retune λ/w
- retune gate / annex sneak
- decision-time mid as incumbent
- invented Poly mid / last-as-mid
- Map 2
- CF
- sibling blend
- CB-VEL
- W2-D rem shop
- 004 retune
- PM-002 union
- invent 604 coverage
- trading

## Artifact paths
- `out_json`: `/workspace/lab/harness/examiner/out/TEST-20260913-007-W2B-LAST-AT-L-INCREMENTAL.json`
- `out_md`: `/workspace/lab/harness/examiner/out/TEST-20260913-007-W2B-LAST-AT-L-INCREMENTAL.md`
- `archive_json`: `/workspace/lab/archive/tests/TEST-20260913-007-W2B-LAST-AT-L-INCREMENTAL.json`
- `archive_md`: `/workspace/lab/archive/tests/TEST-20260913-007-W2B-LAST-AT-L-INCREMENTAL.md`
- `archive_audit`: `/workspace/lab/archive/audit/2026-09-13-Examiner-TEST-20260913-007-W2B-LAST-AT-L-INCREMENTAL.md`

---
**Sealed by Examiner** 2026-09-13T23:38:44Z. Verdict `REDUNDANT / FAIL-INSUFFICIENT`. Trade FORBIDDEN. USED_RESEARCH. Holdout closed. Incumbent = m_L. Δ vs decision-time mid = UNTESTED / out of scope.
