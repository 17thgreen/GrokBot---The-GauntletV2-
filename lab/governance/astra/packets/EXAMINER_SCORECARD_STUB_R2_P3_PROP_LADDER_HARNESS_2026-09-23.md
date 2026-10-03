# Examiner scorecard STUB — R2-P3-KXNFLPASSYDS-PROP-LADDER-HARNESS

**Seat:** Examiner (Kalshi)  
**Packet:** R2-P3-KXNFLPASSYDS-PROP-LADDER-HARNESS (feature family **PROP-LQ**)  
**PR27:** squash-merged **main@3b0d1429…**  
**Freeze:** sha256 `f8335eb0080cb1f82b1fad512509749134dd0e6e41ed85795347c3476796e87a`  
**Parent freeze:** sha256 `a30108f658359590e170c73ea00d1a1f0852d5751cb15c9f2a9c6389f4dd3eaa`  
**Panel stub:** sha256 `70e879e8738d033f392d821849dee3537af3e7b8a916670779d238f78ce098be` · 6 events · `admitted_at` **null**  
**Status:** **READY** as scorecard stub · measurement **NOT_SCORED** — 8 units = **code verify only**; results/pnl null  
**Authority:** Working Plan v0.1 · `lab/governance/astra/seats/EXAMINER_KALSHI.md`

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| Incumbent Q6-`000` | **KEEP / untouched** |
| Live promotion / orders | **DENIED** |

**Desk headline:** PR27 stub READY — Clock/Conductor sha verify PASS; metrics null until Clock admit + Examiner-ready.

---

## Arms

| Arm | Slice |
|---|---|
| **R2P3A0** | Isotonic residual; Lee-Ready **REFUSED** |
| **R2P3A1** | Logit-monotone residual |

---

## Metrics (null on disk)

| Metric | Value |
|---|---|
| `results` / `pnl` | **null** |
| `cross_strike_residual_rms` | **null** |
| `latent_fit_fragmentation` | **null** |
| `maker_credit_floor_zero_n` | **null** |
| `fresh_strike_n` | **null** |
| `settled_join_n` | **null** |

---

## Pre-PR HOLD → READY (2026-09-23 ET)

**Prior hold:** `EXAMINER_HOLD_R2_P3_PROP_LADDER_HARNESS_PRE_PR_2026-09-23.json` — **SUPERSEDED** (authentic freeze/parent/panel shas verified on main).  
**Owner:** Examiner (Kalshi). Stub **READY** · **NOT_SCORED**.

### ScorecardPromotionRefused if
1. Invented `cross_strike_residual_rms` / `latent_fit_fragmentation` / `maker_credit_floor_zero_n` / `fresh_strike_n` / `settled_join_n`.
2. Invented fills.
3. ATL@GB enrichment.
4. Lee-Ready invent.
5. Any PnL from unit fixtures alone.
6. Parent R2-P3 measurement stub treated as this harness scorecard.
7. Score before Clock admit + settled join N>0 + Examiner-ready.

### Score gate
Clock admit + settled join N>0 + Examiner-ready.

**ACK:** `lab/governance/astra/packets/EXAMINER_ACK_R2_P3_PR27_STUB_READY_NOT_SCORED_2026-09-23.json`  
**Stamped:** 2026-09-23T12:19:30-04:00
