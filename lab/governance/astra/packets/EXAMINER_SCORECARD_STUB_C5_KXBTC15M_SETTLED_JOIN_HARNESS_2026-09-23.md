# Examiner scorecard STUB — C5-RJ settled join — READY NOT_SCORED

**Seat:** Examiner (Kalshi)  
**Packet:** C5-KXBTC15M-SETTLED-RESOLUTION-JOIN-HARNESS (feature family **C5-RJ**)  
**Lab:** `kalshi_c5_kxbtc15m_settled_join_lab_20260923/`  
**PR41:** squash-merged **main@8cfcd17a62d3793dee554a4da422e8075bde9cf6** (head `b2c31fc5…`, base `9eba1587…`)  
**ACCEPT:** `e116bbcb5f9518e6008ef412c8ff212a3170d0e3f26eb978f07a204b327aba7d`  
**Units:** **10 OK** (`tests.test_orchestrator`) — code verify only; 10 units ≠ Examiner score  
**Status:** **READY** as scorecard stub · measurement **NOT_SCORED** · admit alone ≠ score

**Freeze:** sha256 `7f4b36eca39d43ee7403628c2e525d5980fa40bcfc906550c7f00bb06ffd4f21`  
**Scout reget:** sha256 `7be17c44aef31abf7a0ab94938d0289f8766670ddacefdec566735818e044796`  
**Seed summary:** sha256 `b39c919809f709bcb81ff10a3d983b266bc7a1303c0de502c7c20be726415198`  
**Panel stub:** sha256 `60f613e8d775b66b9044ad31d2faf77bba84176f214a7bce599aa7a65b6905f8` · `2026-09-22.c5-kxbtc15m-v0` · `admitted_at` **null**  
**Settled reget:** sha256 `319d6d3e394089fd21fefbfaa52c58166e78c2d781077a3f876331d2c54de617` (desk `lab/astra-capture/c5-kxbtc15m/settled_reget_2026-09-23.json` + lab copy on main)  
**Box + main@8cfcd17a digest verification:** **PASS** for freeze/scout/seed/panel/settled/accept.

**Scout pin:** `settled_nonempty_result_N=20` — **NOT** copied into scorecard `settled_join_n` (stays null). Finalized/closed list 429 gaps honest. `admit.py` refused.

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| Pre-PR HOLD | **SUPERSEDED** by PR41 READY |
| Admit alone | **≠ score** |
| S1 / S2 / R2-P4 | **NOT ungated** |
| Live promotion / orders | **DENIED** |

**Desk headline:** PR41 stub READY — authentic pins verified; metrics null; settled_join_n not backfilled from scout N=20.

---

## Arms

| Arm | Gate |
|---|---|
| **J0** | `nonempty_result_required` |
| **J1** | `occurrence_datetime_match` |

Knob: `join_gate`. Measurement only; not a fee arm; not C5 honesty reopen.

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
3. Cap-SR / FQ / C5-honesty / C3-RJ reopened as this packet.
4. Q6-`000` retuned.
5. Claimed this ungates S1 / S2 / R2-P4.
6. Arm B touched.
7. Live orders / admit.py.
8. Backfilled finalized/closed 429 gaps or copied scout N=20 into `settled_join_n` as a score.
9. Treated 10 units or admit as Examiner score.

### Score gate

Clock admit + settled join N>0 (measured, not invented) + Examiner-ready.

**ACK:** `lab/governance/astra/packets/EXAMINER_ACK_C5_RJ_PR41_STUB_READY_NOT_SCORED_2026-09-23.json`  
**Merge stamp:** `lab/governance/astra/packets/CONDUCTOR_MERGE_C5_KXBTC15M_SETTLED_JOIN_HARNESS_PR41_2026-09-23.json`  
**Stamped:** 2026-09-23T15:35:00-04:00
