# Coverage freeze — DATA-PROV-PM-002
**Authority:** Conductor, binding Clock CONDITIONAL 2026-09-11T21:27:41Z  
**RETROACTIVE:** NO  
**Frozen before Examiner run.** No post-result boundary change.

## Slice
240-contract PM-002 stride only. Do **not** reuse full PM-001 label windows for this \(m_t\) path.

## PRIMARY cells (market-relative Examiner — first package)

| Cell | Method | Rules |
|------|--------|-------|
| `KALSHI\|15m\|BTC\|T-14m\|mid` | mid | exclude implied_p ≤0.02 or ≥0.98; exclude last-fallback |
| `KALSHI\|15m\|ETH\|T-14m\|mid` | mid | same |
| `KALSHI\|15m\|BTC\|T-10m\|mid` | mid | same |
| `KALSHI\|15m\|ETH\|T-10m\|mid` | mid | same |
| `KALSHI\|15m\|BTC\|T-5m\|mid` | mid | same |
| `KALSHI\|15m\|ETH\|T-5m\|mid` | mid | same |

Six cells. Report **separately**. No unlabeled pool. Not books. Not oracle.

## ANNEX (optional, after primary; not a substitute)

- Kalshi T−1m mid: `CLEARED_WITH_STRONG_CAVEAT` — same exclude rules.
- Poly last-print, non-T−0, asset×horizon×checkpoint separate: `CLEARED_WEAKER_LAST_PRINT` — never score as mid.

## BLOCKED (do not score)

Kalshi T−0 any; Kalshi last-fallback as mid; Poly T−0; Poly mid; books; independent oracle; full 3824; sealed holdout; unlabeled Kalshi+Poly pool; pre-cutoff `/historical`; exact OPEN rem=900/300; PM-001 `LAST_PRICE_DOLLARS` / `OUTCOME_PRICES` as \(m_t\).

## First TEST
**MARKET BASELINE** of \(m_t\) vs official resolution. No Gauntlet model. No strategy search.
