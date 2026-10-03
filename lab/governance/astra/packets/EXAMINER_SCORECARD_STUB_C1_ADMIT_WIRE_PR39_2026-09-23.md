# Examiner scorecard STUB — C1 admit-wire — READY NOT_SCORED

**Seat:** Examiner (Kalshi)  
**Packet:** C1-KXUFCFIGHT-ADMIT-WIRE (feature family **C1-ADMIT-WIRE**)  
**Lab:** `kalshi_c1_kxufcfight_lab_20260922/`  
**PR39:** squash-merged **main@3972fe4edfd53740219a4d051392f1291cef5f98** (head `24a25479…`, base `82bf7bb9…`)  
**Admit pin:** sha256 `24426d804c51bde23cf2557a11a8481a12026da10024094c4ae546d1f7d3956e` · panel `2026-09-22.c1-kxufcfight-v0` · `admitted_at` `2026-09-23T00:49:43Z` · `PANEL_ADMITTED_C1_UFC_ONLY`  
**Units:** **16 OK** (`tests.test_bakeoff`) — code verify only; 16 units ≠ Examiner score  
**Status:** **READY** as scorecard stub · measurement **NOT_SCORED** · **not a scored promote**

**Fixture verify:** `fixtures/panel_admitted.json` and `lab/astra-capture/c1-kxufcfight/panel_admitted.json` on main@3972fe4edfd5… **MATCH** admit pin (identical to desk `C1_KXUFCFIGHT_PANEL_ADMITTED_2026-09-22.json`).  
**Scorecard state:** `pnl` **null** · settled N **0** (labels joined from panel `result_observed_live_get` are not profit; resolutions capture dir absent — not invented).

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| Admit-wire fixtures | **MATCH** pin `24426d80…` |
| Scored promote | **DENIED** |
| S1 / S2 / R2-P4 | **NOT ungated** |
| Live promotion / orders | **DENIED** |

**Desk headline:** PR39 stub READY — admit fixtures match desk pin; pnl null and settled N=0; admit ≠ score.

---

## Metrics (null / zero)

| Metric | Value |
|---|---|
| `results` | **null** |
| `pnl` | **null** |
| `MZ` / `roi` | **null** (write_scorecard raises) |
| settled N (scorecard) | **0** |

---

## ScorecardPromotionRefused if

1. Invented fills / books / depth / PnL / resolution capture bytes.
2. Treated admit wire or 16 units as Examiner score / scored promote.
3. Lee-Ready invented or used.
4. `000` retuned.
5. EMPTY-OB / Cap-SR / QF / L2 / SOT-ID / fee-queue family reopened as this packet.
6. Claimed this ungates S1 / S2 / R2-P4.
7. Live orders.
8. Scored with settled N=0 pretending payoff.

### Score gate

Examiner-ready declaration with non-null fee-honest completed artifacts (settled join N>0 where required) — admit alone is insufficient.

**ACK:** `lab/governance/astra/packets/EXAMINER_ACK_C1_ADMIT_WIRE_PR39_STUB_READY_NOT_SCORED_2026-09-23.json`  
**Merge stamp:** `lab/governance/astra/packets/CONDUCTOR_MERGE_C1_ADMIT_WIRE_PR39_2026-09-23.json`  
**Still owned NOT_SCORED:** EMPTY-OB PR30 · ETH-FQ PR36 · ATP-FQ PR34 · CPI-FQ PR33 · NHL-FQ PR32 · Q7-B rehab P1 PR38 HOLD · prior conveyor  
**Stamped:** 2026-09-23T15:07:30-04:00
