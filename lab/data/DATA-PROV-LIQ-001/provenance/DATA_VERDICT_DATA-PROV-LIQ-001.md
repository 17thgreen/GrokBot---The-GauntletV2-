# DATA VERDICT — DATA-PROV-LIQ-001
**Issued by:** The Clock  
**Issued UTC:** 2026-09-11T04:33:18Z

---

## DATA VERDICT: REJECTED for historical seal-window RESEARCH

**Mode noted:** **FORWARD_CAPTURE_ONLY**  
**Historical seal-window RESEARCH:** **HISTORICAL_DATA_BLOCKED**  
**EDGE-20260911-003:** remains **HISTORICAL_DATA_BLOCKED** (no free UM liquidation history)

This is **not** an APPROVED/CONDITIONAL clearance for backtest against DATA-PROV-001 SEAL_LOCK (2021-01-01 → 2026-08-31).

---

## Why no historical VERDICT for seal RESEARCH

| Fact | Tag |
|------|-----|
| Vision UM `liquidationSnapshot` empty / discontinued | [V] source map |
| No paid hist authorized (Logan 2026-09-11) | [V] |
| Wick-inferred liq forbidden as this DATA_ID | [V] policy |
| COIN-M snapshots ≠ USD-M BTCUSDT/ETHUSDT | [V] |
| Live WS capture only from go-live | [V] |

---

## Forward capture status (observed this audit)

| Item | Value | Tag |
|------|-------|-----|
| PID | 360571 **ALIVE** | [V] |
| WS | `wss://fstream.binance.com/market/ws/!forceOrder@arr` | [V] |
| Schema | v1: `exchange_event_time` + `local_receipt_time` | [V] |
| Raw chunk | `raw/forceOrder/2026-09-11.jsonl` — 52 lines (at audit) | [V] |
| Capture session start | ~2026-09-11T04:23:32Z | [V] status |
| Coverage usable for seal-window hist | **NONE** | [V] |

Forward stream may later support **forward-only / shadow** measurement once Clock audits stream quality (ordering, dup IDs, side semantics, gap/ops codes) on accumulated span — **separate** commission; not this verdict.

---

## SAFE / UNSAFE

**SAFE (future forward-only, after stream-quality audit):** forceOrder events with `exchange_event_time ≤ t`; lag audit via `local_receipt_time`.

**UNSAFE / FORBIDDEN:**
- Any historical RESEARCH claiming seal-window liqs from this dataset today
- Wick / volume-spike inferred “liquidations”
- CM→UM aliasing
- Invented exchange event times

---

## REQUIRED REMEDIATION to unlock EDGE-003 historical RESEARCH

1. Logan-authorized paid UM forceOrder archive for seal window, **or**
2. Accept forward-only power limits with explicit Edge card rewrite + new DATA coverage dates after sufficient live accumulation + Clock stream audit

---

## Examiner gate

| Claim | Gate |
|-------|------|
| EDGE-003 historical RESEARCH on SEAL_LOCK | **BLOCKED** |
| Forward-only measurement | **NOT YET CLEARED** — needs separate stream-quality Clock audit when Conductor commissions |
