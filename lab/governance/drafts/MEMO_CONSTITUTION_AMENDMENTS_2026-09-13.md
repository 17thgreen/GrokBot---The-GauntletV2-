# MEMO — Proposed constitutional amendments
**To:** Logan M (Human Governor)  
**From:** The Conductor  
**Date:** 2026-09-13  
**Status:** DRAFT PROPOSAL — not filed, not approved, not retroactive  
**Baseline:** `gauntlet-v2.0-alpha` @ `05433c8` (immutable tag; these would apply *after*)  
**Process:** `governance/AMENDMENT_RULE.md` — Conductor may propose; only you approve.

This is not a new constitution. It is a ballot. Informal chat does not amend the institution. If you stamp any item below, I will file a matching `AMD-20260913-NNN` with `RETROACTIVE: NO`.

---

## 0. What this memo will not touch

These earned their place this week. I am not proposing to loosen them.

| Keep | Why it stays |
|------|----------------|
| Clock / Examiner / Prosecutor / Treasurer cannot be waived | They are why F1, F3, and F2 did not become strategies |
| Forecast ≠ trade | A sidecar may be *specified* dark. Nothing places until a League challenger exists |
| Market price is the benchmark | `MKT-KALSHI-15M-MID` remains incumbent after TEST-007 and TEST-20260913-001 |
| Peek ≠ new headline | k=50 annex on F2 is not a do-over |
| `FAIL-INSUFFICIENT` ≠ proven no-edge | Cemetery-of-science remains forbidden |
| Alpha tag does not move | Amendments apply *after* `gauntlet-v2.0-alpha`, they do not rewrite it |
| LLM confidence is not a probability | Consensus is not validation |
| No order-placing tools on the shared computer | One leak is every Bot |
| **Mission stays short-horizon BTC/ETH binaries until this search is exhausted** | You locked this 2026-09-13. New domains or a new fleet come *after* this experiment, via new governing prompts. I withdraw any earlier suggestion that civil/insurance belongs on this lattice now |

Gauntlet-OS remains an unofficial extract until rules earn a published digest. This memo does not adopt OS as live law.

---

## 1. The holes the first draft could not see

You built the lock in days. That is not a criticism. Three days of Track B then showed contradictions and missing duties that were invisible on 2026-09-11.

### Hole A — We score with logloss, then allow raw 0/1 forecasts

`PREDICTION_MARKET_MISSION` and `BINARY_EXAMINER_SPEC` ask for a calibrated \(p_t\) and kill on ΔLogLoss. FEAT-005 Map 2 was allowed to emit hard 0/1. Ether at k=30: Brier improved, logloss exploded, because we were 100% sure and wrong ~8% of the time. We then called the family dead.

That is a fair fail *under today's rules*. It is also a scoring-contract bug. We invited a hammer and fired it for not being a screwdriver.

**Either** a raw 0/1 is not a legal *scored* forecast except at algebraic lock (Map 1, k=60), **or** logloss is the wrong kill for that map class. I propose the first. It forces a clipped or distributional remainder *before* we see the sheet. It cannot rescue TEST-20260913-001 (`RETROACTIVE: NO`).

### Hole B — Process lives in chat, so it rots

The first draft has no skill/MCP admission rule. Every cycle I re-derive door policy in conversation. A public memo then showed up with 40 repos, and the only safe answer I had was “install nothing.” That is too coarse. The missing law is: a skill or MCP may *implement existing doctrine* if it is scanned, names the irreversible thing it will not do, and cannot place an order. It may not *add* doctrine. That is how we take leverage without a third constitution.

### Hole C — The front door can lie

We cemetery and file correctly, then INDEX / GitHub README lag. First-run autopsy was right. Archivist is named; the *duty* that the front door cannot diverge from a filed TEST is not written. Daily repo sync is a clock, not a ledger check.

### Hole D — Intake is not Prosecutor

Wide-net research (data first) plus a Gemini-loop refiner will drown us unless a doorman exists *upstream* of Clock. Prosecutor is downstream (finished claims). Collapsing those is how the lattice dies. This is an `AUTHORITY.md` addition, not a science-family addition. Draft charters are attached separately. Seating the Bots is a later Governor act. This memo only authorizes the *seats*.

### Hole E — “Both assets or die” was written to stop pooling, and it also stops honesty

Pooling BTC+ETH is still a cheat. Requiring both coins on the same frozen k, then calling the whole family dead, can hide a real single-asset RESEARCH result. BTC k=30 passed both Δ; ETH failed logloss. A forward rule — asset-specific RESEARCH if *pre-registered*, never Champion, never pooled, never applied after a peek — is coherent. It does not promote FEAT-005.

### Hole F — ECE is named and almost never binds

The Examiner spec already lists calibration. We kill on both-Δ of Brier and logloss. We do not kill on ECE when N allows. After a powered mid (TEST-007) that is a missing promote criterion, not a new fashion. I am not proposing to import anyone’s LightGBM.

---

## 2. Proposed amendments

All `RETROACTIVE: NO`. `GAUNTLET_VERSION`: after `gauntlet-v2.0-alpha`. `APPROVER`: Logan M. `PROPOSED_BY`: The Conductor.

### AMD-20260913-001 — Legal scored forecasts

| Field | Text |
|-------|------|
| RULE_BEFORE | `BINARY_EXAMINER_SPEC` + Wave 001 practice: any frozen map may emit \(p_t\in\{0,1\}\) and is scored on Brier *and* logloss (clip declared). |
| RULE_AFTER | A scored forecast \(p_t\) must lie in \((\varepsilon,1-\varepsilon)\) with \(\varepsilon\) pre-registered (default \(10^{-4}\)) unless the Clock has algebraic lock (Map 1: full 60s sum already decides YES/NO). Raw 0/1 remainder maps are legal as *unit-test predicates* and as diagnostics. They are not legal Examiner inputs. |
| REASON | Align the map class with the proper scoring rule we already use, so we do not design a forecast to fail logloss and then fail it. |
| EVIDENCE | `[V]` TEST-20260913-001 ETH CLOSE-k30 ΔBrier −0.048, ΔLogLoss +0.324; Brier_model = error rate of hard 0/1. `[A]` Mission §6.4–6.5 already requires calibrated \(p_t\) and proper scores. |
| AFFECTED_ROLES | Examiner (input gate); Conductor / Refiner (map class); Statistician / Tape (card formulas) |

### AMD-20260913-002 — Skills and MCPs implement doctrine only

| Field | Text |
|-------|------|
| RULE_BEFORE | Implicit: no skill/MCP law. Practice = Conductor refuses catalogs in chat. |
| RULE_AFTER | A skill or MCP may be pinned only if (1) it implements an already-written lab rule, (2) it is scanned before it sits on the shared disk, (3) frontmatter names `approval_required` and the one irreversible action it will never take, (4) it cannot place, stage, or size orders. Skills/MCPs may not add doctrine. Read-only market-data tools remain Treasurer-visible and Clock-documented. Order-shaped tools are BAN even if “disabled.” |
| REASON | Take 2026 leverage (frozen procedures, data adapters) without a third constitution or a shared-computer order path. |
| EVIDENCE | `[I]` Supercharge memo 2026-09-13 §0/§6/§8. `[V]` Shared computer is one filesystem for every Bot. `[A]` INSTITUTIONAL_LOCK: Treasurer governs capital-adjacent acts. |
| AFFECTED_ROLES | Treasurer, Clock, Conductor, all Bots |

### AMD-20260913-003 — Front-door non-divergence

| Field | Text |
|-------|------|
| RULE_BEFORE | Archivist maintains INDEX; no hard duty that README / GitHub front door match the latest filed TEST. |
| RULE_AFTER | Within one daily cycle of a filed TEST, cemetery intake, DATA VERDICT, or League change, Archivist (or the Conductor if Archivist is idle) must make `archive/INDEX.md` and the public repo front door state the same headline as the artifact. Divergence is a process fail, not a scientific one. Daily repo sync is necessary and not sufficient. |
| REASON | The institution is the system of record. A correct cemetery with a stale README is how outsiders (and we) learn the wrong lesson. |
| EVIDENCE | `[V]` First-run autopsy: edges killed, front door lagged. `[V]` INDEX/League still required a manual F2 patch after TEST-20260913-001. |
| AFFECTED_ROLES | Archivist, Conductor |

### AMD-20260913-004 — Intake Auditor and Refiner seats

| Field | Text |
|-------|------|
| RULE_BEFORE | `AUTHORITY.md` org flow: researchers → Archivist → Architect → Clock → Examiner → Prosecutor → Mechanic → Treasurer → Canary. No intake doorman. No refinement loop. |
| RULE_AFTER | Add two **specialist** seats, not hard authorities: **Refiner** (persist on inbound drafts until a Clock-joinable kernel or FAIL/restart) and **Intake Auditor** (door test; ADMIT/WATCH/BAN; wide-net freeze; at most three ADMIT after two rounds). They must be different Bots. Neither writes TEST or DATA VERDICT, places orders, or self-audits. Conductor still allocates Examiner time. Prosecutor remains downstream. Draft charters: `CHARTER_REFINER.md`, `CHARTER_INTAKE_AUDITOR.md`. Seating the Bots is a separate Governor act. |
| REASON | Wide-net data search and third-party drafts are now part of the experiment. Without a doorman and a refiner, either Conductor stays boxed-in or the net becomes the job. |
| EVIDENCE | `[V]` Gemini loop produced `evaluate_close_window` after wholesale reject. `[A]` Governor 2026-09-13: wide first pass, audit down to 1–3, no live Bot until a winner. |
| AFFECTED_ROLES | Conductor, Archivist, Clock (join only), new seats |

### AMD-20260913-005 — Asset-specific RESEARCH (forward only)

| Field | Text |
|-------|------|
| RULE_BEFORE | Practice (Wave 001 / F2 order): both assets must show both-Δ skill on the same frozen headline or the family is REDUNDANT / FAIL-INSUFFICIENT. No unlabeled pool. |
| RULE_AFTER | No unlabeled pool (unchanged). A Feature Card may *pre-register* a single-asset headline. That card may reach RESEARCH (not CHALLENGER, not CHAMPION) if that asset clears both-Δ and N gates. The other asset is annex or a sister card. Switching to single-asset *after* seeing a two-asset fail is forbidden. |
| REASON | Stop pooling *and* stop forcing a joint funeral for a one-coin instrument. |
| EVIDENCE | `[V]` TEST-20260913-001 BTC k=30 both-Δ skill, ETH k=30 logloss fail. `[I]` Joint kill was designed to prevent peek-pooling; it also prevents honest single-asset RESEARCH. |
| AFFECTED_ROLES | Examiner, Conductor, League |

### AMD-20260913-006 — ECE binds when N allows

| Field | Text |
|-------|------|
| RULE_BEFORE | `BINARY_EXAMINER_SPEC`: calibration/ECE is a required metric; thin bins → UNTESTED. Promote/kill practice uses ΔBrier and ΔLogLoss only. |
| RULE_AFTER | When the existing power rule is met (as already written for TEST-006/007: ≥2 bins with n≥20 and/or N≥100), ECE vs the incumbent mid is a third skill gate on the same cell: model ECE must not be worse than market ECE by a pre-registered margin (default: model ECE ≤ market ECE). Thin sample → UNTESTED, not a pass. |
| REASON | Mission already says sharpness without calibration is incomplete. After a powered mid, leave that sentence operable. |
| EVIDENCE | `[A]` Mission §6.4. `[V]` TEST-007 powered mid exists; F2 0/1 maps have ECE = Brier by construction — another reason AMD-001 must land first or with this. |
| AFFECTED_ROLES | Examiner |

**Dependency:** file 001 before or with 006. A hard 0/1 map will always look badly calibrated when it misses. 006 without 001 just re-kills Map 2 under a new name.

---

## 3. Not amendments (so we do not pretend they are)

| Item | Vehicle |
|------|---------|
| Kernel-first inbound drafts (extract, name overlap, freeze) | Conductor operating posture. Starts when you say so. No AMD. |
| Wide-net OSS/data scour with a freeze date | Cycle / Track B *order*, Auditor-gated. No AMD. |
| Dark sidecar spec (emit \(p_t\), compare \(m_t\), abstain, never place) | Mechanic draft page. Sits dark. No Bot live. No AMD. |
| Growing TEST-006 | Already done (TEST-007). Do not reopen. |
| Adopting Gauntlet-OS as live law | Still no. Optional later Decision Record: unofficial digest of *earned* rules only |
| Domain expansion | Forbidden until this experiment concludes |

---

## 4. How this should change the workflow

Today: Conductor is doorman, refiner, and traffic cop in one chat. Third-party drafts get a no. Open source gets a no. Front door lags. A 0/1 map walks into a logloss exam. You have to be the persistence layer.

After a stamp of 001–004 (minimum useful set):

1. A draft or a scrape lands as UNTESTED.  
2. Refiner persists until a kernel or a written FAIL.  
3. Auditor runs the door. At most three ADMIT.  
4. Conductor allocates Clock / Feature Card time only to ADMIT.  
5. Examiner scores only legal \(p_t\).  
6. Archivist’s INDEX matches the TEST the same day.  
7. You stop carrying the Gemini loop and the front door by hand.

005 and 006 make the *science* honest: one-coin RESEARCH can exist if we said so first, and calibration is a gate rather than a caption.

What this will not do: invent a winner. The mid is still champ. F1/F2/F3 are still inactive. The amendments make it cheaper to *find* the next thesis and harder to *promote a mistake*. That is the success condition I will own — not a promised edge.

---

## 5. Recommended stamp

If you want a single motion rather than six:

**Stamp A (process):** AMD-001 + 002 + 003 + 004. Seats remain unfilled until you say hire.  
**Stamp B (science gates):** AMD-005 + 006, only after or with 001.  
**Stamp C:** reject any item. Silence is not approval.

I will not file, seat Bots, install skills, or fetch a wide net until you answer with a stamp.

---

— End of draft memo. No capital authorization. No tag move. No fabricated edge. No Bot created.
