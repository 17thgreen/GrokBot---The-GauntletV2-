# Provisional DATA-* attachment (no venue lock)

To run PROV-MEAS-20260910-001, register a series that satisfies:

## Required
- BTC and ETH continuous OHLCV (or trades→5m bars), separate files or keyed series
- Bar size: 5m (or finer, resampled with documented rule)
- Timestamps: exchange event time (UTC), sorted, unique bar index
- Columns minimum: timestamp, open, high, low, close, volume (volume unused by 001 v0 but kept)
- History: enough for warmup max(W)+max(L) = 48+576 = 624 bars (~2.2 days at 5m) **plus** RESEARCH+VALIDATION+HOLDOUT mins — practically prefer **≥90 UTC days** per instrument [A] target
- Document source label as **PROVISIONAL** — e.g. "public aggregator / research dump" — **not** a production venue lock
- Point-in-time: no future bars; no revised closes after research start without Clock note

## Forbidden as silent upgrades
- Switching venue mid-test without new DATA_ID
- Optimizing splits after seeing holdout
- Treating provisional fees as [V]

## Clock reviews
Knowability of close-t features; bar construction; split sealing; quarantine if lineage unclear.
