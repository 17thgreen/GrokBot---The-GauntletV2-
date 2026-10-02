# Study class labels — Astra / Kalshi registry — 2026-09-24 (ET)

**Owner:** The Archivist (Registry) · **Task:** Conductor step-0 record repair (`packets/CONDUCTOR_ROUTING_KALSHI_EDGE_RESEARCH_2026-09-24.md`)  
**Class vocabulary (exact, lowercase):** `unit-only` · `synthetic` · `historical replay` · `prospective shadow` · `live` — as written on research PDF p16 ("Mark each study as unit-only, synthetic, historical replay, prospective shadow or live."), matching Examiner v1.1 `study_label_source.used` = "PDF p16 five classes (unit-only, synthetic, historical replay, prospective shadow, live)" (`packets/EXAMINER_KALSHI_SCORECARD_TEMPLATE_REVISION_v1.1_2026-09-24.json`, sha256 `f2ce985d8e2a85d63336bbbb36b6e9f924959e06fad68060ae17850c178c6cfd`).  
**Definitions (Conductor):** unit-only = harness/code with tests only, no data run · synthetic = generated/simulated data · historical replay = captured historical venue data · prospective shadow = frozen-before-outcome, recorded forward, no orders · live = real orders.  
**Rule applied:** label by what has been *evidenced so far*; a harness whose run is in flight stays `unit-only` until an Examiner-scored run exists. Status and results are copied as recorded — never edited. Tags: [V] verified on disk/GitHub · [I] inferred · [U] unknown. Merge SHAs verified via GitHub `list_pull_requests` (state=all) and confirmed on main history; freeze SHAs = sha256 of the on-disk freeze packet (all Conductor-quoted prefixes matched).

## Counts

| Class | Count |
|---|---|
| unit-only | 61 |
| synthetic | 0 |
| historical replay | 17 |
| prospective shadow | 5 |
| live | 0 |
| **total lines** | 83 |

`live` = **0**: no evidence of real-money orders found (scoped grep; the only order script is R3-P2 `run_trade_step_series.py` against the **demo** host). `synthetic` = 0: no line is evidenced as a run on generated data (unit fixtures counted under unit-only). Of the unit-only lines, 8 are NON_STUDY governance/triage lines flagged CLASS_FIT_POOR. The 4 new cemetery lines (bottom section) are counted separately: all 4 historical replay.

## Table

| Registry id | PR | Merge sha | Lab path | Freeze sha | Class | Status as recorded | Results/PnL as recorded | Tag | Notes |
|---|---|---|---|---|---|---|---|---|---|
| K1 | — | — | lab/astra-kits/ | — | unit-only | Custody open | n/a | [V] | NON_STUDY / CLASS_FIT_POOR (custody packet) |
| R1 | — | — | governance/astra/briefs/R1_* | — | unit-only | TRIAGED | n/a | [V] | NON_STUDY / CLASS_FIT_POOR |
| B0 | — | — | — | — | unit-only | Not started | n/a | [V] | NON_STUDY / CLASS_FIT_POOR |
| ADMIT-1 | — | — | lab/astra-capture/prospective/capture.sqlite | admitted_at 2026-09-22T21:18:13Z · panel 2026-09-22.1-kalshi-occurrence-sot | prospective shadow | LIVE (recorder live) | no PnL · no orders | [V] | "LIVE" = GET-only recorder running; prospective shadow capture, no orders |
| PITCLE-ID-LAG | — | — | lab/astra-capture/prospective/pitcle_holdout_identity_join_2026-09-23.json | freeze pkt sha256 f5ca19f15940a80476d1590e506951df87df619160b477f1dff06cc3554cb520 · holdout f8f6b577… · receipt 72e6b1ed… | prospective shadow | JOINED / HASH_FROZEN (REG-PITCLE-HOLDOUT-ID-JOIN-20260923) | no PnL | [V] | identity join supporting ADMIT-1 prospective holdout; not a re-admit |
| Q6-000-HYGIENE | — | — | packets/Q6_000_COMPLACENCY_SPOTCHECK_2026-09-22.md | — | historical replay | HYGIENE · no verdict change | no PnL | [V] | review of historical-replay incumbent; CLASS_FIT_POOR (review, not a run) |
| R2-P5 (schema) | — | — | registry/schemas/r2_p5_admit_fields.schema.json | REG-R2-P5-SCHEMA-20260922 | unit-only | SCHEMA_ACCEPTED | n/a | [V] | schema only |
| R2-P1 | PR6 | 25ec05381207252abb8abec8f6f99e30765f9704 | astra-science/kalshi_r2p1_hygiene_000_lab_20260922/ | ddcd4427f67fb0ed8d12a7a6a49aabea3b25b356bcb64a7d84d5c4590d08b563 | unit-only | CANONICAL · SOURCE_FROZEN_BEFORE_RESULTS | scorecard/pnl null | [V] |  |
| fee_sensitivity_000_r1p1 | — | — | packets/fee_sensitivity_000_r1p1/ | 467bbfcb73dad437de8a153177ac97aab4fe2cdd3adeb7f1ffcc15983ddf5e0b | unit-only | SUPERSEDED→R2-P1 | null | [V] | kept visible |
| S1 | — | — | packets/S1_KXMLBGAME_PANEL_STUB_2026-09-22.json | 58a0c20182a075ba339629f94451fb65b7876d635ecdd51338d1c2dd852279c5 | unit-only | PANEL_STUB_ACCEPTED · capture idle | no PnL | [V] |  |
| C1-KXUFCFIGHT (panel) | — | — | lab/astra-capture/c1-kxufcfight/ | kernel a191c9b3f71030445d1d32684feb6dc1bf09abb7e09403d5dbdf1927eafc63c9 · panel sha256 24426d804c51bde23cf2557a11a8481a12026da10024094c4ae546d1f7d3956e | historical replay | ADMITTED 2026-09-23T00:49:43Z | results/pnl null | [V] | FLAG CLASS_FIT_POOR: registry treats as admitted measurement panel; panel JSON records both legs already finalized at admit → captured data is post-outcome, so not prospective shadow |
| C3-KXHIGHNY (stub) | — | — | packets/C3_KXHIGHNY_PANEL_STUB_2026-09-22.json | kernel 0e79a0194e2371efae8d8cac0f4f2ec9ce4cf53f60dd870bae1a1ed7acff3604 | unit-only | STUB · not admitted | null | [V] |  |
| C5-KXBTC15M (stub) | — | — | packets/C5_KXBTC15M_PANEL_STUB_2026-09-22.json | kernel 4d1b72a38603de181e71f80b3cc6515b170a2bffe11f8770dac1296373e50263 | unit-only | STUB · not admitted | null | [V] |  |
| C1 recorder | PR1 | cb6223989afaf9e2f2fde8516e5ce16098ef7160 | astra-science/nfl_prospective_recorder_20260922/ | — | prospective shadow | MERGED · ADMIT-1 LIVE | n/a | [V] | GET-only |
| Q7 paircheck | PR2 | a85bfdab0cd7e3b4fcb3d4a5c89cf8627be85bd2 | astra-science/nfl_paircheck_lab_20260922/ | FROZEN_EXPERIMENT b0dd91699d2170e42c3a0ae9e27769a80f64f8121b116da030f253ac0d8a7f2b | historical replay | SCORED_KILL_B_KEEP_000 · packet CLOSED | Examiner scorecard (numbers in packets/Q7_EXAMINER_SCORECARD_2026-09-22.md); cemetery CEM-ASTRA-20260922-001 | [V] | CONFLICT-Q7-ARMS and CONFLICT-Q7-STATUS (see below). Scored run artifacts box-only; main has results/NOT_RUN.json only; FROZEN_EXPERIMENT status IMPLEMENTED_FROZEN_NOT_RUN |
| R1-P1 feebook | PR3 | 22371178cb2663250b4762f328069571c48cb551 | astra-science/kalshi_feebook_lab_20260922/ | FROZEN_EXPERIMENT (on-disk) 1e0ced86cf9b573000aee0d1f8f3ea3993f4060cdf73addec63c2b1704a25fa2 | unit-only | SOURCE frozen · unit results | not a strategy score | [V] | CONV-A fee origin |
| R1-P5 rails | PR4 | 6a28e0d6254327ea4e6451c781bec56215ac6cac | astra-science/kalshi_rails_lab_20260922/ | FROZEN_EXPERIMENT (on-disk) 240bfb2dc09f3eb6ff9f1d9ec99efaeccf4677029c3a42bad6bd93f41d05a06e | unit-only | SOURCE_FROZEN_BEFORE_RESULTS · 44 unit PASS | pnl null | [V] |  |
| PR5 capital-structure | PR5 | ce4671b8201b3fe49ecab91d684815fe6bd51447 | astra-science/kalshi_capital_structure_lab_20260922/ | 27e6b041f592bd7d475c94d8fa22f392b869b0d116b48e264a6df8b048373caa | unit-only | SOURCE_FROZEN_BEFORE_RESULTS | results/pnl null | [V] |  |
| PR6 R2-P1 hygiene | PR6 | 25ec05381207252abb8abec8f6f99e30765f9704 | astra-science/kalshi_r2p1_hygiene_000_lab_20260922/ | ddcd4427f67fb0ed8d12a7a6a49aabea3b25b356bcb64a7d84d5c4590d08b563 | unit-only | SOURCE_FROZEN_BEFORE_RESULTS | scorecard null | [V] | same line as R2-P1 row (board lists it twice) |
| PR7 queue-fragility | PR7 | c33af159d00c07f2d66b2f93174cfcdb4cde8d37 | kalshi_queue_fragility_000_lab_20260922/ (main-only (not on box)) | e01d684abefd2d919ac6546f85619a246ce73098c04f7b24c84451ff49b00308 | unit-only | SOURCE_FROZEN_BEFORE_RESULTS | pnl null | [V] |  |
| PR8 R2-P1 fixture-join | PR8 | 80050e9b6d015cbf394ea8443dd550eea4c2f1ee | kalshi_r2p1_hygiene_000_lab_20260922/ (fixture join) | e9bac91ca908b2ba704d966f0cf48cb181070ac11de1d117b93512bd2719ae1c | unit-only | SOURCE_FROZEN_BEFORE_RESULTS | pnl null | [V] |  |
| R1-P3 | — | — | briefs + risk register | — | unit-only | CLOSED (measurement gate, no code) | n/a | [V] | NON_STUDY / CLASS_FIT_POOR |
| R1-P2 | — | — | — | — | unit-only | QUEUE (reserved) | n/a | [V] | NON_STUDY / CLASS_FIT_POOR |
| R1-P4 | — | — | — | — | unit-only | DEFER | n/a | [V] | NON_STUDY / CLASS_FIT_POOR |
| Scout brief kernels (Spreads/PASSYDS/MLB/CFB/MVE) | — | — | governance/astra/SCOUT_BRIEF_2026-09-22.md | — | unit-only | TRIAGED (TRY/TRY/TRY/DEFER/SKIP) | n/a | [V] | NON_STUDY / CLASS_FIT_POOR |
| Sibling deathmatch review | — | — | packets/SIBLING_DEATHMATCH_REVIEW_2026-09-22.md | — | unit-only | INDEXED | no scoring | [V] | NON_STUDY / CLASS_FIT_POOR |
| Q6 incumbent | — | — | main · nfl_factorial_lab_20260921 SHADOW_CANDIDATE_FREEZE 000 | — | historical replay | FROZEN / KEEP | as recorded by Examiner | [V] | P&L produced under CONV-B fees |
| Q7-B (closed desk packet) | PR2 | a85bfdab0cd7e3b4fcb3d4a5c89cf8627be85bd2 | nfl_paircheck_lab_20260922/ | b0dd91699d2170e42c3a0ae9e27769a80f64f8121b116da030f253ac0d8a7f2b | historical replay | KILL | scorecard + CEM-ASTRA-20260922-001 | [V] | cemetery card stays visible; not removed by rehab (REHAB_POLICY_3PASS) |
| CEM-ASTRA-20260922-001 | PR2 | a85bfdab0cd7e3b4fcb3d4a5c89cf8627be85bd2 | governance/astra/cemetery/CEM-ASTRA-20260922-001_Q7_ARM_B.md | b0dd9169… | historical replay | KILL (95%-of-D bar STANDS) | as recorded | [V] | VISIBLE — unchanged |
| PR9 R2-P1 fixture-join move | PR9 | 79800a82b8ad2c1e10f614f69fd7105d11e0d041 | kalshi_r2p1_hygiene_000_lab_20260922/ | e9bac91ca908b2ba704d966f0cf48cb181070ac11de1d117b93512bd2719ae1c | unit-only | MERGED (move into hygiene lab) | null | [V] |  |
| PR10 QF fixture-join pick B | PR10 | 7026be5104cd00cabcf9b34154506a76b2768b8a | kalshi_queue_fragility_000_lab_20260922/ (main-only (not on box)) | d95adb9b7e8aba852134c96b8f0f7d35a76bbf68254b8808f82f99ec82bb6ca4 | unit-only | MERGED | null | [V] | freeze = PR title d95adb9b [V] |
| PR11 Examiner fee+queue honesty | PR11 | aa0a373671edf6630d188d335d890573a285e0da | kalshi_examiner_fee_queue_honesty_000_lab_20260922/ (main-only (not on box)) | 4799642e54cf233a925697e00c5a9e29f5cb39070962a2e011f0fbe090c169f2 | unit-only | stub NOT_SCORED | null | [V] |  |
| PR12 R3-P1 fee_cost | PR12 | 5f45bf3741de1fc9e96f5304f05ce9f2ddbe91e4 | kalshi_r3_p1_fee_cost_lab_20260922/ (main-only (not on box)) | kernel c4e0a4448b783765154c061e945023163f0a6d59f0cc960640195515c83e944b | unit-only | NOT_SCORED | null | [V] |  |
| PR13 R3-P4 L2 shape | PR13 | 5eeeaa6bf26d226399448be997748d61faeba43d | kalshi_r3_p4_l2_shape_lab_20260922/ (main-only (not on box)) | kernel 4a4e7cc61efcb436955c566edc7a2681603a014725bc79047f9d825392064528 | unit-only | NOT_SCORED | null | [V] |  |
| PR14 honesty join q3300 fills | PR14 | d8957a0061ba601a11b3b03145b1516937239988 | kalshi_examiner_fee_queue_honesty_000_lab_20260922/ (main-only (not on box)) | 4799642e… | unit-only | MERGED | null | [V] |  |
| PR18 C1 honesty harness | PR18 | 254f10548feb293543e61e1a136eff9f78952849 | kalshi_c1_kxufcfight_honesty_lab_20260922/ (main-only (not on box)) | kernel a191c9b3… | unit-only | MERGED · STILL NOT_SCORED | null | [V] | no harness freeze file found on disk [U] |
| PR19 C1 empty orderbooks pin | PR19 | ea4909db79e39b4890447742de287ddf05ea379d | kalshi_c1_kxufcfight_lab_20260922/ (main-only (not on box)) | kernel a191c9b3… | unit-only | EMPTY_BOOKS_PINNED · NOT_SCORED | null | [V] | class=unit-only; GET-only capture of finalized books, CLASS_FIT_POOR |
| PR20 Cap-SR soft-blended reserves | PR20 | 45863037a30af6caf9c00361e46fe8bd5444c426 | kalshi_soft_blended_reserves_000_lab_20260923/ (main-only (not on box)) | 1f263dec7d7810515c3e32c13f3c5eca4344c4951db762a88ea01a8dfde7b1b3 | unit-only | scorecard null | null | [V] |  |
| PR21 C5 honesty harness | PR21 | ee69245a5dba058ee1198c88bb4685893508f273 | kalshi_c5_kxbtc15m_honesty_lab_20260923/ (main-only (not on box)) | 23b908af6e9a7799c9bbdac04b27e683dfccd0c0c25d691df84ff715202d3cab | unit-only | scorecard null | null | [V] |  |
| PR22 C3 bordering harness | PR22 | 637644966bae3737b52ab35826d3a63bf4b9b936 | kalshi_c3_kxhighny_bordering_lab_20260923/ (main-only (not on box)) | 27530d6427794a5559e40c7f56d6cd938d8c57cc8f51406fc26a5b0e36a5fdff | unit-only | scorecard null | null | [V] |  |
| PR23 R3-P3 FL harness | PR23 | cfd5f95a6b2c9bd654ae58bd278f8465b827712b | kalshi_r3p3_fl_maker_taker_lab_20260923/ (main-only (not on box)) | fbc58539b7a469d005b7f75b786efddecc1028a3bb0da601bc0082c9d4aab179 | unit-only | scorecard null | null | [V] | Conductor main@cfd5f95a ✓ |
| PR24 Cap-SR effects path | PR24 | 79347f0ed8562f7df8d539e79a1cb15985d8abfe | kalshi_cap_sr_effects_000_lab_20260923/ (main-only (not on box)) | cd08a93af2659c36f83cd1b9ffc3174364cc767efc374a4e0669e128f6a29074 | unit-only | scorecard null | null | [V] | CAP_SR_EFFECTS_PATH_000 ✓ main@79347f0e ✓ |
| PR25 S5 MVE fill-vs-legs | PR25 | 6626c6892298b015cf63688081545e27363226bc | kalshi_s5_mve_filllegs_lab_20260923/ (main-only (not on box)) | 8a118e6f1fdc8c22c6e559f395667aedffa5d270d067e39b6ae3ee24b2046d16 · parent a28932ba13b4913b69c48b73dde8ba066cebd212670d0b1cbb5ea8e93734b8ba | unit-only | scorecard null | null | [V] | Conductor "PR status unknown" → VERIFIED MERGED PR25 2026-09-23T15:26:55Z |
| PR26 S4 FEEQUEUE | PR26 | d7584dd48a67d38d81f5141654b6f498915a70a5 | kalshi_s4_ncaaf_feequue_lab_20260923/ (main-only (not on box)) | 3318204bf6e962f4f3372dad8c0f302e62d85c26b855de7369718654d0114728 · panel stub 38167d11da5842bc4d39e6e7dcaab20a67294c735ba14d8bbeafde3154c6342a | unit-only | scorecard null | null | [V] | ACK had prefix-only merge sha; full verified |
| PR27 R2-P3 prop ladder | PR27 | 3b0d1429b9ea702f2cb242e79f21f5ab5d3f18a6 | kalshi_r2p3_prop_ladder_lab_20260923/ (main-only (not on box)) | f8335eb0080cb1f82b1fad512509749134dd0e6e41ed85795347c3476796e87a · parent a30108f6… · panel 70e879e8738d033f392d821849dee3537af3e7b8a916670779d238f78ce098be | unit-only | scorecard null | null | [V] |  |
| PR28 R3-P4 L2-CAT | PR28 | e54554ff79b663b30836cd34f8d20004a9022a0a | kalshi_r3p4_l2_cat_lab_20260923/ (main-only (not on box)) | 3fc370d93f0ea42864f7bf482d7f6515254999c76e2fc4477df1273bfcdc051f · parent 4a4e7cc6… · panel 7477e023ab70c59a6739650155ddb9d77077766e3afd80443e540d60b5a86cbb | unit-only | scorecard null | null | [V] |  |
| PR29 R2-P5 SOT-ID | PR29 | 6f1e22e15d8841605be5c34711f202277f4b685d | kalshi_r2p5_sot_id_lab_20260923/ (main-only (not on box)) | 0424455f062b7c46c7c6161b84fb7b29702719acc45bf6a61b4e8f16c5e26457 | unit-only | scorecard null | null | [V] |  |
| PR30 C1 EMPTY-OB | PR30 | d7b935951c9ddd5e6c4d813fad69e401b6a7b6a3 | kalshi_c1_empty_ob_lab_20260923/ (main-only (not on box)) | 1b9f8fbec8bad866e055bcabd38c8c633835d505cbd25c367ff0675bff3a4b27 | unit-only | scorecard null | null | [V] |  |
| PR31 R3-P4 L2-SF | PR31 | ead2cb41d5d171d8972a27b98d144849b6f8c371 | kalshi_r3p4_l2_sf_lab_20260923/ (main-only (not on box)) | f00425261f085aef90e93b186810a0248165273f8bb923ef3597940a9e8345de | unit-only | scorecard null | null | [V] |  |
| PR32 C2 NHL-FQ | PR32 | 677d5d4f0d5ed1235b4827bf89dd98d82bc34356 | kalshi_c2_kxnhlgame_feequue_lab_20260923/ (main-only (not on box)) | a36ec35143a32c7cd24e9fdf2a33f645d356b93e34c131bb1b8a94e3f92e38f5 | unit-only | scorecard null | null | [V] |  |
| PR33 C4 CPI-FQ | PR33 | 6e55a99790f4cc09a437d2e16ccf4e8e826a154b | kalshi_c4_kxcpi_feequue_lab_20260923/ (main-only (not on box)) | 949b255859196f02d73303a1019e51276c583f8d1e3ffb4f0a64d330467c6f93 | unit-only | scorecard null | null | [V] |  |
| PR34 ATP-FQ | PR34 | 438f4abf28a3c0156daf6c96ece5efda9557f1dc | kalshi_atp_kxatpmatch_feequue_lab_20260923/ (main-only (not on box)) | 4d4ce944946e72dd40567d14388fe11c6145fbbb32505a880bcf80a4c8b4dffe | unit-only | scorecard null | null | [V] |  |
| PR36 ETH-FQ | PR36 | 82bf7bb99bcc618b912255cc24022b23f9f15047 | kalshi_eth_kxeth15m_feequue_lab_20260923/ (main-only (not on box)) | 9cae3bad089e6e18bee22694a36a1a2c18db33935a315766cd6bd8f8476aa83a | unit-only | scorecard null | null | [V] | not in Conductor list; found on GitHub |
| PR39 C1 admit-wire | PR39 | 3972fe4edfd53740219a4d051392f1291cef5f98 | kalshi_c1_kxufcfight_lab_20260922/ (main-only (not on box)) | panel 24426d80… (admit pin) | unit-only | scorecard null_pnl_settled_N_0 | null | [V] | not in Conductor list; found on GitHub |
| PR40 C3-RJ | PR40 | 9fd5d7cb89693a0ed29d9e97d2b723c0810989bc | kalshi_c3_kxhighny_settled_join_lab_20260923/ (main-only (not on box)) | 56adcf592239b028aaa8bcffbf09815115b8454f78db39b43c578e64c160a4d5 | unit-only | NOT_SCORED | null | [V] |  |
| PR41 C5-RJ | PR41 | 8cfcd17a62d3793dee554a4da422e8075bde9cf6 | astra-science/kalshi_c5_kxbtc15m_settled_join_lab_20260923/ | 7f4b36eca39d43ee7403628c2e525d5980fa40bcfc906550c7f00bb06ffd4f21 | unit-only | NOT_SCORED | null | [V] |  |
| PR42 R3P3-RJ | PR42 | 2fce8642d1b1961cbe0ef60fae1411cd8906f31a | astra-science/kalshi_r3p3_fl_settled_join_lab_20260923/ | 7fcfc36ab4761e2dec56018b498372fb63c402f2582fe848e8775e28f9b720b9 | unit-only | NOT_SCORED | null | [V] |  |
| PR44 NHL-RJ | PR44 | b450e780fd9752887579ee8d217b6dee76d918f8 | astra-science/kalshi_kxnhlgame_settled_join_lab_20260923/ | d1f71cea6df8f6c5a9fac6f9d1aa418ce61aa650794f22b400a01c4f3fd45810 | unit-only | NOT_SCORED | null | [V] | replaces closed PR43 |
| PR45 S4-RJ | PR45 | aeff380b29dbe89b16da58f9e15e58415b42b147 | astra-science/kalshi_kxncaafgame_settled_join_lab_20260923/ | 3a8e8ba52edd6acdc342c6a2faabb08665fe8a7a76e1b28af1c8e18850b03d99 | unit-only | NOT_SCORED | null | [V] |  |
| PR46 R2P3-RJ | PR46 | b2c1639a77f62114572fd41182f8a3c5ef70cad1 | astra-science/kalshi_r2p3_kxnflpassyds_settled_join_lab_20260923/ | 9ad3b0112243c1020aec2bd6ef0df15011b065c30aa691a988da02eb08be1e0b | unit-only | NOT_SCORED | null | [V] | after PR45; found on GitHub |
| PR48 S5-RJ | PR48 | fec05e8cf7c11f1c975ab791fda64f896d40d1cd | astra-science/kalshi_s5_kxmvecrosscategory_settled_join_lab_20260923/ | cd264a4d41ef055d1cbca80a5dbe6756746211537fb24799dca9dde8980cb799 | unit-only | NOT_SCORED | null | [V] | after PR45 |
| PR49 C1-RJ | PR49 | 34a2720218b4f4f2d6dd0cbde6334ee672a3684b | astra-science/kalshi_c1_kxufcfight_settled_join_lab_20260923/ | 3ea3362ad3c16951369d5f90497ec6079213dd54e5556340c4d3738744126cf1 | unit-only | NOT_SCORED | results/pnl/settled_join_n null | [V] | = current main head |
| PR15 (closed) | PR15 | not merged | — | — | unit-only | CLOSED_NOT_MERGED | null | [V] | superseded by #23 |
| PR16 (closed) | PR16 | not merged | — | — | unit-only | CLOSED_NOT_MERGED | null | [V] | C3 scaffold, not merged |
| PR17 (closed) | PR17 | not merged | — | — | unit-only | CLOSED_NOT_MERGED | null | [V] | C1 scaffold, not merged |
| PR35 (closed) | PR35 | not merged | — | — | unit-only | CLOSED_NOT_MERGED | null | [V] | superseded by #34 |
| PR43 (closed) | PR43 | not merged | — | — | unit-only | CLOSED_NOT_MERGED | null | [V] | closed — wrong ACCEPT cee2705a ≠ ce82d934 (CONDUCTOR_KICK_NHL_RJ / EXAMINER_ACK_NHL_RJ_PR44) |
| R3-P2 queue_position | PR37 | 9eba15870e66dcde8ffc17a56c73016245a833c1 | main: kalshi_r3_p2_queue_position_lab_20260923/ · box: astra-science/kalshi_r3p2_queue_position_lab_20260923/ | kernel d2e8b21d0c9ff818aea5ab462a6c91c8a7bccc11ab6ae7538169041ed905c8c3 | prospective shadow | ABS_ERR/signed-bias SCORED KEEP (measurement honesty) · promote false · cancel model NOT_SCORED · brier null | metrics per EXAMINER_SCORECARD_R3_P2_ABS_ERR_SIGNED_BIAS_2026-09-23.md | [V] | FLAG DEMO_VENUE_ORDERS: rest→poll→cancel orders on demo-api.kalshi.co (demo keys), fill_count 0; no real money; violates strict "no orders" clause of prospective-shadow definition → Conductor to rule (Examiner v1.1 already uses demo/shadow/live tags). Box and main lab dir names differ. |
| Q7-B-REHAB-P1 cadence 600 | PR38 | 9b8fb184a8f1d556e400188127f1753bf35e571e | astra-science/nfl_q7_rehab_p1_cadence_20260923/ | Refiner P1 freeze 91506143c2f75e27dd8a2593e9b484457b61e5b1a8537002bf2b4f4be435ec97 · lab FROZEN_EXPERIMENT 3183754c6880b20ad16b51b4595549409a24508ece6e3b21d507d51142ce3174 | historical replay | SCORED KILL (Examiner) · NO_NEW_SELECTION · promote false | per EXAMINER_SCORECARD_Q7_B_REHAB_P1_TAPE_WALK_KILL_2026-09-23.md | [V] | tape-walk results box-only (main has results/NOT_RUN.json); no CONDUCTOR_MERGE stamp for PR38; Arm B cemetery card NOT removed |
| Q7-B-REHAB-P2 rank sizing | PR47 | a281adc944e4dacffcdb5677a140fabaed675a81 | astra-science/nfl_q7_rehab_p2_rank_sizing_20260923/ | Refiner P2 freeze 5f70d83abe5f45f01a29f5bf4bf10484f934715990aed4759630ee6f90392bfd · lab FROZEN_EXPERIMENT e3e4814abcbb92b5142c1e4783fed53b50372783aeb58f664361966d719bd7d7 | unit-only | FROZEN_PRE_OUTCOME · units only · tape walk IN FLIGHT | results/pnl null; score_outcome null | [V] | tape walk rerun log started 19:33 ET; partial box files (q3300_d0.25_B0*) exist, NOT scored and NOT indexed. Relabel to historical replay only when Examiner scores. |
| C4-RJ KXCPI settled join | — (no PR yet) | — | astra-science/kalshi_c4_kxcpi_settled_join_lab_20260924/ | 5e37f81a8959e83c3d2c0c42739e1ca6c127c748442ac6fe28c0013edee12e2f | unit-only | CONDUCTOR_ACCEPT (freeze) · no PR | null | [V] | orphan-ish: accepted, not on GitHub |
| RES q7-paired-price (report R3) | — | branch head 01c726ae9244d801d359e00df67d6a71f4012669 | branch research/q7-paired-price | branch-internal freeze commit f0a2692a ("Freeze Q7 guard implementation and 115 tests before historical outcomes") | historical replay | branch: router_on selected, "Failed criteria: none" (Q7_RESULTS.md) | commit msg: primary simulated net $354.33 vs $201.52 baseline (quoted, not indexed as registry result) | [V] | CONFLICT-Q7-ARMS with registry Q7 (Arm B KILL). Not registered via Archivist freeze → result NOT indexed as registry outcome (gate 1) |
| RES q8-joint-routing (report R4) | — | branch head d7079b6fece902e6e4603114a1d9ed5ef5a246c5 | branch research/q8-joint-routing | branch-internal (per Q8 doc) [I] | historical replay | Q8_RESULTS.md on branch | not indexed | [I] | head commit message = M2 cohort freeze, not Q8 — PIN_MESSAGE_MISMATCH |
| RES M2 NCAAF/WNBA transport pilot | — | f44574e8… (branch m2-continuation) | branch research/m2-continuation | cohort freeze d7079b6 after spec bcd39b3 [V commit msgs] | historical replay | M2_RESULTS.md on branch | not indexed | [I] |  |
| RES M3 | — | f44574e8… | branch research/m2-continuation | [U] | historical replay | M3_RESULTS.md on branch | not indexed | [I] |  |
| RES M4 (freeze only) | — | f44574e8f318920cc8fdf87c9c3d35c18bca2107 | branch research/m2-continuation | head commit = M4 pre-outcome freeze | unit-only | FROZEN before outcomes | none seen | [I] | CLASS_FIT_POOR (freeze, no run seen) |
| RES AMS-002 static threshold screen | — | a59c9e33 / cba057e6 | astra-science git objects all_market_structure_20260924/threshold_screen/ | AMS FREEZE.json blob c887686e61b00bc7594fe67fd78fe2956504f954 | historical replay | Park | 0 of 180 depth-complete below $1 floor before fees (RESULTS.md) | [V] git object | → CEM-ASTRA-20260924-002 |
| RES AMS-003 triage | — | a59c9e33 / cba057e6 | …/triage/ | FREEZE.json blob 4d9a11769c61b67ca4822a73a6e38533dc730341 | historical replay | decisions table (Park / Reject / Data-blocked / Retain) | n/a | [V] git object |  |
| RES AMS-008 wide threshold | — | cba057e6 only (absent at a59c9e33) | …/wide_threshold/ | FREEZE.json blob 2cac328b6759b210d41f6bd7b907554d7cf866ff | historical replay | keep static taker lane parked | 5 positive gross, none survived M=1 fees (RESULTS.md) | [V] git object | not covered by report pin a59c9e33 → CEM-ASTRA-20260924-002 |
| RES AMS-007/AMS-010 prospective replication / scanner | — | cba057e6 (branch) | branch research/all-market-structure-20260924 | [U] | prospective shadow | per commit messages only | UNVERIFIED | [I] | content not reviewed |
| RES NH-001A neglected hybrid | — | 2253c03cd86eb5515325f1d91b43bdcbea7a902c | branch research/neglected-hybrid-20260924 | freeze commit faa0562f before results 6de80155 [V order] | historical replay | "House signal below breadth gate, failed Senate replication" (commit msg) | not indexed | [I] | negative result not on board until now; kept visible |
| Pre-charter NFL factorial (Q6 source) | — | on main | astra-science/nfl_factorial_lab_20260921/ | RESERVED_HOLDOUT f8f6b577… | historical replay | Q6 selected 000 | as recorded | [I] | CONV-B fees |
| Pre-charter NFL/Stern labs (maker_replay_round2, nfl_queue, nfl_timing, nfl_completion, nfl_adaptive, nfl_measurement, stern_lab) | — | on main | astra-science/<lab>/ | [U] | historical replay | pre-charter | as recorded in each lab | [I] | not Astra registry studies; listed for completeness |

## CONFLICT / UNVERIFIED register (results NOT edited)

| ID | Registry record | Other record | Disposition |
|---|---|---|---|
| CONFLICT-Q7-ARMS | Main/registry Q7 (PR2 + box run): arms A–D; Arm B KILL; `retains_95pct_of_D=false` (B/D ≈ 0.84 primary); cemetery CEM-ASTRA-20260922-001 | Branch `research/q7-paired-price`@01c726ae `Q7_RESULTS.md`: arms router_off/router_on/allocator_off/allocator_on; router_on selected, "Failed criteria: none"; commit msg "primary simulated net $354.33 versus $201.52 baseline" | Both recorded. [I] branch allocator_on figures match the Arm D values in `REFINER_EXTENSION_GAP_METRIC_FREEZE_Q7_ARM_B_2026-09-24.json`; arm mapping UNVERIFIED. No reconciliation, no retune. |
| CONFLICT-Q7-STATUS | Registry: SCORED_KILL_B_KEEP_000 from box-only results | Report: "Main retains a frozen/not-run Q7 study"; GitHub main `nfl_paircheck_lab_20260922/results/` = `NOT_RUN.json` only; box FROZEN_EXPERIMENT status `IMPLEMENTED_FROZEN_NOT_RUN` | Both recorded. Governance: scored artifacts not on main. |
| PIN-AMS-SUPERSEDED | Report pins AMS at a59c9e33 | Branch head now cba057e6 (+25 commits; AMS-005…AMS-012 incl. AMS-008) | Report's AMS view is stale; later content UNVERIFIED except the AMS-002/003/008 git objects pinned in CEM-ASTRA-20260924-002/004. |
| PIN-Q8-MSG | Report: Q8 at d7079b6f | Commit message = M2 cohort freeze; Q8_RESULTS.md present at sha [V] | Recorded. |
| CONFLICT-FEE-CONVENTION | Report L657: repo uses "older cent-ceiling convention" | NFL replay family (Q6/Q7/P1 P&L) uses $0.0001 fixed-point (CONV-B); cent ceiling is the Examiner harness channel (CONV-A) | See FEE-ACCT-MANIFEST-v0-DRAFT-20260924. |
| CLASS-C1-PANEL | Registry: C1-KXUFCFIGHT ADMITTED measurement panel | Panel data finalized at admit | Labeled historical replay, flagged. |
| CLASS-R3P2-DEMO | Prospective measurement | Demo-venue orders placed (fill_count 0) | Labeled prospective shadow + DEMO_VENUE_ORDERS; Conductor to rule on a demo class. |
| UNVERIFIED | AMS-007/010, M3 freeze, Q8 freeze, NH-001A content | — | Content not reviewed; commit messages only. |

## Not yet classified (in flight, other seats, 2026-09-24)

`packets/card01_hybrid_forecast/`, `card02_station_weather/`, `card03_liquidity_rewards/`, `scout_perps_screen_2026-09-24/`, `scout_c4_settled_rejoin_2026-09-24/`, `EXAMINER_KALSHI_SCORECARD_TEMPLATE_REVISION_2026-09-24.json` + `_v1.1_`, `REHAB_POLICY_EXTENSION_AMENDMENT_2026-09-24.md`, `REFINER_EXTENSION_GAP_METRIC_FREEZE_Q7_ARM_B_2026-09-24.json` (+ `_ADDENDUM_A_`), `ADVERSARY_EXTENSION_OVERFIT_CHECK_PROTOCOL_2026-09-24.md`, `ADVERSARY_DEAD_CARD_OVERLAP_EDGE_RESEARCH_2026-09-24.md`. These are policy/template/capture-in-progress packets, not scored studies; classify when a freeze + run exists.

## New cemetery lines (2026-09-24) — see `governance/astra/cemetery/`

| CEM id | Card / family | Class of the killing evidence | Tag |
|---|---|---|---|
| CEM-ASTRA-20260924-001 | Card 09 crypto settlement-window pricing (F2 lineage) | historical replay (TEST-20260913-001 on captured CF/Kalshi data) | [V] |
| CEM-ASTRA-20260924-002 | Card 10 core static threshold-basket taker | historical replay (AMS-002 / AMS-008 snapshots) | [V] git objects |
| CEM-ASTRA-20260924-003 | Card 06 CPI post-release sub-family | historical replay (captured contract rules/close times + AMS-003) — CLASS_FIT_POOR (structural) | [V] |
| CEM-ASTRA-20260924-004 | Card 03 subsidy-only zero-edge taker | historical replay (AMS-003 cost bound) | [V] git object |


---

## Addendum — Conductor rulings + corrections — appended 2026-09-24T19:50:45-04:00 (ET)

Rows above are not rewritten. This addendum supersedes the "Conductor to rule" dispositions where stated.

### Rulings

| ID | Ruling | Effect on rows above |
|---|---|---|
| CLASS-R3P2-DEMO | Class stays **prospective shadow**, sub-tag **DEMO_VENUE_ORDERS**. Demo orders are never `live`. Demo fills and queue behaviour never count as observed live execution (demo matching is not the production book). | R3-P2 row (PR37) stands as prospective shadow + DEMO_VENUE_ORDERS. Counts unchanged: prospective shadow 5, **live 0**. |
| CONFLICT-Q7-ARMS / CONFLICT-Q7-STATUS | Both entries marked **CONFLICT_UNRESOLVED** pending the Simulator's reconciliation memo. The registry's Arm B KILL is the Refiner P1 result on main's Arm B definition (Conductor wording). q7-paired-price `router_on` is treated as a different policy until the arm mapping is proven. | Q7 paircheck row and RES q7-paired-price row both carry **CONFLICT_UNRESOLVED**. Results unchanged. Memo `packets/q7_reconciliation_20260924/Q7_RECONCILIATION_MEMO_2026-09-24.md` (sha256 `0fe219561592ac4c13584017609363f238a08b47069c677c600e4d1482c882c9`, 19:46 ET, `RECONCILIATION_MEMO_READY_NOT_SCORED`) is on disk but not yet ruled on. |
| Card-09 lookahead | `LOOKAHEAD-CONTAMINATED` extended to the k=50 annex rows (BTC and ETH). | CEM-ASTRA-20260924-001 ruling section appended. |

### Correction — main's Q7 results directory (my earlier records were wrong)

- **Wrong (earlier text above and in STATUS):** "GitHub main `nfl_paircheck_lab_20260922/results/` = `NOT_RUN.json` only."
- **Correct [V] (main @ `34a27202` tree, re-read @ `37ad5b7b`):** main holds three files there: `NOT_RUN.json` (blob `85d0675a4082d8866c47d3f20fb89a1c7ae89250`), `analysis_status.json` (blob `24c7a72d8c15b9e2178efd63d92e701aea98b7fd`), `verification.json` (blob `485a7149a13dff19b12e493a57ae36f40908ec62`).
- `git hash-object` (no -w) of the box copies: all three are **byte-identical** to main. All three are not-run stubs. `verification.json` reads `status: NOT_RUN_INPUTS_MISSING` (as PR5's body said). The substance of CONFLICT-Q7-STATUS (scored artifacts not on main) is unchanged.
- **New finding [V]:** the Examiner Q7 scorecard pins scored `verification.json` at sha256 `eb1586bf13b1631951a4f177293350cb89fc7948a50fbb7044f4f05313ebc06f` (status VERIFIED). **No file with those bytes exists on the box.** Every box copy of that path is the NOT_RUN stub (sha256 `9cde03dc3d52eb3ab9d18024155c341451de9e1e8836356cdcf3cf1d0ac006e4`). The scored verification bytes are **UNVERIFIED / missing**. `paircheck_effects.json` does match its pin (`5d87ea61…`). The Examiner verdict is not altered.

### Main moved after the step-0 pin

- main is now `37ad5b7b366c10dcdf278c2325611e6f426a62c6` (PR52, merged 19:46:28 ET). PR50 `959c3f2b` (C4-RJ KXCPI settled-join harness) merged 19:43:06 ET.
- Class for the new lines [I from commit messages]: PR50 C4-RJ = **unit-only** (units 10/10; results/pnl/settled_join_n null). It is the row previously listed as "C4-RJ (no PR)". PR52 = infra (ADMIT-1 recorder throttle), NON_STUDY. The line count and class counts above are not re-tallied in this addendum.


---

## Addendum 2 — appended 2026-09-24T19:55:12-04:00 (ET)

Rows and Addendum 1 above are not rewritten.

| Row | Update | Tag |
|---|---|---|
| R3-P2 queue_position (PR37) | Filed **WARM_SHELF**, plumbing pass: Examiner `MEASUREMENT_PLUMBING_PASS` (`e66d2636…`, promote=false); Conductor ruling `7fa4455f…`. Mechanics verified. **Calibration NOT measured** (all windows trade-free). v2 spec **PARKED_SPEC** `packets/r3_p2_queue_position/PARKED_SPEC_R3_P2_TRADE_STEP_FILL_LABEL_v2.md` (`9488a1d6…`). Class stays **prospective shadow + DEMO_VENUE_ORDERS**. The 2026-09-23 abs_err/signed_bias KEEP is unchanged. | [V] |
| Q7 paircheck (PR2) | Label **Q7-PAIRCHECK-ARM-B (main)**. Conflict status **LABEL_COLLISION** (effective; Examiner memo stamp `641b10d1…` READY_NOT_SCORED on memo `0fe21956…`). Headline **NON_COMPARABLE** with router_on. Result unchanged (SCORED_KILL_B_KEEP_000). Main B/D 0.843 reproduces from box desk ledgers (Examiner ACCEPT), not from an in-git ledger. Scored `verification.json` pin `eb1586bf…` = **UNVERIFIED_BYTES_MISSING**; verdict stands; pin not rewritten. | [V] |
| RES q7-paired-price | Label **Q7PP-ROUTER_ON (branch 01c726ae)**. **LABEL_COLLISION** (effective); different admission and sizing; headline **NON_COMPARABLE**. Still not indexed as a registry outcome. | [V] |
| Q6 factorial / Q7 paircheck freezes | RESERVED_HOLDOUT: ORIGINAL pin `74507e1a…` stays in the freezes; dated re-pin to CURRENT `f8f6b577…` **VERIFIED** (ticker + trailing newline only). See `packets/RESERVED_HOLDOUT_REPIN_2026-09-24.md`. | [V] |


---

## Addendum 3 — appended 2026-09-24 ~20:03 ET

Rows and Addenda 1–2 above are not rewritten. The class counts above are not re-tallied here.

New cemetery line:

| CEM id | Card / family | Class of the killing evidence | Tag |
|---|---|---|---|
| CEM-ASTRA-20260924-005 | Card 04 Kalshi perps stale-quote taker arb, retail (Kalshi Prime Tier 0) account | prospective shadow — **FREEZE_GAP** (forward public-data capture, no orders; **no freeze before outcome**; single ~21 min window 19:36:01–19:56:59 ET). Fails the "frozen-before-outcome" part of the definition, so it is also CLASS_FIT_POOR on that criterion. | [V] |

Row updates:

| Row | Update | Tag |
|---|---|---|
| R3-P2 queue_position (PR37) | Mechanic errata `packets/r3_p2_queue_position/ERRATA_R3_P2_TRADE_STEP_PROVENANCE_2026-09-24.md` (`5692f1cf…`) indexed next to WARM_SHELF. Re-hash: **no frozen JSON or result changed** (24/24 manifest entries match; FROZEN_KNOBS `9a353421…`, stamp `e66d2636…`, retry outputs `755244e2…`/`e109ac02…`, series `6e2c8257…` unchanged). Retry series `6e2c8257…` moved HELD → LANDING (batch 3b `717840a0…`), labelled **COLLECTED_POST_FREEZE** (not pre-declared). Class stays **prospective shadow + DEMO_VENUE_ORDERS**; status WARM_SHELF. | [V] |
| Card 03 liquidity rewards | Fee term uses the DRAFT fee manifest (`aa765876…`) as **FEE_DRAFT** under both precisions (direct $0.0001 / non-direct $0.01); **DRAFT_NOT_ADOPTED** (AMENDMENT_01 `fed1d30c…`). | [V] |
