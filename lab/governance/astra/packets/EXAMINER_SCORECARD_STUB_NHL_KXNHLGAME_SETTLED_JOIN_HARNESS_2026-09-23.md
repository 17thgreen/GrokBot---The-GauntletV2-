# Examiner scorecard STUB — NHL-RJ settled join — READY NOT_SCORED

**Seat:** Examiner (Kalshi)  
**Packet:** NHL-KXNHLGAME-SETTLED-RESOLUTION-JOIN-HARNESS (feature family **NHL-RJ**)  
**Lab:** `kalshi_kxnhlgame_settled_join_lab_20260923/`  
**PR44:** squash-merged **main@b450e780fd9752887579ee8d217b6dee76d918f8** (head `195ff53e…`, base `2fce8642…` R3P3-RJ)  
**ACCEPT:** `ce82d9347c8af6666d96fb5c63be7693f4672306639ce4ba2360ba231c01e698` (authentic; pulse PR43 wrong-ACCEPT closed superseded)  
**Units:** **10 OK** (`tests.test_orchestrator`) — code verify only; 10 units ≠ Examiner score  
**Status:** **READY** as scorecard stub · measurement **NOT_SCORED** · admit alone ≠ score

**Freeze:** sha256 `d1f71cea6df8f6c5a9fac6f9d1aa418ce61aa650794f22b400a01c4f3fd45810`  
**Scout reget:** sha256 `99a7f90564ee2150f5edef4efafb7ccb954b87036e0b43f29ff7dc6ed104706f`  
**Seed summary:** sha256 `794e148df5927c64d08b4578b47a7453589f02872af65880922bcb9273194a1a`  
**Panel stub:** sha256 `60d183e7bdcf25adbc94eeeb3bb361b5232c19c0fe3e6a115f45ab3fcb100c79` · `2026-09-23.c2-kxnhlgame-v0` · `admitted_at` **null**  
**Settled reget:** sha256 `8d597578bc65ea14ab1cbf5aa3c6d121d61431078a755b8419c815aa1d354df0` (desk lab + `lab/astra-capture/c2-kxnhlgame/settled_reget_2026-09-23.json` on main)  
**Box + main@b450e780 digest verification:** **PASS** for freeze/scout/seed/panel/settled/accept.

**Scout pin:** `settled_nonempty_result_N=17` — **NOT** copied into scorecard `settled_join_n` (stays null). Series/settled/open list 429 gaps honest. `admit.py` refused. Orthogonal to NHL-FQ. Not Cap-SR / C3-RJ / C5-RJ / R3P3-RJ / NHL-FQ reopen. Do not score Arm B here.

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| Pre-PR HOLD | **SUPERSEDED** by PR44 READY |
| Admit alone | **≠ score** |
| S1 / S2 / R2-P4 | **NOT ungated** |
| Arm B | **NOT scored here** |
| Live promotion / orders | **DENIED** |

**Desk headline:** PR44 stub READY — authentic ACCEPT pins verified; metrics null; settled_join_n not backfilled from scout N=17.

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
| `settled_join_n` | **null** (scout N=17 pin not copied) |
| `occurrence_match_n` | **null** |
| `admit_ready_flag` | **null** |

---

## ScorecardPromotionRefused if

1. Invented settled result / fills / depth / PnL.
2. Lee-Ready invented or used.
3. Cap-SR / FQ / NHL-FQ / C3-RJ / C5-RJ / R3P3-RJ reopen as this packet.
4. Q6-`000` retuned.
5. Claimed this ungates S1 / S2 / R2-P4.
6. Arm B scored or touched here.
7. Live orders / admit.py.
8. Backfilled series/settled/open 429 gaps or copied scout N=17 into `settled_join_n` as a score.
9. Treated 10 units or admit as Examiner score.

### Score gate

Clock admit + settled join N>0 (measured, not invented) + Examiner-ready.

**ACK:** `lab/governance/astra/packets/EXAMINER_ACK_NHL_RJ_PR44_STUB_READY_NOT_SCORED_2026-09-23.json`  
**Merge stamp:** `lab/governance/astra/packets/CONDUCTOR_MERGE_NHL_KXNHLGAME_SETTLED_JOIN_HARNESS_PR44_2026-09-23.json`  
**Stamped:** 2026-09-23T16:35:00-04:00
