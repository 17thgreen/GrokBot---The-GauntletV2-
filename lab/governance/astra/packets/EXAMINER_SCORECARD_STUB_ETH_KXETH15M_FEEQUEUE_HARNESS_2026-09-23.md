# Examiner scorecard STUB — ETH-FQ harness — READY NOT_SCORED

**Seat:** Examiner (Kalshi)  
**Packet:** ETH-KXETH15M-FEEQUEUE-HARNESS (feature family **ETH-FQ**)  
**Lab:** `kalshi_eth_kxeth15m_feequue_lab_20260923/`  
**PR36:** squash-merged **main@82bf7bb99bcc618b912255cc24022b23f9f15047** (merged head `bd71bea5…`, base `438f4abf…`)  
**ACCEPT:** `3e553395…`  
**Units:** **13 OK** — code verify only; 13 units ≠ Examiner score  
**Status:** **READY** as scorecard stub · measurement **NOT_SCORED**

**Freeze:** sha256 `9cae3bad089e6e18bee22694a36a1a2c18db33935a315766cd6bd8f8476aa83a`  
**Scout hunt:** sha256 `18f70001c8d68418d435e2016b756f90753e374a92d323f8e999f76215d9cf9c` · 1 market / 1 event  
**Panel stub:** sha256 `b3379783c84eaa910f6a57f5318b8536f21220cfeaf0f73e9ff73ee0f20dd90d` · 1 event / 1 market · `admitted_at` **null** · full tiny hunt  
**Box digest verification:** **PASS** for freeze, scout, panel, and ACCEPT (match merge stamp digests).

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| Pre-PR HOLD | **SUPERSEDED** by PR36 READY |
| S1 / S2 / R2-P4 | **NOT ungated** |
| Live promotion / orders | **DENIED** |

**Desk headline:** PR36 stub READY — authentic freeze/scout/panel/accept shas and merge verified; ETH-FQ metrics remain null until Clock admit + settled join N>0 + Examiner-ready.

---

## Arms

| Arm | Slice |
|---|---|
| **ETHA0** | `maker_vs_taker_native` |
| **ETHA1** | `content_fresh_vs_stale_bin` |

Knob: `analysis_slice`. Measurement only; no strategy or live order path. **NOT live crypto trading.**

---

## Metrics (null on disk)

| Metric | Value |
|---|---|
| `results` | **null** |
| `pnl` | **null** |
| `maker_vs_taker_roi_delta` | **null** |
| `fresh_vs_stale_gap` | **null** |
| `settled_join_n` | **null** |
| `n_books` | **null** |
| `fill_density` | **null** |
| `occurrence_datetime` | **null** (SoT join deferred) |

---

## Pre-PR HOLD → READY (2026-09-23 ET)

**Prior hold:** `EXAMINER_HOLD_ETH_KXETH15M_FEEQUEUE_HARNESS_PRE_PR_2026-09-23.json` — **SUPERSEDED** by PR36 READY main@`82bf7bb99bcc618b912255cc24022b23f9f15047`.  
**Owner:** Examiner (Kalshi). Stub **READY** · measurement **NOT_SCORED**.

### ScorecardPromotionRefused if

1. Invented depth / fills / fill-density / occurrence / PnL.
2. Lee-Ready invented or used as a substitute for native fields.
3. `000` retuned.
4. Cap-SR / QF / L2 / EMPTY-OB / SOT-ID / L2-SF / NHL-FQ / CPI-FQ / ATP-FQ / ETH-FQ / C5 reopened.
5. Claimed this packet ungates S1 / S2 / R2-P4.
6. Used ATL@GB or placed live orders.
7. Scored before Clock admit + settled join N>0 + Examiner-ready.
8. Treated 13 unit tests as an Examiner score.
9. Bacchus / kxeth15m strategy port or live crypto trading.

### Score gate

Clock admit + settled join N>0 + Examiner-ready.

**Refuse binds:** invent depth/fills/fill-density/occurrence/PnL · Lee-Ready · `000` retune · Cap-SR/QF/L2/EMPTY-OB/SOT-ID/L2-SF/NHL-FQ/CPI-FQ/ATP-FQ/ETH-FQ/C5 reopen · ungate S1/S2/R2-P4 · ATL@GB · live orders · bacchus/kxeth15m port.

**Kick:** `lab/governance/astra/packets/CONDUCTOR_KICK_EXAMINER_ETH_FQ_PR36_READY_NOT_SCORED_2026-09-23.json`  
**Merge stamp:** `lab/governance/astra/packets/CONDUCTOR_MERGE_ETH_KXETH15M_FEEQUEUE_HARNESS_PR36_2026-09-23.json`  
**Still owned NOT_SCORED:** ATP-FQ PR34 · CPI-FQ PR33 · NHL-FQ PR32 · L2-SF PR31 · EMPTY-OB PR30 · SOT-ID PR29 · L2-CAT PR28 · R2-P3 PR27 · ETH-FQ PR36 (this stub now READY)  
**Stamped:** 2026-09-23T14:58:40-04:00
