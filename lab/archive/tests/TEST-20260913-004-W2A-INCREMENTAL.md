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

| Cell | λ | c | w | N | ΔBrier | ΔLogLoss | Verdict |
|------|--:|--:|--:|--:|-------:|---------:|---------|
| `KALSHI|15m|BTC|T-14m|mid` | 0.1 | 0.05 | 0.003 | 604 | 0.000069 | 0.000212 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.1 | 0.05 | 0.005 | 604 | 0.000243 | 0.000587 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.1 | 0.05 | 0.008 | 604 | 0.000251 | 0.000519 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.1 | 0.1 | 0.003 | 604 | 0.000159 | 0.000472 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.1 | 0.1 | 0.005 | 604 | 0.000360 | 0.000914 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.1 | 0.1 | 0.008 | 604 | 0.000419 | 0.000901 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.1 | 0.15 | 0.003 | 604 | 0.000182 | 0.000537 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.1 | 0.15 | 0.005 | 604 | 0.000407 | 0.001040 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.1 | 0.15 | 0.008 | 604 | 0.000487 | 0.001074 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.2 | 0.05 | 0.003 | 604 | 0.000162 | 0.000480 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.2 | 0.05 | 0.005 | 604 | 0.000517 | 0.001243 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.2 | 0.05 | 0.008 | 604 | 0.000536 | 0.001109 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.2 | 0.1 | 0.003 | 604 | 0.000362 | 0.001060 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.2 | 0.1 | 0.005 | 604 | 0.000792 | 0.001999 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.2 | 0.1 | 0.008 | 604 | 0.000925 | 0.001988 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.2 | 0.15 | 0.003 | 604 | 0.000416 | 0.001214 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.2 | 0.15 | 0.005 | 604 | 0.000902 | 0.002293 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.2 | 0.15 | 0.008 | 604 | 0.001090 | 0.002401 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.3 | 0.05 | 0.003 | 604 | 0.000279 | 0.000805 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.3 | 0.05 | 0.005 | 604 | 0.000822 | 0.001967 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.3 | 0.05 | 0.008 | 604 | 0.000855 | 0.001772 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.3 | 0.1 | 0.003 | 604 | 0.000609 | 0.001766 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.3 | 0.1 | 0.005 | 604 | 0.001295 | 0.003256 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.3 | 0.1 | 0.008 | 604 | 0.001519 | 0.003258 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.3 | 0.15 | 0.003 | 604 | 0.000701 | 0.002036 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.3 | 0.15 | 0.005 | 604 | 0.001483 | 0.003761 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-14m|mid` | 0.3 | 0.15 | 0.008 | 604 | 0.001811 | 0.003978 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.1 | 0.05 | 0.003 | 604 | 0.000137 | 0.000331 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.1 | 0.05 | 0.005 | 604 | 0.000288 | 0.000654 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.1 | 0.05 | 0.008 | 604 | 0.000384 | 0.000784 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.1 | 0.1 | 0.003 | 604 | 0.000113 | 0.000333 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.1 | 0.1 | 0.005 | 604 | 0.000347 | 0.000857 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.1 | 0.1 | 0.008 | 604 | 0.000436 | 0.000933 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.1 | 0.15 | 0.003 | 604 | 0.000114 | 0.000360 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.1 | 0.15 | 0.005 | 604 | 0.000368 | 0.000945 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.1 | 0.15 | 0.008 | 604 | 0.000472 | 0.001043 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.2 | 0.05 | 0.003 | 604 | 0.000296 | 0.000709 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.2 | 0.05 | 0.005 | 604 | 0.000606 | 0.001375 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.2 | 0.05 | 0.008 | 604 | 0.000802 | 0.001642 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.2 | 0.1 | 0.003 | 604 | 0.000262 | 0.000763 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.2 | 0.1 | 0.005 | 604 | 0.000759 | 0.001870 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.2 | 0.1 | 0.008 | 604 | 0.000956 | 0.002050 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.2 | 0.15 | 0.003 | 604 | 0.000271 | 0.000842 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.2 | 0.15 | 0.005 | 604 | 0.000813 | 0.002087 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.2 | 0.15 | 0.008 | 604 | 0.001056 | 0.002344 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.3 | 0.05 | 0.003 | 604 | 0.000475 | 0.001136 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.3 | 0.05 | 0.005 | 604 | 0.000953 | 0.002160 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.3 | 0.05 | 0.008 | 604 | 0.001254 | 0.002571 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.3 | 0.1 | 0.003 | 604 | 0.000448 | 0.001292 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.3 | 0.1 | 0.005 | 604 | 0.001234 | 0.003041 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.3 | 0.1 | 0.008 | 604 | 0.001558 | 0.003347 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.3 | 0.15 | 0.003 | 604 | 0.000471 | 0.001453 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.3 | 0.15 | 0.005 | 604 | 0.001336 | 0.003431 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 0.3 | 0.15 | 0.008 | 604 | 0.001752 | 0.003897 | `REDUNDANT / FAIL-INSUFFICIENT` |

## Placebos (report, not headline switch)

| Placebo | Cell | N | ΔBrier | ΔLogLoss | Notes |
|---------|------|--:|-------:|---------:|-------|
| `lambda_0` | `KALSHI|15m|BTC|T-14m|mid` | 604 | 0.000000 | 0.000000 | λ=0 identity check pass=True |
| `lambda_0` | `KALSHI|15m|ETH|T-14m|mid` | 604 | 0.000000 | 0.000000 | λ=0 identity check pass=True |
| `flip_sign_d` | `KALSHI|15m|BTC|T-14m|mid` | 604 | 0.001304 | 0.002550 | sign(d) flipped; should not beat true sign |
| `flip_sign_d` | `KALSHI|15m|ETH|T-14m|mid` | 604 | 0.001613 | 0.003170 | sign(d) flipped; should not beat true sign |
| `shuffle_cf` | `KALSHI|15m|BTC|T-14m|mid` | 604 | -0.000890 | -0.002183 | cf_t shuffled within cell; K,m fixed |
| `shuffle_cf` | `KALSHI|15m|ETH|T-14m|mid` | 604 | -0.001366 | -0.002946 | cf_t shuffled within cell; K,m fixed |

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
  "n_fail_closed_missing_K": 0,
  "n_fail_closed_missing_cf": 0,
  "n_fail_closed_K_not_knowable": 0,
  "n_fail_closed_locked": 0,
  "n_on_second": 1208,
  "close_minute_extractor_used": false,
  "join_A_used_as_headline": false,
  "policy": "B",
  "join_verdict": "CONDITIONAL",
  "per_cell": {
    "KALSHI|15m|BTC|T-14m|mid": {
      "candidates": 604,
      "scored": 604,
      "speak": 604,
      "abstain": 0,
      "fail_closed_K": 0,
      "fail_closed_cf": 0,
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
      "fail_closed_K": 0,
      "fail_closed_cf": 0,
      "fail_closed_locked": 0,
      "excluded_method_not_mid": 0,
      "excluded_near_deg": 0,
      "excluded_void": 0
    }
  },
  "cf_hours_loaded": {
    "BTC": [
      "2026-09-04T20",
      "2026-09-04T21",
      "2026-09-04T22",
      "2026-09-04T23",
      "2026-09-05T00",
      "2026-09-05T01",
      "2026-09-05T02",
      "2026-09-05T03",
      "2026-09-05T04",
      "2026-09-05T05",
      "2026-09-05T06",
      "2026-09-05T07",
      "2026-09-05T08",
      "2026-09-05T09",
      "2026-09-05T10",
      "2026-09-05T11",
      "2026-09-05T12",
      "2026-09-05T13",
      "2026-09-05T14",
      "2026-09-05T15",
      "2026-09-05T16",
      "2026-09-05T17",
      "2026-09-05T18",
      "2026-09-05T19",
      "2026-09-05T20",
      "2026-09-05T21",
      "2026-09-05T22",
      "2026-09-05T23",
      "2026-09-06T00",
      "2026-09-06T01",
      "2026-09-06T02",
      "2026-09-06T03",
      "2026-09-06T04",
      "2026-09-06T05",
      "2026-09-06T06",
      "2026-09-06T07",
      "2026-09-06T08",
      "2026-09-06T09",
      "2026-09-06T10",
      "2026-09-06T11",
      "2026-09-06T12",
      "2026-09-06T13",
      "2026-09-06T14",
      "2026-09-06T15",
      "2026-09-06T16",
      "2026-09-06T17",
      "2026-09-06T18",
      "2026-09-06T19",
      "2026-09-06T20",
      "2026-09-06T21",
      "2026-09-06T22",
      "2026-09-06T23",
      "2026-09-07T00",
      "2026-09-07T01",
      "2026-09-07T02",
      "2026-09-07T03",
      "2026-09-07T04",
      "2026-09-07T05",
      "2026-09-07T06",
      "2026-09-07T07",
      "2026-09-07T08",
      "2026-09-07T09",
      "2026-09-07T10",
      "2026-09-07T11",
      "2026-09-07T12",
      "2026-09-07T13",
      "2026-09-07T14",
      "2026-09-07T15",
      "2026-09-07T16",
      "2026-09-07T17",
      "2026-09-07T18",
      "2026-09-07T19",
      "2026-09-07T20",
      "2026-09-07T21",
      "2026-09-07T22",
      "2026-09-07T23",
      "2026-09-08T00",
      "2026-09-08T01",
      "2026-09-08T02",
      "2026-09-08T03",
      "2026-09-08T04",
      "2026-09-08T05",
      "2026-09-08T06",
      "2026-09-08T07",
      "2026-09-08T08",
      "2026-09-08T09",
      "2026-09-08T10",
      "2026-09-08T11",
      "2026-09-08T12",
      "2026-09-08T13",
      "2026-09-08T14",
      "2026-09-08T15",
      "2026-09-08T16",
      "2026-09-08T17",
      "2026-09-08T18",
      "2026-09-08T19",
      "2026-09-08T20",
      "2026-09-08T21",
      "2026-09-08T22",
      "2026-09-08T23",
      "2026-09-09T00",
      "2026-09-09T01",
      "2026-09-09T02",
      "2026-09-09T03",
      "2026-09-09T04",
      "2026-09-09T05",
      "2026-09-09T06",
      "2026-09-09T07",
      "2026-09-09T08",
      "2026-09-09T09",
      "2026-09-09T10",
      "2026-09-09T11",
      "2026-09-09T12",
      "2026-09-09T13",
      "2026-09-09T14",
      "2026-09-09T15",
      "2026-09-09T16",
      "2026-09-09T17",
      "2026-09-09T18",
      "2026-09-09T19",
      "2026-09-09T20",
      "2026-09-09T21",
      "2026-09-09T22",
      "2026-09-09T23",
      "2026-09-10T00",
      "2026-09-10T01",
      "2026-09-10T02",
      "2026-09-10T03",
      "2026-09-10T04",
      "2026-09-10T05",
      "2026-09-10T06",
      "2026-09-10T09",
      "2026-09-10T10",
      "2026-09-10T11",
      "2026-09-10T12",
      "2026-09-10T13",
      "2026-09-10T14",
      "2026-09-10T15",
      "2026-09-10T16",
      "2026-09-10T17",
      "2026-09-10T18",
      "2026-09-10T19",
      "2026-09-10T20",
      "2026-09-10T21",
      "2026-09-10T22",
      "2026-09-10T23",
      "2026-09-11T00",
      "2026-09-11T01",
      "2026-09-11T02",
      "2026-09-11T03",
      "2026-09-11T04",
      "2026-09-11T05",
      "2026-09-11T06",
      "2026-09-11T07",
      "2026-09-11T08",
      "2026-09-11T09",
      "2026-09-11T10",
      "2026-09-11T11",
      "2026-09-11T12",
      "2026-09-11T13",
      "2026-09-11T14",
      "2026-09-11T15",
      "2026-09-11T16",
      "2026-09-11T17",
      "2026-09-11T18",
      "2026-09-11T19",
      "2026-09-11T20"
    ],
    "ETH": [
      "2026-09-04T20",
      "2026-09-04T21",
      "2026-09-04T22",
      "2026-09-04T23",
      "2026-09-05T00",
      "2026-09-05T01",
      "2026-09-05T02",
      "2026-09-05T03",
      "2026-09-05T04",
      "2026-09-05T05",
      "2026-09-05T06",
      "2026-09-05T07",
      "2026-09-05T08",
      "2026-09-05T09",
      "2026-09-05T10",
      "2026-09-05T11",
      "2026-09-05T12",
      "2026-09-05T13",
      "2026-09-05T14",
      "2026-09-05T15",
      "2026-09-05T16",
      "2026-09-05T17",
      "2026-09-05T18",
      "2026-09-05T19",
      "2026-09-05T20",
      "2026-09-05T21",
      "2026-09-05T22",
      "2026-09-05T23",
      "2026-09-06T00",
      "2026-09-06T01",
      "2026-09-06T02",
      "2026-09-06T03",
      "2026-09-06T04",
      "2026-09-06T05",
      "2026-09-06T06",
      "2026-09-06T07",
      "2026-09-06T08",
      "2026-09-06T09",
      "2026-09-06T10",
      "2026-09-06T11",
      "2026-09-06T12",
      "2026-09-06T13",
      "2026-09-06T14",
      "2026-09-06T15",
      "2026-09-06T16",
      "2026-09-06T17",
      "2026-09-06T18",
      "2026-09-06T19",
      "2026-09-06T20",
      "2026-09-06T21",
      "2026-09-06T22",
      "2026-09-06T23",
      "2026-09-07T00",
      "2026-09-07T01",
      "2026-09-07T02",
      "2026-09-07T03",
      "2026-09-07T04",
      "2026-09-07T05",
      "2026-09-07T06",
      "2026-09-07T07",
      "2026-09-07T08",
      "2026-09-07T09",
      "2026-09-07T10",
      "2026-09-07T11",
      "2026-09-07T12",
      "2026-09-07T13",
      "2026-09-07T14",
      "2026-09-07T15",
      "2026-09-07T16",
      "2026-09-07T17",
      "2026-09-07T18",
      "2026-09-07T19",
      "2026-09-07T20",
      "2026-09-07T21",
      "2026-09-07T22",
      "2026-09-07T23",
      "2026-09-08T00",
      "2026-09-08T01",
      "2026-09-08T02",
      "2026-09-08T03",
      "2026-09-08T04",
      "2026-09-08T05",
      "2026-09-08T06",
      "2026-09-08T07",
      "2026-09-08T08",
      "2026-09-08T09",
      "2026-09-08T10",
      "2026-09-08T11",
      "2026-09-08T12",
      "2026-09-08T13",
      "2026-09-08T14",
      "2026-09-08T15",
      "2026-09-08T16",
      "2026-09-08T17",
      "2026-09-08T18",
      "2026-09-08T19",
      "2026-09-08T20",
      "2026-09-08T21",
      "2026-09-08T22",
      "2026-09-08T23",
      "2026-09-09T00",
      "2026-09-09T01",
      "2026-09-09T02",
      "2026-09-09T03",
      "2026-09-09T04",
      "2026-09-09T05",
      "2026-09-09T06",
      "2026-09-09T07",
      "2026-09-09T08",
      "2026-09-09T09",
      "2026-09-09T10",
      "2026-09-09T11",
      "2026-09-09T12",
      "2026-09-09T13",
      "2026-09-09T14",
      "2026-09-09T15",
      "2026-09-09T16",
      "2026-09-09T17",
      "2026-09-09T18",
      "2026-09-09T19",
      "2026-09-09T20",
      "2026-09-09T21",
      "2026-09-09T22",
      "2026-09-09T23",
      "2026-09-10T00",
      "2026-09-10T01",
      "2026-09-10T02",
      "2026-09-10T03",
      "2026-09-10T04",
      "2026-09-10T05",
      "2026-09-10T06",
      "2026-09-10T09",
      "2026-09-10T10",
      "2026-09-10T11",
      "2026-09-10T12",
      "2026-09-10T13",
      "2026-09-10T14",
      "2026-09-10T15",
      "2026-09-10T16",
      "2026-09-10T17",
      "2026-09-10T18",
      "2026-09-10T19",
      "2026-09-10T20",
      "2026-09-10T21",
      "2026-09-10T22",
      "2026-09-10T23",
      "2026-09-11T00",
      "2026-09-11T01",
      "2026-09-11T02",
      "2026-09-11T03",
      "2026-09-11T04",
      "2026-09-11T05",
      "2026-09-11T06",
      "2026-09-11T07",
      "2026-09-11T08",
      "2026-09-11T09",
      "2026-09-11T10",
      "2026-09-11T11",
      "2026-09-11T12",
      "2026-09-11T13",
      "2026-09-11T14",
      "2026-09-11T15",
      "2026-09-11T16",
      "2026-09-11T17",
      "2026-09-11T18",
      "2026-09-11T19",
      "2026-09-11T20"
    ]
  },
  "cf_hours_missing": {
    "BTC": [],
    "ETH": []
  },
  "L3_used": false,
  "poly_used": false,
  "map2_used": false,
  "binance_used": false,
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
- Join policy: **B** (completed-second s−1)
- K revision: **[A]** (static dump; no revision feed)
- close-minute CLEARED extractor: **not used** (≠ this join)
- Join A as headline: **not used**
- Map 2 / Φ(z) / sibling blend / W2-E / L3 / Poly / Binance: **not used**
- EXPIRATION_VALUE: **not read / not scored**
- No λ/w/c retune; no gate retune; no annex sneak; no pool

## Overall package verdict
**`REDUNDANT / FAIL-INSUFFICIENT`** — Neither headline improves both Brier and LogLoss vs mid (BTC=REDUNDANT / FAIL-INSUFFICIENT; ETH=REDUNDANT / FAIL-INSUFFICIENT). REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE; not Champion). USED_RESEARCH; holdout closed; no trading. Join CONDITIONAL; Policy B (completed-second s−1); K revision [A]; close-minute CLEARED ≠ this join.

FAIL-INSUFFICIENT ≠ NO_EDGE. This is **not** a Champion / strategy PASS. No trading authorization. Holdout closed. Join CONDITIONAL; Policy B.

## Artifacts
- `/workspace/lab/harness/examiner/out/TEST-20260913-004-W2A-INCREMENTAL.json`
- `/workspace/lab/harness/examiner/out/TEST-20260913-004-W2A-INCREMENTAL.md`
- `/workspace/lab/archive/tests/TEST-20260913-004-W2A-INCREMENTAL.json`
- `/workspace/lab/archive/tests/TEST-20260913-004-W2A-INCREMENTAL.md`
- `/workspace/lab/archive/tests/TEST-20260913-004.json`
- `/workspace/lab/archive/tests/TEST-20260913-004.md`
- `/workspace/lab/archive/audit/2026-09-13-TEST-20260913-004-W2A-INCREMENTAL-examiner.md`
