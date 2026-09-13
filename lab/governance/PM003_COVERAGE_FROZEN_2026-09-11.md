# Coverage freeze — DATA-PROV-PM-003
**Authority:** Conductor, binding Clock CONDITIONAL 2026-09-11T23:03:13Z  
**RETROACTIVE:** NO  
**Frozen before Examiner run.** No post-result boundary change.

## Slice
THIS 1208 only (604 BTC + 604 ETH Kalshi 15m). Opens ~2026-09-04T20:45Z → 2026-09-11T20:15Z.

**Do not** union with PM-002 240 as holdout. PM-002 remains USED_RESEARCH. **Do not** reuse full PM-001 windows.

## PRIMARY cells (TEST-20260911-007 market baseline)

| Cell | Method | Rules |
|------|--------|-------|
| `KALSHI\|15m\|BTC\|T-14m\|mid` | mid | exclude implied_p ≤0.02 or ≥0.98; exclude last-fallback |
| `KALSHI\|15m\|ETH\|T-14m\|mid` | mid | same |
| `KALSHI\|15m\|BTC\|T-10m\|mid` | mid | same |
| `KALSHI\|15m\|ETH\|T-10m\|mid` | mid | same |
| `KALSHI\|15m\|BTC\|T-5m\|mid` | mid | same (Clock: 94/1208 near-deg at T−5m overall) |
| `KALSHI\|15m\|ETH\|T-5m\|mid` | mid | same |

Six cells. Report separately. No Poly. No PM-002 rows.

## ANNEX optional
Kalshi T−1m mid: CLEARED_WITH_STRONG_CAVEAT — exclude last-fallback (114) and near-deg.

## BLOCKED
T−0 any; last-fallback as mid; books; oracle; sealed holdout; PM-002∪PM-003 as holdout; Poly; rem=900; PM-001 terminals as \(m_t\); pre-cutoff historical.
