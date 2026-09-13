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
**T−0 mid incumbent:** NOT USED (near-deg). This is vs an *older* mid, not same-t.
**Run UTC:** `2026-09-13T17:53:52Z`

**Sign convention:** ΔBrier / ΔLogLoss = model − market; negative = skill.
**Skill rule:** both Δ < 0 on a cell.

## Overall reason
ETH headline lacks both-Δ skill. Mapping fail (hard 0/1 logloss), not NO_EDGE, not data-missing. USED_RESEARCH; holdout closed; no trading. No retune.

## Headline cells (k=30)

| Cell | N | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | Verdict |
|------|--:|------------:|-------------:|-------:|--------------:|---------------:|---------:|---------|
| `KALSHI|15m|BTC|CLOSE-k30|mid_T-1m` | 219 | 0.041096 | 0.149206 | -0.108110 | 0.378603 | 0.464352 | -0.085749 | `INCREMENTAL_RESEARCH` |
| `KALSHI|15m|ETH|CLOSE-k30|mid_T-1m` | 178 | 0.078652 | 0.126928 | -0.048276 | 0.724501 | 0.400601 | 0.323900 | `REDUNDANT / FAIL-INSUFFICIENT` |

Exclusions: BTC near_deg 329 last_fallback 56; ETH near_deg 368 last_fallback 58. Clock missing-sec 0/0.

## Annex (not headline; no post-hoc switch)

| Cell | N | ΔBrier | ΔLogLoss | Verdict |
|------|--:|-------:|---------:|---------|
| BTC CLOSE-k10 | 219 | -0.030484 | +0.629201 | REDUNDANT |
| ETH CLOSE-k10 | 178 | +0.002285 | +0.789586 | REDUNDANT |
| BTC CLOSE-k50 | 219 | -0.140074 | -0.380141 | INCREMENTAL_RESEARCH |
| ETH CLOSE-k50 | 178 | -0.126928 | -0.400501 | INCREMENTAL_RESEARCH |

Full machine packet: `TEST-20260913-001-F2-INCREMENTAL.json` in this folder.
