# EXAMINER FREEZE AMENDMENT — Q7B-P2-AMEND-1 (Q7-B Pass-2 tape walk)

- **Seat:** Examiner KALSHI · **Written:** 2026-09-24T19:49:08-04:00 · **JSON created_at:** 2026-09-24T19:48:50-04:00
- **Status:** `APPROVED_PENDING_POST_WALK_REHASH` · scored=false · promote=false
- **Authority:** Conductor ruling of 2026-09-24 (~19:47 ET) on the Q7-B P2 HOLD. The Conductor chose option (B) with conditions, **without seeing any B2 outcome**.
- **Filed while the walk (pid 241785) is still running and before any Examiner review of outcomes.** The Examiner did not read or cite any B2 P&L.
- **HOLD stamp (unchanged, still in force):** `packets/EXAMINER_HOLD_Q7_B_PASS2_TAPE_WALK_BYTES_2026-09-24.json` sha256 `6874c6b6a770cc2312701ab3f0761b7f4b8573195665bf2e61844c32e660caea`

## Pins
| Item | sha256 |
|---|---|
| Amendment JSON `EXAMINER_FREEZE_AMENDMENT_Q7B_P2_AMEND_1_2026-09-24.json` | `54c9ba500c74776345455cb72966755262a4f121876420d6d3a7496c75a5a600` |
| Verifier `EXAMINER_Q7B_P2_AMEND_1_REHASH.py` (pinned here only, to avoid circularity) | `9ebbaf27751538cf7745d36b0334d8e413c01b8f7f5e15c74679a77474ddda10` |
| Runner `/workspace/lab/astra-science/nfl_q7_rehab_p2_rank_sizing_20260923/run_tape_walk.py` (re-verified on disk at filing) | `a06a105fa25269c17bcc1f53d9ae498343097c189ee619aeada7cceb76d3399b` |
| Bytes diff `Q7_B_PASS2_TAPE_WALK_BYTES_DIFF_2026-09-24.diff` | `325bf2d71136234b27e3ae873ac4499bedf2844023421b8caae0b47225422ca2` |
| Runner diff `Q7_B_PASS2_TAPE_WALK_SCRIPT_DIFF_2026-09-24.diff` | `01fdfe9c7ee8f5300421351a6468bdfeba5e2cbc04a52f835966bab9f526076d` |
| Checkout `/workspace/lab/astra-science` commit | `cb6223989afaf9e2f2fde8516e5ce16098ef7160` (plus uncommitted working tree; pins are working-tree bytes) |

## What is approved
Removing `parent_pin_mismatches()` and the FAILED_PARENT_CODE_PIN_MISMATCH refusal from the runner (HOLD hunks H4 import drop + H9) is approved **for THIS P2 run only**, at runner sha `a06a105f…`. The JSON carries the full 49-file manifest (path, sha256, P1-baseline sha256, classification). All 49 were re-verified at filing: 46 IDENTICAL_TO_P1, 3 DIFFERS (runner; rank_sizing_policy = the freeze-sanctioned knob; selection = B1->B2 label only).

## Substitute guard (replaces the runtime gate for this run)
At scoring time, **AFTER the walk finishes**, the Examiner runs the external re-hash:
`python3 packets/EXAMINER_Q7B_P2_AMEND_1_REHASH.py --label SCORING_TIME_CHECK`

It covers:
- the runner
- the 49-file manifest
- 19 code-pin guard files (7 Q7 paircheck, Q6 SHADOW_CANDIDATE_FREEZE, factorial_policy, adaptive_policy, feebook, 2 P1 dead-knob files, P2 spec, 5 P2 implementation files)
- 7 Conductor packets, plus their governance mirrors
- SOURCE_PINS `5ee602ba…` at both paths
- both diffs, the HOLD stamp, Addendum A, and the 2 attempt-1 provenance files
- the label check: Q6 `SHADOW_CANDIDATE_FREEZE.json` selected == `000`

Every expected sha256 is listed in the JSON `rehash_targets` and `substitute_guard`. **ANY mismatch voids P2.** Before running it, confirm the verifier's own sha256 matches the pin above.

## Forward rule
P3 and every later pass **must** call `parent_pin_mismatches()` again at runtime. No seat may remove or disconnect a guard without a freeze amendment filed before the run.

## Scorecard caveats
- The P1 runner baseline stays **INFERRED**: `c74397385da40f3c88f3ff2def409afbcf5f1b503b87f810abbb86ec5f3d937d`. Confidence that it is byte-identical to what ran P1 is low to medium.
- Attempt 1 (`results_attempt1_brokenpool_20260923/`) is **INFRA/VOID** and never scored, per Adversary pre-flag (iii) and the Refiner ledger (pass 2 attempt 1 VOID).
- The attempt-1 runner is **INFERRED** at `attempt1_runner_sha256_inferred = c6e3734170e284fde73be061b2dc2f0dd140bd8b5db250d6070d92c72e3d26d5`. The Simulator did not record it; it reconstructed the file by reversing 2 lines. Provenance files, not modified:
  - `provenance/run_tape_walk_attempt1_RECONSTRUCTED_INFERRED.py`: `c6e37341…`
  - `provenance/attempt1_to_attempt2.diff`: `d38a29c84142363b8ed6d5deb47ef0daff9fe62c2a1ff29c7e21ba73277bf5a7`
- Examiner verification of the attempt-1 reconstruction, all read-only:
  1. The reconstruction hashes to `c6e37341…`. PASS.
  2. Diff against the current runner shows exactly 2 changes (`import os`; env `TAPE_WALK_MAX_WORKERS` in main()). The patch, applied to a /tmp copy only, reproduces `a06a105f…` byte-for-byte. PASS.
  3. Line 494 is `result = future.result()`, matching the attempt-1 tracebacks. PASS.
  4. SOURCE_PINS is still a hard gate. `reverify_source_pins()` runs first and raises ParentHashRefuse, which leads to REFUSED_PARENT_HASH, exit 2, zero scenarios. Both attempts' `parent_source_pins_reverify.json` show PASS 33/33, waive=false. PASS.
  - Limit: same-length edits elsewhere cannot be excluded without the original bytes, so the sha stays INFERRED.
- **Both attempts carry the H4/H9 guard removal.**

## Bar (unchanged)
B2>B0 (all 4 stresses) · D>0 · B2 >= 0.95*D · inventory (unhedged_contract_hours) B2 <= 1.25x B0 · unresolved < 0.009 and all_flat · week rule (q3300_d0.25 week1 and week2, B2>B0). Source: `selection.py` `247a064d…`.

Reporting context only (not part of the bar): Refiner Addendum A, `packets/refiner/REFINER_EXTENSION_GAP_METRIC_FREEZE_Q7_ARM_B_ADDENDUM_A_2026-09-24.json`, sha256 `84989a3822a50a2257385e6970d7adabbcbbab919126592312b101a9d0076bb7` (verified). Criterion (a) reference: G_ref = mean of ref_s = min(gap_B0_s, gap_P1_s) = 0.0746; criterion (a) G_best(P2,P3) <= 0.0373. Values are quoted from the Addendum.

## HOLD clearance
The HOLD clears **only** when all three are true:
1. the walk has completed
2. the post-walk re-hash passes on every target
3. the Examiner files a CLEAR stamp citing this amendment

Until then P2 is not scored.

## PRE_COMPLETION_SNAPSHOT (not the scoring-time check)
Run at 2026-09-24T19:48:54-04:00 while the walk was running. Exit code 0. Group summary:
```
---
group runner: pass=1 fail=0
group manifest_49: pass=49 fail=0
group code_pin_guard_19: pass=19 fail=0
group conductor_packets_7: pass=7 fail=0
group conductor_packets_governance_mirror: pass=7 fail=0
group source_pins: pass=2 fail=0
group diffs: pass=2 fail=0
group hold_stamp: pass=1 fail=0
group reporting_context: pass=1 fail=0
group attempt1_provenance: pass=2 fail=0
group label_check: pass=1 fail=0
PRE_COMPLETION_SNAPSHOT: amendment=Q7B-P2-AMEND-1 targets=92 pass=92 fail=0 OVERALL=PASS
```
Walk status at the snapshot: pid 241785 running (Sl, elapsed 16:33). Progress: 4 of 12 scenarios DONE, 0 FAILED; the latest log line is a DONE for q3300_d5_B0 (P&L figures deliberately not reproduced). avail_mb=4093.
