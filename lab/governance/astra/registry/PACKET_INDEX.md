# Astra / Kalshi — Packet Index
**Owner:** The Archivist (Registry) · agent `5099609`  
**Charter:** Working Plan v0.1 (GO 2026-09-22)  
**Updated:** 2026-09-24T19:50:00-04:00 (ET) — STEP0 record repair appended (sections below "Archivist standing gates"); previous update 2026-09-23T09:59:00-04:00 (ET). Backup: `registry/PACKET_INDEX.md.bak-20260924`.
**Rule:** freeze-before-outcome · done = artifact on disk · no invented results  
**Repo:** `17thgreen/GPT-6-Astra-Deathmatch`

## Open packets

| ID | Packet | Owner | Reviewer | Freeze / board status | Pointer |
|---|---|---|---|---|---|
| K1 | Owner kit ZIPs → restore | Logan (kits) / Simulator verifies | Conductor | Custody · Maker Audit + Measurement restored (Conductor) · Factorial ZIP present under `lab/astra-kits/` · Q7-RUN completed (Examiner scored) · keep open until Conductor closes custody | `lab/astra-kits/` |
| R1 | Deep Research brief + triage | Deep Research / Conductor triage | Conductor | **TRIAGED** · see R1-P* · no Examiner strategy score on R1 itself | `lab/governance/astra/briefs/R1_*` |
| B0 | Bakeoff template | Conductor | Examiner | Not started | Plan GO already |
| ADMIT-1 | Prospective panel + recorder | Collector + Registry | Conductor | **LIVE** · `admitted_at` `2026-09-22T21:18:13Z` · panel `2026-09-22.1-kalshi-occurrence-sot` · 16 events · PHI@CHI not backfilled · recorder GET-only · DB `/workspace/lab/astra-capture/prospective/capture.sqlite` | `lab/governance/astra/packets/ADMIT1_2026-09-22.md` |
| PITCLE-ID-LAG | PIT@CLE holdout identity join | Collector bind · Archivist hash-freeze | Conductor | **JOINED / HASH_FROZEN** · `REG-PITCLE-HOLDOUT-ID-JOIN-20260923` · `event`=`KXNFLGAME-26OCT01PITCLE` on `2026_04_PIT_CLE` · holdout sha256 `f8f6b5773072e92b0babe3c10940ed52c71878caca104c4e072c6a6efcb63bbb` · join receipt sha256 `72e6b1ed1ecbee34c2e74840da8fea1b90bc5368fa05c3c62225f0b924669a99` · canonical `astra-science/nfl_factorial_lab_20260921/RESERVED_HOLDOUT.json` + `astra-src/registry/RESERVED_HOLDOUT.json` · not a re-admit · ADMIT-1 untouched · no PnL · no orders | `packets/PITCLE_HOLDOUT_IDENTITY_JOIN_HASH_FREEZE_2026-09-23.md` · `packets/PITCLE_IDENTITY_LAG_WATCH_2026-09-23.md` · join `lab/astra-capture/prospective/pitcle_holdout_identity_join_2026-09-23.json` |
| Q6-000-HYGIENE | Adversary complacency spotcheck after Q7 score | Adversary | Conductor / Archivist | **HYGIENE** · five named risks · no verdict change · no PnL · no orders | `packets/Q6_000_COMPLACENCY_SPOTCHECK_2026-09-22.md` · risk register `ADVERSARY_RISK_REGISTER_2026-09-22.md` |
| R2-P5 | Kickoff SoT mismatch + R1-P3 adverse join (schema) | Collector + Archivist (+ Clock) | Conductor | **SCHEMA_ACCEPTED** · stub on disk · seed ADMIT-1 SoT-only · Adversary refuse bound to Examiner scorecard · not a strategy · no ADMIT-1 budget steal · schema `registry/schemas/r2_p5_admit_fields.schema.json` · id `REG-R2-P5-SCHEMA-20260922` | `packets/R2-P5_SCHEMA_ACCEPT_2026-09-22.md` · seed `packets/R2-P5_SEED_INSTANCE_ADMIT1_SOT_ONLY_2026-09-22.json` · refuse `packets/R2-P5_ADVERSARY_REFUSE_HYGIENE_2026-09-22.md` |
| R2-P1 | Fee/rails hygiene freeze on Q6-000 | R&D Variants / Simulator | Conductor | **CANONICAL** fee-sensitivity hygiene · older `fee_sensitivity_000_r1p1` packet **SUPERSEDED→R2-P1** · instrument only · pin Q6-`000` · packet `packets/R2-P1_FEEBOOK_RAILS_HYGIENE_000_FREEZE_2026-09-22.md` | alias dir `packets/fee_sensitivity_000_r1p1` superseded |
| S1 | KXMLBGAME measurement panel | Scout / Collector / Deep Research · Simulator units | Conductor | **PANEL_STUB_ACCEPTED** · panel_version `2026-09-22.s1-kxmlbgame-v0` · schema `s1_kxmlbgame_panel` · capture **idle** · Simulator GO for units · measurement only · separate from R2-P1 · no PIT@CLE budget steal · no PnL · no orders | `packets/S1_KXMLBGAME_PANEL_STUB_2026-09-22.json` · schema `registry/schemas/s1_kxmlbgame_panel.schema.json` · freeze `packets/S1_KXMLBGAME_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md` |
| C1-KXUFCFIGHT | KXUFCFIGHT cash-cow measurement panel | Collector (+ Clock join) | Conductor / Archivist | **ADMITTED** · panel_version `2026-09-22.c1-kxufcfight-v0` · admitted_at `2026-09-23T00:49:43Z` · sha256 `24426d804c51bde23cf2557a11a8481a12026da10024094c4ae546d1f7d3956e` · GET-only · results/pnl null · no recorder steal from ADMIT-1 · C3/C5/R3-P3 remain stubs · cemetery untouched | `packets/C1_KXUFCFIGHT_PANEL_ADMITTED_2026-09-22.json` · capture `lab/astra-capture/c1-kxufcfight/` · status `reports/STATUS_C1_KXUFCFIGHT_ADMIT_2026-09-22.md` · freeze `packets/C1_KXUFCFIGHT_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md` |
| C3-KXHIGHNY | KXHIGHNY panel | Collector | Conductor | **STUB** · panel_version `2026-09-22.c3-kxhighny-v0` · not admitted · adversary refuse bound | `packets/C3_KXHIGHNY_PANEL_STUB_2026-09-22.json` |
| C5-KXBTC15M | KXBTC15M panel | Collector | Conductor | **STUB** · panel_version `2026-09-22.c5-kxbtc15m-v0` · not admitted · adversary refuse bound | `packets/C5_KXBTC15M_PANEL_STUB_2026-09-22.json` |

## Merged / on main (desk)

| ID | Packet | Owner | Merged | Freeze / score pointer |
|---|---|---|---|---|
| C1 | Prospective GET-only NFL recorder | Collector Ops | **2026-09-22 17:19 ET** · [PR1](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/1) · merge `cb6223989afaf9e2f2fde8516e5ce16098ef7160` | **MERGED** · `nfl_prospective_recorder_20260922/` · ADMIT-1 LIVE |
| Q7 | Paircheck lab 2×2 (arms A–D) | Simulator · Examiner (Kalshi) scored | **2026-09-22 17:23 ET** · [PR2](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/2) · merge `a85bfdab0cd7e3b4fcb3d4a5c89cf8627be85bd2` | **MERGED** · path `nfl_paircheck_lab_20260922/` · **SCORED_KILL_B_KEEP_000** · KILL Arm B candidacy · KEEP shadow `000` · `NO_NEW_SELECTION` · no live promotion · scorecard `packets/Q7_EXAMINER_SCORECARD_2026-09-22.md` · report `reports/RPT-Q7.md` **SCORED** · packet **CLOSED** · cemetery `cemetery/CEM-ASTRA-20260922-001_Q7_ARM_B.md` |
| R1-P1 | FEEBOOK lab (fee + reciprocal book) | Simulator / R&D Variants | **PR3 MERGED** (Conductor) · lab `kalshi_feebook_lab_20260922/` | **SOURCE frozen** · unit results on disk · extract `packets/R1-P1-FEEBOOK_EXTRACT_2026-09-22.md` · not a strategy score |
| R1-P5 | RAILS lab (queue/fill instrument) | Simulator (+ Collector freshness) | **PR4 squash** · Conductor pin `6a28e0d6` · lab `kalshi_rails_lab_20260922/` | **SOURCE_FROZEN_BEFORE_RESULTS** · `results/pnl` null · unit page `results/RAILS_UNIT_RESULTS.md` (**44 PASS**) · extract `packets/R1-P5-RAILS_EXTRACT_2026-09-22.md` · does not mutate Q1–Q7 · not a strategy score |
| PR5 / capital-structure | Capital-structure lab (measurement rails) | Simulator / R&D Variants | **squash-merged** Conductor pin `ce4671b8` · lab `kalshi_capital_structure_lab_20260922/` | **SOURCE_FROZEN_BEFORE_RESULTS** · `results`/`pnl` null · not a scored challenger · pin Q6-`000` · cites R1-P1@`22371178` + R1-P5@`6a28e0d6` · freeze `packets/CAPITAL_STRUCTURE_PROBE_FREEZE_KERNEL_2026-09-22.md` |
| PR6 / R2-P1 hygiene | Fee/rails hygiene lab on Q6-000 | Simulator / R&D Variants | **squash-merged** Conductor pin `25ec0538` · lab `kalshi_r2p1_hygiene_000_lab_20260922/` | **SOURCE_FROZEN_BEFORE_RESULTS** · scorecard/pnl null · measurement only · `fee_sensitivity_000_r1p1` SUPERSEDED→R2-P1 · pins R1-P1@`22371178` + R1-P5@`6a28e0d6` · freeze `packets/R2-P1_FEEBOOK_RAILS_HYGIENE_000_FREEZE_2026-09-22.md` |
| PR7 / queue-fragility | Queue-fragility twin on Q6-000 | Simulator / R&D Variants | **squash-merged** Conductor pin `c33af159` · lab `kalshi_queue_fragility_000_lab_20260922/` | **SOURCE_FROZEN_BEFORE_RESULTS** · outputs/pnl null · measurement only · pins R1-P1@`22371178` + R1-P5@`6a28e0d6` · R2-P1 pin updated to allow sibling · freeze `packets/QUEUE_FRAGILITY_000_R1P5_FREEZE_2026-09-22.md` |
| PR8 / R2-P1 fixture-join | R2-P1 fixture-join harness on Q6-000 | Simulator / R&D Variants | **squash-merged** Conductor pin `80050e9b` · Kalshi R2-P1 fixture-join lab | **SOURCE_FROZEN_BEFORE_RESULTS** · results/pnl null · measurement harness · Pick B QF join deferred to Variants · freeze `packets/R2-P1_FIXTURE_JOIN_000_FREEZE_2026-09-22.md` |

## R1 child packets (from triage)

| ID | Decision | Packet | Owner | Notes |
|---|---|---|---|---|
| R1-P1 | **MERGED** (lab) | R1-P1-FEEBOOK | Simulator; Examiner (Kalshi) reviews tests | Fee + reciprocal-book unit truth · see Merged row |
| R1-P5 | **MERGED** (lab) | R1-P5-RAILS | Simulator (+ Collector freshness hooks) | Instrument not strategy · 44 unit PASS · pnl null |
| R1-P3 | **CLOSED** | R1-P3-ADVERSE | Adversary · reviewer Conductor accepted | Measurement gate filed, no code |
| R1-P2 | QUEUE | R1-P2-CHALLENGER (reserved, not open) | — | After fee truth + Q7 score (done) or explicit Conductor kick |
| R1-P4 | DEFER | — | Scout+Collector access check first | RFQ combos |

## Scout brief + Conductor triage (2026-09-22)

**Artifact:** `lab/governance/astra/SCOUT_BRIEF_2026-09-22.md`

| Kernel / line | Conductor triage | Notes |
|---|---|---|
| Spreads | **TRY after C1** | C1 MERGED; ADMIT-1 LIVE |
| PASSYDS | **TRY** | NFL pass-yards props kernel |
| MLB | **TRY** | Non-NFL daily cadence candidate |
| CFB | **DEFER** | College football |
| MVE | **SKIP** | Cross-category parlays / MVE inventory |

**Calendar:** PIT@CLE T−7d (Kalshi occurrence SoT) **2026-09-25T03:15:00Z** = **2026-09-24 23:15 ET** · venue `KXNFLGAME-26OCT01PITCLE` live · holdout identity **JOINED** `KXNFLGAME-26OCT01PITCLE` (PITCLE-ID-LAG).

## Sibling deathmatch review (indexed)

**Artifact:** `lab/governance/astra/packets/SIBLING_DEATHMATCH_REVIEW_2026-09-22.md`  
**Board fact:** Factorial kit **not** found in sibling repos; siblings are not a kit substitute. Measurement kernels (fee/book + queue rails) pulled into R1-P1/P5. No scoring from sibling ROI claims.

## Incumbent freeze on main

| Line | Artifact | Status |
|---|---|---|
| Q6 | `SHADOW_CANDIDATE_FREEZE` selected `000` | **KEEP** · remains incumbent shadow freeze · no live · reinforced by Q7 Examiner score |

## Closed desk packets

| ID | Packet | Owner | Reviewer | Closed | Artifacts |
|---|---|---|---|---|---|
| R1-P3 | R1-P3-ADVERSE | Adversary | Conductor | 2026-09-22 | briefs + risk register · measurement gate only |
| Q7-B | Arm B new-shadow candidacy | Examiner (Kalshi) | — | 2026-09-22 | **KILL** · scorecard + `CEM-ASTRA-20260922-001` |

## Active line freezes / scores

| Line | Where | Status |
|---|---|---|
| Q6 incumbent | `main` · selected `000` | **FROZEN / KEEP** (Examiner) |
| C1 recorder | `main` · `nfl_prospective_recorder_20260922/` | **MERGED** · ADMIT-1 LIVE |
| Q7 paircheck | `main` · merge `a85bfdab0cd7e3b4fcb3d4a5c89cf8627be85bd2` · `nfl_paircheck_lab_20260922/` | **SCORED_KILL_B_KEEP_000** · packet closed for measurement · no live promotion · no ITERATE without new freeze |
| R1-P1 feebook | `kalshi_feebook_lab_20260922/` | SOURCE frozen · unit results · not strategy |
| R1-P5 rails | `kalshi_rails_lab_20260922/` | SOURCE_FROZEN_BEFORE_RESULTS · 44 unit PASS · pnl null |
| PR5 capital-structure | `kalshi_capital_structure_lab_20260922/` · pin `ce4671b8` | SOURCE_FROZEN_BEFORE_RESULTS · pnl null · not strategy |
| C1-KXUFCFIGHT panel | `2026-09-22.c1-kxufcfight-v0` · sha256 `24426d804c51…` | **ADMITTED** `2026-09-23T00:49:43Z` · pnl null · cemetery untouched |
| PR6 R2-P1 hygiene | `kalshi_r2p1_hygiene_000_lab_20260922/` · `25ec0538` | SOURCE_FROZEN_BEFORE_RESULTS · scorecard null |
| PR7 queue-fragility | `kalshi_queue_fragility_000_lab_20260922/` · `c33af159` | SOURCE_FROZEN_BEFORE_RESULTS · pnl null |
| PR8 R2-P1 fixture-join | pin `80050e9b` | SOURCE_FROZEN_BEFORE_RESULTS · pnl null |

## Cemetery (Astra Kalshi)

| CEM_ID | Subject | Decision | Packet |
|---|---|---|---|
| CEM-ASTRA-20260922-001 | Q7 Arm B candidacy | **KILL** (displace bar fail; **not** proof pair-check effect is zero; 95%-of-D bar STANDS) | `lab/governance/astra/cemetery/CEM-ASTRA-20260922-001_Q7_ARM_B.md` · hygiene `packets/Q6_000_COMPLACENCY_SPOTCHECK_2026-09-22.md` |

Gauntlet-era CEM entries remain under `/workspace/lab/archive/cemetery/`.

## Admission calendar (clock facts — do not backdate)

| Game | T−7d | Note |
|---|---|---|
| PHI@CHI | full window missed | **Not backfilled** |
| PIT@CLE | **2026-09-25T03:15:00Z** (**2026-09-24 23:15 ET**) | ADMIT-1 LIVE · Kalshi occurrence SoT · **identity JOINED** `KXNFLGAME-26OCT01PITCLE` (Collector 2026-09-23); holdout-derived deadline 20:15 ET still −3h vs SoT (R2-P5) |
| Cohort | admitted_at `2026-09-22T21:18:13Z` | 16 events · panel `2026-09-22.1-kalshi-occurrence-sot` |

## Archivist standing gates

1. Refuse to index result files for any experiment ID lacking a prior freeze.  
2. Q7 outcomes only via Examiner packet after freeze + run artifacts — **filed** (`Q7_EXAMINER_SCORECARD_2026-09-22.md`). Registry does not invent PnL.  
3. On PR merge: file freeze pointer (path, head SHA, status) here.  
4. Missed T−7d → incomplete; never backdate admission.  
5. IDs assigned only here; Conductor closes or reassigns packets.  
6. Live promotion requires explicit Examiner + Conductor stamps — Q7 denies live.


---

## STEP0 record repair — appended 2026-09-24 (ET) by The Archivist

Append-only. No row above this line was deleted, and no result above was rewritten. Class labels for **every** line (existing and new) are in `registry/STUDY_CLASS_LABELS_2026-09-24.md`. The **Class** column below applies that vocabulary to the new rows: unit-only / synthetic / historical replay / prospective shadow / live, per PDF p16.

| ID | Packet | Owner | Status / pointer |
|---|---|---|---|
| STEP0 | Conductor step-0 record repair (pins · class labels · fee manifest) | The Archivist | **FILED** · `packets/ARCHIVIST_STEP0_RECORD_REPAIR_2026-09-24.md` · pins `registry/STEP0_HEAD_PINS_2026-09-24.json` · classes `registry/STUDY_CLASS_LABELS_2026-09-24.md` · fee `registry/FEE_ACCOUNT_MANIFEST_v0_DRAFT_2026-09-24.{json,md}` (**DRAFT_NOT_ADOPTED**) · status `registry/STATUS_2026-09-24.md` |
| STEP0-REPIN-REFINER-LEDGER | Refiner box sha re-pin (ledger amended) | The Archivist | **AMENDED A1** · `packets/refiner/REFINER_BOX_PACKET_SHA256_2026-09-23.md` · ledger `07e5fcdb…` SUPERSEDED → `9f436dafb6e7bb579b0148ed25401502812b7d1fc373c21bb66b367198ae75cf` |

### Merged / closed PRs not previously on this board (GitHub-verified; merge SHA on main)

| PR | Title (GitHub) | State / merged (ET) | Merge sha | Freeze / pointer | Class | Results/PnL as recorded |
|---|---|---|---|---|---|---|
| [PR9](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/9) | Move R2-P1 Q6-000 fixture join into the hygiene lab (pick A) | MERGED 2026-09-22 19:45 ET | `79800a82b8ad2c1e10f614f69fd7105d11e0d041` | e9bac91ca908b2ba704d966f0cf48cb181070ac11de1d117b93512bd2719ae1c | unit-only | null |
| [PR10](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/10) | QF fixture-join pick B on Q6-000 (freeze d95adb9b) | MERGED 2026-09-22 19:55 ET | `7026be5104cd00cabcf9b34154506a76b2768b8a` | d95adb9b7e8aba852134c96b8f0f7d35a76bbf68254b8808f82f99ec82bb6ca4 | unit-only | null |
| [PR11](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/11) | Examiner fee+queue honesty orchestrator on Q6-000 | MERGED 2026-09-22 20:10 ET | `aa0a373671edf6630d188d335d890573a285e0da` | 4799642e54cf233a925697e00c5a9e29f5cb39070962a2e011f0fbe090c169f2 | unit-only | null |
| [PR12](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/12) | R3-P1 fee_cost versus the R1-P1 fee model | MERGED 2026-09-22 20:14 ET | `5f45bf3741de1fc9e96f5304f05ce9f2ddbe91e4` | kernel c4e0a4448b783765154c061e945023163f0a6d59f0cc960640195515c83e944b | unit-only | null |
| [PR13](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/13) | Add Kalshi L2 shape lab for Dubach SF1 and SF2 | MERGED 2026-09-22 20:18 ET | `5eeeaa6bf26d226399448be997748d61faeba43d` | kernel 4a4e7cc61efcb436955c566edc7a2681603a014725bc79047f9d825392064528 | unit-only | null |
| [PR14](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/14) | Prefer pinned q3300 gzip fills in the Examiner honesty join | MERGED 2026-09-22 20:41 ET | `d8957a0061ba601a11b3b03145b1516937239988` | 4799642e… | unit-only | null |
| [PR15](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/15) | R3-P3 maker-taker unit scaffold with a null scorecard | CLOSED_NOT_MERGED | — | — | unit-only | null |
| [PR16](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/16) | C3-KXHIGHNY bordering-strike scaffold with a null scorecard | CLOSED_NOT_MERGED | — | — | unit-only | null |
| [PR17](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/17) | C1 KXUFCFIGHT fee and queue measurement scaffold | CLOSED_NOT_MERGED | — | — | unit-only | null |
| [PR18](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/18) | C1 KXUFCFIGHT fee+queue honesty bakeoff harness | MERGED 2026-09-23 09:15 ET | `254f10548feb293543e61e1a136eff9f78952849` | kernel a191c9b3… | unit-only | null |
| [PR19](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/19) | Pin C1 KXUFCFIGHT orderbooks with a GET-only collector | MERGED 2026-09-23 09:34 ET | `ea4909db79e39b4890447742de287ddf05ea379d` | kernel a191c9b3… | unit-only | null |
| [PR20](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/20) | Cap-SR soft-blended reserves measurement lab (scorecard null) | MERGED 2026-09-23 09:50 ET | `45863037a30af6caf9c00361e46fe8bd5444c426` | 1f263dec7d7810515c3e32c13f3c5eca4344c4951db762a88ea01a8dfde7b1b3 | unit-only | null |
| [PR21](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/21) | C5 KXBTC15M fee+queue honesty harness (scorecard null) | MERGED 2026-09-23 10:04 ET | `ee69245a5dba058ee1198c88bb4685893508f273` | 23b908af6e9a7799c9bbdac04b27e683dfccd0c0c25d691df84ff715202d3cab | unit-only | null |
| [PR22](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/22) | C3 KXHIGHNY bordering-strike harness (scorecard null) | MERGED 2026-09-23 10:15 ET | `637644966bae3737b52ab35826d3a63bf4b9b936` | 27530d6427794a5559e40c7f56d6cd938d8c57cc8f51406fc26a5b0e36a5fdff | unit-only | null |
| [PR23](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/23) | R3-P3 FL maker/taker bands harness (scorecard null) | MERGED 2026-09-23 10:36 ET | `cfd5f95a6b2c9bd654ae58bd278f8465b827712b` | fbc58539b7a469d005b7f75b786efddecc1028a3bb0da601bc0082c9d4aab179 | unit-only | null |
| [PR24](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/24) | Cap-SR-FX effects path on Q6-000 (scorecard null) | MERGED 2026-09-23 10:51 ET | `79347f0ed8562f7df8d539e79a1cb15985d8abfe` | cd08a93af2659c36f83cd1b9ffc3174364cc767efc374a4e0669e128f6a29074 | unit-only | null |
| [PR25](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/25) | S5 KXMVECROSSCATEGORY fill-vs-legs harness (scorecard null) | MERGED 2026-09-23 11:26 ET | `6626c6892298b015cf63688081545e27363226bc` | 8a118e6f1fdc8c22c6e559f395667aedffa5d270d067e39b6ae3ee24b2046d16 · parent a28932ba13b4913b69c48b73dde8ba066cebd212670d0b1cbb5ea8e93734b8ba | unit-only | null |
| [PR26](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/26) | S4 KXNCAAFGAME fee+queue honesty harness (scorecard null) | MERGED 2026-09-23 12:01 ET | `d7584dd48a67d38d81f5141654b6f498915a70a5` | 3318204bf6e962f4f3372dad8c0f302e62d85c26b855de7369718654d0114728 · panel stub 38167d11da5842bc4d39e6e7dcaab20a67294c735ba14d8bbeafde3154c6342a | unit-only | null |
| [PR27](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/27) | R2-P3 KXNFLPASSYDS prop-ladder harness (scorecard null) | MERGED 2026-09-23 12:19 ET | `3b0d1429b9ea702f2cb242e79f21f5ab5d3f18a6` | f8335eb0080cb1f82b1fad512509749134dd0e6e41ed85795347c3476796e87a · parent a30108f6… · panel 70e879e8738d033f392d821849dee3537af3e7b8a916670779d238f78ce098be | unit-only | null |
| [PR28](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/28) | R3-P4 L2-CAT sports-vs-nonsports harness (scorecard null) | MERGED 2026-09-23 12:38 ET | `e54554ff79b663b30836cd34f8d20004a9022a0a` | 3fc370d93f0ea42864f7bf482d7f6515254999c76e2fc4477df1273bfcdc051f · parent 4a4e7cc6… · panel 7477e023ab70c59a6739650155ddb9d77077766e3afd80443e540d60b5a86cbb | unit-only | null |
| [PR29](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/29) | R2-P5 SOT-ID kickoff SoT identity harness (scorecard null) | MERGED 2026-09-23 12:54 ET | `6f1e22e15d8841605be5c34711f202277f4b685d` | 0424455f062b7c46c7c6161b84fb7b29702719acc45bf6a61b4e8f16c5e26457 | unit-only | null |
| [PR30](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/30) | C1 EMPTY-OB harness (scorecard null) | MERGED 2026-09-23 13:13 ET | `d7b935951c9ddd5e6c4d813fad69e401b6a7b6a3` | 1b9f8fbec8bad866e055bcabd38c8c633835d505cbd25c367ff0675bff3a4b27 | unit-only | null |
| [PR31](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/31) | R3-P4 L2-SF harness (scorecard null) | MERGED 2026-09-23 13:33 ET | `ead2cb41d5d171d8972a27b98d144849b6f8c371` | f00425261f085aef90e93b186810a0248165273f8bb923ef3597940a9e8345de | unit-only | null |
| [PR32](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/32) | C2 KXNHLGAME fee+queue honesty harness (NHL-FQ, scorecard null) | MERGED 2026-09-23 13:52 ET | `677d5d4f0d5ed1235b4827bf89dd98d82bc34356` | a36ec35143a32c7cd24e9fdf2a33f645d356b93e34c131bb1b8a94e3f92e38f5 | unit-only | null |
| [PR33](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/33) | C4 KXCPI fee+queue honesty harness (CPI-FQ, scorecard null) | MERGED 2026-09-23 14:10 ET | `6e55a99790f4cc09a437d2e16ccf4e8e826a154b` | 949b255859196f02d73303a1019e51276c583f8d1e3ffb4f0a64d330467c6f93 | unit-only | null |
| [PR34](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/34) | ATP KXATPMATCH fee+queue honesty harness (ATP-FQ, scorecard null) | MERGED 2026-09-23 14:26 ET | `438f4abf28a3c0156daf6c96ece5efda9557f1dc` | 4d4ce944946e72dd40567d14388fe11c6145fbbb32505a880bcf80a4c8b4dffe | unit-only | null |
| [PR35](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/35) | [superseded by #34] ATP KXATPMATCH fee+queue honesty harness (ATP-FQ) | CLOSED_NOT_MERGED | — | — | unit-only | null |
| [PR36](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/36) | ETH-FQ KXETH15M fee+queue honesty harness (scorecard null) | MERGED 2026-09-23 14:57 ET | `82bf7bb99bcc618b912255cc24022b23f9f15047` | 9cae3bad089e6e18bee22694a36a1a2c18db33935a315766cd6bd8f8476aa83a | unit-only | null |
| [PR37](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/37) | R3-P2 queue_position calibration ingest (metrics null) | MERGED 2026-09-23 15:21 ET | `9eba15870e66dcde8ffc17a56c73016245a833c1` | kernel d2e8b21d0c9ff818aea5ab462a6c91c8a7bccc11ab6ae7538169041ed905c8c3 | prospective shadow | metrics per EXAMINER_SCORECARD_R3_P2_ABS_ERR_SIGNED_BIAS_2026-09-23.md |
| [PR38](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/38) | Q7 Arm B rehab pass 1: 600s admission cadence (freeze, scorecard null) | MERGED 2026-09-23 15:13 ET | `9b8fb184a8f1d556e400188127f1753bf35e571e` | Refiner P1 freeze 91506143c2f75e27dd8a2593e9b484457b61e5b1a8537002bf2b4f4be435ec97 · lab FROZEN_EXPERIMENT 3183754c6880b20ad16b51b4595549409a24508ece6e3b21d507d51142ce3174 | historical replay | per EXAMINER_SCORECARD_Q7_B_REHAB_P1_TAPE_WALK_KILL_2026-09-23.md |
| [PR39](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/39) | C1 KXUFCFIGHT admit-wire fixture join (scorecard null) | MERGED 2026-09-23 15:05 ET | `3972fe4edfd53740219a4d051392f1291cef5f98` | panel 24426d80… (admit pin) | unit-only | null |
| [PR40](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/40) | C3-RJ KXHIGHNY settled-resolution join harness (scorecard null) | MERGED 2026-09-23 15:14 ET | `9fd5d7cb89693a0ed29d9e97d2b723c0810989bc` | 56adcf592239b028aaa8bcffbf09815115b8454f78db39b43c578e64c160a4d5 | unit-only | null |
| [PR41](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/41) | C5-RJ KXBTC15M settled-resolution join harness (NOT_SCORED) | MERGED 2026-09-23 15:33 ET | `8cfcd17a62d3793dee554a4da422e8075bde9cf6` | 7f4b36eca39d43ee7403628c2e525d5980fa40bcfc906550c7f00bb06ffd4f21 | unit-only | null |
| [PR42](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/42) | R3P3-RJ FL maker/taker settled-resolution join harness (NOT_SCORED) | MERGED 2026-09-23 15:56 ET | `2fce8642d1b1961cbe0ef60fae1411cd8906f31a` | 7fcfc36ab4761e2dec56018b498372fb63c402f2582fe848e8775e28f9b720b9 | unit-only | null |
| [PR43](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/43) | NHL-RJ KXNHLGAME settled-resolution join harness (NOT_SCORED) | CLOSED_NOT_MERGED | — | — | unit-only | null |
| [PR44](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/44) | NHL-RJ KXNHLGAME settled-resolution join harness (NOT_SCORED) | MERGED 2026-09-23 16:33 ET | `b450e780fd9752887579ee8d217b6dee76d918f8` | d1f71cea6df8f6c5a9fac6f9d1aa418ce61aa650794f22b400a01c4f3fd45810 | unit-only | null |
| [PR45](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/45) | S4-RJ KXNCAAFGAME settled-resolution join harness (NOT_SCORED) | MERGED 2026-09-23 16:56 ET | `aeff380b29dbe89b16da58f9e15e58415b42b147` | 3a8e8ba52edd6acdc342c6a2faabb08665fe8a7a76e1b28af1c8e18850b03d99 | unit-only | null |
| [PR46](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/46) | R2P3-RJ KXNFLPASSYDS settled-resolution join harness (NOT_SCORED) | MERGED 2026-09-23 17:26 ET | `b2c1639a77f62114572fd41182f8a3c5ef70cad1` | 9ad3b0112243c1020aec2bd6ef0df15011b065c30aa691a988da02eb08be1e0b | unit-only | null |
| [PR47](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/47) | Q7 Arm B pass-2 freeze: portfolio_rank sizing (units only) | MERGED 2026-09-23 17:50 ET | `a281adc944e4dacffcdb5677a140fabaed675a81` | Refiner P2 freeze 5f70d83abe5f45f01a29f5bf4bf10484f934715990aed4759630ee6f90392bfd · lab FROZEN_EXPERIMENT e3e4814abcbb92b5142c1e4783fed53b50372783aeb58f664361966d719bd7d7 | unit-only | results/pnl null; score_outcome null |
| [PR48](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/48) | S5-RJ KXMVECROSSCATEGORY settled-resolution join harness (NOT_SCORED) | MERGED 2026-09-23 17:49 ET | `fec05e8cf7c11f1c975ab791fda64f896d40d1cd` | cd264a4d41ef055d1cbca80a5dbe6756746211537fb24799dca9dde8980cb799 | unit-only | null |
| [PR49](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/49) | C1-RJ KXUFCFIGHT settled-join harness (authentic pins, scorecard null) | MERGED 2026-09-24 19:20 ET | `34a2720218b4f4f2d6dd0cbde6334ee672a3684b` | 3ea3362ad3c16951369d5f90497ec6079213dd54e5556340c4d3738744126cf1 | unit-only | results/pnl/settled_join_n null |
| — (no PR) | C4-RJ KXCPI settled-resolution join harness | CONDUCTOR_ACCEPT, no PR | — | `5e37f81a8959e83c3d2c0c42739e1ca6c127c748442ac6fe28c0013edee12e2f` · `astra-science/kalshi_c4_kxcpi_settled_join_lab_20260924/` | unit-only | null |

Notes: PR38 and PR47 are Q7 Arm B rehab passes. P1 = Examiner **KILL** (historical replay, results box-only). P2 = units only, tape walk in flight, results null. The R3-P2 row (PR37) carries the flag **DEMO_VENUE_ORDERS** (demo host, fill_count 0) for a Conductor ruling. Missing CONDUCTOR_MERGE stamps: PR1–29 and PR38. Main head now `34a2720218b4f4f2d6dd0cbde6334ee672a3684b` (PR49).


### Research-branch lines cited by the Kalshi Edge Research report (not Archivist-frozen; negatives indexed, positives not)

| Line | Pin | Class | Note |
|---|---|---|---|
| q7-paired-price | `01c726ae9244d801d359e00df67d6a71f4012669` (still head) | historical replay | **CONFLICT-Q7-ARMS** with Q7 row above; both kept |
| q8-joint-routing | `d7079b6fece902e6e4603114a1d9ed5ef5a246c5` (still head) | historical replay | head msg = M2 cohort freeze |
| m2-continuation (M2/M3; M4 freeze) | `f44574e8f318920cc8fdf87c9c3d35c18bca2107` (still head) | historical replay (M4: unit-only) | |
| all-market-structure | report pin `a59c9e331dcfcd71c957e753bc4fd2460df403c0` **not head**; head `cba057e62b3162bbf5cab17f4e2fee532a209ddc` (+25) | historical replay (AMS-007/010: prospective shadow [I]) | AMS-002/003/008 pinned as git objects in CEM-ASTRA-20260924-002/004 |
| neglected-hybrid NH-001A | `2253c03cd86eb5515325f1d91b43bdcbea7a902c` | historical replay [I] | negative (commit msg); not previously on board |

### Cemetery (Astra Kalshi): appended 2026-09-24. CEM-ASTRA-20260922-001 above is unchanged and visible.

| CEM_ID | Subject | Decision | Packet |
|---|---|---|---|
| CEM-ASTRA-20260924-001 | Card 09 crypto settlement-window pricing (F2 lineage: FEAT-20260912-005 / TEST-20260913-001) | **CEMETERY_UP_FRONT**. TEST-20260913-001 BTC k=30 `INCREMENTAL_RESEARCH` kept visible, flagged **LOOKAHEAD-CONTAMINATED** (T−1m mid comparator) | `cemetery/CEM-ASTRA-20260924-001_CARD09_CRYPTO_SETTLEMENT_WINDOW.md` |
| CEM-ASTRA-20260924-002 | Card 10 core static threshold-basket taker (AMS-002 0/180; AMS-008 none survived M=1 fees) | **CEMETERY_UP_FRONT (core)** | `cemetery/CEM-ASTRA-20260924-002_CARD10_STATIC_THRESHOLD_BASKET_TAKER.md` |
| CEM-ASTRA-20260924-003 | Card 06 CPI post-release sub-family (KXCPI closes 8:25 ET; BLS CPI 08:30 AM ET) | **CEMETERY_UP_FRONT (sub-family)** | `cemetery/CEM-ASTRA-20260924-003_CARD06_CPI_POST_RELEASE.md` |
| CEM-ASTRA-20260924-004 | Card 03 subsidy-only zero-edge taker variant | **CEMETERY_UP_FRONT (variant)**; card-03 resting lane open | `cemetery/CEM-ASTRA-20260924-004_CARD03_SUBSIDY_ONLY_ZERO_EDGE_TAKER.md` |

Source for all four: `packets/ADVERSARY_DEAD_CARD_OVERLAP_EDGE_RESEARCH_2026-09-24.md` (sha256 `b434220493c8dfae34c123786153ad038ae3cb2832272254a2e97673f7e87fdd`). Frozen negatives stay visible. No resurrection without a new freeze.


**Seat note:** The Steward (new seat) owns repo hygiene only. The registry remains the source of truth for pins, manifests and the cemetery.


### Conductor follow-up rulings + results manifest + merge-stamp backfill — appended 2026-09-24T19:51:03-04:00 (ET)

Rulings record: `packets/ARCHIVIST_CONDUCTOR_RULINGS_RECORD_2026-09-24.md`. Rows above are not rewritten.

| Item | Ruling / record | Status |
|---|---|---|
| R3-P2 (PR37) class | **prospective shadow** + sub-tag **DEMO_VENUE_ORDERS**. Demo orders are never `live`; demo fills/queue behaviour never count as observed live execution (demo matching is not the production book). | RULED. Examiner KEEP (abs_err/signed_bias honesty) unchanged. live = 0. |
| Card-09 / CEM-ASTRA-20260924-001 | `LOOKAHEAD-CONTAMINATED` extended to TEST-20260913-001 annex rows BTC k=50 and ETH k=50 (lines 62–63). Kept visible, numbers unchanged. | RULED. Ruling section appended to the CEM file. |
| Q7 registry Arm B KILL vs q7-paired-price `router_on` | Both **CONFLICT_UNRESOLVED** pending the Simulator reconciliation memo. Registry Arm B KILL = Refiner P1 result on main's Arm B definition (Conductor wording). `router_on` = different policy until arm mapping proven. | OPEN. Neither result changed. Memo on disk 19:46 ET (`packets/q7_reconciliation_20260924/`, `RECONCILIATION_MEMO_READY_NOT_SCORED`), not yet ruled on. |
| Results-only PR manifest | `registry/RESULTS_LANDING_MANIFEST_2026-09-24.{json,md}` + `RESULTS_LANDING_SHA256SUMS_2026-09-24.txt`. 171 entries; 159 proposed for landing (Q7 79 · Q7-B P1 67 · R3-P2 13); 12 held/excluded. `sha256sum -c` verified against box bytes (all OK). | MANIFEST ONLY. Archivist does not open the PR. **5 files > 100 MiB** (LFS or archive-by-checksum). **Q7 scored verification.json (sha256 eb1586bf…) missing from box.** |
| Merge stamps PR1–29 + PR38 | `packets/merge_stamps_reconstructed/CONDUCTOR_MERGE_PR<N>_RECONSTRUCTED_FROM_API.json` ×30 + index. `provenance: RECONSTRUCTED_FROM_API`, `contemporaneous: false`. | 27 merged (PR1–14, 18–29, 38) · 3 closed-unmerged (PR15, 16, 17; drafts) · 0 not found. All merged by 17thgreen. |
| Fee manifest | Stays **DRAFT_NOT_ADOPTED**. Until member type resolved (Market Scout checking), Examiner reports net P&L under BOTH precisions ($0.0001 / $0.01) as a sensitivity. Simulator cost-convention stress on Q6-`000` KEEP (stress, not retune). | Note appended to MD; sidecar `_ADDENDUM_01.json`. |
| Correction | Main `nfl_paircheck_lab_20260922/results/` holds NOT_RUN.json + analysis_status.json + verification.json (all not-run stubs, byte-identical to box), not "NOT_RUN.json only". | Correction appended to STUDY_CLASS_LABELS and STATUS. |
| Main head | now `37ad5b7b366c10dcdf278c2325611e6f426a62c6` (PR52, 19:46 ET). PR50 `959c3f2b` (C4-RJ, 19:43 ET) is the previously "no PR" C4-RJ row. | Pin file `STEP0_HEAD_PINS_2026-09-24.json` is a snapshot at PR49; not rewritten. |

New files (sha256 at write):

| File | sha256 |
|---|---|
| `packets/ARCHIVIST_CONDUCTOR_RULINGS_RECORD_2026-09-24.md` | `69c51e755d9a0947a72bf677b9975a1639c846680a3ea88adb5d6c0f838af540` |
| `registry/RESULTS_LANDING_MANIFEST_2026-09-24.json` | `fcbbdddfcecf3248648a4f941f0e252cd20bf0db673cf91b0b2cc2f8212137cf` |
| `registry/RESULTS_LANDING_MANIFEST_2026-09-24.md` | `073ac09fe72559f49def6831b4ae952988f9d3762d7b7380ace4e712df515377` |
| `registry/RESULTS_LANDING_SHA256SUMS_2026-09-24.txt` | `ab17ad934d5902002a7c62facffddc370a544ac50f50ccab4e2dd0f0ff72fd19` |
| `packets/merge_stamps_reconstructed/INDEX_RECONSTRUCTED_MERGE_STAMPS_2026-09-24.md` | `85d45841ea7c0c5e7aa3f76e7c10c8215efb8eeea45c2804ac420acfaa08ec44` |
| `registry/FEE_ACCOUNT_MANIFEST_v0_DRAFT_2026-09-24_ADDENDUM_01.json` | `a9f9c367c785ddd632b983a0a0c700d8cd9ae7593a59712e1d1efe1cd46b8f26` |


### Holdout re-pin · R3-P2 warm shelf · Tier B cold evidence · Q7 LABEL_COLLISION · head pins R2 — appended 2026-09-24T19:55:12-04:00 (ET)

| Item | Record | Status |
|---|---|---|
| RESERVED_HOLDOUT re-pin | `packets/RESERVED_HOLDOUT_REPIN_2026-09-24.md`. ORIGINAL `74507e1a…` stays in the freezes; CURRENT `f8f6b577…` | **VERIFIED**: diff = PIT@CLE ticker + trailing newline (byte-exact). Freezes not edited. |
| R3-P2 (PR37) | Examiner `EXAMINER_SCORE_R3_P2_TRADE_STEP_RETRY_PLUMBING_2026-09-24.json` `e66d2636…` MEASUREMENT_PLUMBING_PASS; Conductor `CONDUCTOR_RULING_R3_P2_WARM_SHELF_2026-09-24.json` `7fa4455f…`; PARKED_SPEC `r3_p2_queue_position/PARKED_SPEC_R3_P2_TRADE_STEP_FILL_LABEL_v2.md` `9488a1d6…` | **WARM_SHELF**, plumbing pass; calibration NOT measured (trade-free windows); prospective shadow + DEMO_VENUE_ORDERS |
| Q7 verification pin | `eb1586bf13b1…` | **UNVERIFIED_BYTES_MISSING**; Examiner verdict stands; pin not rewritten |
| Q7 conflict | Main Arm B vs branch router_on | **LABEL_COLLISION** (effective; Examiner memo stamp `641b10d1…` READY_NOT_SCORED at 19:52 ET); headlines NON_COMPARABLE; main B/D 0.843 reproduces (desk ledgers, per Examiner ACCEPT); memo merged PR51 `eb4a4a94` |
| Landing | Tier A 139 (`89662fa6…`, Steward) · Tier B 13 checksum-only (`1c677347…`) · batch 3 +4 (`RESULTS_LANDING_TIER_A_BATCH3_SHA256SUMS_2026-09-24.txt`) · 2 duplicates dropped · 7 R3-P2 held | `RESULTS_LANDING_MANIFEST_2026-09-24_ADDENDUM_01.json`; manifest JSON not rewritten |
| Tier B cold evidence | `/workspace/lab/evidence_cold/2026-09-24/` 13 × .gz + MANIFEST.json + SHA256SUMS.txt | 13/13 round-trip OK; all < 2 GiB (total 20,946,068 B); not pushed; no LFS |
| Head pins R2 | `registry/STEP0_HEAD_PINS_2026-09-24_R2.json` | main `37ad5b7b…` (requested); observed head `eb4a4a94…` (PR51); research heads unchanged |

New files (sha256 at write):

| File | sha256 |
|---|---|
| `packets/RESERVED_HOLDOUT_REPIN_2026-09-24.md` | `f4ee77b8274bfd712fe030f4d6415df93c2b8dab61cfc6393f658cd0c828a8df` |
| `registry/STEP0_HEAD_PINS_2026-09-24_R2.json` | `d5de9223202f4f1eadd785f53d7a2f4762b6a3e10ed8d1cc9a9ed7c3c24008fe` |
| `registry/RESULTS_LANDING_TIER_A_BATCH3_SHA256SUMS_2026-09-24.txt` | `3ed6f2fa1e10821f2fb667cbbaaa3087d7727a555a5a7ba7edf0e6ba62442677` |
| `registry/RESULTS_LANDING_MANIFEST_2026-09-24_ADDENDUM_01.json` | `ef03c7dfe7172f418301898cac8a645ac46155410331b6af9a45c0aeba339298` |
| `(box) /workspace/lab/evidence_cold/2026-09-24/MANIFEST.json` | `4d3170168210f858e26e0fb036d71e6a0a614aac75af32eec6d83294370069ba` |
| `(box) /workspace/lab/evidence_cold/2026-09-24/SHA256SUMS.txt` | `99a31ba46abe4be4d8fcddac0dbf59f667b26657bff776e19c2155d3957c760d` |


---

## Round 4 — appended 2026-09-24 ~20:03 ET (Archivist). Entries above are not rewritten.

| Item | Packet / file | Status / note |
|---|---|---|
| CEM-ASTRA-20260924-005 | Card 04 perps stale-quote taker arb, retail account | **KILLED (REJECT for this account)**; prospective shadow — **FREEZE_GAP** | `cemetery/CEM-ASTRA-20260924-005_CARD04_PERPS_STALE_QUOTE_RETAIL.md` |
| Scout perps screen | `SCOUT_PERPS_STALE_QUOTE_SCREEN_2026-09-24.md` `3f893cbf…` + `packets/scout_perps_screen_2026-09-24/` (125 files; `MANIFEST.sha256` `61d02651…` OK) | all 126 pinned in `cemetery/CEM-ASTRA-20260924-005_EVIDENCE_SHA256SUMS.txt` (126/126 OK) |
| R3-P2 WARM_SHELF, errata | `packets/r3_p2_queue_position/ERRATA_R3_P2_TRADE_STEP_PROVENANCE_2026-09-24.md` `5692f1cf92f35a975b7a82de324b0c4ef975d64465c15ee3cd7e8f1631d12d0a` | correction of record; **no frozen JSON or result hash changed** (re-hash ~20:02 ET). `FROZEN_TRADE_STEP_FILL_LABEL.json` `518cd981…` (= Examiner-quoted). Mechanic MDs amended 19:58:33 ET, PRIOR_HASH_UNKNOWN: series md `f926cc5f…`, retry abs_err md `1a7b32f2…` |
| R3-P2 retry series landing | `registry/RESULTS_LANDING_TIER_A_BATCH3B_SHA256SUMS_2026-09-24.txt` `717840a0b55735ec1b5f8aa84873ac55d48e4b85d7907d76dfeb2d5d6ee813ad` | `demo_trade_step_sample_series_retry.json` `6e2c8257…` HELD → LANDING; **COLLECTED_POST_FREEZE** (not pre-declared); 6 R3-P2 files still held |
| Card 03 fee term | `packets/card03_liquidity_rewards/AMENDMENT_01_CARD03_PRE_OUTCOME_2026-09-24.md` `add1fefe…`, `AMENDMENT_01.json` `fed1d30c…` | DRAFT fee manifest `aa765876…` routed to the Mechanic; **FEE_DRAFT** under both precisions; **DRAFT_NOT_ADOPTED** |

New files (sha256 at write):

| File | sha256 |
|---|---|
| `cemetery/CEM-ASTRA-20260924-005_CARD04_PERPS_STALE_QUOTE_RETAIL.md` | `3e5319092f15a3c954fa8408caf82fc8a8bb8d2ce55275cfa8a7f1b38f72f841` |
| `cemetery/CEM-ASTRA-20260924-005_EVIDENCE_SHA256SUMS.txt` | `dcd93c52f7a40d0d87d9cd8b38f28014c4d97ccb0599f5973105e4cad7266b16` |


---

## Round 5 — appended 2026-09-24 ~20:11 ET (Archivist). Entries above are not rewritten.

| Item | Packet / file | Status / note |
|---|---|---|
| Card 01 source gate (ElectIndex) | `packets/ARCHIVIST_SOURCE_GATE_ELECTINDEX_CARD01_2026-09-24.md` + `.json` twin | **APPROVED_HASH_ONLY** (gate (a) only; (b) market-independence and (c) track record still open). The freeze is not void. Registry ruling, not legal advice. |
| Card 01 freeze (gated) | `packets/CARD01_HOUSE_ONLY_PROSPECTIVE_FREEZE_2026-09-24.md` `c31724463d81747702910a2d5296c2fc21d2a1dbc594727b26ac3d894b55ec59`; Amendment A `4e36d0db…` (source unchanged) | Provenance pin: 1 GET/day of `raw.githubusercontent.com/ElectIndex/26_us_forecast_data/main/output/races_summary.csv`. Raw bytes go only to `evidence_private/`. The first record must post-date 23:52:48Z. |
| ElectIndex probe files | `packets/card01_hybrid_forecast/source_probe_electindex/` (4 files, 19:45 ET) | **PRE_FREEZE_CAPTURE** (declared universe snapshot, not counted) + **RAW_IN_PACKET_TREE**: must not be landed or committed. Not in any landing manifest. |
| Private evidence rule | `/workspace/lab/evidence_private/` (`.gitignore` `*`, README_DO_NOT_COMMIT) | Never commit, land or push; never copy into `governance/` or the public repo |

New files (sha256 at write):

| File | sha256 |
|---|---|
| `packets/ARCHIVIST_SOURCE_GATE_ELECTINDEX_CARD01_2026-09-24.md` | `fb29ae5c94e357b0d4d6058d3c99a06697239542a61856005c058d4893a61310` |
| `packets/ARCHIVIST_SOURCE_GATE_ELECTINDEX_CARD01_2026-09-24.json` | `8882c450cd51250c705a88ec375078123e32f5b1acdfb726652daa0254fb28a7` |
| `(box) /workspace/lab/evidence_private/.gitignore` | `fc47b400337473f5c92f7fbef06c97b9940c3264c00c11842134490b36d8fe01` |
| `(box) /workspace/lab/evidence_private/README_DO_NOT_COMMIT.md` | `de5b0682121e53bfce3a69255178d760f5465587945866cdb48c9fdf0a563e32` |
| `(box) /workspace/lab/evidence_private/electindex/gate_2026-09-24/SHA256SUMS.txt` | `f84e8e7e7b2c37362b490d0d2c710ef8a5dcef1ba2206a584f1f12d09a779cfd` |

### Appended 2026-09-24 ~20:12 ET (Archivist): card 01/02 re-pins + ElectIndex probe relocation
| path | sha256 |
|---|---|
| `packets/ARCHIVIST_CARD01_02_REPIN_AND_PROBE_RELOCATION_2026-09-24.md` | `d667e753e96332d0ada5a0b2755605d076642897bf5cdd6c90ce30aeb063ad0a` |
| `packets/card01_hybrid_forecast/source_probe_electindex/RELOCATED_TO_PRIVATE_STUB.json` (PRE_FREEZE_DESIGN_INPUT stub) | `996824ae797eb44abe5cfb95acf52996a6b9fff737937ecfd975f7d33b6c70d2` |
| `(box) /workspace/lab/evidence_private/electindex/card01-nh002-house/PRE_FREEZE_2026-09-24/SHA256SUMS.txt` | `e0b86d409830dc550ae561c948cdb188d1071169c2f3edac55d79aed93b707b8` |
| `packets/CARD01_NEGLECTED_HYBRID_DECISION_PACKET_2026-09-24.md` CANONICAL (superseded `58c44c4f…`, bytes missing) | `d59c26420713ef728a306efc0bb12761584125e96ba6a87e84fe0c3e57c69688` |
| `packets/CARD02_STATION_WEATHER_NOWCAST_FREEZE_KERNEL_2026-09-24.md` CANONICAL (at-freeze `9624ab24…`, bytes missing) | `8412439f9a31211acbd66125275734afdf8e42e7a95ba7d9d5534003e587adfb` |

### Appended 2026-09-24 ~20:16 ET (Archivist): Conductor round 6
| path | sha256 |
|---|---|
| `registry/RULE_FROZEN_EDIT_PREV_BYTES_2026-09-24.md` (RULE-FROZEN-EDIT-PREV-BYTES-001, ADOPTED) | `f0aab7d15ca78a097644008db02013eae3a56cb81b2a6aef2cfe6faf21e3e6d1` |
| `packets/card01_hybrid_forecast/CARD01_HASH_ANCHOR_MANIFEST_2026-09-24.json` (hash-only, for Tier A PR) | `e1d019b5385981730eb2dd1c9b718d40a0a675af2fa0545f202c58005f1b11cd` |
| `registry/FEE_ACCOUNT_MANIFEST_v0_DRAFT_2026-09-24_ADDENDUM_02.json` (HOUSE_FEE_MISSING) | `eec516fc8ed8ea09634b24842c7ae4cf55fb8f5b40a81e50418213424139f7f9` |
| `packets/ARCHIVIST_ELECTINDEX_CAPTURE_PIN_AMENDMENT_01_2026-09-24.md` (methodology hash) | `336eca8ff4966b129642761d35a174e0c29dd29d386995feb22523ce99f326a8` |

| `packets/ARCHIVIST_ELECTINDEX_CAPTURE_PIN_AMENDMENT_02_2026-09-24.md` (text hash approved; JS blind spot) | `8615d50373ae6a0758e7b28b8445ead9bfbb7e20d90f4435734c7a8c7db0fb9a` |
| `(box) astra-capture/card01-nh002-house/electindex_capture_log.jsonl` @4 lines | `207a80885b2c4f848c494a192f8c84dfa0517101f405fc4cd07a1bab98ce4af1` |

### Appended 2026-09-24 ~20:22 ET (Archivist): normalizer freeze + ATP-RJ ACCEPT index
| path | sha256 |
|---|---|
| `packets/ARCHIVIST_ELECTINDEX_NORMALIZER_FREEZE_RECEIPT_2026-09-24.md` (e1f5a55b… bound) | `0cf92a0fd27d5f614ead92b7b8760d08131b1e2de45e3c4c142e70a3072e7891` |
| `(box) astra-capture/card01-nh002-house/methodology_text_normalize.py` NORMALIZER_FROZEN | `e1f5a55b396fc25ba3a928b2eabdc9b5d541e0604b753defbe3530da349de18f` |
| `packets/CONDUCTOR_ACCEPT_ATP_KXATPMATCH_MEASURE_HARDENING_INFRA_2026-09-24.json` (ATP-RJ ACCEPT+IMPLEMENT GO) | `8c350baaffa0fae822ba86481eed2362bebd919413c0d3f42847264244ad5411` |

### Correction 2026-09-24 ~20:23 ET (Archivist): ATP-RJ ACCEPT path name
The prior row labeled `packets/CONDUCTOR_ACCEPT_ATP_KXATPMATCH_MEASURE_HARDENING_INFRA_2026-09-24.json` is a path typo. The real path is `packets/CONDUCTOR_ACCEPT_ATP_KXATPMATCH_MEASURE_HARDENING_INFRA_2026-09-24.json`. sha256 unchanged: `8c350baaffa0fae822ba86481eed2362bebd919413c0d3f42847264244ad5411`.

### Clarification 2026-09-24 ~20:24 ET (Archivist)
- The ~20:23 "path typo" note was a false alarm: on-disk ATP-RJ ACCEPT is `packets/CONDUCTOR_ACCEPT_ATP_KXATPMATCH_MEASURE_HARDENING_INFRA_2026-09-24.json` sha256 `8c350baaffa0fae822ba86481eed2362bebd919413c0d3f42847264244ad5411`.
- Normalizer freeze receipt on disk: `packets/ARCHIVIST_ELECTINDEX_NORMALIZER_FREEZE_RECEIPT_2026-09-24.md` sha256 `0cf92a0fd27d5f614ead92b7b8760d08131b1e2de45e3c4c142e70a3072e7891` (re-verified). Bound script sha256 `e1f5a55b396fc25ba3a928b2eabdc9b5d541e0604b753defbe3530da349de18f` [V]. Collector cleared for BACKFILLED self-check.

### Appended 2026-09-24 ~20:28 ET (Archivist): lineage + Amendment B + ElectIndex Amendment 03
| path | sha256 |
|---|---|
| `packets/ARCHIVIST_CARD01_02_LINEAGE_AND_AMENDMENT_B_2026-09-24.md` | `1a39f654ee69df70bfd9e78b3494d427979349adf469eee47263e54da4a841b2` |
| `packets/CARD01_NEGLECTED_HYBRID_DECISION_PACKET_2026-09-24.md` CANONICAL (was d59c2642) | `c0c1aa66f104e3f102228a7a8e16f205977afbee63928f30a6954ec46707a82c` |
| `packets/CARD01_NEGLECTED_HYBRID_DECISION_PACKET_2026-09-24.md.pre-20260925T001140Z` SUPERSEDED v1.1 | `d59c26420713ef728a306efc0bb12761584125e96ba6a87e84fe0c3e57c69688` |
| `packets/CARD01_NEGLECTED_HYBRID_DECISION_PACKET_2026-09-24.md.reconstructed-58c44c4f` SUPERSEDED pre-v1.1 | `58c44c4fb144968ba57e4c8b4a2018026a123d17a02e2e6c09fdfd38f465a353` |
| `packets/CARD02_STATION_WEATHER_NOWCAST_FREEZE_KERNEL_2026-09-24.md` CANONICAL (was 8412439f) | `6b36dacb84f92524b18c3799c50c5818ee44fee89ac1743ceafb1092cd4c7e48` |
| `packets/CARD02_STATION_WEATHER_NOWCAST_FREEZE_KERNEL_2026-09-24.md.pre-20260925T001140Z` SUPERSEDED v1.1 | `8412439f9a31211acbd66125275734afdf8e42e7a95ba7d9d5534003e587adfb` |
| `packets/CARD02_STATION_WEATHER_NOWCAST_FREEZE_KERNEL_2026-09-24.md.reconstructed-9624ab24` at-freeze | `9624ab2498e88896c46e8fd984211b4b8839e613567209841358d7cf5059e5d6` |
| `packets/CARD01_HOUSE_ONLY_PROSPECTIVE_FREEZE_2026-09-24_AMENDMENT_B.md` | `ee6af37cef95f1e468d28e5b06750caaca8b1706ec11ed5cf5cdce460524c2c6` |
| `packets/card01_hybrid_forecast/amendment_b/NH002H_AMENDMENT_B_national_miss.py` PINNED | `049368f942741ff4a63acad328a49ff256252587d6c65f1e7e6d65d6101781f2` |
| `packets/ARCHIVIST_FORWARD_AMENDMENT_B_2026-09-24.md` | `2c6795667c48cee56717abd39f4d65171dc69466120427e1ef1bb82bce0429e6` |
| `packets/card01_hybrid_forecast/LEDGER_2026-09-24.md` | `d8ddfda72bdc6aaedd5627c78da99d6f360c48746b16c662d7ae3263a3d14fe1` |
| `packets/ARCHIVIST_ELECTINDEX_CAPTURE_PIN_AMENDMENT_03_2026-09-24.md` (eifc-info.js R0=caaff53e) | `70e5aba3f3eee9573a9adf30a44072ab29848e76e14bb585b629619d8f8cc624` |
| `feffec51…` EXPLORE_DIAG — NOT PINNED | `feffec5104882174031b43026e629e45771925c05272ee6e51b927dd5dafd144` |

### Appended 2026-09-24 ~20:32 ET (Archivist): Conductor ACCEPT Amendment B + Collector A02 PASS
| path | sha256 |
|---|---|
| `packets/ARCHIVIST_ACCEPT_AMENDMENT_B_AND_COLLECTOR_A02_2026-09-24.md` | `41b09495c92a534f822fe74999bdbf2a1320c3e1ed5867cef4f845dc79578044` |
| `packets/CONDUCTOR_ACCEPT_CARD01_NH002H_AMENDMENT_B_2026-09-24.json` | `74c5d49c0452ce97def7b36129ba362ebc4387627b93d5611bb67c5f8dfcbd23` |
| `packets/CARD01_HOUSE_ONLY_PROSPECTIVE_FREEZE_2026-09-24_AMENDMENT_B.md` (re-confirmed) | `ee6af37cef95f1e468d28e5b06750caaca8b1706ec11ed5cf5cdce460524c2c6` |
| `packets/card01_hybrid_forecast/amendment_b/NH002H_AMENDMENT_B_national_miss.py` PINNED (re-confirmed) | `049368f942741ff4a63acad328a49ff256252587d6c65f1e7e6d65d6101781f2` |
| `(box) astra-capture/card01-nh002-house/methodology_text_normalize.py` | `e1f5a55b396fc25ba3a928b2eabdc9b5d541e0604b753defbe3530da349de18f` |
| `(box) astra-capture/card01-nh002-house/electindex_capture.sh` (post A02) | `44afeecd9458a6068efaec7b68a1b513457dcc6bfe4d20237b65636ae912ca7d` |
| `(box) astra-capture/card01-nh002-house/_prev/f83d0ad3….electindex_capture.sh` | `f83d0ad325769fea5aeaf2963f88497b9c68acc6a2353ba315b27df6a271454a` |
| `(box) astra-capture/card01-nh002-house/electindex_capture_log.jsonl` @8 lines | `aa192f6fe0a9e7a015b994fc7aafe4ee1789f831703dcf0e19b9bc510fe68bd4` |
| methodology_text_sha256 (gate==capture BACKFILLED) | `14e46a33da83ea5403b57e019ce9d7ad90c3423cb00b7793b75fbe31b18a2205` |
| `main` after PR53 squash-merge (Conductor cite) | `95a8645d` |

### Appended 2026-09-24 ~20:35 ET (Archivist): PR55 PASS + Conductor ACKs + Card 03 A02
| path | sha256 |
|---|---|
| `packets/ARCHIVIST_PR55_BYTE_VERIFICATION_2026-09-24.md` **PASS 146/146** | `ae7ce7e649afd1dba5ced8b2f30f0a6488a117dcf71053d14e343e4f74c8573c` |
| `packets/ARCHIVIST_PR55_BYTE_VERIFICATION_2026-09-24.json` | `cadbc9b6f7bfc9a2cad6f7a30e46038a11d1608d403e305ea9e3cb6b09fe5ccb` |
| `packets/CONDUCTOR_ACCEPT_CARD01_NH002H_AMENDMENT_B_2026-09-24.json` (reaffirm LIVE) | `74c5d49c0452ce97def7b36129ba362ebc4387627b93d5611bb67c5f8dfcbd23` |
| `packets/CONDUCTOR_ACK_COLLECTOR_GET_BUDGET_ADDENDUM_2_2026-09-24.json` | `e082e526be62374faa9e306b7165c99589958ad1c1f674040ff288a68b49b6d4` |
| `packets/card03_liquidity_rewards/AMENDMENT_02_CARD03_PRE_OUTCOME_2026-09-24.md` | `72b794ad9af4e4c150d557add378b615516105ed132a690d31611706a0e09d70` |
| `packets/card03_liquidity_rewards/AMENDMENT_02.json` | `ff40a72e258d493852782dc89ce0cbe005d634265c2a1bc4f83a4c73908a0cb6` |
| `packets/card03_liquidity_rewards/CONDUCTOR_ACCEPT_AMENDMENT_02_CARD03_2026-09-24.json` | `51dc87d0e1cbebb97629d564da8891b17023a4f9194e8a17661a67f28259ce75` |
| `packets/ARCHIVIST_ACCEPT_AMENDMENT_B_AND_COLLECTOR_A02_2026-09-24.md` | `41b09495c92a534f822fe74999bdbf2a1320c3e1ed5867cef4f845dc79578044` |

### Appended 2026-09-24 ~20:26 ET (Archivist): ElectIndex Amendment 03 first capture R0_MATCH
| path | sha256 |
|---|---|
| `packets/ARCHIVIST_ELECTINDEX_AMENDMENT_03_FIRST_CAPTURE_2026-09-24.md` | `a6fedb4d29151887dc0eae5bf98fcc583affabb125a473e73e88f115d56bf74e` |
| `(private) evidence_private/electindex/methodology_asset/2026-09-25_eifc-info.js` | `caaff53e739413a8340f0addbec7136ec1995195291cab61889a94c1286ea87f` |
| `(box) astra-capture/card01-nh002-house/electindex_capture_log.jsonl` @10 lines | `b8555aefb9fcaf2931629e0ae5d49d927e5ed9e1d0dcce148f7807fbd1577aa4` |

### Appended 2026-09-24 ~20:28 ET (Archivist): Amendment 03 capture-script edit LIVE
| path | sha256 |
|---|---|
| `packets/ARCHIVIST_ELECTINDEX_AMENDMENT_03_SCRIPT_EDIT_RECEIPT_2026-09-24.md` | `9fe23c9b899ba5cccf92b2cea2c16a98b553b0b1e2a374f892a2da362e287a4f` |
| `packets/COLLECTOR_AMENDMENT_03_CAPTURE_SCRIPT_EDIT_REPORT_2026-09-24.json` | `8f0a7e7e949712cf958a608856da951736ef2267b4be277076c2d1da6990569b` |
| `(box) astra-capture/card01-nh002-house/electindex_capture.sh` (post A03) | `a4ab9969c4386dfd071cfe7166491ecaa8363da1d7dda7f1f1fd5d159a726eaa` |
| `(box) astra-capture/card01-nh002-house/_prev/44afeecd9458a6068efaec7b68a1b513457dcc6bfe4d20237b65636ae912ca7d.electindex_capture.sh` | `44afeecd9458a6068efaec7b68a1b513457dcc6bfe4d20237b65636ae912ca7d` |

### Appended 2026-09-24 ~20:28 ET (Archivist): PR #56 LEDGER extract PASS
| path | sha256 |
|---|---|
| `packets/ARCHIVIST_PR56_BYTE_VERIFICATION_2026-09-24.md` | `c89cf3d0a71aea1863a8073bb81c197a0f65886250826a33d37732ae7ebeb186` |
| `packets/ARCHIVIST_PR56_BYTE_VERIFICATION_2026-09-24.json` | `b63fc86e16000d2852005090a8f307fa7723e3983789320973e97416c020da06` |
| `packets/card01_hybrid_forecast/LEDGER_HASH_REGISTER_EXTRACT_2026-09-24.json` | `03f9c1938ca265c33cbc229e86b4fdda0a988583a28dd9090f4c08c48f1c5cd8` |
| GitHub PR #56 head | `5aeb4b9c739987aeac06178705a31308fff58b15` (draft) |

### Appended 2026-09-24 ~20:30 ET (Archivist): PR #55/#56 merges + EXP2 freeze stub
| path | sha256 |
|---|---|
| `packets/CONDUCTOR_MERGE_TIER_A_RESULTS_LANDING_PR55_2026-09-24.json` | `fff33b2eb6dec470b85a34eec381b4c54b984a4201b042e93bc1aab0454ce9e3` |
| `packets/CONDUCTOR_MERGE_AMENDMENT_B_HASH_REGISTER_EXTRACT_PR56_2026-09-24.json` | `1df45b715078250356c87ab8b1f87497a9b90bab914a07566fab1a5ca2ccd0cb` |
| `packets/ARCHIVIST_INDEX_CONDUCTOR_MERGES_PR55_PR56_2026-09-24.md` | `4b15342bc8fbe7e78b15646b834bf7dcf6323bf9d4794ff18e4a4b5d7028e03f` |
| `packets/CARD01_EXP2_CENSUS_GATECOUNT_FREEZE_KERNEL_2026-09-24.md` | `7087eb45ea8f2af0667f1aa427b674f50f6aa041ba12d3bfde9e22ac676751d8` |
| `briefs/CARD01_EXP2_CENSUS_FREEZE_ACK_2026-09-24.md` | `e0b8584935cc4cff9afb7973542da60944c5f2d45393ebb826f655552a5665de` |
| `packets/ARCHIVIST_INDEX_CARD01_EXP2_CENSUS_FREEZE_AWAITING_ACCEPT_2026-09-24.md` | `83ded05afe0160eb5d68196605150b3f840fbcfb63fb9038558b85e1233bf1c6` |
| merge #55 | `c880e1dbe78b2911727a2a1a226d7dcdc8489fd7` |
| merge #56 | `47f0ec58157a3036ee7992d5efb20fac85f63c98` |

### Appended 2026-09-24 ~21:37 ET (Archivist): catch-up ACK/ACCEPT/PR57 + Scout edit log
| path | sha256 |
|---|---|
| `packets/CONDUCTOR_ACK_ATP_RJ_PROBE_AND_BUDGET_2A_2026-09-24.json` | `b9824df125ddca21691b3241b5c0d5ea6801ae61659c1ae3922d7ca17b9649ab` |
| `packets/CONDUCTOR_ACCEPT_CARD01_EXP2_CENSUS_GATECOUNT_2026-09-24.json` | `ec1ddbb9c4575d32d775ed02682369c4cc1b1f0395251615ce60c9b04b47e189` |
| `packets/CONDUCTOR_MERGE_ATP_KXATPMATCH_MEASURE_HARDENING_INFRA_PR57_2026-09-24.json` | `5dd8006b2e939c0b3eb72fdb25840a499e6ee92ddb07499830785461619fc024` |
| `packets/ARCHIVIST_CATCHUP_INDEX_2026-09-24_2137.md` | `377017a42fe8350377bc4183c46c503069603fcbcc5570315d3115da1dee9980` |
| `packets/ARCHIVIST_STATUS_CARD01_EXP2_CENSUS_ACCEPTED_2026-09-24.md` | `2e8173a427ea94689ae77563595ffee74e41d4310411de54a0efd4e366a32881` |
| Card 04 brief (current) | `773e5abee36f6aae51dc49d0e8bab08f7e800a040b06754e47f5d02b3bda7e43` |
| Card 06 freeze (untouched) | `db3b0a18fd96e2f56d309f1a1b40e46bfd84953699e76163c2ad62440f0044fe` |
| PR #57 merge | `1c5288b4c96fc5dc49ffd6c13ffd690767cadf6f` |

### Appended 2026-09-24 ~21:38 ET (Archivist): Card 06 raw _prev gap CLOSED
| path | sha256 |
|---|---|
| `packets/ARCHIVIST_CARD06_PREV_BYTES_GAP_CLOSED_2026-09-24.md` | `97c2438b48907ec17c6921244bae351d8484062d5b6db73321df0845032029df` |
| `packets/scout_card06_census/_prev/20431e29….bls_schedule_2025_BROWSER.txt` | `20431e29ceeb7d24d5d048300f6ffa60b91e7362e11118486b05904de88d2c26` |
| `packets/scout_card06_census/_prev/385a6ece….tesla_ir_BROWSER_ERRORBODY_http403.txt` | `385a6eceac7f31bce2a8223d04e436687631ee0d10cfe643c9e3291ece445df8` |
| `packets/scout_card06_census/_prev/d57d0e61….bls_empsit_schedule_BROWSER.txt` | `d57d0e61df4a4feb79bac943631124d98f2ab4d448e0ae4cf15cd11e2b489f08` |

### Appended 2026-09-24 ~21:38 ET (Archivist): Card 06 raw _prev gap CLOSED
| path | sha256 |
|---|---|
| `packets/ARCHIVIST_CARD06_PREV_BYTES_GAP_CLOSED_2026-09-24.md` | `97c2438b48907ec17c6921244bae351d8484062d5b6db73321df0845032029df` |
| `packets/scout_card06_census/_prev/20431e29….bls_schedule_2025_BROWSER.txt` | `20431e29ceeb7d24d5d048300f6ffa60b91e7362e11118486b05904de88d2c26` |
| `packets/scout_card06_census/_prev/385a6ece….tesla_ir_BROWSER_ERRORBODY_http403.txt` | `385a6eceac7f31bce2a8223d04e436687631ee0d10cfe643c9e3291ece445df8` |
| `packets/scout_card06_census/_prev/d57d0e61….bls_empsit_schedule_BROWSER.txt` | `d57d0e61df4a4feb79bac943631124d98f2ab4d448e0ae4cf15cd11e2b489f08` |

### CORRECTION 2026-09-24 ~21:39 ET (Archivist): Card 06 `_prev` gap CLOSED — authoritative hashes
Ignore any earlier same-topic index rows with transposed/garbled sha prefixes. Authoritative:
| path | sha256 |
|---|---|
| `packets/ARCHIVIST_CARD06_PREV_BYTES_GAP_CLOSED_2026-09-24.md` | `b6fde4e591e94968a1be407c1dcaffd246c084827ccf10f88e44c374d33e3187` |
| `packets/scout_card06_census/_prev/20431e29ceeb7d24d5d048300f6ffa60b91e7362e11118486b05904de88d2c26.bls_schedule_2025_BROWSER.txt` | `20431e29ceeb7d24d5d048300f6ffa60b91e7362e11118486b05904de88d2c26` |
| `packets/scout_card06_census/_prev/385a6eceac7f31bce2a8223d04e436687631ee0d10cfe643c9e3291ece445df8.tesla_ir_BROWSER_ERRORBODY_http403.txt` | `385a6eceac7f31bce2a8223d04e436687631ee0d10cfe643c9e3291ece445df8` |
| `packets/scout_card06_census/_prev/d57d0e61df4a4feb79bac943631124d98f2ab4d448e0ae4cf15cd11e2b489f08.bls_empsit_schedule_BROWSER.txt` | `d57d0e61df4a4feb79bac943631124d98f2ab4d448e0ae4cf15cd11e2b489f08` |
| `packets/scout_card06_census/FREEZE_CARD06_CENSUS_2026-09-24.md` (untouched) | `db3b0a18fd96e2f56d309f1a1b40e46bfd84953699e76163c2ad62440f0044fe` |

### Appended 2026-09-24 ~21:40 ET (Archivist): Card 06 ACCEPT + CEM-006
| path | sha256 |
|---|---|
| `packets/CONDUCTOR_ACCEPT_CARD06_OPEN_WINDOW_CENSUS_2026-09-24.json` | `ebf6eb03aef7b75552d3d6f3e0b8723b130cca4614c917d9918c671e0f169cef` |
| `cemetery/CEM-ASTRA-20260924-006_CARD06_MACRO_OPEN_WINDOW.md` | `b57a819677e0f633462b021a329b25616806502dee4117286277203c9292545d` |
| `packets/ARCHIVIST_INDEX_CARD06_ACCEPT_AND_CEM006_2026-09-24.md` | `08dd679e73f2d45a4822ea9faad854221607740157b28fae6c3042c9e04351ed` |

### Appended 2026-09-24 ~21:42 ET (Archivist): Scout House fee source (ADDENDUM_02)
| path | sha256 |
|---|---|
| `SCOUT_HOUSE_FEE_SOURCE_2026-09-24.md` | `02fb1de12c573c2330899562cd832b48bd024a1c9f0e3886f23e1be83751b8e8` |
| `packets/scout_house_fee_2026-09-24/MANIFEST.sha256` | `fd2c7894bedbcf53126d7dc2eda5a4ea3164fa027a438ed12d9c42802717eb8f` |
| `packets/scout_house_fee_2026-09-24/raw/docs/kalshi_fee_schedule.pdf` | `c326a69f596a11e8f8be2620402d39a8d4823920c21cc97c93a114d862699601` |
| `packets/ARCHIVIST_INDEX_SCOUT_HOUSE_FEE_SOURCE_2026-09-24.md` | `ae12a636d33441cac9d3ec3ee563010e7125d82d5c4cf3885a306527aa8da171` |

### Appended 2026-09-24 ~23:01 ET (Archivist): CARD01 House mapping live pin
| path | sha256 |
|---|---|
| `packets/card01_hybrid_forecast/collector_mapping_get_2026-09-24/MAPPING_2026_HOUSE.json` | `4af13691c7a4fd629c643444433776d081a4ad9641eb931c3afedc7c3e4eddf1` |
| `packets/ARCHIVIST_INDEX_CARD01_HOUSE_MAPPING_2026-09-24.md` | `bd9f14ba6dd0550e9202418e6ace65b481dea0407afc5a7390d82f0eb394892d` |
| REJECTED_STALE_CLAIM | `bbdd49c079ca98fd7a02f13dd69d75e60cf5b4e97f0c21153cd47de83566b2f6` (no object) |

### Appended 2026-09-24 ~23:48 ET (Archivist): Card 06 company-KPI ACCEPT + House fee ADDENDUM_02 stamp
| path | sha256 |
|---|---|
| `packets/CONDUCTOR_ACCEPT_CARD06_COMPANY_KPI_OPEN_WINDOW_2026-09-24.json` | `53cba54a4f8866da82407b3be2e6d2b4dc3ccbf12944ded2924c55cd8d23e5f3` |
| `packets/scout_card06_company_kpi/FREEZE_CARD06_COMPANY_KPI_2026-09-24.md` | `1413603c964fa8087ea396997e5ecb56c0b0a21e5b3d497629b6078d7fb4a1e8` |
| `SCOUT_CARD06_COMPANY_KPI_OPEN_WINDOW_2026-09-24.md` | `78d53479462d7c3992678cb2652cf0d711f931f96d3c9daff8edaf5321b30eff` |
| `packets/scout_card06_company_kpi/out/census.json` | `41271e8e233a76ee7fb2cae48353b0520da6882407b6bf4d5476dcd369174a41` |
| `packets/scout_card06_company_kpi/AMENDMENT_01_2026-09-24.md` | `69d1c4ec685d4e801daba29162f6ca9e555ef868698935a571e04f51d30287d4` |
| `packets/scout_card06_company_kpi/AMENDMENT_02_2026-09-24.md` | `3a19829dd9b7fd7e9127aa7ae326a07f6c754599e8d2acb16573cade9c922de2` |
| `packets/ARCHIVIST_INDEX_CARD06_COMPANY_KPI_ACCEPT_2026-09-24.md` | `8c8e3db3a9876d093cb781d7b3852ffcf37eb7eb71c585a6c170272801d00574` |
| `packets/CONDUCTOR_KICK_ARCHIVIST_HOUSE_FEE_ADDENDUM_02_2026-09-24.json` | `0a5adcddc702af3e505e6c8b5dddacec44c93568e17b07da0267bfec49f93511` |
| `registry/FEE_ACCOUNT_MANIFEST_v0_DRAFT_2026-09-24_ADDENDUM_02.json` (stamped) | `44a69092461a94b259209b60c583166bf1ec56b322fc5dc9bf69f1b0fa2a9a12` |
| `registry/_prev/eec516fc….FEE_ACCOUNT_MANIFEST_v0_DRAFT_2026-09-24_ADDENDUM_02.json` | `eec516fc8ed8ea09634b24842c7ae4cf55fb8f5b40a81e50418213424139f7f9` |
| `packets/ARCHIVIST_STAMP_FEE_ADDENDUM_02_2026-09-24.md` | `1c0046ba130f548ef33f19351a719cd04e00f1140866364b5ff21cc47d4f69e9` |
| `packets/ARCHIVIST_RECEIPT_CARD06_KPI_AND_FEE_ADDENDUM_02_2026-09-24.md` | `c39e7e702db3714c79b2bcd77278fde5c16ab835563421e2a658ad7a184e4acc` |

### Appended 2026-09-24 ~23:49 ET (Archivist): Refiner Q7-B ledger RULE-FROZEN edit
| path | sha256 |
|---|---|
| `packets/refiner/REFINER_PASS_LEDGER_Q7_ARM_B.md` | `9dad0ad1b8f1d3dcd9dd991ffe8b36d50ab89735bed8c4132f62c247aa982dde` |
| `packets/refiner/_prev/9f436daf….REFINER_PASS_LEDGER_Q7_ARM_B.md` | `9f436dafb6e7bb579b0148ed25401502812b7d1fc373c21bb66b367198ae75cf` |
| `packets/ARCHIVIST_INDEX_REFINER_Q7B_LEDGER_EDIT_2026-09-24.md` | `e3c61916cfd159d563ec9457630696d39d6cab465df28b46f2c69107042a0db2` |

### Appended 2026-09-25 ~00:03 ET (Archivist): Sports Q6 screen ACCEPT + Variants Q6S5 kick
| path | sha256 |
|---|---|
| `packets/CONDUCTOR_ACCEPT_SPORTS_Q6_SCREEN_2026-09-24.json` | `2aefbc1712a0389d65f565439d5599a7275688e872e8bc67d5c6dde3b1cd81f8` |
| `packets/scout_sports_q6_screen/FREEZE_SPORTS_Q6_SCREEN_2026-09-24.md` | `552314d2822f86bf4127be5de03b8d64aa8c16d6c0c81887bdc0cfbd411571df` |
| `SCOUT_SPORTS_Q6_SCREEN_2026-09-24.md` | `fae1d7cb85279a900e20043da697ab189c77c7cf4f7131f8607b6310548f0047` |
| `packets/CONDUCTOR_KICK_VARIANTS_Q6S5_KXMLBSPREAD_FEEQUEUE_FREEZE_2026-09-25.json` | `9c68ab12f6f5561ee176c5669b17ef40c4f5be20299687823ad7f0e9b67701c8` |
| `packets/ARCHIVIST_INDEX_SPORTS_Q6_SCREEN_ACCEPT_AND_VARIANTS_KICK_2026-09-25.md` | `7595402ea76018e506ea54a133fc576ef6a7a9fac3389b71a5fc70fb5acedadf` |

### CORRECTION 2026-09-25 ~00:05 ET (Archivist): Sports Q6 ACCEPT + Variants kick — hash/path fix
Supersedes garbled ~00:03 ET append. Authoritative on-disk:
| path | sha256 |
|---|---|
| `packets/CONDUCTOR_ACCEPT_SPORTS_Q6_SCREEN_2026-09-24.json` | `2aefbc1712a0389d65f565439d5599a7275688e872e8bc67d5c6dde3b1cd81f8` |
| `packets/scout_sports_q6_screen/FREEZE_SPORTS_Q6_SCREEN_2026-09-24.md` | `552314d2822f86bf4127be5de03b8d64aa8c16d6c0c81887bdc0cfbd411571df` |
| `SCOUT_SPORTS_Q6_SCREEN_2026-09-24.md` | `fae1d7cb85279a900e20043da697ab189c77c7cf4f7131f8607b6310548f0047` |
| `packets/CONDUCTOR_KICK_VARIANTS_Q6S5_KXMLBSPREAD_FEEQUEUE_FREEZE_2026-09-25.json` | `9c68ab12f6f5561ee176c5669b17ef40c4f5be20299687823ad7f0e9b67701c8` |
| `packets/ARCHIVIST_INDEX_SPORTS_Q6_SCREEN_ACCEPT_AND_VARIANTS_KICK_2026-09-25.md` | `7629a4e05f52ba00a320e9e6bbe0598235b04246f72bcf0ff4ab2ed8e4ec7533` |
| `packets/_prev/7595402ea76018e506ea54a133fc576ef6a7a9fac3389b71a5fc70fb5acedadf.ARCHIVIST_INDEX_SPORTS_Q6_SCREEN_ACCEPT_AND_VARIANTS_KICK_2026-09-25.md` | `7595402ea76018e506ea54a133fc576ef6a7a9fac3389b71a5fc70fb5acedadf` |

### Appended 2026-09-25 ~00:14 ET (Archivist): Q6S5 ACCEPT+IMPLEMENT GO
| path | sha256 |
|---|---|
| `packets/CONDUCTOR_ACCEPT_Q6S5_KXMLBSPREAD_FEEQUEUE_HARNESS_2026-09-25.json` | `5adc42f9c9533238a2187aafe7593bdf1b8cdec6d12b8d3e9b12cb5ab29000fc` |
| `packets/Q6S5_KXMLBSPREAD_FEEQUEUE_HARNESS_FREEZE_2026-09-25.md` | `4f65dcdf536755b9f7dc2449c2dcd90b2df74cdf99a441b676f1a71c4d709c6e` |
| `lab/astra-capture/q6s5-kxmlbspread/panel_stub.json` | `c7f1f1f4ca263838c4600ed46db8f525b68efc5399a567bd60929d18d76803cc` |
| `packets/Q6S5_KXMLBSPREAD_PANEL_STUB_2026-09-25.json` | `c7f1f1f4ca263838c4600ed46db8f525b68efc5399a567bd60929d18d76803cc` |
| `packets/CONDUCTOR_KICK_EXAMINER_Q6S5_KXMLBSPREAD_FEEQUEUE_HOLD_PRE_PR_2026-09-25.json` | `38375ffe1a554b406c6ea0e48be7cf9b71d3c1f0d0e1b6713cbc4ae76bff6c54` |
| `packets/EXAMINER_HOLD_Q6S5_KXMLBSPREAD_FEEQUEUE_HARNESS_PRE_PR_2026-09-25.json` | `57bbd3ddf8e99fe790eb827f3167f529528f0a30ae27ece1ff909617b2091aa8` |
| `packets/VARIANTS_ACCEPT_PING_Q6S5_KXMLBSPREAD_FEEQUEUE_HARNESS_2026-09-25.json` | `bdbe46edbf04b985c907f8690afe736bd66a5e8de4e69d6594f7117b9363221f` |
| `packets/VARIANTS_ARCHIVIST_REGISTRY_PING_Q6S5_KXMLBSPREAD_FEEQUEUE_HARNESS_2026-09-25.json` | `80ed8dd1bfce3316d5a7086d3ca52fc0dd68bfe2ca777545a1e92e0ffbe8119a` |
| `Q6S5_KXMLBSPREAD_FEEQUEUE_authentic_pins_2026-09-25.tgz` | `d5454dc8cd0a37f942afff812a182a7c90c2d84c3a4badf27aa3f12de3208342` |
| `packets/ARCHIVIST_INDEX_Q6S5_ACCEPT_IMPLEMENT_GO_2026-09-25.md` | `fd5704a682fe5c2bfd3afe866713f64511f2ac7c78522c6df662ee428590aedc` |

### Appended 2026-09-25 ~00:15 ET (Archivist): Examiner HOLD_PRE_PR Q6S5 (verified)
| path | sha256 |
|---|---|
| `packets/EXAMINER_HOLD_PRE_PR_Q6S5_KXMLBSPREAD_FEEQUEUE_HARNESS_2026-09-25.json` | `4fff8de68d763138adce448b0138f87477a2a2bb96248c01f17caa2c05ef2329` |
| `packets/ARCHIVIST_INDEX_EXAMINER_HOLD_PRE_PR_Q6S5_2026-09-25.md` | `ff157244ed9716dcd976bf53ffb0586e0dc36a76ce679f26b44d720f673104bd` |
| pin ACCEPT (reconfirmed) | `5adc42f9c9533238a2187aafe7593bdf1b8cdec6d12b8d3e9b12cb5ab29000fc` |
| pin Kick (reconfirmed) | `38375ffe1a554b406c6ea0e48be7cf9b71d3c1f0d0e1b6713cbc4ae76bff6c54` |
| pin freeze (reconfirmed) | `4f65dcdf536755b9f7dc2449c2dcd90b2df74cdf99a441b676f1a71c4d709c6e` |
| pin panel (reconfirmed) | `c7f1f1f4ca263838c4600ed46db8f525b68efc5399a567bd60929d18d76803cc` |

### Appended 2026-09-25 ~00:30 ET (Archivist): Q7-B Pass-2 Option A SCORE kick
| path | sha256 |
|---|---|
| `packets/SIMULATOR_READY_Q7_B_PASS2_OPTION_A_TAPE_WALK_2026-09-24.json` | `fdb68eba19ec4a12d248f2e949d39f2e1f0a2a37215d597c7f7e70889f66c980` |
| `packets/CONDUCTOR_KICK_EXAMINER_Q7_B_PASS2_OPTION_A_TAPE_WALK_SCORE_2026-09-25.json` | `669fedc4544b9d9aef15220e7e5c144a9c1194f9b81b0d27f690dfbd32862d47` |
| `lab/astra-science/nfl_q7_rehab_p2_rank_sizing_20260923/run_tape_walk.py` (Option A restored) | `9d5ef4c3a65cb6c464c48201324f3ce506ada24e474c9575ed6ebb3a40019f98` |
| `.../_prev/a06a105….run_tape_walk.py` | `a06a105fa25269c17bcc1f53d9ae498343097c189ee619aeada7cceb76d3399b` |
| `packets/ARCHIVIST_INDEX_Q7_B_PASS2_OPTION_A_SCORE_KICK_2026-09-25.md` | `02e046420513c4fd23e63ae6ad1c400295bf207346c3d6b214a6f7623754af54` |

### Appended 2026-09-25 ~00:32 ET (Archivist): PR58 merge + Examiner READY + Q6S1 maximize
| path | sha256 |
|---|---|
| `packets/CONDUCTOR_MERGE_Q6S5_KXMLBSPREAD_FEEQUEUE_HARNESS_PR58_2026-09-25.json` | `4d743c5ddce593f724ca44bf542fe527ce3e42cb0d5c2edfcb5b7ddfaaaf5ad9` |
| `packets/CONDUCTOR_KICK_EXAMINER_Q6S5_KXMLBSPREAD_FEEQUEUE_HARNESS_PR58_READY_NOT_SCORED_2026-09-25.json` | `277e88f51f7a28543faec79280e694aa5c11c8b1a2f293e57747ba3224febe7f` |
| `packets/CONDUCTOR_KICK_VARIANTS_Q6S1_KXATPMATCH_INVENTORY_REPROOF_FREEZE_2026-09-25.json` | `63eab2f727c9636196e08092339d5efc10439396bc9a7d3f696b7344ac746cb6` |
| `packets/MAXIMIZE_PIN_2026-09-25_0031ET.md` | `7629b19f9a9e2d2aabf83bf46918963d118f6333ffc35f4af5bd227f72b9c09e` |
| pin ACCEPT (reconfirmed) | `5adc42f9c9533238a2187aafe7593bdf1b8cdec6d12b8d3e9b12cb5ab29000fc` |
| pin freeze (reconfirmed) | `4f65dcdf536755b9f7dc2449c2dcd90b2df74cdf99a441b676f1a71c4d709c6e` |
| pin panel (reconfirmed) | `c7f1f1f4ca263838c4600ed46db8f525b68efc5399a567bd60929d18d76803cc` |
| `packets/ARCHIVIST_INDEX_PR58_MERGE_READY_Q6S1_MAXIMIZE_2026-09-25.md` | `30371acd6ab02a440cde9941b83020fe8a2987ef9b1ee07fcdb0f0bb0fc612a4` |

### Appended 2026-09-25 ~00:34 ET (Archivist): Q7-B Pass-2 Option A KEEP + ACCEPT + Refiner close
| path | sha256 |
|---|---|
| `packets/EXAMINER_SCORE_Q7_B_PASS2_OPTION_A_TAPE_WALK_2026-09-25.json` | `67d0b01b068793445ee15e71ab2bd4b5d673f3962d1af8db40e974ae4d53b0bc` |
| `packets/EXAMINER_SCORECARD_Q7_B_PASS2_OPTION_A_TAPE_WALK_2026-09-25.md` | `441772590f8f3300ff5ad69ec66b14dbab649b7e55348af895f5354a6394d546` |
| `packets/CONDUCTOR_ACCEPT_EXAMINER_Q7_B_PASS2_OPTION_A_KEEP_2026-09-25.json` | `0d611be8dbfbff6c3a4913aff136c695e4970f40ebd47176c034abe9e6ab5d98` |
| `packets/CONDUCTOR_KICK_REFINER_Q7_B_PASS2_KEEP_CLOSE_2026-09-25.json` | `f0983a2615d221869224bd3eaa63984ae9866d291cea6d3743c0834dacbcffe8` |
| `packets/MAXIMIZE_PIN_2026-09-25_0033ET.md` | `d36b57761fa1ca3d84af1b8c58e03618e94e283857fbade5ff3f82666f0d463d` |
| `packets/refiner/REFINER_PASS_LEDGER_Q7_ARM_B.md` (CLOSED KEEP) | `edc05f977039984140d779d4112e38cb6b9157ba1867919aa108855e0f6c07ac` |
| `packets/refiner/_prev/9dad0ad1….REFINER_PASS_LEDGER_Q7_ARM_B.md` | `9dad0ad1b8f1d3dcd9dd991ffe8b36d50ab89735bed8c4132f62c247aa982dde` |
| `packets/refiner/REFINER_PASS2_CLOSE_KEEP_Q7_B_PORTFOLIO_RANK_SIZING_2026-09-25.json` | `2cfa1781f5291a34ed5504565b924bd176acea9cb17d590ccffc732020f75407` |
| `packets/ARCHIVIST_INDEX_Q7_B_PASS2_OPTION_A_KEEP_CLOSE_2026-09-25.md` | `ef1c178136ce9a86ac163a2ab9107b663c0a6771bbdcbb21b107588193a0e272` |

### CORRECTION 2026-09-25 ~00:37 ET (Archivist): Q7-B Pass-2 KEEP close — receipt hash fix
Supersedes ~00:34 ET receipt row. Authoritative on-disk:
| path | sha256 |
|---|---|
| `packets/EXAMINER_SCORE_Q7_B_PASS2_OPTION_A_TAPE_WALK_2026-09-25.json` | `67d0b01b068793445ee15e71ab2bd4b5d673f3962d1af8db40e974ae4d53b0bc` |
| `packets/EXAMINER_SCORECARD_Q7_B_PASS2_OPTION_A_TAPE_WALK_2026-09-25.md` | `441772590f8f3300ff5ad69ec66b14dbab649b7e55348af895f5354a6394d546` |
| `packets/CONDUCTOR_ACCEPT_EXAMINER_Q7_B_PASS2_OPTION_A_KEEP_2026-09-25.json` | `0d611be8dbfbff6c3a4913aff136c695e4970f40ebd47176c034abe9e6ab5d98` |
| `packets/CONDUCTOR_KICK_REFINER_Q7_B_PASS2_KEEP_CLOSE_2026-09-25.json` | `f0983a2615d221869224bd3eaa63984ae9866d291cea6d3743c0834dacbcffe8` |
| `packets/MAXIMIZE_PIN_2026-09-25_0033ET.md` | `d36b57761fa1ca3d84af1b8c58e03618e94e283857fbade5ff3f82666f0d463d` |
| `packets/refiner/REFINER_PASS_LEDGER_Q7_ARM_B.md` | `edc05f977039984140d779d4112e38cb6b9157ba1867919aa108855e0f6c07ac` |
| `packets/refiner/_prev/9dad0ad1b8f1d3dcd9dd991ffe8b36d50ab89735bed8c4132f62c247aa982dde.REFINER_PASS_LEDGER_Q7_ARM_B.md` | `9dad0ad1b8f1d3dcd9dd991ffe8b36d50ab89735bed8c4132f62c247aa982dde` |
| `packets/refiner/REFINER_PASS2_CLOSE_KEEP_Q7_B_PORTFOLIO_RANK_SIZING_2026-09-25.json` | `2cfa1781f5291a34ed5504565b924bd176acea9cb17d590ccffc732020f75407` |
| `packets/ARCHIVIST_INDEX_Q7_B_PASS2_OPTION_A_KEEP_CLOSE_2026-09-25.md` | `7d8ee73bec04785b214aad1d63cdf10eaab99bb11d54aacf570e659235d8c79b` |
| `packets/_prev/ef1c178136ce9a86ac163a2ab9107b663c0a6771bbdcbb21b107588193a0e272.ARCHIVIST_INDEX_Q7_B_PASS2_OPTION_A_KEEP_CLOSE_2026-09-25.md` | `ef1c178136ce9a86ac163a2ab9107b663c0a6771bbdcbb21b107588193a0e272` |

### Appended 2026-09-25 ~00:38 ET (Archivist): Q6S5 READY ACCEPT + Clock admit kick
| path | sha256 |
|---|---|
| `packets/EXAMINER_READY_NOT_SCORED_Q6S5_KXMLBSPREAD_FEEQUEUE_HARNESS_PR58_2026-09-25.json` | `cb25d9a7aa65ea5bcbeaccab01fe27968542b78399e5049262f1e7ae296cead2` |
| `packets/CONDUCTOR_ACCEPT_EXAMINER_Q6S5_KXMLBSPREAD_FEEQUEUE_HARNESS_PR58_READY_NOT_SCORED_2026-09-25.json` | `96cb4632b2475a6819c5aa1d1bd2f7893de16309f6322a96271eaf0d7713ba8a` |
| `packets/CONDUCTOR_KICK_CLOCK_Q6S5_KXMLBSPREAD_PANEL_ADMIT_2026-09-25.json` | `1e2be3720a90283fffccd04b602d0350591ccc0242204e477086aeccc0d4d95f` |
| `packets/MAXIMIZE_PIN_2026-09-25_0034ET.md` | `1b3eb51e4cdea17d99f79eeb2668114fcce2aa267f8e4f17f535f0351c42e793` |
| pin merge (reconfirmed) | `4d743c5ddce593f724ca44bf542fe527ce3e42cb0d5c2edfcb5b7ddfaaaf5ad9` |
| pin panel (reconfirmed) | `c7f1f1f4ca263838c4600ed46db8f525b68efc5399a567bd60929d18d76803cc` |
| pin HOLD_PRE_PR (untouched) | `4fff8de68d763138adce448b0138f87477a2a2bb96248c01f17caa2c05ef2329` |
| Refiner Pass-2 CLOSE KEEP (noted) | `2cfa1781f5291a34ed5504565b924bd176acea9cb17d590ccffc732020f75407` |
| `packets/ARCHIVIST_INDEX_Q6S5_READY_ACCEPT_CLOCK_ADMIT_2026-09-25.md` | `282f8bfdf2218a01b0b85b2ca380e31f180086cb05b9caa7ff8db8ed89033a9b` |

### Appended 2026-09-25 ~00:39 ET (Archivist): Q6S5 Clock ADMIT + Collector GET kick
| path | sha256 |
|---|---|
| `packets/Q6S5_KXMLBSPREAD_PANEL_ADMITTED_2026-09-25.json` | `e36de2d1ce6286dff90d25f2fae680170c8a469c443c1beed974ffe80383fba1` |
| `lab/astra-capture/q6s5-kxmlbspread/panel_admitted.json` (twin) | `e36de2d1ce6286dff90d25f2fae680170c8a469c443c1beed974ffe80383fba1` |
| `packets/CLOCK_ADMIT_Q6S5_KXMLBSPREAD_2026-09-25.md` | `f73bbaf3faaaa73186a233bfc21699d8ee3c47779253902ccc86159b3cbd7422` |
| `packets/CONDUCTOR_ACCEPT_CLOCK_ADMIT_Q6S5_KXMLBSPREAD_2026-09-25.json` | `64ea00aa682b191d4bd3d39264389e5d813b9b8ae3883ac4337ee258925ab501` |
| `packets/CONDUCTOR_KICK_COLLECTOR_Q6S5_KXMLBSPREAD_GET_CAPTURE_2026-09-25.json` | `83cc234ca1ee511bd38fb3041cb79c99f9d9bdd6a24b7467600884a56f979cb6` |
| `packets/MAXIMIZE_PIN_2026-09-25_0038ET.md` | `9a48477c6dcb81a0b10feaeb07585785a876e6f45e61818f9e4e72d665c9f470` |
| pin panel stub (reconfirmed) | `c7f1f1f4ca263838c4600ed46db8f525b68efc5399a567bd60929d18d76803cc` |
| pin Clock kick (reconfirmed) | `1e2be3720a90283fffccd04b602d0350591ccc0242204e477086aeccc0d4d95f` |
| `packets/ARCHIVIST_INDEX_Q6S5_CLOCK_ADMIT_COLLECTOR_GET_2026-09-25.md` | `b1601efe3d89bcea5e8f6a1b0f7f55eb9301ae4d76d70f9458e2da387c0e80d7` |

### Appended 2026-09-25 ~00:43 ET (Archivist): Q6S1 ACCEPT+IMPLEMENT + HOLD_PRE_PR
| path | sha256 |
|---|---|
| `packets/CONDUCTOR_ACCEPT_Q6S1_KXATPMATCH_INVENTORY_REPROOF_2026-09-25.json` | `162100624297588516390aab51ba0161cf15d0659c439ec6b60e940b99845635` |
| `packets/Q6S1_KXATPMATCH_INVENTORY_REPROOF_FREEZE_2026-09-25.md` | `d86f7a402ea63fb132d80480f844a954fe9061a27b9b6bed125f9785ae64640e` |
| `packets/CONDUCTOR_KICK_EXAMINER_Q6S1_KXATPMATCH_INVENTORY_REPROOF_HOLD_PRE_PR_2026-09-25.json` | `5f4ae8aa1b8e0f9b987a72d48c27651adee6f4591c185ab2410df5896df96925` |
| `packets/EXAMINER_HOLD_Q6S1_KXATPMATCH_INVENTORY_REPROOF_PRE_PR_2026-09-25.json` | `eca9aad2409c5636742fe15cbc7947098cac4ba19c7d610e5e69a7454fdae72d` |
| `packets/MAXIMIZE_PIN_2026-09-25_0042ET.md` | `8baba155c9c38495fde1ba33eb90f42ca3e1fce7ad722987593cbb877843f2b3` |
| `packets/VARIANTS_ARCHIVIST_REGISTRY_PING_Q6S1_KXATPMATCH_INVENTORY_REPROOF_2026-09-25.json` | `e744c0959d17f2e5e4f7771bca63df052c89c3b41244666961e3b224bd1f3a23` |
| `packets/VARIANTS_ACCEPT_PING_Q6S1_KXATPMATCH_INVENTORY_REPROOF_2026-09-25.json` | `e500475e302937c43a856be0c471bbaa706d4f2e91387c5bb505bfd9584a9ed4` |
| pin Variants FREEZE kick (reconfirmed) | `63eab2f727c9636196e08092339d5efc10439396bc9a7d3f696b7344ac746cb6` |
| pin panel stub (reconfirmed) | `ed041c502d1f775d33c44bf900ac91b1339d99045bddd2052edd09a139ae2d3f` |
| `packets/ARCHIVIST_INDEX_Q6S1_ACCEPT_IMPLEMENT_HOLD_PRE_PR_2026-09-25.md` | `a4140d84bc31a69d5ec031381b8ff4b8397317c875764cdd045bec8fff40888c` |

### Appended 2026-09-25 ~00:45 ET (Archivist): Q6S1 Examiner HOLD_PRE_PR ACK
| path | sha256 |
|---|---|
| `packets/EXAMINER_ACK_CONFIRM_HOLD_PRE_PR_Q6S1_KXATPMATCH_INVENTORY_REPROOF_2026-09-25.json` | `2934832ac8d7607563d1643c66cae380132095277377d3cfb4c7f058dd893b80` |
| pin existing HOLD (untouched) | `eca9aad2409c5636742fe15cbc7947098cac4ba19c7d610e5e69a7454fdae72d` |
| pin ACCEPT (reconfirmed) | `162100624297588516390aab51ba0161cf15d0659c439ec6b60e940b99845635` |
| pin HOLD kick (reconfirmed) | `5f4ae8aa1b8e0f9b987a72d48c27651adee6f4591c185ab2410df5896df96925` |
| pin freeze (reconfirmed) | `d86f7a402ea63fb132d80480f844a954fe9061a27b9b6bed125f9785ae64640e` |
| `packets/ARCHIVIST_INDEX_Q6S1_EXAMINER_HOLD_PRE_PR_ACK_2026-09-25.md` | `4dde3b5db917cf55b90a940ff8d524361c18cbb928bd5dddec5866b248c49594` |

### Appended 2026-09-25 ~00:55 ET (Archivist): Q6S5 INCOMPLETE_HONEST + CONTINUE ACK
| path | sha256 |
|---|---|
| `astra-capture/q6s5-kxmlbspread/measured/INCOMPLETE_HONEST.json` | `6e9a2b96a06cfde0931329a4f8be57326f6917e3f1741ad3a5d76676d767f0b6` |
| `astra-capture/q6s5-kxmlbspread/measured/STATUS.json` | `662ab2bdd0cd3a54f5e6b9f3d30da7a8398a1f9240e134db5819ca40419f12f1` |
| `astra-capture/q6s5-kxmlbspread/measured/CAPTURE_MANIFEST.json` | `2591dda5b73331f0328cf3d8a52d6021d22c5076800af27b454524d43027c6d2` |
| `astra-capture/q6s5-kxmlbspread/measured/DIGESTS.txt` | `3b279394372c5fba00de1c99c9646075fd02a28547353f75979e862da1897644` |
| `packets/CONDUCTOR_ACK_COLLECTOR_Q6S5_KXMLBSPREAD_INCOMPLETE_HONEST_2026-09-25.json` | `cc4d95062f0cdfb59381311961daa2a8e995814ad3f31f6be24a43f7d12aaa93` |
| pin panel admitted (reconfirmed) | `e36de2d1ce6286dff90d25f2fae680170c8a469c443c1beed974ffe80383fba1` |
| pin Clock ACCEPT (reconfirmed) | `64ea00aa682b191d4bd3d39264389e5d813b9b8ae3883ac4337ee258925ab501` |
| pin Collector GET kick (reconfirmed) | `83cc234ca1ee511bd38fb3041cb79c99f9d9bdd6a24b7467600884a56f979cb6` |
| `packets/ARCHIVIST_INDEX_Q6S5_INCOMPLETE_HONEST_CONTINUE_2026-09-25.md` | `4b76fd8987e06934e5898985750c3a0c38e26b5971e25e544469ce3c81b45216` |

### Appended 2026-09-25 ~02:05 ET (Archivist): Q6S5 trades READY + Simulator REJOIN
| path | sha256 |
|---|---|
| `packets/CONDUCTOR_ACK_COLLECTOR_Q6S5_KXMLBSPREAD_TRADES_READY_2026-09-25.json` | `95e3140bc7f5ad89287ee1ec5d648f6d938d1cbd18b8eba9615c2eed6b02fd11` |
| `packets/CONDUCTOR_KICK_SIMULATOR_Q6S5_KXMLBSPREAD_TRADES_JOIN_2026-09-25.json` | `76de2f1fa2461008bc1205e5004230ffd45fd2d3e6193d6cc0c11c616b499006` |
| `astra-capture/q6s5-kxmlbspread/trades_fills_2026-09-25/COLLECTOR_READY_TRADES_NOT_SCORED.json` | `57194f272ab6bbe7a4d116c1fd4aabd5199e3a02a6cd96ed5cc6b7bd4bafb867` |
| `astra-capture/q6s5-kxmlbspread/trades_fills_2026-09-25/DIGESTS.txt` | `12b537a25b02fb33177d5a41c821f94677f1da88e8d1dd63178c3c9f59fac12b` |
| `astra-capture/q6s5-kxmlbspread/trades_fills_2026-09-25/STATUS.json` | `e8e23f7d341c2d236243054663caf684c9e3fca40975dd48842d6b4052893e9a` |
| `astra-capture/q6s5-kxmlbspread/trades_fills_2026-09-25/CAPTURE_MANIFEST.json` | `db7257d59faa4bb75acf21e0c5d2326b151d6ecf2a9690ffad13ffeb3744038f` |
| pin Collector trades kick (reconfirmed) | `b7b741745ef513ec5f9b7e31554263baec54518add1da25201e4de8c7665b836` |
| pin ACCEPT harness ITERATE (reconfirmed) | `54b0b1b7d57d42f3a2f2d0caefd72be734532eaae8d8c54fbcb8817a7df99a71` |
| `packets/ARCHIVIST_INDEX_Q6S5_TRADES_READY_SIM_JOIN_2026-09-25.md` | `3385c90962d58c1dcb7915873f685ec8cc4c8e65af534e369e56f0fb261c747c` |

### Appended 2026-09-25 ~02:06 ET (Archivist): Q6S5 INDEX backlog catch-up
| path | sha256 |
|---|---|
| `astra-capture/q6s5-kxmlbspread/measured/READY_NOT_SCORED.json` | `0617d540763d71a813672c9f9aa6766072c8461a1290c124b89e9fb3f2bf5de2` |
| `astra-capture/q6s5-kxmlbspread/measured/DIGESTS.txt` | `6e6898ce956b7d97e71ec675accc52fb29b73843a16b58f4620cf513e1c7d94b` |
| `packets/CONDUCTOR_ACK_COLLECTOR_Q6S5_KXMLBSPREAD_READY_NOT_SCORED_2026-09-25.json` | `c1d82c6e95174ddc322d35a19c63879996883b13773b56fab427dd810ac85bae` |
| `packets/CONDUCTOR_KICK_EXAMINER_Q6S5_KXMLBSPREAD_MEASURED_SCORE_2026-09-25.json` | `fee42dec435553bb375180a98cfa7ca48d3ca032714260f096dcc4e6817ff504` |
| `packets/EXAMINER_SCORE_Q6S5_KXMLBSPREAD_MEASURED_2026-09-25.json` | `db9bd220b5dd61229b6481a27d03222f36ac0ec816efa3402ef35404a0d4fb8e` |
| `packets/EXAMINER_SCORECARD_Q6S5_KXMLBSPREAD_MEASURED_2026-09-25.md` | `9b1e2074e1559f618af3d66b4a23bfc4e75cad2fa2f714c4088bc354c08b7fc1` |
| `packets/CONDUCTOR_ACCEPT_EXAMINER_Q6S5_KXMLBSPREAD_MEASURED_ITERATE_2026-09-25.json` | `4122d100fe27ac855d3c186a2d7e048dbe2d2da547fb25545ed67e13b8e530de` |
| `packets/CONDUCTOR_KICK_SIMULATOR_Q6S5_KXMLBSPREAD_MEASURED_HARNESS_2026-09-25.json` | `c799f3f2771da1b6ae56e80bbbd20b6f5b145176630d9a4bfdf523bafea32961` |
| `packets/CONDUCTOR_KICK_EXAMINER_Q6S5_KXMLBSPREAD_LIVE_SERIES_FEE_PIN_2026-09-25.json` | `abbc2bf1cc789922b882dce0fe3cf9b926a1099d69de24d7757e183b420d6f49` |
| `packets/EXAMINER_FEE_PIN_Q6S5_KXMLBSPREAD_LIVE_SERIES_2026-09-25.json` | `9c0f3554eedc582ed4bed940575bf7ee6c0540ce5134140c5ea19e7c458d2b6a` |
| `governance/astra/packets/SIMULATOR_READY_Q6S5_KXMLBSPREAD_MEASURED_HARNESS_2026-09-25.json` | `1c84cc6b8d44ab720ffe537d6f3e9e257de12e2ca8706cc1ec96c51d127e7bb3` |
| `packets/CONDUCTOR_ACK_SIMULATOR_Q6S5_KXMLBSPREAD_MEASURED_HARNESS_READY_2026-09-25.json` | `1811542260ff28ba28938bb1c2dbbb285d4e30e6ad3cd38e7fec08a609fd0111` |
| `packets/CONDUCTOR_KICK_EXAMINER_Q6S5_KXMLBSPREAD_MEASURED_HARNESS_RESCORE_2026-09-25.json` | `06dc4abc146802a168f13c854fe6f3a265f4e0ade69ae87ba35ede83a61cc3db` |
| `packets/EXAMINER_SCORE_Q6S5_KXMLBSPREAD_MEASURED_HARNESS_2026-09-25.json` | `348e2981d191fda5a228ef77fc578b0821bd731ae6aa38b1b8004d9d82ba3d62` |
| `packets/EXAMINER_SCORECARD_Q6S5_KXMLBSPREAD_MEASURED_HARNESS_2026-09-25.md` | `0a204d49d24d1666e1039251beaceecffb262fbb98b1e68eb78d2f300f5b9ea0` |
| `packets/EXAMINER_HOLD_Q6S5_KXMLBSPREAD_MEASURED_INCOMPLETE_HONEST_2026-09-25.json` | `bd34d2075dc285b2bd2e2a83b15fdb85715b24389aa41e99f46b20672c8a91eb` |
| `packets/CONDUCTOR_ACK_EXAMINER_Q6S5_KXMLBSPREAD_FEE_PIN_2026-09-25.json` | `02fac1bb6375b32922eb534f90ac6ca8c8dc9f8f169f12a6e65831956d41a7b7` |
| `packets/EXAMINER_SCORECARD_STUB_S1_KXMLBGAME_2026-09-22.md` | `8f5fcec48e17de85ea7d655d92f0196a86ddab75ee5746e446f0bebd1ad0dc72` |
| `packets/Q6S5_KXMLBSPREAD_FEEQUEUE_HARNESS/EXAMINER_SCORECARD_STUB_Q6S5_KXMLBSPREAD_FEEQUEUE_HARNESS_2026-09-25.json` | `4da3c3709ffb8783c8e4b2117581d722789e132cf142d151c7ee7bfa15949926` |
| `packets/Q6S5_KXMLBSPREAD_FEEQUEUE_HARNESS/EXAMINER_SCORECARD_STUB_Q6S5_KXMLBSPREAD_FEEQUEUE_HARNESS_2026-09-25.md` | `4b33ecceebf6383073ecb260b319778ca37c1b8c7e46d64c09a91137d7116957` |
| `packets/Q6S5_KXMLBSPREAD_FEEQUEUE_HARNESS/_prev/c209486c1be9b446f361431ab1f6f20c42a83f951037c7d6337e2dc016bd66f9.EXAMINER_SCORECARD_STUB_Q6S5_KXMLBSPREAD_FEEQUEUE_HARNESS_2026-09-25.json` | `c209486c1be9b446f361431ab1f6f20c42a83f951037c7d6337e2dc016bd66f9` |
| `packets/Q6S5_KXMLBSPREAD_FEEQUEUE_HARNESS/_prev/dd1b1a55e55f3ec91b4bdecc3ef5a6d6625a5011c779b5540d233fbb41157732.EXAMINER_SCORECARD_STUB_Q6S5_KXMLBSPREAD_FEEQUEUE_HARNESS_2026-09-25.md` | `dd1b1a55e55f3ec91b4bdecc3ef5a6d6625a5011c779b5540d233fbb41157732` |
| `packets/ARCHIVIST_INDEX_Q6S5_BACKLOG_CATCHUP_2026-09-25.md` | `f2c10429bfbc632b7aad592b3f3782a951e0ebc5c171515c1dd5cde9fcbafc08` |

### Appended 2026-09-25 ~02:06 ET (Archivist): Q6S5 INDEX backlog catch-up
| path | sha256 |
|---|---|
| `astra-capture/q6s5-kxmlbspread/measured/STATUS.json` | `179cc61669510eeac242c12f8db4f34800d3ebb402bab48842fba8e7f8b18163` |
| `packets/ARCHIVIST_INDEX_Q6S5_BACKLOG_CATCHUP_2026-09-25.md` | `895aca1ca825d8f3f8da47151af23c060976b5f248ebacdd38a8520199767c7e` |

### Correction 2026-09-25 ~02:07 ET (Archivist)
- Backlog catch-up receipt rewritten after STATUS_measured pin; authoritative receipt sha256 `895aca1ca825d8f3f8da47151af23c060976b5f248ebacdd38a8520199767c7e`.
- Prior index row citing `f2c10429bfbc632b7aad592b3f3782a951e0ebc5c171515c1dd5cde9fcbafc08` for `ARCHIVIST_INDEX_Q6S5_BACKLOG_CATCHUP_2026-09-25.md` is superseded (stale mid-write). On-disk file matches `895aca1c…`.

### Appended 2026-09-25 ~02:16 ET (Archivist): Q6S5 trades-join READY + Examiner RESCORE
| path | sha256 |
|---|---|
| `packets/CONDUCTOR_ACK_SIMULATOR_Q6S5_KXMLBSPREAD_TRADES_JOIN_READY_2026-09-25.json` | `f338a09652f1da4442bdfcf579087660f435529885eb110a884b87acda3a23f2` |
| `packets/CONDUCTOR_KICK_EXAMINER_Q6S5_KXMLBSPREAD_TRADES_JOIN_RESCORE_2026-09-25.json` | `650283a7a69b4e6411b51c036e876694f27eb8db7908a52325092a1e2142e96f` |
| `packets/SIMULATOR_READY_Q6S5_KXMLBSPREAD_TRADES_JOIN_2026-09-25.json` | `5b47dea926a57e3f1c424e8df62f56ef9b1f02eea87bdd426b4e9248c21465f4` |
| `astra-science/kalshi_q6s5_kxmlbspread_feequue_trades_join_20260925/results/TRADES_JOIN_RUN_RESULTS.json` | `f707bcbdfddbc1505c0b22464200d07747656e703efba1c9cc66aa80eb0819ef` |
| `astra-science/kalshi_q6s5_kxmlbspread_feequue_trades_join_20260925/results/TRADES_JOIN_METRICS.json` | `3dcdf2ab5af1cc58a60f9664f9313ccb2cd95e87f346a009f7e2be2fcc491c32` |
| `astra-science/kalshi_q6s5_kxmlbspread_feequue_trades_join_20260925/DIGESTS.txt` | `02478c879bba61f1e634742c0df31e9fb0bc038b9d90cc0cc3324e313192732c` |
| `packets/EXAMINER_ACK_SIMULATOR_READY_Q6S5_KXMLBSPREAD_TRADES_JOIN_2026-09-25.json` | `5e2235c1d3ee100c5b7dcb1cb7c93579046f5d515b3e52d3cf0fa77d9bc7aacf` |
| pin Simulator trades-join kick (reconfirmed) | `76de2f1fa2461008bc1205e5004230ffd45fd2d3e6193d6cc0c11c616b499006` |
| pin Collector trades READY ACK (reconfirmed) | `95e3140bc7f5ad89287ee1ec5d648f6d938d1cbd18b8eba9615c2eed6b02fd11` |
| `packets/ARCHIVIST_INDEX_Q6S5_TRADES_JOIN_READY_RESCORE_2026-09-25.md` | `6ea270e4193026257241ba5d04ed0d70e32829c807a847486e669eb699a74024` |

### Appended 2026-10-02 ~19:24 ET (Archivist): KALSHI backlog 2026-09-25 → 2026-10-02 (items 1–14) + CEM-ASTRA-20261001-001
| path | sha256 |
|---|---|
| `packets/EXAMINER_SCORE_Q6S5_KXMLBSPREAD_TRADES_JOIN_2026-09-25.json` | `a18f2ad2f704d10ec526ccd2808edf8088f88de307ff8b3fe9845fa14ddde05a` |
| `packets/EXAMINER_SCORECARD_Q6S5_KXMLBSPREAD_TRADES_JOIN_2026-09-25.md` | `e3eeb1a07fddc08824a02a78a68b7f4aba69d77d8cbe5edb0b970bc61c69a9d1` |
| `packets/CONDUCTOR_ACCEPT_EXAMINER_Q6S5_KXMLBSPREAD_TRADES_JOIN_ITERATE_2026-09-25.json` | `ac713e5fcbdda218d98e88bf4faab340204d8ad47dc9f0613d3762feca69b50d` |
| `packets/CONDUCTOR_QUEUE_Q6S5_STRATEGY_FILL_FREEZE_AFTER_Q6S1_2026-09-25.json` | `7472b8ac01fd906577c49eb4d96b8fd5dbb2d7766c5a87fa86e47b3bffad2c61` |
| `packets/MAXIMIZE_PIN_2026-09-25_0220ET.json` | `f23653fbf0ac82e6dc66dcf058553057ea7bcafae069d7b35d5f31e04321a6c5` |
| `packets/CONDUCTOR_MERGE_Q6S1_KXATPMATCH_INVENTORY_REPROOF_PR59_2026-09-25.json` | `ef037c2c628f98a4db87fc05ffefb6a985ab525fcdfcd5ec84e003ef46f8098f` |
| `packets/CONDUCTOR_KICK_EXAMINER_Q6S1_KXATPMATCH_INVENTORY_REPROOF_PR59_READY_NOT_SCORED_2026-09-25.json` | `d2652887e0aa187ada8af96e96d6b0586e9ad938b0ebc19d2ab4d93f2e183803` |
| `packets/CONDUCTOR_KICK_VARIANTS_Q6S5_STRATEGY_FILL_FREEZE_2026-09-25.json` | `dc19794bdb8e26c3a3f4fe86eadc9bec1b02db97d508fca9426e3c3eddfb6bc8` |
| `astra-capture/prospective/ADMIT1_OUTAGE_GAP_2026-09-27_to_2026-09-29.json` | `4f2a5e2693f809e592238c0bf58ecac93f982fb8809c98ca81e51a41d8a65198` |
| `packets/CONDUCTOR_RULING_ADMIT1_OUTAGE_GAP_WEATHER_CARD03_RELAUNCH_2026-09-29.json` | `ac7cfe63623ca342ab5b4285ff58382a8138b58fb6cd8e95310a5d30d90304f2` |
| `packets/CONDUCTOR_ERRATUM_CARD03_GAP_WINDOW_2026-09-29.json` | `31da5974867ee6230928b641e4a939171bce44260a4b87ee9161ffc8f30477d9` |
| `packets/EXAMINER_NOTE_C1_PIT_CLE_ADMIT1_GAP_NOT_SCORED_2026-09-29.json` | `fe5ba611574253d7d6daf07b01bfd6051788775a8261ea82d4e6ae14d19bc1e3` |
| `packets/Q6S5_KXMLBSPREAD_STRATEGY_FILL_FREEZE_2026-09-25.md` | `9f50ba19694083c774bbe2a6cff491d1a2f81ed3a6f9cc21a3641a938c84955d` |
| `astra-science/kalshi_q6s5_kxmlbspread_strategy_fill_lab_20260925/Q6S5_KXMLBSPREAD_STRATEGY_FILL/Q6S5_KXMLBSPREAD_STRATEGY_FILL_authentic_pins_2026-09-25.tgz` | `6602e07ef9b444b8b242086d0cb338025507d117aa0874f24e99390cd9d01993` |
| `packets/VARIANTS_ARCHIVIST_REGISTRY_PING_Q6S5_KXMLBSPREAD_STRATEGY_FILL_2026-09-25.json` | `3cb00d3637ee8653a395e9547b1f4bfed3fbb11eff6abac60f2937d3d282849d` |
| `packets/VARIANTS_ACCEPT_PING_Q6S5_KXMLBSPREAD_STRATEGY_FILL_2026-09-25.json` | `860b808e868acfae265dda0a925679cca0a91f8c7d12b07dd6bed09062fc6ae6` |
| `packets/Q6S1_KXATPMATCH_INVENTORY_REPROOF_V2_BUNDLE/Q6S1_KXATPMATCH_INVENTORY_REPROOF_authentic_pins_v2_2026-09-25.tgz` | `62de476ec3d27b64183d1eba0d223c2c5ad61a6bc8abffde9873f6e76a5e633e` |
| `packets/Q6S1_KXATPMATCH_INVENTORY_REPROOF_V2_BUNDLE/PROVENANCE_NOTE.md` | `160bb6df8efa729468224c452fa9ad7bbc7dc6960c6b9acb0b85e6d52680fb16` |
| `packets/CONDUCTOR_MERGE_Q6S5_KXMLBSPREAD_STRATEGY_FILL_PR60_2026-09-29.json` | `3486a2fe71da0be40a3cb6202abcc30e1783515180e20f594b3c25b034414bef` |
| `packets/Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_FREEZE_2026-09-29.md` | `fb6540f52ed5f819ccf6e80bf0cf7eb6d951e065416b9d550fead0c6d06043fa` |
| `packets/Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE/MANIFEST.sha256` | `901285ed3d559e1a121197c1ee36ead3d8b40498dfd2b4888694fb077fe3c043` |
| `astra-science/kalshi_q6s5_kxmlbspread_fl_band_settled_tape_lab_20260929/pins/Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_authentic_pins_2026-09-29.tgz` | `63b5d981bc06f684eebb69a8ac29394534f8ae52c101f3018557544f14e29857` |
| `packets/VARIANTS_ARCHIVIST_REGISTRY_PING_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_2026-09-29.json` | `eba1260f1ab901a223f3f0b5feb1ff6f023d9f8870c1e69e16007e93e12b3a40` |
| `packets/r3_p3_fl_maker_taker/bands_registry_10c.json` | `0860cbe28d28ecc6142ddf6f1ebb67792084264ed82e0b4d868c3b3138ea5312` |
| `packets/CONDUCTOR_ACCEPT_VARIANTS_Q6S5_FL_BAND_SETTLED_TAPE_FREEZE_2026-10-01.json` | `8e4fbac7d0426bc67c1f53fb8057a382fe46da738bd701cb970a9812a6dc2a3b` |
| `packets/CONDUCTOR_RULING_Q6S5_FL_BAND_IN_SAMPLE_DEV_LABEL_2026-10-01.json` | `09763030c67df066f2b59346200813e181777670cd46fcee6b8877a6dd74d754` |
| `packets/CONDUCTOR_MERGE_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.json` | `469de2376ae413f66684df26c08656e705a7fb5a0a1d128a4270d789c841df32` |
| `packets/EXAMINER_SCORE_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.json` | `2e74f17b1307b8b57f33a6475cd7ce8af48c470099478cadfb07877b0d70745f` |
| `packets/EXAMINER_SCORECARD_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.md` | `1bdb1d9c1e6272a4b95a5080e4681858859e69a053f69e32b9b85b7d9e44c386` |
| `packets/CONDUCTOR_ACCEPT_EXAMINER_KILL_Q6S5_KXMLBSPREAD_FL_BAND_PR61_2026-10-01.json` | `be2357773ca7a842e6896676e3ba0291f40ef8e0b8f997d46f7124d4b2705229` |
| `packets/SIMULATOR_READY_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.json` | `8e8a17566747cb29077c2f7abccb49640739ae873d3d5c20fbfa819bbde36e1b` |
| `packets/CONDUCTOR_SCORE_KICK_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.json` | `0f8de7cd6b2187076e2bd8f914c4de51b3d8bfecdd59e324a41a9f030f5f26b6` |
| `packets/CONDUCTOR_ACCEPT_EXAMINER_ITERATE_Q6S5_GAME_PHASE_PR62_AND_ANNOTATE_be235777_2026-10-01.json` | `546f62c99f1268b14ddb612fe9891c7741e5bee7e8397cae32c75d86fbff65ae` |
| `packets/C4_KXCPI_SETTLED_JOIN_HARNESS/SOURCE_PINS.json` | `bcd27e06f57f0e6b617ce318fb6d42da8c9b0a526816fbc4e41cef07a875154c` |
| `packets/C4_KXCPI_SETTLED_JOIN_HARNESS/FROZEN_EXPERIMENT.json` | `968a46e3733bc17e58c223ccc71525e5090ff7a1204b7c2222de4353a3940191` |
| `packets/ATP_KXATPMATCH_SETTLED_JOIN_HARNESS/SOURCE_PINS.json` | `509e2cf29c701de29a63b8c3cad06a3a405ac30b1677cc04c680c91d65ceddd9` |
| `packets/ATP_KXATPMATCH_SETTLED_JOIN_HARNESS/FROZEN_EXPERIMENT.json` | `382009b93b561f21e5942cf0aa5cfbc8ee21821ad4b89db66468bfbe7ad094dc` |
| `packets/C4_KXCPI_SETTLED_JOIN_HARNESS/DIGESTS.txt` | `a2754a8673bde8a82acb64226877e4f4d4b2d1a135f0b16d18ed7fed409083a8` |
| `packets/ATP_KXATPMATCH_SETTLED_JOIN_HARNESS/DIGESTS.txt` | `e72add7818b65edd32ee0132104611d166934688092c23fce762db4f0a5f8745` |
| `packets/scout_c4_settled_rejoin_2026-09-24/FROZEN_EXPERIMENT.json` | `b72465d809ccd208588ce13baa8749b8f5d1eedfb82abef47d261d84939b067f` |
| `packets/scout_atp_settled_rejoin_2026-09-24/FROZEN_EXPERIMENT.json` | `802b40b308724ae0980da123843d6a0655d087af2f162b3cc3a0f66d25e1d690` |
| `steward/RULING2_REALIGN_RECORD_2026-10-01.json` | `3bb3696927b87eca53011bf69b335130351d585c740ecaaad90320086a57f02a` |
| `/workspace/steward_astra_science_preserve_20261001/FROZEN_PREV_RECORD_astra_science.json` | `9b0d2e89aa6938ea3e71c66a7cb1533e98a3526c0749a29a53e2d7f76332761f` |
| `steward/STEWARD_CONDUCTOR_RULINGS_EXEC_2026-10-01.md` (on disk; cited 7e389f326e05a85612200d0e37bc76c2f2db41878a2412ce57381ad7f380b571 = pre-append bytes, no _prev: UNVERIFIED_BYTES_MISSING) | `133302a440281647f7589f29dad54882928c3d43253e77cf9bef78dbb6f5d578` |
| `steward/STEWARD_CONDUCTOR_RULINGS_EXEC_2026-10-01.json` | `433ba206a2961d56801b95551ae67ed6403da7cb5c1f83e6df9cf32ba7a262ac` |
| `packets/Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE_FREEZE_2026-10-01.md` | `5beba803f3f6d33410409acc23ad3b782be62dc8829a0f54584e1da8ac18575a` |
| `packets/Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE/MANIFEST.sha256` | `88af3bd79ad37c6fa09cfbe1bcd516c72b8a35d2928ce04eeaec994b5c1233a1` |
| `astra-science/kalshi_q6s5_kxmlbspread_game_phase_settled_tape_lab_20261001/pins/Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE_authentic_pins_2026-10-01.tgz` | `6576ee6cf9f023137e4357270f228dd9a5d29e3dc1d5e7ced85384681f2a7ecc` |
| `packets/VARIANTS_ACCEPT_PING_Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE_2026-10-01.json` | `7af58fa9253629c3defdcc52a2198b7d858a2a2a1b00544d10b65bcb7497fa7d` |
| `packets/CONDUCTOR_ACCEPT_VARIANTS_Q6S5_GAME_PHASE_SETTLED_TAPE_FREEZE_2026-10-01.json` | `08d23b363d72b8c8599772ee6fc6736cb90f13e8ed814b12c59b58fd5c7dc91e` |
| `packets/CONDUCTOR_MERGE_Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE_PR62_2026-10-01.json` | `fa361354aa284b36482b0c4a67715ff6cda63fcf70f2d0c535bd1f7bdc465d5b` |
| `packets/EXAMINER_SCORE_Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE_PR62_2026-10-01.json` | `1626e2d0e19f0e8cf35fc7b3a9e551f489957dab8e48be2f35216fd36ebda693` |
| `packets/EXAMINER_SCORECARD_Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE_PR62_2026-10-01.md` | `00c3da8d20a74d8baad8236eb94c43ca6a7d7cc681ad4b308a89884613a2d5ca` |
| `packets/EXAMINER_READY_NOT_SCORED_Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE_PR62_2026-10-01.json` | `e6c9ac56be33af2ccc7757409b3bd918034fd2c48a438fd749827cbbd186e4e6` |
| `packets/SIMULATOR_READY_Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE_PR62_2026-10-01.json` | `98d0e62581ec54a3cbac60d6fb6d1cc538e765d0ea733360993b5d129082f661` |
| `packets/CONDUCTOR_SCORE_KICK_Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE_PR62_2026-10-01.json` | `006d7d5dc08babfb352d94cdde2460d8d49726d87d66d15d05c7cbd7acc2e90a` |
| `packets/VARIANTS_HOLDOUT_PREREG_ADDENDUM_Q6S5_KXMLBSPREAD_UNTOUCHED_CAPTURE_2026-10-01.md` | `370dc31df17191446013b6cebb52d44ee8346f47d2f5b543a1c73049ba52c063` |
| `packets/VARIANTS_HOLDOUT_PREREG_ADDENDUM_Q6S5_KXMLBSPREAD_UNTOUCHED_CAPTURE_2026-10-01.json` | `a76d2673f85a817af435deb2f70ec8b421ac3d8d2eb57f601eb4da39927d9865` |
| `packets/CONDUCTOR_ACCEPT_VARIANTS_HOLDOUT_PREREG_ADDENDUM_Q6S5_KXMLBSPREAD_UNTOUCHED_CAPTURE_2026-10-01.json` | `9a987a77e6cd6293ddaeb14fadbf33a25c1a6cc392af25f46eaaaaae33ebb273` |
| `packets/CONDUCTOR_RULING_VARIANTS_WX_FL_PREFREEZE_2026-10-01.json` | `0e37f91b60289084f4e660b74bcb12a04f83f66fc93410add3a26baf0dd9f6af` |
| `packets/WX_FL_KXHIGH_SETTLED_TAPE/WX_FL_KXHIGH_SETTLED_TAPE_FREEZE_2026-10-01.md` | `aec5b760f8539ea9f30aa1c3601534dccf78a62ee2026cb939842656e3c20e0f` |
| `packets/WX_FL_KXHIGH_SETTLED_TAPE/MANIFEST.sha256` | `21beb0b51f33124e33541f36e36a1bde86c5a79100d8d1a4eea1a106a11af519` |
| `astra-science/wx_fl_kxhigh_settled_tape_lab_20261001/pins/WX_FL_KXHIGH_SETTLED_TAPE_authentic_pins_2026-10-01.tgz` | `febc74af09b06db83fb686e904d6f3e305fe30414e4c4f67c05705f0de597807` |
| `packets/WX_FL_KXHIGH_SETTLED_TAPE/snapshot/archive.sqlite` | `d20d5e7d0cedc79ed77c92e905b2824f0ca1d79f8e524635bfd3a8f0e3c6eae2` |
| `packets/WX_FL_KXHIGH_SETTLED_TAPE/SNAPSHOT_PROVENANCE.json` | `ed31cdf50ed9ae8fb4102272e2d511947309687b19a905e942dc02ef2981d36b` |
| `astra-capture/weather-nowcast/archive.sqlite` | `974ce4b5339b010ee28819f35f365693bfc55dd337ab0d7a192aff668714f60f` |
| `packets/VARIANTS_ACCEPT_PING_WX_FL_KXHIGH_SETTLED_TAPE_2026-10-01.json` | `2fbc2515814f844caf7311b53406d81ae548ef90f5897dc862dbf11c48d13130` |
| `packets/CONDUCTOR_ACCEPT_VARIANTS_WX_FL_KXHIGH_SETTLED_TAPE_FREEZE_2026-10-01.json` | `b5bd4f046b3a48cffc5617e5f8680a8b8d9d1688568a6fd723fd3b46a845045a` |
| `packets/CONDUCTOR_MERGE_WX_FL_KXHIGH_SETTLED_TAPE_PR63_2026-10-01.json` | `42967658ab2e4c5291790a3296d7323549bb203e6c9106a25281004a426614c2` |
| `packets/CONDUCTOR_ACCEPT_ADDENDUM_WX_FL_KXHIGH_PR63_PRE_ROI_RULINGS_2026-10-01.json` | `68e1ff7a3f170a90b74a72448809558c3ce7364e32a8b5296a1d10c3b2590153` |
| `packets/EXAMINER_SCORE_WX_FL_KXHIGH_SETTLED_TAPE_PR63_2026-10-01.json` | `3ab89d3a8a9221461fb286610fc395f9b5bd49091b538011452fcc277b13015d` |
| `packets/EXAMINER_SCORECARD_WX_FL_KXHIGH_SETTLED_TAPE_PR63_2026-10-01.md` | `81f5a9b0169f866fa34e0faa84e4c8e0aa3df41a7cdbf70115c04188d6b6fdf2` |
| `packets/EXAMINER_READY_NOT_SCORED_WX_FL_KXHIGH_SETTLED_TAPE_PR63_2026-10-01.json` | `6ffae37a9242c0a99dad138e0948c4e771fe69842d413c761b85c8e39bf55f42` |
| `packets/SIMULATOR_READY_WX_FL_KXHIGH_SETTLED_TAPE_PR63_2026-10-01.json` | `6256b69867acfa8f35e94fb2d7289ffdca3d8eb378f6359587712dccf0856bd7` |
| `packets/CONDUCTOR_SCORE_KICK_WX_FL_KXHIGH_SETTLED_TAPE_PR63_2026-10-01.json` | `e0c5203da48854d397471973b35f8d99921e469594f6554876f95cb12c6d842f` |
| `packets/CONDUCTOR_ACCEPT_EXAMINER_ITERATE_WX_FL_KXHIGH_PR63_2026-10-01.json` | `5059678525d8b91c751e931ee45fecf7c4ee9f085528fc13c18ffafcb863cd39` |
| `steward/LOSS_INVENTORY_2026-10-01.json` | `feb29c29a9d2b5e5f7c2ab85ac0a4785620f0e0df76a022a67ed40df54e6e2d1` |
| `/workspace/steward_astra_science_preserve_20261001/astra_science_dirty_133_20261001.tar` | `f91ecb6840cd76b69d00354debd54499abd960c7ac724128bcc6e7e2faeec737` |
| `astra-capture/weather-nowcast/collector.py` | `1a3166c4dad72aadf6600e17ef02d0c1b0d889eb9ecb8e84fa639f0eac2a9dff` |
| `astra-capture/weather-nowcast/supervisor.sh` | `709125337c0b22fc57a237eaac464694841e41ac20caf9aebb753a2710ed2bd4` |
| `astra-capture/weather-nowcast/R2B_PREP_2026-10-02.md` | `ae3a903609a4c5d7e331c2cdccf92d04be9760e07c31b2e5d9f650fae7c7a4e1` |
| `astra-capture/weather-nowcast/archive_r2_20261002.sqlite` | `7ee088a6f930362051fc65e0b61905833cfb7304391dda3e63974cb6909685a8` |
| `astra-capture/weather-nowcast/STOP_R2_ON_429_2026-10-02.json` | `aed6c2243b8c989cc7dade273be8a3c222eea77ed78985827b83a9f390812815` |
| `astra-capture/q6s5-kxmlbspread/settlement_only_2026-10-02/COLLECTOR_READY_SETTLEMENT_ONLY.json` | `0dd61920f8e622c336cf9ab2ac88d0d78b04d4152c93cf98cecb14550b7d924c` |
| `incidents/ADMIT1_TRUNCATION_BOX_REBUILD_2026-10-02_v2_CORRECTED.json` | `52a6b8a1378b120a241ce9c6b302ca214b0a04b7360773269293d845b8623d3d` |
| `incidents/ADMIT1_TRUNCATION_BOX_REBUILD_2026-10-02.json` | `d943c13a9d19668d870629fabd9fc0e765b7797889d379c049141e309d604163` |
| `astra-capture/prospective/ADMIT1_POST_RUN_NOTE_2026-10-02.md` | `9a2870dba116645900809026be14303b61cf53913920688197f27d94cbd43362` |
| `astra-capture/weather-nowcast/PROBE_R2C_PM_2026-10-02.json` | `8695cf037abaa4753a9e2a1d1c76fef45eea2a4d0162f1c42ee532ffa5254820` |
| `astra-capture/weather-nowcast/KALSHI_429_STOP` | `a41d074e3c0792d7870cf4158936103e5d129bac3447c8c674a80f130b529399` |
| `astra-capture/weather-nowcast/launch_r2c.sh` | `6ccf6dc6271565849c1bb61f4647e5b9dc8b5e2360b4ec7c577cc1346c0b4806` |
| `astra-capture/weather-nowcast/launch_r2d.sh` | `af0f4db3f578e75db5f1b1336b14cc0a8453daf0d51fcee856567d0fc961acc0` |
| `packets/VARIANTS_Q6S5_KXMLBSPREAD_STRATEGY_FILL_PR60_SCORABILITY_FREEZE_2026-10-02.md` | `213ee6dd33f292c8041977b0b8d7566da9412fd3debe0597643c500dc1e42db4` |
| `packets/VARIANTS_Q6S5_KXMLBSPREAD_STRATEGY_FILL_PR60_SCORABILITY_FREEZE_2026-10-02.json` | `6399ebe6687c64972d2826df8cc36772582604e7a30b60e1b890a6d7e9cb0e55` |
| `packets/Q6S5_PR60_SCORABILITY/MANIFEST.sha256` | `6e89b8098d29971070098e196347f9f75247ade83cc7ba4d79f694d55a790134` |
| `astra-science/kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/pins/Q6S5_PR60_SCORABILITY_authentic_pins_2026-10-02.tgz` | `bd94757c4c5748fc3447cf596435ddee0af129c87599d4c48f002b2b61756308` |
| `packets/VARIANTS_ARCHIVIST_REGISTRY_PING_Q6S5_PR60_SCORABILITY_2026-10-02.json` | `6353034311b5fdf26c982a6df7e8bb203a9c6554d0a6c79ba8e255543971a228` |
| `packets/CONDUCTOR_ACCEPT_VARIANTS_Q6S5_PR60_SCORABILITY_FREEZE_2026-10-02.json` | `9c6e19ca11a855015fb4e3e63cd65ae5e5c334875240e817e164e988426df9f5` |
| `packets/CONDUCTOR_MERGE_PR64_Q6S5_PR60_SCORABILITY_2026-10-02.json` | `f1bab3b2e0cc19ccf64f25ea61c030532b4f5b89965a568624c910e012ccf154` |
| `packets/SIMULATOR_READY_Q6S5_KXMLBSPREAD_PR64_SCORABILITY_SETTLED_2026-10-02.json` | `5b9de869a4f2c8ee61e5af845c3cda2e0ebf4b9ca4b4352a6d7417023ad7a9a5` |
| `packets/EXAMINER_SCORE_Q6S5_KXMLBSPREAD_PR64_SCORABILITY_2026-10-02.json` | `961f72fa76dd57867915b5321635becdc7a1f09d7d93e5147d66860fa0ea6e3e` |
| `packets/EXAMINER_SCORECARD_Q6S5_KXMLBSPREAD_PR64_SCORABILITY_2026-10-02.md` | `1f418bf73315c533cadebabfde939e0e4ea64fba01ddd7939b4185dfc49335fc` |
| `packets/CONDUCTOR_ACCEPT_EXAMINER_ITERATE_Q6S5_PR64_SCORABILITY_2026-10-02.json` | `57a9f5e68f41cf6df1428d2516ace34550267f264396d486f245977a571a871c` |
| `packets/CONDUCTOR_MERGE_PR65_DOCLAG_2026-10-02.json` | `d8f4fb5c1736a29d173a2b63a543658cdb45fcc99bf6b924b656cea2ca7a510d` |
| `packets/CONDUCTOR_MERGE_FLEET_PR1_DOCLAG_2026-10-02.json` | `c732e73f33300af9cef2cecc0a1140760b34ceb2d644797510a3375165990d66` |
| `steward/DOCLAG_PR_REGISTRY_TEXT_2026-10-02.md` | `d0c872cd65109a402ed2e5212a1a9b7e7fe9366af06ce77f60cdada5f3686a8b` |
| `steward/DIGESTS_ANNOTATION_RECORD_2026-10-02.json` | `36f97e7ec9593a2ceebd710296f9483d9935310ea433b648e64f162d0f079f6e` |
| `steward/doclag_2026-10-02/digests_annotated_reverted/C4_KXCPI_SETTLED_JOIN_HARNESS.0404abf51bcdda1742de894d2fe6ed0ae91c4b1cfd73c9af9762c3fc0eed55ab.DIGESTS.txt` | `0404abf51bcdda1742de894d2fe6ed0ae91c4b1cfd73c9af9762c3fc0eed55ab` |
| `steward/doclag_2026-10-02/digests_annotated_reverted/ATP_KXATPMATCH_SETTLED_JOIN_HARNESS.fffe42ef7d9384bafa05c9dfebaf248b4ead40c82d091c7a7d131eadd331c2ea.DIGESTS.txt` | `fffe42ef7d9384bafa05c9dfebaf248b4ead40c82d091c7a7d131eadd331c2ea` |
| `steward/doclag_2026-10-02/primary_new/README.md` (= primary@761eaaed `README.md`, blob 680b6413e621) | `a4e97325cc42d856b91cdaa618c6ea45f99668e94d7af5c55394e498cd519cc5` |
| `steward/doclag_2026-10-02/primary_new/docs/EXPERIMENT_REGISTRY.md` (= primary@761eaaed `docs/EXPERIMENT_REGISTRY.md`, blob ecaa2a548b3e) | `d1d01784ddb50629a6842f0f9055e22f087c48c28eb43ba537e135f5f47660a6` |
| `steward/doclag_2026-10-02/primary_new/docs/_prev/8ee066c3f13fe4677b9a4f7b753a57ada43d8aa81229f2ec3c83af16c1a1e30f.EXPERIMENT_REGISTRY.md` (= primary@761eaaed `docs/_prev/8ee066c3….EXPERIMENT_REGISTRY.md`, blob 0f5e8d801f3f) | `8ee066c3f13fe4677b9a4f7b753a57ada43d8aa81229f2ec3c83af16c1a1e30f` |
| `steward/doclag_2026-10-02/primary_new/kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/EXAMINER_HOLD_Q6S5_PR60_SCORABILITY_PRE_PR_2026-10-02.json` (= primary@761eaaed `kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/EXAMINER_HOLD_Q6S5_PR60_SCORABILITY_PRE_PR_2026-10-02.json`, blob 6e7ea95c3719) | `cf9ce7ca7c8bc677f70388e63cde75c49aa9a5afcdd70cc459fef451214e4880` |
| `steward/doclag_2026-10-02/primary_new/kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/_prev/ffab465a62587587b8630a994414cb1d7cd74741d56c935a81e803c2037ef6a2.EXAMINER_HOLD_Q6S5_PR60_SCORABILITY_PRE_PR_2026-10-02.json` (= primary@761eaaed `kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/_prev/ffab465a….EXAMINER_HOLD…json`, blob 47f10bcb1597) | `ffab465a62587587b8630a994414cb1d7cd74741d56c935a81e803c2037ef6a2` |
| `steward/doclag_2026-10-02/r2_primary_new/kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/README.md` (= primary@761eaaed `kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/README.md`, blob 580a110087f2) | `c9cd9b68ec32b72692a4ed959f40cbdfff42a57e54457f74ff86534a2c6e545a` |
| `steward/doclag_2026-10-02/r2_primary_new/kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/_prev/9a8bc5c6727c8abd30d83e4bfc1b9e6553aae6c449331d11b37b1bcd5ec5b83c.README.md` (= primary@761eaaed `kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/_prev/9a8bc5c6….README.md`, blob 8b625bf333c2) | `9a8bc5c6727c8abd30d83e4bfc1b9e6553aae6c449331d11b37b1bcd5ec5b83c` |
| `steward/doclag_2026-10-02/fleet_new/registry/STATUS.md` (= fleet@6db4d41a `registry/STATUS.md`, blob 371702933afd) | `efc3a8c3a3e3e6aa434507f4b545dabba0318796c7c55807568ff05dd1a27017` |
| `steward/doclag_2026-10-02/fleet_new/registry/_prev/7e22d2a95806e1797774cf0205a7b989fc671e4c3dd40ca2813d3a42efe0298a.STATUS.md` (= fleet@6db4d41a `registry/_prev/7e22d2a9….STATUS.md`, blob 7e7b33202ef0) | `7e22d2a95806e1797774cf0205a7b989fc671e4c3dd40ca2813d3a42efe0298a` |
| `steward/doclag_2026-10-02/r2_fleet_new/registry/PACKET_INDEX.md` (= fleet@6db4d41a `registry/PACKET_INDEX.md`, blob 0800c2145b33) | `0b8aa0ca5bd927b47053e9ddfa3744af4ecfedff2e94888f8ced6ff91947331c` |
| `steward/doclag_2026-10-02/r2_fleet_new/registry/_prev/92320112b06f48f60d4a8aac5e793462e70eddf52acbd58ad007b56968c880e0.PACKET_INDEX.md` (= fleet@6db4d41a `registry/_prev/92320112….PACKET_INDEX.md`, blob eaba7027cff5) | `92320112b06f48f60d4a8aac5e793462e70eddf52acbd58ad007b56968c880e0` |
| pin prior SCORE Q6S5 measured harness (reconfirmed) | `348e2981d191fda5a228ef77fc578b0821bd731ae6aa38b1b8004d9d82ba3d62` |
| pin prior ACCEPT harness ITERATE (reconfirmed) | `54b0b1b7d57d42f3a2f2d0caefd72be734532eaae8d8c54fbcb8817a7df99a71` |
| pin Q6S5 feequeue freeze (reconfirmed) | `4f65dcdf536755b9f7dc2449c2dcd90b2df74cdf99a441b676f1a71c4d709c6e` |
| pin DIGESTS C4 unchanged (reconfirmed; annotation 0404abf5 reverted 19:14:46 ET) | `a2754a8673bde8a82acb64226877e4f4d4b2d1a135f0b16d18ed7fed409083a8` |
| pin DIGESTS ATP unchanged (reconfirmed; annotation fffe42ef reverted 19:14:46 ET) | `e72add7818b65edd32ee0132104611d166934688092c23fce762db4f0a5f8745` |
| git PR59 / PR60 / PR61 / PR62 / PR63 / PR64 commits (verified) | cb8957d7 · `12e760f5bd3b622d8f0d70a74c28655464e2b93c` · `d7558fc4b92256c68eaea66b9700021206de0a2d` · `749bc1464764fda03dcddd1162177ef062b2ece3` · `f233079d9e7d2a91e2100f2085bcf85d0006e28f` · `eb33f094f3341958746f83a8f2f8c1e2c37a7d0a` |
| git PR65 squash / head (primary, connector-verified) | `761eaaedc153dca9807d7630adcea1ae3387d9c1` / `fa86a363ee071c493e86222264da626ade7c283d` |
| git fleet PR1 squash / head (connector-verified) | `6db4d41ad8eb7be94577f17f0b128d370e3116c5` / `dc859604e561b4075b12fd92e39344c8c28a88d2` |
| `cemetery/CEM-ASTRA-20261001-001_Q6S5_KXMLBSPREAD_FL_BAND_MAKER.md` | `41ccd2825c98375135a81e0ae390ecc1e8ebfd9fb94a1e6c6a9f96efade11d0c` |

Exceptions (append-only notes; no row above is rewritten):
- MISSING: `08aa54de2b47314e9d27342c1bf3824400d3c434770d339f2e3c253ee90084f6` (Q6S5 queue). Superseded by 7472b8ac per ACCEPT a5398129; never recreated.
- MISMATCH: `steward/STEWARD_CONDUCTOR_RULINGS_EXEC_2026-10-01.md` cited 7e389f32 vs disk 133302a4. Conductor append "Deletions done" (HYGIENE §11.2 → §11.3). The 7e389f32 bytes are unrestorable.
- MISSING (uncited, box rebuild): Examiner scratch `out/` JSONs PR61 (5dd5ea93, f4571074), PR62 (7f412f32, 1f5d28dd), PR63 (70c58bcc, 7317bfb2, 24e62b49). The scripts are present.
- Note on the 2026-09-25 ~02:16 trades-join rows (f707bcbd / 3dcdf2ab / 02478c87) and runner 9a52bcb7: these were absent from the astra-science clone after the Ruling-1 reset. They are restorable: stream-verified inside preserve tar `f91ecb6840cd76b69d00354debd54499abd960c7ac724128bcc6e7e2faeec737`.
- DIGESTS is NOT indexed as changed. The scout FROZEN_EXPERIMENT copies b72465d8 / 802b40b3 were intentionally not realigned.
- [I] only: DOCLAG text rev1 3c290457 / rev2 c61231b5 and DIGESTS record v-prior 2e9cf447 (no bytes on disk); the ACCEPTED status of 9a2870db (no on-disk ACCEPT).
- Scoreboard unchanged: Q6-000 / Arm D KEEP +$345.24 / +6.90%; no new KEEP.

### Cemetery (Astra Kalshi): appended 2026-10-02. All CEM entries above are unchanged and visible.

| CEM_ID | Subject | Decision | Packet |
|---|---|---|---|
| CEM-ASTRA-20261001-001 | Q6S5 KXMLBSPREAD FL-band maker thesis H1 (FL0 low band beats FL1 mid band), Sep-24 pinned universe | **KILL** (ceiling ITERATE; pre-declared contradicts_H1 rule, directional not significance; KXMLBSPREAD only; not a kill of Q6S5 / parent harness / PR58 / PR60). SCORE `2e74f17b…`, card `1bdb1d9c…`, ACCEPT `be235777…` (erratum_noted WRONG per annotation `546f62c9…`) | `cemetery/CEM-ASTRA-20261001-001_Q6S5_KXMLBSPREAD_FL_BAND_MAKER.md` |

| path | sha256 |
|---|---|
| `packets/ARCHIVIST_INDEX_BACKLOG_2026-09-25_to_2026-10-02.md` | `0e479b7f74584724200f9d61954868373a8cf7f5942db21461a2b380028ec638` |

### Appended 2026-10-03 ~17:25 ET (Archivist): KALSHI batch 2026-10-03 (items A–J) + Card 01 register repin
| path | sha256 |
|---|---|
| `packets/CONDUCTOR_ACCEPT_COLLECTOR_ADMIT1_POST_RUN_NOTE_2026-10-02.json` (ACCEPT of post-run note 9a2870db; burst profile = ADMIT spec; run 19 170 rows ABORTED_SUPERSEDED) | `6e4922d685e1d0ce6b0c6655f21cc2a9c586f0c5407db4ae23db752410293884` |
| `astra-capture/weather-nowcast/KALSHI_429_STOP` (current; recreated by r2e 429 15:17:30 ET) | `e55d6094a801131728399cefe08a1e23850f6d734c00030f625b817ccc1019ba` |
| `astra-capture/weather-nowcast/_prev/a41d074e3c0792d7870cf4158936103e5d129bac3447c8c674a80f130b529399.KALSHI_429_STOP` (r2d clear) | `a41d074e3c0792d7870cf4158936103e5d129bac3447c8c674a80f130b529399` |
| `astra-capture/weather-nowcast/_prev/abed68e79a21eab1ebf721c3ac41be99d95c61cb0676780ac0c240376ba5ba09.KALSHI_429_STOP` (r2d relaunch 429 09:20:46 ET; r2e clear) | `abed68e79a21eab1ebf721c3ac41be99d95c61cb0676780ac0c240376ba5ba09` |
| `astra-capture/weather-nowcast/_prev/e55d6094a801131728399cefe08a1e23850f6d734c00030f625b817ccc1019ba.KALSHI_429_STOP` (copy of current) | `e55d6094a801131728399cefe08a1e23850f6d734c00030f625b817ccc1019ba` |
| `astra-capture/weather-nowcast/PROBE_R2C_2026-10-03.json` | `e69561d3718570aea642334c3874d4fa8e4f3f6baec8be0ae509217e42fda19d` |
| `astra-capture/weather-nowcast/STOP_R2D_AFTER_RELAUNCH_429_2026-10-03.json` | `c9341de0bc51f0a184c708b7f4bc3e040c8590ae0b727f9ed6ce6274f33d9306` |
| `astra-capture/weather-nowcast/archive_r2d_20261003.sqlite` (ABORTED, pre_since 0; EXCLUDED) | `f58f421d8553fd9b13bd3a627dd906f934db17aa83c798b12c57d297562d5be8` |
| `astra-capture/weather-nowcast/launch_r2e.sh` | `c168ca1d9c3d14f7350263bf22514a1baf390a670ce1f276030ce9da0137f812` |
| `astra-capture/weather-nowcast/PROBE_R2E_2026-10-03.json` | `fe615c47fbe12694de7a20f7aafd106901378f05d5bb2af9fbe10fa1292ce813` |
| `astra-capture/weather-nowcast/STOP_R2E_AFTER_RELAUNCH_429_2026-10-03.json` (LAST box-IP attempt) | `b33ada1c68ba7572a0ff88c9cfb710cf56bb8cc12818bf1b5a1d18162ff4b1b0` |
| `astra-capture/weather-nowcast/archive_r2e_20261003.sqlite` (post-run; ABORTED; EXCLUDED like r2b/r2d) | `181977c23e658647f6610d1ce455c66634ef345bcbd1ff2a960ca077498bbb94` |
| pin weather archive.sqlite frozen (reconfirmed) | `974ce4b5339b010ee28819f35f365693bfc55dd337ab0d7a192aff668714f60f` |
| pin launch_r2d.sh unchanged (reconfirmed) | `af0f4db3f578e75db5f1b1336b14cc0a8453daf0d51fcee856567d0fc961acc0` |
| `packets/VARIANTS_EXT_K1_Q6000_LEGGING_RISK_AUDIT_FREEZE_2026-10-03.md` (AWAITING Conductor ACCEPT per brief; DESCRIPTIVE/ITERATE/INCONCLUSIVE; dev-grade 31 games) | `5c40fb9d03a924e40577a81f262231701e331c98922f60f6dc7ab65a2dbed6d3` |
| `packets/VARIANTS_EXT_K1_Q6000_LEGGING_RISK_AUDIT_FREEZE_2026-10-03.json` | `be3e88336389bc62c40413785e6ffb4a572e1dbd006d7cf3dfbc962f8184efaa` |
| `packets/EXT_K1_LEGGING_AUDIT/MANIFEST.sha256` (9/9 OK) | `5e8f79063f132fe2db97ad3ecff5fea463d429f167abed09c58398a87fcadf01` |
| `/workspace/EXT_K1_authentic_pins_2026-10-03.tgz` (38 files; parts 3fd70f7b + 1f8b2ac1; PARTS a92df01d) | `0f8f529733bfd1ccb01b36f312cdc20865cc2811c04dcd3c812d50c67295db38` |
| `packets/CONDUCTOR_RULING_SCOUT_EXTERNAL_HUNT_2026-10-03.json` (issued_et 16:10 vs mtime 16:06:39 ET: clerical, Conductor-confirmed) | `870895a58e80fd1442d0ce97e42df02426bf7e38f64dcd091efc6fbf26b74ebf` |
| `governance/astra/SCOUT_EXTERNAL_HUNT_2026-10-03.md` (scout brief; prev bfb1b7f3 in `_prev/`) | `13e442892d27466f3ee3082509a47ac9706c7f3448aa079de798bec8cb1a1dfb` |
| `packets/VARIANTS_EXT_K2_OPTIMISM_TAX_DEPENDENCE_STRESS_FREEZE_2026-10-03.md` (AWAITING Conductor ACCEPT per brief) | `d69a4f627cb420b59bbc961b072d28242faeb9d21d5d29b9f90a77f6825acbce` |
| `packets/VARIANTS_EXT_K2_OPTIMISM_TAX_DEPENDENCE_STRESS_FREEZE_2026-10-03.json` | `025a01a121e5b3a64a0b683a8030f9cbd1681f132365dadb419377d09d71ff6c` |
| `packets/EXT_K2_OPTIMISM_TAX/MANIFEST.sha256` (11/11 OK) | `3478b4058681992109142bcde3ff87bd91c7e523092ba367d96d18afae693fe5` |
| `/workspace/EXT_K2_authentic_pins_2026-10-03.tgz` (cloud bundle; 0 Becker bytes) | `963f7663a74527db38479bbf4a253870bd5dc6f99c8f85b70750d3600c65907f` |
| `astra-capture/external/ext_k2_becker_boxonly_2026-10-03/BECKER_BOXONLY_PIN_MANIFEST.json` (license [U]; box-only) | `fd5e10531f488f30baf05e2dd6f17c8f8823603ecbae457170dbbde66126fb95` |
| `packets/CONDUCTOR_COMMISSION_EXT_K2_2026-10-03.json` | `1f2c7f68396131d65ef31e492355c2937a9a0a91fb6cdf67c7d66e220f0b51f5` |
| `packets/CLOCK_PROVENANCE_BECKER_ARCHIVE_2026-10-03.md` (embedded support) | `e7424a130e95b72d288d567ef75b00804672b29b15bd93889aafb0722fd84d80` |
| `packets/CLOCK_PROVENANCE_BECKER_ARCHIVE_2026-10-03.json` (embedded support) | `dc54e3dae4bbeeffc0e1c792bd769a2d63daee02a974dbff03d04da8780eebc3` |
| `packets/ADVERSARY_EXT_K1_PRESCORE_REVIEW_2026-10-03.md` (verdict CLEAR) | `676ba2faf0d877fa2f06dc4f2b247b9c7541188c0f9c7de17a622e6502eac130` |
| `governance/astra/ADVERSARY_RISK_REGISTER_2026-09-22.md` (30eb735a → 537408cc → 1aecfd36) | `1aecfd366f8f9024be0f1393903812439a448ea5bf5585e4d21616874b1beab9` |
| `governance/astra/_prev/30eb735a5926206b19547151b4cf8bd331761efe4590eceb19441894c70e275e.ADVERSARY_RISK_REGISTER_2026-09-22.md` | `30eb735a5926206b19547151b4cf8bd331761efe4590eceb19441894c70e275e` |
| `packets/ADVERSARY_CARD01_AMENDMENT_B_REVIEW_2026-10-03.md` (ADVISORY_FLAGS) | `271ec099481ca35a57e4605b28abeff78d2660b6fd2657044666d45bcb728f01` |
| `packets/card01_hybrid_forecast/MANIFEST.md` (current; prior 16f96d3d UNVERIFIED_BYTES_MISSING per AF-9 ruling) | `f22df25bdebd300bfa51f557c940270212475edce6371b2ccaefb4204ce9e427` |
| `packets/CARD01_HOUSE_ONLY_PROSPECTIVE_FREEZE_2026-09-24_AMENDMENT_C.md` (**PENDING**, not accepted, per brief; answers 271ec099; parent B ee6af37c reconfirmed) | `cc75f09614ad285756fd7cb7f7a5c2ce4e711b5adb98102c2dd043ccfc1af0f0` |
| `packets/CARD01_NEGLECTED_HYBRID_DECISION_PACKET_2026-09-24.md` CANONICAL (was c0c1aa66; docs-only edit verified by diff; REPIN of L337) | `d66c9eaf2988bf081fea3096d7052c20def651e813ec29f13906a626effe81ef` |
| `packets/_prev/c0c1aa66f104e3f102228a7a8e16f205977afbee63928f30a6954ec46707a82c.CARD01_NEGLECTED_HYBRID_DECISION_PACKET_2026-09-24.md` | `c0c1aa66f104e3f102228a7a8e16f205977afbee63928f30a6954ec46707a82c` |
| `packets/_prev/ebdaea019fc119d29f96bd04095d64eb60d99ade1a3206d441b94b422431ef25.CARD01_NEGLECTED_HYBRID_DECISION_PACKET_2026-09-24.md` (transient; superseded) | `ebdaea019fc119d29f96bd04095d64eb60d99ade1a3206d441b94b422431ef25` |
| `packets/card01_hybrid_forecast/FROZEN_EXPERIMENT.json` (repinned in place: decision_packet_sha256_current c0c1aa66 → d66c9eaf; was 44cb582f) | `8b716ef0ee2ed2daa5f533681ea6e4c77767094fd95e611b681f9f2807ef855c` |
| `packets/card01_hybrid_forecast/_prev/44cb582fd6f4612574d1a0b58b2d4f24cdf421eddc61e32a681663bf1b16c910.FROZEN_EXPERIMENT.json` | `44cb582fd6f4612574d1a0b58b2d4f24cdf421eddc61e32a681663bf1b16c910` |
| `packets/card01_hybrid_forecast/LEDGER_2026-09-24.md` (repin row RP1 appended; was d8ddfda7) | `ee9d12f75756cebd95e162bccc6ed50eecabff880bf40e7e555df4dcbbca1414` |
| `packets/card01_hybrid_forecast/_prev/d8ddfda72bdc6aaedd5627c78da99d6f360c48746b16c662d7ae3263a3d14fe1.LEDGER_2026-09-24.md` | `d8ddfda72bdc6aaedd5627c78da99d6f360c48746b16c662d7ae3263a3d14fe1` |
| `astra-capture/card01-nh002-house/ELECTINDEX_GAP_2026-09-27_to_2026-10-03_UNMONITORED.json` (UNMONITORED; never backfill) | `38d36b73336d2031204f79dae700f9f79d29eeb490863f491ea6b35dc215b221` |
| `astra-capture/card01-nh002-house/ELECTINDEX_CAPTURE_RESTORE_2026-10-03.md` | `9cdca1301f4dc40846834fea3a92dacfe389790b604b0a966a1e9ed82e8134d9` |
| `astra-capture/card01-nh002-house/METHODOLOGY_CHANGED_2026-10-03.flag.json` | `3e585f84fa5ba2c56748af6a02f539f61a45cac865a33035a2afe63efcc4da6e` |
| `astra-capture/card01-nh002-house/_prev/41d67d400c75630f33f21c8e2b1810dc7a138f6d2be65e33d7e43dfb8aac86b3.run_daily.py` (runner of the 2026-10-03 17:13 ET capture; live file now 4f0854e5, MISMATCH, not indexed as conforming) | `41d67d400c75630f33f21c8e2b1810dc7a138f6d2be65e33d7e43dfb8aac86b3` |
| `(private) evidence_private/electindex/card01-nh002-house/2026-10-03/races_summary.csv` | `4713b5c44ca5f6db6080a55e0843210d953a45ba53e727408c9e4d93eb82fdf9` |
| `(private) evidence_private/electindex/methodology/2026-10-03.html` | `255acb38163549a5ad0709e859f0f1e8a81b6ac506931241658c1e6e7fef0a31` |
| `(private) evidence_private/electindex/methodology_asset/2026-09-26_to_2026-10-03_eifc-info.js.diff` | `efb53b1f07202c78589a95632e267d57b423c434f0dacf55ee8f1943c198ea3f` |
| `(private) evidence_private/electindex/methodology_asset/2026-10-03_eifc-info.js` (methodology regime **R1**, first seen 2026-10-03T21:13:06Z; R0 = caaff53e) | `82b09d7c845c9d04c23d30e2a27441aaaf66606c98558e618a34db7201ac66cd` |

Exceptions and notes (append-only; no row above is rewritten):
- MISMATCH: `astra-capture/card01-nh002-house/run_daily.py` cited 41d67d40 vs disk `4f0854e56265e10b2505a9f371260caa6eaddb57726244a4435e1a424a54d5c8` (edited 17:15:37 ET; re-adds the README GET, which conflicts with the ruling OPTIONAL_NOT_CAPTURED; endpoint is within the Amendment 03 pin). Old bytes are in `_prev`. A Conductor/Archivist decision is needed.
- MISSING: risk register intermediate `537408cc` has no `_prev` (register not frozen; recorded, no rule breach).
- UNVERIFIED_BYTES_MISSING (AF-9, Conductor ruling, index file, low materiality): `packets/card01_hybrid_forecast/MANIFEST.md` prior `16f96d3d4e11e3e17eb0a76a8e4cdcbe097773d8b34cdaf50faf9c0de85b7d18` → current f22df25b.
- RESOLVED (per Conductor via dispatcher [I]): `steward/STEWARD_CONDUCTOR_RULINGS_EXEC_2026-10-01.md` is current at 133302a4. The 7e389f32 bytes are unrestorable and that is accepted. The 7 lost Examiner scratch outputs (PR61 ×2, PR62 ×2, PR63 ×3) are accepted. This closes the 2026-10-02 MISMATCH and MISSING-scratch exceptions above as RESOLVED_ACCEPTED.
- RESOLVED: the ACCEPTED status of 9a2870db is now [V] via 6e4922d6, which closes the 2026-10-02 [I] note.
- REPIN of L337: the decision packet c0c1aa66 → d66c9eaf. The earlier rows that pin c0c1aa66 (L337 and other seats' packets) pin the pre-edit bytes, which are preserved in `packets/_prev/`. LEDGER_HASH_REGISTER_EXTRACT (Steward point-in-time public anchor, 03f9c193) was not repinned.
- ElectIndex: scheduler pid 453207 is gone (ps rc 1) and `electindex_scheduler.sh` is RETIRED, not restarted. The capture now runs as a server-side daily routine at 20:17 UTC. Gap 2026-09-27..2026-10-03 is UNMONITORED and gap snapshots are regime UNATTRIBUTED. The change time is unattributable: after the last R0 capture on 2026-09-26, and no later than 2026-10-03T21:13:06Z. Server Last-Modified 10-02 13:36 ET is [U] and is not the boundary. Card 01 stays frozen, and Amendment B (b) sensitivity rows (i)/(ii) apply at decision. The README fetch is OPTIONAL_NOT_CAPTURED from 2026-10-03. The Monday terms/robots check is kept.
- Seen, not indexed: Conductor ACCEPTs on disk for EXT-K1 (`02129007…`), EXT-K2 (`d76779e1…`) and Card01 Amendment C (`2225c3fa…`). They conflict with the brief's AWAITING/PENDING status and are held for confirmation.
- Scoreboard unchanged: Q6-000 / Arm D KEEP +$345.24 / +6.90%; no new KEEP.

| path | sha256 |
|---|---|
| `packets/ARCHIVIST_INDEX_BATCH_2026-10-03.md` | `dabc41ff55cdec5629dcc306769862b276e0e80d0d3fa3756c40181fbfb17b1a` |

### Appended 2026-10-03 ~17:23 ET (Archivist): corrections per Archivist rulings + related-packet batch (append-only; no earlier row rewritten)

| path | sha256 |
|---|---|
| `packets/CONDUCTOR_ACCEPT_EXT_K1_FREEZE_2026-10-03.json` **ACCEPTED** (issued 16:16:49 ET; pins freeze 5c40fb9d OK, json be3e8833, manifest 5e8f7906, bundle 0f8f5297 OK) | `021290077cbbed277455145d2e56e1335f6ae331d56c2ad79d4d85b405559397` |
| `packets/CONDUCTOR_ACCEPT_EXT_K2_FREEZE_2026-10-03.json` **ACCEPTED** (issued 16:50:38 ET; pins freeze d69a4f62 OK, json 025a01a1, manifest 3478b405, cloud 963f7663, becker fd5e1053 OK) | `d76779e1a309388e6bc7f401a2c992a3be2015ae81ba910b8f5655fb10472fc0` |
| `packets/CONDUCTOR_ACCEPT_CARD01_AMENDMENT_C_2026-10-03.json` **ACCEPTED** (issued 17:14:08 ET; pins amendment cc75f096 OK, Amendment B ee6af37c, adversary 271ec099, script 049368f9 OK) | `2225c3fa0bea7c58cad59f52476f9fbe69e1d6fa813114a7557c748126dd2b1a` |
| `astra-capture/card01-nh002-house/run_daily.py` **CURRENT runner** (README re-add accepted; authority [I] Conductor msg 2026-10-03 17:09 ET, no packet at ruling; endpoint check PASS, 6/6 pinned) | `4f0854e56265e10b2505a9f371260caa6eaddb57726244a4435e1a424a54d5c8` |
| `packets/CONDUCTOR_KICK_ADVERSARY_EXT_K1_PR66_DESCRIPTIVE_2026-10-03.json` | `113c111ad6e1bc02d0ff413945f5364038bf8cc4d4128be542a7ac3ed4beab7b` |
| `packets/CONDUCTOR_KICK_COLLECTOR_WEATHER_R2E_GATE_2026-10-03.json` | `18ed1592ff92d302d198bae25a962ca84ffd5c9bff3fe0dbaac586b5f414c046` |
| `packets/CONDUCTOR_KICK_SCOUT_EXTERNAL_HUNT_WHILE_BOX_IP_CLOSED_2026-10-03.json` | `9c583e82aec1c5d622f222875c19c1edc5f4c11de4908fe32f503494aa7f60c9` |
| `packets/CONDUCTOR_KICK_VARIANTS_CLOUD_EXT_K2_LAUNCH_2026-10-03.json` | `c8e4ff43f86cdb0f04d08f0e89cbed68c657fc637ccae40ac6ad9a02773f4292` |
| `packets/CONDUCTOR_MERGE_PR66_EXT_K1_2026-10-03.json` | `9de0933b8ec8ade5cbb89d5372116fb76048e30007af1b8f0e09f17fbae28deb` |
| `packets/CONDUCTOR_PIN_GV2_SYNC_V3_2_REV5_2026-10-03.json` | `c2bb096113a62cfb84c9574437b2a9d957921fd6266d8ea7f4b1f977298c6157` |
| `packets/CONDUCTOR_PIN_GV2_SYNC_V3_2_REV6_2026-10-03.json` | `9f30783437172fd3c6ebeee9a535bd0c0089f07fbe54725f1b4024b1eaf9cb34` |
| `packets/CONDUCTOR_RULING_EXT_K1_N6_UNDEFINED_DELTA_2026-10-03.json` | `0b68c4bf218e7f85fa8af760ebcf5424d4e77262e62a5d71c43e9a5d2b929291` |
| `packets/CONDUCTOR_RULING_GV2_SYNC_PAUSE_AFTER_1050_DRIFT_2026-10-03.json` | `f195d558e3e1aace911ac191f7ab778d761e1e174d575f4210e4b62cef474467` |
| `packets/CONDUCTOR_RULING_WEATHER_BOX_IP_CLOSED_AFTER_R2E_429_2026-10-03.json` | `dd1d70396472a72fce2bad5233ba0190f5df4c14568d9b7746bf282ef892b2dc` |
| `packets/CONDUCTOR_RULING_WEATHER_SILENCE_AFTER_R2D_429_2026-10-03.json` | `8c90e6577559001a9c7b41bf17f14a6fe2058bd9c93af02e10f2dc36d0a08414` |
| `packets/CONDUCTOR_SUPERSEDE_PAUSE_GV2_SYNC_2026-10-03.json` | `e69d1de87871ea58611122e87fb8f13bacd56bc7e191acff2e05b794984ac12b` |
| `packets/MAXIMIZE_PIN_2026-10-02_2050ET.json` | `465fcc79ff467251340f582c6fe48a02574dce327184fc950435e5643d251ee8` |
| `packets/MAXIMIZE_PIN_2026-10-02_2050ET.md` | `f155239046891b2e6435fa634efaefc979717357201057f2021a4578a894a14b` |
| `packets/MAXIMIZE_PIN_2026-10-02_2150ET.json` | `6b9bfbbeabf73908d2fc9e8d4fe53a414d67a3f8811ff34f356cf3d5b9755a3e` |
| `packets/MAXIMIZE_PIN_2026-10-02_2150ET.md` | `bbfd929159e6e3dcab3f084f8e31b22790e5a59edfa9dbca7275b2241f604181` |
| `packets/MAXIMIZE_PIN_2026-10-03_0848ET.json` | `064d6ca81b405ed6c8a46868ee0742ae235a128b113b0c43abdfa1f1501d438b` |
| `packets/MAXIMIZE_PIN_2026-10-03_0848ET.md` | `89f709b0596ccfdfafc0d54a9d9ec9d6dd688467c72eaffec60f5d53786a417d` |
| `packets/MAXIMIZE_PIN_2026-10-03_0946ET.json` | `fa96ef06463e11c55f8e0b5205f4f34159ae6cc6ae2a9293df34942909f679ce` |
| `packets/MAXIMIZE_PIN_2026-10-03_0946ET.md` | `0d672912a81dbf72b2ea58b653720b824d99c2782987011f64dbd9672dac9432` |
| `packets/MAXIMIZE_PIN_2026-10-03_1055ET.json` | `6db6b4eef15cb9326fe94b1d2299252d36f9bcabdc261220f9c422181e3777c5` |
| `packets/MAXIMIZE_PIN_2026-10-03_1055ET.md` | `b0ea1c71c1dab72dd47308e95103a6ca4ddbda99135d4951b4f627187fe95074` |
| `packets/MAXIMIZE_PIN_2026-10-03_1145ET.json` | `8a4e2d0a5511e12416a2158a746112ba010f08a57d36e900e8a47978fa1f724c` |
| `packets/MAXIMIZE_PIN_2026-10-03_1145ET.md` | `64fd51c04e153a3d0c6dcb73914acdb22d65ecafa53712c329ca434ba8f94163` |
| `packets/MAXIMIZE_PIN_2026-10-03_1246ET.json` | `258a957efa10bcf53e4cbf0fb24a2088d3cbe2531259cc7fbcaac4de7a05e683` |
| `packets/MAXIMIZE_PIN_2026-10-03_1246ET.md` | `71de4e3b27acc552c870da77460b18428e2473e979e68e87e40dc5d85b5f6f78` |
| `packets/MAXIMIZE_PIN_2026-10-03_1351ET.json` | `49606cb4b436b1b842d603ab24b5fa23e31bc5431c5a57af6358abd5bce38097` |
| `packets/MAXIMIZE_PIN_2026-10-03_1351ET.md` | `f90fafb8efaadbe5daa3a860b6390ce19756217f9436b5c7f3ec64d13828e4d6` |
| `packets/MAXIMIZE_PIN_2026-10-03_1453ET.json` | `ef299576c93e439fcf5f224098a647f4d35d9847d56a6b3ba95ef262b18d0b7a` |
| `packets/MAXIMIZE_PIN_2026-10-03_1453ET.md` | `a82d523bc364f892043753ae572eedcc2e3fe901e908c031c2b5d6c92db4307a` |
| `packets/MAXIMIZE_PIN_2026-10-03_1551ET.json` | `ccf32b36ddb9487adcbe0b172d976abb5261b0c95a08fe516088e9138e8a25f7` |
| `packets/MAXIMIZE_PIN_2026-10-03_1551ET.md` | `f48e1e77b4fa455eef36fdd6f5720545878207623ce37b73c01c5870ab9db632` |
| `packets/MAXIMIZE_PIN_2026-10-03_1655ET.json` | `079fb999af49f39bb2848678ab64aa465888a5e18065d3859edd780d3fb24176` |
| `packets/MAXIMIZE_PIN_2026-10-03_1655ET.md` | `7dba2e3c2cc7370849dd356ab0ef03492d9c1173bf8c39115ef3ee61c4e6cc91` |
| `packets/MERGE_GV2_PR2_COMBINED_BYTE_EXACT_2026-10-03.json` | `10a3c5634f5980cda52614c63e42fbb5769fa2c93dfed195ff74594b8f8dbc21` |
| `packets/MERGE_GV2_PR3_DELETE_STATUS_JSON_2026-10-03.json` | `62890c50f8add9dcd941e5374bb6778c49307024c0332f8f1e48f65c774f1324` |

Correction rows (each supersedes the earlier note it names; the earlier rows stay as written):
- CORRECTION (round-1 note "Seen, not indexed: Conductor ACCEPTs…"): EXT-K1 `02129007…`, EXT-K2 `d76779e1…` and Card01 Amendment C `2225c3fa…` → **ACCEPTED** [V]. The Archivist ruled them real Conductor stamps that were issued before the FYIs (the brief was stale). Embedded pins match the indexed shas 5c40fb9d / d69a4f62 / cc75f096. 0 mismatch.
- CORRECTION (round-1 MISMATCH on run_daily.py): `4f0854e5…` is the **CURRENT** runner, authority **[I]** (Conductor message 2026-10-03 17:09 ET; no packet on disk at ruling). `41d67d40…` (preserved at `_prev/`, self-hash OK) is the runner that made the 2026-10-03 17:13 ET capture. MISMATCH → RESOLVED by ruling.
- CORRECTION (round-1 ElectIndex note "README fetch is OPTIONAL_NOT_CAPTURED from 10-03"): OPTIONAL_NOT_CAPTURED applies **only to the 2026-10-03 capture**. README capture resumes from the next daily run under its own `METHODOLOGY_CHANGED_README` flag. Endpoint set of 4f0854e5 = forecasts/, eifc-info.js, README and races_summary.csv on raw.githubusercontent.com ElectIndex/26_us_forecast_data, terms-of-service (Mon), robots.txt (Mon). No `-L`. Kalshi hosts refused.
- NOTE (FROZEN_EXPERIMENT `8b716ef0…`): the `decision_packet_lineage` list still ends at c0c1aa66 and is left as is. **The current pin is the `decision_packet_sha256_current` field = d66c9eaf.** The file was not edited again.
- Related-packet batch: 36 rows above, 36 [V] / 0 MISMATCH / 0 MISSING. Embedded pins resolve, including GV2 commits b361017c / 785c99ff / c19b9232 / 25f23a24, PR66 merge 09b56273, and oversize bundles 5cd0595c / efe55738. The v3.2 prompt frozen-edit chain 4efc4caa → fce33b3b → 5d1889f6 has `_prev` OK. Clerical issued-vs-mtime skews (≤3 min) are recorded in the receipt §C4. Duplicate skipped: `CONDUCTOR_RULING_SCOUT_EXTERNAL_HUNT_2026-10-03.json` 870895a5 (already indexed).
- Seen, not indexed (after ruling; outside scope): `CONDUCTOR_RULING_ELECTINDEX_README_READD_2026-10-03.json` `20605d1a…` (17:20:33 ET; agrees with the run_daily correction), Examiner EXT-K1 READY `49011265…`, SCORE `0e5b1060…` (DESCRIPTIVE), SCORECARD `b5e08bf8…`, and `CONDUCTOR_ACCEPT_EXAMINER_SCORE_EXT_K1_2026-10-03.json` `530cca94…` (DESCRIPTIVE; no change to Q6-000 KEEP).
- Receipt `packets/ARCHIVIST_INDEX_BATCH_2026-10-03.md`: pre-correction `dabc41ff…` → post-correction (Corrections section appended) row below.
- Scoreboard unchanged: Q6-000 / Arm D KEEP +$345.24 / +6.90%. No new KEEP, KILL or CEM.

| path | sha256 |
|---|---|
| `packets/ARCHIVIST_INDEX_BATCH_2026-10-03.md` (post-correction; was dabc41ff) | `e19d217888499cebbbed0c6a9075f890e3edf85bf8815efbf6a9768d02ded468` |

### Appended 2026-10-03 ~17:25 ET (Archivist): run_daily authority upgrade + EXT-K1 score chain (append-only; no earlier row rewritten)

| path | sha256 |
|---|---|
| `packets/CONDUCTOR_RULING_ELECTINDEX_README_READD_2026-10-03.json` (issued 17:20:33 ET; runner_current 4f0854e5, capture 41d67d40 in _prev; Adversary R1 display-only, Card01 stays frozen) | `20605d1afbab593876a6d7114d8dbb23ba6b412561a9f6b06f5c7641995d9a22` |
| `packets/EXAMINER_READY_NOT_SCORED_EXT_K1_Q6000_LEGGING_AUDIT_PR66_2026-10-03.json` | `490112654a87699ea33bc60a60c05954428ecc41d0a31ac54556e89e3971b00f` |
| `packets/EXAMINER_SCORE_EXT_K1_Q6000_LEGGING_AUDIT_PR66_2026-10-03.json` (verdict DESCRIPTIVE) | `0e5b10605798b45d69fde326e06fa1b9be52642dd4c64b28f79657b4d68edd5b` |
| `packets/EXAMINER_SCORECARD_EXT_K1_Q6000_LEGGING_AUDIT_PR66_2026-10-03.md` | `b5e08bf8088a973c0f9919834b03593d8dc850cb9d875ba352fd9d9bec9a5958` |
| `packets/CONDUCTOR_ACCEPT_EXAMINER_SCORE_EXT_K1_2026-10-03.json` (DESCRIPTIVE; "no change to Q6-000 KEEP; no gate adoption") | `530cca949ba4246602c853467bce5a7450be57e8e2815dba1590235d4e6a0fd5` |
| `/workspace/v66/REPORT.md` (EXT-K1 run record per ACCEPT_SCORE; Variants box verify PASS-with-notes) | `f3552b58d571be2147024e94e666831e036cb11f199214c53d0c6750b978c4d0` |

Correction rows and notes:
- CORRECTION (previous section's run_daily.py CURRENT row, authority [I]): authority of `astra-capture/card01-nh002-house/run_daily.py` `4f0854e5…` → **[V]**, citing `packets/CONDUCTOR_RULING_ELECTINDEX_README_READD_2026-10-03.json` `20605d1a…`. Its message time is given as "17:1x EDT", consistent with the 17:09 ET cited in run_daily line 4.
- Adversary R1 ruling, verbatim from 20605d1a: "Adversary: R0 caaff53e -> R1 82b09d7c display-only; named seats outside 92-race universe; Card01 stays frozen; gap labeled CHANGED_IN_GAP".
- CORRECTION (previous section's "Seen, not indexed" note for 20605d1a / 49011265 / 0e5b1060 / b5e08bf8 / 530cca94): these are now indexed above. 6 rows, 6 [V] / 0 MISMATCH / 0 MISSING; all embedded pins resolve (receipt §D2). No frozen edits, no `_prev` needed.
- Cross-ref: `packets/ADVERSARY_EXT_K1_PRESCORE_REVIEW_2026-10-03.md` `676ba2fa…` (CLEAR) was already indexed; it re-hashes OK. No duplicate row.
- EXT-K1 PR66 = DESCRIPTIVE (not a KEEP or KILL; no CEM). Scoreboard unchanged: Q6-000 / Arm D KEEP +$345.24 / +6.90%.

| path | sha256 |
|---|---|
| `packets/ARCHIVIST_INDEX_BATCH_2026-10-03.md` (post-section-D; was e19d2178) | `7dc1d6b97aa92b1e8338be914f19e6c9a97d44e151ccf9aa207787285837b05d` |
