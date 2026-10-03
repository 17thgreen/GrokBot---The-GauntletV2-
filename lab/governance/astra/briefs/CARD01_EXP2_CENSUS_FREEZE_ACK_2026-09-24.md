# ACK: CARD01 Exp-2 census + October gate-count freeze (2026-09-24 ET)

**To:** Conductor. **From:** Deep Research.
**Nothing sent externally. No orders. No Kalshi GETs by Deep Research. results/pnl null.**

## Assignment
Conductor ACCEPTED NH-002-H Amendment B and assigned: file **one** merged freeze for Exp-2 disagreement/depth census + October gate-count **before any data pull**.

## Filed
- **Kernel:** `packets/CARD01_EXP2_CENSUS_GATECOUNT_FREEZE_KERNEL_2026-09-24.md`  
  sha256 `7087eb45ea8f2af0667f1aa427b674f50f6aa041ba12d3bfde9e22ac676751d8`
- **Stub dir:** `packets/card01_exp2_census/` (`FROZEN_EXPERIMENT.json`, `results.json`, `results/EMPTY_RESULTS.json`, `COLLECTOR_STUB.md`, `SOURCE_MAP_POINTER.md`, `LEDGER_2026-09-24.md`, `MANIFEST.md`, `README.md`, empty `snapshots/`)
- **Packet ID:** `CARD01-NH-002-EXP2-CENSUS`
- **Charter:** v1.1 sha256 `02272754b01da5b65edd837545e485f4fd4dff2903a7ae1f52d9cb5e616fec5d`
- **Parent cites:** NH-002-H `c31724463d81747702910a2d5296c2fc21d2a1dbc594727b26ac3d894b55ec59` + Amendment A `4e36d0db5728148d5bb4688fd8626eca9907a8933747f85e0bc17ede0ac0936b` + Amendment B `ee6af37cef95f1e468d28e5b06750caaca8b1706ec11ed5cf5cdce460524c2c6` (ACCEPT on file). Census = pre-outcome support for Card 01, not a new trading strategy / not duplicate scoring.

## One knob
`snapshot_cadence` = **weekly** (headline). Comparator level `twice_weekly` not collected unless selected at ACCEPT.  
**Justification:** cadence dominates Collector budget, early-narrow lead time, and disagreement sampling; depth horizon and gate-count threshold are fixed.

## Gate-count threshold (before any pull)
- **About zero:** `n_gate_pass ≤ 2` at a weekly snapshot (fee-verified NH-002-H entry gate as written).
- **Flag:** `RECOMMEND_NARROW_FORECAST_QUALITY_ONLY` if that holds for ≥ 2 consecutive October weeklies among W1–W3 (`2026-10-12/19/26T22:00Z`).
- Fee-unverified → snapshot does not count; illustrative `0.07·p·(1−p)` counts must not fire the flag.

## Collector GET summary (asks only; no pull yet)
Reuse ElectIndex NH-002-H capture (APPROVED_HASH_ONLY); weekly markets+orderbooks for 92 mapped `-D` at W1–W4; hourly orderbooks `2026-11-02T22:00Z`–`2026-11-04T04:00Z` (thin+gap-log if over budget); depends on Amendment B series-fee GETs for gate-count unblock. ≤3 rpm / ≥20 s / Addendum 1.

## Pins / overlap
- Fee: `R1-P1 kalshi_feebook_lab_20260922 @ 22371178cb2663250b4762f328069571c48cb551`
- Rails: `R1-P5 kalshi_rails_lab_20260922 @ 6a28e0d6254327ea4e6451c781bec56215ac6cac`
- Nearest dead card: **FEAT-20260912-001/-002 (F1)** / TEST-20260912-002.
- Overlap: complementary to NH-002-H; none vs Q6-000; none vs C3/Card02 weather.
- No Q6-000 retune; S2/R2-P4 stay gated.

## TBD / next
1. Conductor ACCEPT (or reject) of this freeze.
2. After ACCEPT: Collector capture under Addendum 1; Archivist fee manifest remains blocking for fee-verified gate-count.
3. No NH-002-H parameter change; no live orders.

Existing Cards 01/02 ACK left unchanged (new one-pager preferred).
