# FEATURE_LEARNED_PT — named card class (packet §1.4)

**Document:** `archive/templates/FEATURE_LEARNED_PT.md`  
**Authority:** Governor Packet 2026-09-13 §1.4  
**Date:** 2026-09-13  
**Classification:** Feature **template / run-configuration class** — **not** an OS principle that every domain must learn weights  
**RETROACTIVE:** NO  
**Baseline:** `gauntlet-v2.0-alpha` unchanged  

**Not a general fitting license.** Do not write “training is legitimate” into AMD-001 or the Refiner charter as a blanket. Peeking a fit onto a dead algebraic card is **BAN**.

---

## Map-class fit rules (packet §1.4)

| Map class | Fit rule |
|-----------|----------|
| Algebraic / locked / frozen-formula Features (Wave 001 style) | No in-sample fit. No retune after the sheet. |
| **Learned \(p_t\)** (this template) | Legal only as a **named card class** declared **before any fit**: research-fit slice, selection rule, sealed eval slice, model frozen before the independent slice. Holdout remains sealed. |

---

## Required fields (in addition to `FEATURE.md`)

- **FEATURE_ID:** (Archivist-assigned)
- **NAME:**
- **CARD_CLASS:** `LEARNED_PT` (must be declared before any fit)
- **STATUS:** HYPOTHESIS | RESEARCH | ACTIVE | INACTIVE | RETIRED | CEMETERY
- **PROVENANCE:** originator · date UTC · related FEAT/EDGE/CONTRACT/DATA/TEST/CEM IDs · **lineage if replacing a failed map** (AMD-001: new map = new card)
- **LEGAL_P_T:** AMD-20260913-001 — scored \(p_t \in (\varepsilon,1-\varepsilon)\) unless Clock algebraic lock; raw 0/1 not Examiner inputs
- **SAME_T_INCUMBENT:** decision timestamp = mid timestamp, or Clock-named substitute
- **RESEARCH_FIT_SLICE:** span / filter declared before fit
- **SELECTION_RULE:** how the model / hyperparameters are chosen (no post-sheet peek)
- **SEALED_EVAL_SLICE:** independent of fit; model **frozen** before this slice
- **HOLDOUT:** remains sealed per constitutional path
- **ASSET_HEADLINE:** per AMD-20260913-005 — pre-register single- vs two-asset; no unlabeled pool; RESEARCH ≠ book
- **ECE:** report via `expected_calibration_error` when N allows (AMD-20260913-006)

## DEFINITION

Exact computable definition of the learned map (inputs, architecture or formula class, output = legal \(p_t\)). Not vibes.

## MECHANISM

Why this learned map could improve \(P(\text{YES} \mid \mathcal{I}_t)\) vs same-\(t\) mid without look-ahead.

## BANS

- Fitting as “development” on an algebraic / locked Feature
- Retuning after the sheet
- Sister card after peek (AMD-005)
- Unlabeled pool
- Order emission
- Using this template to rehabilitate TEST-20260913-001 / FEAT-005

---

*End FEATURE_LEARNED_PT — named class only; not a general fitting license.*
