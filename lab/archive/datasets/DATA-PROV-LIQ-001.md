# DATA-PROV-LIQ-001

- **DATA_ID:** DATA-PROV-LIQ-001
- **STATUS:** **FORWARD_CAPTURE_ONLY** · **HISTORICAL_DATA_BLOCKED** (Clock noted)
- **Registered:** 2026-09-11 UTC (live collector go-live)
- **Authorized:** Logan M 2026-09-11 — live forward only; **no** paid historical backfill
- **Path:** `/workspace/lab/data/DATA-PROV-LIQ-001/`
- **Layout:** `{raw,derived,manifests,quality}/` (+ `logs/`, `provenance/`)
- **Provenance:** `data/DATA-PROV-LIQ-001/provenance/FORWARD_CAPTURE.md`
- **Schema:** v1 — `exchange_event_time` + `local_receipt_time`; no invented fields

## Role

Actual Binance **USD-M** forceOrder / liquidation events for `BTCUSDT` + `ETHUSDT`. Not OHLCV. Not aggTrades. Not wick-inferred.

## Inventory

| Item | Value |
|------|-------|
| Vision UM hist | **None** |
| Live WS | `wss://fstream.binance.com/market/ws/!forceOrder@arr` → filter BTC/ETH |
| Raw | `raw/forceOrder/YYYY-MM-DD.jsonl` append-only + chunk sha256 in `manifests/` |
| Backfill | **None** by policy |

## Access gates

| Path | Access |
|------|--------|
| raw/ | append-only; prior lines immutable |
| derived/ | empty until approved |
| manifests/ | chunk hashes |
| quality/ | PENDING_CLOCK |
| EDGE-20260911-003 | **Historically blocked**; forward-only until Clock |

## Status history

1. **FORWARD_CAPTURE_ONLY / PENDING_CLOCK** ← current (2026-09-11)

## Clock note (2026-09-11T04:33:18Z)

- **Historical seal-window VERDICT:** REJECTED / HISTORICAL_DATA_BLOCKED
- **Mode:** FORWARD_CAPTURE_ONLY (live PID observed alive at audit)
- **EDGE-20260911-003:** HISTORICAL_DATA_BLOCKED
- **Full note:** `/workspace/lab/data/DATA-PROV-LIQ-001/provenance/DATA_VERDICT_DATA-PROV-LIQ-001.md`

## Archivist note (Cycle 5 CLOSE)
- LIQ forward capture = **PASSIVE accumulation** (no Examiner route; EDGE-003 remains HISTORICAL_DATA_BLOCKED).
