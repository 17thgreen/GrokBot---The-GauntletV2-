# Examiner scorecard STUB — S5-RJ settled join — READY NOT_SCORED

**Seat:** Examiner (Kalshi)  
**Packet:** S5-KXMVECROSSCATEGORY-SETTLED-RESOLUTION-JOIN-HARNESS (feature family **S5-RJ**)  
**Lab:** `kalshi_s5_kxmvecrosscategory_settled_join_lab_20260923/`  
**PR48:** squash-merged **main@fec05e8cf7c11f1c975ab791fda64f896d40d1cd** (head `4b20bdf6…`, base `b2c1639a…` R2P3-RJ)  
**ACCEPT:** `495675175589c08122bc57375dd8e7d00aea9f4a154df3aff086b015a2513a8c` (authentic; Variants sole implement; no Conductor pulse cloud)  
**Units:** **10 OK** (`tests.test_orchestrator`) — code verify only; 10 units ≠ Examiner score  
**Status:** **READY** as scorecard stub · measurement **NOT_SCORED** · admit alone ≠ score · promote=false

**Freeze:** sha256 `cd264a4d41ef055d1cbca80a5dbe6756746211537fb24799dca9dde8980cb799`  
**Scout reget:** sha256 `33db60a50f2e7746315f4603b9f78a9260145cb49d0250e141471de46f4df9e3`  
**Seed summary:** sha256 `3bc4aa5f44d7d31295dfd25f7bac3a3e39463c237315e8228c3fcf434d08419a`  
**Panel stub:** sha256 `4918b820d454c5f997ea100917859f7e9467d92933bed1bc8a55c81ab8ce5b8e` · `2026-09-22.s5-kxmvecrosscategory-v0` · `admitted_at` **null**  
**Settled reget:** sha256 `91111f20586a1b684e430baa0e8b62a3fffc7d510de99e43bab7d213dfeb26da` (desk lab + `lab/astra-capture/s5-kxmvecrosscategory/settled_reget_2026-09-23.json` on main)  
**Box + main@fec05e8c digest verification:** **PASS** for freeze/scout/seed/panel/settled/accept.

**Scout pin:** `settled_nonempty_result_N=20` — **NOT** copied into scorecard `settled_join_n` (stays null). Settled list HTTP 200; earlier settled/finalized/events list 429 gaps honest. `occurrence_datetime` null on settled lim20 honest — J1 uses `expected_expiration_time`. `admit.py` refused. Orthogonal to S5 FILLLEGS / MVE-FL. Not Cap-SR / C3-RJ / C5-RJ / R3P3-RJ / NHL-RJ / S4-RJ / R2P3-RJ / FQ reopen. Do not score Arm B here.

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| Pre-PR HOLD | **SUPERSEDED** by PR48 READY |
| Pin ACK CD264A4D | **SUPERSEDED** (merge gate cleared) |
| Admit alone | **≠ score** |
| S1 / S2 / R2-P4 | **NOT ungated** |
| Arm B | **NOT scored here** |
| Live promotion / orders | **DENIED** |

**Desk headline:** PR48 stub READY — authentic ACCEPT pins verified; metrics null; settled_join_n not backfilled from scout N=20.

---

## Arms

| Arm | Gate |
|---|---|
| **J0** | `nonempty_result_required` |
| **J1** | `occurrence_datetime_match` (`expected_expiration_time` when `occurrence_datetime` null honest) |

Knob: `join_gate`. Measurement only; not a fee arm. Orthogonal to S5 FILLLEGS / MVE-FL.

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
3. Cap-SR / FQ / S5-FILLLEGS / MVE-FL / C3-RJ / C5-RJ / R3P3-RJ / NHL-RJ / S4-RJ / R2P3-RJ reopen as this packet.
4. Q6-`000` retuned.
5. Claimed this ungates S1 / S2 / R2-P4.
6. Arm B scored or touched here.
7. Live orders / admit.py.
8. Backfilled earlier list 429 gaps or copied scout N=20 into `settled_join_n` as a score.
9. Invented `occurrence_datetime` when API null.
10. Treated 10 units or admit as Examiner score.
11. Conductor pulse cloud kick (Variants sole implement).

### Score gate

Clock admit + settled join N>0 (measured, not invented) + Examiner-ready.

**ACK:** `lab/governance/astra/packets/EXAMINER_ACK_S5_RJ_PR48_STUB_READY_NOT_SCORED_2026-09-23.json`  
**READY packet:** `lab/governance/astra/packets/EXAMINER_READY_S5_KXMVECROSSCATEGORY_SETTLED_JOIN_HARNESS_PR48_NOT_SCORED_2026-09-23.json`  
**Merge stamp:** `lab/governance/astra/packets/CONDUCTOR_MERGE_S5_KXMVECROSSCATEGORY_SETTLED_JOIN_HARNESS_PR48_2026-09-23.json`  
**Stamped:** 2026-09-23T17:51:30-04:00
