# DATA-PROV-TRADES-001 — Specification
Provisional reference trades family. Distinct from DATA-PROV-001 (OHLCV).

## Intent
Stage-1 microstructure input for incremental predictive-value tests. Not a venue marriage. Not full L2.

## Scope
- Venue family: Binance USD-M Futures (same provisional reference as DATA-PROV-001)
- Instruments: BTCUSDT, ETHUSDT perpetual
- Stream: aggTrades (preferred) or trades with aggressor/maker if available
- Target calendar: 2021-01-01 → 2026-08-31 UTC if practical; document any shortfall

## Required fields (raw)
- exchange event timestamp
- price
- quantity
- aggressor side / is_buyer_maker (Binance aggTrade convention)
- trade / agg trade ID
- sequence continuity notes

## Hard rules
- Preserve raw immutably; hash; full provenance
- No silent gap/duplicate repair
- No merge into OHLCV dataset
- Derive features only in derived/; never rewrite EDGE-005/006 to match available columns
- Seal policy for research/validation/holdout to be defined after Clock sees coverage (may align calendar to OHLCV SEAL_LOCK dates where timestamps allow)

## Clock audit checklist
event-time semantics · trade ordering · duplicate/missing IDs · aggressor-side interpretation · aggregation artifacts · exchange clock · alignment to 5m bars · knowability before entry
