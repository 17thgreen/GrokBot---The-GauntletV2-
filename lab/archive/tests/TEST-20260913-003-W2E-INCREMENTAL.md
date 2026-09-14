# TEST-20260913-003 — W2E-INCREMENTAL vs MKT-KALSHI-15M-MID

**TEST_ID:** `TEST-20260913-003`
**Package:** `W2E-INCREMENTAL`
**Feature:** `DRAFT-FEAT-20260913-002` (FLOOR_STRIKE signed distance vs mid, λ=0.25 δ=0.002 frozen; disagreement pull)
**Gate:** `DRAFT-ABST-20260913-002` (speak only on BTC/ETH T-5m mid when FLOOR_STRIKE knowable)
**Incumbent:** `MKT-KALSHI-15M-MID` (TEST-20260911-007 mid-only)
**Purpose:** W2-E strike-distance vs mid incrementality on two AMD-005 headlines
**DATA:** `DATA-PROV-PM-003` + `DATA-PROV-L3-001` + PM-001 FLOOR_STRIKE / RESOLUTION
**Join:** DATA_VERDICT_W2E_STRIKE_L3_JOIN **CONDITIONAL** (L3 ≠ oracle; K revision [A])
**Slice use:** USED_RESEARCH — not validation, not sealed holdout
**Overall verdict:** `REDUNDANT / FAIL-INSUFFICIENT`
**invented_numbers:** `False`
**Trading:** FORBIDDEN
**Stamp:** L3 is **not** the CF/Kalshi settlement oracle. CONDITIONAL join. No CF. No Poly. No EXPIRATION_VALUE. No Φ(z). No sibling blend.
**Annex:** none (no W2-C cells; no other rem)
**Run UTC:** `2026-09-13T19:27:28Z`
**SHA256 verified:** `True`

## Authority
- `governance/EXAMINER_ORDER_TEST-20260913-003-W2E.md`
- `archive/features/DRAFT-FEAT-20260913-002-W2E-strike-vs-mid.md`
- `archive/features/DRAFT-ABST-20260913-002-W2E-rules-strike.md`
- `data/DATA-PROV-L3-001/provenance/DATA_VERDICT_W2E_STRIKE_L3_JOIN.md`

## Frozen map
- d = (S − K) / K
- p_dist = 0.5 + 0.5·clip(d/δ, −1, 1) with δ=0.002; clip to [0.0001, 1−0.0001]
- agree = (d==0) or (m==0.5) or sign(d)==sign(m−0.5)
- if ABSTAIN or missing K/S: p = m
- elif agree: p = m
- else: p = clip((1−0.25)·m + 0.25·p_dist, 0.0001, 1−0.0001)
- λ=0.25, δ=0.002 frozen. Robustness annex λ∈[0.15, 0.25, 0.35] / δ∈[0.001, 0.002, 0.004] — do not pick winner. λ=0 ⇒ Δ=0.

## Filters / join
- venue=KALSHI, window=15m; BTC/ETH **separate** (no pool)
- DATA-PROV-PM-003 1208-slice only — **no** PM-002 union
- Headlines only: T-5m (rem=300); **no annex**
- `implied_p_method == mid` only; last-fallback excluded
- exclude `implied_p ≤ 0.02` or `≥ 0.98` (near-deg)
- VOID/DISPUTED out of scored N
- K = PM-001 `FLOOR_STRIKE` after OPEN (OPEN_TIME ≤ decision_time)
- S_t = L3 completed 1m close: argmax{bar | close_time_ms ≤ decision_time_ms}; lag ≤ 90s
- Missing K or S_t → fail-closed p_t := m_t
- **L3 ≠ oracle.** No CF. No Poly. No EXPIRATION_VALUE. No Φ(z).

**Sign convention:** ΔBrier = Brier_model − Brier_market; ΔLogLoss = LogLoss_model − LogLoss_market; **negative = skill** vs mid.

**Skill rule:** both Δ < 0 on a headline. Kill if either Δ ≥ 0, N < 80, or one headline works and the other inverts. Not NO_EDGE. Not Champion.

## Overall reason
Neither headline improves both Brier and LogLoss vs mid (BTC=REDUNDANT / FAIL-INSUFFICIENT; ETH=REDUNDANT / FAIL-INSUFFICIENT). REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE; not Champion). USED_RESEARCH; holdout closed; no trading. L3 ≠ oracle; CONDITIONAL join.

## Headlines (AMD-005, no pool, no annex)

| Cell | N | speak N | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | mean(m)_speak | mean(p)_speak | mean(d)_speak | speak_rate | ECE | Verdict |
|------|--:|--------:|------------:|-------------:|-------:|--------------:|---------------:|---------:|-------------:|-------------:|-------------:|-----------:|-----|---------|
| `KALSHI|15m|BTC|T-5m|mid` | 569 | 51 | 0.141909 | 0.141266 | 0.000644 | 0.436179 | 0.434744 | 0.001435 | 0.5238 | 0.5177 | -0.000003 | 0.0896 | 0.024553 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 545 | 38 | 0.134464 | 0.134160 | 0.000304 | 0.416486 | 0.415843 | 0.000643 | 0.5008 | 0.5035 | 0.000047 | 0.0697 | 0.027129 | `REDUNDANT / FAIL-INSUFFICIENT` |

### `KALSHI|15m|BTC|T-5m|mid`
- n_speak=51; n_agree=518; fail_closed_missing_KS=0; speak_rate=0.0896
- mean(m)_all=0.5055; mean(p)_all=0.5050; mean(S_t)=78858.036380; mean(K)=78849.331670
- Reason: ΔBrier≥0 and ΔLogLoss≥0 vs mid-only on headline; REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)
- Calibration: powered bins present; ECE on p_t (model)
- ECE_market: 0.024279
- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no trading)

### `KALSHI|15m|ETH|T-5m|mid`
- n_speak=38; n_agree=507; fail_closed_missing_KS=0; speak_rate=0.0697
- mean(m)_all=0.4879; mean(p)_all=0.4881; mean(S_t)=2482.960679; mean(K)=2482.801780
- Reason: ΔBrier≥0 and ΔLogLoss≥0 vs mid-only on headline; REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE)
- Calibration: powered bins present; ECE on p_t (model)
- ECE_market: 0.032856
- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no trading)

## Robustness annex (λ×δ grids; not headline; do not pick winner)

| Cell | λ | δ | N | ΔBrier | ΔLogLoss | Verdict |
|------|--:|--:|--:|-------:|---------:|---------|
| `KALSHI|15m|BTC|T-5m|mid` | 0.15 | 0.001 | 569 | 0.000427 | 0.000962 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-5m|mid` | 0.15 | 0.002 | 569 | 0.000363 | 0.000825 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-5m|mid` | 0.15 | 0.004 | 569 | 0.000334 | 0.000763 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-5m|mid` | 0.25 | 0.001 | 569 | 0.000777 | 0.001714 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-5m|mid` | 0.25 | 0.002 | 569 | 0.000644 | 0.001435 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-5m|mid` | 0.25 | 0.004 | 569 | 0.000587 | 0.001315 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-5m|mid` | 0.35 | 0.001 | 569 | 0.000777 | 0.001714 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-5m|mid` | 0.35 | 0.002 | 569 | 0.000955 | 0.002096 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-5m|mid` | 0.35 | 0.004 | 569 | 0.000862 | 0.001904 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.15 | 0.001 | 545 | 0.000241 | 0.000509 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.15 | 0.002 | 545 | 0.000172 | 0.000368 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.15 | 0.004 | 545 | 0.000140 | 0.000302 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.25 | 0.001 | 545 | 0.000436 | 0.000910 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.25 | 0.002 | 545 | 0.000304 | 0.000643 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.25 | 0.004 | 545 | 0.000245 | 0.000524 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.35 | 0.001 | 545 | 0.000658 | 0.001363 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.35 | 0.002 | 545 | 0.000450 | 0.000943 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.35 | 0.004 | 545 | 0.000360 | 0.000761 | `REDUNDANT / FAIL-INSUFFICIENT` |

## Placebos (report, not headline switch)

| Placebo | Cell | N | ΔBrier | ΔLogLoss | Notes |
|---------|------|--:|-------:|---------:|-------|
| `lambda_0` | `KALSHI|15m|BTC|T-5m|mid` | 569 | 0.000000 | 0.000000 | λ=0 identity check pass=True |
| `lambda_0` | `KALSHI|15m|ETH|T-5m|mid` | 545 | 0.000000 | 0.000000 | λ=0 identity check pass=True |
| `flip_sign_d` | `KALSHI|15m|BTC|T-5m|mid` | 569 | 0.020817 | 0.070915 | sign(d) flipped; should not beat true sign |
| `flip_sign_d` | `KALSHI|15m|ETH|T-5m|mid` | 545 | 0.025436 | 0.085168 | sign(d) flipped; should not beat true sign |
| `shuffle_S` | `KALSHI|15m|BTC|T-5m|mid` | 569 | 0.018066 | 0.049277 | S_t shuffled within cell; K,m fixed |
| `shuffle_S` | `KALSHI|15m|ETH|T-5m|mid` | 545 | 0.022367 | 0.064066 | S_t shuffled within cell; K,m fixed |

- placebo_seed: `20260913`
- λ=0 must give ΔBrier=0 and ΔLogLoss=0 (identity vs mid).

## Filter / join stats
```json
{
  "candidates": 1208,
  "excluded_method_not_mid": 0,
  "excluded_near_deg": 94,
  "excluded_void_or_other": 0,
  "excluded_no_y": 0,
  "scored": 1114,
  "n_speak": 89,
  "n_agree": 1025,
  "n_fail_closed_missing_K": 0,
  "n_fail_closed_missing_S": 0,
  "n_fail_closed_K_not_knowable": 0,
  "join_open_eq_decision_minus_60s": 1114,
  "join_open_ne_decision_minus_60s": 0,
  "expiration_value_read": false,
  "incomplete_bar_used": false,
  "per_cell": {
    "KALSHI|15m|BTC|T-5m|mid": {
      "candidates": 604,
      "scored": 569,
      "speak": 51,
      "agree": 518,
      "fail_closed_K": 0,
      "fail_closed_S": 0,
      "excluded_method_not_mid": 0,
      "excluded_near_deg": 35,
      "excluded_void": 0
    },
    "KALSHI|15m|ETH|T-5m|mid": {
      "candidates": 604,
      "scored": 545,
      "speak": 38,
      "agree": 507,
      "fail_closed_K": 0,
      "fail_closed_S": 0,
      "excluded_method_not_mid": 0,
      "excluded_near_deg": 59,
      "excluded_void": 0
    }
  },
  "L3_is_oracle": false,
  "join_verdict": "CONDITIONAL",
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
- **L3 ≠ oracle** (Binance spot proxy only; not CF BRTI / Kalshi settlement)
- Join verdict: **CONDITIONAL**
- EXPIRATION_VALUE: **not read / not scored**
- incomplete-bar close: **not used**
- Φ(z) / sibling blend / CF / Poly: **not used**
- No λ/δ retune; no gate retune; no annex sneak; no pool
- join open==decision−60s: `1114`
- join open≠decision−60s: `0`

## Overall package verdict
**`REDUNDANT / FAIL-INSUFFICIENT`** — Neither headline improves both Brier and LogLoss vs mid (BTC=REDUNDANT / FAIL-INSUFFICIENT; ETH=REDUNDANT / FAIL-INSUFFICIENT). REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE; not Champion). USED_RESEARCH; holdout closed; no trading. L3 ≠ oracle; CONDITIONAL join.

FAIL-INSUFFICIENT ≠ NO_EDGE. This is **not** a Champion / strategy PASS. No trading authorization. Holdout closed. L3 ≠ oracle.

## Artifacts
- `/workspace/lab/harness/examiner/out/TEST-20260913-003-W2E-INCREMENTAL.json`
- `/workspace/lab/harness/examiner/out/TEST-20260913-003-W2E-INCREMENTAL.md`
- `/workspace/lab/archive/tests/TEST-20260913-003-W2E-INCREMENTAL.json`
- `/workspace/lab/archive/tests/TEST-20260913-003-W2E-INCREMENTAL.md`
- `/workspace/lab/archive/tests/TEST-20260913-003.json`
- `/workspace/lab/archive/tests/TEST-20260913-003.md`
- `/workspace/lab/archive/audit/2026-09-13-TEST-20260913-003-W2E-INCREMENTAL-examiner.md`
