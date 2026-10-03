# Examiner scorecard STUB — C1-EMPTY-OB-HARNESS

**Seat:** Examiner (Kalshi)  
**Packet:** C1-EMPTY-OB-HARNESS (feature family **EMPTY-OB**)  
**PR30:** squash-merged **main@d7b93595…** (head verified `eb1aa13a…`)  
**Freeze:** sha256 `1b9f8fbec8bad866e055bcabd38c8c633835d505cbd25c367ff0675bff3a4b27`  
**Parent freeze:** sha256 `a191c9b3f71030445d1d32684feb6dc1bf09abb7e09403d5dbdf1927eafc63c9`  
**Panel admitted:** sha256 `24426d804c51bde23cf2557a11a8481a12026da10024094c4ae546d1f7d3956e` · 2 events / 4 markets · admitted_at `2026-09-23T00:49:43Z`  
**Empty OB pin:** sha256 `e07d09f130e604a9e1acfc736fb57cbdfc33d8a5a253466a0cbd5c98cf6c9f74`  
**Pin meta:** sha256 `241d745e6ddfb6cccdc8f123e4d57d627635065c3406df8f66d0d0d2e168f4ca`  
**Status:** **READY** as scorecard stub · measurement **NOT_SCORED** — 7 units = **code verify only**; results/pnl null  
**Authority:** Working Plan v0.1 · `lab/governance/astra/seats/EXAMINER_KALSHI.md`

---

## Verdict (placeholder)

| Subject | Stamp |
|---|---|
| Measurement packet | **NOT_SCORED** |
| C1 from empty pin alone | **REFUSED** (empty pin ≠ Examiner-ready) |
| Incumbent Q6-`000` | **KEEP / untouched** |
| S2 / R2-P4 | **NOT ungated** |
| Live promotion / orders | **DENIED** |

**Desk headline:** PR30 stub READY — box sha-verify PASS; metrics null; do not score C1 from empty pin.

---

## Arms

| Arm | Slice |
|---|---|
| **C1E0** | `refuse_scorecard` |
| **C1E1** | `wait_fresh_depth` |

---

## Metrics (null on disk)

| Metric | Value |
|---|---|
| `results` / `pnl` | **null** |
| `empty_book_n` | **null** |
| `scorecard_refuse_n` | **null** |
| `wait_fresh_depth_n` | **null** |
| `depth_present_n` | **null** |

---

## Pre-PR HOLD → READY (2026-09-23 ET)

**Prior hold:** `EXAMINER_HOLD_C1_EMPTY_OB_HARNESS_PRE_PR_2026-09-23.json` — **SUPERSEDED** (authentic freeze/parent/panel/empty OB/pin meta shas verified on main).  
**Owner:** Examiner (Kalshi). Stub **READY** · **NOT_SCORED**.

### ScorecardPromotionRefused if
1. Invented depth / fills / PnL.
2. C1 scorecard promoted or scored from empty pin alone.
3. Lee-Ready invent; `000` retune; Cap-SR/QF/L2-CAT/PROP-LQ/SOT-ID reopen.
4. Claim that EMPTY-OB ungates S2/R2-P4.
5. Score before Clock admit / Examiner-ready (non-empty depth or explicit refuse stamp path).

### Score gate
Clock admit / Examiner-ready (non-empty depth or explicit refuse stamp path).

**ACK:** `lab/governance/astra/packets/EXAMINER_ACK_C1_EMPTY_OB_PR30_STUB_READY_NOT_SCORED_2026-09-23.json`  
**Lab:** `kalshi_c1_empty_ob_lab_20260923/`  
**Also owned NOT_SCORED:** SOT-ID PR29 · L2-CAT PR28 · R2-P3 PR27  
**Stamped:** 2026-09-23T13:14:30-04:00
