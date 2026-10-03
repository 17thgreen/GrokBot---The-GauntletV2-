# Examiner scorecard STUB — R3-P1-FEE-COST-VS-MODEL

**Seat:** Examiner (Kalshi)  
**Packet:** R3-P1-FEE-COST-VS-MODEL  
**Subject:** Venue `fee_cost` vs R1-P1 model delta  
**Freeze:** `lab/governance/astra/packets/R3-P1_FEE_COST_VS_MODEL_FREEZE_KERNEL_2026-09-22.md`  
**Stub dir:** `lab/governance/astra/packets/r3_p1_fee_cost/`  
**Fixture gap:** `lab/governance/astra/packets/r3_p1_fee_cost/R3-P1_FIXTURE_GAP_2026-09-22.md`  
**Harness:** PR12 squash-merged `main@5f45bf3741de1fc9e96f5304f05ce9f2ddbe91e4` (Conductor ASSIGN OWN 2026-09-22 ET)  
**Status:** **NOT_SCORED** — `fee_model_minus_venue_delta` / `results` / `pnl` **null** until authenticated `fee_cost` fills exist  
**Authority:** Working Plan v0.1 · `lab/governance/astra/seats/EXAMINER_KALSHI.md`

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| Incumbent Q6-`000` | **untouched** (no retune) |
| Live promotion / orders | **DENIED** |

**Desk headline:** Stub owned post-PR12 — blocked on FIXTURE_GAP / demo keys until auth `fee_cost` fills land.

---

## Gates (pre-score checklist)

| Gate | Result | Notes |
|---|---|---|
| Freeze before outcomes | **PASS** | results/pnl null at freeze |
| Auth fill fixtures with `fee_cost` | **BLOCKED** | Collector FIXTURE_GAP; demo keys / Mechanic path |
| Units / refuse-flag fixtures | **PENDING** | Simulator after fixtures |
| Fee model = R1-P1 pin | **REQUIRED** | @ `22371178cb2663250b4762f328069571c48cb551` · `formula_id` `astra.r1p1.feebook.claude_order_level_ceil.v1` |
| Prefer venue when non-null | **REQUIRED** | Accounting instrument — not strategy |
| Dead-overlap named | **PASS at freeze** | complementary to Variants 000 honesty |
| Completed PnL non-null | **null** | Not run |

---

## Metrics (null — mandatory until auth fee_cost fills)

| Metric | Value |
|---|---|
| `fee_model_minus_venue_delta` | **null** |
| `results` | **null** |
| `pnl` / `completed_strategy_pnl` | **null** |
| `n_fills_venue_present` | **null** |
| `n_fills_model_only` | **null** |
| `refuse_flag_unit_pass` | **null** |
| `fee_channel_id` | pin required: R1-P1 @ `22371178…` |
| `knob` | `fee_cost_vs_model_honesty` |

---

## Examiner ownership ack (2026-09-22 ET) — PR12 OWN

**Owner:** Examiner (Kalshi). Stub accepted as **NOT_SCORED**.  
**Harness cite:** PR12 squash-merge `main@5f45bf3741de1fc9e96f5304f05ce9f2ddbe91e4`.

### Refuse binds

1. **Null until auth fills:** `fee_model_minus_venue_delta` / `results` / `pnl` stay **null** until authenticated `fee_cost` fills exist (demo keys / FIXTURE_GAP).  
2. **Refuse model-only completed net** when `fee_cost` was available → refuse / ScorecardPromotionRefused.  
3. **No invented PnL** (including synthetic `fee_cost` rows).  
4. No KEEP/ITERATE/KILL until artifacts exist.  
5. No live orders as evidence.  
6. No Q6-`000` retune via this stub.  
7. No bacchus 15m strategy port / author PnL as Astra EV.  
8. Standing: R2-P5 hygiene · R1-P1 `formula_id` · R1-P5 rails when rails claims appear.

**Empty results:** `lab/governance/astra/packets/r3_p1_fee_cost/results.json`

**Stub READY filed-at:** `2026-09-22T20:14:00-04:00` ET (post-PR12 ownership)
