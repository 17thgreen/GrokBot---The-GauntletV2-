# R3-P2 — queue_position_fp vs L2 FIFO cancel models — FREEZE 2026-09-22 (ET)

**Packet ID:** R3-P2-QUEUE-POSITION-CALIB  
**Owner (freeze):** Deep Research  
**Implementer (later):** Mechanic (demo keys) → Collector (demo poll) → Simulator (cancel-model harness) → Examiner  
**Reviewer:** Conductor triage  
**Status:** **FROZEN** — results/pnl **null** (not run)  
**Cite:** Conductor R3 triage ADMIT (demo/paper only); R3 brief §R3-P2; Kalshi queue_position API; tfrmma realistic-mm-backtester; acheron  
**Hard rules:** **Demo/paper resting orders only.** Never Astra live resting. No `000` queue-bin retune. No invented PnL.

---

## Intent

Calibrate L2 FIFO cancel-model queue-ahead estimates against official `queue_position_fp` (contracts ahead). Outputs: `abs_err_contracts`, `signed_bias`, fill-prediction Brier under acheron estimate-queue knobs and tfrmma ReduceRatioCancelModel / ProbQueueCancelModel.

**Not a strategy.** Estimator calibration only — does not reopen queue-fragility scoring on `000`.

---

## Dead-card / live-pin overlap (named)

| Pin | Overlap | Handling |
|---|---|---|
| R1-P5 rails / QF freeze on `000` | **Related** | Calibrates estimator vs venue truth; **no** change to assumed q3300/q10000 or QF score reopen |
| Q6-`000` | **None on signal** | No retune |
| S2/R2-P4 | **Not a start** | Stay WAIT on C1 |
| Live Astra resting | **Forbidden** | Demo/paper only |

---

## Mandatory pins

| Dep | Pin | Rule |
|---|---|---|
| Rails | R1-P5 @ `6a28e0d6…` | Queue-attribution instrument family |
| Venue | `queue_position_fp` API | Poll on demo/paper resting only |
| Models | acheron estimate-queue; tfrmma cancel models | Algebra port only |

---

## Measurement objects

`queue_position_fp`, L2 estimate under each cancel model, `abs_err_contracts`, `signed_bias`, Brier — all null until run.

## Empty results

`packets/r3_p2_queue_position/` — `results`/`pnl` null

## Frozen-at
`2026-09-22T23:59:59+00:00` UTC. Deep Research under Conductor R3 ADMIT (after P1).
