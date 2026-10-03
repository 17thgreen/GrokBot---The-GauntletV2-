# DATA-PROV-PM-006

Polymarket Global BTC/ETH Up/Down **live YES best bid + best ask** forward capture.

- **Historical Sep 4–11 2026 bid/ask:** **BLOCKED** (see `provenance/HISTORICAL_HUNT_BLOCKED.md`)
- **Live:** `provenance/forward_capture_book.py` polls CLOB `/book` after Gamma slug resolve
- `mid = (best_bid + best_ask) / 2` only when both sides exist — never from last trade
- Not a Feature. Not Examiner. Trade FORBIDDEN. Auth: none.
