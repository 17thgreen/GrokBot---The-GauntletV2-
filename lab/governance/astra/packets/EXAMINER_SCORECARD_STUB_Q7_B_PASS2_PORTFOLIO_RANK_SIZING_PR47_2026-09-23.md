# Examiner scorecard STUB — Q7-B rehab Pass 2 portfolio_rank_sizing PR47 — READY NOT_SCORED

**Seat:** Examiner (Kalshi)  
**Packet:** Q7-B-REHAB-P2-PORTFOLIO-RANK-SIZING (feature family **Q7-B-REHAB-P2**)  
**Corpse:** `CEM-ASTRA-20260922-001` · Q7 Arm B KILL salvage Pass 2 of 3  
**Lab:** `nfl_q7_rehab_p2_rank_sizing_20260923/`  
**PR47:** squash-merged **main@a281adc944e4dacffcdb5677a140fabaed675a81** (head was `10904fce31e368a314d332929fb5ebed8c49520f`; base `fec05e8cf7c11f1c975ab791fda64f896d40d1cd`)  
**Units:** **11 OK** (`test_rank_sizing` @ 2026-09-23T21:44:39Z) — code verify only; 11 units ≠ Examiner score  
**Status:** **READY** as units stub · measurement **NOT_SCORED** · **not a scored promote** · `promote=false`

**FROZEN_EXPERIMENT.json:** sha256 `e3e4814abcbb92b5142c1e4783fed53b50372783aeb58f664361966d719bd7d7` · status `IMPLEMENTED_FROZEN_NOT_RUN` · `results`/`pnl` **null** · `score_run_in_this_freeze=false`  
**waive_parent_ledger_hash_check:** **false**  
**SOURCE_PINS:** `packets/refiner/PARENT_Q7_BD_LEDGER_SOURCE_PINS_2026-09-23.json` sha256 `5ee602ba5d6537956c87eca0d5af5bf4443b80e935e85d1c7c61279f4fed432a`  
**Digest verify:** freeze `5f70d83a…` · diagnosis `a9539677…` · hand `8acc6811…` · accept `eb2e7e84…` · MATCH vs FROZEN_EXPERIMENT.conductor_packets

**Tape walk:** **NOT scored here** — in flight under Refiner GO (`REFINER_HAND_SIMULATOR_Q7_B_PASS2_TAPE_WALK_2026-09-23.json`) + Conductor ACK. This stub is **units merge only**. Do not invent or promote partial tape-walk PnL.

**Bar unchanged (Pass-2 arm B2):** B2>B0 every stress · B2 ≥ 95% of D · inventory B2 unhedged ≤ 1.25× B0 · else NO_NEW_SELECTION / fallback_shadow=`000` / `promote=false` — **do not soften**.

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Units / PR47 merge | **READY_NOT_SCORED** |
| Measurement / rehab Pass 2 | **NOT_SCORED** |
| Tape walk | **NOT_SCORED** (in flight; separate commission) |
| 95%-of-D / B2>B0 bar | **unchanged** (no soften) |
| Scored promote / live orders | **DENIED** |

**Desk headline:** PR47 units stub READY NOT_SCORED; results/pnl null; tape walk not scored here; bar unchanged.

---

## Arms

| Arm | Role |
|---|---|
| **B0** | Q7 Arm B control (original + check, continuous full-wanted) |
| **B2** | Rehab: B0 + **portfolio_rank_sizing only** (Pass-1 cadence not reopened) |
| **D** | Q7 Arm D / Q6-`000` retention reference (`000` freeze not edited) |

Knob: `portfolio_rank_sizing` only. Orthogonal to Pass-1 `admission_cadence` (KILL closed).

---

## Metrics (null on freeze / this stub)

| Metric | Value |
|---|---|
| `results` | **null** |
| `pnl` | **null** |
| 12-scenario completed_strategy_pnl | **not Examiner-scored here** |

---

## ScorecardPromotionRefused if

1. Invented fills / PnL / ledger hashes.
2. Treated 11 units or merge as Examiner score / scored promote.
3. Softened 95%-of-D or B2>B0 after peek / outcome.
4. Q6-`000` edited or retuned.
5. Reopened Pass-1 admission_cadence.
6. Live orders / live_promotion.
7. Scored tape walk inside this units-stub commission.
8. Waived parent ledger hash / treated absence as pass.

### Score gate (still open — separate commission)

1. Authentic parent Arm B/D ledger bytes present and hash-PASS vs SOURCE_PINS (no waive).  
2. 12-scenario tape-walk artifacts with non-null results under frozen selection bar.  
3. Examiner-ready handoff.

**ACK:** `lab/governance/astra/packets/EXAMINER_ACK_Q7_B_PASS2_PR47_UNITS_STUB_READY_NOT_SCORED_2026-09-23.json`  
**READY:** `lab/governance/astra/packets/EXAMINER_READY_Q7_B_PASS2_PORTFOLIO_RANK_SIZING_PR47_NOT_SCORED_2026-09-23.json`  
**Merge stamp:** `lab/governance/astra/packets/CONDUCTOR_MERGE_Q7_B_PASS2_PORTFOLIO_RANK_SIZING_PR47_2026-09-23.json`  
**Prior P1:** separate stub `EXAMINER_ACK_Q7_B_REHAB_P1_PR38_STUB_READY_NOT_SCORED` / P1 tape walk SCORED KILL — not this file.  
**Stamped:** 2026-09-23T17:52:00-04:00
