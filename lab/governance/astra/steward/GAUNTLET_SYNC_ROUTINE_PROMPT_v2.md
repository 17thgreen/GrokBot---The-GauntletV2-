# GauntletV2 repo sync, daily routine prompt (v2)

Author: The Steward, 2026-10-01, at Conductor's request. Conductor installs this prompt. The Steward did not edit the routine.
This replaces the v1 prompt in full. It is written to you, the routine, for every future run.

---

## 0. Why v2 exists (read once, then follow the rules)

Every failed run since 2026-09-22 ended with the platform message **"Activity task failed"**. That means the run itself died, from a timeout or a crash mid-run. It was not a GitHub refusal. The last good sync was commit `61e284fb` ("lab sync 2026-09-22: micro 22/22", 2026-09-22 18:09:45 ET).

Conductor's root cause has two parts:
- Runs tried to push oversized files. The MCP inline payload ceiling is about 27 KB.
- Runs worked from a stale manifest (`/workspace/gauntlet_sync_20260922/manifest.json`) instead of the live difference.

v2 makes every run **small, bounded, self-diffing, logged as it goes, and quiet when nothing happens**. If you ever feel tempted to "just push everything", that is the failure mode. Don't.

## 1. Fixed facts

- **Source:** `/workspace/lab` on the box. The box is the source of truth for content.
- **Target:** GitHub repo `17thgreen/GrokBot---The-GauntletV2-`, branch **`main`**. Commit directly to main. That is the established convention (`lab sync YYYY-MM-DD: …` commits via MCP `push_files`).
- **Write path:** the GitHub MCP connector only.
  - At the start of every run, discover the live namespace with tool discovery (GetMcpTools / GetDynamicTools; pattern `push_files`). As of 2026-10-01 it is **`user-GitHub-xai`** (capital G, capital H, `-xai` suffix). It is **never `user-Github`**.
  - If discovery shows a different exact name, use the name discovery shows and note it in the log.
  - If no GitHub namespace with `push_files` is `ready`, log `ERROR namespace-unavailable` and stop. That is an error run, so report it.
  - Look up the input schema of `push_files` (and `create_or_update_file`, if you use it) **every run** before the first write. Never call from memory.
- **Log file:** `/workspace/lab/governance/astra/steward/GAUNTLET_SYNC_<YYYY-MM-DD>.log`. Use the run date in America/New_York. Append only; create the file if it is missing.

## 2. Forbidden inputs

- Never read a file list from `/tmp`.
- Never read `/workspace/gauntlet_sync_20260922/manifest.json`, or any other saved manifest, as the to-do list. It is stale by construction.
- Never resume "where the last run left off" from memory. The diff (§4) is the only to-do list.

## 3. Scope: what is eligible to sync

Mirror GauntletV2's existing `lab/` layout. Box path `/workspace/lab/<X>` maps to repo path `lab/<X>`.

| box subtree | rule |
|---|---|
| `lab/governance/**` | eligible, except: in `lab/governance/astra/packets/`, only the top-level `*.md` files and `packets/extracts/**` are eligible (the selective packets rule, unchanged since 2026-09-22). Other packet subdirectories are not mirrored. |
| `lab/archive/**` | eligible |
| `lab/execution/**` | eligible |
| `lab/harness/**` | eligible text sources/specs only: `*.py *.md *.json *.yaml *.yml *.toml *.txt *.cfg *.ini *.sh`. Skip any `results/`, `out/`, `runs/`, `data/`, `.venv*/` and `__pycache__/` directories. |
| `lab/data/**` | **metadata only:** `*.md` files, plus `*.json` files directly under a `provenance/` directory. Never `raw/`, `slices/`, `sealed/`, parquet, zip, ndjson, csv or tick files. GauntletV2's `.gitignore` ignores `lab/data/` because the data is too large; MCP writes bypass `.gitignore`, so **you** enforce this. |
| everything else under `/workspace/lab` | **out of scope. Never push.** This includes `astra-science/` (a clone of a different repo), `astra-capture/`, `astra-data/`, `astra-kits/`, `astra-src/`, `catalyst/`, `evidence_private/`, `evidence_cold/`, `tmp/`, `.venv/`, `.venv_scout/`, and top-level loose files such as `tmp_grok_memo.txt`. |

Also out of scope:
- All `steward/GAUNTLET_SYNC_*.log` files. They are box-only, because they name paths of files that were refused.
- Any file not valid UTF-8 text. Log it `SKIPPED_NEVER_PUSH` with message `non-utf8/binary`. Binary files need a real checkout and a Conductor decision.

Never delete anything on GauntletV2. A file present on GauntletV2 but absent on the box is only counted, as `remote_only=N` in the run summary.

## 4. Build the pending list fresh, every run

1. **Read GauntletV2 main's tree.** Pick one method:
   - **Preferred (keeps the tree out of your context):** a persistent blobless bare cache at `/workspace/gauntlet_sync_cache.git`. **Not `/tmp`.**
     - First time only: `git init --bare /workspace/gauntlet_sync_cache.git`
     - Each run:
       - `git -C /workspace/gauntlet_sync_cache.git fetch --filter=blob:none --depth=1 https://github.com/17thgreen/GrokBot---The-GauntletV2-.git +refs/heads/main:refs/heads/main`
       - then `git -C … ls-tree -r main`
     - **Never pass `-l` to `ls-tree` on this cache.** That lazily downloads every blob and is a known way to hang a run.
   - **Fallback:** the MCP `get_repository_tree` tool for `main`, recursive. Look up its schema first.
2. **Walk the eligible box files** (§3). Skip symlinks. Prune `.venv*`, `__pycache__`, `.git` and `node_modules` while walking; do not descend into them.
3. **Compute each file's git blob sha** = `sha1("blob " + <byte length> + "\0" + <bytes>)`. Also compute `sha256` for the log.
4. **Classify each file:**
   - blob sha equals the repo entry at the same path → in sync. Not logged per file; counted.
   - path absent in repo → NEW
   - present with a different blob → MODIFIED
5. **Order the pending files:** MODIFIED first, then NEW, each sorted by path. The order must be deterministic, so consecutive runs make progress and do not thrash.

A Python helper is fine. Run it with Shell. Write the pending list only to memory, or to a scratch file under `/workspace/gauntlet_sync_work/` (not `/tmp`). It is rebuilt next run anyway.

## 5. Gates before every write, in this order

For each pending file, before it enters a batch:

1. **Never-push check.** If any rule below matches, log `SKIPPED_NEVER_PUSH` with the matching rule and do not push.
   - path under `lab/evidence_private/` (any depth), or any `_prev/` copy of evidence_private material
   - path under `lab/governance/astra/packets/card01_hybrid_forecast/source_probe_electindex/`
   - **ElectIndex raw bytes:** any capture, response body, HTML/JSON dump or log fetched from ElectIndex. Any path containing `electindex` (case-insensitive) that is not a governance `.md` note is refused. Hash-only references in governance notes are allowed; this follows the ARCHIVIST_SOURCE_GATE_ELECTINDEX_CARD01_2026-09-24 ruling, APPROVED_HASH_ONLY.
   - **Secrets:**
     - API keys, Key IDs, PEM/private keys (`*.pem`, `*.key`, `*.p12`, `*.pfx`, `id_*`), `.env` / `.env.*`, anything from `/home/box/.secrets/`
     - Alchemy (or other RPC) URLs with embedded keys
     - `Gauntletkey.docx`, and **all `*.docx`**
   - **Raw market data:**
     - raw ticks (CF/BRTI/Kalshi/Polymarket tick or orderbook dumps)
     - `*.ndjson`, `*.parquet`, `*.zip`, `*.gz`, `*.sqlite*`, `*.db`, `*.csv` over 25 KB
     - `data/DATA-PROV-001/` OHLCV parquets, `data/DATA-PROV-TRADES-001/` aggTrade zips
     - `**/DATA-PROV-*/raw|slices|sealed/`
     - any multi-MB data file
   - Examiner or any `.venv*/`, `__pycache__/`, `*.pyc`
   - anything that came from `/tmp`
   - any file under `lab/astra-science/` (a different repo's clone)
2. **Content secret scan** (text files only). Refuse with `SKIPPED_NEVER_PUSH secret-pattern:<name>` if the file contains any of:
   - `-----BEGIN` … `PRIVATE KEY`
   - `KALSHI-ACCESS-KEY` followed by a value
   - `api[_-]?key\s*[:=]\s*['"][A-Za-z0-9_\-]{16,}`
   - `sk-[A-Za-z0-9]{20,}`
   - `ghp_[A-Za-z0-9]{30,}` or `github_pat_`
   - `alchemy\.com/v2/[A-Za-z0-9_\-]{10,}`
   - `Bearer [A-Za-z0-9\-_.]{20,}`

   Do not print the matched text into the log.
3. **Size gate.** If size is over **25 KB** (25,600 bytes), log `DEFERRED_OVERSIZE` and do not push. **This is not a failure.** Oversize files need a real-checkout cloud agent, which Conductor arranges separately.

When unsure, refuse. A refused file costs nothing. A leaked file cannot be recalled.

## 6. Batching and the run bound

- **Batch size:** the summed content of one `push_files` call must be **20 KB or less** (20,480 bytes). Fill batches greedily in pending order.
- A single eligible file of 20–25 KB goes **alone** in its own call.
- One commit per call. Message: `lab sync <YYYY-MM-DD>: batch <k> (<n> files)`.
- **Run bound:** stop after **30 files landed or attempted**, or **about 10 minutes** wall-clock from run start, whichever comes first. Do not start a new batch after about 8.5 minutes.
- Every pending file not attempted is logged `PENDING_NEXT_RUN`, one line per file, with path, size and sha. If there are more than 200, write per-file lines for the first 200 and one aggregate line `PENDING_NEXT_RUN count=<N>`.
- **On a write error:**
  - Log `ERROR <short message>` for each file in that batch.
  - Retry that batch **once** as single-file calls.
  - If 3 calls in a row error, stop the run. Log the rest as `PENDING_NEXT_RUN`.
- **Post-write verification:** after the last batch, re-fetch the tree (§4 step 1). Compare each LANDED file's repo blob sha to the box blob sha. A mismatch rewrites that file's result to `ERROR verify-mismatch` (for example, newline or encoding drift).

## 7. Log format

Append to `/workspace/lab/governance/astra/steward/GAUNTLET_SYNC_<YYYY-MM-DD>.log` **as you go**: after every batch, not only at the end. A run that dies still leaves its trail.

Tab-separated, one line per file:

```
<ISO time ET>  <run_id>  <repo path>  <size bytes>  <sha256>  <git blob sha>  <RESULT>  <message or ->  <commit sha or ->
```

RESULT is one of:
- `LANDED`
- `SKIPPED_NEVER_PUSH`
- `DEFERRED_OVERSIZE`
- `PENDING_NEXT_RUN`
- `ERROR`

Also write:
- `RUN_START <run_id> namespace=<name> main_head=<sha>` at the start
- `RUN_END <run_id> outcome=<…> eligible_pending=<N> landed=<N> deferred_oversize=<N> skipped_never_push=<N> pending_next_run=<N> errors=<N> in_sync=<N> remote_only=<N> new_main_head=<sha> elapsed_s=<N>` at the end

Out-of-scope subtrees (§3) are counted, not listed.

## 8. Outcome rule

- `eligible_pending` = pending files that passed every gate in §5. These are the files this run should land.
- `eligible_pending == 0` → **SUCCESS** (nothing to do). Deferred or skipped files alone never make a run fail.
- `eligible_pending > 0` and `landed >= 1` → **SUCCESS**. Use `SUCCESS_PARTIAL` if any ERROR or PENDING_NEXT_RUN remains.
- `eligible_pending > 0` and `landed == 0` → **FAILED**.

Finish cleanly: always write `RUN_END`, then end normally. Do not let an exception escape. Catch it, log `ERROR`, and write `RUN_END`.

## 9. Repo conduct

- No force-push. No history rewrite. No branch creation or deletion.
- No PR creation, merge, close or edit. **Leave GauntletV2 draft PR #1 alone** until sync has been green (SUCCESS with `pending_next_run=0` and `errors=0`) and Conductor rules on it.
- Never delete repo files. Never write outside `lab/` in the repo.
- Never touch `17thgreen/GPT-6-Astra-Deathmatch` or any other repo from this routine.
- Touch only your own log file on the box. Do not modify `/workspace/lab` content, and never touch running recorders or processes.

## 10. Reporting

Send Conductor a **concise** summary **only if** at least one of these is true:
- something LANDED
- any ERROR occurred, or the outcome is FAILED
- `deferred_oversize > 0` (report the count and the paths, up to 15)

Otherwise stay quiet (no message), and the log line is the record.

Summary template, at most 8 lines:
`GauntletV2 sync <date> <outcome>: landed <n> in <k> commits (<first>..<last>), pending_next_run <n>, deferred_oversize <n>, skipped_never_push <n>, errors <n>. Log: steward/GAUNTLET_SYNC_<date>.log.` Add one line naming any error.

## 11. Context as of 2026-10-01

- GauntletV2 main = `61e284fb` (528 tree entries).
- A rough Steward estimate of the in-scope backlog at 19:12 ET is about 660 eligible files (about 2.7 MB) and about 51 oversize files. At 30 files per run, that is about 22 runs to catch up.
  - This is [I], an approximation of §3. Your own diff is authoritative.
  - Conductor may change cadence; this prompt does not.
- 10 oversize `lab/harness/examiner/src/run_*.py` files (27–41 KB) are known DEFERRED_OVERSIZE. Conductor handles them outside this routine.
