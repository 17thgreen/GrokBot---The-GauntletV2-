# SUPERSEDED → R2-P1

**Status:** SUPERSEDED  
**Canonical freeze:** `R2-P1_FEEBOOK_RAILS_HYGIENE_000_FREEZE_2026-09-22.md` (sha256 `ddcd4427f67fb0ed8d12a7a6a49aabea3b25b356bcb64a7d84d5c4590d08b563`)  
**Bundle:** `packets/R2-P1_FEEBOOK_RAILS_HYGIENE_000/`  
**Do not implement** this fee-sensitivity packet as a second lab.  
**Superseded_at:** 2026-09-22T22:59:24.143631+00:00

Former content retained below for audit only.

---

# FEE-SENSITIVITY OF Q6-000 UNDER R1-P1 — FREEZE KERNEL 2026-09-22 (ET)

**Owner:** R&D Variants (freeze / pin ownership)  
**Implementer:** Cloud agent after capital-structure PR5 merge  
**Reviewer:** Examiner (Kalshi); Adversary on fee-blind / inherited-literal hygiene  
**Status:** FROZEN — queued for implement **after** PR5 merge (Conductor PASS on PR5; Auto-review undraft may await Logan card)  
**Cite:** Conductor 2026-09-22 maximize twin; Examiner KEEP 000 / KILL B; R1-P1 feebook @22371178cb2663250b4762f328069571c48cb551; R1-P5 rails @6a28e0d6254327ea4e6451c781bec56215ac6cac (queue held fixed)  
**Repo:** `https://github.com/17thgreen/GPT-6-Astra-Deathmatch`  
**Hard rules:** One knob = **fee treatment only**. No capital redesign. No Q6-000 signal retune. No live orders. No invented PnL. `results`/`pnl` null until Examiner-ready run.

---

## Intent (one knob)

Holding strategy **Q6-`000`**, shared **$5,000** account, 31-game development tape, and **R1-P5 queue/fill rails fixed**, measure how **R1-P1 fee-channel choices** change fee-honest measurement labels (not promotion claims until Examiner).

This is the preferred twin after capital-structure. **Queue-fragility twin** stays queued **only after this fee-sensitivity lab merges**.

---

## Depends on

| Dep | Pin |
|---|---|
| Strategy | Q6-`000` shadow · `SHADOW_CANDIDATE_FREEZE.json` sha256=`b55ff36cb161c824a3d1b490795c8ac6891f01489456f61da311ac863366af48` · Examiner KEEP 000 |
| Tape | `nfl_factorial_lab_20260921/inputs/manifest.json` sha256=`375ea6e2c9125a411d5444a88115213542d5b19c874d73a2bed0b9355fd6277d` · N_events=31 |
| Fee instrument | R1-P1 `kalshi_feebook_lab_20260922/` @ `22371178cb2663250b4762f328069571c48cb551` — **mandatory bind**; no inherited `0.0175`/`0.07` literals from shadow `common_config` |
| Queue instrument | R1-P5 `kalshi_rails_lab_20260922/` @ `6a28e0d6254327ea4e6451c781bec56215ac6cac` — **fixed across arms** (not the knob) |
| Capital | Shared pool status quo (A1-equivalent). Do **not** reopen A2/A3 in this probe |
| Prior maximize | Capital-structure PR5 — implement this lab only after PR5 is on main |

---

## Arms (fee treatment only; same C_total, same tape, same queue, same 000)

| Arm | Name | Fee treatment (via feebook API only) |
|---|---|---|
| **FS0** | Examiner baseline | R1-P1 order-level ceil channel as merged (`order_fee` + `examiner_fee_channel` / `classify_scorecard`). Maker ceil when `round_up=True`; partials `round_up=False` per feebook pin |
| **FS1** | Maker-fee off (series override) | Same feebook path with series `maker_fees_enabled=False` (or equivalent table flag) — isolates maker-fee contribution |
| **FS2** | Maker unrounded comparator | Same rates through feebook loaders, but maker path uses **unrounded** paper comparator (Grok-style) **labeled non-promotion** — rounding sensitivity only |

**Not arms:** capital A2/A3; pair-check on/off; queue 3300 vs 10000 as a fee knob (harsh queue may appear as a **fixed** stress label twin later, not here); any Q6 signal change.

---

## Constants

| Pin | Value |
|---|---|
| C_total | 5000 USD shared |
| Strategy | Q6-000 |
| Primary stress (queue fixed) | `q3300_d0.25` via rails |
| Promotion scoreboard | shared account only |
| Empty results file | `packets/fee_sensitivity_000_r1p1/results.json` + `results/EMPTY_RESULTS.json` (`results`/`pnl` = null) |

---

## Do-not-modify

1. No live orders / no live adapter.  
2. No Q6-000 retune; no Q7 arm reopen (KILL B stands).  
3. No capital-structure redesign (A2/A3 out of scope).  
4. No scoring with shadow `common_config` fee literals.  
5. No invented walk PnL; empty results stay null until instrument-verified run.  
6. Do not start queue-fragility twin until **this** fee-sensitivity lab merges.  
7. Do not mutate feebook/rails/Q labs — new lab dir only when implementing.

---

## Implement when PR5 merges (not before)

New dir e.g. `kalshi_fee_sensitivity_000_lab_20260922/`:

- `EXPERIMENT_SPEC.md` + `FROZEN_EXPERIMENT.json` (pnl null)  
- Unit tests: arms differ only in feebook flags; rails queue identical; forbid fee literals; empty results unchanged by units  
- Optional thin runner later — units first  

---

## Twin queue (after this merges)

**Queue-fragility of Q6-000 under R1-P5** (one knob: queue/fill stress with feebook fixed) — draft only after fee-sensitivity merge ack.

---

## Frozen-at

`2026-09-22T22:57:22.294105+00:00` UTC. Desk 2026-09-22 ET.  
Conductor asked: freeze on disk immediately; ping path.
