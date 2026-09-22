# R1 — Deep Research brief: Kalshi MM / sports / OSS vs Astra incumbent
**Packet:** R1  
**Date:** 2026-09-22 (America/New_York)  
**Owner:** Deep Research  
**Reviewer:** Conductor  
**Incumbent:** `17thgreen/GPT-6-Astra-Deathmatch` Q6 core allocator (F/P/R off); Q7 paircheck 2×2 in flight  

---

## Executive

Scanned public Kalshi venue docs (orderbook reciprocity, fee schedule PDF + fee-schedule page, API changelog on combo maker fees), GitHub OSS for Kalshi/Polymarket makers, one sports MM autopsy (polymm / kacho.io), and one academic binary-PM control paper (Feil & Nendel, arXiv:2607.17991). Roughly ~25 distinct sources touched; most Polymarket UI bots, LMSR toys, and crypto 5/15m makers were rejected as non-kernels or charter-idle. What survived are **measurement kernels**: (1) exact Kalshi fee + bids-only reciprocal book algebra; (2) binary Avellaneda–Stoikov with Bernoulli variance and explicit settlement penalty; (3) sports de-vig → quote → hedge with adverse-selection markout; (4) RFQ combo independent-leg calibration (Scout/displacement candidate); (5) maker ops rails (fee-credit floor, content-fresh book, queue attribution) from spencerfletcher. None of these invent P&L for Astra; all are proposals for Conductor triage under freeze → measure → Examiner. Incumbent remains primary until a bakeoff wins; non-NFL Kalshi structures flagged where kernel is clearer than retuning NFL maker.

---

## Landscape table

| Source | Type | Transferable kernel | Venue fit | Risk |
|---|---|---|---|---|
| [Kalshi orderbook responses](https://docs.kalshi.com/getting_started/orderbook_responses.md) | Venue doc | Bids-only; YES bid @ X ≡ NO ask @ 1−X; spread from complementary best bids | Kalshi native | Stale CDN GETs if not busted |
| [Kalshi fee schedule PDF](https://kalshi.com/docs/kalshi-fee-schedule.pdf) + [fee-schedule](https://kalshi.com/fee-schedule) | Venue doc | `fees = round_up(M×0.07×C×P×(1−P))` taker; maker often 0 else `0.0175×…`; series overrides; cancel free | Kalshi native | Series/combo overrides change economics silently |
| [API changelog — combo maker fees](https://docs.kalshi.com/changelog/index.md) | Venue doc | Combo maker fee multiplier; independent-NFL combo shard `KXMVECROSSCATEGORY0-SHARD1` no maker fee (post Aug 19 2026 rules) | Kalshi combos | RFQ / combo infra ≠ game-book MM |
| [spencerfletcher/market-maker](https://github.com/spencerfletcher/market-maker) | OSS Kalshi+Poly MM | Exact Decimal fee formula + credit-floor refuse; content-fresh WS; queue tracker; teardown rails | Kalshi path present | Strategy/sizing withheld; do not import live launcher |
| [rodlaf/KalshiMarketMaker](https://github.com/rodlaf/KalshiMarketMaker) | OSS Kalshi AS MM | Volume×spread selector; per-market A-S worker; inventory γ ramp; cancel-verify deselect | Kalshi | Naive σ; live-oriented; no sports pair algebra |
| [tfrmma/prediction-market-maker](https://github.com/tfrmma/prediction-market-maker) | OSS binary/categorical MM | `σ²=p(1−p)`; `r=p_fair−q·γ·p(1−p)·(T−t)`; Prelec favorite-longshot; 30s adverse mid markout | Kalshi+Poly | Hyperliquid hedge irrelevant; marketing density high |
| [Feil & Nendel arXiv:2607.17991](https://arxiv.org/html/2607.17991) | Academic | Latent-belief → price martingale; HJB quotes; running `γ q² ς²` + terminal `Φ=−γ_T q² p(1−p)` | Venue-agnostic LOB PM | Calibration heavy; not an executable bot |
| [kachence/polymm](https://github.com/kachence/polymm) + [adverse-selection autopsy](https://kacho.io/why-my-polymarket-arbitrage-bot-lost-money) | OSS sports MM + blog | De-vig fair; min_edge quote; fill→hedge both sides < $1; EDGE_LOST cancel; residual directional book | **Polymarket** (venue mismatch) | Stale odds → toxic fills; paid odds API; author P&L is anecdote not evidence |
| [jsteng19/kalshi-combos-research](https://github.com/jsteng19/kalshi-combos-research) | OSS Kalshi research | Fill vs resolution calibration; independent-leg product of 1-min mids; same-game correlation premium | Kalshi RFQ combos | Needs RFQ maker seat; retail-flow edge may decay |
| Hummingbot A-S guide | Blog | Classic `r=s−q γ σ²(T−t)` inventory skew | Continuous assets | Wrong variance for binaries unless adapted |
| openpx / Homerun / DRADIS / ImMike arb | SDK / platform / spam | Thin or UI-first | Mixed | Skip — no reconstructable measurement kernel |

---

## Proposals (≤5)

### R1-P1 — Kalshi fee + reciprocal-book measurement kernel (venue ground truth)
- **id:** R1-P1  
- **title:** Pin Examiner fee + book algebra to published Kalshi formulas  
- **source:** https://docs.kalshi.com/getting_started/orderbook_responses.md ; https://kalshi.com/docs/kalshi-fee-schedule.pdf ; https://kalshi.com/fee-schedule  
- **measurement_kernel:** For each tape tick, reconstruct YES/NO best bid/ask via complementarity (`ask_YES = 1 − best_NO_bid`). Fee on a fill of size C at price P: `round_up(M × rate × C × P × (1−P))` with rate ∈ {0.07 taker, 0 or 0.0175 maker, series overrides}. Joinable to Collector orderbook + trades GETs; scorecard must refuse “completed profit” without fee channel.  
- **dead_overlap:** Astra Q1–Q6 already assume an “inherited fee model”; this does **not** retune allocator. Overlap is documentation/hardening only. Distinct from Q7 pair-margin check. Cemetery irrelevant.  
- **cost_to_try:** ~4–8 person-hours (Simulator + Examiner unit tests + series-override table stub). Data deps: public fee PDF + one captured orderbook fixture. No paid data.  
- **recommend:** **try**  
- **why:** Without exact fee + reciprocal book, every later MM/challenger bakeoff is fee-blind. Lowest-cost gate for all seats.

### R1-P2 — Binary inventory MM with Bernoulli variance + settlement penalty
- **id:** R1-P2  
- **title:** Challenger kernel: binary A-S / Feil–Nendel settlement-aware quotes  
- **source:** https://arxiv.org/html/2607.17991 ; https://github.com/tfrmma/prediction-market-maker (pricing/fair_value.py algebra in README)  
- **measurement_kernel:** Fair mid \(p\); inventory \(q\); time-to-resolution \(T−t\). Reservation \(r = p_{\mathrm{fair}} − q\,\gamma\,p(1−p)\,(T−t)\); half-spread from intensity/γ (tfrmma closed form) **or** Feil optimal \(\pi^{b,*},\pi^{a,*}\) from HJB with running penalty \(\gamma q^2\varsigma^2\) and terminal \(\Phi=-\gamma_T q^2 p(1−p)\). Pre-settlement metrics: quote mid skew vs \(q\), width vs \(p(1−p)\), inventory path — **no** outcome P&L required for first freeze. Clock-joinable on Collector L2 + position ledger.  
- **dead_overlap:** **Not** Q6 paired NFL allocator; not Q7 chosen-pair cost filter. Partial conceptual overlap with inventory/completion ideas from Q2 (completion reduced inventory but did not maximize net) — treat as new challenger line, not silent retune of `000`. Crypto Gauntlet cards irrelevant.  
- **cost_to_try:** ~20–40 hours for a frozen offline simulator arm on non-NFL binary series (weather/politics) **or** single-game YES/NO without pair routing. Data deps: public orderbook tape; no kits required for synthetic intensity first pass.  
- **recommend:** **try**  
- **why:** Clearest LOB-PM theory with reconstructable algebra; fair-game displacement path if single-market inventory EV beats paired NFL maker under same capital constraints.

### R1-P3 — Sports de-vig / fill→hedge / adverse-selection markout (Kalshi-adapted)
- **id:** R1-P3  
- **title:** Sportsbook fair + paired hedge + odds-staleness adverse gate  
- **source:** https://github.com/kachence/polymm ; https://kacho.io/why-my-polymarket-arbitrage-bot-lost-money  
- **measurement_kernel:** (1) De-vig book odds → \(p_{\mathrm{fair}}\) (test proportional vs Shin; Shin was a silent bias in the autopsy). (2) Quote only if edge ≥ min_edge vs Kalshi touch. (3) On fill, attempt opposite-side hedge so YES+NO acquisition < 1 (paired lock). (4) Adverse markout: compare \(p_{\mathrm{fair}}\) at quote vs at fill vs +Δt odds; cancel on EDGE_LOST. Pre-settlement objects: edge_at_quote, edge_at_fill, hedge_complete_flag, odds_age_sec. Venue mismatch flagged: Polymarket CLOB ≠ Kalshi — port algebra only.  
- **dead_overlap:** **High conceptual overlap with Q6/Q7 pair economics** (combined acquisition cost of chosen routes; Q7 isolates pair price check). Do **not** ship as silent Q6 retune. Useful as: (a) external-odds feature arm **after** Q7 freeze, or (b) adverse-selection scorecard Adversary can demand on any sports maker. Author’s +$5k wallet claim is **not** evidence for Astra.  
- **cost_to_try:** ~15–25 hours for measurement-only (odds freshness + markout join on Collector panel); + paid the-odds-api or equivalent if Scout approves. Full bot port: defer.  
- **recommend:** **try** (measurement / Adversary gate first; strategy port secondary)  
- **why:** Only OSS sports MM with honest adverse-selection autopsy; directly stress-tests Astra’s queue/pair assumptions without inventing EV.

### R1-P4 — Kalshi RFQ combo independent-leg calibration (displacement Scout)
- **id:** R1-P4  
- **title:** RFQ combo maker edge: fill vs independent-leg product vs resolution  
- **source:** https://github.com/jsteng19/kalshi-combos-research  
- **measurement_kernel:** For settled RFQ combo fills: independent-leg price = product of per-leg 1-minute top-of-book mids at fill minute (flip 1−mid for NO legs); compare fill − model and fill − resolution. Slice by price band, same-game vs decorrelated, leg count. Read-only REST/WS crawl; no live quoting required for first measurement freeze.  
- **dead_overlap:** None with Q1–Q6 NFL game-book allocator. Distinct market structure (RFQ parlays). Fee note: combos often have maker fees (50% of taker) except specified independent-NFL shards — must pin against fee schedule/changelog.  
- **cost_to_try:** ~30–60 hours for crawl + Polars pipeline on a bounded series-day window; needs read-only Kalshi API credentials (Collector/Mechanic path — not chat). Disk for Parquet shards.  
- **recommend:** **defer**  
- **why:** Strongest non-NFL displacement candidate if edge survives fee+collateral, but RFQ maker ops and credentialed crawl are out of Deep Research scope this week; Conductor should assign Scout + Collector before R&D Variants build.

### R1-P5 — Maker measurement rails: fee-credit floor, content-fresh book, queue attribution
- **id:** R1-P5  
- **title:** Adopt spencerfletcher measurement rails (not live launcher) into Astra sim/collector  
- **source:** https://github.com/spencerfletcher/market-maker (README + CASE_STUDY.md)  
- **measurement_kernel:** (1) Evaluate published fee with venue rounding; **refuse** quotes whose maker credit floors to zero. (2) Book freshness = content/transaction-time change, not socket ping. (3) Queue-attribution tracker for resting fills vs assumed early queue. Join to Astra Q1 queue scenarios (3300 / 10000) as **instrument**, not as new strategy.  
- **dead_overlap:** Directly critiques Q1 “early queue remains an assumption” and any fee-table approximations in maker replay. Does not replace Q6 allocator. Live arming shim explicitly **out of scope** (NO LIVE ORDERS).  
- **cost_to_try:** ~12–20 hours to port Decimal fee+floor tests + freshness predicate into Simulator/Collector unit suite. No production constants from that repo (withheld).  
- **recommend:** **try**  
- **why:** Hardens incumbent evidence quality before shadow; cheap relative to new strategy waves.

---

## Explicit skips (with reason)

| Source | Why skip |
|---|---|
| `braedonsaunders/homerun` | Platform/UI + “25+ strategies” marketing; no single reconstructable kernel |
| `ImMike/polymarket-arbitrage` | Cross-venue UI bot; winrate/dashboard spam; text-similarity matching unreliable |
| `mbordash/DRADIS` | LLM advisor / quantum marketing; not a measurement kernel |
| `artyomderkach-bit/kalshi-15m-market-maker` | BTC/ETH short-horizon — Gauntlet science **IDLE** |
| `milesChild/kalshi-naive-market-maker` (+ sophisticated fork) | Thin naïve LOB; low transfer beyond “quote both sides” |
| LMSR / Hanson AMM repos | AMM cost-function markets ≠ Kalshi LOB |
| `openpx-trade/openpx` | Unified SDK only; no strategy/measurement algebra |
| Hummingbot A-S alone | Continuous-asset σ; use only via binary adaptation (covered in R1-P2) |
| Crypto Gauntlet dead cards (F1–F4, W2-*, CB-VEL) | Charter: irrelevant unless OSS clearly maps; none did for sports/MM |

---

## Next fetch list (Conductor → Collector / Simulator)

1. **Collector:** Durable GET orderbook + trades for ≥1 non-NFL binary series (weather or politics) and continuing NFL panel — needed for R1-P2 synthetic→historical bridge.  
2. **Collector:** Series ticker → fee multiplier / maker-fee flag table (from fee schedule + changelog), frozen as JSON before any sim claims.  
3. **Simulator:** Unit tests for reciprocal ask derivation + fee `round_up` against PDF examples (R1-P1).  
4. **Simulator:** Optional intensity/markout harness stubs for R1-P2/P3 (pre-settlement only).  
5. **Scout:** Confirm whether RFQ combo historical fills are accessible with desk’s read-only key before un-deferring R1-P4.  
6. **Do not fetch:** paid sportsbook scrapers into live path; owner kit ZIPs belong to KITS-1 not R1.

---

## Footer

NO invented Δ / P&L / fill rates / win rates for Astra. Author OSS P&L cited only as narrative context, never as desk evidence. Examiner not bypassed. Not for live. Extrapolations = projections only. Incumbent Q6 stands until bakeoff.
