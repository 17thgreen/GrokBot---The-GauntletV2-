# Fixtures

`tiny_synthetic_ohlcv.csv` is **SYNTHETIC** — for unit tests of mechanics
(lookahead / splits) only.

**NEVER** treat this file as RESEARCH evidence, VALIDATION evidence, or a DATA-PROV series.
It must not appear in any MEASUREMENT report as real market data.

`mock_slice_layout/` is **SYNTHETIC** pre-sliced parquet (warmup/research/validation/sealed)
for unit tests of the DATA-PROV-001 on-disk layout adapter.

**NEVER** treat mock_slice_layout as RESEARCH/VALIDATION evidence or real DATA-PROV.
