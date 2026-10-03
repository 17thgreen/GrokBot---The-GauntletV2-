# DATA-PROV-LIQ-001 — Forward capture provenance

- **DATA_ID:** DATA-PROV-LIQ-001
- **Mode:** **LIVE FORWARD CAPTURE ONLY** — no historical backfill
- **Authorized:** Logan M · 2026-09-11 (Governor: LIQ live-forward; paid hist **not** authorized)
- **Schema:** **v1** — `exchange_event_time` + `local_receipt_time`; omit absent fields (do **not** invent `[U]`)
- **Script:** `provenance/forward_capture_forceOrder.py`
- **PID:** `provenance/capture.pid` · status: `provenance/capture_status.json`

## Layout

```
data/DATA-PROV-LIQ-001/
  raw/forceOrder/YYYY-MM-DD.jsonl   # append-only; past lines immutable after write
  derived/                          # empty until approved transforms
  manifests/chunks.jsonl            # per-chunk sha256 + bytes + lines
  manifests/YYYY-MM-DD.sha256       # sidecar hash
  quality/                          # PENDING_CLOCK stream-quality notes
  logs/capture.log                  # human text
  logs/ops_events.jsonl             # structured ops codes
  provenance/FORWARD_CAPTURE.md
```

## Timing fields (SIGNAL vs audit)

| Field | Source | Use |
|-------|--------|-----|
| `exchange_event_time` | Binance `E` (ms) | Decision / burst windows — event_ts ≤ t |
| `exchange_order_time` | Binance `o.T` when present | Order time; omit if absent |
| `local_receipt_time` | Box clock ISO-Z | Audit / lag only — **never** substitute for event time |
| `receipt_minus_event_ms` | local_ms − E when E present | Drift diagnostic; `CLOCK_DRIFT` ops if \|drift\| > 5s |

Missing exchange fields are **omitted**, not filled with nulls invented as known values.

## Ops log codes (`logs/ops_events.jsonl`)

`CONNECT` · `DISCONNECT` · `RECONNECT` · `HEARTBEAT` · `TIMEOUT` · `GAP` · `PARSE_FAILURE` · `SOURCE_FAILURE` · `CLOCK_DRIFT` · `SESSION_RESET`

## Stream (verified 2026-09-11 from this box)

- **URL:** `wss://fstream.binance.com/market/ws/!forceOrder@arr` (USD-M market path)
- **Persist filter:** `BTCUSDT`, `ETHUSDT` only
- **fapi REST:** HTTP **451** geo eligibility block — **not** used; WS fstream **reachable** (live forceOrders observed)
- **Vision UM liquidationSnapshot:** empty / discontinued — **no hist path**
- **EDGE-20260911-003:** historically blocked (no free UM liq hist)

## Immutability + hashes

- Raw JSONL is **append-only**; collector never rewrites prior lines in steady state.
- One-time v0→v1 rematerialize of go-live lines (same `raw` payloads; field rename) recorded as `SESSION_RESET reason=schema_v0_to_v1_rematerialize`; v0 bak: `*.jsonl.v0bak`.
- `manifests/chunks.jsonl` refreshed after each append with full-file sha256.

## What is forbidden

- Historical Vision / paid backfill without new authorization
- Wick-inferred liquidations labeled as this dataset
- COIN-M snapshot aliased to USD-M
- Inventing missing `exchange_event_time` or other fields

## Related

- `governance/DATA_PROV_CATALYST_SOURCES_2026-09-11.md` §3
- `archive/audit/2026-09-11-Governor-authorize-FUNDING-OI-fetch-LIQ-forward.md`
- `archive/datasets/DATA-PROV-LIQ-001.md`
