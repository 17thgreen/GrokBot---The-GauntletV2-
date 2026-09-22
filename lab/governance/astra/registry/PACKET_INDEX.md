# Astra / Kalshi — Packet Index
**Owner:** The Archivist (Registry) · agent `5099609`  
**Charter:** Working Plan v0.1 (GO 2026-09-22)  
**Updated:** 2026-09-22T17:25:12-04:00 (ET)
**Rule:** freeze-before-outcome · done = artifact on disk · no invented results  
**Repo:** `17thgreen/GPT-6-Astra-Deathmatch`

## Open packets

| ID | Packet | Owner | Reviewer | Freeze / board status | Pointer |
|---|---|---|---|---|---|
| K1 | Owner kit ZIPs → restore | Logan (kits) / Simulator verifies | Conductor | N/A (custody) · **blocks Q7-RUN** | Needs kit restore before scenarios |
| R1 | Deep Research brief + triage | Deep Research / Conductor triage | Conductor | **TRIAGED** · P1 ACCEPT (Sim) · P5 ACCEPT (Sim rails) · P3 CLOSED (measurement gate filed) · P2 QUEUE · P4 DEFER · no Examiner score packet | `lab/governance/astra/briefs/R1_*` · see R1-P* rows |
| B0 | Bakeoff template | Conductor | Examiner | Not started | Plan GO already |
| ADMIT-1 | Prospective panel + recorder | Collector + Registry | Conductor | **LIVE** · `admitted_at` `2026-09-22T21:18:13Z` · panel `2026-09-22.1-kalshi-occurrence-sot` · 16 events · PHI@CHI not backfilled · recorder PID `852286` GET-only 86400s/30s · DB `/workspace/lab/astra-capture/prospective/capture.sqlite` · cool-wipe shell killed | `lab/governance/astra/packets/ADMIT1_2026-09-22.md` |

## Merged / on main (desk)

| ID | Packet | Owner | Merged | Freeze pointer |
|---|---|---|---|---|
| C1 | Prospective GET-only NFL recorder | Collector Ops | **2026-09-22 17:19 ET** · [PR1](https:/github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/1) · merge `cb6223989afaf9e2f2fde8516e5ce16098ef7160` · head was `42f35e27d9cca92a7388f6d3bddce29d8130eb98` | **MERGED on main** · path `nfl_prospective_recorder_20260922/` · smoke PASSED · ADMIT-1 LIVE on admitted panel |
| Q7 | Paircheck lab 2×2 (arms A–D) | Simulator | **2026-09-22 17:23 ET** · [PR2](https:/github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/2) · merge `a85bfdab0cd7e3b4fcb3d4a5c89cf8627be85bd2` | **MERGED on main** · path `nfl_paircheck_lab_20260922/` · `EXPERIMENT_SPEC` + `FROZEN_EXPERIMENT` · status **FROZEN_IMPLEMENTED_NOT_RUN** until K1 kits · **Q7-PR2-REVIEW PASS** · **no outcome emission** until Q7-RUN artifacts + Examiner packet · no scoring |

## R1 child packets (from triage)

| ID | Decision | Packet | Owner | Notes |
|---|---|---|---|---|
| R1-P1 | IN_PROGRESS | R1-P1-FEEBOOK | Simulator; Examiner (Kalshi) reviews tests | Fee + reciprocal-book unit truth |
| R1-P5 | QUEUED | R1-P5-RAILS | Simulator (+ Collector freshness hooks) | Queued after P1 start; instrument not strategy; no live launcher |
| R1-P3 | **CLOSED** | R1-P3-ADVERSE | Adversary · reviewer Conductor accepted | Measurement gate filed, no code · artifacts: `briefs/R1-P3-ADVERSE_2026-09-22.md` + `ADVERSARY_RISK_REGISTER_2026-09-22.md` |
| R1-P2 | QUEUE | R1-P2-CHALLENGER (reserved, not open) | — | After P1 fee truth + Q7-RUN or explicit Conductor kick |
| R1-P4 | DEFER | — | Scout+Collector access check first | RFQ combos |

Artifacts: `lab/governance/astra/briefs/R1_DEEP_RESEARCH_2026-09-22.md`, `R1_PROPOSALS_2026-09-22.json`, `R1_TRIAGE_2026-09-22.md`.

## Scout brief + Conductor triage (2026-09-22)

**Artifact:** `lab/governance/astra/SCOUT_BRIEF_2026-09-22.md`  
**Indexed:** 2026-09-22 · Scout measurement kernels only (no bots / no panel admit)

| Kernel / line | Conductor triage | Notes |
|---|---|---|
| Spreads | **TRY after C1** | C1 MERGED; ADMIT-1 LIVE — spreads TRY unblocked at board level |
| PASSYDS | **TRY** | NFL pass-yards props kernel |
| MLB | **TRY** | Non-NFL daily cadence candidate |
| CFB | **DEFER** | College football |
| MVE | **SKIP** | Cross-category parlays / MVE inventory |

**Calendar notes (board facts):**
- PIT@CLE venue id **live:** `KXNFLGAME-26OCT01PITCLE`.
- Kickoff source of truth = Kalshi `occurrence_datetime`.
- PIT@CLE T−7d (admit packet / Kalshi occurrence SoT): **2026-09-25T03:15:00Z** (= **2026-09-24 23:15 ET**). Prior schedule-derived board clock was 2026-09-24 20:15 ET; SoT supersedes for ADMIT-1.

## Incumbent freeze on main

| Line | Artifact | Status |
|---|---|---|
| Q6 | `SHADOW_CANDIDATE_FREEZE` selected `000` | **Remains incumbent freeze on main** · shadow research only · no live |

## Closed desk packets

| ID | Packet | Owner | Reviewer | Closed | Artifacts |
|---|---|---|---|---|---|
| R1-P3 | R1-P3-ADVERSE (sports adverse / de-vig measurement gate) | Adversary | Conductor accepted | 2026-09-22 | `lab/governance/astra/briefs/R1-P3-ADVERSE_2026-09-22.md` · `lab/governance/astra/ADVERSARY_RISK_REGISTER_2026-09-22.md` · measurement gate only, no code |

## Closed / historical (imported — not desk packets)

Q1–Q5 historical results + Q6 freeze via repo experiment registry. Archivist does not re-score.

## Active line freezes

| Line | Where | Status |
|---|---|---|
| Q6 incumbent | `main` · `SHADOW_CANDIDATE_FREEZE` · selected `000` | **FROZEN on main** |
| C1 recorder | `main` · merge `cb6223989afaf9e2f2fde8516e5ce16098ef7160` · `nfl_prospective_recorder_20260922/` | **MERGED** · ADMIT-1 LIVE on admitted panel |
| Q7 paircheck | `main` · merge `a85bfdab0cd7e3b4fcb3d4a5c89cf8627be85bd2` · `nfl_paircheck_lab_20260922/{EXPERIMENT_SPEC,FROZEN_EXPERIMENT}` | **MERGED** · **FROZEN_IMPLEMENTED_NOT_RUN** · freeze pointer filed · no Examiner score until run artifacts · K1 blocks Q7-RUN |

## Cemetery

Gauntlet-era CEM entries remain under `/workspace/lab/archive/cemetery/`. Astra Kalshi cemetery opens on first kill under this registry.

## Admission calendar (clock facts — do not backdate)

| Game | Kickoff / SoT | T−7d | Note |
|---|---|---|---|
| PHI@CHI | — | full window missed | **Not backfilled** · `KXNFLGAME-26SEP28PHICHI` · ineligible incomplete |
| PIT@CLE | Kalshi occurrence SoT | **2026-09-25T03:15:00Z** (**2026-09-24 23:15 ET**) | Venue `KXNFLGAME-26OCT01PITCLE` · ADMIT-1 LIVE · SoT supersedes prior schedule-derived 20:15 ET board clock |
| Cohort | schedule-only-20260922-after-phi-chi-miss | admitted_at `2026-09-22T21:18:13Z` | 16 events PIT@CLE→ATL@NO · panel `2026-09-22.1-kalshi-occurrence-sot` |

## Archivist standing gates

1. Refuse to index result files for any experiment ID lacking a prior freeze (on main after merge, or explicitly admitted draft pointer).  
2. Q7: no outcome emission until run artifacts exist + Examiner packet; no scoring from Registry.  
3. On PR merge: file freeze pointer (path, head SHA, status) here.  
4. Missed T−7d → label incomplete; never backdate admission.  
5. IDs assigned only here; Conductor closes or reassigns packets.
