# Examiner scorecard STUB — R3-P4-L2-SF-HARNESS

**Seat:** Examiner (Kalshi)  
**Packet:** R3-P4-L2-SF-HARNESS (feature family **L2-SF**)  
**PR31:** squash-merged **main@ead2cb41…** (head verified `23fdd8d0…`)  
**Freeze:** sha256 `f00425261f085aef90e93b186810a0248165273f8bb923ef3597940a9e8345de`  
**Parent freeze:** sha256 `4a4e7cc61efcb436955c566edc7a2681603a014725bc79047f9d825392064528`  
**Panel stub:** sha256 `7477e023ab70c59a6739650155ddb9d77077766e3afd80443e540d60b5a86cbb` · 4 events / 6 markets · `admitted_at` **null**  
**ACCEPT stamp:** `4ebf316f…`  
**Status:** **READY** as scorecard stub · measurement **NOT_SCORED** — 7 units = **code verify only**; results/pnl/SF metrics null  
**Authority:** Working Plan v0.1 · `lab/governance/astra/seats/EXAMINER_KALSHI.md`

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| In-memory SF without Clock admit | **REFUSED** |
| L2-CAT / PR13 base | **untouched** (category not an arm) |
| Incumbent Q6-`000` | **KEEP / untouched** |
| S2 / R2-P4 | **NOT ungated** |
| Live promotion / orders | **DENIED** |

**Desk headline:** PR31 stub READY — box sha-verify PASS; SF metrics null until Clock admit + Examiner-ready.

---

## Arms

| Arm | Slice |
|---|---|
| **R3P4S0** | `sf1_half_spread` |
| **R3P4S1** | `sf2_depth_kl` |

Category slice is **not** an arm (L2-CAT sibling — do not reopen).

---

## Metrics (null on disk)

| Metric | Value |
|---|---|
| `results` / `pnl` | **null** |
| `sf1_median_half_spread_bps_by_mid_decile` | **null** |
| `sf2_l1_top10_depth_share` | **null** |
| `sf2_kl_vs_uniform_1_10` | **null** |
| `n_books` / `n_snapshots` | **null** |

---

## Pre-PR HOLD → READY (2026-09-23 ET)

**Prior hold:** `EXAMINER_HOLD_R3_P4_L2_SF_HARNESS_PRE_PR_2026-09-23.json` — **SUPERSEDED** (authentic freeze/parent/panel + OB fixtures + ACCEPT stamp verified on main).  
**Owner:** Examiner (Kalshi). Stub **READY** · **NOT_SCORED**.

### ScorecardPromotionRefused if
1. Invented depth / fills / PnL.
2. In-memory SF written into scorecard without Clock admit.
3. Lee-Ready invent; L2-CAT reopen; PR13 dual-edit into PnL.
4. Cap-SR / QF / PROP-LQ / SOT-ID / EMPTY-OB reopen; `000` retune.
5. Claim that L2-SF ungates S2/R2-P4.
6. Score before Clock admit + Examiner-ready.

### Score gate
Clock admit + Examiner-ready.

**ACK:** `lab/governance/astra/packets/EXAMINER_ACK_R3_P4_L2_SF_PR31_STUB_READY_NOT_SCORED_2026-09-23.json`  
**Lab:** `kalshi_r3p4_l2_sf_lab_20260923/`  
**Also owned NOT_SCORED:** EMPTY-OB PR30 · SOT-ID PR29 · L2-CAT PR28 · R2-P3 PR27  
**Stamped:** 2026-09-23T13:33:30-04:00
