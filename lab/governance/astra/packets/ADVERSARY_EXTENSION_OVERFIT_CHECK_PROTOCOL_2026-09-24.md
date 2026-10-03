# Adversary overfit-check protocol — Refiner extension passes & warm shelf — 2026-09-24 (ET)

**Seat:** The Adversary "KALSHI" · **Authority:** Logan's rehab rule as relayed by the Conductor (`packets/refiner/REHAB_POLICY_EXTENSION_AMENDMENT_2026-09-24.md`) · **Stamped:** 2026-09-24T19:50:00-04:00  
**Role:** A CHECK on each extension pass (4, 5) and each warm-shelf parking. It is not a vote. Output is **CLEAN**, or **FLAG + reason**, advisory to Refiner and Conductor. The one exception is **pass > 5**, where Adversary sign-off is required: a real vote, alongside Conductor's. Never re-scores; Examiner remains of record.

## Checklist (run on every pass 4, pass 5, and every SHELVE)

| # | Check | How (concrete, checkable) | FLAG if |
|---|---|---|---|
| 1 | Gap arithmetic recomputed | Recompute `target_s`, `gap_s` and `G` from **Examiner-scored** `completed_strategy_pnl` only (Examiner scorecard/ACK per pass), using the formula frozen in the corpse's gap-metric freeze. Ignore Refiner summaries and Simulator previews. Report closure vs the aggregate baseline **and** vs the per-stress baseline `mean(ref_s)`. | Any recomputed G differs from Refiner's by more than rounding. (a) holds only under one baseline definition. Any input is a Simulator preview. |
| 2 | (a) ≥ half closed, P1→P3 | `G_best(P2,P3) ≤ 0.5 × G_ref` on the recomputed numbers. | Fails, or the baseline was redefined after P1. |
| 3 | (b) leave-one-out | Using Examiner's per-game/per-event table: drop each game/event in turn and recompute the arm−B0 delta and `G` on every stress. Also check that `gap_s ≤ ref_s` on ≥ 3 of 4 stresses, and that no single stress supplies > 50% of the closure. | Any single drop flips the sign or undoes > 50% of the gain. Top-1 game share > 50%. No per-game table exists (a missing table is itself a FLAG, not a pass). |
| 4 | Stress set unchanged | sha256 of the stress list and scenario grid equals the pass-1 frozen set (same 4 stresses, same queue/delay values). | Hash differs, or a stress was added, dropped or renamed. |
| 5 | Bar unchanged | sha256 of `selection.py` equals the pass-1 value, and the bar text still reads "arm > B0 AND arm ≥ 0.95×D on every stress; weeks + inventory gates". | Any change in threshold, gate order or tolerance. The 95%-of-D bar and B>B0 must stand. |
| 6 | Holdout untouched | No reads, loads or hash-joins of the holdout/prospective panel (e.g. PIT@CLE holdout; ADMIT-1 prospective DB). Check run logs, file access traces and code imports. Check the reused 31-game development cohort label is unchanged. | Any access, or ambiguity that can't be ruled out from logs. |
| 7 | Knob pre-declared and orthogonal | The freeze file for the knob is on disk with a stamp **earlier than** the first result file of that pass (compare mtime and in-file stamp). The knob is not a re-parameterization of a prior knob: no new value or range of `admission_cadence` or `portfolio_rank_sizing`, and no combination of them. | Stamp is later than results. The knob touches a prior knob's code path or parameter. More than one knob. |
| 8 | Full variant count | The count of every attempt logged in the pass ledger variant log includes failed, aborted and infra-rerun attempts (e.g. `results_attempt*` dirs), each with its freeze pointer and outcome. Report N_variants tried vs passes counted (garden-of-forking-paths count). | Any on-disk attempt dir or run log is not in the ledger. Any variant has no Examiner or explicit NOT_RUN status. |
| 9 | 10%-of-remaining-gap exit | `(G_best_before − G_k) / G_best_before`, computed from check #1 numbers. If < 0.10, the pass must route to CEMETERY or SHELVE; no "one more try". | Rule not applied, or applied to a different baseline. |
| 10 | Warm-shelf entry hygiene | The SHELVE file records revival conditions: which new data class (prospective/live/queue), the minimum N, and who can revive it. It also carries the frozen bar/stress hashes and the pass-by-pass G. It states "not promotion evidence". | Missing revival conditions. The shelf is cited as evidence for promotion or bakeoff. The shelf is revived on the same development data. |
| 11 | Pass > 5 | Needs Conductor + Adversary sign-off **before** the pass-6 freeze exists. Adversary signs only if #1–#10 are CLEAN on passes 4–5 and a new evidence class is named. | Any pass-6 artifact exists without both stamps. **This is the only blocking item.** |

**Always carried:** code files that run the tape walk but are not pinned in `FROZEN_EXPERIMENT.implementation_sha256` get their diff checked (infra-only or not). Promotion still requires untouched prospective data. An improvement is never a pass. No live orders.

## Output format (one line per check)
`ADVERSARY_OVERFIT_CHECK <corpse_id> pass=<k> #1..#11: CLEAN|FLAG(<reason>) · overall CLEAN|FLAG · advisory (vote only if pass>5)`

## First live application — Q7 Arm B (`CEM-ASTRA-20260922-001`) — status on disk at 19:45 ET

| Item | Status / path |
|---|---|
| Pass 1 | **KILL** stamped: `packets/EXAMINER_SCORECARD_Q7_B_REHAB_P1_TAPE_WALK_KILL_2026-09-23.md` (2026-09-23 17:32 ET). First fail `b1_vs_b0:q3300_d0.25`. The 95%-of-D bar and B1>B0 stand. |
| Pass 2 | **In flight.** Freeze `packets/REFINER_PASS2_FREEZE_Q7_B_PORTFOLIO_RANK_SIZING_2026-09-23.md`; PR47 units stub READY_NOT_SCORED. Tape-walk rerun running: `astra-science/nfl_q7_rehab_p2_rank_sizing_20260923/results/experiment_summary.json` shows `status: RUNNING`, 1 of 12 scenarios done at 19:33 ET (the B0 control only). Not scored; no B2 number exists. |
| Pass 3 / extensions | Not started. Extension checks apply **only after pass 3**, so none are due yet. |
| Gap metric | `packets/refiner/REFINER_EXTENSION_GAP_METRIC_FREEZE_Q7_ARM_B_2026-09-24.json` (19:31:51 ET, before P2 outcomes). Ledger: `packets/refiner/REFINER_PASS_LEDGER_Q7_ARM_B.md`. |
| Pre-flags (advisory, for Refiner/Conductor) | **(i)** `G_ref`=0.2493 (= G_P1 = min(G_B0 0.2543, G_P1)), but `mean(ref_s)` = 0.0746. The per-stress "better of B0 and P1" baseline stated in the amendment is not the one criterion (a) uses. Declare which one governs before P2 is scored. My recompute of G_B0 and G_P1 matches the file. **(ii)** `run_tape_walk.py` (sha256 `a06a105f…`, mtime 2026-09-24 19:31:52 ET) is not in the P2 `implementation_sha256` pins and changed after attempt 1. `selection.py` and `rank_sizing_policy.py` hashes do match the freeze. Examiner should confirm the diff is infra-only. **(iii)** `results_attempt1_brokenpool_20260923/` (BrokenProcessPool, 5/12 done, no B2, NOT_RUN) is not in the ledger variant log. Log it as an infra attempt for (d). **(iv)** The ledger sha in `packets/refiner/REFINER_BOX_PACKET_SHA256_2026-09-23.md` is stale (ledger was amended 19:31). Archivist should re-pin. |
