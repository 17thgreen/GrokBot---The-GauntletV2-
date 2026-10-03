# GITHUB_HUNT — DATA-PROV-PM-007 (Logan MO required)

**DATA_ID:** DATA-PROV-PM-007  
**Hole:** Kalshi 15m BTC/ETH **rem=180 (T-3m) mid** checkpoints for PM-003 window `2026-09-04T20:00Z`–`2026-09-11T20:59Z`  
**Stamp:** 2026-09-13T21:02Z (box)  
**Trade / paid vendors:** FORBIDDEN — not used.

## Verdict of hunt: **no external dump required / no Sep rem=180 host found**

Official Kalshi candlesticks (already in DATA-PROV-PM-003 raw + live re-probe) **GETTABLE** rem=180 mid for full 1208. GitHub/HF third-party dumps do **not** cover this window as a usable rem=180 mid substrate. Hunt completed **before** any BLOCKED call (none needed).

---

## Searches performed

| Channel | Query / target | Result |
|---------|----------------|--------|
| GitHub REST `search/repositories` | `kalshi 15m BTC candlestick` | total_count **0** |
| GitHub REST `search/repositories` | `kalshi checkpoint OR kalshi orderbook dump` | total_count **0** |
| GitHub REST `search/repositories` | `KXBTC15M OR KXETH15M` | 13 repos — bots/dashboards/paper ledgers; **no Sep 4–11 checkpoint dump** |
| GitHub REST `search/repositories` | `kalshi KXBTC15M OR KXETH15M data OR dump OR candlestick` | noisy bot list; no windowed mid dump |
| GitHub code search | `KXBTC15M candlesticks extension:json` | **403** rate limit (unauthenticated) |
| Web search | Kalshi KXBTC15M/KXETH15M candlestick checkpoint dump Sep 2026 | No public GitHub archive for this week |
| HF `huthvincent/btc15-dataset` | `market_ticks/machine=server-h200` date partitions | dates **2026-07-04 → 2026-08-07** only; **0** paths in `2026-09-04`…`2026-09-11` |
| HF `bennett-tan/kalshi-btc-15m` | dataset card / tree | trade-oriented; lastModified **2026-05-29**; not PM-003 week rem=180 mids |
| `mdowis/Kalshi_orderbook_streamer` | default branch `claude/kalshi-orderbook-streaming-CNpHb`; `data/KXBTC15M/2026-09-04` HTML | README describes JSONL + **R2 offload**; tree path **404** for Sep 4; no `2026-09` string on repo landing |
| Paid vendors (Lychee, CryptoStruct, etc.) | noted in search hits | **not used** (FORBIDDEN) |

## Notable near-misses (out of window or wrong product)

| Source | Why not usable for this hole |
|--------|------------------------------|
| `huthvincent/btc15-dataset` | Real yes_bid/yes_ask ticks, but partitions end **2026-08-07** (misses Sep 4–11) |
| `bennett-tan/kalshi-btc-15m` | Sample tickers in May 2026; not rem=180 checkpoint product for PM-003 week |
| `mdowis/Kalshi_orderbook_streamer` | Live orderbook streamer; Sep data not on GitHub tree (R2); cannot replace official candles for sealed rem=180 |
| `gensx-x1/polymarket-btc-eth-updown-data` | **Polymarket**, not Kalshi; prior PM-006 hunt — wrong venue |
| PMXT R2 | Polymarket books — wrong venue |

## Conclusion

- **GitHub does not fill the rem=180 hole** for the PM-003 week.
- **Do not BLOCKED** on GitHub miss: official Kalshi `period_interval=1` candlesticks already contain `end_period_ts = close - 180` with valid bid/ask for all 1208 PM-003 contracts (proven by re-extract + live HTTP 200 probes).
- Primary provision path for PM-007 = **official Kalshi** via PM-003 raw re-derive + live evidence.

*End GITHUB_HUNT DATA-PROV-PM-007.*
