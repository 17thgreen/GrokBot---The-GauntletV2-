# Examiner scorecard STUB — S5-KXMVECROSSCATEGORY-FILLLEGS-HARNESS

**Seat:** Examiner (Kalshi)
**Packet:** S5-KXMVECROSSCATEGORY-FILLLEGS-HARNESS (feature family **MVE-FL**)
**Lab (expected):** `kalshi_s5_mve_filllegs_lab_20260923`
**Freeze:** `lab/governance/astra/packets/S5_KXMVECROSSCATEGORY_FILLLEGS_HARNESS_FREEZE_2026-09-23.md` sha256 `8a118e6f1fdc8c22c6e559f395667aedffa5d270d067e39b6ae3ee24b2046d16`
**Stub dir:** `lab/governance/astra/packets/S5_KXMVECROSSCATEGORY_FILLLEGS_HARNESS/`
**Parent measurement:** `EXAMINER_SCORECARD_STUB_S5_KXMVECROSSCATEGORY_2026-09-22.md` — **orthogonal**; do **not** treat parent S5 measurement stub as this harness scorecard
**Panel:** `2026-09-22.s5-kxmvecrosscategory-v0` · `admitted_at` **null**
**Status:** **HOLD / NOT_SCORED** — pre-PR; EMPTY_RESULTS until PR lands; Examiner stub **READY** stamps only when PR lands
**Authority:** Working Plan v0.1 · `lab/governance/astra/seats/EXAMINER_KALSHI.md`

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Harness packet | **NOT_SCORED** (pre-PR hold) |
| Parent S5-MEAS stub | **not this scorecard** |
| Incumbent Q6-`000` | **untouched** |
| R1-P4 strategy | **CLOSED** (not opened) |
| Live promotion / orders | **DENIED** |

---

## Arms (leg_mid_source only)

| Arm | Source |
|---|---|
| S5L0 | `tob_1m` |
| S5L1 | `synthetic_leg_product` (unit/fixture only) |

---

## Metrics (null)

| Metric | Value |
|---|---|
| `results` / `pnl` | **null** |
| `fill_vs_legs_mid_gap` | **null** |
| `combo_fee_delta_vs_feebook` | **null** |
| `legs_join_rate` | **null** |
| `freshness_gap_sec` | **null** |

---

## Examiner HOLD (2026-09-23 ET) — Conductor pre-PR

**Owner:** Examiner (Kalshi). Freeze ACCEPT with refuse binds locked. Stub READY when PR lands (**NOT_SCORED** only).

### ScorecardPromotionRefused if
1. Invented `fill_vs_legs_mid_gap` / `combo_fee_delta_vs_feebook` / `legs_join_rate` / `freshness_gap_sec`.
2. Invented fills when tape empty.
3. Any **RFQ** path / `/communications` use.
4. Any **R1-P4** strategy score opened via this harness.
5. PnL from unit fixtures / S5L1 synthetic alone.
6. Parent S5 measurement stub treated as this harness scorecard.
7. KEEP/ITERATE/KILL / promotion / `000` retune / live orders before Examiner-ready.

**Score gate (post-PR READY):** Clock admit + settled join N>0 + Examiner-ready declaration.
**Empty results:** `S5_KXMVECROSSCATEGORY_FILLLEGS_HARNESS/EMPTY_RESULTS.json`
**Hold stamped-at:** `2026-09-23T10:53:25-04:00` ET
