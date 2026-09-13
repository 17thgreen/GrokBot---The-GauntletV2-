# EXAMINER ORDER — TEST-20260913-001 F2-INCREMENTAL
**Package:** F2-INCREMENTAL · FEAT-20260912-005 Map 2  
**Incumbent:** T−1m Kalshi mid from PM-003 (`implied_p_method==mid`)  
**DATA:** DATA-PROV-CF-001 (after Clock) + PM-003 T−1m + PM-001 FLOOR_STRIKE / RESOLUTION  
**Slice:** USED_RESEARCH — RESEARCH only  
**Trading:** FORBIDDEN

## Map (frozen)
`harness/f2/evaluate_close_window.py` Map 2. No retune.

## Headline
BTC and ETH CLOSE-k=30 vs T−1m mid. Separate. No pool.

Skill = both ΔBrier < 0 and ΔLogLoss < 0 vs mid on that cell (model − market).  
Kill if either Δ ≥ 0, if N_scored < 80, if one asset flips, if Clock MISSING rate > 20% on a headline.

## Placebos
Sign-flip p_remainder; use T−0 mid as incumbent (must not be the rescue); λ-style blend forbidden this test.

## Forbidden
EXPIRATION_VALUE feature · incomplete second · k from len(ticks) · Examiner before Clock
