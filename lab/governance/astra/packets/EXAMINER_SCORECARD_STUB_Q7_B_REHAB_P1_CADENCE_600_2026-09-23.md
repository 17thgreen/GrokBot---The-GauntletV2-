# Examiner scorecard STUB — Q7-B rehab Pass 1 cadence-600 — READY NOT_SCORED

**Seat:** Examiner (Kalshi)  
**Packet:** Q7-B-REHAB-P1-CADENCE-600 (feature family **Q7-B-REHAB-P1**)  
**Corpse:** `CEM-ASTRA-20260922-001` · Q7 Arm B KILL salvage Pass 1 of 3  
**Lab:** `nfl_q7_rehab_p1_cadence_20260923/`  
**PR38:** squash-merged **main@9b8fb184a8f1d556e400188127f1753bf35e571e** (head was `9cbb639afe9bfdec7114b4d93a3e7d10439e21a7`)  
**Units:** **10 OK** (`test_cadence`) — code verify only; 10 units ≠ Examiner score  
**Status:** **READY** as scorecard stub (units-only harness admit) · measurement **NOT_SCORED** · **not a scored promote**

**FROZEN_EXPERIMENT.json:** sha256 `3183754c6880b20ad16b51b4595549409a24508ece6e3b21d507d51142ce3174` · status `IMPLEMENTED_FROZEN_NOT_RUN` · `results`/`pnl` **null** · `score_run_in_this_freeze=false`  
**waive_parent_ledger_hash_check:** **false** (Conductor NO_WAIVE)  
**Parent ledgers in git:** **absent** (32 blobs ~247MB; SOURCE_PINS only) → **absence_is_not_a_pass** at SCORE time  
**SOURCE_PINS:** `packets/refiner/PARENT_Q7_BD_LEDGER_SOURCE_PINS_2026-09-23.json` sha256 `5ee602ba5d6537956c87eca0d5af5bf4443b80e935e85d1c7c61279f4fed432a` · desk primaries **MATCH** (`370ccbcf…` / `fc38cfbc…` / effects `5d87ea61…`) · all 32 artifact digests desk-verified  

**packets/refiner/* (5) desk+main MATCH:**  
- freeze `91506143…` · accept `6ff909e9…` · diagnosis `2f5beac5…` · decision `78c4cf44…` · SOURCE_PINS `5ee602ba5d653795…`

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement / rehab Pass 1 | **NOT_SCORED** |
| Pre-merge HOLD | **SUPERSEDED** by PR38 READY |
| Positive-control hash at SCORE | **BLOCKED** until authentic parent B/D ledgers present (no waive) |
| 12-scenario tape walk | **NOT RUN** |
| 95%-of-D bar | **unchanged** (no soften) |
| Scored promote / live orders | **DENIED** |

**Desk headline:** PR38 stub READY for units-only harness admit; SCORE gate still requires authentic parent ledgers PASS — SOURCE_PINS alone ≠ pass.

---

## Arms

| Arm | Role |
|---|---|
| **B0** | Q7 Arm B control (original + check, continuous) |
| **B1** | Rehab: B0 + **600s admission cadence only** |
| **D** | Q7 Arm D / Q6-`000` retention reference (`000` freeze not edited) |

Knob: `admission_cadence=600` only.

---

## Metrics (null on disk)

| Metric | Value |
|---|---|
| `results` | **null** |
| `pnl` | **null** |
| 12-scenario completed_strategy_pnl | **not run** |

---

## ScorecardPromotionRefused if

1. Invented fills / PnL / ledger hashes / tape walk.
2. Treated 10 units or merge as Examiner score / scored promote.
3. Waived parent ledger hash check or treated absence as pass.
4. Softened 95%-of-D after peek / outcome.
5. Q6-`000` edited or retuned.
6. Multi-knob beyond admission_cadence.
7. Live orders / live_promotion.
8. 12-scenario score before positive controls PASS.

### Score gate (still open)

1. Authentic parent Arm B/D ledger bytes present and hash-PASS vs SOURCE_PINS (no waive).  
2. 12-scenario artifacts with non-null results under frozen selection bar.  
3. Examiner-ready.

**ACK:** `lab/governance/astra/packets/EXAMINER_ACK_Q7_B_REHAB_P1_PR38_STUB_READY_NOT_SCORED_2026-09-23.json`  
**Prior HOLD:** `EXAMINER_HOLD_Q7_B_REHAB_P1_CADENCE_600_PRE_MERGE_2026-09-23.json` (**SUPERSEDED**)  
**Decision bind:** `packets/refiner/CONDUCTOR_DECISION_Q7_B_P1_PARENT_LEDGERS_2026-09-23.json`  
**Stamped:** 2026-09-23T15:14:30-04:00

---

**UPDATE 2026-09-23T17:32 ET:** Tape walk **SCORED KILL** — see `EXAMINER_SCORECARD_Q7_B_REHAB_P1_TAPE_WALK_KILL_2026-09-23.md` (frozen 95%-of-D bar; first fail `b1_vs_b0:q3300_d0.25`; `000` remains).
