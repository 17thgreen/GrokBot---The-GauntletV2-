# DATA-PROV-CF-001 — entitled CF close-minute ticks
**Authority:** Logan M via Conductor · 2026-09-13  
**RETROACTIVE:** NO  
**Trade:** FORBIDDEN

## Why
F2 / FEAT-20260912-005 was DATA-BLOCKED. Production Kalshi CF passthrough is now ENTITLED (BRTI / ETHUSD_RTI live + history 200). This label is the official L2 close-minute tape for Map 2.

## Slice (frozen before fetch)
- Universe: DATA-PROV-PM-003 1208 Kalshi 15m BTC/ETH only (same USED_RESEARCH arena).
- Close window per contract: `[close_time_ms - 60000, close_time_ms)`.
- Also keep 1s immediately before `close_start` as `pre_close_last` only.
- Indices: BTC → BRTI; ETH → ETHUSD_RTI.
- Time span: hours covering 2026-09-04T20:00Z → 2026-09-11T20:59Z (PM-003 close minutes only). No earlier archive. No live forward stream this label.

## Construction
- Source: signed `GET /trade-api/v2/cfbenchmarks/history/values` (Kalshi CF passthrough). Production host.
- 1Hz official print = `max(timestamp_ms)` in that unix second (same as frozen `evaluate_close_window`).
- Missing locked second → row MISSING (do not shrink /60).
- **Not** Binance. **Not** trimmed mean. **Not** EXPIRATION_VALUE as a feature.

## Mid for incrementality
Knowable `m_t` during the close minute from PM-003 is the **T−1m mid** (last completed 1m yes candle; incomplete last-minute candle forbidden). T−0 mid is **BLOCKED** (near-deg / leakage).

## Examiner (after Clock)
See `EXAMINER_ORDER_TEST-20260913-001-F2.md`. RESEARCH only. No holdout. No trade.

## Secrets
Use Desktop `GauntletGrokBot/Gauntletkey.docx` in memory only. Do not write PEM/Key ID into lab data, git, or chat.
