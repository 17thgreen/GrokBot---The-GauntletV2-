# Coverage freeze — DATA-PROV-CF-001
**Frozen before fetch.** No post-result boundary change.

## Universe
PM-003 1208 only. Close minute `[close-60s, close)`. 1Hz last-in-second. BRTI for BTC, ETHUSD_RTI for ETH.

## Headline cells (F2)
`KALSHI|15m|BTC|CLOSE-k30|mid_T-1m`  
`KALSHI|15m|ETH|CLOSE-k30|mid_T-1m`

## Annex
k=10 and k=50, same mid rule. Not T−14/T−10/T−5 (those are not close-minute). Not T−0 mid.

## BLOCKED
Binance-as-oracle · EXPIRATION_VALUE as p · holdout open · PM-002 union · BTC+ETH pool · trading
