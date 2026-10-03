# Examiner scorecard STUB — R3P3-RJ settled join — READY NOT_SCORED

**Seat:** Examiner (Kalshi)  
**Packet:** R3P3-FL-MAKER-TAKER-SETTLED-RESOLUTION-JOIN-HARNESS (feature family **R3P3-RJ**)  
**Lab:** `kalshi_r3p3_fl_settled_join_lab_20260923/`  
**PR42:** squash-merged **main@2fce8642d1b1961cbe0ef60fae1411cd8906f31a** (head `c7510302…`, base `8cfcd17a…` C5-RJ)  
**ACCEPT:** `a6434fe4854b850df24a0a081168ba5d90d4646ba9a409418d7b874262a5fa9c`  
**Units:** **10 OK** (`tests.test_orchestrator`) — code verify only; 10 units ≠ Examiner score  
**Status:** **READY** as scorecard stub · measurement **NOT_SCORED** · admit alone ≠ score

**Freeze:** sha256 `7fcfc36ab4761e2dec56018b498372fb63c402f2582fe848e8775e28f9b720b9`  
**Scout reget:** sha256 `f675d7c40ccad37173b2cb54837349cd3053b7b76606c43efba5759a1bde551f`  
**Seed summary:** sha256 `b43d4ab065b712f5bf1b87eb164bccb00e8e9993f97db9d86a8d1619ce9ec13d`  
**Panel stub:** sha256 `6f640dd3a6091ba6b896ded38fdded4676583aa3c885223da21ddf03780250c0` · `2026-09-22.r3-p3-fl-maker-taker-v0` · `admitted_at` **null**  
**Settled reget:** sha256 `c5f680e4ff66af67691672c4b8c43eb57906f25b4d79fdeb65f61e031c13efda` (desk `lab/astra-capture/r3-p3-fl-maker-taker/settled_reget_2026-09-23.json` + lab copy on main)  
**Box + main@2fce8642 digest verification:** **PASS** for freeze/scout/seed/panel/settled/accept.

**Scout pin:** `settled_nonempty_result_N=20` — **NOT** copied into scorecard `settled_join_n` (stays null). CHI settled + NY open 429 gaps honest. `admit.py` refused. Not R3-P3 fee / FQ / C3-RJ / C5-RJ reopen. Do not score Arm B here.

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| Pre-PR HOLD | **SUPERSEDED** by PR42 READY |
| Admit alone | **≠ score** |
| S1 / S2 / R2-P4 | **NOT ungated** |
| Arm B | **NOT scored here** |
| Live promotion / orders | **DENIED** |

**Desk headline:** PR42 stub READY — authentic pins verified; metrics null; settled_join_n not backfilled from scout N=20.

---

## Arms

| Arm | Gate |
|---|---|
| **J0** | `nonempty_result_required` |
| **J1** | `occurrence_datetime_match` |

Knob: `join_gate`. Measurement only; not a fee arm.

---

## Metrics (null on disk)

| Metric | Value |
|---|---|
| `results` | **null** |
| `pnl` | **null** |
| `settled_join_n` | **null** (scout N=20 pin not copied) |
| `occurrence_match_n` | **null** |
| `admit_ready_flag` | **null** |

---

## ScorecardPromotionRefused if

1. Invented settled result / fills / depth / PnL.
2. Lee-Ready invented or used.
3. Cap-SR / FQ / C3-RJ / C5-RJ / R3-P3 fee reopen as this packet.
4. Q6-`000` retuned.
5. Claimed this ungates S1 / S2 / R2-P4.
6. Arm B scored or touched here.
7. Live orders / admit.py.
8. Backfilled CHI settled / NY open 429 gaps or copied scout N=20 into `settled_join_n` as a score.
9. Treated 10 units or admit as Examiner score.

### Score gate

Clock admit + settled join N>0 (measured, not invented) + Examiner-ready.

**ACK:** `lab/governance/astra/packets/EXAMINER_ACK_R3P3_RJ_PR42_STUB_READY_NOT_SCORED_2026-09-23.json`  
**Merge stamp:** `lab/governance/astra/packets/CONDUCTOR_MERGE_R3P3_FL_SETTLED_JOIN_HARNESS_PR42_2026-09-23.json`  
**Stamped:** 2026-09-23T15:58:00-04:00
