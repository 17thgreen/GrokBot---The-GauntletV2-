# Adversary hygiene — R2-P5 scorecard refuse rules
**Date:** 2026-09-22 (America/New_York)  
**Packet:** R2-P5 (SCHEMA_ACCEPTED / stub)  
**Owner:** The Adversary · **Reviewer:** Conductor  
**Cite:** `R2-P5_SCHEMA_STUB_2026-09-22.md` · `R2-P5_KICKOFF_ADVERSE_SCHEMA_STUB_2026-09-22.json` · seed `R2-P5_SEED_INSTANCE_ADMIT1_SOT_ONLY_2026-09-22.json` · `briefs/R1-P3-ADVERSE_2026-09-22.md`  
**Stance:** Wire refuse rules. No verdict change on Q6-000. No orders. No invented edge/PnL.

---

## Direct answer

**Yes — refuse.**

Adversary (and Examiner scorecard refuse) **must refuse** a scorecard that claims **fee-honest `hedge_complete`** when either:

1. **No feebook pin** — `hedge_complete_flag` is non-null but `fee_model_ref` is missing, null, or ≠ pinned R1-P1 `examiner_formula_id` (`astra.r1p1.feebook.claude_order_level_ceil.v1` per stub), **or**  
2. **Mixed clocks** — kickoff / T−7d / window math mixes holdout and occurrence clocks **without** `window_clock_source=holdout_mixed` (and an explicit audit of which fields used which clock).

Label: **measurement / provenance refuse** — not a strategy kill, not a Q6-000 reopen.

---

## Refuse matrix (short)

| Claim on scorecard | Condition | Adversary stamp |
|---|---|---|
| Fee-honest `hedge_complete` | `fee_model_ref` absent / wrong / not R1-P1 pin | **REFUSE** |
| Fee-honest `hedge_complete` | R1-P1 Examiner tests not closed | **REFUSE** absolute “venue fee-honest”; allow only **modeled under stated `formula_id`** if pin present |
| Any hedge/edge lock EV | Mixed holdout+occurrence clocks and `window_clock_source` ≠ `holdout_mixed` | **REFUSE** |
| Edge / hedge / odds-age as evidence | `external_odds_present=false` or R1-P3 four-core null (seed state) | **measurement_gap** — refuse completed-edge / lock-EV claims |
| Shin/proportional silent | `de_vig_method` null while edges non-null | **REFUSE** (R1-P3 freeze note) |
| Promote / live | Any | **DENIED** (out of scope) |

Seed check (this stub): 16 rows · `external_odds_present=false` · all four-core null · `window_clock_source=kalshi_occurrence` · SoT-only. Correct: **no** hedge/edge claims possible yet. Inventing filled adverse columns here would itself be refuse grounds.

---

## Alignment with schema stub

Stub already hard-rules: refuse mixing clocks without `holdout_mixed`; `hedge_complete_flag` fee-aware via R1-P1 when non-null; missing four-core → measurement gap. This note **binds Adversary refuse** to those rules for Examiner scorecards and does not add strategy content.

Gap to watch: JSON Schema `allOf` requires `fee_model_ref` when hedge is boolean, but does not yet encode “must equal pinned formula_id” or “refuse fee-honest wording without closed P1 tests.” Scorecard language must carry that; do not rely on schema alone.

---

## Explicit non-actions

- No change to Q6-000 KEEP / Q7 KILL_B.  
- No ADMIT-1 re-admit / recorder touch.  
- No orders.

**Artifact:** `lab/governance/astra/packets/R2-P5_ADVERSARY_REFUSE_HYGIENE_2026-09-22.md`
