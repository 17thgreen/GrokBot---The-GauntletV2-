# Examiner scorecard STUB — R3-P4-L2-CAT-HARNESS

**Seat:** Examiner (Kalshi)  
**Packet:** R3-P4-L2-CAT-HARNESS (feature family **L2-CAT**)  
**PR28:** squash-merged **main@e54554ff…**  
**Freeze:** sha256 `3fc370d93f0ea42864f7bf482d7f6515254999c76e2fc4477df1273bfcdc051f` (committed as `*_2259.md` filename; bytes match)  
**Parent freeze:** sha256 `4a4e7cc61efcb436955c566edc7a2681603a014725bc79047f9d825392064528`  
**Panel stub:** sha256 `7477e023ab70c59a6739650155ddb9d77077766e3afd80443e540d60b5a86cbb` · 4 events / 6 markets · `admitted_at` **null**  
**Status:** **READY** as scorecard stub · measurement **NOT_SCORED** — 7 units = **code verify only**; results/pnl/SF1/SF2 null  
**Authority:** Working Plan v0.1 · `lab/governance/astra/seats/EXAMINER_KALSHI.md`

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| Parent R3-P4 meas / PR13 | **untouched** ≠ this harness |
| Incumbent Q6-`000` | **KEEP / untouched** |
| Live promotion / orders | **DENIED** |

**Desk headline:** PR28 stub READY — Clock/Conductor sha verify PASS; metrics null until Clock admit + Examiner-ready.

---

## Arms

| Arm | Slice |
|---|---|
| **R3P4C0** | `sports_only` |
| **R3P4C1** | `nonsports_only` |

---

## Metrics (null on disk)

| Metric | Value |
|---|---|
| `results` / `pnl` | **null** |
| `sf1_median_half_spread_bps_by_mid_decile` | **null** |
| `sf2_l1_top10_depth_share` | **null** |
| `sf2_kl_vs_uniform_1_10` | **null** |
| `sports_vs_nonsports_sf_gap` | **null** |
| `n_books` / `n_snapshots` | **null** |

---

## Pre-PR HOLD → READY (2026-09-23 ET)

**Prior hold:** `EXAMINER_HOLD_R3_P4_L2_CAT_HARNESS_PRE_PR_2026-09-23.json` — **SUPERSEDED** (authentic freeze/parent/panel shas verified on main; pin `3fc370d9…` supersedes `e7c6b6d5…`).  
**Owner:** Examiner (Kalshi). Stub **READY** · **NOT_SCORED**.

### ScorecardPromotionRefused if
1. Invented `sf1_median_half_spread_bps_by_mid_decile` / `sf2_l1_top10_depth_share` / `sf2_kl_vs_uniform_1_10` / `sports_vs_nonsports_sf_gap` / `n_books` / `n_snapshots`.
2. Invented fills or depth.
3. Any PnL from unit fixtures alone.
4. Lee-Ready invent; `000` retune; Cap-SR/QF reopen.
5. Parent R3-P4 measurement / PR13 treated as this harness scorecard.
6. Score before Clock admit + Examiner-ready.

### Score gate
Clock admit + Examiner-ready.

**ACK:** `lab/governance/astra/packets/EXAMINER_ACK_R3_P4_L2_CAT_PR28_STUB_READY_NOT_SCORED_2026-09-23.json`  
**Stamped:** 2026-09-23T12:38:30-04:00
