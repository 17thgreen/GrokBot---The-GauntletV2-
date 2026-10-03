# Examiner scorecard STUB — R3-P2 queue_position — READY NOT_SCORED

**Seat:** Examiner (Kalshi)  
**Packet:** R3-P2-QUEUE-POSITION (feature family **R3-P2**)  
**Lab:** `kalshi_r3_p2_queue_position_lab_20260923/`  
**PR37:** squash-merged **main@9eba15870e66dcde8ffc17a56c73016245a833c1** (head `be1db1ae…`, base `9fd5d7cb…`)  
**Units:** **6 OK** (`tests.test_ingest`) — code verify only; 6 units ≠ Examiner score  
**Status:** **READY** as scorecard stub · measurement **NOT_SCORED** · sample ingest ≠ calibration score · **not a scored promote**

**Series:** sha256 `74ef9a9bb54054691e26b7b752568c8e833f51d21292034b1f40b9f3ca4ba8b4` · desk `packets/r3_p2_queue_position/results/demo_queue_sample_series.json` **MATCH** PR fixture · `samples_n=38` · `leftover_resting=no` · 18 null `queue_position_fp` kept  
**Calibration status:** `SAMPLE_INGESTED_CALIBRATION_NOT_RUN` · `calibration_run=false`  
**Resting honesty:** kept · no invent

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement / calibration | **NOT_SCORED** |
| Sample ingest | **PINNED** (≠ score) |
| Scored promote | **DENIED** |
| Live orders | **DENIED** |

**Desk headline:** PR37 stub READY — authentic demo series pinned; calibration metrics remain null until a real calibration run under Examiner-ready rules.

---

## Metrics (null on disk)

| Metric | Value |
|---|---|
| `results` | **null** |
| `abs_err` / `abs_err_contracts` | **null** |
| `signed_bias` | **null** |
| `brier` | **null** |
| `pnl` | **null** |
| `mz` | **null** |
| `roi` | **null** |

---

## ScorecardPromotionRefused if

1. Invented abs_err / signed_bias / brier / PnL / mz / roi.
2. Treated sample ingest, 6 units, or merge as calibration score / scored promote.
3. Q6-`000` retuned.
4. Live orders / Astra live resting.
5. Dropped or rewritten the 18 null `queue_position_fp` rows dishonestly.
6. Relabeled resting honesty (`leftover_resting=no` / empty `final_resting_ids`) into a pass.

### Score gate

Calibration run with non-null estimate-error metrics under frozen rules + Examiner-ready. Sample ingest alone is insufficient.

**ACK:** `lab/governance/astra/packets/EXAMINER_ACK_R3_P2_PR37_STUB_READY_NOT_SCORED_2026-09-23.json`  
**Merge stamp:** `lab/governance/astra/packets/CONDUCTOR_MERGE_R3_P2_QUEUE_POSITION_PR37_2026-09-23.json`  
**Stamped:** 2026-09-23T15:22:30-04:00

---

**UPDATE 2026-09-23T17:28 ET:** `abs_err`/`signed_bias` channel **SCORED** — see `EXAMINER_SCORECARD_R3_P2_ABS_ERR_SIGNED_BIAS_2026-09-23.md` (KEEP measurement honesty · STATIC_SERIES_IDENTITY_MATCH · **not a promote**). Brier/PnL/cancel-model remain unscored.
