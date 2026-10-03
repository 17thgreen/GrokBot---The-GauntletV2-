# Examiner scorecard STUB — C3-RJ settled join — READY NOT_SCORED

**Seat:** Examiner (Kalshi)  
**Packet:** C3-KXHIGHNY-SETTLED-RESOLUTION-JOIN-HARNESS (feature family **C3-RJ**)  
**Lab:** `kalshi_c3_kxhighny_settled_join_lab_20260923/`  
**PR40:** squash-merged **main@9fd5d7cb89693a0ed29d9e97d2b723c0810989bc** (head `71136937…`, base `9b8fb184…`)  
**ACCEPT:** `9adb77ed01fd9ccb894564efa9d5534d2edf189365ca0852fff49dafd3598d69`  
**Units:** **10 OK** (`tests.test_orchestrator`) — code verify only; 10 units ≠ Examiner score  
**Status:** **READY** as scorecard stub · measurement **NOT_SCORED** · admit alone ≠ score

**Freeze:** sha256 `56adcf592239b028aaa8bcffbf09815115b8454f78db39b43c578e64c160a4d5`  
**Scout reget:** sha256 `e8950352745007d3cb565050161430807fa5de70d15321bb00bede6ca9ac18ee`  
**Seed summary:** sha256 `b32bbf3200649bcea4fb61a98a4869d5123060a57702a9327262cccbc8e1ca93`  
**Panel stub:** sha256 `2a5da7fe85ca1adc6b7c4dcf9e09ed5c6bb62be6b5c9b42731e36e31d1e8dfea` · `2026-09-22.c3-kxhighny-v0` · `admitted_at` **null**  
**Settled reget:** sha256 `0055faae508ba034eb49a12d52713566cbfe20bfbfbd2a16203ef350152ac24a` (desk `lab/astra-capture/c3-kxhighny/settled_reget_2026-09-23.json` + lab copy on main)  
**Box digest verification:** **PASS** for freeze/scout/seed/panel/settled/accept.

**Scout pin:** `settled_nonempty_result_N=4` — **NOT** copied into scorecard `settled_join_n` (stays null). CHI 429 gap honest.

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| Pre-PR HOLD | **SUPERSEDED** by PR40 READY |
| Admit alone | **≠ score** |
| S1 / S2 / R2-P4 | **NOT ungated** |
| Live promotion / orders | **DENIED** |

**Desk headline:** PR40 stub READY — authentic pins verified; metrics null; settled_join_n not backfilled from scout N=4.

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
| `settled_join_n` | **null** (scout N=4 pin not copied) |
| `occurrence_match_n` | **null** |
| `admit_ready_flag` | **null** |

---

## ScorecardPromotionRefused if

1. Invented settled result / fills / depth / PnL.
2. Lee-Ready invented or used.
3. Cap-SR / FQ (incl. ETH-FQ) / EMPTY-OB / C3 bordering reopened as this packet.
4. Q6-`000` retuned.
5. Claimed this ungates S1 / S2 / R2-P4.
6. Live orders / admit.py.
7. Backfilled CHI 429 gap or copied scout N=4 into `settled_join_n` as a score.
8. Treated 10 units or admit as Examiner score.

### Score gate

Clock admit + settled join N>0 (measured, not invented) + Examiner-ready.

**ACK:** `lab/governance/astra/packets/EXAMINER_ACK_C3_RJ_PR40_STUB_READY_NOT_SCORED_2026-09-23.json`  
**Merge stamp:** `lab/governance/astra/packets/CONDUCTOR_MERGE_C3_KXHIGHNY_SETTLED_JOIN_HARNESS_PR40_2026-09-23.json`  
**Stamped:** 2026-09-23T15:15:30-04:00
