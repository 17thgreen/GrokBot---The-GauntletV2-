# DATA VERDICT — DATA-PROV-TRADES-001
**Issued by:** The Clock (Data Integrity Sentinel)  
**Issued UTC:** 2026-09-11T00:59:35Z  
**Audit report:** `/workspace/lab/data/DATA-PROV-TRADES-001/provenance/CLOCK_AUDIT_REPORT.json`  
**Distinct from:** DATA-PROV-001 (OHLCV) — **no merge**

---

## DATA VERDICT: CONDITIONAL

**QUALITY_STATUS:** APPROVED_WITH_LIMITATIONS

Usable for provisional RESEARCH/VALIDATION of **trade-flow-only** edges (e.g. EDGE-20260911-001/002) that use aggressor-signed aggTrades under explicit knowability rules.

**Does not** unlock EDGE-005 or EDGE-006 (UNMEASURABLE WITHOUT L2).  
**Not** venue marriage. **Not** capital. **Not** full L2.

Examiner may proceed on trade-flow cards after Conductor routes. Conductor may cut timestamp-aligned seals after this verdict — **prefer timestamp alignment** over calendar-day cuts (boundary leak days 2024-05-27 and 2025-07-14).

---

## DATA MANIFEST

| Field | Value |
|-------|-------|
| DATASET_ID | DATA-PROV-TRADES-001 |
| SOURCE | Binance Vision daily UM aggTrades zips (`data.binance.vision`) [V] |
| VENUE | Binance USD-M Futures — **PROVISIONAL REFERENCE only** |
| INSTRUMENT | BTCUSDT, ETHUSDT perpetual |
| START | 2021-01-01 UTC |
| END | 2026-08-31 UTC |
| FREQUENCY | tick / aggTrade events (daily zip partitions) |
| TIMESTAMP_DEFINITION | `transact_time` = exchange event time, UTC epoch **milliseconds** [V] |
| KNOWN_LATENCY | **[U]** — no receipt-time in Vision archives |
| KNOWN_GAPS | Calendar missing_days=0 both symbols [V]; full per-day row inventory not computed [V] |
| TRANSFORMATIONS | None — raw zips immutable; derived/ empty [V] |
| QUALITY_STATUS | APPROVED_WITH_LIMITATIONS |
| FILES | 2069 zips × 2 symbols; SHA256 4138/4138 verified [V] |

### Schema [V]
`agg_trade_id, price, quantity, first_trade_id, last_trade_id, transact_time, is_buyer_maker`  
Header optional on some days — parse as 7-col Vision order when absent (verified safe on samples including ETH 2021-01-01, BTC/ETH 2022-06-15).

### Aggressor semantics [V]
`is_buyer_maker==true` → aggressor **SELL**; `false` → aggressor **BUY**.

---

## HARD TESTS [V]

| Test | Result |
|------|--------|
| Inventory / calendar | PASS — 2069/2069 each; contiguous; recovery 24/24 present |
| HASH_VERIFY | PASS — 4138/4138 sidecar + SHA256SUMS |
| DUPLICATES (sampled) | PASS — dup agg_trade_id=0 |
| ORDERING (sampled) | PASS — ID strictly ↑; time-back=0; in-day bounds |
| Cross-day continuity (6 pairs) | PASS |
| Header / schema handling | PASS — headerless days handled safely |
| Aggressor domain | PASS — {true,false} only on samples |
| OHLCV 5m alignment (8 days) | PASS — empty_ohlcv_bars=0; clock compatible |
| LOOKAHEAD / knowability | PASS (rules documented); receipt-time [U] |
| CROSS-VENUE | N/A single venue |
| L2 proxy check | PASS policy — no depth/spread proxy from trades |

Deep CSV coverage: **33 sampled days** (not all 4138 content-scanned). Full content scan of every zip: **UNTESTED**.

---

## FAILURES

None that fail hard tests on inventory, hashes, or sampled integrity.

---

## LIMITATIONS (why CONDITIONAL, not APPROVED)

1. **Receipt-time [U]** — knowability bounded by exchange `transact_time` only.
2. **Provisional reference** — not production venue lock / not capital.
3. **Content audit is sampled** — full per-day row inventory across all zips not measured [V].
4. **EDGE-005/006 remain UNMEASURABLE WITHOUT L2** — this series does not provide depth troughs, bid/ask sizes, or spread repair path.
5. **Seal cuts:** calendar-day alignment leaks on OHLCV boundary days; use **timestamp-aligned** cuts.
6. Distinct Vision historical path vs DATA-PROV-001 klines API path — do not assume byte-identical market identity beyond measured sample alignment [I].

---

## SAFE FEATURES (trade-flow edges only)

- Aggressor-signed aggTrade events at/after `transact_time`
- Features for decision at 5m bar close `C` using only trades with `transact_time <= C` (and after bar `close_time_ms`)
- Counts / signed volume / imbalance over completed intervals
- Separate BTC/ETH pipelines
- Alignment to DATA-PROV-001 bar grid when timestamp rule respected (samples compatible)

---

## UNSAFE FEATURES

- Any **depth trough / replenishment** feature (EDGE-005) → **UNMEASURABLE / QUARANTINE proxy**
- Any **bid/ask size or spread-repair** feature (EDGE-006) → **UNMEASURABLE / QUARANTINE proxy**
- Using trades with `transact_time >` decision time → **LOOKAHEAD**
- Treating Vision archive as live receipt-time latency model → **[U] / block**
- Calendar-day seal cuts that straddle OHLCV research/validation/holdout boundaries → **MISALIGNMENT / contamination risk**
- Merging silently into DATA-PROV-001 → **forbidden**

---

## REQUIRED REMEDIATION (before upgrading / before capital)

1. Optional: full per-day row inventory + ID continuity scan across all zips.
2. Instrument receipt-time on live/shadow trade feeds.
3. L2 dataset required before any EDGE-005/006 measurement.
4. Timestamp-aligned seal slices cut by Conductor/Archivist after this verdict.
5. Venue-specific live path + cross-venue replication before capital.
6. Future sealed forward window still mandatory before capital.

---

## Examiner / routing gate

| Claim class | Gate |
|-------------|------|
| EDGE-20260911-001/002 (trade-flow only) | **CLEARED** for provisional measurement after Conductor route |
| EDGE-005 / EDGE-006 | **BLOCKED** — UNMEASURABLE WITHOUT L2 |
| Historical holdout / capital / venue marriage | **HOLD** |
