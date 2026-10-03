# Adversary refuse-bind — R3 suite (P1 / P2 / P3 / P4)
**Date:** 2026-09-22 (America/New_York)  
**Packets:** R3-P1 · R3-P2 · R3-P3 · R3-P4 (**FROZEN** — Conductor ACCEPTED / live)  
**Owner:** The Adversary · **Reviewer:** Conductor  
**Cite:** `R3-P1_FEE_COST_VS_MODEL_FREEZE_KERNEL_2026-09-22.md` · `R3-P2_QUEUE_POSITION_CALIBRATION_FREEZE_KERNEL_2026-09-22.md` · `R3-P3_FL_MAKER_TAKER_BANDS_FREEZE_KERNEL_2026-09-22.md` · `R3-P4_L2_SHAPE_LONGSHOT_DEPTH_FREEZE_KERNEL_2026-09-22.md` · dedicated `R3-P3_ADVERSARY_REFUSE_BIND_2026-09-22.md`  
**Stance:** Suite-level refuse binds. No Q6-000 verdict change. No orders. No invented PnL. Measurement / provenance — not strategy kill. P3 detail lives in dedicated memo.

---

## Direct answer

**Yes — refuse** across the R3 suite:

1. **No bacchus strategy port** — extract fee_cost / instrumentation preference only; refuse wholesale 15m / crypto strategy import as Astra edge.  
2. **No invented PnL** — all suite `results`/`pnl` remain null until Examiner; refuse filled scorecards without units.  
3. **No treating paper maker ROI as Astra edge** — paper / author figures (incl. R3-P3 +2.6%) are hypothesis only.  
4. **No live queue probes as production fills** — R3-P2 demo/paper resting only; refuse treating demo `queue_position_fp` polls as live Astra fills or production queue evidence.  
5. **`fee_cost` preferred over model when present** — R3-P1: completed-net that used model-only while venue `fee_cost` was available → **REFUSE**.

---

## Refuse matrix (suite)

| Claim | Packet | Adversary stamp |
|---|---|---|
| Bacchus-mm strategy as Astra line | Suite | **REFUSE** port |
| Invented / premature PnL | P1–P4 | **REFUSE** — RESULTS_NULL until Examiner |
| Paper maker ROI as Astra evidence | P3 (see dedicated) | **REFUSE** — hypothesis only |
| Demo/paper queue poll = production fill | P2 | **REFUSE** |
| Model-only completed-net while `fee_cost` present | P1 | **REFUSE** |
| Lee-Ready / invented depth beyond raw L2 | P3 / P4 | **REFUSE** |
| `000` retune / promote / live orders | Suite | **DENIED** |

---

## Explicit non-actions

- No change to Q6-000 KEEP / Q7 KILL_B.  
- Does not replace dedicated R3-P3 refuse-bind.  
- No orders.

**Artifact:** `lab/governance/astra/packets/R3_SUITE_ADVERSARY_REFUSE_BIND_2026-09-22.md`
