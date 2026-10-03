# Examiner scorecard STUB — C1-RJ KXUFCFIGHT settled join — READY NOT_SCORED

**Seat:** Examiner (Kalshi) · Astra desk  
**Packet:** C1-KXUFCFIGHT-SETTLED-RESOLUTION-JOIN-HARNESS (feature family **C1-RJ**)  
**Lab:** `kalshi_c1_kxufcfight_settled_join_lab_20260923/`  
**PR49:** squash-merged **main@34a2720218b4f4f2d6dd0cbde6334ee672a3684b** (head `7a10497b56718301d823fe2838c573df28b11fd6`, base `a281adc944e4dacffcdb5677a140fabaed675a81`), merged 2026-09-24 19:20:39 ET  
**ACCEPT:** `5c3d559a055482301340102246835c7657c6b5ba9b1ceb69022dbd04c9895ac3` (authentic; Variants implement bc-986a32c2; Conductor pin fixup bc-aa3db543 same branch)  
**Units:** **10 OK** (`tests.test_orchestrator`; Examiner re-ran at main@34a27202 → Ran 10, OK) — code verify only; 10 units ≠ Examiner score  
**Status:** **READY** as scorecard stub · measurement **NOT_SCORED** · admit alone ≠ score · promote=false

## Pins (8/8 PASS)

| Pin | Path | sha256 | Box | head@7a10497b | main@34a27202 |
|---|---|---|---|---|---|
| freeze | `lab/governance/astra/packets/C1_KXUFCFIGHT_SETTLED_RESOLUTION_JOIN_HARNESS_FREEZE_2026-09-23.md` | `3ea3362ad3c16951369d5f90497ec6079213dd54e5556340c4d3738744126cf1` | PASS | PASS | PASS |
| accept | `lab/governance/astra/packets/CONDUCTOR_ACCEPT_C1_KXUFCFIGHT_SETTLED_JOIN_HARNESS_2026-09-24.json` | `5c3d559a055482301340102246835c7657c6b5ba9b1ceb69022dbd04c9895ac3` | PASS | PASS | PASS |
| maximize_pin | `lab/governance/astra/packets/MAXIMIZE_PIN_2026-09-23_1750ET.md` | `6fad9acbff410b36432c7f20f6d19adce37ee9703b9e42a7b0ba9e059f3990df` | PASS | PASS | PASS |
| scout_reget | `lab/governance/astra/packets/scout_c1_settled_rejoin_2026-09-23/scout_settled_rejoin_C1_KXUFCFIGHT.json` | `1175029927603a957a2ae2b1fcf1b59bb244118c1e090e53bf8278f4614a686f` | PASS | PASS | PASS |
| seed_summary | `lab/governance/astra/packets/scout_c1_settled_rejoin_2026-09-23/SEED_SETTLED_SUMMARY.json` | `b3e62f5902e5cf536d2635fdaee4613093ce0f397c26b3186b25d9c6eb742600` | PASS | PASS | PASS |
| panel_stub | `lab/governance/astra/packets/scout_c1_settled_rejoin_2026-09-23/C1_KXUFCFIGHT_PANEL_STUB_2026-09-22.json` | `24426d804c51bde23cf2557a11a8481a12026da10024094c4ae546d1f7d3956e` | PASS | PASS | PASS |
| settled_reget | `lab/governance/astra/packets/scout_c1_settled_rejoin_2026-09-23/settled_reget_2026-09-23.json` | `77457212b2427b9ef29499a6619cabf0b43955a569419acbb1abd468e2e79a23` | PASS | PASS | PASS |
| examiner_hold | `lab/governance/astra/packets/EXAMINER_HOLD_C1_KXUFCFIGHT_SETTLED_JOIN_HARNESS_PRE_PR_2026-09-23.json` | `7ceb4bedf6a3e132ae410992851eb977e6cbdf85a337949d223be4bdb5de8a0b` | PASS | PASS | PASS |

**SOURCE_PINS copies (repo):** 4/4 git blob `cc2392d8f3632caa35836a96ee1f7762a0928a33` (sha256 `785c9eb84fb2d97baf14242dd18b2340448fe4e4280186f86d585e2b636b0f2e`) at head and main; `digest_all_match_claimed=true`. Box desk SOURCE_PINS copies are the pre-PR desk declaration (blob `d339e3f8…`), same digests — not a mismatch.

**Scout pin:** `settled_nonempty_result_N=4` — pin only, **NOT** copied into scorecard `settled_join_n` (stays null). Settled/finalized/events list HTTP 429 honest; not backfilled. J1 uses `occurrence_datetime` (present on all 4 parent seeds); no `expected_expiration_time` substitution. `admit.py` refused. Orthogonal to C1-EMPTY-OB / C1-MEAS / C1-ADMIT-WIRE.

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| Pre-PR HOLD `EXAMINER_HOLD_C1_KXUFCFIGHT_SETTLED_JOIN_HARNESS_PRE_PR` (sha256 `7ceb4bed…`) | **SUPERSEDED** by PR49 READY |
| Admit alone | **≠ score** |
| 10 units | **≠ score** |
| S1 / S2 / R2-P4 | **NOT ungated** |
| Arm B | **NOT scored here** |
| Live promotion / orders | **DENIED** |

**Desk headline:** PR49 stub READY — authentic ACCEPT 8/8 pins verified (box + head + main); metrics null; settled_join_n not backfilled from scout N=4.

---

## Arms

| Arm | Gate |
|---|---|
| **J0** | `nonempty_result_required` |
| **J1** | `occurrence_datetime_match` |

Knob: `join_gate`. Measurement only; not a fee arm.

---

## Metrics (null on disk — box and main@34a27202)

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
2. Empty-books invent (C1 PR19) / invented books / padded settled list past authentic parent-seed N=4.
3. Lee-Ready invented or used.
4. Q6-`000` retuned.
5. Live orders / admit.py.
6. Copied scout N=4 into `settled_join_n` as a score, or backfilled 429 list gaps.
7. Treated 10 units or admit as Examiner score.
8. Invented `occurrence_datetime` or substituted `expected_expiration_time`.
9. Cap-SR / FQ / C1-EMPTY-OB / C3-RJ / C5-RJ / R3P3-RJ / NHL-RJ / S4-RJ / R2P3-RJ / S5-RJ reopen as this packet.
10. Claimed this ungates S1 / S2 / R2-P4; Arm B scored or touched here.
11. Conductor pulse cloud kick.

### Score gate

Clock admit + measured settled_join_n>0 (not invented, not scout N) + Examiner-ready.

### Non-blocking doc nit

`UNIT_RESULTS.md` on main still carries pre-fixup wording ("Examiner status stays HOLD_PRE_PR"; "refuses to claim ALL_MATCH until a follow-up wires those bytes"). Superseded by `PIN_GAP.json` (`gap_resolved_at_head` 73e08514) and SOURCE_PINS `digest_all_match_claimed=true`. Not a pin failure.

**ACK:** `lab/governance/astra/packets/EXAMINER_ACK_C1_RJ_PR49_STUB_READY_NOT_SCORED_2026-09-24.json`  
**READY packet:** `lab/governance/astra/packets/EXAMINER_READY_C1_KXUFCFIGHT_SETTLED_JOIN_HARNESS_PR49_NOT_SCORED_2026-09-24.json`  
**Merge stamp:** `lab/governance/astra/packets/CONDUCTOR_MERGE_C1_KXUFCFIGHT_SETTLED_JOIN_HARNESS_PR49_2026-09-24.json` (sha256 `a726436b53826c30cb0686d9a5d0e7802e039d4dcce2cd32999a1925d196273f`)  
**Stamped:** 2026-09-24T19:22:36-04:00
