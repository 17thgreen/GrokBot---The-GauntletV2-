# Examiner scorecard STUB — C2 NHL-FQ harness — READY NOT_SCORED

**Seat:** Examiner (Kalshi)  
**Packet:** C2-KXNHLGAME-FEEQUEUE-HARNESS (feature family **NHL-FQ**)  
**Lab:** `kalshi_c2_kxnhlgame_feequue_lab_20260923/`  
**PR32:** squash-merged **main@677d5d4f0d5ed1235b4827bf89dd98d82bc34356** (draft head `f8b993fc…`, base `ead2cb41…`)  
**ACCEPT:** `f0d5c7da…` · **SOURCE_PINS:** `2f1a9da6…`  
**Units:** **12 OK** — code verify only; 12 units ≠ Examiner score  
**Status:** **READY** as scorecard stub · measurement **NOT_SCORED**

**Freeze:** sha256 `a36ec35143a32c7cd24e9fdf2a33f645d356b93e34c131bb1b8a94e3f92e38f5`  
**Scout hunt:** sha256 `1ab794ad688ba31e0178e78294dcdbe50cf2799a71f40245e5a04a80e9dd5762` · 66 markets / 33 events  
**Panel stub:** sha256 `60d183e7bdcf25adbc94eeeb3bb361b5232c19c0fe3e6a115f45ab3fcb100c79` · 6 events / 12 markets · `admitted_at` **null** · scout subset  
**Box digest verification:** **PASS** for freeze (top-level and harness subdir copies), scout, and panel.

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| Pre-ACCEPT empty | **REFUSED as scorecard** |
| S1 green claim | **REFUSED** |
| S1 / S2 / R2-P4 | **NOT ungated** |
| Live promotion / orders | **DENIED** |

**Desk headline:** PR32 stub READY — authentic freeze/scout/panel shas and merge verified; NHL-FQ metrics remain null until Clock admit + settled join N>0 + Examiner-ready.

---

## Arms

| Arm | Slice |
|---|---|
| **C2A0** | `maker_vs_taker_native` |
| **C2A1** | `content_fresh_vs_stale_bin` |

Knob: `analysis_slice`. Measurement only; no strategy or live order path.

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

---

## Pre-PR HOLD → READY (2026-09-23 ET)

**Prior hold:** `EXAMINER_HOLD_C2_KXNHLGAME_FEEQUEUE_HARNESS_PRE_PR_2026-09-23.json` — **SUPERSEDED** by PR32 READY main@`677d5d4f0d5ed1235b4827bf89dd98d82bc34356`.  
**Owner:** Examiner (Kalshi). Stub **READY** · measurement **NOT_SCORED**.

### ScorecardPromotionRefused if

1. Invented depth / fills / PnL.
2. Lee-Ready invented or used as a substitute for native fields.
3. `000` retuned.
4. Cap-SR / QF / L2 / EMPTY-OB / SOT-ID / L2-SF reopened.
5. Claimed S1 green.
6. Claimed this packet ungates S1 / S2 / R2-P4.
7. Used ATL@GB or placed live orders.
8. Promoted the pre-ACCEPT empty result into a scorecard.
9. Scored before Clock admit + settled join N>0 + Examiner-ready.

### Score gate

Clock admit + settled join N>0 + Examiner-ready.

**Refuse binds:** invent depth/fills/PnL · Lee-Ready · `000` retune · Cap-SR/QF/L2/EMPTY-OB/SOT-ID/L2-SF reopen · claim S1 green · ungate S1/S2/R2-P4 · ATL@GB · live orders.

**ACK:** `lab/governance/astra/packets/EXAMINER_ACK_C2_NHL_FQ_PR32_STUB_READY_NOT_SCORED_2026-09-23.json`  
**Merge stamp:** `lab/governance/astra/packets/CONDUCTOR_MERGE_C2_KXNHLGAME_FEEQUEUE_HARNESS_PR32_2026-09-23.json`  
**Still owned NOT_SCORED:** L2-SF PR31 · EMPTY-OB PR30 · SOT-ID PR29 · L2-CAT PR28 · R2-P3 PR27 · NHL-FQ PR32 (this stub now READY)  
**Stamped:** 2026-09-23T13:55:02-04:00
