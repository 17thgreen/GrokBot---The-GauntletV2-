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
