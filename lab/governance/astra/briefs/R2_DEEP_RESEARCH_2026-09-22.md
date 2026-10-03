# R2 — Deep Research brief: post-Q7 orthogonal kernels
**Packet:** R2  
**Date:** 2026-09-22 (America/New_York)  
**Owner:** Deep Research  
**Reviewer:** Conductor  
**Context:** Q7 **SCORED_KILL_B_KEEP_000**; capital-structure freeze in flight; prefer **R1-P1 feebook + R1-P5 rails** stress on Q6-`000`.  

---

## Executive

After Q7 KILL Arm B / KEEP shadow `000`, this cycle does **not** reopen pair-check or capital-structure. R2 delivers five measurement kernels that either (a) harden fee/queue truth under the KEEP line, or (b) open Scout-accepted non-ML structures (MLB, pass-yards) and process gates (kickoff SoT), with spread/total **deferred** until C1 PIT@CLE smoke. Four of five explicitly consume R1-P1; three consume R1-P5; R2-P5 uses feebook for fee-aware adverse objects. Crypto F1–F3, more `KXNFLGAME` MM capacity, R1-P2 challenger open, and RFQ remain out of scope. No invented PnL. No live orders.

## Proposals

### R2-P1 — Feebook+rails hygiene stress on Q6-000 (instrument only)
- **source:** lab/governance/astra/packets/R1-P1-FEEBOOK_EXTRACT_2026-09-22.md ; lab/governance/astra/packets/R1-P5-RAILS_EXTRACT_2026-09-22.md ; BOARD_2026-09-22 fee-pin ≠ R1-P1 risk
- **measurement_kernel:** Re-score Q6-000 historical completed-net channel using published Kalshi fee round_up algebra (R1-P1) and label fills with R1-P5 instruments: maker_credit_floor_zero_refuse, content_fresh_flag, queue_attribution_bin vs assumed q3300/q10000. Pre-settlement outputs only: fee_delta_vs_inherited_model, freshness_gap_sec, queue_bin_mismatch_rate. No signal retune of 000.
- **dead_overlap:** Touches Q6-000 as measurement subject only — NOT a Q7 reopen, NOT capital-structure A1/A2/A3, NOT F1–F3. Distinct from Q7 pair-check 2×2 (cemetery CEM-ASTRA-20260922-001).
- **uses_r1_p1_feebook:** True
- **uses_r1_p5_rails:** True
- **cost_to_try:** 8-16h Simulator unit+fixture join; Examiner reviews test artifacts; Adversary spot-check fee-pin claim
- **recommend:** **try**
- **why:** Board risk #1: KEEP 000 fee-honest PASS used inherited model not closed R1-P1 pin. Highest-leverage hygiene before any challenger bakeoff.

### R2-P2 — KXMLBGAME daily T-window microstructure generalization
- **source:** lab/governance/astra/SCOUT_BRIEF_2026-09-22.md §kernel3 ; Scout triage TRY
- **measurement_kernel:** On KXMLBGAME same-day events: capture orderbook+trades under GET allowlist; join R1-P1 fee on fills and R1-P5 content-fresh + queue-attribution labels. Measure: time-to-kickoff liquidity shape, reciprocal-book spread, adverse mid markout over short windows — compare shape statistics to NFL T−7d→T−3h lab objects without porting Q6 allocator.
- **dead_overlap:** Low vs Q6–Q7 NFL game MM; orthogonal to capital-structure; crypto F1–F3 N/A. Not more KXNFLGAME capacity.
- **uses_r1_p1_feebook:** True
- **uses_r1_p5_rails:** True
- **cost_to_try:** 12-24h Collector panel design + Simulator markout harness; high event count / short windows
- **recommend:** **try**
- **why:** Scout-accepted fair-game displacement measurement; daily sport stress-tests timing lab without touching KEEP 000 arms.

### R2-P3 — KXNFLPASSYDS multi-strike ladder latent (next prop-rich slate)
- **source:** SCOUT_BRIEF_2026-09-22.md §kernel2 ; Scout triage TRY (not ATL@GB)
- **measurement_kernel:** For a prop-rich slate: at each decision minute, record ladder strike set, TOB mid per strike, and fee-aware effective touch via R1-P1. Test whether strike mids share one latent (player-mean) via cross-strike residual after monotone fit, vs fragmented independent books. Rails: content_fresh_flag per strike book; refuse stale WS-only freshness.
- **dead_overlap:** Medium same-game overlap with incumbent events — different contracts; not Q7 pair-check; not capital-structure; not F1–F3.
- **uses_r1_p1_feebook:** True
- **uses_r1_p5_rails:** True
- **cost_to_try:** 10-20h small panel + Polars residual harness after next prop-rich slate mapped
- **recommend:** **try**
- **why:** Multi-outcome kernel without leaving football; Scout gate already TRY.

### R2-P4 — Same-event KXNFLSPREAD(+TOTAL) vs ML microstructure contrast
- **source:** SCOUT_BRIEF_2026-09-22.md §kernel1 ; Scout triage TRY after C1 PIT@CLE
- **measurement_kernel:** Once C1 PIT@CLE admit/smoke stable and spread/total listing unblocked: same kickoff, compare ML vs spread vs total books on reciprocal spread, queue-attribution bins (R1-P5), fee-aware adverse markout (R1-P1). Question: is ML already a sufficient statistic for maker adverse selection, or do side markets diverge?
- **dead_overlap:** High thematic overlap with incumbent NFL events/T−7d — measurement contrast only; do NOT steal poll budget from PIT@CLE; not Q7 retune; not capital-structure.
- **uses_r1_p1_feebook:** True
- **uses_r1_p5_rails:** True
- **cost_to_try:** Same collector pattern × N side markets; gated start
- **recommend:** **defer**
- **why:** Conductor/Scout gate: only after C1 PIT@CLE smoke; 429 blocked listing this pass.

### R2-P5 — Kickoff SoT mismatch + adverse objects join (Clock/Collector)
- **source:** SCOUT_BRIEF kickoff +3h note ; R1-P3-ADVERSE demanded objects ; occurrence_datetime pin
- **measurement_kernel:** Measurement-only: for holdout vs live events, record holdout_kickoff_utc, kalshi_occurrence_datetime, delta_sec, and which clock Collector windows used. Join R1-P3 objects when external odds present: edge_at_quote, edge_at_fill, hedge_complete_flag (fee-aware via R1-P1), odds_age_sec. Output is a provenance/scorecard gate — not a strategy.
- **dead_overlap:** Orthogonal to Q6–Q7 signal/capital-structure/F1–F3. Complements ADMIT-1; does not reopen Q7.
- **uses_r1_p1_feebook:** True
- **uses_r1_p5_rails:** False
- **cost_to_try:** 4-10h Collector+Archivist schema + Adversary scorecard refuse rule
- **recommend:** **try**
- **why:** Wrong T−7d from mixed clocks is process failure; cheap gate; uses feebook for fee-aware hedge_complete when odds path exists.

## Explicit skips

| Item | Why |
|---|---|
| Q7 ITERATE / Arm B revive | Cemetery CLOSED; 95%-of-D bar stands |
| Capital-structure A1/A2/A3 variants | Separate freeze in flight — out of R2 |
| More KXNFLGAME MM capacity | Incumbent; Scout excluded |
| KXNCAAFGAME | Scout DEFER until listing |
| KXMVENFL* | Scout SKIP empty inventory |
| R1-P2-CHALLENGER open | Still QUEUE until Conductor kick |
| R1-P4 RFQ | DEFER Scout+Collector access |
| Crypto F1–F3 / Gauntlet waves | Idle science |

## Next fetch

1. Simulator+Examiner: R2-P1 fee_delta + rails labels on Q6-000 fixtures (no retune).
2. Collector: KXMLBGAME panel path for R2-P2 (after ADMIT-1/C1 priorities).
3. Scout: next prop-rich slate for R2-P3 (not ATL@GB).
4. Do not start R2-P4 until C1 PIT@CLE smoke stable + spread listing OK.
5. Collector+Archivist: kickoff SoT fields for R2-P5.

## Footer

NO invented Δ / PnL / fill rates / win rates. Examiner not bypassed. Not for live. Dead-card overlap named above.
