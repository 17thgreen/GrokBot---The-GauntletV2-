# Examiner scorecard STUB — Cap-SR SOFT-BLENDED-RESERVES-000

**Seat:** Examiner (Kalshi)
**Packet:** SOFT-BLENDED-RESERVES-000 (feature family **Cap-SR**)
**Lab:** `kalshi_soft_blended_reserves_000_lab_20260923`
**PR20:** merged **main@45863037**
**Freeze:** `lab/governance/astra/packets/SOFT_BLENDED_RESERVES_000_FREEZE_2026-09-23.md` · packet sha `1f263dec7d7810515c3e32c13f3c5eca4344c4951db762a88ea01a8dfde7b1b3`
**Stub dir:** `lab/governance/astra/packets/SOFT_BLENDED_RESERVES_000/`
**Status:** **NOT_SCORED** — 32/32 unit = **code verify only**
**Authority:** Working Plan v0.1 · `lab/governance/astra/seats/EXAMINER_KALSHI.md`

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| Incumbent Q6-`000` | **KEEP / untouched** (no retune via Cap-SR) |
| Live promotion / orders | **DENIED** |

---

## Metrics (null)

| Metric | Value |
|---|---|
| `results` / `pnl` | **null** |
| `borrow_count_delta_vs_fifo` | **null** |
| `blend_utilization_gap` | **null** |
| `soft_breach_or_blend_rate` | **null** |

---

## Arms (soft_policy only)

| Arm | Policy |
|---|---|
| SR0 | `borrow_unused_event_id_FIFO` |
| SR1 | `borrow_unused_proportional` |
| SR2 | `soft_blend_pool_fraction_0_5` |

---

## Examiner ownership ack (2026-09-23 ET) — PR20 merged

**Owner:** Examiner (Kalshi). Stub **READY** as **NOT_SCORED**.
**Refuse:** invent / KEEP/ITERATE/KILL / promotion from 32/32 units alone → ScorecardPromotionRefused.
**Score gate:** Examiner-ready declaration on a **real run** (not unit verify). No invent from merge. No `000` retune. No orders.
**Pins:** fee R1-P1 @`22371178cb2663250b4762f328069571c48cb551` · rails R1-P5 @`6a28e0d6254327ea4e6451c781bec56215ac6cac` · parent capital @`ce4671b8`
**Empty results:** `SOFT_BLENDED_RESERVES_000/EMPTY_RESULTS.json`
**Stamped-at:** `2026-09-23T10:36:49-04:00` ET


---

## Orthogonal note — Cap-SR-FX effects path (2026-09-23 ET)

**CAP-SR-EFFECTS-PATH-000** freeze sha `cd08a93af2659c36f83cd1b9ffc3174364cc767efc374a4e0669e128f6a29074` is a **separate** Cap-SR-FX packet (FX0/FX1 fixture-stress). Do **not** re-score this PR20 soft_policy packet as the effects-path outcome. Effects-path owns its own stub: `EXAMINER_SCORECARD_STUB_CAP_SR_EFFECTS_PATH_000_2026-09-23.md` (HOLD until PR lands).
**Noted-at:** `2026-09-23T10:38:10-04:00` ET
