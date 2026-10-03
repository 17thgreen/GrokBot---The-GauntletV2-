# Steward sync analysis, 2026-10-02

Author: The Steward (KALSHI). Written 2026-10-02 about 18:58 ET. All times are ET (America/New_York).
This is a read-only analysis. There were no pushes, no PRs and no repo writes. The pinned v3.1 prompt (`df2f54a6…2997`) was not edited. No recorder or process was touched, and no missing directory was created.
Evidence tags: [V] verified, [I] inferred, [H] hypothesis.

**Inputs**
- Log: `GAUNTLET_SYNC_2026-10-02.log`, sha256 `a5fe5f70…191a` at 18:58 (3,239 lines; last RUN_END is 1840).
- Work dirs: `/workspace/gauntlet_sync_work/run1645`, `run1840` and `t0_iso.txt`.
- Commit times: GauntletV2 commit list (read-only MCP).
- Remote tree: `gauntlet_sync_cache.git` tree at aa9f0f0e, read only, no fetch.
- Ground truth: a fresh walk of `/workspace/lab` under the v3.1 §5 scope (`sa_truth.json` sha256 `d2b6a0e4…4e52`).

The daily hygiene sweep is still writing `HYGIENE_2026-10-02.md`. I did not touch that file.

---

## 1. Why deferred_oversize and in_sync swing: a counting artifact, not box churn

**Short answer:** almost all of the swing is classification drift between runs. The real oversize backlog stayed level at about 47 files all day.

### Ground truth (18:55)
- 1,211 in-scope files: 680 in sync, 530 NEW, 1 MODIFIED [V].
- 130 in-scope text files are over 12 KB [V]:
  - **83 of them are already identical on main** (the 46-file a196580 bundle, the 6 files repaired by 72875aa, and others).
  - **47 are not on main.** This is the real backlog: 44 files of 12–25 KB and 3 over 25 KB.

### Each run's deferred set compared with ground truth [V]

| run | deferred | already on main (miscounted) | real backlog | binaries counted as deferred | real backlog missed |
|---|---|---|---|---|---|
| 0442 | 45 | 0 | 39 | 6 | 8 |
| 0648 | 129 | 83 | 46 | 0 | 1 |
| 0841 | 77 | 38 | 39 | 0 | 8 |
| 1045 | 130 | 83 | 47 | 0 | 0 |
| 1249 | 130 | 83 | 47 | 0 | 0 |
| 1446 | 115 | 75 | 40 | 0 | 7 |
| 1645 | 136 | 83 | 47 | 6 | 0 |
| 1840 | 46 | 0 | 40 | 6 | 7 |

- The union of all deferred paths across the 8 runs is 136. The 1645 set is exactly that union [V].
- Diffs between runs add or remove whole groups of paths: +90/−6, 0/−52, +53/0, 0/0, 0/−15, +21/0, 0/−90 [V].

### Mechanisms
1. **Size gate applied before the in-sync comparison (main driver)** [V]. Runs 0648, 1045, 1249 and 1645 (and 0841 and 1446 in part) tagged the 83 in-sync files over 12 KB as `DEFERRED_OVERSIZE` and dropped them from `in_sync`.
   - The 1645 work file `run1645/summary.json` shows this: in_sync 590 + pending 477 + deferred 136 + skipped 2 = box_elig 1205.
   - If the miscounted files are added back, in_sync rises roughly with landings: 559, 598, 619, 646, 654, 657, 673, 664. The leftover ±9 swing comes from mechanism 3.
2. **Binary check placed before or after the size check** [V]. Five PNGs and one PDF (6 files) are logged `DEFERRED_OVERSIZE` in 0442, 1645 and 1840, and `SKIPPED_NEVER_PUSH non-utf8/binary` in the other runs.
3. **The scope walk differs from run to run** [V by the counts; cause I]. Per-run totals (in_sync + eligible + deferred + skipped) were 1144, 1188, 1146, 1195, 1196, 1157, 1205 and 1203.
   - 0442, 0841, 1446 and 1840 left out 7 in-scope `lab/data/*/provenance/CLOCK_AUDIT_*.json` files (14–24 KB).
   - 1840 also refused 3 `DATA-PROV-TRADES-001/provenance/*.md` files as `data-prov`. That over-reads the never-push rule for "TRADES-001 aggTrade zips".
   - 1249 and 1446 logged 7 `astra-science` skips.
4. **Root cause** [V]. The routine writes a new classifier each run. The reason labels change between runs ("over-25KB", "size-gate-25KB", "gate-25KB", "gate3-25KB"), and so do the order of the gates and the scope rules.

### Real churn: very small [V]
- Only 1 backlog file appeared today: `VARIANTS_HOLDOUT_MAKER_NULL_FEASIBILITY_NOTE_2026-10-02.md` (09:56).
- No deferred path had more than one logged blob across runs.
- All 46 paths in the 1840 deferred set still match their logged blob.
- The 27 in-scope files written since 04:44 are all NEW and small: hourly PULSE and MAXIMIZE_PIN files, one brief, and 3 `capture_status.json`.

### Ruled out
- **Runs cut short before discovery finished** [V]. Every run wrote a full classification, and 1645's summary.json covers all of it.
- **Duplicates** [V]. In the v3.1 runs, each path has exactly one result line per run.

**Suggestion for Conductor (not applied):** pin one classifier script on the box, with a sha256 checked like the prompt. It should compare with main first, then apply never-push, binary, scope and size gates in a fixed order, and only to files that are not in sync. Report `in_sync` and `deferred_oversize` from that script.

## 2. Elapsed time past the 420 s write stop: no write after t0+420 in any v3.1 run

Method: t0 = RUN_END time − elapsed_s. For 1840, t0 is also in `t0_iso.txt` = 18:40:45 [V]. RUN_END has no timestamp in 1045, 1249, 1446 and 1645, so I used the last timestamped line before it. That gives an upper bound on each write's offset. Write times are GauntletV2 commit times.

| run | t0 | last write | offset | verdict |
|---|---|---|---|---|
| 0442 | 04:42:37 | 04:48:35 | +358 | OK [V] |
| 0648 | 06:48:22 | 06:52:43 | +261 | OK [V] |
| 0841 | 08:41:03 | 08:46:58 | +355 | OK [V] |
| 1045 | ≥10:45:40 | 10:52:17 | ≤+397 | OK [V, bound] |
| 1249 | ≥12:49:44 | 12:56:33 | ≤+409 | OK [V, bound] |
| 1446 | ≥14:46:44 | 14:53:23 | ≤+399 | OK [V, bound] |
| 1645 | ≥16:45:52 | 16:49:34 (only write) | ≤+222 | OK [V, bound] |
| 1840 | 18:40:45 | 18:47:12 | +387 | OK [V] |

- The commit chain from 01e9df2 is ebe1a6e → 4723399 → ae42b2a → aa9f0f0, then a6af242, which is the external Cursor Agent repair at 18:51 ET [V]. There are no other routine commits.
- **1840 (491 s):** writes at +231, +327 and +387. `run1840/stats.json` records `write_cutoff_stopped: true` at 433 s, with batch 4 not tried. Only verification of the BAD_ON_MAIN path (logged 18:47:35) and logging ran up to RUN_END at +491, inside the 600 s cap [V].
- **1645 (513 s, 1 landed):**
  - Discovery and staging took until about +157 s (first log line 16:48:29).
  - Batch 1 was the 2 live `capture_status.json` files; both failed the pre-check hash (16:49:13) [V].
  - One 2.3 KB file landed at 16:49:34 (+222).
  - Batch 2 was a single 10,252-byte JSON (`DATA-PROV-CB-001/provenance/CLOCK_AUDIT_CB001_PM007_JOIN.json`). It was staged at 16:50:15 and `_push_args.json` was written at 16:52:21. No commit followed, and no LANDED or ERROR line was logged [V].
  - [I] The run used the rest of its write window trying to send that roughly 10 KB payload exactly as required, and hit the 420 s cutoff at about 16:52:52. The rest went into the PENDING total; logging ran to +513.
  - Small conformance gap [I]: v3.1 §7.3 says a payload that can't be reproduced is logged `DEFERRED_OVERSIZE inline-not-reproducible`. This one wasn't logged at all.
- **Throughput:** a batch of 6–12 KB takes about 60–100 s to send. Discovery and staging take another 130–230 s. So a run lands 5–30 files depending on file size. About 470 files are pending; at today's rate that clears in days, not hours [I].
- **Logging gap** [V]: RUN_START and RUN_END in 1045, 1249, 1446 and 1645 have no timestamp and aren't tab-separated (§8). Suggestion: log t0 in RUN_START and timestamp every line.

## 3. Files that change while the sync runs: inventory and proposed exclusion rule

Running writers (read-only observation; nothing touched) [V]:
- PID 365425: `forward_capture_book.py`, cwd DATA-PROV-PM-006
- PID 365427: `forward_capture_candles.py`, cwd DATA-PROV-CB-002
- PID 366603: `forward_capture_forceOrder.py`, cwd DATA-PROV-LIQ-001

All three started at about 08:49 ET. Their open handles are only `logs/capture.log` and `raw/**`.

The status files are rewritten in place rather than held open, so a check of open files misses them. An mtime check is needed.

| in-scope file | mutation | evidence |
|---|---|---|
| `lab/data/DATA-PROV-CB-002/provenance/capture_status.json` | about every 30 s | mtime samples 18:52:51, 18:53:22, 18:53:53 [V]; 1645 `ERROR precheck-hash` [V] |
| `lab/data/DATA-PROV-LIQ-001/provenance/capture_status.json` | about every 20–40 s | 18:52:55, 18:53:08, 18:53:46, 18:54:13 [V]; 1645 `ERROR precheck-hash` [V] |
| `lab/data/DATA-PROV-PM-006/provenance/capture_status.json` | about every 20 s | 18:53:04, 18:53:15, 18:53:33, 18:53:56, 18:54:16 [V] |
| `lab/data/DATA-PROV-PM-008/provenance/capture_status.json` | not changing now (mtime 10-01 23:12, restore time); its recorder isn't running | `forward_capture_mid.py` writes it [V] |
| `lab/data/DATA-PROV-PM-009/provenance/pull_status.json` | changes only while a pull runs | `pull_starter_l2.py` writes it [V] |
| `lab/governance/astra/steward/HYGIENE_<today>.md` | changes during the daily sweep (18:48 → still being written at 18:52) | mtime [V] |
| `lab/governance/pulses/LAST_LOGAN_BRIEF_<date>.json`, `packets/MAXIMIZE_PIN_*`, `pulses/PULSE_*` | hourly or once-written files, not fast-changing | mtime [V] |

Already outside the sync scope but changing every few seconds: `logs/*.log`, `logs/ops_events.jsonl`, `manifests/chunks.jsonl` and `*.sha256`, `raw/**` (jsonl and csv), `provenance/capture.pid`. The status JSONs also carry market price samples (`last_sample.close`) and the PID, which is runtime telemetry, not provenance.

### Proposed rule for a future prompt version (not applied)

```
never_push (live-mutating runtime state):
  lab/data/**/provenance/capture_status.json
  lab/data/**/provenance/*status.json          # pull_status.json, status.json
  lab/data/**/provenance/progress.json
  **/*.pid  **/*.lock  **/.locks/**  **/*heartbeat*
  **/*-wal  **/*-shm  **/*-journal  **/*.tmp  **/*.partial  **/*.swp
  lab/governance/astra/steward/GAUNTLET_SYNC_*.log   # already
quiescence (DEFERRED_LIVE, not ERROR, not never-push):
  any in-scope file with mtime > t0 - 15 min, or whose sha256 changes between discovery and pre-check,
  or that is open for writing in /proc/*/fd (fdinfo flags O_WRONLY|O_RDWR)
  -> log DEFERRED_LIVE; retry next run; after 3 consecutive DEFERRED_LIVE runs, alert Conductor to classify.
```

**Why:**
- The status files change faster than one sync batch, so they can never verify. They also add a commit every run with no provenance value, and they contain PIDs and price samples.
- Quiescence covers the hygiene sweep's file of the day and any file written in the middle of a run. A hash change found by the pre-check becomes a deferral instead of an ERROR.

## 4. Oversize backlog: real, bundle prepared (not launched)

Input: the `DEFERRED_OVERSIZE` set of the last completed run, `sync-20261002-1840` (46 paths). Every file was re-hashed and all 46 match their logged sha256 [V].

**Excluded or held (9):**
- 6 binaries (5 PNG charts and `KALSHI_EDGE_RESEARCH_2026-09-24.pdf`), which fail UTF-8.
- **HELD for Conductor:** 2 `_prev/` copies of `SCOUT_PERPS_STALE_QUOTE_SCREEN_2026-09-24.md`. The 2026-10-01 ruling says `_prev/` copies stay box-only, and last night's builder refused `_prev/`. The v3.1 scope doesn't exclude them, which is a rule gap.
- **HELD for Conductor:** 1 `packets/ARCHIVIST_SOURCE_GATE_ELECTINDEX_CARD01_2026-09-24.md`. v3.1 allows governance `.md` notes that reference ElectIndex by hash only, but last night's builder refused electindex paths.

**No exclusions were needed for:** live-changing files, never-push paths, secret-scan hits, or files already identical on main (main = a6af242; a6af242 changed only CF_T14_JOIN.md) [V].

**Main bundle:** 37 files, 2,103,664 bytes, all NEW on main. The largest is `LOSS_INVENTORY_2026-10-01.json` (1.40 MB, governance metadata; only names of the private directories, no contents). Conductor may want to drop it.

**Supplement bundle (optional):** the 7 in-scope `lab/data/*/provenance/CLOCK_AUDIT_*.json` files (127,841 B). Earlier runs deferred them, but 1840 skipped them because of the scope variance in §1. They're re-hashed against the 1645 log lines and pass every check.

| artifact | sha256 | bytes |
|---|---|---|
| `steward/GAUNTLET_OVERSIZE_LANDING_LIST_2026-10-02.json` | `0543fbd118f43272772980836ed6fb551e18f56b884ed938cfee2ff84de5fc41` | — |
| `/workspace/steward_gauntlet_oversize_20261001/oversize_bundle_2026-10-02.tar.gz` (37 files) | `26f0fd5b55cc6957fc8b273688c94df3ff0f4e19768e612c0511d2a83219caf8` | 422,626 |
| `/workspace/steward_gauntlet_oversize_20261001/oversize_bundle_2026-10-02_supplement.tar.gz` (7 files) | `efe5573868ec8c460cc3a78879333d70b6eec93cf79b3f1f144ab56a7daea8e3` | 21,905 |

- Each tar has `LANDING_LIST.json` and `SHA256SUMS.txt` at its root, with repo-relative `lab/…` paths.
- Verified by reading every member in memory: each hash matches SHA256SUMS, the box file and LANDING_LIST [V].
- Both are under 25 MB, so no split was needed.
- The builder is `build_list_2026-10-02.py` in the same folder. I put the bundle in the existing `steward_gauntlet_oversize_20261001/` folder, not a new one, because of the no-new-directories rule.
- Nothing was launched.

## 5. Empty-directory sweep (read-only; nothing created)

Method:
- Static scan of 1,209 scripts, configs and routine prompts under `/workspace/lab` and `/workspace/gauntlet_sync_work`, plus 2,476 under `collector_ops`, `kalshi_tools`, `agent-tools`, `teach-sessions`, `mcp_ready` and `tmp`.
- Each script's absolute paths and `__file__`-relative paths were resolved.
- Each directory missing on the box was checked by hand for whether its code creates it.
- `repo_*/.git/refs` was left out on Conductor's ruling.

| missing dir | referenced by | creates it itself? | risk |
|---|---|---|---|
| `/workspace/lab/harness/examiner/out` | 19 harness runners (`run_edge001/003/004`, `run_edge_20260911_001/002/004/005/006`, `run_f1/f3/f4_wick/w2a/w2b/w2c/w2d/w2e/cbvel_incremental`, `run_pm002/pm003_market_baseline`) via `OUT_DIR`/`--out` | yes: every one calls `OUT_DIR.mkdir(...)` or `out_dir.mkdir(parents=True, exist_ok=True)` before writing [V] | low |
| `/workspace/lab/data/DATA-PROV-001/derived` | `provenance/clock_audit_DATA-PROV-001.py:25` (read only, guarded by `DERIVED.exists()`) | n/a (read) | **evidence drift:** the existing audit JSON says `derived_dir_exists: true`, `derived_empty: true` [V], so the dir existed empty before the rebuild. A re-run would now report `false` |
| `/workspace/lab/data/DATA-PROV-FUNDING-001/derived` | `clock_audit_…FUNDING-001.py:24` (guarded read), `download_runner.sh:10` | runner: yes (`mkdir -p "$BASE/derived"`) [V] | low; audit re-run output drifts |
| `/workspace/lab/data/DATA-PROV-OI-001/derived` | `clock_audit_…OI-001.py:28` (guarded read), `download_runner.sh:10` | runner: yes [V] | low; audit report shows `derived_empty: true` [V], so a re-run drifts |
| `/workspace/lab/data/DATA-PROV-TRADES-001/derived` | `clock_audit_…TRADES-001.py:29` (guarded read), `download_runner.sh:15` | runner: yes [V] | low; same drift as above |
| `/workspace/lab/data/DATA-PROV-TRADES-001/provenance/.locks` | `download_runner.sh:10` (`LOCK_DIR`) | yes (`mkdir -p … "$LOCK_DIR"`) [V] | low |
| `/workspace/recovery` | v3 and v3.1 prompts §11 (listed only as "never modify") | n/a | none; deleted on purpose 10-02 03:25 |

Not real gaps, so not counted:
- Sentinel or flag files that are absent by design: weather-nowcast `FORCE_PHASE_A_LOW`, `FORCE_PHASE_B`, `KALSHI_429_STOP`.
- File-name prefixes the scan matched as directories (`supervisor/record_`, `logs/collector_`).
- About 90 references inside frozen vendored pin copies (astra-science `runner_tree/**/pins/**`, `snapshot_runner_extract`, `/workspace/tmp/examiner_scratch_*`, `tmp/c4run`, `tmp/wxfl/bundle_stage`) and the 10-02 repair stage copies. These point to their original layout (`results/`, `pins/`, `fixtures/`, `logs/`) and aren't run where they sit.
- `scout_card06_company_kpi/raw/kalshi` was a false positive (the scan misread `$(dirname $0)/..`). It exists [V].
- Recorder supervisors (ADMIT-1 `admit1_supervisor.sh`, weather `supervisor.sh` and `collector.py`, the 3 forward-capture recorders): every directory they reference exists [V].
- Observation only: at 18:52 there was no `record.py` process on the box. ADMIT-1 run 19 belongs to Collector; I didn't touch it.

**Conclusion:** none of the lost empty directories breaks a running recorder, capture job or the sync. The only material effect is that a clock-audit re-run would see 4 missing `derived/` folders. I'm listing this only; nothing was created.
