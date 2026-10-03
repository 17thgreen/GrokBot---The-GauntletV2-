# Examiner scorecard STUB — C5-KXBTC15M-MEAS

**Seat:** Examiner (Kalshi)  
**Packet:** C5-KXBTC15M-MEAS  
**Series / subject:** `KXBTC15M`  
**Freeze:** `lab/governance/astra/packets/C5_KXBTC15M_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md`  
**Stub dir:** `lab/governance/astra/packets/scout_c5_kxbtc15m/`  
**Panel stub:** `lab/governance/astra/packets/C5_KXBTC15M_PANEL_STUB_2026-09-22.json` (READY; `admitted_at` **null**; `2026-09-22.c5-kxbtc15m-v0`)  
**Panel status:** `lab/governance/astra/packets/C5_KXBTC15M_PANEL_STUB_STATUS_2026-09-22.md`
**Status:** **NOT_SCORED** — panel stub READY but not admitted; `results`/`pnl` **null** until Clock admit + units  
**Authority:** Working Plan v0.1 · `lab/governance/astra/seats/EXAMINER_KALSHI.md`  
**Hard rules:** No invented rates. No promote without freeze + artifacts. No live orders. No dual-hat with build seats. Score only after units + Clock admit.

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| Incumbent Q6-`000` | **untouched** (no bakeoff scored yet) |
| Live promotion / orders | **DENIED** |

**Desk headline:** 15m crypto fee/queue honesty stress — not live crypto trading; no bacchus/kxeth15m strategy port.

---

## Gates (pre-score checklist)

| Gate | Result | Notes |
|---|---|---|
| Freeze before outcomes | **PASS** | results/pnl null at freeze |
| Panel admitted | **PENDING** | Collector + **Clock admit** required |
| Units / fixtures complete | **PENDING** | Simulator |
| Fee-honest channel = R1-P1 pin | **REQUIRED** | Forbid inherited Q7/Q6 fee literals |
| Rails labels = R1-P5 pin | **REQUIRED** | Instrument only |
| Completed PnL non-null | **null** | Not run |

---

## Metrics (null)

| Metric | Value |
|---|---|
| `completed_strategy_pnl` | **null** |
| `results` / `pnl` | **null** |
| `pct_gain` | **null** |
| `fee_channel_id` | pin required at score: R1-P1 @ `22371178…` |
| `rails_instrument_id` | pin required at score: R1-P5 @ `6a28e0d6…` |
| `knob` | `kxbtc15m_fee_queue_honesty_stress` |

---

## Banned / refused

- No invented PnL or annualization  
- No KEEP/ITERATE/KILL until artifacts exist  
- No live orders  
- No Q6-`000` retune via this stub  
- No live crypto trading
- No bacchus / kxeth15m strategy port or author PnL as Astra EV
- Completed-profit / live-trading claim without feebook → refuse

---

## Examiner ownership ack (2026-09-22 ET) — CASH-COW FREEZE ACCEPT

**Owner:** Examiner (Kalshi). Stub accepted as **NOT_SCORED**; `results`/`pnl` remain **null** until units + Clock admit + Examiner-ready.
**Score gate:** Score only after Simulator units complete **and** Clock admit. No invent.
**Refuse binds acknowledged:**
- R2-P5 `lab/governance/astra/packets/R2-P5_ADVERSARY_REFUSE_HYGIENE_2026-09-22.md`
- R1-P1 formula_id `astra.r1p1.feebook.claude_order_level_ceil.v1` (feebook @ `22371178cb2663250b4762f328069571c48cb551`)
- R1-P5 rails @ `6a28e0d6254327ea4e6451c781bec56215ac6cac`
- No invented PnL · no KEEP/ITERATE/KILL until artifacts · no promotion · no orders · Q6-`000` untouched

**Empty results:** `lab/governance/astra/packets/scout_c5_kxbtc15m/results.json`  
**Stub READY filed-at:** `2026-09-22T20:15:30-04:00` ET

---

## Panel stub READY confirm (2026-09-22 ET)

**Confirm:** NOT_SCORED stub **owned**. Panel stub READY (`PANEL_SCHEMA_STUB_SEED`); `admitted_at` **null**.  
**results / pnl:** remain **null** until Clock admit + Simulator units + Examiner-ready.  
**Refuse:** any non-null results/pnl / KEEP/ITERATE/KILL / promotion / invent from panel stub alone → ScorecardPromotionRefused.  
**Also noted:** Clock ADMIT REFUSED on R3-P3 keeps that packet's N=0 refuse binding (orthogonal).

**Confirm stamped-at:** `2026-09-22T20:41:51-04:00` ET


---

---

## PR21 honesty harness merged — still NOT_SCORED (2026-09-23 ET)

**Harness:** `kalshi_c5_kxbtc15m_honesty_lab_20260923` · **PR21** merged **main@ee69245a**
**Harness freeze:** `C5_KXBTC15M_HONESTY_HARNESS_FREEZE_2026-09-23.md` sha `23b908af6e9a7799c9bbdac04b27e683dfccd0c0c25d691df84ff715202d3cab`
**Units:** 8/8 = **code verify only**
**Panel `admitted_at`:** still **null**

**Examiner status:** **NOT_SCORED**. Stub READY owned.
**results / pnl / freshness / queue / fee_delta fields:** **null**.
**Refuse:** invent / KEEP/ITERATE/KILL / promotion from units alone → ScorecardPromotionRefused.
**Score gate:** Clock admit + Examiner-ready declaration.
**Stamped-at:** `2026-09-23T10:36:49-04:00` ET
