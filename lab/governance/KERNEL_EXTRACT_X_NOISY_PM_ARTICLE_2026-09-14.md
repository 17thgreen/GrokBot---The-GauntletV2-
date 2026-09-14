# Kernel extract — X article @noisyb0y1 + Grok-in-X pointers

**Article:** https://x.com/noisyb0y1/status/2031661714987454664
**Stamp:** 2026-09-14T01:43Z · Conductor
**Trade:** FORBIDDEN. Not READY. Not Examiner.

## Article method (full)
- Horizons: **1 / 7 / 30 day** directional classification on **daily** bars
- Markets: BTC, S&P, ETH, “major prediction-market series” (claimed 30) — not Kalshi 15m mid cells
- Train 2000–2020 / test 2021–2025 (stated)
- Features named: Yesterday OHLC/Vol log returns, MA10/20/30, Dow/Dom/Month, EMA10/30, RSI, MACD(+signal), Bollinger U/L, Vol10/20/30, OBV, Z-score, insider_*, sentiment, num_articles, overnight_gap, abnormal_vol, vol_5d/20d, mom_5d/20d, skew_5d (first lines cropped — do not invent)
- Arch: Conv1D → LSTM → MC Dropout 0.2 → sigmoid; 50 dropout passes → mean + std; BUY if p≥0.70 else HOLD; top-3 daily
- No intraday, no 1m/1s, no book, no contract-level Kalshi/Poly mechanics. “Full code on GitHub” with **no URL shown**
- 79%/59% claims = marketing

## Article verdict
**Refuse as Feature.** Horizon wrong. Multi-indicator soup. Not Δ vs Kalshi mid. Keep only the *analogy* (binary event vs price) as already lab-native.

## Grok-in-X pointers — sift

| Object / link | Verdict | Nearest dead / note |
|---------------|---------|---------------------|
| Polymarket 15m BTC Probability (Brownian/Φ, dist-to-strike, τ, ATR) `tradingview.com/script/bKp6f7yZ-Polymarket-15m-BTC-Probability-10x/` | **Refuse as p_t** | = unconditional F1 / FEAT-002 digital. Wick-gate already died (F4). |
| Polymarket Smart Money 5m (SMC, CHOCH, BOS) `.../CCndHaaT-Polymarket-Smart-Money-5m-Madrimov/` | **Refuse** | Unfrozen geometry |
| Kalshi 15m BTC Intel (EMA27/63, RSI14 on 3m, vol surge, micro-mom) `.../dt0pHc5W-Kalshi-15m-BTC-Intel/` | **Inspect** | EMA/RSI/vol = CB-VEL cousins if used as direction; vol-surge / micro-mom may be a *gate* only |
| Polymarket Helper (EW intrabar vol delta, first ~25s, OBV) `.../k9yK1osw-Polymarket-Helper/` | **Inspect** | Volume-delta speak-gate; needs sub-minute tape = NEEDS_DATA |
| Squeeze Momentum (named by Grok) | **Keep** | Same family as TV squeeze leftover vs dead F4 expansion |
| OB imbalance `(bid−ask)/(bid+ask)`, OFI, L2 near expiry | **Keep / follow-vs-fade** | PM-006/008 path; hist Poly book still BLOCKED |
| Funding / L-S ratio / OI | Parked Layer-3 | Not this leftover |
| VWAP / Hull / Supertrend / UT Bot / Heikin | Catalog only | Mostly CB-VEL / regime cousins |
| `github.com/messified/tradingview-crypto-indicator` | Inspect | |
| `github.com/aulekator/Polymarket-BTC-15-Minute-Trading-Bot` | Inspect as **method peer / protocol**, not p_t (order bots often PROHIBITED path) | |
| depthfeed.com BNB 15m | Out of scope (BNB) | |

## Next physical
1. Fetch TV script pages + GitHub READMEs for Helper / Kalshi-Intel / messified / aulekator (extract algebra only).
2. Do **not** Examiner any of the above.
3. Follow-vs-fade + squeeze remain oldest leftovers; PM-006/008 keep running.
