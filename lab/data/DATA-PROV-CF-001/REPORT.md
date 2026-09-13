# DATA-PROV-CF-001 REPORT
**Generated UTC:** 2026-09-13T17:53:12Z
**Trade:** FORBIDDEN · secrets not present in this tree

## Fetch
- Hours planned per asset: 169 (2026-09-04T20 → 2026-09-11T20 inclusive)
- Assets: BRTI, ETHUSD_RTI
- Raw hour files: 338
- HTTP status counts: {"200": 337, "SKIP_EXISTING": 1}
- DAY timespan: not used (DAY probe HTTP 503/400); HOUR used
- Schema: top-level `data` → `payload` (list), `serverTime`. Each payload elem: `time` (unix ms int), `value` (str).
- `timespan=HOUR` + `timestamp=T` = hour **starting at T**: prints in `[T, T+1h)`. Probe BRTI 2026-09-11T20: 18000 prints / 3600 unique seconds (5/s).

## Derive (1Hz last-in-second)
- Rule: per unix second, keep print with max `timestamp_ms`
- Contracts: 1208
- n with 60/60 locked seconds: 1208
- n with any MISSING slot in close minute: 0
- n with pre_close_last: 1208
- Missing-slot rate BTC: 0.000000
- Missing-slot rate ETH: 0.000000

## Clock audit only (NOT a feature)
- Reconstructed 60s mean vs EXPIRATION_VALUE: n=1208, MAE=0.144134
- EXPIRATION_VALUE not used as p / feature

## Artifacts (local only; not in git)
- raw/: hour JSON
- derived/close_minute_1hz.ndjson
