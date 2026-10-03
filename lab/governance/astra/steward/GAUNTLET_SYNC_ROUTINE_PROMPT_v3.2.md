# GauntletV2 repo sync, routine prompt (v3.2 rev6)

Author: The Steward. v3 written 2026-10-01 22:55 ET; v3.1 written 2026-10-02 ~03:20 ET after the second placeholder-corruption incident (run `sync-20261002-0248`), revised ~03:30 ET per Conductor (no in-run retries, absolute write cutoff, live-schema-only encoding exception) before pinning. Conductor installs and pins this prompt. The Steward does not edit the routine.
v3 replaces v2 in full. v2 (sha256 `bb0a90e567c44be76928759b3d6aa20b8effd1beff9a8663f4a8c1e688ed7a66`) was reconstructed from the Steward's own record while the box was re-hydrating. The box copy then came back byte-identical (sha256 verified 23:21 ET), so the base is confirmed. v3 = v2 + changes (a)–(e) from Conductor's 2026-10-01 incident ruling, marked **[v3]**.
v3.1 = v3 (sha256 `cc0a17895d32a2e3ca97bce915849a4405c402dcdd0f514c3d97665f53484ed2`) + changes marked **[v3.1]**: the inline-content rule, the pre-call self-check, BAD_ON_MAIN (with cross-run quarantine), a 12 KB inline cap, an absolute write cutoff, and **no in-run repair or retry of any kind**.
v3.2 = v3.1 (sha256 `df2f54a65ad1d2a0611e446d4bd6cac0df098402a54b838d35ac3fef1aa52997`) + changes marked **[v3.2]**, accepted in principle by Conductor (2026-10-02 19:14 ET ruling on STEWARD_SYNC_ANALYSIS_2026-10-02): a fixed gate order (compare with main, then binary, then size), one fixed classifier embedded in this file, timestamped RUN_START/RUN_END, never_push globs for live/state files, an explicit box-only never_push list (including `**/ARCHIVIST_ELECTINDEX_*`, Conductor ~19:20 ET), and DEFERRED_LIVE. Per Conductor's 2026-10-03 ~04:53 ET ruling, v3.2 also requires (a) **every `*.md` to be byte-exact only** (`DEFERRED_MD_BYTE_EXACT`; never pushed inline) and (b) never-push paths already on main to be logged `SKIPPED_NEVER_PUSH_ON_MAIN` (never BAD_ON_MAIN, never an alert), with stale register entries `RETIRED`. Per Conductor's 2026-10-03 ~04:57 ET ruling, the whole `steward/LOSS_INVENTORY_2026-10-01*` family is box-only. Changes marked **[v3.2 OPTIONAL]** are Steward additions that Conductor may strip before pinning. Proposed by the Steward 2026-10-02 ~19:30 ET; Conductor installs and pins.
**[rev5] v3.2 rev5** (Conductor ask 2026-10-03 ~10:58 ET, after run `sync-20261003-1050` FAILED with 3 BAD_ON_MAIN and Conductor PAUSED v3.1): **this routine never writes to the repo.** It classifies, logs, reports and writes one landing manifest per run. Every landing goes through one combined byte-exact real-checkout PR that Conductor arranges, verifies and merges (§7). Text marked **[rev5]** overrides any earlier v3.1/v3.2 text it contradicts. The v3.1 inline-write rules (old §7.1–7.5), the 30-file cap, the 420 s write cutoff and the post-write blob compare are retired.
**[rev6] v3.2 rev6** (Conductor accepted in principle 2026-10-03 ~15:07 ET): rev5 (sha256 `fce33b3b7ebf891a0a295d3a4cd601761e1af2167d144a00284bd4449fb6eaa6`) plus one never-push glob, `**/*status.json` (case-insensitive), minus any path Conductor has ruled pushable (none as of 2026-10-03). Trigger: `lab/governance/pulses/GV2_SYNC_ROUTINE_STATUS.json`, a routine status note outside `lab/data`, was `READY_FOR_BYTE_EXACT_PR` under rev5 and had to be dropped by hand from combined PR #2. Everything else in rev5 is unchanged.
It is written to you, the routine, for every future run.

---

## 0. Why this exists (read once, then follow the rules)

- **v1 failures:** every failed run before 2026-10-01 ended with the platform message "Activity task failed". The run died from a timeout or crash mid-run, caused by oversized files (the MCP inline ceiling is about 27 KB) and a stale manifest. v2 made runs small, bounded, self-diffing, logged as they go, and quiet.
- **[v3] Box rebuild:** on 2026-10-01 at about 22:24 ET the box was rebuilt and `/workspace` was re-hydrated from the box store over a long period. The 22:42 run found the prompt missing and paused, which was correct. v3 adds hard guards so a wiped, partial or re-hydrating box can **never** be read as "the box deleted these files".

- **[v3.1] Placeholder corruption (2026-10-02, second incident; the first was repaired by cloud agent bc-c724bb2f).** In run `sync-20261002-0248`, 14 of the 15 files in batches 3–10 landed on GauntletV2 main as the 55-byte literal string `$file:/workspace/gauntlet_sync_work/run0248/bNN_fMM.txt` instead of their content (commits f53d289…84415bc, 03:00–03:01 ET).
  - **Mechanism:** the run staged each file's bytes to `run0248/bNN_fMM.txt`. Batches 1–2 (15 files, typed inline) verified fine. From batch 3, the first file of 12.9 KB, it switched to putting `"content": "$file:<path>"` into every `push_files` call (files of 0.3–19.8 KB), expecting the tool layer to expand it.
  - **The MCP call path performs no expansion.** It sends every argument verbatim, so the placeholder text itself became the file.
  - **What made it worse:** the in-run "repair" loop then made 10 more commits (03:04–03:19 ET). One inline re-push landed a truncated 248-byte prefix. A re-push of `$file:` repeated the corruption. A **base64** attempt landed 1,344 bytes of base64 text, because `push_files` has no encoding field.
  - **The cost:** the run took **1,678 s** against a ~600 s cap, and wrote 3 RUN_END lines. 6 files were left wrong on main at d989151d. **They were repaired externally** (from the box files, not from a196580) by commit `72875aafeabec5798828209cf58763af630f6a4d` (03:25 ET); each now matches its box blob. Conductor confirmed that the 03:04–03:19 commits were the 0248 run's own repair attempts. A small file pushed inline also landed **+1 byte** (AMD-20260911-PM-002.md, 2,799 → 2,800 B), which shows that retyped inline content can drift too.
  - **v3.1 therefore:**
    - forbids every indirect content form
    - caps inline content small enough to reproduce exactly
    - self-checks the payload before each call
    - verifies every pushed path after each call
    - marks any failed path BAD_ON_MAIN and **never retries it**, in this run or later runs, until a start-of-run read-only check shows it was fixed externally
    - defers every file over 12 KB to a real-checkout job; such files are never pushed inline
    - forbids base64 and other encodings unless the live tool schema explicitly says the tool decodes them
    - enforces an absolute write cutoff

- **[v3.2] Counting artifact (2026-10-02, runs 0442–1840).** `deferred_oversize` swung 45 → 129 → 77 → 130 → 130 → 115 → 136 → 46 and `in_sync` 515 → 664 with no matching box churn (one new oversize file all day). Each run wrote its own classifier, so:
  - the size gate sometimes ran **before** the comparison with main, counting up to 83 files already byte-identical on main as deferred instead of in sync;
  - the binary check ran before or after the size gate (5 PNG + 1 PDF flipped between deferred and skipped);
  - the scope walk varied: 7 `lab/data/*/provenance/CLOCK_AUDIT_*.json` files were omitted in 4 runs, and run 1840 refused 3 `DATA-PROV-TRADES-001/provenance/*.md` notes as "data-prov";
  - run 1645 logged 2 `ERROR precheck` for live `capture_status.json` files that the capture recorders rewrite every 20–40 s.

  v3.2 therefore fixes the gate order (§6), embeds one classifier that you run unchanged (§4.1), never pushes live/state files (§6 gate 1), logs hash drift as `DEFERRED_LIVE` instead of `ERROR`, and timestamps `RUN_START`/`RUN_END` (§8).
- **[v3.2] Inline retype drift: 3 drifts in 3 days, all `.md` files retyped inline.** In each case the box bytes were right and the retyped call was not:
  1. `lab/governance/AMD-20260911-PM-002.md`: run `sync-20261002-0248`, +1 byte (2,799 to 2,800 B).
  2. `lab/data/DATA-PROV-CF-001/provenance/CLOCK_AUDIT_W2A_CF_T14_JOIN.md`: run `sync-20261002-1840`. The scratch JSON was correct (blob `32d5f03c`), but a `## Verdict recommendation (join only)` heading and the blank line before it landed as a `- **…**` bullet (10,018 to 10,020 B, blob `5229a5da`, commit `aa9f0f0e`). Repaired externally by `a6af2420`.
  3. `lab/data/DATA-PROV-L3-001/provenance/CLOCK_AUDIT_W2E_STRIKE_L3_JOIN.md`: run `sync-20261003-0445`. Same length (7,445 B), but 2 bytes changed: `[V]/ no revision feed` became `[V]; no revision feed` twice (expected blob `792d9169`, landed `6780d1c4`, commit `386be3a2`).

  The mangling differs each time (one extra byte, a heading rewritten, punctuation changed), so no content-pattern rule can catch it. v3.2 therefore **never pushes any `*.md` inline** (§6 G5). Every changed `.md` is labelled `DEFERRED_MD_BYTE_EXACT` and left for a separate byte-exact real-checkout job. Post-push verification caught all three, but only after they had landed. **[rev5: superseded.** No file is pushed inline at all; see the next item and §7.**]**

- **[rev5] Inline writes drifted on `.json` too: 5 wrong files on GauntletV2 main in 2 days, plus the `$file:` incident.** Box bytes were right every time; the inline write call was not.

  | # | path (under `lab/`) | type | box size | written by | what landed on main |
  |---|---|---|---|---|---|
  | 1 | `governance/AMD-20260911-PM-002.md` | `.md` | 2,799 B | inline `push_files`, run `sync-20261002-0248` (v3) | +1 byte (2,800 B) |
  | 2 | `data/DATA-PROV-CF-001/provenance/CLOCK_AUDIT_W2A_CF_T14_JOIN.md` | `.md` | 10,018 B | inline, `sync-20261002-1840` (v3.1) | heading rewritten as a bullet; blob `5229a5da`, commit `aa9f0f0e`; repaired `a6af2420` |
  | 3 | `data/DATA-PROV-L3-001/provenance/CLOCK_AUDIT_W2E_STRIKE_L3_JOIN.md` | `.md` | 7,445 B | inline, `sync-20261003-0445` (v3.1) | 2 punctuation bytes changed, same length; blob `6780d1c4`, commit `386be3a2`; repaired `06d04867` |
  | 4 | `data/DATA-PROV-PM-003/provenance/CLOCK_AUDIT_REPORT.md` | `.md` | 11,735 B | inline, `sync-20261003-1050` (v3.1) | the 24-byte literal `PLACEHOLDER_WILL_REPLACE`; blob `987bf95f`, commit `5cba80f8` |
  | 5 | `data/DATA-PROV-PM-003/provenance/CLOCK_AUDIT_W2C_SIBLING_JOIN.json` | static `.json` | 12,021 B | inline, `sync-20261003-1050` (v3.1) | same length, 3 lines reworded (`p_t := m_t (own mid)` became `own mid (p_t := m_t)`); blob `a1ea1c6c`, commit `76883e2c` |

  Also: run `sync-20261002-0248` (v3) landed 14 files, including `.py` sources, as a 55-byte `$file:` placeholder (above). `DATA-PROV-CB-002/provenance/capture_status.json` (BAD_ON_MAIN since `sync-20261003-0445`) is a live file that changed after it was pushed, not a retype; it has been never-push since v3.2.

  So the drift is not limited to `.md`. A static `.json` under the 12 KB cap drifted, and a placeholder landed under v3.1's explicit ban (#4). Post-write verification caught #2–#5, but only after the wrong bytes were already on main. **rev5 therefore removes every inline write.** The routine only classifies and lists. Landings happen only through the byte-exact PR (§7), which checks blobs before the commit and again after landing.

If you ever feel tempted to "just push everything", or to "mirror the box state including deletions", or to "just re-push it a different way", that is the failure mode. Don't.

## 1. Run gate: prompt pin, cadence [rev5: namespace step retired]

1. **[v3] Prompt pin.**
   - Compute sha256 of this file, `/workspace/lab/governance/astra/steward/GAUNTLET_SYNC_ROUTINE_PROMPT_v3.2.md`. **[v3.2: file name]**
   - Compare it to Conductor's pin, `PROMPT_SHA256=<hex>`. The pin is supplied in the routine launcher, outside this file; a file cannot hold its own hash.
   - **If the file is missing, or its sha differs from the pin, or no pin was supplied:** do nothing else. Write no log, call no GitHub tool, and **ping Logan**: `GauntletV2 sync: prompt <MISSING|SHA_MISMATCH|NO_PIN> (got <sha or ->, want <pin>) — routine stopped`. Then end.
2. **[v3] Cadence** (Conductor override, kept from v2): every 2 hours at minute :40, America/New_York. One run at a time. If a previous run's `RUN_START` has no matching `RUN_END` and is under 15 minutes old, end silently.
3. **[rev5] Namespace: retired.** This routine calls no GitHub write tool, so it no longer discovers `push_files` or looks up write schemas. `NAMESPACE_UNAVAILABLE` is retired. The only GitHub access is reading main (§4 step 1).

4. **[v3.1] Clock.** Record `t0` (monotonic, plus ISO time ET) **before** step 1. Every time limit in this prompt is measured from `t0`, so it includes the tree fetch, the classifier, logging and reporting (§7.4).
   - **[v3.2]** Record `t0` as both ISO time ET (`TZ=America/New_York date +%Y-%m-%dT%H:%M:%S%:z`) and integer epoch seconds (`date +%s`). Write them to `/workspace/gauntlet_sync_work/t0_iso.txt` and `t0_epoch.txt`. Both appear in `RUN_START` (§8), and `t0_epoch` is passed to the classifier (§4.1).
5. **[v3.1] BAD_ON_MAIN re-check (start of run, read-only).**
   - Build the BAD_ON_MAIN register: every path with a `BAD_ON_MAIN` line in **any** `GAUNTLET_SYNC_*.log` that has no later `REPAIRED` (**[v3.2]** or `RETIRED`) line, **plus** the §12 seed list (until each seed path has a `REPAIRED` line). There is no age limit; a path stays quarantined until it is logged `REPAIRED` (**[v3.2]** or `RETIRED`, for never-push paths only).
   - Compare each path's current GauntletV2 main blob (from the §4 tree) with `git hash-object` of the box file.
     - Equal → log `REPAIRED` (with the remote blob).
     - Different → log `BAD_ON_MAIN` again with both shas.
   - **[v3.2] Register entries that are never-push paths are retired, not re-flagged.** A never-push path is never written by this routine, so a mismatch for it is stale, not a repair need (example: `DATA-PROV-CB-002/provenance/capture_status.json`, BAD_ON_MAIN in `sync-20261003-0445`, ruled STALE_LIVE_ACCEPTED). For every register path listed in the classifier's `register_never_push` (§4.1):
     - log `RETIRED never_push:<rule>` once, instead of `REPAIRED` or `BAD_ON_MAIN`;
     - from then on it is off the register (a `RETIRED` line counts like a later `REPAIRED` line);
     - it is not an alert, and it is not included in `bad_on_main`.
   - **[v3.2]** The `REPAIRED`, `BAD_ON_MAIN` and `RETIRED` lines of this step are written once the pre-flight (§3) has passed and the classifier has run.
   - **Exclude** still-bad paths from this run's pending list. **[v3.2]** Write them, one repo path per line, to `/workspace/gauntlet_sync_work/quarantine.txt` (an empty file if none) and pass that file to the classifier (§4.1), which labels them `BAD_ON_MAIN_OPEN`. The routine **never writes** a BAD_ON_MAIN path, in any form, in this run or any later run, until this read-only check logs it `REPAIRED`. Repair is always external (a cloud-agent or real-checkout job that Conductor launches). This check only reads.
   - Every open BAD_ON_MAIN path is included in this run's alert (§10).
   - **[rev5] New BAD_ON_MAIN paths** come from the classifier label `BAD_ON_MAIN_NEW` (§6 G6), not from a post-write check (this routine no longer writes). Log each as `BAD_ON_MAIN` with `expected=<box blob> got=<main blob> commit=- detected=drift prev_main=<sha or ->`. From the next run on, it is on the register like any other BAD_ON_MAIN path.

## 2. Fixed facts

- **Source:** `/workspace/lab` on the box. The box is the source of truth for **content**. It is **not** the source of truth for **existence** (see §4a).
- **Target:** `17thgreen/GrokBot---The-GauntletV2-`, branch **`main`**. **[rev5]** Read-only for this routine: it never commits, pushes, branches or opens a PR. Files land only through the byte-exact PR in §7, which Conductor arranges, verifies and merges.
- **Log:** `/workspace/lab/governance/astra/steward/GAUNTLET_SYNC_<YYYY-MM-DD>.log` (America/New_York date). Append only; create it if missing. This applies only after the pre-flight in §3 passes.
- **Forbidden inputs:**
  - never read a file list from `/tmp`
  - never use `/workspace/gauntlet_sync_20260922/manifest.json` or any saved manifest as the to-do list
  - never resume from memory

  The diff (§4) is the only to-do list. **[rev5]** The landing manifest (§7.2) is this routine's output, never its input. The one exception is the previous run's `classified_<run_id>.json`, which is passed to the classifier for drift detection only (§4.1).

## 3. [v3] Pre-flight guard: is the box complete?

Run this **before any write, including the log**. If any check fails:
- outcome = **`ABORTED_BOX_INCOMPLETE`**
- write **nothing**: no log line, no GitHub call
- **alert Conductor** with the failing check(s) and their numbers
- send the Steward the non-priority note (§10)
- end

| check | abort if |
|---|---|
| G1 | `/workspace/lab/governance/astra/packets/` does not exist, or contains fewer than 100 files |
| G2 | `/workspace/lab/governance/astra/steward/` does not exist |
| G3 | box re-hydration in progress: `/tmp/sand-copy-in-status.json` exists and its `phase` is not a finished state (anything other than `complete`/`completed`/`done`/`idle`), or `restored < total` |
| G4 | in-scope box file count (classifier `in_scope_total`, §4.1) < **75 %** of the number of files under `lab/` on GauntletV2 main (classifier `main_lab_files`) **[v3.2: values from the classifier]** |
| G5 | more than **25** MISSING_ON_BOX paths (§4a; classifier `missing_on_box`) in one run. A real edit seldom removes more than a few files; a wipe removes hundreds. |

G4 and G5 need the remote tree (§4 step 1) and the classifier output (§4.1). Reading the tree and running the classifier (which writes only its own JSON **[rev5]** and the landing manifest under `/workspace/gauntlet_sync_work/`) are allowed before the guard decision; writing the log is not. **[rev5]** A manifest from an aborted run is void: no `RUN_END` names its sha256, and the PR uses only a manifest whose sha256 appears in a `SUCCESS_CLASSIFIED` `RUN_END` line (§7.2).

## 4. Build the pending list fresh, every run

1. **Read GauntletV2 main's tree.**
   - **[v3] Cache location may be missing.** Do not assume `/workspace/gauntlet_sync_cache.git` exists or is healthy. If it is missing, or `git -C … rev-parse` fails, rebuild it:
     - `git init --bare /workspace/gauntlet_sync_cache.git`
   - Each run:
     - `git -C /workspace/gauntlet_sync_cache.git fetch --filter=blob:none --depth=1 https://github.com/17thgreen/GrokBot---The-GauntletV2-.git +refs/heads/main:refs/heads/main`
     - (`--filter=tree:0` is also acceptable)
     - then `git -C … ls-tree -r main`
   - **Never pass `-l` to `ls-tree` on this cache.** It lazily downloads every blob and hangs the run.
   - Never place the cache under `/tmp`.
   - Fallback: MCP `get_repository_tree` for `main`, recursive (schema looked up first). **[v3.2]** The classifier (§4.1) reads only the cache, so if the cache cannot be fetched, the run stops as `CLASSIFIER_MISMATCH` (no write).
2. **[v3.2] Run the fixed classifier (§4.1).** It walks the box (skipping symlinks; pruning `.venv*`, `__pycache__`, `.git`, `node_modules`), applies the §5 scope, computes each file's **git blob sha** = `sha1("blob " + <byte length> + "\0" + <bytes>)` and sha256, compares it with main (same blob → `IN_SYNC`; path absent → NEW; different blob → MODIFIED), applies the §6 gates in their fixed order, sorts all rows by path **[rev5]**, and writes the landing manifest (§7.2).
3. **[v3.2] Do not write, edit, extend or re-implement any classifier, scope walk or gate script of your own, and do not re-label or re-count its output.** Its labels and counts are the run's labels and counts (§8). If it fails, outcome `CLASSIFIER_MISMATCH` (§4.1).
4. Scratch files go only under `/workspace/gauntlet_sync_work/`, never `/tmp`. Create that directory if it is missing.

### 4.1 [v3.2] The fixed classifier

1. **Extract** the code block between the exact lines `# >>> CLASSIFIER v3.2 BEGIN` and `# <<< CLASSIFIER v3.2 END` (both included) from this prompt file, with this command and no other method:
   `python3 -c "import sys;L=open(sys.argv[1],encoding='utf-8').read().split('\n');s=L.index('# >>> CLASSIFIER v3.2 BEGIN');e=L.index('# <<< CLASSIFIER v3.2 END');open(sys.argv[2],'w',encoding='utf-8').write('\n'.join(L[s:e+1])+'\n')" /workspace/lab/governance/astra/steward/GAUNTLET_SYNC_ROUTINE_PROMPT_v3.2.md /workspace/gauntlet_sync_work/classify_v3_2.py`
2. **Check** `sha256sum /workspace/gauntlet_sync_work/classify_v3_2.py` equals **`21ed95774bbb4b20be6a4a51b29bafb92b6bd5f25d16409af56839af753d2185`** **[rev6]**. If it differs, or the classifier exits non-zero, outcome = **`CLASSIFIER_MISMATCH`**: write the log `RUN_START` and `RUN_END` only, alert Conductor (§10), end.
3. **[rev5] Run** `python3 /workspace/gauntlet_sync_work/classify_v3_2.py <t0_epoch> /workspace/gauntlet_sync_work/classified_<run_id>.json /workspace/gauntlet_sync_work/quarantine.txt <prev> /workspace/gauntlet_sync_work` after the tree fetch (§4 step 1) and the BAD_ON_MAIN register build (§1 step 5). It reads `/workspace/lab` and the cache tree only, writes `classified_<run_id>.json` and the landing manifest (§7.2), and prints one summary line.
   - `<prev>` is the newest `/workspace/gauntlet_sync_work/classified_<run_id>.json` from an earlier run whose `RUN_END` has `outcome=SUCCESS_CLASSIFIED` and whose `summary.classifier` is `v3.2r5` or **[rev6]** `v3.2r6` (same row format). If there is none, pass `-`.
4. **Output:**
   - `summary`: `in_scope_total`, `in_sync`, `skipped_never_push`, `skipped_never_push_on_main`, `bad_on_main_open`, `bad_on_main_new`, `deferred_live`, `ready_for_pr`, `ready_md`, `ready_s`, `ready_m`, `ready_l`, `ready_xl`, `missing_on_box`, `main_lab_files`, `main_head`, `manifest_path`, `manifest_sha256`, `manifest_rows`.
   - `missing_on_box`: paths.
   - `never_push_on_main_unclassified`: never-push paths on main with no in-scope box row.
   - `register_never_push`: `{path: rule}` for `quarantine.txt` paths that match a never-push rule (§1 step 5).
   - `files`: one row per in-scope box file (`path size sha256 blob mtime main_blob state size_class ext label message`), sorted by path.

   Labels **[rev5]**: `IN_SYNC`, `SKIPPED_NEVER_PUSH`, `SKIPPED_NEVER_PUSH_ON_MAIN`, `BAD_ON_MAIN_OPEN`, `BAD_ON_MAIN_NEW`, `DEFERRED_LIVE`, `READY_FOR_BYTE_EXACT_PR`. Every in-scope file gets exactly one label, so `in_scope_total` = the sum of the seven label counts (the classifier asserts this). The rev4 labels `DEFERRED_MD_BYTE_EXACT`, `DEFERRED_OVERSIZE` and `PENDING` are retired; those files are all `READY_FOR_BYTE_EXACT_PR`, tagged with `size_class` and `ext`.
5. **Logging [rev5]:** write one per-file log line (§8) for every row labelled `SKIPPED_NEVER_PUSH`, `SKIPPED_NEVER_PUSH_ON_MAIN` or `DEFERRED_LIVE`, with the classifier's `message`, and one `BAD_ON_MAIN` line per `BAD_ON_MAIN_NEW` row (§1 step 5).
   - `IN_SYNC` and `READY_FOR_BYTE_EXACT_PR` rows are counted only. The manifest is the list of ready files; log one aggregate `LANDING_MANIFEST` line for it (§8).
   - `BAD_ON_MAIN_OPEN` rows are logged by §1 step 5.
6. The only inputs are this prompt, `/workspace/lab`, the cache tree, `t0_epoch`, `quarantine.txt` and `<prev>`. There are no tunables; changing a rule means a new prompt version.

```python
# >>> CLASSIFIER v3.2 BEGIN
# GauntletV2 sync classifier, fixed for prompt v3.2 rev6. Do not edit, re-implement or re-type.
# Usage: python3 classify_v3_2.py <t0_epoch> <out_json> <quarantine_paths_file> <prev_classified_json or -> <manifest_dir>
# Read-only on /workspace/lab and the cache tree. Writes only <out_json> and the landing manifest
# <manifest_dir>/GV2_LANDING_MANIFEST_<t0 ET, YYYYMMDDTHHMMSS-hhmm>.json (box-only, never pushed).
# rev5: this routine never writes to the repo. Every file that needs to land is listed in the manifest
# for ONE byte-exact real-checkout PR that Conductor arranges, verifies and merges.
import os, re, sys, json, hashlib, subprocess, datetime, zoneinfo
ROOT = "/workspace/lab"
CACHE = "/workspace/gauntlet_sync_cache.git"
ET = zoneinfo.ZoneInfo("America/New_York")
CLASS_S = 12288         # size class S: <= 12 KB
CLASS_M = 25600         # size class M: <= 25 KB (also the csv never-push threshold)
CLASS_L = 1048576       # size class L: <= 1 MiB; XL above (needs Conductor's explicit OK in the PR)
LIVE_WINDOW = 900       # 15 min before t0
TEXT_EXT = (".py", ".md", ".json", ".yaml", ".yml", ".toml", ".txt", ".cfg", ".ini", ".sh")
PROMPT_RE = re.compile(r"^lab/governance/astra/steward/GAUNTLET_SYNC_ROUTINE_PROMPT_[^/]*\.md$")
MANIFEST_LABELS = ("READY_FOR_BYTE_EXACT_PR", "BAD_ON_MAIN_NEW", "BAD_ON_MAIN_OPEN")

def in_scope(rel):
    # rel is relative to lab/, e.g. "governance/x.md". Fixed scope (prompt 5).
    p = rel.split("/")
    if p[0] == "governance":
        if rel.startswith("governance/astra/packets/"):
            sub = p[3:]
            return sub[0].endswith(".md") if len(sub) == 1 else sub[0] == "extracts"
        return not re.match(r"governance/astra/steward/GAUNTLET_SYNC_[^/]*\.log$", rel)
    if p[0] in ("archive", "execution"):
        return True
    if p[0] == "harness":
        if any(x in ("results", "out", "runs", "data") or x.startswith(".venv") for x in p[1:-1]):
            return False
        return rel.endswith(TEXT_EXT)
    if p[0] == "data":
        if any(x in ("raw", "slices", "sealed") for x in p):
            return False
        # every *.md (incl. DATA-PROV-TRADES-001/provenance/*.md) and every
        # provenance/*.json (incl. CLOCK_AUDIT_*.json) is in scope
        return rel.endswith(".md") or (rel.endswith(".json") and len(p) >= 3 and p[-2] == "provenance")
    return False

BOX_ONLY = {  # explicit never_push files (Conductor rulings 2026-10-01/02; see also PATH_RULES)
    "lab/governance/astra/packets/ARCHIVIST_SOURCE_GATE_ELECTINDEX_CARD01_2026-09-24.md": "box-only:electindex-note",
    "lab/governance/astra/steward/LOSS_INVENTORY_2026-10-01.json": "box-only:loss-inventory-json",
}
PATH_RULES = [  # (rule name, regex on repo path); first match wins
    ("evidence_private", r"(^|/)evidence_private/"),
    ("box-only:_prev", r"(^|/)_prev/"),
    ("box-only:archivist-electindex", r"(^|/)ARCHIVIST_ELECTINDEX_[^/]*$"),
    ("box-only:loss-inventory", r"^lab/governance/astra/steward/LOSS_INVENTORY_2026-10-01[^/]*$"),
    ("box-only:landing-manifest", r"(^|/)GV2_LANDING_MANIFEST_[^/]*$"),
    ("electindex-probe", r"/source_probe_electindex/"),
    ("live:status-json", r"^lab/data/.+/provenance/[^/]*status\.json$"),
    ("live:status-json-any", r"status\.json$"),   # rev6: **/*status.json, case-insensitive
    ("live:progress-json", r"(^|/)progress\.json$"),
    ("live:pid", r"\.pid$"),
    ("live:lock", r"\.lock$"),
    ("live:locks-dir", r"(^|/)\.locks/"),
    ("live:heartbeat", r"heartbeat[^/]*$"),
    ("live:sqlite-sidecar", r"-(wal|shm|journal)$"),
    ("live:temp", r"\.(tmp|partial|swp)$"),
    ("secret-file", r"(\.(pem|key|p12|pfx|docx)$)|(^|/)(id_[^/]*|\.env|\.env\.[^/]*)$"),
    ("raw-ext", r"(\.(ndjson|parquet|zip|gz|db|pyc)$)|\.sqlite[^/]*$"),
    ("data-prov-raw", r"/DATA-PROV-[^/]*/(raw|slices|sealed)/"),
    ("astra-science", r"^lab/astra-science/"),
]
# rev6: *status.json paths Conductor has ruled pushable (exempt from live:status-json-any only).
# None found in CONDUCTOR_RULING_*/CONDUCTOR_PIN_* packets or the steward rulings exec file (2026-10-03).
STATUS_JSON_PUSHABLE = frozenset()
SECRET = [
    ("private-key", rb"-----BEGIN[^\n]*PRIVATE KEY"),
    ("kalshi-access-key", rb"KALSHI-ACCESS-KEY\s*[:=]?\s*['\"]?[A-Za-z0-9\-]{8,}"),
    ("api-key", rb"(?i)api[_-]?key\s*[:=]\s*['\"][A-Za-z0-9_\-]{16,}"),
    ("sk", rb"sk-[A-Za-z0-9]{20,}"),
    ("ghp", rb"ghp_[A-Za-z0-9]{30,}|github_pat_"),
    ("alchemy", rb"alchemy\.com/v2/[A-Za-z0-9_\-]{10,}"),
    ("bearer", rb"Bearer [A-Za-z0-9\-_.]{20,}"),
]

def never_push(rp):
    if rp in BOX_ONLY:
        return BOX_ONLY[rp]
    for name, rx in PATH_RULES:
        if name == "live:status-json-any" and rp in STATUS_JSON_PUSHABLE:
            continue
        if re.search(rx, rp, re.I if name in ("secret-file", "raw-ext", "live:status-json-any") else 0):
            return name
    if "electindex" in rp.lower() and not (rp.startswith("lab/governance/") and rp.endswith(".md")):
        return "electindex"
    return None

def size_class(n):
    return "S" if n <= CLASS_S else "M" if n <= CLASS_M else "L" if n <= CLASS_L else "XL"

def main():
    t0 = int(float(sys.argv[1])); out = sys.argv[2]
    quarantine = {l.strip() for l in open(sys.argv[3], encoding="utf-8") if l.strip()}
    prev = {}
    if sys.argv[4] != "-":
        prev = {r["path"]: r for r in json.load(open(sys.argv[4], encoding="utf-8"))["files"]}
    mdir = sys.argv[5]
    head = subprocess.run(["git", "-C", CACHE, "rev-parse", "main"], capture_output=True, text=True, check=True).stdout.strip()
    ls = subprocess.run(["git", "-C", CACHE, "ls-tree", "-r", "main"], capture_output=True, text=True, check=True).stdout
    tree = {}
    for line in ls.splitlines():
        meta, path = line.split("\t", 1)
        tree[path] = meta.split()[2]
    rows = []
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = sorted(d for d in dns if not (d.startswith(".venv") or d in ("__pycache__", ".git", "node_modules")))
        for fn in sorted(fns):
            ap = os.path.join(dp, fn)
            if os.path.islink(ap) or not os.path.isfile(ap):
                continue
            rel = os.path.relpath(ap, ROOT)
            if not in_scope(rel):
                continue
            rp = "lab/" + rel
            b = open(ap, "rb").read()
            r = {"path": rp, "size": len(b), "sha256": hashlib.sha256(b).hexdigest(),
                 "blob": hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest(),
                 "mtime": os.stat(ap).st_mtime, "main_blob": tree.get(rp)}
            r["state"] = "IN_SYNC" if r["main_blob"] == r["blob"] else ("NEW" if r["main_blob"] is None else "MODIFIED")
            r["size_class"] = size_class(len(b))
            r["ext"] = os.path.splitext(fn)[1].lower() or "-"
            label, msg = None, "-"
            n = never_push(rp)                                   # G1 never-push path
            if n:
                # already present on main: listed, never BAD_ON_MAIN, never an alert
                label = "SKIPPED_NEVER_PUSH_ON_MAIN" if r["main_blob"] is not None else "SKIPPED_NEVER_PUSH"
                msg = n
            elif r["state"] == "IN_SYNC":                        # G2 compare with main
                label = "IN_SYNC"
            else:
                try:
                    b.decode("utf-8"); binary = b"\0" in b
                except UnicodeDecodeError:
                    binary = True
                if binary:                                       # G3 binary / non-UTF-8
                    label, msg = "SKIPPED_NEVER_PUSH", "non-utf8/binary"
                if not label and not PROMPT_RE.match(rp):        # G4 content secret scan
                    for name, rx in SECRET:
                        if re.search(rx, b):
                            label, msg = "SKIPPED_NEVER_PUSH", "secret-pattern:" + name
                            break
                if not label and r["ext"] == ".csv" and len(b) > CLASS_M:
                    label, msg = "SKIPPED_NEVER_PUSH", "csv-over-25KB"
                if not label and rp in quarantine:               # G5 open BAD_ON_MAIN (prompt 1 step 5)
                    label, msg = "BAD_ON_MAIN_OPEN", "quarantined"
                if not label and rp in prev:                     # G6 drift: main moved to a blob the box never had
                    p = prev[rp]
                    if r["main_blob"] is not None and r["main_blob"] != p.get("main_blob") \
                            and r["main_blob"] not in (p.get("blob"), r["blob"]):
                        label, msg = "BAD_ON_MAIN_NEW", "main-changed-to-unknown-blob prev_main=%s" % (p.get("main_blob") or "-")
                if not label and r["mtime"] >= t0 - LIVE_WINDOW:  # G7 live
                    label, msg = "DEFERRED_LIVE", "mtime-within-15min"
                if not label:
                    label, msg = "READY_FOR_BYTE_EXACT_PR", "class=%s ext=%s state=%s" % (r["size_class"], r["ext"], r["state"])
            r["label"], r["message"] = label, msg
            rows.append(r)
    box = {r["path"] for r in rows}
    missing = sorted(p for p in tree if p.startswith("lab/") and in_scope(p[4:]) and not never_push(p) and p not in box)
    np_main_unclassified = sorted(p for p in tree if p.startswith("lab/") and never_push(p) and p not in box)
    register_never_push = {p: never_push(p) for p in sorted(quarantine) if never_push(p)}
    rows.sort(key=lambda r: r["path"])
    labels = ("IN_SYNC", "SKIPPED_NEVER_PUSH", "SKIPPED_NEVER_PUSH_ON_MAIN", "BAD_ON_MAIN_OPEN",
              "BAD_ON_MAIN_NEW", "DEFERRED_LIVE", "READY_FOR_BYTE_EXACT_PR")
    c = {k: sum(1 for r in rows if r["label"] == k) for k in labels}
    assert sum(c.values()) == len(rows)
    ready = [r for r in rows if r["label"] == "READY_FOR_BYTE_EXACT_PR"]
    t0_et = datetime.datetime.fromtimestamp(t0, ET)
    mrows = [{k: r[k] for k in ("path", "size", "sha256", "blob", "main_blob", "state", "label", "size_class", "ext")}
             for r in rows if r["label"] in MANIFEST_LABELS]
    mname = "GV2_LANDING_MANIFEST_%s.json" % t0_et.strftime("%Y%m%dT%H%M%S%z")
    manifest = {"manifest": "gv2-landing-manifest/1", "classifier": "v3.2r6",
                "classifier_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
                "t0_epoch": t0, "t0_et": t0_et.isoformat(), "main_head": head,
                "repo": "17thgreen/GrokBot---The-GauntletV2-", "branch": "main",
                "rows_total": len(mrows), "rows": mrows}
    mbytes = (json.dumps(manifest, indent=1, sort_keys=True) + "\n").encode("utf-8")
    mpath = os.path.join(mdir, mname)
    open(mpath, "wb").write(mbytes)
    summary = {"classifier": "v3.2r6", "t0_epoch": t0, "main_head": head, "in_scope_total": len(rows),
               "in_sync": c["IN_SYNC"], "skipped_never_push": c["SKIPPED_NEVER_PUSH"],
               "skipped_never_push_on_main": c["SKIPPED_NEVER_PUSH_ON_MAIN"],
               "bad_on_main_open": c["BAD_ON_MAIN_OPEN"], "bad_on_main_new": c["BAD_ON_MAIN_NEW"],
               "deferred_live": c["DEFERRED_LIVE"], "ready_for_pr": c["READY_FOR_BYTE_EXACT_PR"],
               "ready_md": sum(1 for r in ready if r["ext"] == ".md"),
               "ready_s": sum(1 for r in ready if r["size_class"] == "S"),
               "ready_m": sum(1 for r in ready if r["size_class"] == "M"),
               "ready_l": sum(1 for r in ready if r["size_class"] == "L"),
               "ready_xl": sum(1 for r in ready if r["size_class"] == "XL"),
               "missing_on_box": len(missing), "main_lab_files": sum(1 for p in tree if p.startswith("lab/")),
               "manifest_path": mpath, "manifest_sha256": hashlib.sha256(mbytes).hexdigest(),
               "manifest_rows": len(mrows)}
    json.dump({"summary": summary, "missing_on_box": missing, "never_push_on_main_unclassified": np_main_unclassified,
               "register_never_push": register_never_push, "files": rows}, open(out, "w", encoding="utf-8"), indent=1)
    print(json.dumps(summary))

main()
# <<< CLASSIFIER v3.2 END
```

### 4a. [v3] Present on GauntletV2 but missing on the box = NO-OP

- An in-scope repo path with no box file is **never** a change: never delete it, never "restore" it, never count it as pending.
- Log one aggregate line `MISSING_ON_BOX count=<N>` (**[v3.2]** N = classifier `missing_on_box`) and add `missing_on_box=<N>` to `RUN_END`. List up to 25 paths in the log for diagnosis. Over 25 triggers G5 → ABORTED_BOX_INCOMPLETE.
- The routine has **no delete capability at all**, by design.

## 5. Scope: what is eligible to sync

Box `/workspace/lab/<X>` ↔ repo `lab/<X>`.

**[v3.2]** This table is implemented exactly by the classifier's `in_scope()` (§4.1). Out-of-scope files are not walked, logged or counted (no more `SKIPPED_NEVER_PUSH astra-science` lines for out-of-scope trees).

| box subtree | rule |
|---|---|
| `lab/governance/**` | eligible. Exception: in `lab/governance/astra/packets/`, only top-level `*.md` files and `packets/extracts/**` are eligible (the selective packets rule). |
| `lab/archive/**` | eligible |
| `lab/execution/**` | eligible |
| `lab/harness/**` | text sources/specs only: `*.py *.md *.json *.yaml *.yml *.toml *.txt *.cfg *.ini *.sh`. Skip `results/`, `out/`, `runs/`, `data/`, `.venv*/`, `__pycache__/`. |
| `lab/data/**` | metadata only: `*.md`, and `*.json` directly under `provenance/`. Never `raw/`, `slices/`, `sealed/`, parquet, zip, ndjson, csv or tick files. MCP bypasses `.gitignore`, so **you** enforce this. **[v3.2 OPTIONAL clarification]** In scope means every `*.md` outside `raw/`/`slices/`/`sealed/` (including `DATA-PROV-TRADES-001/provenance/*.md` and other dataset notes) and every `*.json` whose parent directory is `provenance/` (including every `CLOCK_AUDIT_*.json`), minus the §6 gate 1 never-push paths. |
| everything else | **out of scope; never push.** This covers `astra-science/`, `astra-capture/`, `astra-data/`, `astra-kits/`, `astra-src/`, `catalyst/`, `evidence_private/`, `evidence_cold/`, `incidents/`, `tmp/`, `.venv*`, and loose top-level files. |

Also out of scope:
- `steward/GAUNTLET_SYNC_*.log`: box-only, because they name refused paths
- non-UTF-8 or binary files: log `SKIPPED_NEVER_PUSH non-utf8/binary`

**[v3]** Steward routine prompt files `lab/governance/astra/steward/GAUNTLET_SYNC_ROUTINE_PROMPT_*.md` follow this normal scope like any governance file. They are eligible unless a path rule in §6 gate 1 matches. See §6 gate 2 for the scan exemption.

## 6. Gates, in this fixed order [v3.2; rev5: no write gates; implemented by the §4.1 classifier]

Each in-scope file gets exactly one label: the first gate that fires.

| step | gate | result | in manifest |
|---|---|---|---|
| G1 | never-push path (gate 1 below) | `SKIPPED_NEVER_PUSH <rule>`, or **`SKIPPED_NEVER_PUSH_ON_MAIN <rule>`** if the path is already present on main | no |
| G2 | **compare with main**: same blob at the same repo path | `IN_SYNC` (counted only) | no |
| G3 | **binary / non-UTF-8** (NUL byte or UTF-8 decode failure) | `SKIPPED_NEVER_PUSH non-utf8/binary` | no |
| G4 | content secret scan (gate 2 below); then `*.csv` over 25 KB | `SKIPPED_NEVER_PUSH secret-pattern:<name>` / `csv-over-25KB` | no |
| G5 | open BAD_ON_MAIN register path (§1 step 5) | `BAD_ON_MAIN_OPEN quarantined` | yes (repair) |
| G6 | **[rev5] drift:** main's blob changed since `<prev>` to a blob that is neither `<prev>`'s box blob nor the current box blob | `BAD_ON_MAIN_NEW main-changed-to-unknown-blob prev_main=<sha or ->` | yes (repair) |
| G7 | live: mtime ≥ `t0` − 15 min | `DEFERRED_LIVE mtime-within-15min` | no (next run) |
| — | none fired | **`READY_FOR_BYTE_EXACT_PR class=<S\|M\|L\|XL> ext=<ext> state=<NEW\|MODIFIED>`** | yes |

Why this order:
- G1 runs first because it is a path-only rule that must hold whatever the bytes are.
  - A never-push path that is already on main is `SKIPPED_NEVER_PUSH_ON_MAIN`. It is not compared, not BAD_ON_MAIN and not an alert. It is listed in the log (§4.1 step 5) and counted in `RUN_END`.
  - Removing it from main is a separate Conductor decision; this routine never deletes.
- G2 comes before every content gate, so a file already byte-identical on main is never counted as anything but `IN_SYNC`.
- **[rev5]** G3 and G4 come before G5 and G6, so no manifest row (ready or repair) is ever binary or a secret-pattern hit.
- **[rev5]** G5 before G6: a path already on the register stays `BAD_ON_MAIN_OPEN` and is not re-detected as new.
- **[rev5]** G6 replaces the post-write blob compare. Main changing to a blob the box never had (according to the previous snapshot and now) means something wrote wrong bytes to main: a failed PR landing, a retype, a placeholder or any other writer. It needs `<prev>`; on the first rev5 run it cannot fire. Main changing to the previous or current box blob is a correct landing (`IN_SYNC`, or `READY` again if the box has moved on since).
- G7 runs last so the other counts do not depend on box activity. Live files are left out of the manifest and picked up by a later run. The PR job re-hashes every manifest row against the box anyway (§7.3).

1. **Never-push path check.** If any rule matches, log `SKIPPED_NEVER_PUSH <rule>`.
   - anything under `lab/evidence_private/` (any depth), and any `_prev/` copy of evidence_private material
   - anything under `lab/governance/astra/packets/card01_hybrid_forecast/source_probe_electindex/`
   - **ElectIndex raw bytes:** any capture, response body, dump or log fetched from ElectIndex. Any path containing `electindex` (case-insensitive) that is not a governance `.md` note is refused. **[v3.2]** Hash-only governance `.md` notes are otherwise allowed, **except** the box-only notes listed below.
   - **[v3.2] Box-only, never push (Conductor rulings; listed explicitly):**
     - `lab/evidence_private/**` (above)
     - `lab/governance/astra/packets/card01_hybrid_forecast/source_probe_electindex/**` (above)
     - `**/_prev/**`: every `_prev/` copy, of any material (Conductor ruling 2026-10-01)
     - `lab/governance/astra/packets/ARCHIVIST_SOURCE_GATE_ELECTINDEX_CARD01_2026-09-24.md`: the ElectIndex-named note
     - `**/ARCHIVIST_ELECTINDEX_*`: the six `packets/ARCHIVIST_ELECTINDEX_*_2026-09-24.md` notes and any later file with that prefix (Conductor ruling 2026-10-02 ~19:20 ET)
     - `lab/governance/astra/steward/LOSS_INVENTORY_2026-10-01.json`
     - **[rev5]** `**/GV2_LANDING_MANIFEST_*`: this routine's landing manifests (§7.2), wherever a copy lands
     - `lab/governance/astra/steward/LOSS_INVENTORY_2026-10-01*` (glob `steward/LOSS_INVENTORY_2026-10-01*`): every sibling, including `LOSS_INVENTORY_2026-10-01.md`, `LOSS_INVENTORY_2026-10-01_AMEND1.json` and `LOSS_INVENTORY_2026-10-01_AMEND1.md`, and any later file with that prefix (Conductor ruling 2026-10-03 ~04:57 ET)
   - **[v3.2] Live and state files** (rewritten by running processes; content is meaningless off the box and races the precheck):
     - `lab/data/**/provenance/*status.json`: covers `capture_status.json` (CB-002, LIQ-001, PM-006 rewrite theirs every 20–40 s; PM-008) and `pull_status.json` (PM-009)
     - **[rev6]** `**/*status.json`, case-insensitive (rule `live:status-json-any`): every other status file anywhere in scope, for example `lab/governance/pulses/GV2_SYNC_ROUTINE_STATUS.json`. Exception: a path listed in the classifier's `STATUS_JSON_PUSHABLE` (Conductor-ruled pushable). That list is empty as of 2026-10-03; adding a path needs a new prompt version.
     - `**/progress.json`
     - `**/*.pid`, `**/*.lock`, `**/.locks/**`: process and lock state
     - `**/*heartbeat*`
     - `**/*-wal`, `**/*-shm`, `**/*-journal`: SQLite side files
     - `**/*.tmp`, `**/*.partial`, `**/*.swp`: half-written files
   - **Secrets:**
     - API keys, Key IDs, PEM/private keys (`*.pem *.key *.p12 *.pfx`, `id_*`), `.env` / `.env.*`, anything from `/home/box/.secrets/`
     - RPC URLs with embedded keys (for example Alchemy)
     - `Gauntletkey.docx`, and all `*.docx`
   - **Raw market data:**
     - raw ticks (CF/BRTI/Kalshi/Polymarket tick or orderbook dumps)
     - `*.ndjson *.parquet *.zip *.gz *.sqlite* *.db`, and `*.csv` over 25 KB
     - `data/DATA-PROV-001/` OHLCV, `data/DATA-PROV-TRADES-001/` aggTrade zips, `**/DATA-PROV-*/raw|slices|sealed/` (**[v3.2 OPTIONAL clarification]** data files only; these datasets' `*.md` and `provenance/*.json` notes are in scope per §5)
     - any multi-MB data file
   - `.venv*/`, `__pycache__/`, `*.pyc`
   - anything from `/tmp`
   - anything under `lab/astra-science/`
2. **Content secret scan** (text files). Refuse with `SKIPPED_NEVER_PUSH secret-pattern:<name>` on any of:
   - `-----BEGIN` … `PRIVATE KEY`
   - `KALSHI-ACCESS-KEY` followed by a value
   - `api[_-]?key\s*[:=]\s*['"][A-Za-z0-9_\-]{16,}`
   - `sk-[A-Za-z0-9]{20,}`
   - `ghp_[A-Za-z0-9]{30,}` or `github_pat_`
   - `alchemy\.com/v2/[A-Za-z0-9_\-]{10,}`
   - `Bearer [A-Za-z0-9\-_.]{20,}`

   Never print the matched text.
   **[v3] Exemption:** files matching `lab/governance/astra/steward/GAUNTLET_SYNC_ROUTINE_PROMPT_*.md` skip **this content scan only**, because they quote the patterns themselves. v2 refused itself as `secret-pattern:private-key` on 2026-10-01. They are still subject to gate 1, the binary check (G3) and the §5 scope.
3. **[rev5] Size classes (tags, not gates).** There is no inline cap any more, so size never defers a file. Every `READY_FOR_BYTE_EXACT_PR` row carries `size_class`: **S** ≤ 12,288 B, **M** ≤ 25,600 B, **L** ≤ 1,048,576 B, **XL** above that. XL rows may be landed only with Conductor's explicit OK in the PR. `*.csv` over 25 KB stays `SKIPPED_NEVER_PUSH csv-over-25KB` (G4).
4. **[rev5] Markdown gate: retired.** No file takes an inline path, so `.md` needs no gate of its own. Changed `.md` files are `READY_FOR_BYTE_EXACT_PR` with `ext=.md` and are counted in `ready_md`.

When unsure, refuse.

## 7. [rev5] No writes: landing manifest and the byte-exact PR (replaces v3.1 §7)

### 7.1 This routine never writes to the repo
- Never call `push_files`, `create_or_update_file`, `delete_file`, `create_branch`, `create_pull_request`, `merge_pull_request` or any other GitHub write tool. Never `git commit` or `git push`. Never launch a cloud agent or any other job.
- The only GitHub access is reading main: the cache fetch and the read-only MCP tree fallback (§4 step 1).
- **Retired from v3.1 §7 and v3.2 rev4** (do not apply any of these): the inline-content rule and placeholder ban (old §7.1); the 12 KB inline cap and per-call caps (old §7.2); the pre-call self-check and the precheck `hash-drift` entry (old §7.3); post-push verification, the per-run BAD_ON_MAIN write-stop limit, `write_error` and `verify-timeout` (old §7.4); the 30-file cap, the 420 s write cutoff and `PENDING_NEXT_RUN` (old §7.5); `LANDED`, `ERROR`, `DEFERRED_OVERSIZE`, `DEFERRED_MD_BYTE_EXACT`, `PENDING`; the `non-md-drift` tag.

### 7.2 The landing manifest
- **Written by the classifier** (§4.1), never by hand: `/workspace/gauntlet_sync_work/GV2_LANDING_MANIFEST_<YYYYMMDDTHHMMSS±hhmm>.json`, where the timestamp is `t0` in America/New_York (example: `GV2_LANDING_MANIFEST_20261003T124000-0400.json`).
- **Box-only and never pushed:** it lives outside `/workspace/lab` (so it is out of §5 scope), and `**/GV2_LANDING_MANIFEST_*` is a §6 gate 1 never-push rule in case a copy is ever placed under `lab/`.
- **Content:** UTF-8 JSON with sorted keys: `manifest` (`gv2-landing-manifest/1`), `classifier` (**[rev6]** `v3.2r6`), `classifier_sha256`, `t0_epoch`, `t0_et`, `main_head`, `repo`, `branch`, `rows_total`, and `rows`. Rows are sorted by path, one per file that needs to land: every `READY_FOR_BYTE_EXACT_PR`, `BAD_ON_MAIN_OPEN` and `BAD_ON_MAIN_NEW` row, with `path size sha256 blob main_blob state label size_class ext`. `blob` is the box git blob sha the landed file must have; `main_blob` is what main had at `t0` (`null` if absent).
- It holds no mtimes, so for the same `t0`, box and main its bytes are identical (deterministic).
- **Valid manifest:** only a manifest whose sha256 appears in a `SUCCESS_CLASSIFIED` `RUN_END` line (§8) may feed a PR. Older manifests are history; do not delete them.

### 7.3 The byte-exact PR (outside this routine; for Conductor)
This routine does **not** start, launch or wait for it. It is recorded here so the manifest's purpose is unambiguous:
1. Conductor picks one valid manifest and decides which rows go in (default: every `READY_FOR_BYTE_EXACT_PR` row except `XL`; `BAD_ON_MAIN_*` repair rows only by explicit GO).
2. A bundle is built from the box bytes. Each row is re-hashed first; a row whose box sha256/blob no longer matches the manifest is dropped from this PR and left for a later manifest.
3. A cloud agent on a real checkout of GauntletV2 receives the bundle as base64 or a tarball with SHA256SUMS. Before committing, it checks that `git hash-object` of every file equals the row's `blob`. It commits only manifest paths (no deletes, no other files) on one branch and opens **one** PR.
4. Conductor verifies the PR's blobs against the manifest and merges it (no force-push).
5. After the merge, Conductor checks main's blob for every landed row. Any mismatch is a failed landing. The next routine run also catches it as `BAD_ON_MAIN_NEW` (G6) and alerts.

### 7.4 Run bound
- Classification only: there is no write window. Aim to finish by `t0` + 300 s.
- Hard wall at `t0` + 600 s: if you get there, write `RUN_END` with what you have and add `timeout=1` to it. Never write a second `RUN_END`.
- **[v3.2 OPTIONAL] BAD_ON_MAIN diagnostic (read-only).** For each `BAD_ON_MAIN_NEW` path, you may fetch main's bytes for that path read-only and add `box_bytes=<N> main_bytes=<N> first_diff_line=<n>` to its log line. Never print file content.

## 8. Log format

Append as you go. Tab-separated, one line per file:

```
<ISO time ET>  <run_id>  <repo path>  <size>  <sha256>  <git blob sha>  <RESULT>  <message or ->  <commit sha or ->
```

RESULT is one of **[rev5]**:
- `SKIPPED_NEVER_PUSH`: message `<rule>` (§6 G1, G3, G4).
- `SKIPPED_NEVER_PUSH_ON_MAIN`: message `<rule>` (§6 G1). The path is already on main. Not BAD_ON_MAIN, not an alert; listed for the daily report.
- `DEFERRED_LIVE`: message `mtime-within-15min` (§6 G7). Not an error; it is reconsidered next run.
- `BAD_ON_MAIN`: message `expected=<box blob> got=<main blob or -> commit=<sha or ->`, plus `detected=drift prev_main=<sha or ->` for a classifier `BAD_ON_MAIN_NEW` row (§1 step 5).
- `REPAIRED`: a register (or §12 seed) path that the start-of-run read-only check finds equal to the box (§1 step 5).
- `RETIRED`: message `never_push:<rule>`. A register path that is now a never-push path (§1 step 5), logged once.

Aggregate lines (not per file):
- `MISSING_ON_BOX count=<N>` **[v3]**
- **[rev5]** `LANDING_MANIFEST path=<manifest_path> sha256=<manifest_sha256> rows=<manifest_rows>`

Also write these two lines, tab-separated, in exactly this form **[v3.2; rev5 fields]**:
- `<ISO time ET>  <run_id>  RUN_START  epoch=<s>  t0_iso=<ISO time ET>  t0_epoch=<s>  main_head=<sha>  prompt_sha256=<sha>  classifier_sha256=<sha>`
- `<ISO time ET>  <run_id>  RUN_END  epoch=<s>  outcome=<…>  in_scope_total=<N>  in_sync=<N>  ready_for_pr=<N>  ready_md=<N>  ready_s=<N>  ready_m=<N>  ready_l=<N>  ready_xl=<N>  deferred_live=<N>  skipped_never_push=<N>  skipped_never_push_on_main=<N>  missing_on_box=<N>  bad_on_main=<N>  bad_on_main_new=<N>  repaired=<N>  retired=<N>  manifest_rows=<N>  manifest_sha256=<sha>  main_head=<sha>  elapsed_s=<N>`

`<ISO time ET>` is `TZ=America/New_York date +%Y-%m-%dT%H:%M:%S%:z` at the moment the line is written. `epoch` is integer seconds. `elapsed_s` = `epoch` − `t0_epoch`.

**[rev5] Counting rule** (every field is a copy or a fixed sum; none is estimated):
- `in_scope_total`, `in_sync`, `ready_for_pr`, `ready_md`, `ready_s`, `ready_m`, `ready_l`, `ready_xl`, `deferred_live`, `skipped_never_push`, `skipped_never_push_on_main`, `missing_on_box`, `bad_on_main_new`, `manifest_rows`, `manifest_sha256` and `main_head` are copied unchanged from the classifier summary.
- `in_scope_total` = `in_sync` + `ready_for_pr` + `deferred_live` + `skipped_never_push` + `skipped_never_push_on_main` + classifier `bad_on_main_open` + `bad_on_main_new`.
- `ready_for_pr` = `ready_s` + `ready_m` + `ready_l` + `ready_xl`. `ready_md` is the `.md` subset of `ready_for_pr`.
- `manifest_rows` = `ready_for_pr` + classifier `bad_on_main_open` + `bad_on_main_new`.
- `repaired` and `retired` = the `REPAIRED` and `RETIRED` lines written this run (§1 step 5).
- `bad_on_main` = every path open after this run = classifier `bad_on_main_open` + `bad_on_main_new`. Retired and repaired paths are not included.
- No counter depends on time spent, on batching or on write outcomes, so two runs with the same `t0`, box and main give the same `RUN_END` apart from `epoch` and `elapsed_s`.

On ABORTED_BOX_INCOMPLETE or a prompt-gate stop, write **no** log (§1, §3).

## 9. Outcome rule [rev5]

- **`SUCCESS_CLASSIFIED`**: the classifier ran with the pinned sha, and the log lines, the manifest and `RUN_END` were written. This is the normal outcome whether `ready_for_pr` is 0 or 500. No write ever happens, so there is no SUCCESS / SUCCESS_PARTIAL / FAILED.
- Alerts (§10) are independent of the outcome: a `SUCCESS_CLASSIFIED` run with an open BAD_ON_MAIN still alerts.
- Pre-run stops are outcomes too: `ABORTED_BOX_INCOMPLETE` (§3), and `PROMPT_MISSING` / `PROMPT_SHA_MISMATCH` / `NO_PIN` (§1; Logan is pinged).
- `CLASSIFIER_MISMATCH` (§4.1): `RUN_START` and `RUN_END` only, no manifest is valid, alert Conductor.
- `NAMESPACE_UNAVAILABLE`, `SUCCESS`, `SUCCESS_PARTIAL` and `FAILED` are retired.
- Always finish cleanly. On an unexpected exception after `RUN_START`, write `RUN_END` with `outcome=CLASSIFIER_MISMATCH` and `error=<short reason>`, and alert.

## 10. Reporting [v3: Conductor overrides; rev5 triggers]

- **Quiet on normal runs**, including `SUCCESS_CLASSIFIED` with any number of ready files. `READY_FOR_BYTE_EXACT_PR`, `SKIPPED_NEVER_PUSH_ON_MAIN`, `RETIRED` and size classes are **not** alert triggers.
- **Alert Conductor only on:**
  - **any `BAD_ON_MAIN`**, new this run (`BAD_ON_MAIN_NEW`) or still open from a prior run. This is always non-quiet. The alert lists **every** open path with its expected and got shas, and repeats every run until each path is logged `REPAIRED`.
  - `ABORTED_BOX_INCOMPLETE`
  - `CLASSIFIER_MISMATCH` (including `timeout=1` or `error=…`)
  - any path logged `DEFERRED_LIVE` in **3 consecutive runs** (this run and the two previous `RUN_START`s in the `GAUNTLET_SYNC_*.log` files). List each such path once per day with its last message. It probably needs a never-push rule in the next prompt version.
  - **backlog = 0** (`manifest_rows == 0`, meaning main is caught up with the box); report once per day at most.
  - `ready_xl > 0`, once per day at most (an XL file needs Conductor's explicit OK).

  Alert format, at most 6 lines: `GauntletV2 sync <date> <outcome>: <one-line reason>`, then the RUN_END line (or the failing guard checks), then the log path and, if any, the manifest path.
- **Steward non-priority note:** on the same triggers, send the Steward one non-priority line containing the RUN_END line (or the guard result).
- **Prompt missing, mismatched or unpinned:** ping **Logan** (§1). No Conductor or Steward note is needed beyond that.

## 11. Repo conduct

- **[rev5] No repo writes of any kind:** no commit, push, force-push, history rewrite, branch, tag, PR, merge, comment or delete. Leave GauntletV2 draft PR #1 alone.
- Never touch `17thgreen/GPT-6-Astra-Deathmatch` or any other repo.
- Never launch a cloud agent or other job; the byte-exact PR is Conductor's (§7.3).
- On the box, touch only your log, `/workspace/gauntlet_sync_cache.git` and `/workspace/gauntlet_sync_work/` (including `classify_v3_2.py`, `classified_<run_id>.json`, `quarantine.txt` and **[rev5]** `GV2_LANDING_MANIFEST_*.json`). Never delete earlier manifests or classified files. Never modify `/workspace/lab` content, `/workspace/recovery`, recorders or processes.

## 12. Context (informational)

- GauntletV2 main = `a196580b6de5d35229ce9dc055786093b2f763e3` ("lab sync 2026-10-01: oversize batch (46 files)", 21:00:07 ET), about 567 files under `lab/`.
- v2 run `sync-20261001-2046`: SUCCESS_PARTIAL, 9 landed, 650 pending.
- The 46 oversize files were landed by a real-checkout cloud agent from sha256-pinned box bytes.
- Box rebuild at about 22:24 ET. The 22:42 run stopped (PROMPT_MISSING) and was paused by Conductor. The box store then re-hydrated `/workspace` from 22:24 to about 23:13 ET: 74,954 files, 95.4 GB, `outcome=hydrated`, `failures=0`. That re-hydration window is exactly what guard G3 exists for.
- **[v3.1] 2026-10-02:**
  - `sync-20261002-0044`: SUCCESS_PARTIAL, 30 landed, head a9cd1e76, 839 s.
  - `sync-20261002-0248`: 24 verified, 6 left wrong on main, head d989151d, 1,678 s.
  - **The 6 paths were repaired externally** by commit `72875aafeabec5798828209cf58763af630f6a4d` ("lab sync 2026-10-02: repair placeholder-corrupted files (6 files)", 03:25 ET), from the box files, not from a196580. Each now matches its box blob (Steward verified at 03:26 ET).
  - **Seed list for §1 step 5.** These 6 paths are on the start-of-run read-only re-check list **once**: the first v3.1 run should log each `REPAIRED`, after which they leave the register. If any of them is ever found different, log it `BAD_ON_MAIN` and quarantine it as usual.
    - `lab/harness/examiner/src/f1_incremental.py` (box blob 9124092b)
    - `lab/harness/examiner/src/run_edge_20260911_005.py` (310e3ee5)
    - `lab/harness/examiner/src/run_pm002_market_baseline.py` (596bb9c2)
    - `lab/harness/examiner/src/w2c_incremental.py` (1427d6c2)
    - `lab/harness/examiner/src/w2d_ivrv_incremental.py` (ec917fc3)
    - `lab/harness/examiner/src/w2e_incremental.py` (8031f10f)
  - All 6 are over 12 KB. **Every file over the 12 KB inline cap is deferred (`DEFERRED_OVERSIZE inline-cap-12KB`) to a real-checkout job that Conductor arranges, and is never pushed inline by this routine.** **[rev5: superseded by §7;** no file is pushed inline.**]**
- **[v3.2 OPTIONAL, informational] 2026-10-02, later:**
  - The 6 seed paths were logged `REPAIRED` by `sync-20261002-0442` (04:44 ET) and have left the register.
  - v3.1 runs 0442–1840: all SUCCESS_PARTIAL; landed 30/30/18/8/12/7/1/6. No write was sent after `t0` + 420 s in any run.
  - Run 1840 BAD_ON_MAIN `CLOCK_AUDIT_W2A_CF_T14_JOIN.md` (§0) was repaired externally by `a6af2420` (18:51 ET). The next run's §1 step 5 check should log it `REPAIRED`.
- **[rev5, informational] 2026-10-03:**
  - `sync-20261003-0445`: BAD_ON_MAIN L3 `.md` (repaired `06d04867`) and CB-002 `capture_status.json` (STALE_LIVE_ACCEPTED; RETIRED under v3.2).
  - `sync-20261003-1050`: `outcome=FAILED landed=0 bad_on_main=3`, main `76883e2c`. The new BAD_ON_MAIN paths were PM-003 `CLOCK_AUDIT_REPORT.md` (placeholder) and `CLOCK_AUDIT_W2C_SIBLING_JOIN.json` (static `.json` retype). Conductor paused v3.1 at 10:58 ET and arranged an external byte-exact repair of both.
  - The rev5 classifier, run against a 04:58 ET snapshot as `<prev>` and main `76883e2c` with an empty register, labels exactly those two PM-003 paths `BAD_ON_MAIN_NEW` and nothing else.
- **[rev6, informational] 2026-10-03:**
  - The first rev5 run, `sync-20261003-1444`, was `SUCCESS_CLASSIFIED` with `manifest_rows=522`. Combined byte-exact PR #2 landed 521 of those rows and was squash-merged as `c19b9232`. `GV2_SYNC_ROUTINE_STATUS.json` was held out by hand, which is the case rev6 now covers.
  - CB-002 `capture_status.json` and PM-009 `pull_status.json` are still on main at `c19b9232` (`SKIPPED_NEVER_PUSH_ON_MAIN`). Their removal is a separate Conductor-GO'd deletion PR.
