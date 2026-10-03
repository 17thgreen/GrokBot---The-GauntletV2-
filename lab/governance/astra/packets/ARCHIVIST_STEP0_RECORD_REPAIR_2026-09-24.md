# Archivist — STEP0 record repair — 2026-09-24 (ET)

**Seat:** The Archivist (Registry) · **Routed by:** `packets/CONDUCTOR_ROUTING_KALSHI_EDGE_RESEARCH_2026-09-24.md` (sha256 `91f87bcfa7ab6c25234c9e6aa7e46d68ea6c9840b6e2550f585ca752c100e028`) plus Conductor steering (Adversary dead cards, Refiner re-pin)
**Stamped:** 2026-09-24T19:44:34-04:00
**Rules kept:** records only. No scoring, runs, orders or invented numbers. No result deleted, rewritten or softened. CEM-ASTRA-20260922-001 is unchanged (sha256 `1061864d8ef6a6bf44b8caafb42dd8e96562455c371a74bc75b2d1c0f27f65e8`).

## 1. Head pins (GitHub read-only; `registry/STEP0_HEAD_PINS_2026-09-24.json`)

| Pin | Full sha | Branch | Still head? | Commit (ET) |
|---|---|---|---|---|
| main | `34a2720218b4f4f2d6dd0cbde6334ee672a3684b` | main | YES | 2026-09-24 19:20:39 (PR49) |
| q7-paired-price | `01c726ae9244d801d359e00df67d6a71f4012669` | research/q7-paired-price | YES | 2026-09-21 14:29:16 |
| q8-joint-routing | `d7079b6fece902e6e4603114a1d9ed5ef5a246c5` | research/q8-joint-routing | YES | 2026-09-22 13:51:39 |
| m2-continuation | `f44574e8f318920cc8fdf87c9c3d35c18bca2107` | research/m2-continuation | YES | 2026-09-22 15:33:05 |
| all-market-structure | `a59c9e331dcfcd71c957e753bc4fd2460df403c0` | research/all-market-structure-20260924 (ancestor) | **NO**. Head is `cba057e62b3162bbf5cab17f4e2fee532a209ddc` (+25) | 2026-09-23 23:51:18 |

All pins were authored by 17thgreen. None is UNRESOLVED and none was substituted. The report reviewed main at `a281adc9…` (PR47), one commit behind the current head. An extra branch, `research/neglected-hybrid-20260924` @ `2253c03c…`, holds an NH-001A negative.

## 2. Class labels (`registry/STUDY_CLASS_LABELS_2026-09-24.md`)

- The vocabulary matches PDF p16 exactly: unit-only, synthetic, historical replay, prospective shadow, live. Examiner v1.1 uses the same five.
- Counts (83 lines): unit-only **61**, synthetic **0**, historical replay **17**, prospective shadow **5**, live **0**. Plus 4 new cemetery lines, all historical replay.
- Board rows were added for PR9–PR49 and C4-RJ.
- Conductor said PR25 (S5 fill-legs) status was unknown. It is **verified merged**.
- PR36, PR37, PR39 and PR46–49 were found on GitHub. There is no PR50.
- Flags: CONFLICT-Q7-ARMS, CONFLICT-Q7-STATUS, PIN-AMS-SUPERSEDED, PIN-Q8-MSG, CONFLICT-FEE-CONVENTION, CLASS-C1-PANEL, CLASS-R3P2-DEMO (**DEMO_VENUE_ORDERS**).

## 3. Fee manifest (`registry/FEE_ACCOUNT_MANIFEST_v0_DRAFT_2026-09-24.{json,md}`)

- `FEE-ACCT-MANIFEST-v0-DRAFT-20260924` · **DRAFT_NOT_ADOPTED**.
- Values from the feebook stub: taker 0.07, maker 0.0175, M=1. PDF prose says the maker multiplier defaults to 0, which **CONFLICTS** with the stub.
- The report states no numeric multiplier (null, flagged).
- Precision: direct --.0001 / non-direct --.01 (report L655-657). Account member type is **UNKNOWN**.
- CONV-A (order-level cent ceiling) covers all Examiner harnesses. CONV-B (--.0001 fixed-point) covers the NFL replay family behind the Q6/Q7/P1 P&L. hygiene.py is dual. The status is **RECONCILIATION_REQUIRED**.
- No past result was recomputed.

## 4. Additional work (Conductor steering)

- **(A)** Class names confirmed against PDF p16 and Examiner v1.1. No spelling changes were needed.
- **(B)** Cemetery entries CEM-ASTRA-20260924-001 through 004:
  - card 09: F2 lineage. The TEST-20260913-001 BTC result is flagged **LOOKAHEAD-CONTAMINATED**; its numbers are unchanged.
  - card 10 core: AMS-002/008 git objects pinned @ `cba057e62b3162bbf5cab17f4e2fee532a209ddc`. The AMS-008 tree is absent at a59c9e33.
  - card 06 CPI: KXCPI closes at 8:25 ET per the C4 panel stub rules. BLS CPI release is 08:30 AM ET, fetched from bls.gov (curl returned 403, so no raw-byte hash).
  - card 03: subsidy-only zero-edge taker.
- **(C)** Refiner ledger re-pinned by appending A1. Old `07e5fcdb…` is SUPERSEDED; new `9f436dafb6e7bb579b0148ed25401502812b7d1fc373c21bb66b367198ae75cf`.

## 5. Governance problems

1. Scored run artifacts exist on the box only; main shows NOT_RUN. Affects Q7, Q7-B P1 and R3-P2.
2. R3-P2 placed demo-venue orders, so it does not meet the strict "no orders" definition.
3. No CONDUCTOR_MERGE stamps for PR1–29 and PR38. C4-RJ is accepted but has no PR.
4. Research-branch results (q7/q8/M2/M3/AMS/NH) have no Archivist freeze packets. Their branch-internal freeze commits come before results [V order where checked]. Only negatives are indexed.
5. The box astra-science clone is stale: HEAD `cb622398…`, origin/main `6a28e0d6…`. Refer to the Steward.
6. The AMS report pin is stale.
7. No 'live' claim was found. No study has results without a prior freeze.

## 6. Files written or modified (sha256 at stamp time)

| Path (under lab/governance/astra/) | Action | sha256 |
|---|---|---|
| registry/STEP0_HEAD_PINS_2026-09-24.json | new | `4c7d2a3e746c138d04b45fa5ad793fd8f5a325debb68b5ffc61aec2cb24ddfe4` |
| registry/STUDY_CLASS_LABELS_2026-09-24.md | new | `d3f3fa9a0bce3476e2c4737f06914ec140fb8cf42350104060930b9238cbd3b3` |
| registry/FEE_ACCOUNT_MANIFEST_v0_DRAFT_2026-09-24.json | new | `aa7658764061912073b8d9fc1f2ae03fc970fa382dca1c49335944be650552ba` |
| registry/FEE_ACCOUNT_MANIFEST_v0_DRAFT_2026-09-24.md | new | `c62084b914dd0c73aff5ed87d95d688f3d3d580ecb535d1748253da3c1d8ba61` |
| registry/PACKET_INDEX.md.bak-20260924 | backup | `5f21a548591327a7b53e99689e1eea53003197d39814bf1ff007b36602b094d2` |
| registry/PACKET_INDEX.md | appended (+ Updated line) | `3119ab0c8d567e1004d2d9a6ddcff62bc5cf5c2da49bc80f335b001b9e7cd4e1` |
| registry/STATUS_2026-09-24.md | new | `1d149526183e44271adf27e90d69ebdc7e4cde6d8aaf42e201aa53127f35f6c8` |
| cemetery/CEM-ASTRA-20260924-001_CARD09_CRYPTO_SETTLEMENT_WINDOW.md | new | `30ba0243b8535079e050d13706e5cd585f313cbcceed8b285cc6cec0131df54c` |
| cemetery/CEM-ASTRA-20260924-002_CARD10_STATIC_THRESHOLD_BASKET_TAKER.md | new | `9e27fec93344f0351af49c853cb9bcce5a75a019be8504a0f908a8314b76a4d5` |
| cemetery/CEM-ASTRA-20260924-003_CARD06_CPI_POST_RELEASE.md | new | `3e2059032c541ddeee457ae8f8e7891b92e73b7cef64b99e0ab0c13e6d2b0f02` |
| cemetery/CEM-ASTRA-20260924-004_CARD03_SUBSIDY_ONLY_ZERO_EDGE_TAKER.md | new | `fef54c5e5e741e6b00c4b02966163571b3bc8fdc27a84620ccc1534de7ed0255` |
| packets/refiner/REFINER_BOX_PACKET_SHA256_2026-09-23.md | appended A1 | `468b97e56d85aff07c13b2a40babd32f642b333de5f0126f0271b028b67113b6` |
| packets/ARCHIVIST_STEP0_RECORD_REPAIR_2026-09-24.md | this file | (cannot contain its own hash; reported separately) |

## 7. New refiner/ files pinned (not in the 2026-09-23 box table)

| File | sha256 |
|---|---|
| CONDUCTOR_DECISION_Q7_B_P1_PARENT_LEDGERS_2026-09-23.json | `78c4cf447d13c922540601d41ea11b12e5c90011622dcf92f25af4b8e1a580cf` |
| CONDUCTOR_KICK_REFINER_Q7_B_PASS2_2026-09-23.json | `ba815344f276c40a627a10144d972d9b1cdaf652f221f8b1e476ec4eb606bab4` |
| PARENT_Q7_BD_LEDGER_SOURCE_PINS_2026-09-23.json | `5ee602ba5d6537956c87eca0d5af5bf4443b80e935e85d1c7c61279f4fed432a` |
| REFINER_EXTENSION_GAP_METRIC_FREEZE_Q7_ARM_B_2026-09-24.json | `6f3f5a660e95c6d5f241ca99e795fab1ea4eda9c86eaa264b7db58fbf5b83550` |
| REFINER_EXTENSION_GAP_METRIC_FREEZE_Q7_ARM_B_ADDENDUM_A_2026-09-24.json | `84989a3822a50a2257385e6970d7adabbcbbab919126592312b101a9d0076bb7` |
| REFINER_HAND_SIMULATOR_ARM_B_TAPE_WALK_2026-09-23.json | `520a42e439d260222136656e9c13a2b19550acbc49e0fe13860ae61315b435e2` |
| REFINER_HAND_SIMULATOR_Q7_B_PASS2_RANK_SIZING_2026-09-23.json | `8acc6811a880df96c943b53481743f14ca9240996b59e073f2ee2aacd81d3118` |
| REFINER_HAND_SIMULATOR_Q7_B_PASS2_TAPE_WALK_2026-09-23.json | `80bef188bee23690b8080680856255c875a4057e9629dc6835212328085e12cc` |
| REFINER_PASS2_DIAGNOSIS_Q7_ARM_B_2026-09-23.md | `a9539677db0c775534f3b15c07bf572d3d8877844867561e49b059716f1af292` |
| REFINER_PASS2_FREEZE_Q7_B_PORTFOLIO_RANK_SIZING_2026-09-23.md | `5f70d83abe5f45f01a29f5bf4bf10484f934715990aed4759630ee6f90392bfd` |
| REFINER_POSITIVE_CONTROL_HASH_PASS_Q7_B_REHAB_P1_2026-09-23.json | `ccdecf5b76ffe271816bf4fcef0656c258b316313f47757152d022c08144223b` |
| REFINER_POSITIVE_CONTROL_HASH_PASS_Q7_B_REHAB_P2_2026-09-23.json | `621b77cf0bcbef9e0e46c0b7962993a6db6f461676c2b2901033d45bf98c1513` |
| REHAB_POLICY_EXTENSION_AMENDMENT_2026-09-24.md | `59c2222590103838cdf119691c9cb67a92cdd601b254760af612a993000aeba8` |
| SIMULATOR_READY_Q7_B_REHAB_P1_TAPE_WALK_2026-09-23.json | `8edc708dc7727c7132578f221a79372b7f8c3622826759516509f7a14ca8e642` |

Inputs cited: Adversary `packets/ADVERSARY_DEAD_CARD_OVERLAP_EDGE_RESEARCH_2026-09-24.md` (sha256 `b434220493c8dfae34c123786153ad038ae3cb2832272254a2e97673f7e87fdd`) · report txt `e0223a39dcb1336fef2ad572d4fcfc7770ceb55ee69496bb59438a40dec990c3` · pdf `7e55bc260526aa5088ee31f74475851219ab2cd7f19fdd2f0dd5e9f998c8b45e`.
