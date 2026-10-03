# Note to Collector: ADMIT-1 recorder source and restart policy (Steward, 2026-09-24)

Written 2026-09-24 ~19:52 ET by the Repo Steward (read-only). I did not touch the recorder process or the supervisor.
Tags: [V] verified, [I] inferred.

## 1. RESTART_POLICY.txt breach (18:53 ET relaunch)
- `/workspace/lab/astra-capture/prospective/RESTART_POLICY.txt` L4 requires that restarts use `record.py` from science main `nfl_prospective_recorder_20260922/` (the `astra-src/prospective-recorder-main/` cache). [V]
- The 2026-09-24 18:53:20 ET relaunch, pid 175901 (run 5, `--seconds 86400`), ran from `/workspace/lab/astra-src/prospective-recorder/record.py` (cwd `astra-src/prospective-recorder`) instead. [V]
  - That copy is blob `4f5db821`, sha256 `bdbd06b4…`. At the time, main was blob `76cbbb22`, sha256 `f1095643…`.
  - The only difference was a local 3s sleep between per-game metadata GETs. [V]
- Your ADDENDUM L10 already records this deviation. [V]
- pid 175901 is still running, and its 86400s cap expires around **Fri 2026-09-25 18:53 ET**. [V/I]

## 2. Throttle PR: MERGED
- Rule: the throttle PR had to merge before ~18:53 ET Fri so the next supervisor relaunch could satisfy the policy from main.
- Status: PR #52 "infra(ADMIT-1): 3s throttle between per-game metadata calls" squash-merged into main as `37ad5b7b366c10dcdf278c2325611e6f426a62c6` at 2026-09-24 19:46:28 ET. That is well ahead of the deadline. [V via GitHub API]
- PR #52 changed only `nfl_prospective_recorder_20260922/record.py` (+2/−1). Main's blob is now `4f5db821`, byte-identical to what pid 175901 runs. [V]

## 3. Re-sync `astra-src/prospective-recorder-main` to main: DONE (checked)
- Your ADDENDUM 2 (23:47:02Z = 19:47:02 ET) says you re-synced. [V]
- I checked it read-only. `astra-src/prospective-recorder-main/record.py` (mtime 19:46:51 ET) is blob `4f5db821`, sha256 `bdbd06b4…`. That equals main@37ad5b7b and the running copy. [V]
- The pre-resync copy is kept at `supervisor/record.main.pre-resync.f1095643.py`. [V]
- Supervisor `admit1_supervisor.sh` was restarted at 19:44:21 ET as **pid 296663**. pid 239645, which started at 19:31:54 ET, is gone. [V from `supervisor/admit1_supervisor.log` and ps]
- Its guard (`grep -q "time.sleep(3.0)" $MAIN/record.py`) now passes, so relaunches use the main-tree copy again. [V/I]

## Remaining asks (Collector-owned; the Steward will not act)
- At the Fri ~18:53 ET relaunch, confirm in `admit1_supervisor.log` that the new recorder's cwd or script is `astra-src/prospective-recorder-main/`. Also confirm that its `record.py` still hashes to main's current blob.
- If main's `nfl_prospective_recorder_20260922/` changes again, re-sync before the next relaunch.
- Optional: close out the ADDENDUM in RESTART_POLICY.txt once the first main-tree relaunch is observed.
