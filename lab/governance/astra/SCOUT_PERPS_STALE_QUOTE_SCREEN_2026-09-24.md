# SCOUT — Perps Stale-Quote Feasibility Screen (Research Card 04)

- **Seat:** Market Scout (Astra/Kalshi desk), executor for The Conductor
- **Written:** 2026-09-24 ~20:00 ET
- **Mode:** READ-ONLY. Public GETs, public docs, and unauthenticated public WS only. No orders, no accounts, no keys, no paid feeds, no VPN, proxy, or alternate-region hosts. Kept separate from the binary BTC work (KXBTC15M etc.).
- **Scope:** Kalshi perps KXBTCPERP and KXETHPERP against Coinbase Exchange BTC-USD and ETH-USD.
- **Raw proof:** `packets/scout_perps_screen_2026-09-24/` (`docs/`, `feeds/` + `feeds/FEED_AUDIT.md`, `raw/`, `script/`, `MANIFEST.sha256`)

## Verdict: **REJECT** (for this account, as it stands)
Two parts of the card 04 rule are met.
1. **Fees consume the spread.** Over ~20 min of synchronized sampling (1,290 Kalshi book snapshots: 1,138 baseline + 152 arrival-delay rechecks), the largest gross cross between Kalshi and Coinbase was **1.78 bps**. No snapshot went above 2 bps. The retail Kalshi taker fee alone is **12 bps** of notional, before any hedge fee.
2. **Profitable execution needs membership economics this account can't get.** The fee holiday is a 100% monthly rebate for **Self-Clearing Members only**. Retail trades through Kalshi Prime (an FCM, i.e. a futures broker). SCM status requires a Guaranty Fund capital contribution and "significant financial and operational thresholds."
There is also a speed issue. The Kalshi perps WS needs authentication (401 without it), and public REST gives about 320 ms RTT with snapshots only every ~2 s. That setup can't win cancel races (S12 fn.5: "no speed bumps").
The crosses we did see (≤1.8 bps) mostly **persist**. They look like a structural perp-vs-Coinbase basis (Kalshi marks to CF BRTI, a multi-venue index, and perps carry a funding premium), not stale quotes that vanish on arrival.

## Q1 — Fees and access for a non-member retail account (official text, fetched 2026-09-24 ET)
| Item | Finding | Source (fetch time ET) |
|---|---|---|
| Retail fee schedule | Kalshi Prime tab: "applies to most users trading Perpetuals through the Kalshi.com website and app. Launch Fee Schedule". **Tier 0 (<$100k 30D): Taker 0.120%, Maker 0.020%.** T1 ≥$100k 0.100/0.015; T2 ≥$1M 0.060/0.012; T3 ≥$10M 0.020/0.000; T4 ≥$100M 0.015/0; T5 ≥$1B 0.010/0. "*30D Trailing Perps + Prediction Notional Volume (maker + taker)" | https://kalshi.com/fee-schedule?product=perps (19:33, via browser; curl/WebFetch got a Vercel 429 checkpoint) → `docs/fee_schedule_perps_browser.txt`, PNGs |
| SCM schedule (for comparison) | Taker 12.0 bps at T0 down to 2.6 bps at T10 (≥$3B); maker 5.0 down to 0.6 bps. Currently 100% rebated to SCMs | same page, self-clearing tab (19:34) |
| Fee basis | "Trading fees on perpetual futures are charged as a percentage of your position's notional value … not the margin you posted." "A round trip involves two fees" | S13 https://help.kalshi.com/en/articles/16071417-perps-fees-explained (19:31:45) |
| Funding | "Every 8 hours, Kalshi computes a time-weighted average price (TWAP) of 1-minute candlestick premiums over the 480 candles"; paid 12:00 AM / 8:00 AM / 4:00 PM ET; cap "+2% / –2% per 8-hour interval"; <0.01% set to zero; "Funding payments are transfers between traders, not fees" | https://help.kalshi.com/en/articles/15357613-how-funding-works (19:31:59) |
| Margin/leverage | "up to 6x"; "Isolated margin is the only mode currently available in the Kalshi app"; portfolio margin "via API" (BTC spec); settlement cycles 12:00 PM and 4:00 PM ET; BTC contract 0.0001 BTC, index CF BRTI (1 s updates) | what-are-perps (19:32:00), how-margin-works (19:32:02), BTC spec (19:32:42) |
| Fee holiday eligibility | CFTC filing (June 24, 2026): "Eligible Participants are all Self-Clearing Members of Kalshi." Monthly rebate of "all net taker and maker fees", in effect until the earlier of Dec 31, 2026 or termination; no net-negative fees. S12: "In order to become a Self-Clearing Member for margined products, one must contribute capital to the Guaranty Fund". Help center: SCM "requires meeting significant financial and operational thresholds". **→ Does NOT apply to a retail/Kalshi Prime account (confirms the card's expectation).** | https://www.cftc.gov/filings/orgrules/rules0625267305.pdf (19:32:07); S12 https://news.kalshi.com/p/the-facts-behind-kalshi-s-perpetuals-volume (19:31:46); https://help.kalshi.com/en/articles/15357656-applying-for-perpetuals-access (19:32:41) |
| +0.3/−0.3 bp program | S12 fn.4: "This program is not live" | S12 |
| Liquidity obligations | Only for LP incentive program participants ("$W a month if you have bid and ask orders of size $X … no more than Y% apart … Z% of the time"). No obligation found for ordinary retail takers | S12 |
| Eligibility | "US-based Kalshi users who have completed KYC verification are eligible to apply." Perps are "not automatically available"; you must apply for a margin account (questionnaire, review, mandatory tutorial). "Most retail users … trade perpetuals currently through Kalshi Prime, a registered Futures Commission Merchant." **No official per-state perps restriction list was found.** Verify in the app | applying-for-access (19:32:41) |
| API for retail | The perps REST/WS/FIX API exists under `/margin`. Production is marked "(rolling out member by member)". The fee-tier API enum includes `kalshi_prime`, and `/margin/enabled` exists to check per-account enablement. **Whether Logan's account has API perps access is UNVERIFIED** and needs an account check | https://docs.kalshi.com/margin.md (19:32:23), get-fee-tier-rates.md (19:32:24) |
| Market data access | `GET /margin/markets` and `/margin/markets/{t}/orderbook` are **public** (`security: []`, 200 without auth). The margin WS returns **401 without auth** | live GETs from 19:32 ET; `feeds/ws_reach_test.txt` |
| Maintenance | "Thursdays from approximately 3:00 AM to 5:00 AM ET" | margin-account article |

## Q2 — External executable feeds (tested from this box, 2026-09-24 19:33–19:42 ET)
All files were audited in `feeds/FEED_AUDIT.md`: HTTP code, JSON validity, error/restriction bodies, non-empty two-sided book, bid < ask. **Bybit is BLOCKED (geo).** `bybit_book.json` (sha 7ef856c94570) is a CloudFront geoblock error body, not a book, so there is zero Bybit depth. It is kept as evidence only.
| Venue / endpoint | Reachable (HTTP) | Audit | Timestamps in payload | Rate limit (source) |
|---|---|---|---|---|
| Coinbase Exchange REST `api.exchange.coinbase.com/products/{BTC,ETH}-USD/book?level=2` | Y (200, re-verified 19:41) | VALID | book `time` (exchange, ns) + `sequence` | public 10 rps/IP, burst 15 (docs.cdp.coinbase.com rest rate-limits, 19:36) |
| Coinbase Exchange WS `ws-feed.exchange.coinbase.com` `level2_batch` (→level2_50) and `ticker` | Y | VALID (**used for all counts**) | l2update `time` (exchange); receipt stamped locally. Exchange→receipt ≈ 6 ms on ticker test; median book age at Kalshi receipt 28–35 ms | WS 8 rps/IP, burst 20 connects; inbound 10 RPS (docs, 19:36) |
| Coinbase Advanced REST/WS | Y (200) | VALID | WS `timestamp` | not verified |
| Kraken REST Depth / WS v2 ticker (bbo) | Y (200, re-verified) | VALID | per-level epoch-s (REST); WS `timestamp`, `time_in/out` | not verified in this screen |
| Binance.US REST depth BTCUSD / BTCUSDT | Y (200, re-verified) | VALID | `lastUpdateId` only (no timestamp) | not verified |
| Gemini REST book | Y (200, re-verified) | VALID | per-level epoch-s | not verified |
| Bitstamp REST order_book | Y (200, re-verified) | VALID | `timestamp`, `microtimestamp` | not verified |
| OKX global REST | readable (200) | READABLE, NOT USABLE | – | excluded: OKX global doesn't serve US persons for trading |
| Binance.com | **N (451)** | BLOCKED | restricted-location JSON | excluded |
| Bybit | **N (403)** | BLOCKED (geo) | CloudFront error body | excluded, zero depth |
| CME | **N (no HTTP response)**; paid data anyway | BLOCKED | – | excluded |
Hedge-venue fees: **Kraken Tier 1 spot taker 0.80%, maker 0.40%** (public page, browser ~19:38). The Coinbase retail fee table requires sign-in ("sign in to your Coinbase.com account"), so it is **not verified and not assumed**.
Earlier note (repo's "external spot-data access failed"): **not reproduced** from this box for Coinbase, Kraken, Binance.US, Gemini, or Bitstamp.

## Q3 — Stale-quote counts (feed: **Coinbase Exchange WS level2_batch only**)
**Method:** script `script/perps_stale_sampler.py`, analysis `script/analyze_sample.py`.
- Kalshi public REST orderbook (depth=10), polled alternately for BTC and ETH, so each market is seen every ~2.0 s. RTT median 322 ms, p90 ~360 ms.
- The Kalshi body has **no timestamp**; the Date header has 1 s resolution. Each snapshot falls somewhere in [send, receive].
- Local Coinbase book maintained from the public WS.
- Definitions: raw sell-side = Kalshi best bid > Coinbase best ask; raw buy-side = Kalshi best ask < Coinbase best bid. "Adj" subtracts the causal rolling median Kalshi−Coinbase mid basis (last 60 samples).
- Main run: 19:36:01–19:51:00 ET, 899 Kalshi GETs, 0×429. Phase 2: 19:51:56–19:56:59 ET, 391 GETs, 0×429. Phase 2 fired event-triggered re-GETs at +250/500/1000/2000 ms whenever edge > 0.5 bp (≤1 sequence per 10 s per market).
**Main run (450 BTC / 449 ETH snapshots):**
| | KXBTCPERP | KXETHPERP |
|---|---|---|
| Kalshi spread (median) | 0.24 bps | 0.37 bps |
| Kalshi−Coinbase mid basis, median [min, max] | +0.77 [−0.21, +1.95] bps | −0.02 [−1.25, +1.13] bps |
| Snapshots with raw cross > 0 / > 1 / > 2 bps | 433 / 98 / **0** | 120 / 0 / **0** |
| … > 12 bps (Kalshi retail taker) / > 14 / > 24 / > 92 (12 + Kraken T1 taker) | **0 / 0 / 0 / 0** | **0 / 0 / 0 / 0** |
| Basis-adjusted > 0 / > 1 / > 2 bps | 260 / 15 / **0** | 105 / 0 / **0** |
| Max raw / adj edge (main; phase 2: BTC 1.66/1.22, ETH 1.04/1.03) | 1.78 / 1.34 bps | 0.93 / 0.72 bps |
| Kalshi depth at crossing levels (median, max) | 0.163 BTC (~$13.8k), 0.175 BTC | 2.02 ETH (~$5.4k), 4.10 ETH |
| Coinbase hedge slippage to fill that size (median, max) | 0.02, 1.01 bps | 0.19, 1.05 bps |
| Raw cross still at same-or-better price on next poll (~2 s) | 308/432 | 80/120 |
**Arrival-delay rechecks (phase 2; approx. effective server-side delay 0.41 / 0.75 / 1.16 / 2.16 s):**
- BTC: 26 sequences. Quote still present 22/22/24/23. Edge still > 0: 26/26/26/26. Edge still > 2 bps: **0**. Edge still > 12 bps: **0**.
- ETH: 12 sequences. Quote still present 9/9/9/8. Edge still > 0: 12/12/12/10. Edge still > 2 bps: **0**. Edge still > 12 bps: **0**.
**Net-of-fee stale-quote count at 250 / 500 / 1000 / 2000 ms: 0 / 0 / 0 / 0 for both markets.** No snapshot at any time had even a gross cross above 2 bps.
**Caveats on granularity:** With ~2 s polls and ~320 ms RTT, crosses that live less than ~2 s can be missed, so the snapshot count is a **lower bound** on sub-second events. The "net-of-fee = 0" result is therefore about what a REST-polling retail taker can see and act on. It does not show that HFT-scale transient crosses never happen. It does show that anything catchable at our arrival delay (≥ ~400 ms effective) is too small to cover a 12 bp fee. Those HFT-scale crosses would be SCM territory anyway (S12's "Thames River"). Rechecks tell us whether a quote was present at each recheck; they can't prove continuous presence in between. The data came from one 20-minute window on a Thursday evening ET. Volatile periods could differ, but a 12 bp hurdle is ~7× the max gross cross seen.

## Card 04 rule applied
- Spread disappears at arrival? The small crosses mostly *persist*, which marks them as basis, not staleness.
- **Fees consume it? YES.** Max gross 1.78 bps vs 12 bps retail taker (24 bps for a taker round trip; +80 bps if hedged at Kraken T1).
- **Needs inaccessible membership economics? YES.** A zero-fee taker (SCM rebate) plus lower latency (authenticated WS/FIX) is the only way the S12 mechanism pays.
→ **REJECT** for Logan's retail account. Re-open only if Logan becomes a perps SCM (not recommended at this scale), or if public fee filings drop the retail taker fee below the observed crosses.

## Q5 — Logan account details (only needed to reopen; no credentials requested)
1. Kalshi account type for perps: Kalshi Prime (FCM) retail vs Self-Clearing Member (expected: Prime/retail, or not yet applied).
2. Perps/margin application status: not applied / pending / approved, and tutorial completed Y/N.
3. Fee tier shown in the app for perps (expected Tier 0: 0.120% taker / 0.020% maker) and 30D trailing notional volume (perps + predictions).
4. Whether the API key has perps/margin scope: what `/margin/enabled` returns for the account, and the perps API usage tier (Basic, etc.).
5. Margin mode available (isolated only in app; portfolio via API?) and the max leverage granted.
6. State of residence (confirm US; confirm the app shows perps as available there).
7. Any active perps promo or referral fee discount shown in the app (terms and expiry).
8. Coinbase/Kraken account fee tier, if a hedge leg were ever contemplated (the Coinbase retail fee isn't public).

## Sources (fetch times ET, 2026-09-24; full log `packets/.../docs/fetch_log.txt`)
- S13 Perps Fees Explained: https://help.kalshi.com/en/articles/16071417-perps-fees-explained (19:31:45)
- S12 The Facts Behind Kalshi's Perpetuals Volume: https://news.kalshi.com/p/the-facts-behind-kalshi-s-perpetuals-volume (19:31:46)
- S11 Sethi: https://rajivsethi.substack.com/p/volume-inflation-without-wash-trading (19:31:46; context only)
- Fee schedule (perps, Prime + Self-Clearing): https://kalshi.com/fee-schedule?product=perps (19:33–19:34, browser). `kalshi.com/docs/kalshi-fee-schedule.pdf` returned a Vercel checkpoint (429); that error body is kept and labeled.
- CFTC fee rebate filing: https://www.cftc.gov/filings/orgrules/rules0625267305.pdf (19:32:07)
- Help: funding (19:31:59), what-are-perps (19:32:00), margin (19:32:02), applying-for-access (19:32:41), BTC spec (19:32:42), available perps (19:32:43), margin account (19:32:45)
- Kalshi Perps API docs: https://docs.kalshi.com/margin.md, orderbook, markets, and fee-tier-rates pages (19:32:23–24); rate limits: https://docs.kalshi.com/getting_started/rate_limits.md
- Kalshi live public GETs: `/trade-api/v2/margin/markets`, `/margin/exchange/status` (19:32:32), `/margin/markets/{KXBTCPERP,KXETHPERP}/orderbook` (19:34–19:57)
- Coinbase rate limits (19:36); Kraken fee schedule (browser ~19:38); Coinbase Advanced fees (19:36; login-gated)

---
## AMENDMENT 01 — 2026-09-24 20:05 EDT (appended; the text above is unchanged. Pre-amendment sha256: 3f893cbfbc020fc6735b8557d3e7950745ea43c7c6564d59e3f79d3ac6d03fe0)
**Fees, per side and round trip.**
- Doc-quoted (Kalshi Prime Launch Fee Schedule, Tier 0): taker 0.120% and maker 0.020% of notional, per side. The doc says a round trip carries two fees.
- *Scout arithmetic* from those per-side rates:
  - maker 0.020% per side → **0.040% round trip** (4 bps)
  - taker 0.120% per side → **0.240% round trip** (24 bps)
  - taker-in plus maker-out → 0.140% (14 bps)
- Kraken Tier 1 spot taker 0.80% per side (doc-quoted) → *Scout arithmetic* 1.60% round trip.
- The verdict comparison "max gross cross 1.78 bps vs 12 bps" uses the one-side taker rate, which is the most lenient hurdle.

**FREEZE_GAP acknowledged (Archivist flag).** No freeze file was written before sampling.
- `script/perps_stale_sampler.py` was edited after the main run started: the `TRIGGER_BPS` argv was added, and the value used in the run was unchanged at 2.0.
- `script/analyze_sample.py` was edited mid-run (next-poll persistence block added).
- The phase-2 trigger (0.5 bp) was chosen **after** the main-run results showed no rechecks had fired.

The phase-2 arrival-delay numbers are therefore post-hoc and descriptive only. **The REJECT stands as a screen.** It rests on doc-quoted fees and eligibility (12 bp retail taker; SCM-only rebate), and no snapshot in either run exceeded 2 bps gross. The threshold list (0/1/2/5/12/14/24/92 bp) was also written during the main run, after partial data had been seen, so it is not pre-specified either, so the trigger choice doesn't matter to the verdict. Any reopening needs a fresh freeze.
