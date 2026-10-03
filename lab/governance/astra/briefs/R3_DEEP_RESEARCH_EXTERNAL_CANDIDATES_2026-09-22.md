# R3 — Deep Research: sharp external candidate hunt (post-R1/R2)
**Packet:** R3  
**Date:** 2026-09-22 ~19:58 EDT (America/New_York)  
**Owner:** Deep Research  
**Reviewer:** Conductor  
**Incumbent:** Q6-000 KEEP (no retune); Q7 SCORED_KILL_B_KEEP_000; R1-P1/R1-P5 pinned; Variants owns R2-P1 fee-sensitivity; queue-fragility freeze on 000  

---

## Executive

**Thin-well call: YES for strategy challengers that could BEAT Q6-000; NO (usable) for fee+queue HARD-STRESS measurement kernels.**

Post-R1/R2, public Kalshi/PM OSS is crowded with dashboards, AI wrappers, crypto 15m makers (Gauntlet idle), and LMSR toys. Re-scanning GitHub + papers/blogs for *new measurable objects* (not R1-P1/P5 retreads, not frozen S1/S4/S5/R2-P3 subjects, not S2/R2-P4 start) yields **four** reconstructable kernels and no fifth strong enough to pad. The highest-leverage finds are: (1) venue-reported `fee_cost` as superior ground truth to closed-form R1-P1; (2) official `queue_position_fp` as calibrator for L2 FIFO cancel models (acheron/tfrmma); (3) Bürgi–Deng–Whelan native Maker/Taker + favorite–longshot band expectancy on Kalshi settled tape; (4) Dubach SF1/SF2 longshot-spread + depth-concentration shape stats ported to Kalshi bids-only books. Bacchus-mm's *instrumentation* (not its retired 15m strategy) supplies fee_cost preference and refusal-lease algebra; its crypto PnL is **not** Astra evidence. No invented PnL. No live orders. No 000 retune. No wholesale strategy ports.

---

## Landscape table (sources touched this pass)

| Source | Type | Transferable kernel | Venue fit | Risk / disposition |
|---|---|---|---|---|
| [zainbacchus/bacchus-mm](https://github.com/zainbacchus/bacchus-mm) | OSS Kalshi MM lab + autopsy | Prefer WS/API `fee_cost` over model; queue-depth-at-join logs; markouts; refusal leases (flow gate, first-minute toxicity, protection-cost floor) | Kalshi native | **15m crypto strategy SKIP** (Gauntlet idle); extract measurement only; author −$62.92 is not Astra EV |
| [Kalshi Fill model](https://docs.kalshi.com/python-sdk/models/Fill) / [get-fills](https://docs.kalshi.com/api-reference/portfolio/get-fills) | Venue API | `fee_cost`, `is_taker` on own fills | Kalshi native | Auth'd portfolio path — Collector/Mechanic, not chat |
| [Kalshi queue_position](https://docs.kalshi.com/api-reference/orders/get-order-queue-position.md) / [queue_positions](https://docs.kalshi.com/api-reference/orders/get-queue-positions-for-orders) | Venue API | `queue_position_fp` = contracts ahead (price-time) | Kalshi native | Needs resting order (demo/paper); no live Astra orders |
| [tfrmma/realistic-mm-backtester](https://github.com/tfrmma/realistic-mm-backtester) | OSS FIFO MM backtester | `ReduceRatioCancelModel` / `ProbQueueCancelModel`; fill.qty_in_front; latency lognormal | Venue-agnostic LOB | Crypto examples — port algebra to Kalshi L2 only |
| [UjaanRakshit/acheron](https://github.com/UjaanRakshit/acheron) | OSS L3/queue sim | Three fill models (optimistic / pro_rata_cancel / conservative); `estimate-queue` from top-N; markout sign-flip when fill model changes | Equity ITCH heritage | Extract fill-model triad + estimate-queue; do not import equity strategy |
| [Bürgi, Deng & Whelan 2026](https://www.karlwhelan.com/Papers/Kalshi.pdf) (also SSRN 5502658 / CEPR DP20631) | Academic Kalshi | Native Maker/Taker ID; FL bias; Mincer–Zarnowitz \(Y-P=\alpha+\psi P\); post-fee ROI by 10¢ bands; makers ≥50¢ ~+2.6% (paper claim — **replicate, do not cite as Astra EV**) | Kalshi native | Pre-2025 fee regime in sample; pin post-Apr-2025 maker fees via R1-P1 |
| [Kalshi Get Trades](https://docs.kalshi.com/api-reference/market/get-trades.md) | Venue API | Public `taker_outcome_side` / `taker_book_side` (aggressor ground truth) | Kalshi native | Unlike Polymarket — refuse Lee-Ready on Kalshi |
| [Dubach arXiv:2604.24366](https://arxiv.org/html/2604.24366v2) + [philippdubach/polymarket-microstructure](https://github.com/philippdubach/polymarket-microstructure) | Academic Polymarket | SF1 longshot spread premium; SF2 depth ~uniform grid; feed-inferred direction ~59% (Poly-specific) | Poly CLOB | Port SF1/SF2 shape algebra to Kalshi bids-only; **skip** Poly direction-inference as Kalshi already exposes taker fields |
| [ElijahElrod/Kalm](https://github.com/ElijahElrod/Kalm) | OSS Rust Kalshi MM | Queue-position threshold requote; multi-level quoting | Kalshi | Thin README; A-S overlaps R1-P2 QUEUE — **skip as proposal** |
| [Rahman et al. arXiv:2510.15612](https://arxiv.org/html/2510.15612) SoK DePM | Survey | Taxonomy only | Mixed | **skip** — no measurable object |
| [arxiv:2606.04217](https://arxiv.org/html/2606.04217v2) Polymarket-v1 / True VPIN | Academic | Ground-truth VPIN vs classifiers | Poly on-chain | Skip unless Kalshi toxic-flow proxy defined without inventing VPIN on sparse sports books |

**Approx sources touched this pass:** ~22 (GitHub search batches + venue docs + papers + skipped dashboards/AI bots). Cumulative with R1 (~25) / R2 (~12) overlap discounted; **new high-signal objects: ~8**.

---

## Proposals (4 — well thin for a 5th)

### R3-P1 — Venue `fee_cost` ground truth vs closed-form R1-P1
- **id:** R3-P1  
- **title:** Prefer exchange-reported fee_cost; score model−venue fee delta  
- **source:** https://github.com/zainbacchus/bacchus-mm ; https://docs.kalshi.com/python-sdk/models/Fill ; https://docs.kalshi.com/api-reference/portfolio/get-fills  
- **measurement_kernel:** For each fill with venue `fee_cost` present: compute `fee_model = round_up(M×rate×C×P×(1−P))` via R1-P1; emit `fee_model_minus_venue_delta`, `is_taker`, and a scorecard refuse flag when completed-net claims use model-only while `fee_cost` was available. Prefer venue over model (bacchus rule). Pre-settlement / accounting objects only — no PnL invention.  
- **dead_overlap:** Touches fee channel of **R1-P1** (formula pin) and **R2-P1** (fee-sensitivity on 000, Variants-owned) but **new object** is venue-reported fee as superior ground truth, not another closed-form retune. Not Q7, not capital-structure, not F1–F3, not frozen S1/S4/S5/R2-P3.  
- **uses_r1_p1:** true (comparator)  
- **uses_r1_p5:** false  
- **cost_to_try:** 6–12h Simulator unit join on auth'd fill fixtures; Examiner refuse rule  
- **recommend:** **try**  
- **why:** Hard-stress fee honesty under R1-P1/R1-P5 regime; cheapest new instrument that can falsify model-only completed-net.

### R3-P2 — Official `queue_position_fp` vs L2 FIFO cancel-model estimate
- **id:** R3-P2  
- **title:** Calibrate L2 queue estimators against Kalshi queue_position_fp  
- **source:** https://docs.kalshi.com/api-reference/orders/get-order-queue-position.md ; https://github.com/tfrmma/realistic-mm-backtester ; https://github.com/UjaanRakshit/acheron  
- **measurement_kernel:** On demo/paper resting orders only: poll `queue_position_fp`. In parallel, estimate queue-ahead from L2 depth using (a) acheron `estimate-queue` knobs (`initial_ahead_fraction`, `depletion_ahead_probability`) and (b) tfrmma `ReduceRatioCancelModel` / `ProbQueueCancelModel`. Outputs: `abs_err_contracts`, `signed_bias`, fill-prediction Brier under each cancel model. No Astra live orders. Does **not** retune Q6-000 queue bins.  
- **dead_overlap:** Related to **R1-P5 rails** and **queue-fragility / R1-P5 QF freeze on 000** — named dead card: this calibrates the *estimator* against venue truth; it does **not** reopen QF scoring on 000 or change assumed q3300/q10000. Not S2/R2-P4 start.  
- **uses_r1_p1:** false  
- **uses_r1_p5:** true (extends queue-attribution instrument)  
- **cost_to_try:** 12–24h Collector demo poll + Simulator cancel-model harness; Mechanic for demo keys  
- **recommend:** **try**  
- **why:** Direct hard-stress of queue honesty — the one number bacchus said "no study could simulate."

### R3-P3 — Native Maker/Taker + favorite–longshot band expectancy (Bürgi–Deng–Whelan kernel)
- **id:** R3-P3  
- **title:** Kalshi settled-tape FL bias + Maker/Taker ROI by price band (measurement)  
- **source:** https://www.karlwhelan.com/Papers/Kalshi.pdf ; https://docs.kalshi.com/api-reference/market/get-trades.md  
- **measurement_kernel:** On a bounded settled panel (exclude crypto 5/15m; prefer weather/politics/economics first; sports only if Scout unblocks non-frozen series): join public trades (`taker_outcome_side` / `taker_book_side`) + resolution. Compute (1) Mincer–Zarnowitz \(Y_{ij}-P_{ij}=\alpha+\psi P_{ij}\) with event-clustered SE; (2) post-fee ROI by 10¢ bands using R1-P1 fee algebra (pin post-Apr-2025 maker-fee regime); (3) Maker vs Taker slice via native taker fields — **refuse Lee-Ready**. Pre-register bands before looking. Paper's +2.6% maker≥50¢ is **hypothesis to replicate**, not Astra evidence.  
- **dead_overlap:** Distinct from **R1-P3** (external-odds de-vig / hedge / odds_age — different objects). Not frozen **S1 KXMLBGAME / S4 KXNCAAFGAME / S5 RFQ / R2-P3 KXNFLPASSYDS**. Not Q6-000 retune. Not capital-structure / F1–F3.  
- **uses_r1_p1:** true  
- **uses_r1_p5:** false  
- **cost_to_try:** 16–30h Collector historical trades+settlement crawl + Polars panel; Examiner replication checklist  
- **recommend:** **try**  
- **why:** Only systematic Kalshi pricing paper with reconstructable Maker/Taker algebra; stress-tests whether incumbent sports maker sits in toxic longshot bands under fee honesty.

### R3-P4 — Longshot quoted-spread premium + depth-concentration shape (Dubach SF1/SF2 → Kalshi)
- **id:** R3-P4  
- **title:** Kalshi L2 shape panel: half-spread by mid decile + L1/top-10 depth vs uniform null  
- **source:** https://arxiv.org/html/2604.24366v2 ; Kalshi orderbook via R1-P1 reciprocal book  
- **measurement_kernel:** On a stratified Kalshi L2 panel (content_fresh via R1-P5): reconstruct YES/NO asks from bids-only (`ask_YES=1−best_NO_bid`). Emit (SF1) median quoted half-spread (bps of mid) by mid-price decile; (SF2) per-level share of cumulative top-10 depth and KL divergence from uniform \(1/10\) null. Compare sports vs non-sports category slices without porting Q6 allocator. No direction-dependent measures that need Lee-Ready (Kalshi has native taker).  
- **dead_overlap:** Low vs live pins. Orthogonal to capital-structure / Q7 / F1–F3. Not a retune of 000. Complements R3-P3 (price→outcome) with quote-side shape.  
- **uses_r1_p1:** true (reciprocal book)  
- **uses_r1_p5:** true (content_fresh_flag)  
- **cost_to_try:** 10–18h Collector L2 panel + Polars shape stats  
- **recommend:** **try**  
- **why:** Portable stylized-fact algebra; falsifies "PM books are top-heavy" assumption that often sneaks into queue/fill models.

---

## Explicit skips (with reason)

| Source / idea | Why skip |
|---|---|
| bacchus-mm **fifteen** crypto strategy wholesale | Gauntlet F1–F3 idle; author negative settled edge — extract instruments only (→ R3-P1/P2 objects) |
| ElijahElrod/Kalm live A-S / multi-level quoting | Thin; overlaps **R1-P2** QUEUE challenger; no new measurable object beyond queue thresholds (covered by R3-P2) |
| Dubach §7 feed direction ~59% as Kalshi kernel | Kalshi public trades already expose `taker_outcome_side` — Poly-specific failure mode; fold "refuse Lee-Ready" into R3-P3 |
| Rahman SoK DePM (arXiv:2510.15612) | Taxonomy / design survey — no reconstructable measurement object |
| Polymarket-v1 True VPIN (arXiv:2606.04217) | On-chain Poly; sparse sports books make VPIN fragile; no clean Kalshi port without inventing |
| Dashboards / AI bots (gamma-dashboard, Hexagon, kalshi-ai-trading-bot, hunch, etc.) | UI / marketing / LLM wrappers — no kernel |
| Crypto 15m arb / BTC-ETH makers (haoo99, artyomderkach, etc.) | Gauntlet idle |
| LMSR / Hanson AMM toys | Wrong market structure vs Kalshi LOB |
| spencerfletcher / rodlaf / tfrmma prediction-market-maker / Feil&Nendel / polymm / kalshi-combos | **Already consumed in R1** — do not re-propose |
| R1-P2 challenger open / R1-P4 RFQ / S2 R2-P4 start | Status quo: QUEUE / DEFER / WAIT — out of R3 hunt |
| Q6-000 retune / Q7 reopen / capital-structure / R2-P1 Variants work | Freeze / ownership rules |
| Fill-model triad as separate 5th proposal | Merged conceptually into R3-P2 cancel-model calibration; standalone acheron optimistic-vs-conservative markout flip is useful but not orthogonal enough to pad a 5th |

---

## Next for Conductor

1. Triage R3-P1…P4 (recommend all **try**; no pad-to-5).  
2. If capacity-constrained: **R3-P1 → R3-P2 → R3-P3 → R3-P4** (fee truth → queue truth → pricing bias → book shape).  
3. Assign Mechanic/Collector for auth'd fill + demo queue_position fixtures (R3-P1/P2) — not chat agents.  
4. Examiner: refuse model-only fee claims when `fee_cost` present; refuse Lee-Ready on Kalshi public tape.  
5. Do **not** start S2/R2-P4 capture; do **not** unfreeze S1/S4/S5/R2-P3; do **not** retune 000.  
6. If Conductor wants a 5th later: acheron fill-model markout sign-flip sweep on non-000 weather/politics L2 — currently skipped as near-duplicate of R3-P2.

---

## Footer

NO invented Δ / PnL / fill rates / win rates for Astra. Paper/OSS author returns cited only as replication hypotheses. Examiner not bypassed. Not for live. Dead-card overlaps named above. Thin-well for BEAT-000 strategy challengers stated explicitly.
