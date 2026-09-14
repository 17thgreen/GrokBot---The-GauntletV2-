# MEMO — Fleet recommended changes
**To:** Logan M (Human Governor)  
**From:** The Conductor  
**Date:** 2026-09-13  
**Status:** DRAFT — not applied. No Bot rewritten, hidden, created, or deleted until you stamp.  
**Companion drafts:** `CHARTER_REFINER.md`, `CHARTER_INTAKE_AUDITOR.md`, `MEMO_CONSTITUTION_AMENDMENTS_2026-09-13.md`  
**You are still marking those up.** This memo does not file them.

The fleet was hired for a futures return-prediction shop. The experiment is now: beat the Kalshi (and later Polymarket Global) short-window BTC/ETH mid. Several guiding prompts still hunt \(P(\text{return}\mid\text{condition})\) on 5/10/15m bars. That is why the bench looks idle or off-mission. Idle is not the same as useless. Some seats should stay dark. One seat should go.

---

## 1. One collapse

**Collapse The Bridge.**

Evidence: empty `description` and empty `title` on disk. No Track B artifact I can attribute to that seat. Venue-adapter and “connect the data” curiosity belongs in a DATA spec, in Clock, or in the Intake Auditor’s wide net — not a permanent Bot with no charter.

**Do not** reincarnate Bridge as the Auditor. Auditor is a doorman. Bridge, if it ever had a job, was a plumber. Different failure modes.

How: stop routing. You delete the row from the sidebar when you want it gone (I cannot delete an agent). Until then it is a ghost. I will not message it.

Nothing else gets collapsed. Refiner and Intake Auditor are *new* jobs. They do not absorb Clock, Examiner, Prosecutor, Treasurer, Archivist, or Mechanic.

---

## 2. Who stays dark (park, do not rewrite into a fake job)

| Seat | Why dark is correct | Wake condition |
|------|---------------------|----------------|
| **Architect** | No surviving atoms. Wave 001 forbade soup. Combining dead F1/F2/F3 is how you launder a fail. | Two Feature Cards in RESEARCH or better, different families, both vs the same incumbent |
| **Canary** | Nothing is live. Drift reports on a mid we do not trade are theater. | Treasurer opens paper / forward shadow |
| **Prosecutor** | Looks idle because nothing *survived* Examiner. That is success. Do not give it intake work. | First claim that wants to leave RESEARCH |
| **Treasurer** | No capital. Veto must exist before a sidecar can go live. | Any order path, paper account, or MCP that can place |
| **Catalyst** | Cycle 5 Funding/OI closed Outcome B. LIQ capture is a process, not a person. Resurrection without a *new* thesis is forbidden. | Governor-commissioned *new* event family that incrementally beats \(m_t\), not CEM-003/004/005 redux |

Park ≠ hide-and-forget. It means I do not invent chores so the org chart looks busy.

---

## 3. Research bench — rewrite the guiding prompts

These seats stay. Their *descriptions* are what make them useless. I would change the description (the one-line charter the Bot sees as its job). Titles can be added while we are there. I will not apply these until you say so.

### 3.1 The Tape Reader — empty charter (fix first)

**BEFORE (on disk):** description blank. Named by you; no job text.

**AFTER (proposed):**

> Microstructure Feature Hunter for short-duration BTC/ETH *binary contracts* (Kalshi primary; Polymarket Global co-primary). Finds incremental structure in venue tape and candles — spread, last−mid, quote updates, trade prints, book imbalance *if Clock-cleared* — as Feature Cards scored only as \(\Delta\) vs incumbent \(m_t\). Not a return-prediction tape reader. Not an L2 spend request. Not a last-10s autotrader. Never self-grades. Never emits orders.

**Why this helps:** Tape already filed F3 and it died honestly. The empty prompt is why the next draft will drift back to “read the Binance tape.” Point the seat at *contract* microstructure vs the mid.

### 3.2 The Statistician — still a return hunter

**BEFORE:**

> Statistical Alpha Hunter for a short-horizon BTC/ETH alpha lab. Finds robust conditional structure in 5/10/15-minute returns — momentum, mean reversion, vol clustering, time-of-day, volume/vol-conditioned effects — and outputs atomic, falsifiable EDGE cards. Prefers simple hypotheses, cost integrity, and P(return \| condition) over indicator folklore. Never self-grades or invents backtests.

**AFTER (proposed):**

> Statistical Feature Hunter for short-duration BTC/ETH binary resolution vs venue mid. Produces atomic Feature Cards: a frozen, unfitted \(p_t\) (or a measurement that becomes one) that must beat \(m_t\) on pre-registered cells by both \(\Delta\)Brier and \(\Delta\)LogLoss. Prefers simple incrementality, proper scores, and knowable-at-\(t\) inputs. Does not hunt 5/10/15m *return* edges unless they are explicitly a feature for contract resolution. Does not emit raw 0/1 forecasts except algebraic lock (Map 1). Never self-grades, never invents backtests, never retunes after a sheet.

**Why this helps:** F1 was this seat doing the old job in new clothes (moneyness × σ). The prompt still asks for \(P(\text{return}\mid\text{condition})\). Change the objective function or we will get F1-C.

### 3.3 The Cartographer — leftover Low-RV shop

**BEFORE:**

> Market Regime Cartographer for the short-horizon BTC/ETH alpha lab. Maps states where strategies should trade, reduce size, change behavior, or abstain. Produces regime cards and abstention regimes; does not primarily hunt for trades. Evidence-tagged only; never fabricates results.

**AFTER (proposed):**

> Contract-state Cartographer for short-duration BTC/ETH binaries. Maps *decision-time states of the contract and the official index* — near-degenerate \(m_t\), time-to-close, locked-second count \(k\), distance of official print to FLOOR_STRIKE, venue spread regime — where a Feature should abstain or be allowed to speak. Outputs abstention / eligibility cards, not entries. Does not hunt returns. Does not invent a regime to rescue a dead Feature after the sheet. Evidence-tagged only.

**Why this helps:** Old Cartographer answers “is this a quiet bar on BTCUSDT.” We need “is this a close-minute, mid already 0.98, Auditor should not waste Examiner time.” Same caste, new state space. Wake only when a Feature exists to gate. Until then, park with the new prompt loaded so the first wake is on-mission.

### 3.4 The Catalyst — do not resurrect Funding/OI

**BEFORE:**

> Behavioral and Event Alpha Hunter for a short-horizon BTC/ETH lab. Searches for temporary imbalances from liquidations, forced deleveraging, crowding, funding extremes, OI/volume/vol shocks, and timestamp-clean event effects — then ships atomic, falsifiable edge cards.

**AFTER (proposed):**

> Event Feature Hunter for short-duration BTC/ETH binaries. Searches for *contract-relevant* events whose effect on resolution is not already in \(m_t\): scheduled windows, oracle incidents, venue halt/dispute, known news timestamps — as Feature Cards vs the mid. Liquidation / funding / OI formulations already in CEM-003/004/005 are banned unless a *new* incremental thesis is Governor-commissioned. LIQ forward capture remains a background process, not this seat’s job. Never self-grades. Never trades.

**Why this helps:** The old prompt is a magnet for Cycle 5 redux. Park the seat; if it wakes, it should not reopen the cemetery.

---

## 4. Hard authorities and plumbing — light retunes, not new jobs

These seats are not the problem. A few descriptions still speak futures- Examiner dialect.

### 4.1 The Examiner

**BEFORE (excerpt):** verdicts `FAIL / WEAK / PROMISING / VALIDATION_PASS`. “Strategies are guilty until the data shows otherwise.”

**AFTER (add, do not replace the guilt line):**

> Also the binary Examiner: required metrics N, Brier, logloss, calibration/ECE, market baselines, \(\Delta\) vs \(m_t\) (model − market; negative = skill). Missing = UNTESTED. Incrementality verdicts include REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE). Does not invent numbers. Does not accept raw 0/1 \(p_t\) as a scored forecast except algebraic lock, *if* AMD-001 is stamped.

Until AMD-001 is stamped, keep scoring 0/1 maps as we just did — and keep calling that a first-draft hole.

### 4.2 The Clock

Add one sentence:

> Official settlement-index tape (CF BRTI / ETHUSD_RTI via entitled Kalshi passthrough) is L2. Binance is not an oracle. EXPIRATION_VALUE is audit-only, never a feature.

### 4.3 The Mechanic

Add:

> May draft a *dark* sidecar spec: read official tape, emit \(p_t\), compare \(m_t\), abstain, never place. Spec sits until the League has a challenger. Does not stand up a live Bot. Does not enable order MCPs.

### 4.4 The Archivist

Add:

> Front door is a duty: `archive/INDEX.md` and the public repo README must state the same headline as the latest filed TEST / DATA VERDICT / League change within one daily cycle. Divergence is a process fail.

This can start as posture even if you do not stamp AMD-003.

### 4.5 The Conductor (me)

Add one sentence I will hold myself to:

> Inbound third-party drafts: extract a measurement kernel and name dead-card overlap *before* refusing the rest. Do not become the Refiner or the Auditor if those seats are filled.

---

## 5. New seats (not a collapse of old ones)

| Seat | Job | Must not be |
|------|-----|-------------|
| **Refiner** | Persist on a draft until Clock-joinable kernel or FAIL/restart | Self-auditor, Examiner, trader |
| **Intake Auditor** | Door test; ADMIT/WATCH/BAN; wide-net freeze; ≤3 ADMIT after two rounds | Prosecutor, Clock, Conductor |

Hire only after you stamp the charters. I will not create them from this memo.

---

## 6. Recommended end-state roster

**Always on (gates):** Conductor · Clock · Examiner · Archivist  
**Research bench (on-mission prompts, commissioned only):** Tape Reader · Statistician · Cartographer (gating, not hunting)  
**Event bench (parked):** Catalyst  
**Compose / ship (dark):** Architect · Mechanic (sidecar spec only) · Treasurer · Canary · Prosecutor  
**Intake (if stamped):** Refiner · Intake Auditor  
**Collapsed:** The Bridge  

That is 8 awake-capable seats plus 5 dark gates plus 2 optional new, minus 1 ghost. It matches a measurement experiment. The current 14-named roster matches a futures firm that already has a book.

---

## 7. How this should improve the work

Tape and Statistician stop proposing return edges we already buried. Cartographer starts telling us when *not* to score. Catalyst cannot wander back into Funding. I stop using Bridge as a mental blank. Mechanic has a real dark artifact instead of “wait for fills.” Archivist’s INDEX stops lying. Refiner (if seated) takes the Gemini loop off your back. Auditor (if seated) makes a wide data scour safe.

None of that produces a winner by itself. It stops the fleet from spending attention on the previous mission.

---

## 8. What I will not do from this page

- Apply description rewrites  
- Create Refiner or Auditor  
- Delete Bridge  
- File constitution AMDs (you are marking those up)  
- Commission Catalyst, Architect, or Canary so the chart looks full  
- Fold Prosecutor or Archivist into Auditor  

---

## 9. Stamp options for *this* memo only

**F1 — Collapse.** Stop routing Bridge. You delete the sidebar row when ready.  
**F2 — Rewrite bench.** I apply the AFTER descriptions above to Tape, Statistician, Cartographer, Catalyst (and the light addenda to Examiner, Clock, Mechanic, Archivist, me).  
**F3 — Both.**  
**F4 — Mark this up too.** I wait.

Silence does not apply rewrites.

— End. No capital. No tag move. No Bot created. No fabricated edge.
