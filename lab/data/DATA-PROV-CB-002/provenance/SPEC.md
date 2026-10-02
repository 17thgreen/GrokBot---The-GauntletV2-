# DATA-PROV-CB-002 — Coinbase Exchange 1m live forward candles

**Class:** DATA spec / forward capture. Not a Feature. Not READY. Not Examiner.
**Stamp:** 2026-09-14T01:55Z
**Trade:** FORBIDDEN. Public Exchange API only — **no key**.
**Auth:** none.

## Why
Follow-vs-fade join (`JOIN_SPEC_FOLLOW_VS_FADE_2026-09-14.md`) needs Coinbase 1m velocity on the **live** PM-006 / PM-008 span. DATA-PROV-CB-001 is the sealed Sep 4–11 research week only — do not append live rows there.

## Register
- **DATA_ID:** DATA-PROV-CB-002
- **Venue:** Coinbase Exchange
- **Products:** `BTC-USD`, `ETH-USD`
- **Granularity:** 60s
- **Policy:** completed bars only (`bar_end <= now`). No partial-minute close. No Binance/CF fill.
- **Paths:** `raw/candles/{BTC,ETH}-USD_YYYY-MM-DD.csv`

## Forbidden
Orders · Examiner · inventing closes · mixing into CB-001 · CB-VEL retune
