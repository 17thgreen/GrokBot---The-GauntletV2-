# TEST-20260913-001 — F2-INCREMENTAL vs T−1m mid

**TEST_ID:** `TEST-20260913-001`
**Package:** `F2-INCREMENTAL`
**Feature:** `FEAT-20260912-005` Map 2 (`FEAT-20260912-005/evaluate_close_window/2026-09-12-patch2`)
**Incumbent:** PM-003 T−1m mid (`implied_p_method==mid`)
**DATA:** DATA-PROV-CF-001 (CLEARED) + PM-003 T−1m + PM-001 FLOOR_STRIKE / RESOLUTION
**Slice use:** USED_RESEARCH — not validation, not sealed holdout
**Overall verdict:** `REDUNDANT / FAIL-INSUFFICIENT`
**invented_numbers:** `False`
**Trading:** FORBIDDEN
**EXPIRATION_VALUE as feature:** NOT USED
**Binance-as-oracle:** NOT USED
**T−0 mid incumbent:** NOT USED
**Run UTC:** `2026-09-13T17:53:52Z`

## Authority
- `governance/EXAMINER_ORDER_TEST-20260913-001-F2.md`
- `governance/CF_001_COVERAGE_FROZEN_2026-09-13.md`
- `governance/DATA_PROV_CF_001_SPEC.md`
- `data/DATA-PROV-CF-001/provenance/DATA_VERDICT_DATA-PROV-CF-001.md`
- `harness/f2/evaluate_close_window.py` (no retune)

## Filters / join
- venue=KALSHI, window=15m; BTC/ETH **separate** (no pool)
- DATA-PROV-PM-003 1208-slice only
- now_ms = close_start_ms + k*1000; **k from Clock** (not len(ticks))
- Headline k=30; Annex k=10, k=50
- m_t = T−1m checkpoint mid only; last-fallback excluded; near-deg (≤0.02 or ≥0.98) excluded
- VOID/DISPUTED out; MISSING remainder out of scored N
- K = PM-001 `FLOOR_STRIKE` (never EXPIRATION_VALUE)
- Map 2: `p_remainder` = 1 iff projected_sum ≥ K*60 else 0

**Sign convention:** ΔBrier = Brier_model − Brier_market; ΔLogLoss = LogLoss_model − LogLoss_market; **negative = skill**.

**Skill rule:** both Δ < 0 on a cell. Kill if either Δ ≥ 0, N_scored < 80, one asset flips, or Clock MISSING rate > 20% on a headline.

## Overall reason
ETH headline lacks both-Δ skill REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE). USED_RESEARCH; holdout closed; no trading.

## Headline cells (k=30)

| Cell | N | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | mean(m) | mean(p) | ECE | Verdict |
|------|--:|------------:|-------------:|-------:|--------------:|---------------:|---------:|--------:|--------:|-----|---------|
| `KALSHI|15m|BTC|CLOSE-k30|mid_T-1m` | 219 | 0.041096 | 0.149206 | -0.108110 | 0.378603 | 0.464352 | -0.085749 | 0.4463 | 0.4703 | 0.041096 | `INCREMENTAL_RESEARCH` |
| `KALSHI|15m|ETH|CLOSE-k30|mid_T-1m` | 178 | 0.078652 | 0.126928 | -0.048276 | 0.724501 | 0.400601 | 0.323900 | 0.5240 | 0.5281 | 0.078652 | `REDUNDANT / FAIL-INSUFFICIENT` |

### Exclusions (headline)
- BTC: {"near_deg": 329, "last_fallback": 56}
- ETH: {"last_fallback": 58, "near_deg": 368}

### Missing stats
- Close-minute missing-sec rate (Clock): BTC=0.000000, ETH=0.000000
- MISSING remainder (Map 2) excluded from N as above

## Annex (k=10, k=50; not headline)

| Cell | N | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | mean(m) | mean(p) | ECE | Verdict |
|------|--:|------------:|-------------:|-------:|--------------:|---------------:|---------:|--------:|--------:|-----|---------|
| `KALSHI|15m|BTC|CLOSE-k10|mid_T-1m` | 219 | 0.118721 | 0.149206 | -0.030484 | 1.093553 | 0.464352 | 0.629201 | 0.4463 | 0.4384 | 0.118721 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|CLOSE-k10|mid_T-1m` | 178 | 0.129213 | 0.126928 | 0.002285 | 1.190187 | 0.400601 | 0.789586 | 0.5240 | 0.5112 | 0.129213 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|CLOSE-k50|mid_T-1m` | 219 | 0.009132 | 0.149206 | -0.140074 | 0.084212 | 0.464352 | -0.380141 | 0.4463 | 0.4658 | 0.009132 | `INCREMENTAL_RESEARCH` |
| `KALSHI|15m|ETH|CLOSE-k50|mid_T-1m` | 178 | 0.000000 | 0.126928 | -0.126928 | 0.000100 | 0.400601 | -0.400501 | 0.5240 | 0.5393 | 0.000000 | `INCREMENTAL_RESEARCH` |

### Annex exclusions
- KALSHI|15m|BTC|CLOSE-k10|mid_T-1m: {"near_deg": 329, "last_fallback": 56}
- KALSHI|15m|ETH|CLOSE-k10|mid_T-1m: {"last_fallback": 58, "near_deg": 368}
- KALSHI|15m|BTC|CLOSE-k50|mid_T-1m: {"near_deg": 329, "last_fallback": 56}
- KALSHI|15m|ETH|CLOSE-k50|mid_T-1m: {"last_fallback": 58, "near_deg": 368}

## Placebos (pre-registered)
- Sign-flip p_remainder and T−0 mid rescue **not** used as primary; λ-blend forbidden this test.
- No retune of Map 2.

## Artifacts
- `/workspace/lab/harness/examiner/out/TEST-20260913-001-F2-INCREMENTAL.md`
- `/workspace/lab/harness/examiner/out/TEST-20260913-001-F2-INCREMENTAL.json`
