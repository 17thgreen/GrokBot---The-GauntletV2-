# RESEARCH PRIORITIES — Cycle 4 (Tape / staged microstructure)
Opened 2026-09-11 by Logan + Conductor.

## Goal (explicit)
**Not** “make EDGE-005/006 pass.”
**Yes:** Determine whether transaction-level information contains **incremental** 5/10/15-minute predictive value that OHLCV bars do not.
If trades add nothing → cheaply kill the family before paying for historical L2.
If they add something → acquire **minimum** L2 needed for real market-mechanics claims.

## Acquisition order
1. **DATA-PROV-TRADES-001** — raw aggTrades / trades (BTC+ETH perps, provisional Binance USD-M reference, same venue family as DATA-PROV-001)
2. Measurability audit vs frozen EDGE-005/006 (no silent proxy)
3. Escalate to L2 only for components that require book state

## Measurability [I from card text — Clock confirms]
| EDGE | Full claim needs | Trade-only status |
|------|------------------|-------------------|
| EDGE-20260910-005 | L2 top-N depth + aggressor trades (replenishment, depth trough) | **UNMEASURABLE WITHOUT L2** for frozen thesis — do not invent depth from trades |
| EDGE-20260910-006 | Best bid/ask sizes, spread_z, one-side empty, repair | **UNMEASURABLE WITHOUT L2** for frozen thesis — do not proxy spread from trade gaps |

Frozen cards stay frozen. No rewriting because a convenient trade feature exists.

## Research tracks
### A. Incremental trade-flow (OHLCV-orthogonal)
New atomic Edge Cards (Tape Reader) using **only** trade-derived features knowable before entry:
signed volume, imbalance, aggressor ratio, trade-count imbalance, volume acceleration, large-trade clustering, short-horizon flow persistence.
**Control (mandatory):** feature must add information beyond OHLCV variables already tested (001/003/004 cemetery). If it recreates recent return/volume → reject REDUNDANT.

### B. Frozen 005/006
Remain DATA-BLOCKED until L2 DATA-* registered. Clock marks components UNMEASURABLE WITHOUT L2.

## Execution discipline
- Distinct DATA-* family — **not** merged into DATA-PROV-001
- Immutable raw + hashes + provenance
- Clock: event-time, ordering, IDs, aggressor semantics, aggregation artifacts, exchange clock, bar alignment, knowability
- Examiner: measure after **realistic execution delay** — not at the same instant as the last trade used in the signal
- Economics: keep provisional cost stack discipline; microstructure edges are cost-sensitive
- Catalyst (liq/OI/funding) = **Cycle 5** unless Tape fails fast or acquisition path is worse

## Attention lock
PRIMARY: staged Tape acquisition + incremental trade-flow cards
DATA-BLOCKED: 005/006 (need L2), 009/010 (Cycle 5)
DARK: 002
CEMETERY: 001 NO_EDGE, 003 COST_KILLED, 004 NO_EDGE
