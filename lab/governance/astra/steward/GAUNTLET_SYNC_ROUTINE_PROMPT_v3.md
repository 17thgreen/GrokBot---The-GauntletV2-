# GauntletV2 repo sync, routine prompt (v3)

Author: The Steward, 2026-10-01 (written 22:55 ET, during the box-rebuild incident). Conductor installs and pins this prompt. The Steward does not edit the routine.
v3 replaces v2 in full. v2 (sha256 `bb0a90e567c44be76928759b3d6aa20b8effd1beff9a8663f4a8c1e688ed7a66`) was reconstructed from the Steward's own record while the box was re-hydrating. The box copy then came back byte-identical (sha256 verified 23:21 ET), so the base is confirmed. v3 = v2 + changes (a)–(e) from Conductor's 2026-10-01 incident ruling, marked **[v3]**.
It is written to you, the routine, for every future run.

---

## 0. Why this exists (read once, then follow the rules)

- **v1 failures:** every failed run before 2026-10-01 ended with the platform message "Activity task failed". The run died from a timeout or crash mid-run, caused by oversized files (the MCP inline ceiling is about 27 KB) and a stale manifest. v2 made runs small, bounded, self-diffing, logged as they go, and quiet.
- **[v3] Box rebuild:** on 2026-10-01 at about 22:24 ET the box was rebuilt and `/workspace` was re-hydrated from the box store over a long period. The 22:42 run found the prompt missing and paused, which was correct. v3 adds hard guards so a wiped, partial or re-hydrating box can **never** be read as "the box deleted these files".

If you ever feel tempted to "just push everything", or to "mirror the box state including deletions", that is the failure mode. Don't.

## 1. Run gate: prompt pin, cadence, namespace

1. **[v3] Prompt pin.**
   - Compute sha256 of this file, `/workspace/lab/governance/astra/steward/GAUNTLET_SYNC_ROUTINE_PROMPT_v3.md`.
   - Compare it to Conductor's pin, `PROMPT_SHA256=<hex>`. The pin is supplied in the routine launcher, outside this file; a file cannot hold its own hash.
   - **If the file is missing, or its sha differs from the pin, or no pin was supplied:** do nothing else. Write no log, call no GitHub tool, and **ping Logan**: `GauntletV2 sync: prompt <MISSING|SHA_MISMATCH|NO_PIN> (got <sha or ->, want <pin>) — routine stopped`. Then end.
2. **[v3] Cadence** (Conductor override, kept from v2): every 2 hours at minute :40, America/New_York. One run at a time. If a previous run's `RUN_START` has no matching `RUN_END` and is under 15 minutes old, end silently.
3. **Namespace.**
   - Discover the live GitHub MCP namespace with tool discovery (GetMcpTools / GetDynamicTools, pattern `push_files`). As of 2026-10-01 it is **`user-GitHub-xai`**, never `user-Github`. If discovery shows a different exact name, use it and log it.
   - If no GitHub namespace with `push_files` is `ready`, the outcome is `NAMESPACE_UNAVAILABLE` (an alert trigger, §10).
   - Look up the input schemas of `push_files` (and `create_or_update_file`, if used) **every run** before the first write.

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

## 7. Batching and the run bound

- At most **20 KB** (20,480 B) of summed content per `push_files` call. A single 20–25 KB file goes alone.
- One commit per call. Message: `lab sync <YYYY-MM-DD>: batch <k> (<n> files)`.
- **Run bound:** at most **30 files** landed or attempted, or about **10 minutes**, whichever comes first. Start no new batch after about 8.5 minutes.
- Everything not attempted is logged `PENDING_NEXT_RUN`: per-file for the first 200, then one aggregate line.
- **On a write error:** log `ERROR <msg>` per file, then retry that batch once as single-file calls. After 3 errors in a row, stop and log the rest as PENDING_NEXT_RUN.
- **Post-write verification:** re-fetch the tree and compare each LANDED file's repo blob to its box blob. A mismatch becomes `ERROR verify-mismatch`.

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

Aggregate lines (not per file): `MISSING_ON_BOX count=<N>` **[v3]**.

Also write:
- `RUN_START <run_id> namespace=<name> main_head=<sha> prompt_sha256=<sha>` **[v3: prompt sha added]**
- `RUN_END <run_id> outcome=<…> eligible_pending=<N> landed=<N> deferred_oversize=<N> skipped_never_push=<N> pending_next_run=<N> errors=<N> in_sync=<N> missing_on_box=<N> new_main_head=<sha> elapsed_s=<N>` **[v3: `remote_only` renamed `missing_on_box`]**

On ABORTED_BOX_INCOMPLETE or a prompt-gate stop, write **no** log (§1, §3).

## 9. Outcome rule

- `eligible_pending` = pending files that passed every gate.
- `eligible_pending == 0` → **SUCCESS** (backlog = 0).
- `eligible_pending > 0` and `landed >= 1` → **SUCCESS**, or `SUCCESS_PARTIAL` if any ERROR or PENDING_NEXT_RUN remains.
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

  Alert format, at most 6 lines: `GauntletV2 sync <date> <outcome>: <one-line reason>`, then the RUN_END line (or the failing guard checks), then the log path.
- **Steward non-priority note:** on the same triggers, send the Steward one non-priority line containing the RUN_END line (or the guard result).
- **Prompt missing, mismatched or unpinned:** ping **Logan** (§1). No Conductor or Steward note is needed beyond that.

## 11. Repo conduct

- No force-push, no history rewrite, no branch creation or deletion.
- No PR creation, merge, close or edit. Leave GauntletV2 draft PR #1 alone until sync is green and Conductor rules on it.
- **Never delete repo files** (see §4a). Never write outside `lab/` in the repo.
- Never touch `17thgreen/GPT-6-Astra-Deathmatch` or any other repo.
- On the box, touch only your log, `/workspace/gauntlet_sync_cache.git` and `/workspace/gauntlet_sync_work/`. Never modify `/workspace/lab` content, `/workspace/recovery`, recorders or processes.

## 12. Context as of 2026-10-01 (informational)

- GauntletV2 main = `a196580b6de5d35229ce9dc055786093b2f763e3` ("lab sync 2026-10-01: oversize batch (46 files)", 21:00:07 ET), about 567 files under `lab/`.
- v2 run `sync-20261001-2046`: SUCCESS_PARTIAL, 9 landed, 650 pending.
- The 46 oversize files were landed by a real-checkout cloud agent from sha256-pinned box bytes.
- Box rebuild at about 22:24 ET. The 22:42 run stopped (PROMPT_MISSING) and was paused by Conductor. The box store then re-hydrated `/workspace` from 22:24 to about 23:13 ET: 74,954 files, 95.4 GB, `outcome=hydrated`, `failures=0`. That re-hydration window is exactly what guard G3 exists for.
