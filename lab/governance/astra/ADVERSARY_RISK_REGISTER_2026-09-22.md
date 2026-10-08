# Adversary risk register — Astra Deathmatch / Q6–Q7 / C1
**Date:** 2026-09-22 (America/New_York)  
**Seat:** The Adversary (Drift Guard)  
**Charter:** Working Plan v0.1 §4 / §4b / weekly cadence  
**Stance:** Name risks onto the scorecard. Do **not** invent failures. Do **not** block trials by default. Do **not** replace Examiner of record.

**Queue status:** Empty for bakeoff — Q7 scored **SCORED_KILL_B_KEEP_000** (no new KEEP/bakeoff). Hygiene memo indexed. Conductor wake protocol: **KEEP/bakeoff only**.

**Updated:** 2026-10-03T19:25:17-04:00 (Adversary: EXT-K2 PR67 pre-score review CLEAR_WITH_ADVISORIES, linked below). Prior: 2026-10-03T17:08:53-04:00 (Adversary: Card 01 NH-002-H Amendment B pre-outcome review ADVISORY_FLAGS, linked below); 2026-10-03T17:05:02-04:00 (Adversary: EXT-K1 PR66 pre-score review CLEAR, linked below); 2026-09-24T20:08:57-04:00 (Card 01 NH-002-H leakage/circularity check); 2026-09-24T19:50:00-04:00 (Edge Research dead-card overlap + Refiner extension overfit-check protocol).

---

## Active lines in scope (awareness — not full weekly red-team yet)

| Line | Stage | Notes |
|---|---|---|
| Q6 incumbent (label `000`, F/P/R off) | Historical sim freeze → shadow candidate only | Modeled P&L only; not live |
| Q7 `nfl_paircheck_lab_20260922` 2×2 | **SCORED_KILL_B_KEEP_000** on `main` | Examiner closed measurement · Arm B KILL · shadow `000` KEEP · live DENIED · see scorecard + cemetery CEM-ASTRA-20260922-001 · hygiene: `packets/Q6_000_COMPLACENCY_SPOTCHECK_2026-09-22.md` |
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



---

## Packet R1-P3-ADVERSE (2026-09-22)

**Status:** ACCEPT — measurement/Adversary gate only (Conductor triage).  
**Detail:** `briefs/R1-P3-ADVERSE_2026-09-22.md`

**Demanded objects on sports maker lines claiming odds/hedge edge:** `edge_at_quote`, `edge_at_fill`, `hedge_complete_flag`, `odds_age_sec`. Missing → measurement gap, not invented kill.

**Freeze note:** name Shin vs proportional de-vig (or factorial both); silent method switch after outcomes = drift.

**Banned:** Polymarket/polymm full bot port; silent Q6/Q7 retune; author wallet P&L as Astra evidence.



---

## Packet Q6-000 complacency (2026-09-22)

After Examiner **KILL** Arm B · **KEEP** shadow `000`: see `packets/Q6_000_COMPLACENCY_SPOTCHECK_2026-09-22.md`.

Watch: inherited-fee ≠ venue pin; queue 3,300 vs 10,000 EV gap; no reopen of freeze after Q7 peek; 31-game reuse ≠ holdout; pair-check-on ≠ pair economics solved. No capital redesign from this seat.



### Hygiene stamp (Archivist) — 2026-09-22

| Field | Value |
|---|---|
| Status | **HYGIENE** after **SCORED_KILL_B_KEEP_000** |
| Packet | `packets/Q6_000_COMPLACENCY_SPOTCHECK_2026-09-22.md` |
| Named risks | (1) fee blindness (2) queue/capital contention (3) lookahead/freeze integrity (4) 31-game overfit (5) mechanism complacency |
| Verdict change | **None** — Examiner KILL_B / KEEP_000 / live DENIED stands |
| Cemetery-adjacent | Risks parked here + noted on `CEM-ASTRA-20260922-001` · not a second kill |
| Banned | Invented PnL · promote language · orders · capital redesign from this memo |



---

## Packet R2-P5 refuse hygiene (2026-09-22)

**Yes — refuse** fee-honest `hedge_complete` without R1-P1 feebook pin, or with mixed kickoff clocks not labeled `holdout_mixed`. Detail: `packets/R2-P5_ADVERSARY_REFUSE_HYGIENE_2026-09-22.md`. No Q6-000 verdict change.

## Freeze refuse-binds (Conductor ACCEPTED — 2026-09-22 ~20:15 ET)

Adversary filed short refuse-bind memos on freezes Conductor put live. Measurement/provenance only. No Q6-000 verdict change. No orders. Results null until Examiner.

| Packet | Memo | Key refuse (one-line) |
|---|---|---|
| **C1+C3+C5** (cash-cow) | `packets/C1_C3_C5_ADVERSARY_REFUSE_BIND_2026-09-22.md` | C1: no UFC strategy; $5k bakeoff label only · C3: weather-spread GitHub = hypothesis only, never Astra EV · C5: not live crypto; no bacchus/kxeth15m port · Simulator units NOT_FOUND → spot-check deferred |
| **R3-P3** (priority) | `packets/R3-P3_ADVERSARY_REFUSE_BIND_2026-09-22.md` | Paper +2.6% = hypothesis only; refuse Lee-Ready; refuse scoring before settled panel + R1-P1; Simulator units NOT_FOUND → spot-check deferred |
| **R3 suite** P1–P4 | `packets/R3_SUITE_ADVERSARY_REFUSE_BIND_2026-09-22.md` | No bacchus port; no invented PnL; no paper maker ROI as Astra edge; no demo queue = production fills; prefer `fee_cost` over model when present |
| **R2-P3** | `packets/R2-P3_ADVERSARY_REFUSE_BIND_2026-09-22.md` | Refuse completed-profit w/o R1-P1; freshness from WS ping; maker-credit floor-zero near 0/1; `000` retune; ATL@GB sub |
| **S5** | `packets/S5_ADVERSARY_REFUSE_BIND_2026-09-22.md` | Refuse PnL/strategy claims; R1-P4 reopen; RFQ-density while 401/429; fee-honest w/o combo fee channel; inventing fills; `000` retune |
| **S4** | `packets/S4_ADVERSARY_REFUSE_BIND_2026-09-22.md` | Refuse `000` retune / NFL ML capacity; fee-honest w/o R1-P1; freshness from WS ping; invented OI/vol; weekend-overlap as same-edge proof |

**Simulator R3-P3:** RESULTS_NULL / units NOT_FOUND (`r3_p3_fl_maker_taker/results/EMPTY_RESULTS.json`). Spot-check deferred.  
**Simulator C1/C3/C5:** RESULTS_NULL / units NOT_FOUND (`scout_c1_kxufcfight/`, `scout_c3_kxhighny/`, `scout_c5_kxbtc15m/` — `FROZEN_NOT_RUN` / `NOT_RUN`). Spot-check deferred.

## Edge Research + Refiner extensions (2026-09-24 ~19:50 ET)

- Dead-card overlap, cards 01–10: `packets/ADVERSARY_DEAD_CARD_OVERLAP_EDGE_RESEARCH_2026-09-24.md`. Up-front cemetery: 09, 10-core, 06-CPI, 03 volume-subsidy taker. Conductor's three flags confirmed on disk. No Q6-`000` verdict change.
- Extension overfit CHECK (advisory; vote only at pass > 5): `packets/ADVERSARY_EXTENSION_OVERFIT_CHECK_PROTOCOL_2026-09-24.md`. First application: Q7 Arm B. P2 in flight, extensions not yet due, 4 pre-flags filed.

## Card 01 NH-002-H leakage check (2026-09-24 ~20:09 ET)

- `packets/ADVERSARY_CARD01_NH002H_LEAKAGE_CHECK_2026-09-24.md`: ElectIndex INDEPENDENT (documentary; code unaudited); w grid [V] pre-price; universe price-independent by reproduction, 'no price viewed' claim [A]; one-draw handled (state bootstrap + recentering, scoped to this cycle); 6 advisory flags (fee pin default for House series, ElectIndex model drift, unanchored timestamps, recentering not pinned, legacy-series attrition, gate (c) text). Advisory only; Q6-`000` unchanged.

## EXT-K1 pre-score review (2026-10-03 ~17:05 ET)

- 2026-10-03: `packets/ADVERSARY_EXT_K1_PRESCORE_REVIEW_2026-10-03.md`: **CLEAR** (Examiner may score in DESCRIPTIVE/ITERATE/INCONCLUSIVE). PR66 main@09b56273. No blocking fixes; 9 tracked advisories (T01 end-to-end rebuild, INVARIANCE R33 flags, empty-bucket→INCONCLUSIVE, overround/T11, gate share vs Shin twin, fee account-class pin, registry outcome-exposure note). Advisory only; Q6-`000` unchanged.

## Card 01 NH-002-H Amendment B review (2026-10-03 ~17:08 ET)

- 2026-10-03: `packets/ADVERSARY_CARD01_AMENDMENT_B_REVIEW_2026-10-03.md`: **ADVISORY_FLAGS** (Amendment B ee6af37c / script 049368f9 verified; M_f + Bernoulli-MLE recentering well-defined, deterministic, shift recovery exact on toys). 11 pre-outcome fixes: REJECT(b) not complement of PASS(ii); fee-BLOCKED verdict cap; ElectIndex capture stalled since 09-26; fee provenance not enforced in code; swing-stress fragility/defect rule; unpinned input builder; MANIFEST 16f96d3d bytes missing. Advisory only; Q6-`000` unchanged.

## EXT-K2 pre-score review (2026-10-03 ~19:25 ET)

- 2026-10-03: `packets/ADVERSARY_EXT_K2_PRESCORE_REVIEW_2026-10-03.md`: **CLEAR_WITH_ADVISORIES** (Examiner may score part (a) in DESCRIPTIVE/ITERATE/INCONCLUSIVE; part (b) output review pending Simulator box run, checklist §11). PR67 main@a940355a; part (a) reproduced exactly (Δ* −0.000301641, CI [−0.001030989, 0.000450135], constancy 523f840b); R45 main-tree scan 0 Becker ids/numbers; T01 rebuild + N6 inherited from K1. No blocking fixes; 12 tracked advisories (part (b) RAM gate + clean-tree/pin check are mandatory pre-run conditions). Advisory only; Q6-`000` unchanged.

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
