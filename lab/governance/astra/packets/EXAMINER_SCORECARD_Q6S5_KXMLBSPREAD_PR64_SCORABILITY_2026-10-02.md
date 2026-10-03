# EXAMINER SCORECARD: Q6S5 KXMLBSPREAD strategy-fill PR60 scorability (PR64)

Filed 2026-10-02T00:40:16-04:00 (ET) · template v1.2 `56bcf626…` · SCORE `EXAMINER_SCORE_Q6S5_KXMLBSPREAD_PR64_SCORABILITY_2026-10-02.json` sha256 `961f72fa76dd57867915b5321635becdc7a1f09d7d93e5147d66860fa0ea6e3e`

## Verdict: **ITERATE**
This is ITERATE-capped. counts_toward_keep=false and promote=false. No KEEP and no KILL.

**Rule (verbatim).** Freeze `213ee6dd` L216:
> - **Decision rule:** PR60 froze **no outcome hypothesis and no threshold**. FROZEN_EXPERIMENT `7383b483…` has no hypothesis field; the PR60 EXPERIMENT_SPEC says "Measurement infrastructure only". So the primary is measurement-only: **co-primary** `Q6S5A0 maker_vs_taker_roi_delta` (CACHE-fee-net per 9f50ba19 L90/L93) and `Q6S5A1 fresh_vs_stale_gap` (expected NOT_ESTIMABLE, R26). PR60 defines no A1−A0 contrast (the arms are two slices of one strategy, not competing strategies), so none is computed. **No new thresholds.** Any reading is descriptive and ITERATE-capped. The Examiner owns the verdict, within {ITERATE, KILL per a5398129, NOT_SCORED}; this freeze proposes no KILL criterion.

ACCEPT `9c6e19ca` binding condition 2:
> Verdict domain: ITERATE or INCONCLUSIVE/NOT_SCORABLE only. No KEEP (n = 3 games / 6 markets; MODEL fills; counts_toward_keep=false; v1.2 L777). No KILL either, because PR60 froze no hypothesis or threshold and the primary is measurement-only.

**Derivation.** No pre-declared text gives a threshold that chooses between ITERATE and INCONCLUSIVE. The freeze set intersected with the ACCEPT set is {ITERATE, NOT_SCORED/NOT_SCORABLE}. The run is scorable, so the verdict is **ITERATE**. 9f50ba19 L117 calls this "a measurement ITERATE path". *Flag:* if the Conductor treats the ACCEPT set alone as controlling, INCONCLUSIVE could be argued. That would be a Conductor ruling.

**Authority.** Conductor SCORE KICK for PR64, relayed as a message at ~00:35 ET. No `CONDUCTOR_SCORE_KICK_*PR64*` file is on disk.

## Primary (co-primary, measurement-only)
| Metric | Value | Reason |
|---|---|---|
| Q6S5A0 maker_vs_taker_roi_delta | **null** | empty_bin: 0/30 maker fills, so ROI(maker) is undefined. R27 says null, never 0. |
| Q6S5A1 fresh_vs_stale_gap | **null** | STALE_BIN_EMPTY: 15/15 placements are fresh. This was pre-declared as a structural null (ACCEPT ruling 2). |

## Descriptive settled PnL: STRUCTURAL ARTIFACT (not evidence for any arm)
PnL **−0.5400**. ROI = −0.54 / 15.54 = **−0.034749…**, which rounds to **−0.0347** at 4 dp (−0.0348 is not a correct rounding). fees_2x −0.84; one_tick_worse −0.84.
All 30 fills are taker legs. Each placement buys **both** YES and NO at the displayed touch, so exactly one leg pays $1. Every placement has YES+NO > $1 and YES+NO+fees > $1, so the PnL does not depend on the outcome: all 720 settlement permutations give −0.54. The total is 0.24 spread + 0.30 fees.

| mkt | t0 (09-25 UTC) | YES | NO | YES+NO | fees | all-in | pnl |
|---|---|---|---|---|---|---|---|
| DET2 | 04:48:31Z | 0.3300 | 0.6900 | 1.0200 | 0.02 | 1.0400 | -0.0400 |
| DET2 | 05:09:10Z | 0.3300 | 0.6900 | 1.0200 | 0.02 | 1.0400 | -0.0400 |
| DET2 | 05:30:26Z | 0.3300 | 0.6900 | 1.0200 | 0.02 | 1.0400 | -0.0400 |
| PIT2 | 04:49:15Z | 0.3800 | 0.6400 | 1.0200 | 0.02 | 1.0400 | -0.0400 |
| PIT2 | 05:09:54Z | 0.3800 | 0.6400 | 1.0200 | 0.02 | 1.0400 | -0.0400 |
| PHI2 | 04:49:59Z | 0.3900 | 0.6200 | 1.0100 | 0.02 | 1.0300 | -0.0300 |
| PHI2 | 05:10:38Z | 0.3900 | 0.6200 | 1.0100 | 0.02 | 1.0300 | -0.0300 |
| PHI2 | 05:31:54Z | 0.3900 | 0.6200 | 1.0100 | 0.02 | 1.0300 | -0.0300 |
| TB2 | 04:50:43Z | 0.2800 | 0.7400 | 1.0200 | 0.02 | 1.0400 | -0.0400 |
| TB2 | 05:11:22Z | 0.2800 | 0.7400 | 1.0200 | 0.02 | 1.0400 | -0.0400 |
| TB2 | 05:32:38Z | 0.2800 | 0.7400 | 1.0200 | 0.02 | 1.0400 | -0.0400 |
| NYM2 | 04:51:27Z | 0.4200 | 0.5900 | 1.0100 | 0.02 | 1.0300 | -0.0300 |
| NYM2 | 05:12:05Z | 0.4200 | 0.5900 | 1.0100 | 0.02 | 1.0300 | -0.0300 |
| NYM2 | 05:33:22Z | 0.4200 | 0.5900 | 1.0100 | 0.02 | 1.0300 | -0.0300 |
| WSH2 | 05:34:06Z | 0.2900 | 0.7300 | 1.0200 | 0.02 | 1.0400 | -0.0400 |

## Verification
- **Git:** eb33f094 is a commit object (parent f233079d; tree 1f1ccead; 2026-10-02 00:29:59 ET) in the Simulator clone, read through a scratch copy. The diff covers 181 files, +161633/−0 lines, all inside the new lab plus 1 registry row. runner_tree equals git: 3191/3191 blobs. Containment on origin main is attested by the Conductor (no fetch).
- **Digests:** lab DIGESTS 18/18; READY sha claims 33/33; freeze SOURCE_PINS 149/149; tape SOURCE_PINS 96/96; pins MANIFEST 159/159; BUNDLE_MANIFEST 156/156; packet MANIFEST 6/6; settlement DIGESTS 8/8; folder digest 65cfe9e4 matches. **0 failures.**
- **Flag 2 (digest addendum): SUFFICIENT.** The only FAIL, "fee pin fields", came from verify_digests.py L55 reading top-level keys. The fee pin nests them under /observed. The fee pin sha `9c0f3554…` equals its pin (6 identical copies on disk). The fields read quadratic / 0.5 / formula_id null / CACHE_NOT_R1P1.
- **T1b: PASS, run not void.** The unit test passes, and passes on the Examiner re-run (41/41). The in-run identity check covers 720 permutations with 1 quotes sha and 1 fills sha. The Examiner reproduced quotes 3780742e / fills 6fa0f543 byte-identically. A file-open trace of quote+fill reads 0 settlement files. Caveat: the test is constant by construction.
- **Independent recompute** (no runner code): 15 placements; maker 0/30 (every queue_ahead+1 exceeds the ticker's total tape volume); taker 30/30. fills.json rows 60/60 and PnL rows 30/30 match. pnl, ROI, fees_2x and one_tick_worse equal the Simulator's values exactly.
- **Settlements:** TBPHI-TB2 YES (1.0000); DET2, PIT2, PHI2, NYM2 and WSH2 NO (0.0000). S3–S6 PASS.

## v1.2 common scorecard
All 11 fields are null (calibration N/A) with measured=false. Reasons: no Astra orders/fills; the net_pnl formula is pending_definition; simulated fills are reported only under simulated_fills (60 requested / 30 filled; maker 0/30, taker 30/30; tag replay).

## Labels
IN_SAMPLE_DEV / HISTORICAL_REPLAY · family_size 1 · n = 3 games / 6 markets · MODEL fills → simulated_fills · fee CACHE_NOT_R1P1 (not R1-P1) · study_label "historical replay".

## Sep-25 universe
**CONSUMED** by this score. Any further outcome-scored use is in-sample and needs a new freeze. It is permanently ineligible for the KXMLBSPREAD holdout (ACCEPT ruling 1).

## Anomalies
- No CONDUCTOR_SCORE_KICK_*PR64* file on disk at write time; authority is the parent-relayed Conductor message (00:35 ET).
- The 00:34 ET task said "pins do-not-score on disk" for the ACCEPT; the ACCEPT 9c6e19ca contains no do-not-score text. Its "next" field names Examiner SCORE (cap ITERATE). Freeze attention item 2 says do-not-score was relayed, not filed.
- Simulator READY says the PR64 merge packet is absent on disk. CONDUCTOR_MERGE_PR64 (f1bab3b2, date_et 00:31 ET, mtime 00:34 ET) is present now. Likely a race with the Simulator grep (~00:32 ET); the READY statement is stale, not a run defect.
- Verdict-set wording differs: freeze {ITERATE, KILL per a5398129, NOT_SCORED}; ACCEPT "ITERATE or INCONCLUSIVE/NOT_SCORABLE"; committed HOLD/registry "ITERATE|INCONCLUSIVE". No text selects between ITERATE and INCONCLUSIVE.
- The T1b unit test is constant by construction (the permuted vector never reaches run_quote_fill); its weight rests on the absence of any settlement read path, which the Examiner confirmed by a file-open trace.
- The PR64 registry row (in git) and the committed implementer HOLD still say Examiner status HOLD_PRE_PR. Not edited (not Examiner-writable).
- PR head bb5f3d78 is not in the local object store (squash merge); eb33f094 containment on origin main is conductor-attested only (no fetch).
- The box restore (~23:13 ET 10-01) removed refs/ from /workspace/repo_f233079/.git; /workspace/repo_eb33f09 is intact. Neither was modified.
- All 720 permutations give PnL -0.54, so the T1 "PnL changes when a label flips" property is not exhibited on the real data. That is expected when every placement holds both sides.

No orders, no messages, no fetch. No prior file was edited.
