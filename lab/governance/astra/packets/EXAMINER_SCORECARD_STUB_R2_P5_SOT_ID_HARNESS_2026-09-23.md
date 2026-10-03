# Examiner scorecard STUB — R2-P5-SOT-ID-HARNESS

**Seat:** Examiner (Kalshi)  
**Packet:** R2-P5-SOT-ID-HARNESS (feature family **SOT-ID**)  
**PR29:** squash-merged **main@6f1e22e1…** (head was `55be4d02…`)  
**Freeze:** sha256 `0424455f062b7c46c7c6161b84fb7b29702719acc45bf6a61b4e8f16c5e26457`  
**Parent SCHEMA_ACCEPT:** sha256 `712e4771bf2783dbee1e4c553194cd2896a468184f2849f24e58c3eb350ff499`  
**Seed ADMIT-1 SoT:** sha256 `1edfa91979ab5dac72e28cc5e2ad5ff08aab414b5574fe115f86fb7d85e2ac4b` · 16 rows  
**Schema:** sha256 `da7f6badd37d52fbd977681924379c3552f0dbfec94729d86ea411fb473ce53c`  
**PIT@CLE identity cite:** sha256 `f5ca19f15940a80476d1590e506951df87df619160b477f1dff06cc3554cb520`  
**Status:** **READY** as scorecard stub · measurement **NOT_SCORED** — units green = **code verify only**; results/pnl null  
**Authority:** Working Plan v0.1 · `lab/governance/astra/seats/EXAMINER_KALSHI.md`

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| Parent SCHEMA_ACCEPT | **untouched** ≠ this harness |
| Incumbent Q6-`000` | **KEEP / untouched** |
| Live promotion / orders | **DENIED** |

**Desk headline:** PR29 stub READY — Clock/Conductor sha verify PASS; metrics null until Clock admit + Examiner-ready.

---

## Arms

| Arm | Slice |
|---|---|
| **R2P5A0** | `sot_pin_match` |
| **R2P5A1** | `holdout_delta_bin` |

---

## Metrics (null on disk)

| Metric | Value |
|---|---|
| `results` / `pnl` | **null** |
| `sot_pin_mismatch_n` | **null** |
| `holdout_mixed_refuse_n` | **null** |
| `delta_kickoff_sec_mode` | **null** |
| `identity_join_ok_n` | **null** |
| `external_odds_invent_refuse_n` | **null** |

---

## Pre-PR HOLD → READY (2026-09-23 ET)

**Prior hold:** `EXAMINER_HOLD_R2_P5_SOT_ID_HARNESS_PRE_PR_2026-09-23.json` — **SUPERSEDED** (authentic freeze/parent/seed/schema/pitcle shas verified on main).  
**Owner:** Examiner (Kalshi). Stub **READY** · **NOT_SCORED**.

### ScorecardPromotionRefused if
1. Invented `sot_pin_mismatch_n` / `holdout_mixed_refuse_n` / `delta_kickoff_sec_mode` / `identity_join_ok_n` / `external_odds_invent_refuse_n`.
2. Invented fills or odds.
3. Any PnL from unit fixtures alone.
4. Parent SCHEMA_ACCEPT treated as this harness scorecard.
5. Fee-honest hedge_complete / mixed clocks / external-odds claims without R2-P5 adversary hygiene pins.
6. Score before Clock admit + Examiner-ready.

### Score gate
Clock admit + Examiner-ready.

**ACK:** `lab/governance/astra/packets/EXAMINER_ACK_R2_P5_SOT_ID_PR29_STUB_READY_NOT_SCORED_2026-09-23.json`  
**Lab:** `kalshi_r2p5_sot_id_lab_20260923/`  
**Also owned NOT_SCORED:** L2-CAT PR28 · R2-P3 PR27  
**Stamped:** 2026-09-23T12:55:30-04:00
