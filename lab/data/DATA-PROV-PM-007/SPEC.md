# SPEC — DATA-PROV-PM-007

**DATA_ID:** DATA-PROV-PM-007  
**Wave / slot:** WAVE_008 / W2-D  
**Declared:** BEFORE peek (see `/workspace/lab/governance/WAVE_008_ORTHOGONAL_SLOT_2026-09-13.md`)  
**Class:** NEEDS_DATA provision — **Not a Feature. Not Examiner. Not T-1 rescue. Trade FORBIDDEN.**  
**Stamp:** 2026-09-13T21:01:44Z

## Goal

Fetch / derive Kalshi 15m BTC/ETH **mid** checkpoints at **rem=180 (T-3m)** for the PM-003 window, paired to the same `(asset, OPEN_TIME, CLOSE_TIME)` universe.

## Window

- **UTC:** `2026-09-04T20:00Z` – `2026-09-11T20:59Z`
- **Universe:** DATA-PROV-PM-003 remaining Kalshi 15m (604 BTC + 604 ETH = 1208)
- **Pair key:** `(asset, OPEN_TIME, CLOSE_TIME)` via `VENUE_NATIVE_ID` / PM-003 `remaining_universe.ndjson`

## Cell

| Field | Value |
|-------|-------|
| Venue | Kalshi |
| Series | `KXBTC15M` / `KXETH15M` |
| Window length | 15m |
| Decision | rem=180 (T-3m) = `CLOSE_TIME - 180s` |
| Price | **mid only** = `(yes_bid + yes_ask) / 2` when `bid>0`, `ask>0`, `bid<=ask` |
| Forbidden | invented mid; last-as-mid; `p_t`; READY; Examiner; trades |

## Source (ordered)

1. **Primary:** Official Kalshi 1-minute candlesticks already fetched under DATA-PROV-PM-003 (`raw/kalshi_candles/{ticker}.json`, batch `GET /markets/candlesticks` / series candlesticks, `period_interval=1`). Re-extract candle whose `end_period_ts == close_u - 180`.
2. **Live HTTP evidence:** Public `GET /series/{series}/markets/{ticker}/candlesticks` probes confirming rem=180 candle + bid/ask still served.
3. **GitHub hunt (required):** Search for third-party Kalshi 15m checkpoint dumps covering this window — documented in `GITHUB_HUNT.md`. No substitute dump found; does not block (official candles GETTABLE).

## Non-goals

- No new rem=840/600/300/60 shop
- No Poly / PM-005 / PM-006
- No Clock join, Cartographer, Feature, Examiner, or trading
- No keys / no Trade API

## Success criteria

- Real row counts vs PM-003 **604 BTC + 604 ETH**
- Verdict **GETTABLE / PARTIAL / BLOCKED** with HTTP evidence
- Artifacts: `SPEC.md`, `INVENTORY.md`, `GITHUB_HUNT.md`, `FETCH_SUMMARY` (+ derived checkpoints)

*End SPEC DATA-PROV-PM-007.*
