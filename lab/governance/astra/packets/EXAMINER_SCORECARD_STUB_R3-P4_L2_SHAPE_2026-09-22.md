# Examiner scorecard STUB — R3-P4-L2-SHAPE-SF1-SF2

**Seat:** Examiner (Kalshi)  
**Packet:** R3-P4-L2-SHAPE-SF1-SF2  
**Subject:** L2 longshot half-spread + depth shape (Dubach SF1/SF2 → Kalshi)  
**Freeze:** `lab/governance/astra/packets/R3-P4_L2_SHAPE_LONGSHOT_DEPTH_FREEZE_KERNEL_2026-09-22.md`  
**Stub dir:** `lab/governance/astra/packets/r3_p4_l2_shape/`  
**Harness:** PR13 squash-merged `main@5eeeaa6bf26d226399448be997748d61faeba43d` (Conductor FYI — keep null)
**Status:** **NOT_SCORED** — SF1/SF2/results/pnl **null** until Clock-admitted L2 panel  
**Authority:** Working Plan v0.1 · `lab/governance/astra/seats/EXAMINER_KALSHI.md`  
**Hard rules:** No invented depth. No promote without freeze + artifacts. No live orders. GET-only L2. Score only after units + Clock admit.

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| Incumbent Q6-`000` | **untouched** (shape panel ≠ allocator) |
| Live promotion / orders | **DENIED** |

**Desk headline:** Stub owned — wait Collector L2 panel + Simulator SF1/SF2 units + Clock admit + Examiner score.

---

## Gates (pre-score checklist)

| Gate | Result | Notes |
|---|---|---|
| Freeze before outcomes | **PASS** | results/pnl null at freeze |
| L2 panel admitted | **PENDING** | Collector GET-only + **Clock admit** |
| SF1/SF2 units complete | **PENDING** | Simulator |
| Reciprocal book = R1-P1 | **REQUIRED** | @ `22371178…` |
| Freshness = R1-P5 | **REQUIRED** | @ `6a28e0d6…` |
| Refuse Lee-Ready | **REQUIRED** | native fields only |
| Dead-overlap named | **PASS at freeze** | low/none vs 000 |
| Completed PnL non-null | **null** | Not run |

---

## Metrics (null)

| Metric | Value |
|---|---|
| `completed_strategy_pnl` | **null** |
| `results` / `pnl` | **null** |
| `sf1_median_half_spread_bps_by_mid_decile` | **null** |
| `sf2_l1_top10_depth_share` | **null** |
| `sf2_kl_vs_uniform_1_10` | **null** |
| `n_books` / `n_snapshots` | **null** until panel |
| `fee_channel_id` | pin required: R1-P1 @ `22371178…` |
| `rails_instrument_id` | pin required: R1-P5 @ `6a28e0d6…` |
| `knob` | `l2_longshot_depth_shape` |

---

## Banned / refused

- No invented PnL or depth  
- No KEEP/ITERATE/KILL until artifacts exist  
- No live orders  
- No Q6-`000` allocator port via this stub  
- No Lee-Ready inference  
- R3 suite refuse: `lab/governance/astra/packets/R3_SUITE_ADVERSARY_REFUSE_BIND_2026-09-22.md`

---

## Examiner ownership ack (2026-09-22 ET)

**Owner:** Examiner (Kalshi). Optional Deep Research stub **owned**. Metrics/pnl **null** until units + Clock admit + Examiner-ready.  
**Refuse binds:** R2-P5 · R1-P1 formula_id · R1-P5 rails · refuse Lee-Ready · no invent PnL/depth · no promotion · no orders · Q6-`000` untouched.  
**Also:** R3-P1 already owned separately (FIXTURE_GAP / auth fee_cost).

**Empty results:** `lab/governance/astra/packets/r3_p4_l2_shape/results.json`  
**Stub READY filed-at:** `2026-09-22T20:15:30-04:00` ET
