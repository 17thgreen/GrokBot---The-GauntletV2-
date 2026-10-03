# CEM-ASTRA-20261001-001: Q6S5 KXMLBSPREAD FL-band maker thesis (H1: FL0 low band beats FL1 mid band)

- **CEM_ID:** CEM-ASTRA-20261001-001
- **DATE:** 2026-10-01 (ET). Examiner SCORE filed 2026-10-01T19:30:46-04:00; Conductor ACCEPT KILL stamped 2026-10-01T19:33:00-04:00. Indexed by the Archivist on 2026-10-02 (ET) in `packets/ARCHIVIST_INDEX_BACKLOG_2026-09-25_to_2026-10-02.md`.
- **CARD-LINE:** Q6S5 KXMLBSPREAD. FL-band settled-tape measurement (PR61), on the parent R3-P3 10¢ favorite–longshot bands (`packets/r3_p3_fl_maker_taker/bands_registry_10c.json`).
- **FAMILY:** FL-band maker thesis, KXMLBSPREAD only. family_size 4.
- **DECISION:** **KILL** (verdict_ceiling ITERATE). Conductor ACCEPT `be235777` scope, verbatim: "FL-band maker thesis H1 (FL0 low-band beats FL1 mid-band), KXMLBSPREAD only, Sep-24 pinned universe".
- **CLASS of killing evidence:** historical replay, IN_SAMPLE_DEV (Conductor addendum `09763030`), public_counterparty_realized. Effective n = 3 games. Fee view CACHE_NOT_R1P1 (not fee-honest). Astra fills/results/pnl null. counts_toward_keep false; promote false.

## Cause of death

Examiner verdict_scope, verbatim (SCORE `2e74f17b`): "FL-band maker thesis (H1: maker_gross_roi_delta_FL0_minus_FL1 > 0) for KXMLBSPREAD only, per freeze. Not a kill of Q6S5, of the parent harness, of PR58/PR60, or of any other series."

Pre-declared freeze rule, verbatim (freeze `fb6540f5` line 118): "`contradicts_H1` if the full-sample delta ≤ 0 **and** ≥2 of 3 LOEO deltas ≤ 0. … `contradicts_H1` supports a KILL of the FL-band maker thesis **for KXMLBSPREAD only**."

Examiner reading, verbatim (scorecard `1bdb1d9c`): "Reading: **contradicts_H1**. The full-sample pre delta is -0.104764 (≤ 0). LOEO deltas are excl. HOUATH -0.240144, excl. LAASEA +0.031111, excl. SDLAD -0.122538, so 2/3 are ≤ 0."

- "**Primary H1 delta FL0−FL1 = -0.104764**" (scorecard).
- "All 6 LOMO H1 deltas are negative. H1 stays negative under both stresses." (scorecard)
- Multiplicity, verbatim: "With 3 games, the minimum one-sided sign-test p is 0.125 … The KILL rests on the pre-declared directional rule, not on a significance test." (scorecard)
- Conductor basis, verbatim (ACCEPT `be235777`): "pre-declared freeze rule contradicts_H1 -> KILL (full-sample delta <= 0 and >= 2 of 3 LOEO <= 0); directional, not significance-based"
- scoreboard_effect, verbatim: "none (Q6-000 remains KEEP leader; nothing promoted)"

## Erratum (recorded as annotation; be235777 not edited)

ACCEPT `be235777` field `erratum_noted` is WRONG. Conductor annotation in `546f62c9` (`annotation_of_be235777`), verbatim: "the erratum_noted field is WRONG. Per Examiner correction: finalized markets closed 04:30:17-20Z (HOUATH/LAASEA) and 05:06:42Z (SDLAD); 2026-09-28T01:40Z is latest_expiration / stale pre-close panel close. The original PR61 note was right." Effect, verbatim: "none on any PR61/PR62 number or verdict; 04:31Z prints were post-close and excluded".

## Evidence pins (sha256, re-hashed 2026-10-02 ET by the Archivist [V] unless marked)

| Role | Path (relative to `lab/governance/astra/` unless noted) | sha256 |
|---|---|---|
| Freeze | `packets/Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_FREEZE_2026-09-29.md` | `fb6540f52ed5f819ccf6e80bf0cf7eb6d951e065416b9d550fead0c6d06043fa` |
| Packet MANIFEST (8/8 OK) | `packets/Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE/MANIFEST.sha256` | `901285ed3d559e1a121197c1ee36ead3d8b40498dfd2b4888694fb077fe3c043` |
| Pin bundle (101 files) | `lab/astra-science/kalshi_q6s5_kxmlbspread_fl_band_settled_tape_lab_20260929/pins/…FL_BAND…2026-09-29.tgz` | `63b5d981bc06f684eebb69a8ac29394534f8ae52c101f3018557544f14e29857` |
| Variants registry ping | `packets/VARIANTS_ARCHIVIST_REGISTRY_PING_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_2026-09-29.json` | `eba1260f1ab901a223f3f0b5feb1ff6f023d9f8870c1e69e16007e93e12b3a40` |
| Bands registry | `packets/r3_p3_fl_maker_taker/bands_registry_10c.json` | `0860cbe28d28ecc6142ddf6f1ebb67792084264ed82e0b4d868c3b3138ea5312` |
| Conductor ACCEPT freeze | `packets/CONDUCTOR_ACCEPT_VARIANTS_Q6S5_FL_BAND_SETTLED_TAPE_FREEZE_2026-10-01.json` | `8e4fbac7d0426bc67c1f53fb8057a382fe46da738bd701cb970a9812a6dc2a3b` |
| IN_SAMPLE_DEV addendum | `packets/CONDUCTOR_RULING_Q6S5_FL_BAND_IN_SAMPLE_DEV_LABEL_2026-10-01.json` | `09763030c67df066f2b59346200813e181777670cd46fcee6b8877a6dd74d754` |
| PR61 merge commit (git) | 17thgreen/GPT-6-Astra-Deathmatch | `d7558fc4b92256c68eaea66b9700021206de0a2d` |
| Conductor MERGE | `packets/CONDUCTOR_MERGE_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.json` | `469de2376ae413f66684df26c08656e705a7fb5a0a1d128a4270d789c841df32` |
| Simulator READY | `packets/SIMULATOR_READY_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.json` | `8e8a17566747cb29077c2f7abccb49640739ae873d3d5c20fbfa819bbde36e1b` |
| Examiner READY_NOT_SCORED | `packets/EXAMINER_READY_NOT_SCORED_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.json` | `bf9aafa3363a45388aa8ebac2fffbaa0a556dba56d1cb59914119f6f78cfbffc` |
| Conductor score kick | `packets/CONDUCTOR_SCORE_KICK_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.json` | `0f8de7cd6b2187076e2bd8f914c4de51b3d8bfecdd59e324a41a9f030f5f26b6` |
| Examiner SCORE (KILL) | `packets/EXAMINER_SCORE_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.json` | `2e74f17b1307b8b57f33a6475cd7ce8af48c470099478cadfb07877b0d70745f` |
| Examiner scorecard | `packets/EXAMINER_SCORECARD_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.md` | `1bdb1d9c1e6272a4b95a5080e4681858859e69a053f69e32b9b85b7d9e44c386` |
| Conductor ACCEPT KILL | `packets/CONDUCTOR_ACCEPT_EXAMINER_KILL_Q6S5_KXMLBSPREAD_FL_BAND_PR61_2026-10-01.json` | `be2357773ca7a842e6896676e3ba0291f40ef8e0b8f997d46f7124d4b2705229` |
| Annotation of be235777 | `packets/CONDUCTOR_ACCEPT_EXAMINER_ITERATE_Q6S5_GAME_PHASE_PR62_AND_ANNOTATE_be235777_2026-10-01.json` | `546f62c99f1268b14ddb612fe9891c7741e5bee7e8397cae32c75d86fbff65ae` |

Flag: Examiner scratch outputs `/workspace/tmp/examiner_scratch_pr61_score/out/measure_pre_post.json` (`5dd5ea93…`) and `out/independent_recompute.json` (`f4571074…`) are **MISSING** on disk (box rebuild). Scripts `score_pr61.py` (`d6f52f01…`) and `independent_recompute.py` (`36fd44de…`) are present. The SCORE and scorecard bytes above are intact. The verdict does not depend on the scratch files being re-hashable.

## What this did NOT prove

- Not a kill of Q6S5, of the parent harness, of PR58/PR60, or of any other series (verdict_scope).
- Not evidence that FL1 or FL2 bands have edge. Conductor caveat, verbatim: "H2 (FL2 - FL1 = -0.4282) and the FL1 mid-band lead (+0.1443 gross) are hypothesis-generating only; carried to the untouched holdout as a pre-registered candidate, NOT a KEEP".
- Not a significance result. Effective n = 3 games; min sign-test p 0.125 > Bonferroni 0.0125.
- Not fee-honest (CACHE_NOT_R1P1). No Astra fills. No PnL.

## Rules

- Frozen negative stays visible. Never delete or soften.
- No resurrection without a **new freeze**. Scorecard, verbatim: "any re-test needs a new freeze with an untouched post-freeze settled set (p16 item 12)."
- The Sep-24 pinned universe is consumed for this thesis.
- No live orders. No invented PnL. Scoreboard unchanged: Q6-000 / Arm D KEEP +$345.24 / +6.90%.
