# Examiner scorecard — Q7-B Pass-2 PORTFOLIO-RANK-SIZING Option A — **KEEP**

**Seat:** Examiner (Kalshi)  
**Packet:** Q7-B-PASS2-PORTFOLIO-RANK-SIZING  
**Lab:** `nfl_q7_rehab_p2_rank_sizing_20260923/`  
**Main pin:** `9b8fb184a8f1d556e400188127f1753bf35e571e`  
**Runner (Option A restored):** `9d5ef4c3a65cb6c464c48201324f3ce506ada24e474c9575ed6ebb3a40019f98`  
**READY:** `fdb68eba19ec4a12d248f2e949d39f2e1f0a2a37215d597c7f7e70889f66c980`  
**Conductor SCORE kick:** `669fedc4544b9d9aef15220e7e5c144a9c1194f9b81b0d27f690dfbd32862d47`  
**HOLD cleared:** `6874c6b6a770cc2312701ab3f0761b7f4b8573195665bf2e61844c32e660caea`  
**Digest:** `5ee898c1e3c1f3336706a71afcb252c5e9f3fd56c53286cd2e38750575e8c1d3`  
**Scorecard template:** v1.2  
**Status:** **SCORED** · Simulator `selection_status=NOT_SCORED` honored (arithmetic_preview ≠ SCORED)

---

## Gates (pre-score re-diff)

| Gate | Result |
|---|---|
| Runner sha == restored pin 9d5ef4c3… | **PASS** |
| `parent_pin_mismatches()` + `FAILED_PARENT_CODE_PIN_MISMATCH` present; H9 deferred gone | **PASS** |
| Parent SOURCE_PINS re-verify | **PASS 33/33** · `waive=false` · pins `5ee602ba…` |
| Positive controls (B0≡parent B, D≡parent D) | **PASS** · 8 comparisons |
| 12/12 cells COMPLETE · all_flat · non-null PnL · digest match | **PASS** |
| Soften 95%-of-D / invent PnL / Q6-`000` / live / score attempt2 ungated | **DENIED** |

---

## Verdict

| Subject | Stamp |
|---|---|
| Rehab packet Q7-B-PASS2 Option A tape walk | **KEEP** |
| B2 shadow candidate vs frozen bar | **B2_SHADOW_CANDIDATE** |
| Fallback shadow | **`000` remains** until Conductor promote |
| Live promotion | **DENIED** (`live_promotion=false`) |
| Counted as experiment PnL promote | **false** |

**Desk headline:** Pass-2 `portfolio_rank_sizing` clears the frozen selection bar on all four stresses under the Option A restored H9 gate. B2 > B0 and B2 ≥ 95% of D on every stress (B2 exceeds D on all four). Primary weeks and inventory ≤ 1.25× B0 pass; unresolved = 0. KEEP as B2 shadow candidate only.

**Evidence tags:** [V][H][A][U]

**Independent Examiner `selection.select`:** `status=B2_SHADOW_CANDIDATE` · `reason=bar_passed_on_supplied_rows` · `candidate_arm=B2` · `live_promotion=false` · `fallback_shadow_candidate=000`

---

## Frozen bar (selection.py — not softened)

Apply only if all 12 flat with non-null `completed_strategy_pnl` and unresolved < 0.009:

1. Every stress: **B2 > B0**
2. Every stress: **D > 0**
3. Every stress: **B2 ≥ 0.95 × D**
4. Every stress: B2 `unhedged_contract_hours` ≤ 1.25 × B0
5. Primary `q3300_d0.25`: B2 week1 > B0 week1 **and** B2 week2 > B0 week2

---

## Fee-honest PnL (`completed_strategy_pnl`)

**Fee honesty label:** fee-honest under standing feebook `formula_id=astra.r1p1.feebook.claude_order_level_ceil.v1` (feebook.py sha `eaf5aac7…` matches freeze). Archivist fee/account-version manifest still pending — common_scorecard net_pnl columns remain null per template v1.2.

| Stress | B0 | B2 | D | B2/D | B2>B0 | B2≥95%D | inv B2/B0 |
|---|---:|---:|---:|---:|:---:|:---:|---:|
| q3300_d0.25 | 290.9934 | 354.3310 | 345.2444 | 102.63% | **pass** | **pass** | 0.9493 |
| q3300_d5 | 291.1962 | 353.8934 | 345.4174 | 102.45% | **pass** | **pass** | 0.9509 |
| q10000_d0.25 | 45.5310 | 90.4451 | 75.9049 | 119.16% | **pass** | **pass** | 0.9064 |
| q10000_d5 | 37.8335 | 79.0758 | 69.0574 | 114.51% | **pass** | **pass** | 0.9084 |

Primary weeks `q3300_d0.25`: B2 week1 219.5698 > B0 179.1492 · B2 week2 134.7612 > B0 111.8442 (**pass** both).

Unresolved contracts: 0.0 on all 12 cells (**pass** < 0.009).

---

## Per-game (B2−B0) on `q3300_d0.25` (reporting)

Metric: per-game `cashflow` delta. n=31 · sum Δ = +63.3376 (matches B2−B0 PnL).

- Top-1 positive delta: `KXNFLGAME-26SEP20MINCHI` Δ=+20.6269 · share of positive delta = **32.56%** (flag >50%: **false**)
- HHI on |Δ| (0–1 scale): **0.2147**

---

## Addendum A G_ref (reporting only)

G_ref=0.0746 · 0.5·G_ref=0.0373 · G_best(mean max(0,gap_B2))=**0.0** (B2 > D all stresses). Not a Pass-2 freeze KEEP/KILL gate.

---

## Caveats

1. P1 runner baseline `c7439738…` is **INFERRED** (not pinned).
2. Attempt-1 runner `c6e37341…` is **INFERRED**; attempt1 INFRA/VOID — `results_attempt1_brokenpool_20260923/` never scored.
3. Attempt-2 ungated hold `results_attempt2_hold_pre_optionA_20260924/` **NOT** scored.
4. AMEND-1 `54c9ba50…` remains **REJECTED_SUPERSEDED_BY_OPTION_A**.
5. Calibration **N/A** (no probabilities).

---

## ScorecardPromotionRefused if

1. Softened or rewrote the 95%-of-D bar after peek.
2. Invented fills / PnL / depth.
3. Waived parent SOURCE_PINS, positive-control, or H9 gate.
4. Q6-`000` retune / treated arithmetic_preview as KEEP without Examiner stamp.
5. Live orders / counted this as promote PnL.
6. Scored ungated attempt2 hold or attempt1 brokenpool as Option A.

**SCORE JSON:** `lab/governance/astra/packets/EXAMINER_SCORE_Q7_B_PASS2_OPTION_A_TAPE_WALK_2026-09-25.json`  
**Stamped:** 2026-09-25T00:32:34-04:00
