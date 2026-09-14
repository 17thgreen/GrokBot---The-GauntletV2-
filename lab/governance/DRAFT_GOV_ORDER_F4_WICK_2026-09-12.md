# DRAFT — Governor order F4 (wick-gated structural)
**STATUS:** DRAFT / NOT COMMISSIONED  
**Author:** Conductor, 2026-09-12 — Logan asked how this would be filed  
**Does not authorize Examiner, data fetch, or researcher fan-out.**

## Why a new family
Wave 001 F1 (FEAT-001/002) already tested *unconditional* structural P(YES) vs Kalshi mid on the six cells and lost (`TEST-20260912-002` REDUNDANT / FAIL-INSUFFICIENT). This filing is **not** an F1 retune, not a λ/σ grid, not an annex rescue of BTC T-10m.

**F4 claim (one sentence):** mid-window *spot* wicks make \(m_t\) overshoot structural P(YES); a frozen structural blend beats mid *only on wick rows*, and equals mid otherwise.

That is a **selection gate**, not a new digital.

## Contamination stamp [V]
PM-003 is USED_RESEARCH. TEST-002 annex has been seen (including BTC T-10m FEAT-002 ΔBrier −0.0005). Scoring F4 on PM-003 cannot be validation or promotion evidence. Preferred measure: contracts with OPEN **after** PM-003 end (`2026-09-11T20:15Z`). Until that DATA-* exists, Examiner stays unrouted.

If Governor insists on a PM-003 RESEARCH peek: stamp RESEARCH only; same freeze; no threshold change after N_wick is known.

## Frozen cut (lock before any wick histogram)
See `archive/features/DRAFT-FEAT-20260912-006.md`. No preview of wick counts, no κ search, no “only when m=0.25” definition.

## Forbidden
- Wick defined from cheap binaries (`m_t < 0.25`) or from `|m − p_struct| > 0.15` (that is the conclusion, not the wick)
- 15-minute TWAP settlement language (false). Algebraic lock (that is F2 / FEAT-005)
- BUY/NO 15¢ action rule, EV, trading, cockpit
- Fit of θ, W, λ on any seen slice
- Pool BTC+ETH or checkpoints
- Holdout open; PM-002 union
- Statistician / Tape / Examiner until this draft is commissioned

## If commissioned
1. Archivist assigns FEATURE_ID (draft stamp 006), pretest QUERY vs cemetery / F1
2. Clock: confirm L3 five-bar lookback under existing completed-bar join (no new DATA if scoring old windows)
3. New DATA-* for post-2026-09-11 windows before Examiner (preferred)
4. Conductor routes one incremental TEST vs `MKT-KALSHI-15M-MID`
5. Kill = both Δ ≥ 0 on either headline, or N_wick < 80, or ETH/BTC sign split
