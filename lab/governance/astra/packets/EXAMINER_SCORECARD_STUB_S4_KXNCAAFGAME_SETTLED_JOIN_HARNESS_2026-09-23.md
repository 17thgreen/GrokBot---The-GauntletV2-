# Examiner scorecard STUB — S4-RJ settled join — READY NOT_SCORED

**Seat:** Examiner (Kalshi)  
**Packet:** S4-KXNCAAFGAME-SETTLED-RESOLUTION-JOIN-HARNESS (feature family **S4-RJ**)  
**Lab:** `kalshi_kxncaafgame_settled_join_lab_20260923/`  
**PR45:** squash-merged **main@aeff380b29dbe89b16da58f9e15e58415b42b147** (head `310d4377…`, base `b450e780…` NHL-RJ)  
**ACCEPT:** `87bb8d44e8ac50099cc66d0469dcd4a5cfafb78d92dd24e7a218100a6254da4a` (authentic; Variants sole implement; no Conductor pulse cloud)  
**Units:** **10 OK** (`tests.test_orchestrator`) — code verify only; 10 units ≠ Examiner score  
**Status:** **READY** as scorecard stub · measurement **NOT_SCORED** · admit alone ≠ score

**Freeze:** sha256 `3a8e8ba52edd6acdc342c6a2faabb08665fe8a7a76e1b28af1c8e18850b03d99`  
**Scout reget:** sha256 `57fa0b28325ac13015f49521a87661b3cc064d22a13cf960f4fcdfd9badaa3dc`  
**Seed summary:** sha256 `9e67cd16f3ec6536d5dae3fe07de6e6b073c1c8d1adc9bb7e9297090ef567ce1`  
**Panel stub:** sha256 `38167d11da5842bc4d39e6e7dcaab20a67294c735ba14d8bbeafde3154c6342a` · `2026-09-22.s4-kxncaafgame-v0` · `admitted_at` **null**  
**Settled reget:** sha256 `5bb0acfaa429e2ec1ad22e2e35e296540ac5b8e66eba4df6a0b2419d43257528` (desk lab + `lab/astra-capture/s4-kxncaafgame/settled_reget_2026-09-23.json` on main)  
**Box + main@aeff380b digest verification:** **PASS** for freeze/scout/seed/panel/settled/accept.

**Scout pin:** `settled_nonempty_result_N=18` — **NOT** copied into scorecard `settled_join_n` (stays null). Series/settled/open list 429 gaps honest. `admit.py` refused. Orthogonal to S4-FQ / NCAAF-FQ. Not Cap-SR / C3-RJ / C5-RJ / R3P3-RJ / NHL-RJ / FQ reopen. Do not score Arm B here.

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| Pre-PR HOLD | **SUPERSEDED** by PR45 READY |
| Admit alone | **≠ score** |
| S1 / S2 / R2-P4 | **NOT ungated** |
| Arm B | **NOT scored here** |
| Live promotion / orders | **DENIED** |

**Desk headline:** PR45 stub READY — authentic ACCEPT pins verified; metrics null; settled_join_n not backfilled from scout N=18.

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
| `settled_join_n` | **null** (scout N=18 pin not copied) |
| `occurrence_match_n` | **null** |
| `admit_ready_flag` | **null** |

---

## ScorecardPromotionRefused if

1. Invented settled result / fills / depth / PnL.
2. Lee-Ready invented or used.
3. Cap-SR / FQ / S4-FQ / NCAAF-FQ / C3-RJ / C5-RJ / R3P3-RJ / NHL-RJ reopen as this packet.
4. Q6-`000` retuned.
5. Claimed this ungates S1 / S2 / R2-P4.
6. Arm B scored or touched here.
7. Live orders / admit.py.
8. Backfilled series/settled/open 429 gaps or copied scout N=18 into `settled_join_n` as a score.
9. Treated 10 units or admit as Examiner score.
10. Conductor pulse cloud kick (Variants sole implement).

### Score gate

Clock admit + settled join N>0 (measured, not invented) + Examiner-ready.

**ACK:** `lab/governance/astra/packets/EXAMINER_ACK_S4_RJ_PR45_STUB_READY_NOT_SCORED_2026-09-23.json`  
**Merge stamp:** `lab/governance/astra/packets/CONDUCTOR_MERGE_S4_KXNCAAFGAME_SETTLED_JOIN_HARNESS_PR45_2026-09-23.json`  
**Stamped:** 2026-09-23T16:57:00-04:00
