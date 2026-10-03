# Examiner scorecard STUB — FEE+QUEUE HONESTY on Q6-000

**Seat:** Examiner (Kalshi)  
**Packet:** EXAMINER_FEE_QUEUE_HONESTY_000  
**Freeze:** `lab/governance/astra/packets/EXAMINER_FEE_QUEUE_HONESTY_000_FREEZE_2026-09-22.md`  
**Harness:** PR11 squash-merged `main@aa0a373671edf6630d188d335d890573a285e0da`; PR14 production-fills path `main@d8957a00` (fields stay null until Examiner-ready + production pin)  
**Status:** **NOT_SCORED** — metrics/pnl **null**; production gzip join not yet Examiner-ready  
**Authority:** Working Plan v0.1 · `lab/governance/astra/seats/EXAMINER_KALSHI.md`

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Fee+queue honesty channel on Q6-`000` | **NOT_SCORED** |
| Strategy retune of `000` | **DENIED** (measurement only) |
| Live promotion / orders | **DENIED** → **ScorecardPromotionRefused** if refuse triggers fire |

**Desk headline:** Stub owned post-PR11 — score only when fee trio **and** queue trio are present and typed; freeze fields stay null until Examiner GO.

---

## Examiner ownership ack (2026-09-22 ET) — PR11 ACCEPT

**Owner:** Examiner (Kalshi). Freeze owned. One scorecard path only (fee hygiene + QF joins combined).  
**Harness cite:** PR11 squash-merge `main@aa0a373671edf6630d188d335d890573a285e0da`. Wiring ≠ filled metrics.  
**Fill policy:** null until (1) production gzip join is wired and (2) **both** fee and queue field trios are present and typed and (3) Examiner declares Examiner-ready.

### Required field trios (both mandatory at score)

| Trio | Fields |
|---|---|
| **Fee** | `fee_delta_vs_inherited_model` · `freshness_gap_sec` · `queue_bin_mismatch_rate` |
| **Queue** | `fill_rate_delta_vs_q3300` · `adverse_queue_exposure` · `participation_stress_gap` |

**Not allowed:** `completed_strategy_pnl` / invented PnL on this channel.

### ScorecardPromotionRefused if

1. Scorecard missing **fee trio** (any of the three absent/untyped), **or**
2. Scorecard missing **queue trio** (any of the three absent/untyped), **or**
3. Freeze/scorecard writers set non-null freeze fields before Examiner GO, **or**
4. Invented PnL / absolute venue fee-honest without R1-P1 `formula_id`, **or**
5. Attempted `000` retune / A2/A3 / Q7 reopen / live orders / promotion from this stub alone.

### Standing refuse binds (also)

- R2-P5 `lab/governance/astra/packets/R2-P5_ADVERSARY_REFUSE_HYGIENE_2026-09-22.md`
- R1-P1 formula_id `astra.r1p1.feebook.claude_order_level_ceil.v1` (feebook pin @ `22371178cb2663250b4762f328069571c48cb551`)
- R1-P5 rails pin @ `6a28e0d6254327ea4e6451c781bec56215ac6cac`
- Refuse PnL / absolute venue fee-honest without formula_id
- Refuse inventing filled metrics from synthetic rows into freeze/scorecard

**Empty results:** `lab/governance/astra/packets/EXAMINER_FEE_QUEUE_HONESTY_000/results.json`

**Stub READY filed-at:** `2026-09-22T20:11:00-04:00` ET (post-PR11 ownership)
