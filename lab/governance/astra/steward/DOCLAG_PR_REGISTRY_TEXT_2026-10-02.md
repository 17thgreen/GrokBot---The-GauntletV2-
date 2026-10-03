# DOC-LAG PR registry text for Archivist ACK (2026-10-02), revision 3

Prepared by: Steward KALSHI executor. Rev 1 about 19:00 ET; rev 2 about 19:13 ET; rev 3 2026-10-02 about 19:25 ET (America/New_York).
Rev 3 adds section 3 (round 2, Conductor GO 19:14 ET): the PR64 lab README line 5 (PR A) and fleet registry/PACKET_INDEX.md (PR B). Sections 1 and 2 are unchanged from rev 2 (already ACKed).
Rev 2 changes: Archivist wording for the row and the hold applied exactly; README `_prev` copy dropped (README is not frozen). The Archivist's ACK of bytes and mechanics stands; this revision changes only the two wording strings and their resulting sha256.
Authority: Conductor ruling 2026-10-02 18:53 ET explicitly ordered a docs-only PR including the PR64 housekeeping. It overrides the "Correct in the next landing PR only; no standalone PR" line in `lab/governance/astra/packets/CONDUCTOR_ACCEPT_EXAMINER_ITERATE_Q6S5_PR64_SCORABILITY_2026-10-02.json`.
Cited ids [V on box]: score `961f72fa` = `lab/governance/astra/packets/EXAMINER_SCORE_Q6S5_KXMLBSPREAD_PR64_SCORABILITY_2026-10-02.json` sha256 `961f72fa76dd57867915b5321635becdc7a1f09d7d93e5147d66860fa0ea6e3e`; Conductor ACCEPT `57a9f5e6` = `lab/governance/astra/packets/CONDUCTOR_ACCEPT_EXAMINER_ITERATE_Q6S5_PR64_SCORABILITY_2026-10-02.json` sha256 `57a9f5e68f41cf6df1428d2516ace34550267f264396d486f245977a571a871c`.
Merge fact: PR64 merged to `17thgreen/GPT-6-Astra-Deathmatch` main as `eb33f094f3341958746f83a8f2f8c1e2c37a7d0a` (2026-10-02T04:29:59Z = 2026-10-02 00:29:59 ET) [V via GitHub connector].
Base: main @ `eb33f094f3341958746f83a8f2f8c1e2c37a7d0a`. Old bytes verified against GitHub blob shas [V].

## 1. Registry row: `docs/EXPERIMENT_REGISTRY.md` (line 87 at eb33f094)

Single substitution inside the row; nothing else in the row or file changes. The sentence's trailing `.` stays.

- OLD fragment: `Examiner status `HOLD_PRE_PR``
- NEW fragment: `Examiner status `SCORED ITERATE` (score `961f72fa`, Conductor ACCEPT `57a9f5e6`; ITERATE = carry the design to fresh data only, not edge evidence; PR64 merged to main as `eb33f094f3341958746f83a8f2f8c1e2c37a7d0a` on 2026-10-02 00:29:59 ET; previously `HOLD_PRE_PR`)`

File sha256 old `8ee066c3f13fe4677b9a4f7b753a57ada43d8aa81229f2ec3c83af16c1a1e30f` (git blob `0f5e8d801f3fead1866b3af6f96ba348ede1b915`) -> new `d1d01784ddb50629a6842f0f9055e22f087c48c28eb43ba537e135f5f47660a6`.
_prev copy: `docs/_prev/8ee066c3f13fe4677b9a4f7b753a57ada43d8aa81229f2ec3c83af16c1a1e30f.EXPERIMENT_REGISTRY.md`.

### Full OLD row (exact)
```
| Q6S5 KXMLBSPREAD strategy-fill scorability | Hypothesis frozen 2026-10-02 before this implementation. Measurement only. Feature family `strategy_fill_pnl_path`. Series `KXMLBSPREAD` only. One knob: `fill_model`, value `public_trade_through_conservative`. `mechanic_demo_observed` stays unavailable. `family_size` 1. Universe is the 6 Sep-25 markets. Sep-24 and KXHIGH are closed. ADMIT-1 window `[2026-09-27T00:00:00Z, 2026-09-30T04:00:00Z)` is excluded. Fee label `CACHE_NOT_R1P1`. `promote` false. `counts_toward_keep` false. Verdict domain `ITERATE|INCONCLUSIVE`. Conductor ACCEPT sha256 `9c6e19ca11a855015fb4e3e63cd65ae5e5c334875240e817e164e988426df9f5`. Freeze sha256 `213ee6dd33f292c8041977b0b8d7566da9412fd3debe0597643c500dc1e42db4`. Bundle sha256 `bd94757c4c5748fc3447cf596435ddee0af129c87599d4c48f002b2b61756308`. Base `f233079d9e7d2a91e2100f2085bcf85d0006e28f`. `A1_null_reason` `STALE_BIN_EMPTY`. `results`, `pnl`, and `roi` stay null. Examiner status `HOLD_PRE_PR`. Structural counts only: books 15, eligible 15, crossed 0, empty sides 0, fresh 15, stale 0, requested maker 30, requested taker 30, prints 21, block 0, native-conflict 0, price-inconsistent 0, ADMIT-1 exclusions 0, maker filled 0, maker unfilled 30, taker filled 30, taker unfilled 0. Quote sha256 `3780742e41fa49d7d72ff11d4378eb0adeae9264d4a8913d9cc887c81b961946`. Fill sha256 `6fa0f543d8e8cc4c572f5385d83098639927d78e4f2be8364d833a92389d40f4`, constant across all 720 settlement-vector permutations. Code verification `python3 -m unittest discover -s tests -v` from `kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/`: Ran 41 tests in 5.009s. Result: OK. Failures: 0. Errors: 0. This run is not an Examiner score. No live orders. No GET. Does not replace the Q6 candidate. | `kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/results/UNIT_RESULTS.md` |
```

### Full NEW row (exact)
```
| Q6S5 KXMLBSPREAD strategy-fill scorability | Hypothesis frozen 2026-10-02 before this implementation. Measurement only. Feature family `strategy_fill_pnl_path`. Series `KXMLBSPREAD` only. One knob: `fill_model`, value `public_trade_through_conservative`. `mechanic_demo_observed` stays unavailable. `family_size` 1. Universe is the 6 Sep-25 markets. Sep-24 and KXHIGH are closed. ADMIT-1 window `[2026-09-27T00:00:00Z, 2026-09-30T04:00:00Z)` is excluded. Fee label `CACHE_NOT_R1P1`. `promote` false. `counts_toward_keep` false. Verdict domain `ITERATE|INCONCLUSIVE`. Conductor ACCEPT sha256 `9c6e19ca11a855015fb4e3e63cd65ae5e5c334875240e817e164e988426df9f5`. Freeze sha256 `213ee6dd33f292c8041977b0b8d7566da9412fd3debe0597643c500dc1e42db4`. Bundle sha256 `bd94757c4c5748fc3447cf596435ddee0af129c87599d4c48f002b2b61756308`. Base `f233079d9e7d2a91e2100f2085bcf85d0006e28f`. `A1_null_reason` `STALE_BIN_EMPTY`. `results`, `pnl`, and `roi` stay null. Examiner status `SCORED ITERATE` (score `961f72fa`, Conductor ACCEPT `57a9f5e6`; ITERATE = carry the design to fresh data only, not edge evidence; PR64 merged to main as `eb33f094f3341958746f83a8f2f8c1e2c37a7d0a` on 2026-10-02 00:29:59 ET; previously `HOLD_PRE_PR`). Structural counts only: books 15, eligible 15, crossed 0, empty sides 0, fresh 15, stale 0, requested maker 30, requested taker 30, prints 21, block 0, native-conflict 0, price-inconsistent 0, ADMIT-1 exclusions 0, maker filled 0, maker unfilled 30, taker filled 30, taker unfilled 0. Quote sha256 `3780742e41fa49d7d72ff11d4378eb0adeae9264d4a8913d9cc887c81b961946`. Fill sha256 `6fa0f543d8e8cc4c572f5385d83098639927d78e4f2be8364d833a92389d40f4`, constant across all 720 settlement-vector permutations. Code verification `python3 -m unittest discover -s tests -v` from `kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/`: Ran 41 tests in 5.009s. Result: OK. Failures: 0. Errors: 0. This run is not an Examiner score. No live orders. No GET. Does not replace the Q6 candidate. | `kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/results/UNIT_RESULTS.md` |
```

Row sha256 (utf-8, no newline): old `7f39be7613efd46d8dbbf94369a9a7f0ebfcf9c6cb8b9a02ba8bfcda29598090` -> new `4daa2807a928c6cd26a10f1adcdf64a03e4507f2be19f0667a67357cf1d9960e`.

## 2. Hold ffab465a: `kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/EXAMINER_HOLD_Q6S5_PR60_SCORABILITY_PRE_PR_2026-10-02.json`

- OLD line (exact): `  "status": "HOLD_PRE_PR",`
- NEW line (exact): `  "status": "SUPERSEDED (PR64 merged eb33f094; Examiner SCORE 961f72fa ITERATE)",`

Only the `status` value changes. The `id` (`EXAMINER_HOLD_Q6S5_PR60_SCORABILITY_PRE_PR`) and the file name stay the same, and the edited file parses as JSON (dry run) [V].
File sha256 old `ffab465a62587587b8630a994414cb1d7cd74741d56c935a81e803c2037ef6a2` (= hold ffab465a; git blob `47f10bcb1597053e914cda599edd12436f5404e2`) -> new `cf9ce7ca7c8bc677f70388e63cde75c49aa9a5afcdd70cc459fef451214e4880`.
_prev copy (unchanged from rev 1): `kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/_prev/ffab465a62587587b8630a994414cb1d7cd74741d56c935a81e803c2037ef6a2.EXAMINER_HOLD_Q6S5_PR60_SCORABILITY_PRE_PR_2026-10-02.json`.

Note for Archivist: box packets that pin `ffab465a` (EXAMINER_SCORE / EXAMINER_READY_NOT_SCORED PR64, runner_tree provenance) still pin the pre-edit bytes, which stay byte-exact in the `_prev` copy. At eb33f094, no repo file other than the hold itself pins `ffab465a` or the hold file name (git grep) [V].

## 3. Round 2 (Conductor GO 2026-10-02 19:14 ET); one extra commit on each existing draft PR

### 3a. PR A: `kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/README.md` (line 5 at eb33f094)
Frozen? Treated as frozen (`_prev` added). Its sha256 is pinned in the box run manifest `lab/astra-science/kalshi_q6s5_kxmlbspread_pr64_scorability_settled_run_20261002/provenance/runner_tree_files_sha256_BEFORE_RUN.txt`, and the 10-01 realign saved `_prev` for lab READMEs [V]. The root README stays without `_prev` per the Steward ruling.
- OLD line (exact):
```
The Examiner file in this directory is `HOLD_PRE_PR`. This lab does not place orders and does not open a network client.
```
- NEW line (exact):
```
The Examiner hold file in this directory is `SUPERSEDED` (PR64 merged `eb33f094`; Examiner SCORE `961f72fa` ITERATE, Conductor ACCEPT `57a9f5e6`). This lab does not place orders and does not open a network client.
```
File sha256 old `9a8bc5c6727c8abd30d83e4bfc1b9e6553aae6c449331d11b37b1bcd5ec5b83c` (git blob `8b625bf333c2d581f816789dbcbd0b2a8e13d845` at eb33f094) -> new `c9cd9b68ec32b72692a4ed959f40cbdfff42a57e54457f74ff86534a2c6e545a`.
_prev copy: `kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/_prev/9a8bc5c6727c8abd30d83e4bfc1b9e6553aae6c449331d11b37b1bcd5ec5b83c.README.md`.
Wording mirrors the hold file's status (`SUPERSEDED`). It doesn't use "MERGED" as an Examiner status. `results/UNIT_RESULTS.md` is not edited.

### 3b. PR B: fleet `registry/PACKET_INDEX.md` (at 1825ec8c)
Frozen? Treated as frozen (`_prev` added), like `registry/STATUS.md` in round 1 (fleet registry file) [A].
- OLD line (exact):
```
| ADMIT-1 | **LIVE** — PIT@CLE `KXNFLGAME-26OCT01PITCLE`; admitted_at `2026-09-22T21:18:13Z`; 16 events. GET-only recorder alive on Conductor host. |
```
- NEW line (exact):
```
| ADMIT-1 | **CLOSED/DOWN** per Conductor ruling. Run 18 closed truncated: record `lab/incidents/ADMIT1_TRUNCATION_BOX_REBUILD_2026-10-02_v2_CORRECTED.json` sha256 `52a6b8a1378b120a241ce9c6b302ca214b0a04b7360773269293d845b8623d3d`. Burst-profile spec: `lab/astra-capture/prospective/ADMIT1_POST_RUN_NOTE_2026-10-02.md` sha256 `9a2870dba116645900809026be14303b61cf53913920688197f27d94cbd43362`. Recorder **DOWN**: no recorder is running (was GET-only on Conductor host). Previously LIVE: PIT@CLE `KXNFLGAME-26OCT01PITCLE`; admitted_at `2026-09-22T21:18:13Z`; 16 events. |
```
File sha256 old `92320112b06f48f60d4a8aac5e793462e70eddf52acbd58ad007b56968c880e0` (git blob `eaba7027cff5a86c3571fec709a381b5ee67662a`, 566 B, reconstructed from a connector read and blob-verified) -> new `0b8aa0ca5bd927b47053e9ddfa3744af4ecfedff2e94888f8ced6ff91947331c`.
_prev copy: `registry/_prev/92320112b06f48f60d4a8aac5e793462e70eddf52acbd58ad007b56968c880e0.PACKET_INDEX.md`.
Wording and citations match `registry/STATUS.md` round 1: run 18 record sha256 `52a6b8a1…`, burst-profile spec sha256 `9a2870db…`, "Recorder **DOWN**: no recorder is running".

## Remaining items (not in either PR) [V]
- Never edited: `kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/results/UNIT_RESULTS.md` line 51 (a results file).
