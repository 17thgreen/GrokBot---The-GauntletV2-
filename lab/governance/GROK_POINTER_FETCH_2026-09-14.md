# GROK pointer fetch — TV / GH peers for Conductor (2026-09-14)

**Audience:** The Conductor (BTC/ETH short-horizon binary lab)  
**Stamp:** 2026-09-14 (fetch pass)  
**Trade:** FORBIDDEN. Protocol / pointer only. Not Examiner. Not READY.  
**Rule:** Do **not** invent numbers. Only values named in source pages / READMEs / open Pine are listed.  
**PROHIBITED peers:** Any path that places orders or runs live trading bots — protocol flag only; do not clone, wire, or Examiner.

Dead-card overlap keys used below: **F1 digital**, **CB-VEL**, **SMC**, **squeeze**, **book imbalance**.

---

## 1. Polymarket Helper

| Field | Content |
|-------|---------|
| **URL** | https://www.tradingview.com/script/k9yK1osw-Polymarket-Helper/ |
| **Title** | Polymarket Helper |
| **Author** | RafaelZioni |
| **License surface** | Open-source (TradingView House Rules on republish) |
| **Claims to compute** | Directional 5m binary helper via **Intrabar Volume Delta (IVD)** + cross-checks → Strong / Moderate / CONFLICT; plus OBV Hidden Divergence |
| **Named algebra** | IVD from sub-minute ticks, **exponential decay** weighting (recent ticks heavier); cross-validate with **OBV momentum**, **Delta Volume**, **1m/3m timeframe convergence**; IVD vs **10-candle rolling average** baseline; OBV hidden bullish = red candle + rising OBV; hidden bearish = green + falling OBV |
| **Inputs / params named** | Signal fires at **25 seconds** into a new **5-minute** candle (countdown UI); strength from how many of 4 layers agree (4=Strong, 3=Moderate, fewer/contradict=CONFLICT). Exact decay λ / OBV lengths **not** named in the public description text fetched. |
| **Horizons** | Decision window on **5m** candle open; confirmation TF **1m / 3m** |
| **Data dependencies** | **Sub-minute / tick** volume for IVD (beyond completed 1m OHLCV); chart volume for OBV / Delta Volume |
| **Reconstructable on completed 1m / book / strike+τ?** | **Partial.** OBV + delta-volume + 1m/3m convergence ≈ yes on completed 1m (+ resample). Full IVD **no** without tick / intrabar tape. **Not** strike+τ. **Not** book L2. |
| **Dead-card overlap guess** | **book imbalance** (cousin: signed flow / IVD) · **CB-VEL** (momentum / TF agreement) · not F1 digital · not SMC · not squeeze |
| **PROHIBITED?** | No (indicator / alert surface). Usage text pushes “enter Up/Down on Polymarket” — that is user action, not an order bot. |

---

## 2. Kalshi 15m BTC Intel

| Field | Content |
|-------|---------|
| **URL** | https://www.tradingview.com/script/dt0pHc5W-Kalshi-15m-BTC-Intel/ |
| **Title** | Kalshi 15m BTC Intel |
| **Author** | jalilstephens18 |
| **License surface** | Open-source |
| **Claims to compute** | Regime classifier over rolling **15m**: **UPTREND / DOWNTREND / RANGING / STABLE** via **7-indicator confluence vote**; confidence = majority agreement count **x/7** |
| **Named algebra** | Votes +1 / −1 / 0 from: (1) **EMA cross** EMA **27/63** on 1m closes (noted ≡ **9/21** on 3m) + deadband; (2) **RSI(14)** on **3m** resample — bullish **>55**, bearish **<45**; (3) **Volume surge** — last 15m vol vs **4-hour** baseline of 15m blocks; surge **≥1.5×** votes with concurrent price move; (4) **Window delta** — % move over trailing 15m + deadband; (5) **Micro momentum** — EMA-smoothed 1m returns; (6) **Acceleration** — momentum now vs **5 bars** ago; (7) **Tick trend** — net direction of last **5** one-minute closes. Classifier also uses trend strength (15m move + EMA alignment), momentum-family label, **realized vol** = population stdev of 1m returns. Internal buffer: rolling **300** 1m bars (**5h**). |
| **Inputs** | All thresholds (RSI levels, deadbands, surge ratio, confidence bands) exposed; defaults = “values the original bot ran with” (page does not list every numeric default beyond those above). Symbol designed for **COINBASE:BTCUSD**. |
| **Horizons** | **15-minute** event-contract horizon; computes on **1m** request.security buffer; chart TF-independent |
| **Data dependencies** | Completed **1m** OHLCV (volume for surge); no Polymarket/Kalshi book required for the classifier itself |
| **Reconstructable on completed 1m / book / strike+τ?** | **Yes on completed 1m** (all seven votes + vol). **No** book. **No** strike+τ (regime lean, not digital fair value). |
| **Dead-card overlap guess** | **CB-VEL** (strong: EMA sep, 1m returns, acceleration) · light F1-adjacent only as “15m lean” narrative · not SMC · not squeeze · not book imbalance |
| **PROHIBITED?** | No as published indicator. Text says “originally built as an alerting bot” for KXBTC15M — **alerts ≠ CLOB orders**. Still protocol-only; do not wire execution. |

---

## 3. Polymarket 15m BTC Probability [10x]

| Field | Content |
|-------|---------|
| **URL** | https://www.tradingview.com/script/bKp6f7yZ-Polymarket-15m-BTC-Probability-10x/ |
| **Title** | Polymarket 15m BTC Probability [10x] |
| **Author** | esshka |
| **License surface** | **Closed-source / protected** |
| **Claims to compute** | Real-time **fair-value probability** for 15m BTC binaries via “**Micro-Temporal Density Collapse**” / **Brownian Bridge** framing; output used to spot mispricing vs venue cents |
| **Named algebra** | Outcome ≈ f(**Standardized Distance to Strike**, **Time to Expiry**, **Volatility**). **Normal CDF** via **Abramowitz & Stegun** approximation to **erf**. Volatility from **ATR / StDev** lookback. Exact standardization formula / bridge residual **not** published (protected). |
| **Inputs named** | **Volatility Lookback** default **15**; chart **1 minute**; symbol **COINBASE:BTCUSD** (or index matching the market); Ghost Overlay / HUD toggles |
| **Horizons** | **15-minute** binary / τ-to-expiry inside the candle |
| **Data dependencies** | Spot path + **strike** + **τ** + vol estimate; venue book **not** required for the stated fair-value engine (comparison to market price is manual) |
| **Reconstructable on completed 1m / book / strike+τ?** | **Conceptually yes on strike+τ + completed-1m vol** (classic digital / barrier CDF). Exact TV implementation **not** reconstructable from open code (protected). Book not required for the named claim. |
| **Dead-card overlap guess** | **F1 digital** (strong) · not CB-VEL · not SMC · not squeeze · not book imbalance |
| **PROHIBITED?** | No (indicator). Closed-source → pointer / peer only; do not scrape or reverse for Examiner. |

---

## 4. Polymarket Smart Money 5m (Madrimov)

| Field | Content |
|-------|---------|
| **URL** | https://www.tradingview.com/script/CCndHaaT-Polymarket-Smart-Money-5m-Madrimov/ |
| **Title** | Polymarket Smart Money 5m (Madrimov) |
| **Author** | Madrimov_trade |
| **License surface** | Open-source |
| **Claims to compute** | **SMC** market-structure signals (CHOCH / BOS) with volume filter and **5m entry window**; UP/DOWN arrows + confidence % labels |
| **Named algebra** | Swing High / Swing Low → **CHOCH** (change of character) = major shift; **BOS** (break of structure) = continuation (**BOS requires volume confirmation**). Volume engine: current vol vs **highest volume in lookback**; needs **volume spike** (multiplied threshold) + min price displacement **0.15%**. Entry only in first **X** minutes of each 5m block — default **first 2 minutes**; **one signal per 5m block**. Confidence labels claimed: CHOCH only **~65%**; BOS+volume **~60%**; CHOCH+volume spike **~72%** (author-stated labels, not lab-measured). |
| **Inputs** | Entry-window minutes (default 2); volume multiplier / lookback (named as concepts; exact default ints beyond 0.15% / 2m not fully listed in fetched blurb) |
| **Horizons** | **5-minute** charts / Polymarket short-term; “5M timeframe only” |
| **Data dependencies** | OHLC structure + volume; webhooks mentioned for automation |
| **Reconstructable on completed 1m / book / strike+τ?** | Structure rules **partially** on completed bars, but CHOCH/BOS geometry is **unfrozen** (same family as LuxAlgo SMC). Volume gate on completed 5m/1m ≈ yes. **No** book. **No** strike+τ. |
| **Dead-card overlap guess** | **SMC** (strong — refuse as Feature until frozen geometry) · not F1 digital · not CB-VEL primary · not squeeze · not book imbalance |
| **PROHIBITED?** | Indicator + webhook-ready — **not** itself a CLOB bot. Webhook→order glue would become PROHIBITED; do not build that path. |

---

## 5. messified / tradingview-crypto-indicator

| Field | Content |
|-------|---------|
| **URL** | https://github.com/messified/tradingview-crypto-indicator |
| **Title** | Refined Multi-TF Crypto Analyzer (`crypto-analyzer.pine`) |
| **Author** | Messified (repo: messified) |
| **License surface** | Pine under MPL 2.0 header in file; README marks script as **hypothetical Pine v6** / illustrative |
| **Claims to compute** | Multi-TF buy/sell/hold: critical vs regular signals from EMA trend + RSI extremes + ADX strength + volume spike + RSI divergence + HTF confirmation; ATR-based stop/target |
| **Named algebra (from open Pine)** | `fastEMA`/`slowEMA` = `ta.ema(close, fastLength/slowLength)`; `rsi = ta.rsi(close, rsiLength)`; `atr = ta.atr(atrLength)`; ADX length **14** (DI/DX/RMA); `volumeSpike = volume > sma(volume,20) * volumeMultiplier`; support/resistance = lowest/highest over `supportResistanceLen`; bullish/bearish divergence = adjacent-bar price LL/HH with RSI HL/LH; `bullishTrend = fastEMA > slowEMA and adx > adxThreshold` (+ HTF twin via `request.security`); `criticalBuy = bullishTrend & htf & rsi < rsiOversold & volumeSpike & bullishDivergence` (sell symmetric); `regularBuy/Sell` weaker RSI/ADX gates; `stopLoss = close - atr`, `targetPrice = close + atr * riskRewardMultiplier` |
| **Inputs (defaults in Pine)** | fastLength **9**, slowLength **26**, rsiLength **14**, rsiOverbought **75**, rsiOversold **25**, atrLength **14**, adxThreshold **20**, volumeMultiplier **2.0**, supportResistanceLen **50**, riskRewardMultiplier **1.0** (README prose also cites 2.5 as “typical” — **Pine default is 1.0**), htf **"30"** |
| **Horizons** | Example use: chart **15m** + HTF **30m** (configurable) |
| **Data dependencies** | OHLCV on chart TF + HTF security; no PM/Kalshi API |
| **Reconstructable on completed 1m / book / strike+τ?** | **Yes on completed bars** (classic TA stack). **No** book. **No** strike+τ. Note: hypothetical v6 may not run as-is on current TV. |
| **Dead-card overlap guess** | **CB-VEL** (EMA/ADX/momentum family) · RSI extreme / divergence cousins to regime gates · not F1 digital · not SMC · **not squeeze** (no BB/KC) · not book imbalance |
| **PROHIBITED?** | No (indicator source). |

---

## 6. aulekator / Polymarket-BTC-15-Minute-Trading-Bot — **PROHIBITED-path peer**

| Field | Content |
|-------|---------|
| **URL** | https://github.com/aulekator/Polymarket-BTC-15-Minute-Trading-Bot |
| **Title** | Polymarket BTC 15-Minute Trading Bot |
| **Author** | aulekator (contact surfaces named in README: @Kator07 / Telegram) |
| **Status for lab** | **PROHIBITED-path peer (protocol only).** Live / sim **order placement** on Polymarket CLOB. Do **not** clone, configure keys, run `--live`, or Examiner. |
| **Claims to compute / do** | Production-style **7-phase** bot: ingest → NautilusTrader core → signal processors (**Spike Detection**, **Sentiment Analysis**, **Price Divergence**) → **Fusion Engine** (weighted voting) → **Risk** → **Execution (Polymarket orders)** → monitoring → learning weight optimization |
| **Named algebra / thresholds (README only)** | Risk caps named: **MAX_POSITION_SIZE=1.0**, **STOP_LOSS_PCT=0.30**, **TAKE_PROFIT_PCT=0.20**, **SPIKE_THRESHOLD=0.15**, **DIVERGENCE_THRESHOLD=0.05**. Exact spike/divergence formulas not fully specified in README prose. Self-learning = optimize signal weights from performance (placeholder learning_engine noted in tree). |
| **Inputs / deps** | Polymarket API credentials (PK, API key/secret, passphrase); Redis; Coinbase + Binance + news/social (Fear & Greed) + optional Solana; Grafana/Prometheus |
| **Horizons** | Polymarket **15-minute** BTC prediction markets; `--test-mode` trades every minute (test harness) |
| **Data dependencies** | Multi-venue spot WS/REST + Polymarket CLOB + optional sentiment; **not** reconstructable as a pure completed-1m Feature without the execution stack |
| **Reconstructable on completed 1m / book / strike+τ?** | Signal pieces (spike / divergence) **might** be re-derived later as **non-executing** measurements — **out of scope this pass**. Full bot path **forbidden**. Book/CLOB is for **orders**, not lab fair-value join. |
| **Dead-card overlap guess** | CB-VEL / flow cousins possible in spike+divergence narrative; **not** treated as Feature candidates while execution-coupled. Not SMC. Not squeeze. Not F1 digital CDF. |
| **PROHIBITED?** | **YES — order-placement / live trading bot.** Protocol peer flag only. |

---

## Summary table

| # | Title | Author | Horizon | Core claim | Reconstruct? | Dead-card guess | PROHIBITED? |
|---|-------|--------|---------|------------|--------------|-----------------|-------------|
| 1 | Polymarket Helper | RafaelZioni | 5m @ 25s | IVD + OBV/ΔV/TF vote | Partial (needs ticks for IVD) | book imb. · CB-VEL | No |
| 2 | Kalshi 15m BTC Intel | jalilstephens18 | 15m (1m buf) | 7-vote regime 4-state | Yes on completed 1m | **CB-VEL** | No (alert heritage) |
| 3 | Polymarket 15m BTC Probability [10x] | esshka | 15m τ | Normal-CDF digital FV | Concept yes (strike+τ+vol); code closed | **F1 digital** | No |
| 4 | Polymarket Smart Money 5m | Madrimov_trade | 5m | SMC CHOCH/BOS + vol window | Partial; geometry unfrozen | **SMC** | No (webhook risk) |
| 5 | Refined Multi-TF Crypto Analyzer | Messified | e.g. 15m+30m HTF | EMA/RSI/ADX/vol/div | Yes on completed bars | **CB-VEL** | No |
| 6 | Polymarket BTC 15m Trading Bot | aulekator | 15m PM | Multi-signal **+ CLOB exec** | N/A — do not | — | **YES** |

## Conductor notes (non-invented)

- Strongest **F1-digital** peer by named math: **#3** (CDF / strike / τ / vol) — but **protected**, so peer pointer only.
- Strongest **completed-1m reconstructable** regime stack with explicit constants: **#2**.
- **#1** needs **tick/intrabar** for the named IVD core → NEEDS_DATA relative to completed-1m lock unless IVD is dropped.
- **#4** lands on dead **SMC** refuse family (same as LuxAlgo SMC on dry-run chart).
- **#5** is generic multi-TF TA; overlaps CB-VEL; **no squeeze** object.
- **#6** is the only hard **PROHIBITED-path** peer in this list (orders / live mode / API keys).

**Trade remains FORBIDDEN.** No Feature promotion from this fetch alone.
