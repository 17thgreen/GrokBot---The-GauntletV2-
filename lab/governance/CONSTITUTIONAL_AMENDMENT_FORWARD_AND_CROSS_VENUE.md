# Constitutional Amendment — Forward Holdout & Cross-Venue
Locked by Logan 2026-09-10. Conductor cannot waive.

## Epistemic hierarchy of tests (increasing credibility)

1. **Unseen-by-code historical data** — chronological research / validation / historical sealed holdout on a registered series (code never trained on holdout; researchers must not inspect holdout before seal).
2. **Independent-venue data** — same frozen spec on ≥1 other sufficiently liquid venue with equivalent data.
3. **Genuinely future data** — **FUTURE SEALED FORWARD WINDOW**: market data that **did not exist** when the strategy specification was frozen.

Historical sealed holdout is a useful gate. It is **not** pristine final proof. Models (and humans) may possess broad prior knowledge of regimes (COVID, 2021 bull, FTX, ETF periods, etc.). Blindness to a file ≠ epistemic virginity about history.

**No strategy earns production-capital status solely from historical holdout success.**

## Updated promotion hierarchy

```
HYPOTHESIS
  → RESEARCH TEST
  → VALIDATION
  → HISTORICAL SEALED HOLDOUT
  → CROSS-VENUE REPLICATION   (mandatory before capital)
  → FUTURE SEALED FORWARD WINDOW / FORWARD SHADOW
  → PAPER
  → MICRO CAPITAL
  → LIMITED CAPITAL
  → PRODUCTION
```

(Prior shorthand SEALED HOLDOUT = historical sealed holdout on the research sample.)

## Cross-venue replication (mandatory before capital)

- Provisional reference venue (e.g. Binance USD-M for DATA-PROV-001) is **not** a venue marriage.
- Surviving validation must later be tested on **at least one independent, sufficiently liquid venue** with equivalent data.
- If the edge disappears outside the original venue → classify **venue-specific**; decide executability there — do **not** call it universal alpha.

## Future sealed forward window

Once a strategy spec is **frozen**:
1. Record freeze timestamp UTC.
2. Begin collecting new market data with `t > freeze`.
3. That untouched forward period is the strongest pre-capital test.
4. Canary / shadow monitors this window; Treasurer blocks capital if forward evidence fails.

## EDGE-001 note

OHLCV tests the **narrow statistical claim** only. Order-flow mechanism remains **[H]** until Tape has appropriate microstructure data.
