# R2-P1 — FEEBOOK+RAILS HYGIENE STRESS ON Q6-000 (FREEZE) 2026-09-22 (ET)

**ID:** R2-P1 ADMIT (Conductor triage)  
**Owner:** R&D Variants (freeze) → Simulator fixture join → Examiner  
**Status:** FROZEN — implement in flight / ASAP  
**Cite:** `briefs/R2_DEEP_RESEARCH_2026-09-22.md` §R2-P1; `briefs/R2_PROPOSALS_2026-09-22.json` id R2-P1; `briefs/R2_CONDUCTOR_TRIAGE_2026-09-22.md`; post-PR5 maximize twin  
**Alias:** supersedes / narrows prior `FEE_SENSITIVITY_000_R1P1_FREEZE_KERNEL_2026-09-22.md` to the R2-P1 measurement kernel  
**Repo:** `https://github.com/17thgreen/GPT-6-Astra-Deathmatch`  
**Hard rules:** Instrument only. No Q6-000 signal retune. No capital A1/A2/A3 redesign. No Q7 reopen. No live orders. No invented PnL. `results`/`pnl` null until Examiner.

---

## Measurement kernel (locked)

Re-score Q6-000 historical **completed-net channel** using published Kalshi fee round_up algebra (**R1-P1**) and label fills with **R1-P5** instruments:

- `maker_credit_floor_zero_refuse`
- `content_fresh_flag` (content/transaction-time — not WS ping)
- `queue_attribution_bin` vs assumed `q3300` / `q10000`

**Pre-settlement outputs only** (nullable until instrument-verified run):

| Output | Meaning |
|---|---|
| `fee_delta_vs_inherited_model` | Delta between R1-P1 feebook fees and inherited Q6/shadow fee model on the same fills |
| `freshness_gap_sec` | Gap implied by content-fresh vs keepalive-style freshness |
| `queue_bin_mismatch_rate` | Rate that attributed queue bin ≠ assumed scenario bin (3300/10000) |

These are hygiene / label artifacts — **not** a strategy scorecard promotion claim.

---

## Pins

| Pin | Value |
|---|---|
| Strategy subject | Q6-`000` KEEP (shadow sha `b55ff36cb161c824a3d1b490795c8ac6891f01489456f61da311ac863366af48`) — measurement subject only |
| Tape | factorial inputs manifest sha `375ea6e2c9125a411d5444a88115213542d5b19c874d73a2bed0b9355fd6277d` |
| Fee | `kalshi_feebook_lab_20260922/` @22371178cb2663250b4762f328069571c48cb551 — mandatory; forbid inherited `0.0175`/`0.07` literals from shadow `common_config` as fee source |
| Rails | `kalshi_rails_lab_20260922/` @6a28e0d6254327ea4e6451c781bec56215ac6cac |
| Capital | unchanged shared $5k; capital-structure lab merged @ce4671b8201b3fe49ecab91d684815fe6bd51447 is **out of scope** for this knob |
| Empty results | `packets/R2-P1_FEEBOOK_RAILS_HYGIENE_000/results.json` |

---

## Do-not-modify

1. No live orders / no live adapter.  
2. No signal retune of 000; no pair-check reopen (CEM-ASTRA-20260922-001).  
3. Not capital-structure A1/A2/A3; not F1–F3; not queue-fragility twin (waits).  
4. Do not invent walk PnL; leave `fee_delta` / `freshness_gap` / `queue_bin_mismatch` null until real fixture join.  
5. New lab dir only; do not mutate feebook/rails/Q/capital labs.

---

## Implement deliverables

Lab e.g. `kalshi_r2p1_hygiene_000_lab_20260922/` (or continue fee-sensitivity lab renamed to R2-P1):

- Units: feebook vs inherited delta helper; content-fresh vs keepalive; queue bin vs assumed scenario; ban fee literals  
- Fixture join stubs with null outputs in `FROZEN_EXPERIMENT.json`  
- PR body cites R2-P1 + feebook/rails SHAs  

---

## Frozen-at

`2026-09-22T22:58:42.402280+00:00` UTC. Desk 2026-09-22 ET.
