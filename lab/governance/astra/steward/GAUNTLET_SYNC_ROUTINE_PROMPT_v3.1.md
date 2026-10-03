# GauntletV2 repo sync, routine prompt (v3.1)

Author: The Steward. v3 written 2026-10-01 22:55 ET; v3.1 written 2026-10-02 ~03:20 ET after the second placeholder-corruption incident (run `sync-20261002-0248`), revised ~03:30 ET per Conductor (no in-run retries, absolute write cutoff, live-schema-only encoding exception) before pinning. Conductor installs and pins this prompt. The Steward does not edit the routine.
v3 replaces v2 in full. v2 (sha256 `bb0a90e567c44be76928759b3d6aa20b8effd1beff9a8663f4a8c1e688ed7a66`) was reconstructed from the Steward's own record while the box was re-hydrating. The box copy then came back byte-identical (sha256 verified 23:21 ET), so the base is confirmed. v3 = v2 + changes (a)–(e) from Conductor's 2026-10-01 incident ruling, marked **[v3]**.
v3.1 = v3 (sha256 `cc0a17895d32a2e3ca97bce915849a4405c402dcdd0f514c3d97665f53484ed2`) + changes marked **[v3.1]**: the inline-content rule, the pre-call self-check, BAD_ON_MAIN (with cross-run quarantine), a 12 KB inline cap, an absolute write cutoff, and **no in-run repair or retry of any kind**.
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

If you ever feel tempted to "just push everything", or to "mirror the box state including deletions", or to "just re-push it a different way", that is the failure mode. Don't.

## 1. Run gate: prompt pin, cadence, namespace

1. **[v3] Prompt pin.**
   - Compute sha256 of this file, `/workspace/lab/governance/astra/steward/GAUNTLET_SYNC_ROUTINE_PROMPT_v3.1.md`.
   - Compare it to Conductor's pin, `PROMPT_SHA256=<hex>`. The pin is supplied in the routine launcher, outside this file; a file cannot hold its own hash.
   - **If the file is missing, or its sha differs from the pin, or no pin was supplied:** do nothing else. Write no log, call no GitHub tool, and **ping Logan**: `GauntletV2 sync: prompt <MISSING|SHA_MISMATCH|NO_PIN> (got <sha or ->, want <pin>) — routine stopped`. Then end.
2. **[v3] Cadence** (Conductor override, kept from v2): every 2 hours at minute :40, America/New_York. One run at a time. If a previous run's `RUN_START` has no matching `RUN_END` and is under 15 minutes old, end silently.
3. **Namespace.**
   - Discover the live GitHub MCP namespace with tool discovery (GetMcpTools / GetDynamicTools, pattern `push_files`). As of 2026-10-01 it is **`user-GitHub-xai`**, never `user-Github`. If discovery shows a different exact name, use it and log it.
   - If no GitHub namespace with `push_files` is `ready`, the outcome is `NAMESPACE_UNAVAILABLE` (an alert trigger, §10).
   - Look up the input schemas of `push_files` (and `create_or_update_file`, if used) **every run** before the first write.

4. **[v3.1] Clock.** Record `t0` (monotonic, plus ISO time ET) **before** step 1. Every time limit in this prompt is measured from `t0`, so it includes discovery, the diff, staging and verification (§7.5).
5. **[v3.1] BAD_ON_MAIN re-check (start of run, read-only).**
   - Build the BAD_ON_MAIN register: every path with a `BAD_ON_MAIN` line in **any** `GAUNTLET_SYNC_*.log` that has no later `REPAIRED` line, **plus** the §12 seed list (until each seed path has a `REPAIRED` line). There is no age limit; a path stays quarantined until it is logged `REPAIRED`.
   - Compare each path's current GauntletV2 main blob (from the §4 tree) with `git hash-object` of the box file.
     - Equal → log `REPAIRED` (with the remote blob).
     - Different → log `BAD_ON_MAIN` again with both shas.
   - **Exclude** still-bad paths from this run's pending list. The routine **never writes** a BAD_ON_MAIN path, in any form, in this run or any later run, until this read-only check logs it `REPAIRED`. Repair is always external (a cloud-agent or real-checkout job that Conductor launches). This check only reads.
   - Every open BAD_ON_MAIN path is included in this run's alert (§10).

## 2. Fixed facts

- **Source:** `/workspace/lab` on the box. The box is the source of truth for **content**. It is **not** the source of truth for **existence** (see §4a).
- **Target:** `17thgreen/GrokBot---The-GauntletV2-`, branch **`main`**. Commit directly to main via MCP `push_files`. That is the established convention.
- **Log:** `/workspace/lab/governance/astra/steward/GAUNTLET_SYNC_<YYYY-MM-DD>.log` (America/New_York date). Append only; create it if missing. This applies only after the pre-flight in §3 passes.
- **Forbidden inputs:**
  - never read a file list from `/tmp`
  - never use `/workspace/gauntlet_sync_20260922/manifest.json` or any saved manifest as the to-do list
  - never resume from memory

  The diff (§4) is the only to-do list.

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
| G4 | in-scope box file count (per §5) < **75 %** of the number of files under `lab/` on GauntletV2 main |
| G5 | more than **25** MISSING_ON_BOX paths (§4a) in one run. A real edit seldom removes more than a few files; a wipe removes hundreds. |

G4 and G5 need the remote tree (§4 step 1). Reading the tree is allowed before the guard decision, because it is a read; writing is not.

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
   - Fallback: MCP `get_repository_tree` for `main`, recursive (schema looked up first).
2. **Walk eligible box files** (§5). Skip symlinks. Prune `.venv*`, `__pycache__`, `.git` and `node_modules`.
3. For each file, compute its **git blob sha** = `sha1("blob " + <byte length> + "\0" + <bytes>)`, and its sha256 for the log.
4. **Classify each file:**
   - same blob at the same repo path → in sync (counted only)
   - path absent in repo → NEW
   - different blob → MODIFIED
5. **Order the pending files:** MODIFIED first, then NEW, each sorted by path.
6. Scratch files go only under `/workspace/gauntlet_sync_work/`, never `/tmp`. Create that directory if it is missing.

### 4a. [v3] Present on GauntletV2 but missing on the box = NO-OP

- An in-scope repo path with no box file is **never** a change: never delete it, never "restore" it, never count it as pending.
- Log one aggregate line `MISSING_ON_BOX count=<N>` and add `missing_on_box=<N>` to `RUN_END`. List up to 25 paths in the log for diagnosis. Over 25 triggers G5 → ABORTED_BOX_INCOMPLETE.
- The routine has **no delete capability at all**, by design.

## 5. Scope: what is eligible to sync

Box `/workspace/lab/<X>` ↔ repo `lab/<X>`.

| box subtree | rule |
|---|---|
| `lab/governance/**` | eligible. Exception: in `lab/governance/astra/packets/`, only top-level `*.md` files and `packets/extracts/**` are eligible (the selective packets rule). |
| `lab/archive/**` | eligible |
| `lab/execution/**` | eligible |
| `lab/harness/**` | text sources/specs only: `*.py *.md *.json *.yaml *.yml *.toml *.txt *.cfg *.ini *.sh`. Skip `results/`, `out/`, `runs/`, `data/`, `.venv*/`, `__pycache__/`. |
| `lab/data/**` | metadata only: `*.md`, and `*.json` directly under `provenance/`. Never `raw/`, `slices/`, `sealed/`, parquet, zip, ndjson, csv or tick files. MCP bypasses `.gitignore`, so **you** enforce this. |
| everything else | **out of scope; never push.** This covers `astra-science/`, `astra-capture/`, `astra-data/`, `astra-kits/`, `astra-src/`, `catalyst/`, `evidence_private/`, `evidence_cold/`, `incidents/`, `tmp/`, `.venv*`, and loose top-level files. |

Also out of scope:
- `steward/GAUNTLET_SYNC_*.log`: box-only, because they name refused paths
- non-UTF-8 or binary files: log `SKIPPED_NEVER_PUSH non-utf8/binary`

**[v3]** Steward routine prompt files `lab/governance/astra/steward/GAUNTLET_SYNC_ROUTINE_PROMPT_*.md` follow this normal scope like any governance file. They are eligible unless a path rule in §6 gate 1 matches. See §6 gate 2 for the scan exemption.

## 6. Gates before every write, in this order

1. **Never-push path check.** If any rule matches, log `SKIPPED_NEVER_PUSH <rule>`.
   - anything under `lab/evidence_private/` (any depth), and any `_prev/` copy of evidence_private material
   - anything under `lab/governance/astra/packets/card01_hybrid_forecast/source_probe_electindex/`
   - **ElectIndex raw bytes:** any capture, response body, dump or log fetched from ElectIndex. Any path containing `electindex` (case-insensitive) that is not a governance `.md` note is refused. Hash-only references in governance notes are allowed (ARCHIVIST_SOURCE_GATE_ELECTINDEX_CARD01_2026-09-24, APPROVED_HASH_ONLY).
   - **Secrets:**
     - API keys, Key IDs, PEM/private keys (`*.pem *.key *.p12 *.pfx`, `id_*`), `.env` / `.env.*`, anything from `/home/box/.secrets/`
     - RPC URLs with embedded keys (for example Alchemy)
     - `Gauntletkey.docx`, and all `*.docx`
   - **Raw market data:**
     - raw ticks (CF/BRTI/Kalshi/Polymarket tick or orderbook dumps)
     - `*.ndjson *.parquet *.zip *.gz *.sqlite* *.db`, and `*.csv` over 25 KB
     - `data/DATA-PROV-001/` OHLCV, `data/DATA-PROV-TRADES-001/` aggTrade zips, `**/DATA-PROV-*/raw|slices|sealed/`
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
   **[v3] Exemption:** files matching `lab/governance/astra/steward/GAUNTLET_SYNC_ROUTINE_PROMPT_*.md` skip **this content scan only**, because they quote the patterns themselves. v2 refused itself as `secret-pattern:private-key` on 2026-10-01. They are still subject to gate 1 and gate 3, and to the §5 scope.
3. **Size gate:** over **25 KB** (25,600 B) → `DEFERRED_OVERSIZE`. Not a failure; Conductor arranges real-checkout landings separately.

When unsure, refuse.

## 7. Batching, inline content, verification and the run bound [v3.1: rewritten]

### 7.1 Inline content only [v3.1]

- **Every `content` value in a write call (`push_files`, `create_or_update_file`) is the literal UTF-8 text of the box file**, written out in full inside the tool call.
- **Forbidden in any write-call argument:**
  - `$file:` or any other placeholder or reference syntax (`@file`, `file://`, `{{…}}`, `${…}`, `<<…>>`)
  - a box path, a URL, a gist or blob link
  - "see attached" / "content of X" / "same as before"
  - base64 or any other encoding. **The only exception:** the tool's **live input schema, looked up this run** (§1 step 3), explicitly states that the tool decodes that exact encoding (for example, a documented `encoding` field that the server decodes). Memory, examples, other tools or past runs are not a contract. When the Steward checked on 2026-10-02 (03:27 ET), the live descriptions of `push_files` and `create_or_update_file` in `user-GitHub-xai` stated no decode contract, so encoded text lands as encoded text and encoding is **forbidden**. If an explicit contract does exist, log the schema text you relied on, and the §7.3 hash check applies to the **decoded** bytes.
  - truncation markers (`…`, `[snip]`)
  - JSON files you prepared on disk and "refer" to

  No layer between you and GitHub expands anything. What you type in the call is exactly what lands.
- Staging files under `/workspace/gauntlet_sync_work/` are allowed only as **your own scratch** for building and checking the payload. They never appear in a call.

### 7.2 Size caps [v3.1: lowered]

- **Inline cap per file: 12 KB** (12,288 B). A file over 12 KB is logged `DEFERRED_OVERSIZE` with message `inline-cap-12KB` and is never pushed by this routine. It joins the real-checkout landing queue that Conductor arranges (as for the 46-file oversize batch on 2026-10-01).
  - Reason: in run 0248 the `$file:` shortcut began at the first file over 12 KB (12.9 KB, batch 3) and then persisted for every later batch. The cap keeps each call short enough to emit verbatim. The §7.3 self-check and the §7.1 ban cover smaller files.
- **Per call:** at most **12 KB** summed content and at most **6 files**. One commit per call. Message: `lab sync <YYYY-MM-DD>: batch <k> (<n> files)`.
- The §6 gate 3 limit (25 KB) stays as the never-push size gate. The 12 KB cap is an additional routine-only limit.

### 7.3 Pre-call self-check (abort the call if it fails) [v3.1]

Before **each** write call:

1. **Build the call arguments** as a JSON file in scratch, using a script that reads the box bytes: `json.dumps({"owner":…, "files":[{"path":…, "content": <bytes.decode("utf-8")>}…]})`.
2. **Check that JSON file with a script**, for every file entry:
   - `content` contains no `$file:`, `file://`, `{{` / `${` placeholder, and is not a path or URL
   - `content` is not base64 (or another encoding) of the file, unless the §7.1 live-schema exception applies
   - `git hash-object --stdin` of `content.encode("utf-8")` **equals** the box blob sha (`git hash-object <box file>`)
   - the byte length equals the box size
3. **The call you send must carry exactly those arguments, character for character.** Do not retype, re-wrap, re-escape, summarize or "clean up" the content. If you cannot reproduce it exactly (for example, it is too long to emit reliably), **do not send the call**. Log the files as `DEFERRED_OVERSIZE inline-not-reproducible`.
4. If any entry fails step 2: **abort that call** (send nothing), log those files as `ERROR precheck-<reason>`, and continue with the next batch. Nothing was written, so these paths simply stay pending for the next run.
5. **Immediately before sending, check the clock** (§7.5). If `now − t0 ≥ 420 s`, do not send.

### 7.4 Post-push verification and BAD_ON_MAIN [v3.1]

After **every** write call that was sent, whether it succeeded or returned an error (not only at the end of the run):

1. Re-read the remote blob sha of **each path in the call** on GauntletV2 main. Use `git fetch` into the cache (§4 step 1) then `git ls-tree main -- <paths>`, or MCP `get_file_contents` (the `sha` field).
2. Compare it with `git hash-object` of the box file.
   - Equal → `LANDED` (with the commit sha).
   - Different, **or the write call returned an error** → **`BAD_ON_MAIN`**. Log both shas: `expected=<box blob> got=<remote blob> commit=<sha or ->`, plus `write_error=<msg>` if there was one. It is **not** counted as landed.
3. **No in-run repair or retry, of any kind.** A BAD_ON_MAIN path is quarantined:
   - never written again in this run: no re-push, no single-file retry, no "test" commit
   - never written in any later run, until the start-of-run read-only check (§1 step 5) logs it `REPAIRED` because it was fixed **externally**
   - never "fixed" through `$file:`, base64, chunks, partial content or any other indirect form
   - always alerted (§10)

   Repair is a separate cloud-agent or real-checkout job that Conductor launches.
4. After 2 BAD_ON_MAIN results in one run (from mismatches or write errors), **stop writing**. Log the remaining files as PENDING_NEXT_RUN and go to §8/§10. Something systematic is wrong.

### 7.5 Run bound and hard time wall [v3.1: tightened]

- At most **30 files** attempted per run.
- **Absolute write cutoff: `t0` + 7 min (420 s).** No write call of any kind (`push_files`, `create_or_update_file`, or any other GitHub write tool, for a first push, a retry or anything else) is sent once `now − t0 ≥ 420 s`. Check the clock immediately before every write call. There is no exception and no "one last batch".
- Post-push verification and logging must finish by `t0` + 9 min.
- `RUN_END` is written by `t0` + **10 min** (600 s) at the latest. If verification is still incomplete at 9 min, log the unverified paths as `BAD_ON_MAIN` with message `verify-timeout expected=<box blob> got=- commit=<sha>`; they are re-checked next run as in §1 step 5.
- **Hard stop at 600 s:** if anything is still running, write `RUN_END` immediately and end. After `RUN_END`, no tool call of any kind.
- Do not build alternative payload variants (oneline, chunked, base64, "ascii") to work around a failure. One payload per batch.
- **Exactly one `RUN_END` per run.** No `RUN_END_AMENDED` lines and no second repair pass.
- Everything not attempted is logged `PENDING_NEXT_RUN`: per-file for the first 200, then one aggregate line.
- **On a write error** (the tool returns an error): **no retry.** Run the §7.4 read-back for every path in that call and log each as `BAD_ON_MAIN` with `write_error=<msg>` (§7.4). Those paths are quarantined. Then continue only if the §7.4 step 4 limit and the write cutoff allow it.

## 8. Log format

Append **after every batch**. Tab-separated, one line per file:

```
<ISO time ET>  <run_id>  <repo path>  <size>  <sha256>  <git blob sha>  <RESULT>  <message or ->  <commit sha or ->
```

RESULT is one of:
- `LANDED`
- `SKIPPED_NEVER_PUSH`
- `DEFERRED_OVERSIZE`
- `PENDING_NEXT_RUN`
- `ERROR`
- `BAD_ON_MAIN` **[v3.1]**: message `expected=<box blob> got=<remote blob or -> commit=<sha or ->`, plus `write_error=<msg>` or `verify-timeout` when applicable
- `REPAIRED` **[v3.1]**: a previously BAD_ON_MAIN (or §12 seed) path that the start-of-run read-only check finds fixed externally. Logged only by §1 step 5, never after a write by this routine.

Aggregate lines (not per file): `MISSING_ON_BOX count=<N>` **[v3]**.

Also write:
- `RUN_START <run_id> namespace=<name> main_head=<sha> prompt_sha256=<sha>` **[v3: prompt sha added]**
- `RUN_END <run_id> outcome=<…> eligible_pending=<N> landed=<N> deferred_oversize=<N> skipped_never_push=<N> pending_next_run=<N> errors=<N> in_sync=<N> missing_on_box=<N> bad_on_main=<N> repaired=<N> new_main_head=<sha> elapsed_s=<N>` **[v3: `remote_only` renamed `missing_on_box`; v3.1: `bad_on_main`, `repaired` added; `elapsed_s` measured from `t0`]**

On ABORTED_BOX_INCOMPLETE or a prompt-gate stop, write **no** log (§1, §3).

## 9. Outcome rule

- `eligible_pending` = pending files that passed every gate.
- `eligible_pending == 0` → **SUCCESS** (backlog = 0).
- `eligible_pending > 0` and `landed >= 1` → **SUCCESS**, or `SUCCESS_PARTIAL` if any ERROR, BAD_ON_MAIN or PENDING_NEXT_RUN remains. **[v3.1]** `landed` counts verified files only (§7.4).
- `eligible_pending > 0` and `landed == 0` → **FAILED**.
- **[v3]** Pre-run stops are outcomes too: `ABORTED_BOX_INCOMPLETE` (§3), `NAMESPACE_UNAVAILABLE` (§1), and `PROMPT_MISSING` / `PROMPT_SHA_MISMATCH` / `NO_PIN` (§1, Logan is pinged).
- Always finish cleanly. Catch exceptions, log `ERROR`, write `RUN_END` (except for the no-write stops).

## 10. Reporting [v3: Conductor overrides]

- **Quiet on normal runs.** That includes runs that land files, and SUCCESS_PARTIAL with no alert trigger. Deferred-oversize alone is **not** an alert.
- **Alert Conductor only on:**
  - `FAILED`
  - 3 or more errors in the run
  - `NAMESPACE_UNAVAILABLE`
  - **backlog = 0** (eligible_pending == 0, meaning the sync is caught up; report once per day at most)
  - `ABORTED_BOX_INCOMPLETE`
  - **[v3.1] any `BAD_ON_MAIN`**, new this run (mismatch, write error or verify-timeout) or still open from a prior run. This is always non-quiet. The alert lists **every** open BAD_ON_MAIN path with its expected and got shas, and repeats every run until each path is logged `REPAIRED`.

  Alert format, at most 6 lines: `GauntletV2 sync <date> <outcome>: <one-line reason>`, then the RUN_END line (or the failing guard checks), then the log path.
- **Steward non-priority note:** on the same triggers, send the Steward one non-priority line containing the RUN_END line (or the guard result).
- **Prompt missing, mismatched or unpinned:** ping **Logan** (§1). No Conductor or Steward note is needed beyond that.

## 11. Repo conduct

- No force-push, no history rewrite, no branch creation or deletion.
- No PR creation, merge, close or edit. Leave GauntletV2 draft PR #1 alone until sync is green and Conductor rules on it.
- **Never delete repo files** (see §4a). Never write outside `lab/` in the repo.
- Never touch `17thgreen/GPT-6-Astra-Deathmatch` or any other repo.
- On the box, touch only your log, `/workspace/gauntlet_sync_cache.git` and `/workspace/gauntlet_sync_work/`. Never modify `/workspace/lab` content, `/workspace/recovery`, recorders or processes.

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
  - All 6 are over 12 KB. **Every file over the 12 KB inline cap is deferred (`DEFERRED_OVERSIZE inline-cap-12KB`) to a real-checkout job that Conductor arranges, and is never pushed inline by this routine.**
