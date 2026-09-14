# Kernel extract — Grok-in-X closing block (order books / L2 / GitHub)

**Stamp:** 2026-09-14 · Logan flagged I undersold this vs TV scripts
**Trade:** FORBIDDEN. Not Examiner. Not READY.

## What Grok named (measurement, not marketing)

1. **Order-book imbalance** `(bid_vol − ask_vol) / (bid + ask)` as a real-time signal on Polymarket CLOB (example threshold >0.30).  
   Incumbent: Kalshi same-t mid. Speak-gate or clip-into-mid. **Follow-vs-fade leftover.**
2. **Depth dynamics near expiry** — spread widen, one side empties, OFI stronger in last seconds/minutes. Needs **full L2**, not last/mid.
3. **Time remaining + live book + execution cost** as the honest fill filter (Mechanic/Treasurer, not p_t).
4. Paid/OSS archives that claim BTC/ETH 5m–15m books.

Refuse as Feature: XGBoost/AI direction soups, Kelly bots, YES+NO<$1 MM (inventory, not mid-beat), SMC+tech confluence.

## Inventory vs that list

| Source | What it is | Covers our hole? |
|--------|------------|------------------|
| DATA-PROV-PM-006 | Live Poly **top-of-book** ~1s, BTC/ETH 5m+15m | Forward only. Can compute **TOB imbalance** now. Not L2. Not Sep hist. |
| DATA-PROV-PM-008 | Live Kalshi yes bid/ask | Same-t mid for the live join. Running. |
| gensx-x1 dump | Poly TOB Aug 6–18 | **Not** Sep 4–11. Already filed. |
| DepthFeed | Full L2 Poly/Kalshi/Limitless, Jan 2026+, REST+WS | **Paid.** Public `/v3/overview` is a probability tape, not the ladder. Explorer $0 = 7d capped BTC. Quant $29 / Research $99 / Desk $249. Spend = Governor. |
| kalshibacktest.com | Kalshi 15m L2 ~100ms | Paid key. Same class as DepthFeed. |
| krish301/polymarket-raw-15m (HF) | Poly 15m trades + 5s book during window; full L2 at **resolution boundary**; start 2026-06-04 | **Inspect** as free hist. Coverage of Sep 4–11 UNTESTED until files listed. |

## Next physical
1. Inventory HF `krish301/polymarket-raw-15m` date range (do not Examiner).
2. Keep PM-006/008 running — TOB imbalance is scorable **forward** without spend once N≥80.
3. Full-L2 hist / DepthFeed = **Governor spend** after that inventory. Do not auto-buy.

Clock still owns any join. Examiner dark on imbalance until a Feature + door + lift.
