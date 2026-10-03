# CEM-ASTRA-20260924-005 — Card 04: Kalshi perps stale-quote arbitrage on a retail (Kalshi Prime Tier 0) account (KILLED by Scout screen)

- **CEM_ID:** CEM-ASTRA-20260924-005
- **DATE:** 2026-09-24 (ET) · The Archivist (Registry) · written ~20:02 ET
- **CARD:** Kalshi Edge Research card 04, "Stale quotes in subsidized perps". This entry covers the **retail-account taker stale-quote arbitrage only**, measured against the Coinbase Exchange WS (`level2_batch`) reference on KXBTCPERP / KXETHPERP.
- **FAMILY:** taker "stale quote" arb, Kalshi perps vs a spot reference, on a Kalshi Prime retail fee tier
- **DECISION:** **KILLED (REJECT for this account)**. Killed 2026-09-24 by the Market Scout's screen.
- **CLASS of killing evidence:** **prospective shadow — FREEZE_GAP** [V]. The screen was a forward live capture of public data (Scout mode line 5: "READ-ONLY. Public GETs, public docs, and unauthenticated public WS only. No orders, no accounts, no keys…"). However, the Conductor definition of prospective shadow requires "frozen-before-outcome", and **no freeze existed before the screen ran** (see Freeze status). The class is therefore recorded with the **FREEZE_GAP** flag (CLASS_FIT_POOR on the frozen criterion). The gap is not hidden. Scope: a single window of about 21 min on one evening.

## Cause of death

`SCOUT_PERPS_STALE_QUOTE_SCREEN_2026-09-24.md` (sha256 `3f893cbfbc020fc6735b8557d3e7950745ea43c7c6564d59e3f79d3ac6d03fe0`), verbatim:

- Line 72: "**Net-of-fee stale-quote count at 250 / 500 / 1000 / 2000 ms: 0 / 0 / 0 / 0 for both markets.** No snapshot at any time had even a gross cross above 2 bps."
- Line 76: "Spread disappears at arrival? The small crosses mostly *persist*, which marks them as basis, not staleness."
- Line 77: "**Fees consume it? YES.** Max gross 1.78 bps vs 12 bps retail taker (24 bps for a taker round trip; +80 bps if hedged at Kraken T1)."
- Line 79: "→ **REJECT** for Logan's retail account. Re-open only if Logan becomes a perps SCM (not recommended at this scale), or if public fee filings drop the retail taker fee below the observed crosses."

Supporting numbers, quoted from the packet [V]:
- Fees (Scout line 19, Kalshi Prime tab): "**Tier 0 (<$100k 30D): Taker 0.120%, Maker 0.020%.**" The +0.3/−0.3 bp program (line 25): "This program is not live".
- Sample (line 56): "Main run: 19:36:01–19:51:00 ET, 899 Kalshi GETs, 0×429. Phase 2: 19:51:56–19:56:59 ET, 391 GETs, 0×429. Phase 2 fired event-triggered re-GETs at +250/500/1000/2000 ms whenever edge > 0.5 bp (≤1 sequence per 10 s per market)."
- `raw/sample_main/analysis.json` (`681aafb3…`), KXBTCPERP: `max_raw_edge_bps` 1.7754350615368502, `max_adj_edge_bps` 1.344218940695224, `snap_count_raw_edge_gt_2bps` 0, `snap_count_raw_edge_gt_12bps` 0, `poll_gap_s_median` 2.0001580715179443, `rtt_ms_median` 322.34084606170654, `n_trigger_sequences` 0.
- `raw/sample_phase2_rechecks/analysis.json` (`f3fa72ee…`), KXBTCPERP: `max_raw_edge_bps` 1.6591806018067823, `n_trigger_sequences` 26, `recheck_persistence` effective delay medians 0.40974920988082886 / 0.7485902309417725 / 1.1626766324043274 / 2.1603320837020874 s for the 0.25 / 0.5 / 1.0 / 2.0 s rechecks; `edge_still_gt0` 26 of 26 at every recheck.
- Venues (lines 43–46): Binance.com "N (451)" BLOCKED; Bybit "N (403)" BLOCKED (geo); CME "N (no HTTP response)" BLOCKED; OKX global "READABLE, NOT USABLE", excluded.

## Check of the Conductor's summary against the Scout files

| Conductor claim | Scout source | Verdict |
|---|---|---|
| Taker stale-quote arb vs Coinbase Exchange WS on a Prime retail fee tier | Lines 5, 19; FEED_AUDIT | MATCH [V] |
| "Round-trip fees are 12 bps taker" | Line 77: "12 bps retail taker (**24 bps for a taker round trip**…)"; line 19 Taker 0.120% per side | **MISMATCH [V]**: 12 bps is the **per-side** taker fee. The Scout's taker round trip is **24 bps** (+80 bps if hedged at Kraken T1). |
| "4 bps all-maker" round trip | Line 19 Maker 0.020% per side | CONSISTENT [I]: 2 × 0.020% = 4 bps is arithmetic. The Scout does not state a 4 bps figure. |
| Max observed gap 1.78 bps | Line 77; main analysis.json 1.7754… | MATCH [V] |
| Net-of-fee opportunities at 250/500/1000/2000 ms: 0 BTC, 0 ETH | Line 72 | MATCH [V] |
| Gaps looked like steady basis, not staleness | Line 76 | MATCH [V] |
| Did NOT prove "anything below 2 s (polling was about every 2 s)" | Lines 56, 73; phase-2 recheck delays ~0.41–2.16 s | **PARTIAL / NUANCE [V]**: the base poll was ~2 s, and line 73 says sub-~2 s crosses "can be missed, so the snapshot count is a **lower bound** on sub-second events". But phase-2 triggered rechecks **did** probe effective delays of about 0.41/0.75/1.16/2.16 s, and line 73 concludes "anything catchable at our arrival delay (≥ ~400 ms effective) is too small to cover a 12 bp fee". Correct scope: NOT proven below about 400 ms effective arrival, or for crosses that live and die between polls. |
| Single 20-minute window 19:36–19:57 ET | Line 56 (19:36:01–19:51:00 + 19:51:56–19:56:59); line 73 "one 20-minute window on a Thursday evening ET" | MATCH [V] (about 21 min wall clock including the phase gap; a 20 s smoke run at about 19:35 ET is not counted) |
| Nothing about self-clearing-member economics or the unlaunched ±0.3 bp program | Lines 25, 73 ("SCM territory") | MATCH [V] |
| Nothing against Bybit, Binance.com, CME, OKX (blocked/excluded, not tested) | Lines 43–46 | MATCH [V]. Omission [V]: other venues listed in FEED_AUDIT but not used for counts (for example Kraken, Binance.US) were also not tested for staleness; counts use Coinbase Exchange only. |
| Reopen: verified member-tier fee schedule on our account, or sub-second capture showing gaps above round-trip cost. No retune. | Line 79: "Re-open only if Logan becomes a perps SCM … or if public fee filings drop the retail taker fee below the observed crosses." | **WORDING DIFFERS [V]**: the two are compatible, not identical. Both are recorded below; the Conductor's is the registry rule. |

## Freeze status

- **No freeze before outcome: FREEZE_GAP [V].** No card-04 FROZEN_*/pre-registration file exists for this screen.
- Pre-run artifact: `packets/CONDUCTOR_ROUTING_KALSHI_EDGE_RESEARCH_2026-09-24.md` (sha256 `91f87bcfa7ab6c25234c9e6aa7e46d68ea6c9840b6e2550f585ca752c100e028`, mtime 19:30:47 ET). Line 13: "Perps (card 04) — Market Scout: short read-only feasibility screen (account fee tier/access, synced feeds, stale quotes surviving realistic arrival). No speed spend." This is a routing brief, not a freeze. It has no thresholds, delays or sha pins.
- The Adversary packet `packets/ADVERSARY_DEAD_CARD_OVERLAP_EDGE_RESEARCH_2026-09-24.md` (`b434220493c8dfae34c123786153ad038ae3cb2832272254a2e97673f7e87fdd`, mtime 19:37:49 ET) postdates the start of the main run (19:36:01 ET). Its card-04 row says the "Scout … is in progress".
- Script timing [V]: `script/perps_stale_sampler.py` mtime 19:37:36 ET and `script/analyze_sample.py` mtime 19:37:41 ET, both after the main run began. README line 5: "TRIGGER was made an argv after the main run started. Main run used the hard-coded 2.0, identical value". The phase-2 trigger of 0.5 bp was chosen after the main run fired 0 rechecks at 2.0 bp [V: README line 4, main `n_trigger_sequences` 0].
- **Effect:** the kill rests on public fee schedules (independent of the sample) versus a max gross cross of 1.78 bps. That margin (line 73: "a 12 bp hurdle is ~7× the max gross cross seen") does not depend on the post-start knobs [I]. The FREEZE_GAP flag stays anyway.

## Evidence IDs + pins

All 126 files (the Scout md and all 125 files in the packet dir, including `MANIFEST.sha256`) are pinned in `cemetery/CEM-ASTRA-20260924-005_EVIDENCE_SHA256SUMS.txt`. Paths there are relative to `lab/governance/astra/`. Re-verified `sha256sum -c` 126/126 OK at ~20:01 ET. The packet's own `MANIFEST.sha256` (`61d026519cb7c92290a0a62a03df8ad3d75e706838f2d9494a63c55664820361`) also passes `sha256sum -c` and covers every packet file except itself. The packet dir has 125 files and 17,850,878 bytes.

| Evidence ID | Path | sha256 |
|---|---|---|
| Scout screen | `SCOUT_PERPS_STALE_QUOTE_SCREEN_2026-09-24.md` | `3f893cbfbc020fc6735b8557d3e7950745ea43c7c6564d59e3f79d3ac6d03fe0` |
| Packet manifest | `packets/scout_perps_screen_2026-09-24/MANIFEST.sha256` | `61d026519cb7c92290a0a62a03df8ad3d75e706838f2d9494a63c55664820361` |
| Packet README | `…/README.md` | `0c9c2ef30e7fd5c03a0790a9073993c6230fe897756fe3928d1ec472ff530bc5` |
| Fee schedule capture | `…/docs/fee_schedule_perps_browser.txt` | `b751feeef75023f7cd71a4ca5d3bb12688d60270be4da795919af40132806b32` |
| Feed audit | `…/feeds/FEED_AUDIT.md` | `8e1d2772bdd0a8cd784a91887735ca76191cd9d6be7e2bbbcdc1ad93ee9b6fcd` |
| Bybit geoblock body | `…/feeds/bybit_book.json` | `7ef856c945703d5772f1b1f2a8c65913247c9b0769302b10facfe14fa1e2083c` |
| Binance.com 451 body | `…/feeds/binance_com_book.json` | `79c1db471a4cdc1c8565b5dfc52e0ed2d29962738ee4d28597696fcd0920e348` |
| Kalshi call log | `…/kalshi_call_log.txt` | `03e446cd646895e96c6b366fd03ca6002f87edfd8ecb941085f42d5cdf5d0993` |
| Sampler | `…/script/perps_stale_sampler.py` | `c601e8a268c5438e8cd8a8dc0a6248c934eb2bb10a7d2a1c5194e52145254e9c` |
| Analyzer | `…/script/analyze_sample.py` | `aa33b9637828c48e4c8e36a71cd55a2009980906474310fbf8e395880fe9f799` |
| Main analysis | `…/raw/sample_main/analysis.json` | `681aafb3ee4baa0aea3cf78f971b063450ea7a9e3d1ab7dc58fc755eaee4147c` |
| Main samples | `…/raw/sample_main/kalshi_samples.jsonl` | `2a488571c2d094b52dee015fa55d20af2f8422d3e2824b0ade3f3960ebceb57c` |
| Main run times | `…/raw/sample_main/run_times.txt` | `71aadb5f27e6ab75067486db9efc49303f62efa8f3982c420e8c56f00b7f0957` |
| Phase-2 analysis | `…/raw/sample_phase2_rechecks/analysis.json` | `f3fa72ee98cd793ed2041299dd0074e8e015b168f30cb19743e19416896da8bf` |
| Phase-2 samples | `…/raw/sample_phase2_rechecks/kalshi_samples.jsonl` | `ec36b2dd35c0116bcc0d5da3baf06d25301fca4376e2c147d598d8814d41970e` |
| Phase-2 run times | `…/raw/sample_phase2_rechecks/run_times.txt` | `a0d62f54c53ff66e481165ecd83f433046f4adcdff1e5d6867af6601b4d7dc8a` |
| Smoke samples | `…/raw/sample_smoke/kalshi_samples.jsonl` | `af234c93c3c70eab2c2317c93528a76dee4d481b25b0cc7b6bd5bc7619cd1451` |
| Routing brief (pre-run, not a freeze) | `packets/CONDUCTOR_ROUTING_KALSHI_EDGE_RESEARCH_2026-09-24.md` | `91f87bcfa7ab6c25234c9e6aa7e46d68ea6c9840b6e2550f585ca752c100e028` |
| Adversary overlap (post-start) | `packets/ADVERSARY_DEAD_CARD_OVERLAP_EDGE_RESEARCH_2026-09-24.md` | `b434220493c8dfae34c123786153ad038ae3cb2832272254a2e97673f7e87fdd` |

Prior dead cards in the same family, cited by the Adversary card-04 row (not re-verified here): `archive/cemetery/CEM-20260910-003.md`, `CEM-20260911-003/-004/-005`.

## What this did NOT prove

- Anything below about 400 ms effective arrival, or crosses that open and close between the ~2 s polls (Scout line 73: the count is a lower bound). The Conductor phrased this as "below 2 s"; see the check table above.
- Anything beyond one window of about 21 min (19:36:01–19:56:59 ET, one Thursday evening). Volatile periods could differ (line 73).
- Anything about self-clearing-member (SCM) economics, or the ±0.3 bp program that "is not live".
- Anything against Bybit, Binance.com, CME or OKX (blocked or excluded, not tested), or any reference other than Coinbase Exchange.
- API perps access for this account: UNVERIFIED (Scout Q5).

## Reopen rule (registry)

- **Conductor:** reopen only with new evidence: (a) a verified member-tier fee schedule on our account, or (b) sub-second capture showing gaps above round-trip cost. **No retune.**
- **Scout (line 79), also on record:** Logan becomes a perps SCM, or public fee filings drop the retail taker fee below the observed crosses.
- Any reopen needs a **new freeze before outcome**. That closes this entry's FREEZE_GAP.

## Rules

- Frozen negative stays visible. Never delete or soften this entry.
- No resurrection without a **new freeze**.
- No live orders. No PnL invented.
