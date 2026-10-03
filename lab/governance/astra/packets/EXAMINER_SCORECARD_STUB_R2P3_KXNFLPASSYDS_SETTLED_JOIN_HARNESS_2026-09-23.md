# Examiner scorecard STUB — R2P3-RJ settled join — READY NOT_SCORED

**Seat:** Examiner (Kalshi)  
**Packet:** R2P3-KXNFLPASSYDS-SETTLED-RESOLUTION-JOIN-HARNESS (feature family **R2P3-RJ**)  
**Lab:** `kalshi_r2p3_kxnflpassyds_settled_join_lab_20260923/`  
**PR46:** squash-merged **main@b2c1639a77f62114572fd41182f8a3c5ef70cad1** (head `4131cc33…`, base `aeff380b…` S4-RJ)  
**ACCEPT:** `e5218cf2511607211ec1d825a9dad36abaee3d9cfda24488524c3d6bcbe3a565` (authentic; Variants sole implement; no Conductor pulse cloud)  
**Units:** **10 OK** (`tests.test_orchestrator`) — code verify only; 10 units ≠ Examiner score  
**Status:** **READY** as scorecard stub · measurement **NOT_SCORED** · admit alone ≠ score

**Freeze:** sha256 `9ad3b0112243c1020aec2bd6ef0df15011b065c30aa691a988da02eb08be1e0b`  
**Scout reget:** sha256 `2c3664ac240887026076a84e451ca798e0c2d10d42bdaf61a9a83844881681e5`  
**Seed summary:** sha256 `534a617bc3f18be501c07237d261e945b1bcf0301ac956cddae46e0431b75cd3`  
**Panel stub:** sha256 `70e879e8738d033f392d821849dee3537af3e7b8a916670779d238f78ce098be` · `2026-09-22.r2-p3-prop-slate-v0` · `admitted_at` **null**  
**Settled reget:** sha256 `2ce8426edb4ee5053f63bf2fe1439dbd046978eb76afa1e0537b17cca9b8b0e4` (desk lab + `lab/astra-capture/r2-p3-prop-slate/settled_reget_2026-09-23.json` on main)  
**Box + main@b2c1639a digest verification:** **PASS** for freeze/scout/seed/panel/settled/accept.

**Scout pin:** `settled_nonempty_result_N=20` — **NOT** copied into scorecard `settled_join_n` (stays null). Settled list HTTP 200; finalized/events closed|settled 429 gaps honest. `admit.py` refused. Orthogonal to R2-P3 prop-ladder / PASSYDS-PROP. Not Cap-SR / C3-RJ / C5-RJ / R3P3-RJ / NHL-RJ / S4-RJ / FQ reopen. Do not score Arm B here.

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| Pre-PR HOLD | **SUPERSEDED** by PR46 READY |
| Admit alone | **≠ score** |
| S1 / S2 / R2-P4 | **NOT ungated** |
| Arm B | **NOT scored here** |
| Live promotion / orders | **DENIED** |

**Desk headline:** PR46 stub READY — authentic ACCEPT pins verified; metrics null; settled_join_n not backfilled from scout N=20.

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
3. Cap-SR / FQ / R2-P3-prop-ladder / PASSYDS-PROP / C3-RJ / C5-RJ / R3P3-RJ / NHL-RJ / S4-RJ reopen as this packet.
4. Q6-`000` retuned.
5. Claimed this ungates S1 / S2 / R2-P4.
6. Arm B scored or touched here.
7. Live orders / admit.py.
8. Backfilled finalized/events 429 gaps or copied scout N=20 into `settled_join_n` as a score.
9. Treated 10 units or admit as Examiner score.
10. Conductor pulse cloud kick (Variants sole implement).

### Score gate

Clock admit + settled join N>0 (measured, not invented) + Examiner-ready.

**ACK:** `lab/governance/astra/packets/EXAMINER_ACK_R2P3_RJ_PR46_STUB_READY_NOT_SCORED_2026-09-23.json`  
**Merge stamp:** `lab/governance/astra/packets/CONDUCTOR_MERGE_R2P3_KXNFLPASSYDS_SETTLED_JOIN_HARNESS_PR46_2026-09-23.json`  
**Stamped:** 2026-09-23T17:29:00-04:00
