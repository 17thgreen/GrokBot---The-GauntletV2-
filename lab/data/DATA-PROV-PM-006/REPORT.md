# DATA-PROV-PM-006 — Report (2026-09-13)

## (a) Historical bid/ask — **BLOCKED**

Sought: YES best bid+ask timestamps for BTC/ETH 15m Up/Down over **2026-09-04 → 2026-09-11 UTC**.

Probed free paths with real HTTP (see `provenance/HISTORICAL_HUNT_BLOCKED.md` + `HISTORICAL_HUNT_PROBES.json`):

- CLOB `/orderbook-history` → **200** `{"count":0,"data":[]}` (live and hist tokens)
- CLOB `/book` on resolved hist token → **404** (live-only)
- CLOB `/prices-history` → **200** last-trade series only (not bid/ask)
- data-api book endpoints → **404**
- pmxt R2 mirrors for 2026-09-04 → **404**
- HF `Joseph3222/polymarket-orderbook` → free CC-BY but partitions **end 2026-08-10** (zero Sep paths)

**Verdict: NOT GETTABLE** on free public paths for the PM-003 window. Paid vendors not used.

## (b) Live forward capture — **RUNNING**

- Spec: `governance/DATA_PROV_PM_006_SPEC.md`
- Collector: `provenance/forward_capture_book.py`
- Status/PID: `provenance/capture_status.json`, `provenance/capture.pid`
- Raw: `raw/book/YYYY-MM-DD.jsonl` append-only
- Resolve: Gamma slug → Up `clobTokenIds`; poll CLOB `/book`
- Rule: emit mid only when both best_bid and best_ask exist

Confirmed real rows with both sides (example in status `last_sample`). Trade FORBIDDEN. No keys.
