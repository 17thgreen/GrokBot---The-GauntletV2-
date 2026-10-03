# PROPOSAL: *status.json files on GauntletV2 main (2026-10-03)

Author: The Steward, 2026-10-03 04:52 EDT. Trigger: RUN_END sync-20261003-0445 BAD_ON_MAIN on `lab/data/DATA-PROV-CB-002/provenance/capture_status.json` (expected cf09a8a4, main b22de473, box since moved on). Conductor ruled it **STALE_LIVE_ACCEPTED**. Nothing was repaired or deleted. This is a proposal only.

## 1. Inventory (connector tree of main `386be3a221dc9268df6040cf9e377ca893ca518d`, recursive, not truncated, 712 blobs) [V]
Searched for: `*status.json`, `progress.json`, `*.pid`, `*.lock`, `.locks/`, `*heartbeat*`, `-wal/-shm/-journal`, `*.tmp/.partial/.swp`, `_prev/`, `ARCHIVIST_ELECTINDEX_*`, `LOSS_INVENTORY_2026-10-01.json`, evidence_private, electindex. Only 2 matches are on main, both `provenance/*status.json`:

| path | main blob | size | last commit touching it | box blob | box mtime (ET) | live? (modified within 1 h) |
|---|---|---|---|---|---|---|
| `lab/data/DATA-PROV-CB-002/provenance/capture_status.json` | `b22de473` | 596 | `6341a616` "lab sync 2026-10-03: batch 1 (2 files)", 04:47:11 ET 10-03 | changes every ~30 s (3c13f9c0 at 04:51:05) | 10-03 04:51:05 | **YES**: recorder PID 365427 running, `state: running` |
| `lab/data/DATA-PROV-PM-009/provenance/pull_status.json` | `c9efe32a` | 285 | `128bf876` "lab sync 2026-10-02: batch 2 (6 files)", 20:50:08 ET 10-02 | `c9efe32a` (= main) | 10-01 22:51:21 | **NO**: terminal `state: done`, `updated_at 2026-09-14` |

Content is runtime state only: data_id, updated_at, pid, state, counters, last sample. No secrets [V]. Both were pushed by the live v3.1 routine, which has no status-file rule [V].

**Not yet on main, but still pending under v3.1** [V, by v3.2 classifier dry run 04:52 ET]: LIQ-001, PM-006 and PM-008 `capture_status.json` (NEW). v3.1 will keep trying to push them, and each one is live (or dormant, for PM-008). Expect more precheck ERRORs or BAD_ON_MAIN until v3.2 is pinned [I].

## 2. How v3.2 (proposal ece11daa…, classifier 573658fd…) treats these
- Classifier [V, dry run 04:52 ET, main 386be3a2]: all 5 box `provenance/*status.json` → `SKIPPED_NEVER_PUSH live:status-json`. That covers the CB-002 path on main (state MODIFIED) and the PM-009 path (state IN_SYNC).
  - G1 runs before the compare and before the quarantine check, so they are **not** counted as BAD, in-sync or pending, even when listed in `quarantine.txt` (tested) [V].
- `missing_on_box` excludes never-push paths, so deleting them from main would not raise MISSING_ON_BOX or guard G5 [V, code].
- **Gap [V, prose §1 step 5]:** the BAD_ON_MAIN register is built from log lines ("BAD_ON_MAIN with no later REPAIRED"). The CB-002 path will stay on it forever. Each run would re-compare it (main b22de473 vs an ever-changing box blob, or vs an absent blob after a delete), re-log BAD_ON_MAIN and alert every run. The classifier skipping it does not stop that.
  - **Proposed v3.2 delta (not applied):** in §1 step 5, a register path that matches a §6 gate 1 never-push rule is logged once as `RETIRED never_push:<rule>`, leaves the register like REPAIRED, and is never written.
  - Under v3.1 the same alert repeats every run until v3.2 is pinned. Conductor may want to accept that knowingly [I].

## 3. Options
**(i) Leave as frozen historical snapshots**, plus a marker note (for example `lab/data/README_STATUS_SNAPSHOTS.md`, or a line in each dataset's FORWARD_CAPTURE.md) saying the files are frozen copies, not live.
- Pro: no deletion, and git keeps everything anyway.
- Pro: PM-009's terminal `done` record is a valid provenance fact.
- Con: CB-002's snapshot says `state: running` and `updated_at 2026-10-03T08:47Z` forever, which misleads any reader of main.
- Con: the marker note is itself a push that v3.1 would do inline.
- Con: v3.2 never-push means the snapshots never update, so the main copy and the box copy disagree permanently.

**(ii) Delete both from main in one Conductor-GO'd PR.**
- Pro: main returns to the intended state. No status file was on main before 20:50 ET 10-02; both arrived as v3.1 side effects.
- Pro: consistent with the v3.2 never-push policy (these paths should not exist on main).
- Pro: removes a misleading "running" record.
- Pro: git history keeps both versions if anyone needs them.
- Downstream readers: references found [V] are `DATA-PROV-PM-006/FORWARD_CAPTURE.md` and `REPORT.md`, `LIQ-001/FORWARD_CAPTURE.md`, and the capture/pull scripts. They describe the **box** runtime file the recorder writes. None cites a copy on main as evidence.

## 4. Recommendation: (ii), sequenced after v3.2 is pinned
Delete both status files from main in one PR, but only **after** v3.2 (with the `lab/data/**/provenance/*status.json` never-push glob) is pinned. Deleting under v3.1 would make them NEW again, and v3.1 would re-push them on the next run [I, from v3.1 §4/§5].

Pair the PR with the `RETIRED never_push` register delta in §2, so the CB-002 BAD_ON_MAIN stops alerting. Until then, take no action (effectively (i) without a marker), and accept the repeating CB-002 alert as STALE_LIVE_ACCEPTED.

`_prev`/provenance rules: no `_prev` copy is needed for a repo deletion. The box files are the originals and stay untouched, and git history preserves the main versions. The PR must touch only these 2 paths, and nothing from evidence_private, source_probe_electindex or ElectIndex.
