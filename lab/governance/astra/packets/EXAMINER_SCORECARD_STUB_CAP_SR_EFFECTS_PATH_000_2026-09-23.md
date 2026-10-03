# Examiner scorecard STUB — CAP-SR-EFFECTS-PATH-000

**Seat:** Examiner (Kalshi)
**Packet:** CAP-SR-EFFECTS-PATH-000 (feature family **Cap-SR-FX**)
**Lab:** `kalshi_cap_sr_effects_000_lab_20260923/`
**PR24:** squash-merged **main@79347f0e…** (head was `d9b2da26…` · base was `cfd5f95a…`)
**Freeze:** `lab/governance/astra/packets/CAP_SR_EFFECTS_PATH_000_FREEZE_2026-09-23.md` sha256 `cd08a93af2659c36f83cd1b9ffc3174364cc767efc374a4e0669e128f6a29074`
**Stub dir:** `lab/governance/astra/packets/CAP_SR_EFFECTS_PATH_000/`
**Parent Cap-SR:** soft_policy SR0/SR1/SR2 **FIXED** import from Cap-SR PR20@`45863037` — parent Cap-SR lab **untouched**; do **not** re-score PR20 soft_policy as this packet’s outcome
**Status:** **READY** as scorecard stub · measurement **NOT_SCORED** — 11 unit tests = **code verify only**; FX0 used schema stand-in (indexed gzip absent) — **NOT** Examiner score
**Authority:** Working Plan v0.1 · `lab/governance/astra/seats/EXAMINER_KALSHI.md`

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| Cap-SR PR20 soft_policy | **orthogonal / not this outcome** |
| Incumbent Q6-`000` | **KEEP / untouched** |
| Live promotion / orders | **DENIED** |

**Desk headline:** PR24 stub READY — fixture-stress FX0/FX1 only; metrics null until real Examiner join.

---

## Arms (fixture-stress knob only)

| Arm | Fixture stress |
|---|---|
| FX0 | `q3300_d0.25` (schema stand-in this merge — indexed gzip absent) |
| FX1 | `synthetic_borrow_stress` (unit/fixture-stress only) |

Soft policies SR0/SR1/SR2 are **fixed imports** from Cap-SR — not re-armed here.

---

## Metrics (null on disk)

| Metric | Value |
|---|---|
| `results` / `pnl` | **null** |
| `borrow_count_delta_vs_fifo` | **null** |
| `blend_utilization_gap` | **null** |
| `soft_breach_or_blend_rate` | **null** |
| `effects_path_fixture_id` | **null** |

---

## Pre-PR HOLD → READY (2026-09-23 ET)

**Prior hold:** `EXAMINER_HOLD_CAP_SR_EFFECTS_PATH_000_PRE_PR_2026-09-23.json` — **SUPERSEDED** by this READY stamp.
**Owner:** Examiner (Kalshi). Stub **READY** · **NOT_SCORED**.

### ScorecardPromotionRefused if
1. Invented `borrow_count_delta_vs_fifo` / `blend_utilization_gap` / `soft_breach_or_blend_rate` from unit fixtures or FX0 schema stand-in.
2. Any PnL from unit fixtures / synthetic FX1 alone.
3. Soft_policy re-scored as **new arms** (SR0/SR1/SR2 stay fixed Cap-SR imports).
4. FX0/FX1 treated as anything other than **fixture-stress**.
5. Cap-SR PR20 soft_policy re-scored as this packet’s outcome.
6. KEEP/ITERATE/KILL / promotion / `000` retune / live orders before Examiner-ready.

**Score gate:** Clock admit + settled join N>0 + Examiner-ready declaration — then score. `results`/`pnl` stay null until real Examiner join.
**Empty results:** `CAP_SR_EFFECTS_PATH_000/EMPTY_RESULTS.json`
**Stub READY (PR24) stamped-at:** `2026-09-23T10:51:45-04:00` ET
