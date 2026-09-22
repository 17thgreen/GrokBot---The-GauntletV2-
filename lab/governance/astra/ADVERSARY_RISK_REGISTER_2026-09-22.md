# Adversary risk register — Astra Deathmatch / Q6–Q7 / C1
**Date:** 2026-09-22 (America/New_York)  
**Seat:** The Adversary (Drift Guard)  
**Charter:** Working Plan v0.1 §4 / §4b / weekly cadence  
**Stance:** Name risks onto the scorecard. Do **not** invent failures. Do **not** block trials by default. Do **not** replace Examiner of record.

**Queue status:** Empty — no Examiner KEEP / bakeoff awaiting Adversary. Conductor wake protocol: **KEEP/bakeoff only**.

**Updated:** 2026-09-22 ~17:05 ET (Conductor handoff + PR status).

---

## Active lines in scope (awareness — not full weekly red-team yet)

| Line | Stage | Notes |
|---|---|---|
| Q6 incumbent (label `000`, F/P/R off) | Historical sim freeze → shadow candidate only | Modeled P&L only; not live |
| Q7 `nfl_paircheck_lab_20260922` 2×2 | **IMPLEMENTED / FROZEN, not run** on draft [PR2](https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/2) | 16 scenarios **NOT_RUN** (kits pending). Do not treat draft-PR freeze as `main` evidence until Archivist indexes. |
| C1 durable GET collector + panel | PR1 draft, **undeployed** | PHI@CHI full T−7d incomplete — no backdate |
| Bakeoff B0 | Template pending | Needed before any challenger displaces incumbent |

### Process note (named, not invented)
Registry `PACKET_INDEX.md` / `STATUS_2026-09-22.md` (17:04 ET) still show Q7 freeze **GAP on main** while Conductor reports freeze on **draft PR2**. Until Archivist indexes the freeze commit, treat outcome files as **orphan-run risk** if they appear ahead of an indexed freeze.

---

## Named risks (force onto scorecard / freeze)

### 1. Lookahead
- Q7 check must not inspect **future** quotes when deciding pair admission.
- Candidate selection / “simplest retain” rule must be declared **before** outcome files exist.
- Holdout / prospective panel identity resolution must not use post-window information to “complete” a missed T−7d.

### 2. Leakage
- Dev cohort (31 games) must not silently inform holdout scoring or shadow labels.
- Q6 `SHADOW_CANDIDATE_FREEZE` selection must not be reopened after peeking at Q7 results.
- Rejection ledgers: skipped hypothetical profits ≠ completed money; do not fold them into net EV.

### 3. Fee blindness
- Completed net **after fees** is the only claimable completed P&L; open inventory separate.
- Fee model pinned across all 16 Q7 scenarios; any fee-regime change is a **new** freeze, not a retune.
- Shared $5k / shared liquidity: no double-counting concurrent sims as additive capacity.

### 4. Regime break
- Queue 3,300 vs 10,000 and delay 0.25s vs 5s are stress axes, not interchangeable “the” EV.
- NFL week / season regime shift: historical Q6 improvement is not transferable without fresh tape.
- Missed PHI@CHI window: incomplete capture is a process/regime fact — label incomplete; do not repair by backfill.

### 5. Capacity fantasy
- 250 event cap + 250 assumed exit depth are assumptions; scale claims require a capacity model (§8 Working Plan).
- Incumbent displacement bakeoff must use same capital constraints (or explicitly scaled) and Kalshi microstructure we can actually access.
- Extrapolations from 31-game modeled nets must be labeled **projections**, never evidence.

### 6. Prompt / strategy drift
- One change per trial when Variants touch Q6/Q7 (no silent multi-knob retunes).
- Arm C must remove **only** the combined-cost filter; residual margin gates via another eligibility path = drift failure mode to test, not assume absent.
- Docker committed ≠ collector deployed; docs claiming “capture ready” without always-on host = process drift.

---

## Packet R1-P3-ADVERSE (2026-09-22)

**Status:** ACCEPT — measurement/Adversary gate only (Conductor triage).  
**Detail:** `briefs/R1-P3-ADVERSE_2026-09-22.md`

**Demanded objects on sports maker lines claiming odds/hedge edge:** `edge_at_quote`, `edge_at_fill`, `hedge_complete_flag`, `odds_age_sec`. Missing → measurement gap, not invented kill.

**Freeze note:** name Shin vs proportional de-vig (or factorial both); silent method switch after outcomes = drift.

**Banned:** Polymarket/polymm full bot port; silent Q6/Q7 retune; author wallet P&L as Astra evidence.

## What I will / will not do on promote

| Will | Will not |
|---|---|
| Spot-check Examiner KEEP packets against this register | Self-certify TEST/live or override Examiner score |
| Flag missing freeze hashes, fee/inventory gaps, capacity leaps | Kill creativity or block all trials by default |
| Weekly red-team memo on active lines | Invent P&L, fills, or failures without artifact evidence |
| Escalate only named, evidenced risks to Conductor | Ping Logan for routine triage |

---

## Immediate asks (Conductor / Registry)

1. Pointer to freeze manifests + Examiner scorecards once Q7/C1 land (registry folder currently empty on box).  
2. Notify Adversary when any packet hits Examiner KEEP / bakeoff candidate.  
3. Confirm weekly red-team slot (proposed: Mondays 10:00 ET) for active Kalshi lines only.

**Artifact path:** `lab/governance/astra/ADVERSARY_RISK_REGISTER_2026-09-22.md`
