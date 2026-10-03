# DATA-PROV-PM-006 — Forward capture provenance

- **DATA_ID:** DATA-PROV-PM-006
- **Mode:** **LIVE FORWARD CAPTURE** — historical bid/ask for Sep 4–11 2026 is **BLOCKED** (see HISTORICAL_HUNT_BLOCKED.md)
- **Authorized:** Logan M via Conductor order 2026-09-13 (get real Poly bid/ask; public only; no keys; no orders)
- **Schema:** **v1** — `best_bid` + `best_ask` required to emit `mid`; omit absent sides; never invent
- **Script:** `provenance/forward_capture_book.py`
- **PID:** `provenance/capture.pid` · status: `provenance/capture_status.json`

## Layout

```
data/DATA-PROV-PM-006/
  raw/book/YYYY-MM-DD.jsonl    # append-only bid/ask rows (both sides present)
  raw/book_partial/YYYY-MM-DD.jsonl  # optional: one-sided books (no mid) — audit only
  logs/capture.log
  logs/ops_events.jsonl
  manifests/chunks.jsonl
  provenance/FORWARD_CAPTURE.md
  provenance/HISTORICAL_HUNT_BLOCKED.md
```

## Timing

| Field | Source | Use |
|-------|--------|-----|
| `book_timestamp` | CLOB `/book` `timestamp` (ms string) | Venue book time |
| `local_receipt_time` | Box clock ISO-Z | Audit / lag only |
| `receipt_minus_book_ms` | local_ms − book_ts | Drift diagnostic |

## Resolution

- Gamma `GET https://gamma-api.polymarket.com/events?slug={btc\|eth}-updown-{15m\|5m}-{unix}`
- Up token = first `clobTokenIds[0]` when outcomes `["Up","Down"]`
- Poll `GET https://clob.polymarket.com/book?token_id=`

## Row rule

Emit a **kept** row only when `best_bid` and `best_ask` are both finite and `best_ask >= best_bid`.  
`mid = (best_bid + best_ask) / 2`. Never from `/prices-history` or `/midpoint` alone.

## Forbidden

- Inventing bid/ask
- Treating last trade as mid
- Trading / wallet / API keys
- Examiner scoring / Feature READY
