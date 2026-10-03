# R3-P2 JOIN SCAFFOLDING — plug-in prep 2026-09-22 (ET)

**Status:** SCAFFOLD ONLY — HOLD implement until Mechanic demo/paper keys (Conductor: ADMIT demo-gated)  
**Purpose:** After FEE+QUEUE HONESTY orchestrator lands, this defines the join surface so `queue_position_fp` can plug in fast.  
**Cite:** R3-P2 freeze `R3-P2_QUEUE_POSITION_CALIBRATION_FREEZE_KERNEL_2026-09-22.md`; Logan queue-position maximize signal  
**Hard:** No live orders. No 000 retune. No invented 110% / PnL. Metrics null until Examiner.

---

## Plug-in interface (draft)

Honesty orchestrator / future Examiner packet should accept an optional queue-truth provider:

```
QueueTruthProvider.poll(order_id) -> {
  queue_position_fp: Decimal | None,  # contracts ahead (venue)
  source: "kalshi_demo" | "synthetic_null",
  ts: str
}
```

L2 estimate side (acheron / tfrmma cancel models) stays behind the same provider boundary as `estimate_ahead(order_book_l2, model_id)`.

Outputs (null until demo fixtures): `abs_err_contracts`, `signed_bias`, Brier — see R3-P2 freeze.

---

## Wire-after-honesty

1. Import honesty orchestrator scorecard path (fee+queue null fields).  
2. Add `queue_truth` optional dependency — default returns null / synthetic_null.  
3. Do **not** start demo polling until Mechanic keys.  
4. Framing: calibration toward stronger queue honesty (Logan ~110% edge-test framing) is a **hypothesis label**, never a freeze number.

---

## Scaffolded-at

`2026-09-23T00:03:18.679293+00:00` UTC
