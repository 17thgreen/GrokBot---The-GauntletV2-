# STEWARD — Conductor rulings execution — 2026-10-01

Author: The Steward "KALSHI". Window: 18:55–19:10 ET, Thu 2026-10-01. Generated 2026-10-01T19:05:15-04:00. Source report: `lab/governance/astra/steward/HYGIENE_2026-10-01.md` (§11 appended). Evidence tags: [V] verified · [I] inferred · [H] hypothesis · [A] assumption · [U] unknown.

**Summary.** R1 DONE: clone archived and verified, then reset to `12e760f5`, status clean. R2 DONE: main is the reference everywhere (no Conductor ACCEPT pins the box bytes), so box copies were realigned to main with `_prev` copies saved. No PR needed. R3 VERIFIED, NOT EXECUTED: 14 branches qualify for deletion, 1 skipped, 5 `research/*` held. Deletions are **blocked** because this session has no CloudAgent tool. R4 DIAGNOSED: the sync has no working write path for its outstanding payload. Fix proposed; no routine or script was changed. ElectIndex/private leakage: **NONE**.

## Hard-rule compliance
- No merges, force-pushes, history rewrites, PR closes, or PR refreshes. GauntletV2 PR #1 untouched (still open draft) [V].
- No market or venue API calls. GitHub was read only, through MCP, public REST GETs, `git ls-remote`, and `git fetch` [V].
- Running processes untouched. ADMIT-1 pids 2305742/2305743 and the capture pids were not signaled. Nothing had cwd or open fds under `/workspace/lab/astra-science` or the two packet dirs, apart from the Steward's own shell [V].
- Nothing was pushed to any repo. Local git was used only on the astra-science clone (fetch/reset/clean, plus a local `.git/info/exclude` entry for `_prev/`) [V].
- RULE-FROZEN-EDIT-PREV-BYTES-001: every overwritten frozen/pin/README file has `_prev/<sha256>.<name>` and an old→new record [V].

## Ruling 1 — astra-science box clone (GO, preserve first) — DONE
- Pre-state: HEAD `cb6223989afaf9e2f2fde8516e5ce16098ef7160`. Porcelain 133 entries (412 with `-uall`: 63 staged A, 3 staged M, 3 unstaged M, 343 untracked incl. 8 symlinks). Local branches `main`=cb62239 (no commits beyond origin) and `pr-55`=0cbe603c (5 commits beyond the stale origin refs; = PR55 head) [V].
- Preserve dir `/workspace/steward_astra_science_preserve_20261001/`. Hashes were written into HYGIENE §11.1 at ~18:59 ET, **before** the clone changed [V].

| artifact | sha256 |
|---|---|
| `astra_science_dirty_133_20261001.tar` | `f91ecb6840cd76b69d00354debd54499abd960c7ac724128bcc6e7e2faeec737` |
| `astra_science_local_branches_20261001.bundle` | `9e39de38442a01840edd3d0f525d8c58c1bbc2b8ffaa5139fda475048ebe0f59` |
| `git_status_porcelain_v1_uall.txt` | `62a25e0e0993d6260b0ac04bf5874356b5f2503539c25ae33fb76be95e19cf26` |
| `git_status_porcelain_v1.txt` | `2d147b9520349d95e816d62444f543da303b60abe936ad65b4548c3bfc6a3bb8` |
| `git_diff.patch` | `febaf3e0055cf185119a71a7bfcca2eddfd7344233cddd5efc99135bfc9675eb` |
| `git_diff_cached.patch` | `b84072fe9f9c5333cb0727693920e1b22624ffb1d1ab4666a573af7638aa3439` |
| `originals_sha256.txt` | `7bfa5944df8a038997097dea78285504700f97cd0b2e154d75b5ba9e097b6513` |
| `symlinks.txt` | `b0c3f91312a955becf376861a2a1de4975e02fc0690d17efaa188bcea4958b5b` |
| `tar_listing.txt` | `f3e6d55f4b8c4850d63b31a35528b10e42e711ea4e40b71a7c1fdc5c3114b467` |
| `file_list_uall.txt` | `fdb20494d0cda226c5a91b94131dc26ce4b871142081b99d84c636bf0334e2bb` |
| `HEAD_before.txt` | `d2f4ab4f965707d1b142344fc8e85f55c014ed8c2a25200cc92ebc7ace3c6b8c` |
| `git_branches_before.txt` | `546cf7d57edf0ebffdaf4d5905e5fc4743f95b8b4370237e9a8a791ab351b7f3` |
| `TAR_VERIFY_RESULT.txt` | `122f5f034a04383fbb8220e01a2a2c313eae0c1c160b893e68e1415f5c8d1998` |
| `FROZEN_PREV_RECORD_astra_science.json` | `9b0d2e89aa6938ea3e71c66a7cb1533e98a3526c0749a29a53e2d7f76332761f` |

- Tar verification: extracted to a temp dir. `sha256sum -c` passed 404/404 regular files, and 8/8 symlink targets matched. Temp dir removed [V]. Bundle: `git bundle verify` OK, full history of `main` and `pr-55` [V].
- Change: `git fetch origin` → `git reset --hard origin/main` → `git clean -fd` (not `-x`, so the 237 ignored files were kept; before/after lists match). A dry run confirmed all 159 clean targets were inside the tar [V].
- **Result: HEAD = `12e760f5bd3b622d8f0d70a74c28655464e2b93c`, `## main...origin/main`, porcelain 0 (clean)** [V].
- Frozen files overwritten by the reset: 14, each with `_prev/` inside the clone. A local `.git/info/exclude` entry for `_prev/` keeps status clean and stops `git clean` from removing them. Record: `FROZEN_PREV_RECORD_astra_science.json`. The 33 frozen-named box-only files removed by clean are preserved byte-exact in the tar (shas in `originals_sha256.txt`) [V].
- Results files in the clone (e.g. `kalshi_r2p1_hygiene_000_lab_20260922/results/R2P1_UNIT_RESULTS.md`) went back to main bytes as part of the resync. No result content was authored or edited, and the old bytes are in the tar [V].
- Docs drift **resolved**: `README.md` 1e564370, `docs/EXPERIMENT_REGISTRY.md` b84e5899, `docs/NEXT_EXPERIMENT.md` 2a9b4f6a all equal main. `nfl_prospective_recorder_20260922/record.py` is now 4f5db821 (throttled) and the 3× `RESERVED_HOLDOUT.json` are 3af85f2e, both = main [V].
- Side effects: fetched `refs/pull/*/head` into the clone as `refs/remotes/pr/*` (local, aids recovery). Stale remote-tracking refs of deleted branches were not pruned. A `git status` in `/tmp/astra_repo` refreshed its index mtime (no content change) [V].

## Ruling 2 — C4-RJ / ATP-RJ SOURCE_PINS — REALIGNED TO MAIN (no PR)
ACCEPT/MERGE packets read (box and main bytes identical: C4 ACCEPT `8a86ae6b…`, ATP ACCEPT `e42d7583…`, ATP MERGE PR54 `d02674a0…`; C4 MERGE PR50 `e0afb530…` exists on box only) [V]. No Conductor ACCEPT pins the box bytes of any divergent file. The only packet pinning a divergent file is C4 MERGE PR50 (`source_pins_sha256` = bcd27e06 = **main**) [V]. Main is therefore the reference everywhere.

| box path (lab/…) | box sha256 | main sha256 | ACCEPT/MERGE pin | action |
|---|---|---|---|---|
| `astra-science/kalshi_c4_kxcpi_settled_join_lab_20260924/SOURCE_PINS.json` | 21df2532fd0c016c…(1290B, blob f1f5f2b4) | bcd27e06f57f0e6b…(11080B, blob 38cfacb1) | CONDUCTOR_MERGE_C4…PR50 `source_pins_sha256`=bcd27e06 (=main). C4 ACCEPT 8a86ae6b pins freeze/scout/seed/panel/settled/hold/maximize only, not SOURCE_PINS. Main EXPERIMENT_SPEC + EXAMINER_READY call 21df2532 the superseded pre-harness desk declaration. | realigned -> main (ruling-1 reset); _prev saved |
| `astra-science/kalshi_c4_kxcpi_settled_join_lab_20260924/FROZEN_EXPERIMENT.json` | b72465d809ccd208…(1486B) | 968a46e3733bc17e…(1375B) at root; b72465d8 also on main at lab/astra-science/ mirror + scout dir | none in ACCEPT/MERGE (b72465d8 is pinned inside main SOURCE_PINS as the scout_c4 freeze-bundle copy, which is untouched) | realigned -> main root bytes (ruling-1 reset); _prev saved |
| `astra-science/kalshi_c4_kxcpi_settled_join_lab_20260924/README.md` | 748e59cd7c143134…(400B) | 07a7ef310b1a78f7…(1440B); 748e59cd on main mirror | none | realigned (reset); _prev saved |
| `astra-science/kalshi_atp_kxatpmatch_settled_join_lab_20260924/SOURCE_PINS.json` | 4de33473fd9bab91…(1910B, blob bf1a9b5c) | 509e2cf29c701de2…(15537B, blob 0ddd23fb) | none: ATP ACCEPT e42d7583 pins freeze dc9fcb32, maximize 70020baf, ping a666102d, bundle 531d3b41; MERGE PR54 pins accept/freeze/maximize/template. Main EXPERIMENT_SPEC calls 4de33473 the pre-harness declaration. | realigned (reset); _prev saved |
| `astra-science/kalshi_atp_kxatpmatch_settled_join_lab_20260924/FROZEN_EXPERIMENT.json` | 802b40b308724ae0…(8062B) | 382009b93b561f21…(8209B); 802b40b3 on main mirror/scout | none | realigned (reset); _prev saved |
| `astra-science/kalshi_atp_kxatpmatch_settled_join_lab_20260924/README.md` | 39f555bf1e560a5d…(606B) | a37834ea27c56aa1…(2379B); 39f555bf on main mirror | none | realigned (reset); _prev saved |
| `governance/astra/packets/C4_KXCPI_SETTLED_JOIN_HARNESS/SOURCE_PINS.json` | 21df2532fd0c016c… | bcd27e06f57f0e6b… (main packets/C4_…/SOURCE_PINS.json) | MERGE PR50 pins main bytes | realigned in place; _prev/21df2532….SOURCE_PINS.json |
| `governance/astra/packets/C4_KXCPI_SETTLED_JOIN_HARNESS/FROZEN_EXPERIMENT.json` | b72465d809ccd208… | 968a46e3733bc17e… | none | realigned in place; _prev/b72465d8….FROZEN_EXPERIMENT.json |
| `governance/astra/packets/ATP_KXATPMATCH_SETTLED_JOIN_HARNESS/SOURCE_PINS.json` | 4de33473fd9bab91… | 509e2cf29c701de2… | none | realigned in place; _prev/4de33473….SOURCE_PINS.json |
| `governance/astra/packets/ATP_KXATPMATCH_SETTLED_JOIN_HARNESS/FROZEN_EXPERIMENT.json` | 802b40b308724ae0… | 382009b93b561f21… | none | realigned in place; _prev/802b40b3….FROZEN_EXPERIMENT.json |
| `governance/astra/packets/{C4,ATP}_…_HARNESS/README.md` | (absent on box) | 07a7ef31… / a37834ea… | — | no action (missing on box, not divergent) |

**Old → new pairs (for the Archivist):**

| path | old sha256 | new sha256 | _prev copy |
|---|---|---|---|
| `lab/governance/astra/packets/C4_KXCPI_SETTLED_JOIN_HARNESS/SOURCE_PINS.json` | `21df2532fd0c016ca17bd4b12e8e0eab06c18e05a2f2955e3fbe6004333c80ca` | `bcd27e06f57f0e6b617ce318fb6d42da8c9b0a526816fbc4e41cef07a875154c` | `lab/governance/astra/packets/C4_KXCPI_SETTLED_JOIN_HARNESS/_prev/21df2532fd0c016ca17bd4b12e8e0eab06c18e05a2f2955e3fbe6004333c80ca.SOURCE_PINS.json` |
| `lab/governance/astra/packets/C4_KXCPI_SETTLED_JOIN_HARNESS/FROZEN_EXPERIMENT.json` | `b72465d809ccd208588ce13baa8749b8f5d1eedfb82abef47d261d84939b067f` | `968a46e3733bc17e58c223ccc71525e5090ff7a1204b7c2222de4353a3940191` | `lab/governance/astra/packets/C4_KXCPI_SETTLED_JOIN_HARNESS/_prev/b72465d809ccd208588ce13baa8749b8f5d1eedfb82abef47d261d84939b067f.FROZEN_EXPERIMENT.json` |
| `lab/governance/astra/packets/ATP_KXATPMATCH_SETTLED_JOIN_HARNESS/SOURCE_PINS.json` | `4de33473fd9bab9133ab30e55c7cfc409ee9c92b26d92a1b7ac237a587319a60` | `509e2cf29c701de29a63b8c3cad06a3a405ac30b1677cc04c680c91d65ceddd9` | `lab/governance/astra/packets/ATP_KXATPMATCH_SETTLED_JOIN_HARNESS/_prev/4de33473fd9bab9133ab30e55c7cfc409ee9c92b26d92a1b7ac237a587319a60.SOURCE_PINS.json` |
| `lab/governance/astra/packets/ATP_KXATPMATCH_SETTLED_JOIN_HARNESS/FROZEN_EXPERIMENT.json` | `802b40b308724ae0980da123843d6a0655d087af2f162b3cc3a0f66d25e1d690` | `382009b93b561f21e5942cf0aa5cfbc8ee21821ad4b89db66468bfbe7ad094dc` | `lab/governance/astra/packets/ATP_KXATPMATCH_SETTLED_JOIN_HARNESS/_prev/802b40b308724ae0980da123843d6a0655d087af2f162b3cc3a0f66d25e1d690.FROZEN_EXPERIMENT.json` |
| `lab/astra-science/kalshi_atp_kxatpmatch_settled_join_lab_20260924/FROZEN_EXPERIMENT.json` | `802b40b308724ae0980da123843d6a0655d087af2f162b3cc3a0f66d25e1d690` | `382009b93b561f21e5942cf0aa5cfbc8ee21821ad4b89db66468bfbe7ad094dc` | `lab/astra-science/kalshi_atp_kxatpmatch_settled_join_lab_20260924/_prev/802b40b308724ae0980da123843d6a0655d087af2f162b3cc3a0f66d25e1d690.FROZEN_EXPERIMENT.json` |
| `lab/astra-science/kalshi_atp_kxatpmatch_settled_join_lab_20260924/SOURCE_PINS.json` | `4de33473fd9bab9133ab30e55c7cfc409ee9c92b26d92a1b7ac237a587319a60` | `509e2cf29c701de29a63b8c3cad06a3a405ac30b1677cc04c680c91d65ceddd9` | `lab/astra-science/kalshi_atp_kxatpmatch_settled_join_lab_20260924/_prev/4de33473fd9bab9133ab30e55c7cfc409ee9c92b26d92a1b7ac237a587319a60.SOURCE_PINS.json` |
| `lab/astra-science/kalshi_c4_kxcpi_settled_join_lab_20260924/FROZEN_EXPERIMENT.json` | `b72465d809ccd208588ce13baa8749b8f5d1eedfb82abef47d261d84939b067f` | `968a46e3733bc17e58c223ccc71525e5090ff7a1204b7c2222de4353a3940191` | `lab/astra-science/kalshi_c4_kxcpi_settled_join_lab_20260924/_prev/b72465d809ccd208588ce13baa8749b8f5d1eedfb82abef47d261d84939b067f.FROZEN_EXPERIMENT.json` |
| `lab/astra-science/kalshi_c4_kxcpi_settled_join_lab_20260924/SOURCE_PINS.json` | `21df2532fd0c016ca17bd4b12e8e0eab06c18e05a2f2955e3fbe6004333c80ca` | `bcd27e06f57f0e6b617ce318fb6d42da8c9b0a526816fbc4e41cef07a875154c` | `lab/astra-science/kalshi_c4_kxcpi_settled_join_lab_20260924/_prev/21df2532fd0c016ca17bd4b12e8e0eab06c18e05a2f2955e3fbe6004333c80ca.SOURCE_PINS.json` |
| `lab/astra-science/kalshi_c4_kxcpi_settled_join_lab_20260924/README.md` | `748e59cd7c14313443916196b528afd904cba5065725b2ab5edd286de2223c0d` | `07a7ef310b1a78f7f2a2a6da3758d4f5786e1699bab09550dcb2ea6c2935991b` | `lab/astra-science/kalshi_c4_kxcpi_settled_join_lab_20260924/_prev/748e59cd7c14313443916196b528afd904cba5065725b2ab5edd286de2223c0d.README.md` |
| `lab/astra-science/kalshi_atp_kxatpmatch_settled_join_lab_20260924/README.md` | `39f555bf1e560a5da3a42cff204431abcd707cbe2471888ba28e70824917c2f8` | `a37834ea27c56aa1d3568657815df992c15cdf4b22c27abaa7fa25f5c4f72b36` | `lab/astra-science/kalshi_atp_kxatpmatch_settled_join_lab_20260924/_prev/39f555bf1e560a5da3a42cff204431abcd707cbe2471888ba28e70824917c2f8.README.md` |

Record of the packet-dir edits: `lab/governance/astra/steward/RULING2_REALIGN_RECORD_2026-10-01.json` (sha256 `3bb3696927b87eca53011bf69b335130351d585c740ecaaad90320086a57f02a`).

Residual (not edited): box-only `DIGESTS.txt` in both packet dirs (desk-bundle digest records) still list the pre-harness FROZEN hashes. They are historical records; whether to annotate them is the Archivist's call [V/I]. The box packet dirs have no `README.md`, while main has one; that file is missing on the box rather than divergent [V].

## Ruling 3 — Branches
Primary repo `17thgreen/GPT-6-Astra-Deathmatch`: 21 heads (main plus 20). Open PRs: 0 (60 PRs, all closed) [V]. Fleet repo: `main` only, 0 open PRs [V]. GauntletV2: `main` plus `cursor/lab-sync-remaining-inventory-f89f` (head of open draft PR #1, which **must not** be deleted) [V].

**Status: deletions NOT performed. BLOCKER:** this session has no CloudAgent tool (no `cursor` namespace; an MCP catalog search for cloud/agent returned nothing), and the rules require repo writes to go through a cloud agent. No other route was attempted. The 14 branches below were verified eligible (each tip == `refs/pull/N/head`, PR closed, no open PR) [V]:

| branch | tip | PR | PR state |
|---|---|---|---|
| `cursor/amendment-b-hash-register-extract-9af5` | `a91f2389b594` | #56 | merged |
| `cursor/atp-kxatpmatch-feequue-harness-cb69` | `c1df03e021f9` | #35 | closed_unmerged |
| `cursor/atp-kxatpmatch-measure-hardening-infra-94b4` | `38eefc93683a` | #57 | merged |
| `cursor/atp-rj-kxatpmatch-join-harness-2149` | `f499ee306228` | #54 | merged |
| `cursor/c1-kxufcfight-meas-scaffold-63a7` | `fc246f12a859` | #17 | closed_unmerged |
| `cursor/c3-kxhighny-meas-scaffold-aa1e` | `07b6df8e277f` | #16 | closed_unmerged |
| `cursor/nhl-kxnhlgame-settled-join-d697` | `515e5474d923` | #43 | closed_unmerged |
| `cursor/q6s1-kxatpmatch-inventory-reproof-4016` | `e709b98a0914` | #59 | merged |
| `cursor/q6s5-kxmlbspread-feequue-harness-281e` | `f8409201594a` | #58 | merged |
| `cursor/q6s5-strategy-fill-path-90d3` | `f8264ad79367` | #60 | merged |
| `cursor/q7-reconciliation-memo-bd6a` | `9ca0cc1532d3` | #51 | merged |
| `cursor/r3-p3-fl-maker-taker-scaffold-af29` | `1332fad5dbe1` | #15 | closed_unmerged |
| `cursor/ready-not-scored-status-docs-3be0` | `fa9a01d31070` | #53 | merged |
| `cursor/tier-a-results-q7-r3p2-3be0` | `0cbe603c4d83` | #55 | merged |

Skipped:
- `cursor/r2p1-fixture-join-q6-000-ede3` @ `7224ad882431` (PR #8 head `9a0acafb`): tip 7224ad88 != PR8 head 9a0acafb; 2 commits (c6bb876 "Move the Q6-000 fixture join into the hygiene lab", 7224ad8 "Record the one-lab fixture-join unit timing", 2026-09-22 19:43:03 ET, Cursor Agent) not in main and not reachable from any refs/pull/*/head -> NOT recoverable; HOLD [V]
- `main`: never deleted. `research/*` ×5: HOLD per ruling.

Proposed cloud-agent instruction (one agent, primary repo only): *"For each branch in [the 14 above], GET `refs/heads/<b>` and confirm the sha equals the listed tip and equals `refs/pull/<N>/head`, and that the PR has no open state. Only then `DELETE /repos/17thgreen/GPT-6-Astra-Deathmatch/git/refs/heads/<b>`. Never touch main, research/*, or cursor/r2p1-fixture-join-q6-000-ede3. Report the deleted list and the post-delete `list_branches`."* The Steward will confirm afterwards with `git ls-remote`.

**research/* HOLD (no PR, no delete):**

| branch | last commit | author | date (ET) | message | ahead/behind main |
|---|---|---|---|---|---|
| `research/all-market-structure-20260924` | `cba057e62b3162bbf5cab17f4e2fee532a209ddc` | 17thgreen | 2026-09-24 02:21:28 ET | Report original gap strategy windows, capacity and $5,000 sensitivity | +39 / −12 |
| `research/neglected-hybrid-20260924` | `2253c03cd86eb5515325f1d91b43bdcbea7a902c` | 17thgreen | 2026-09-24 01:31:47 ET | Preserve original CSV line endings for byte-exact offline reproduction | +6 / −12 |
| `research/m2-continuation` | `f44574e8f318920cc8fdf87c9c3d35c18bca2107` | 17thgreen | 2026-09-22 15:33:05 ET | Freeze M4 tested source, exact cohorts and retained capture blockers before outcomes | +20 / −55 |
| `research/q8-joint-routing` | `d7079b6fece902e6e4603114a1d9ed5ef5a246c5` | 17thgreen | 2026-09-22 13:51:39 ET | Freeze eight-game NCAAF/WNBA cohort and bounded capture before tape download | +12 / −55 |
| `research/q7-paired-price` | `01c726ae9244d801d359e00df67d6a71f4012669` | 17thgreen | 2026-09-21 14:29:16 ET | Record verified Q7 results and freeze simpler guarded router | +3 / −55 |

`delete_branch_on_merge`: untouched (still false; Conductor raises it with Logan).

## Ruling 4 — GauntletV2 sync diagnosis (no routine or script changed)
**Root cause (best supported):** the daily sync has **no working write path for the payload it must land** [I, from the facts below]. The routine's own error text is not visible on the box [U].
1. **No box-side routine definition or run log.** Every agent `automations/` folder on the box is empty. The Conductor's prompt snapshot says "No routines yet". The routine runs server-side, so its 17:44 ET error string cannot be read here [V].
2. **Box git/gh are unauthenticated.** `gh auth status` reports not logged in. There is no `~/.git-credentials` and no `~/.config/gh`. A dry-run push to GauntletV2 fails with `could not read Username for https://github.com` (dry-run, nothing sent) [V]. Any routine step using `git push` or `gh` fails deterministically [V].
3. **The MCP write path cannot carry the backlog.** `user-GitHub-xai` is authenticated as `17thgreen` (owner) [V]. But the 10 deferred `lab/harness/examiner/src/run_*.py` (27,221–41,276 B each) are still **missing** on GauntletV2 `main` [V], and SYNC_NOTE 09-21/09-22 record a ~27 KB inline MCP payload ceiling [V doc / I limit]. A routine that must land them fails the same way every day. This fits a failure series that started 09-23/24, before the box rehydrate [H, strong].
4. **Staging paths moved.** The box was rehydrated 2026-09-27 09:32–09:40 ET (`/tmp/sand-copy-in.log`) [V]. `/workspace/gauntlet_sync_20260922/manifest.json` still points batches at `/tmp/gauntlet_sync_20260922/batch_*.json`, which no longer exist [V]. This breaks any run since 09-27 that replays the manifest [I].
5. **MCP server rename.** The sync notes name `user-Github`; the live namespace is `user-GitHub-xai` (also `cursor-github`) [V]. A saved prompt that pins the old name would fail [H].
6. **Common-mode signal.** PULSE 2026-10-01 18:48 ET says the hourly pulses also failed around 17:45 ET today, and the desk had a ~49 h conveyor gap. Part of today's failure may be routine-runner-wide, not sync-specific [I].

Last success: GauntletV2 `main` `61e284fb` "lab sync 2026-09-22: micro 22/22", 2026-09-22 18:09:45 ET. No commits since [V]. Remote refs and branch names are as expected (`main`, tag `gauntlet-v2.0-alpha`) [V].

**Proposed fix (for the routine owner; not applied):**
1. Copy the 10-01 17:44 ET run error from the routine's run history into `lab/governance/astra/steward/` to confirm which of causes 2, 3 and 5 fired.
2. Change the routine prompt:
   - (a) Use ONE Cursor cloud agent on `17thgreen/GrokBot---The-GauntletV2-` as the write path. It has a real git checkout and push rights, so it bypasses both the 27 KB MCP ceiling and the logged-out `gh`. It commits the day's sync on `sync/lab-<date>` and fast-forwards main, or opens a PR, per Logan's policy.
   - (b) If MCP stays the path, use `user-GitHub-xai` `push_files` with batches of 20 KB or less. Skip and log any file over 25 KB instead of aborting.
   - (c) Rebuild the file list each run from `/workspace/lab/...` against a GauntletV2 tree diff. Never read `/tmp` or the stale `manifest.json`.
   - (d) Fail-soft: write per-file status to `lab/governance/astra/steward/GAUNTLET_SYNC_<date>.log`, and mark the run failed only if the diff is non-empty and zero files landed.
   - (e) Keep the never-push guard (`evidence_private/`, `source_probe_electindex/`, keys/PEM/Key IDs, `*.docx`, raw ticks, ndjson/parquet over 1 MB, `/tmp`) and pre-scan every batch.
3. Optional (Logan decision): a fine-grained PAT with contents:write on GauntletV2 only, set up via `gh auth login`, so box-side git can push.

**GauntletV2 PR #1:** open, **draft**, "lab sync 2026-09-14: SYNC_REMAINING inventory". Head `cursor/lab-sync-remaining-inventory-f89f` @ `1eb0176689be41ba9411e0fd5238c431b330868c` (2026-09-14 18:49:46 ET). Base `main` (PR-object base sha `99accb4a`, merge-base `f62bb11e`). It is **121 commits behind** main `61e284fb`, 1 ahead, 1 file (+194, `lab/archive/audit/SYNC_REMAINING_2026-09-14.md`). GitHub reports mergeable_state=clean. Not refreshed, closed, or commented [V].

## ElectIndex / private leakage check — PASS
- Nothing was committed, branched, PR'd or pushed by this run [V].
- Path scan: main plus all 60 `refs/pull/*/head` plus every fetched remote-tracking ref. 0 paths match `evidence_private|source_probe_electindex|electindex`. GauntletV2 main and PR #1 also show 0 [V].
- Byte scan: the 31 non-empty files under `lab/evidence_private/` and `…/source_probe_electindex/` hashed as git blobs share 0 blobs with main and 0 with all 2,503 blobs across fetched refs [V].
- Content mentions on main exist only in the hash-only card01 manifests and the PR54 merge note (allowed per HYGIENE §7) [V].
- The new `_prev/` copies are box-only, and none involve evidence_private [V].

## Blockers / open items
1. **R3 deletions blocked:** no CloudAgent tool in this session. The 14-branch list and instruction are above, ready for the parent or Conductor to launch [V].
2. **R4:** the routine error text is needed to confirm the root cause. Prompt changes belong to the routine owner (Steward changed nothing) [U].
3. Archivist: old→new sha pairs above. Optional annotation of the box-only `DIGESTS.txt` files.
4. `cursor/r2p1-fixture-join-q6-000-ede3` holds 2 unrecoverable commits. Its owner should decide whether to PR or archive them before any delete.

## Addendum 2026-10-01 19:07 ET — Ruling 3 executed
Cloud agent bc-217893c7-b413-5586-9f10-27f66cc91752 re-verified the 14 branches and deleted all of them; 14/14 passed [V]. Each tip equals refs/pull/N/head and is recoverable from its PR; none is an ancestor of main. No files changed, no PR opened. main is unchanged at 12e760f5.
Remaining remote branches: main; cursor/q6s5-fl-band-settled-tape-c65b (open PR #61, 8c6f8430); cursor/r2p1-fixture-join-q6-000-ede3 (7224ad88, unrecovered commits, held); 5 research/* (held).
