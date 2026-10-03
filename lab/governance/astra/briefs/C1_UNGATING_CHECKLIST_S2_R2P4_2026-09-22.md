# C1 ungating checklist — before S2 / R2-P4 freeze

**Seat:** Deep Research (one-pager for Conductor)  
**Purpose:** What **C1 PIT@CLE smoke** must show before Deep Research freezes `KXNFLSPREAD` (+ `KXNFLTOTAL` if clear) / R2-P4.  
**Locked next freeze:** WAIT → S2 / R2-P4 after this checklist PASSes (Conductor maximize backlog 2026-09-22).  
**Hard rules:** No inventing 429/401 inventory. No orders. No invented PnL. No `000` retune. Do not steal PIT@CLE poll budget for side-market capture until ungated.

---

## Anchor (Scout / ADMIT-1)

| Field | Value |
|---|---|
| Event | PIT@CLE |
| Venue ticker | `KXNFLGAME-26OCT01PITCLE` |
| Kickoff SoT (Conductor lock) | **`2026-10-02T03:15:00Z`** (Kalshi `occurrence_datetime`) |
| T−7d production smoke (Conductor) | **Not before `2026-09-25T03:15:00Z`** (= 2026-09-24 23:15 ET) |
| Scout wall-clock note (superseded for smoke gate) | Earlier Scout calendar wrote T−7d as 2026-09-24 20:15 ET — **prefer Conductor UTC SoT above** for ungating |
| ADMIT-1 prior cite | `2026-09-25T03:15:00+00:00` T−7d aligned with Conductor; recorder HEALTHY standby |
| ADMIT-1 panel | `2026-09-22.1-kalshi-occurrence-sot` · 16 events · GET-only recorder |
| PHI@CHI | **Not** backfilled / out of admit — do not treat as C1 smoke subject |

---

## Must-show smoke (all required unless noted)

### A. Identity + clock
1. **Venue identity stable** for PIT@CLE = `KXNFLGAME-26OCT01PITCLE` (no null / rename churn).  
2. **Kickoff SoT = Kalshi `occurrence_datetime`** used for T− windows (R2-P5 / Clock discipline).  
3. **T−7d boundary crossed or in-window capture healthy** relative to Conductor SoT — production smoke **not before** `2026-09-25T03:15:00Z` (kickoff SoT `2026-10-02T03:15:00Z`).

### B. ADMIT-1 / C1 recorder health
4. Prospective recorder **alive**, GET-only, writing durable DB (ADMIT-1 pattern: `capture.sqlite` growing; not wiped).  
5. **Metadata responses** covering admitted PIT@CLE (and cohort) without silent panel rewrite.  
6. **No second conflicting admit** on a different path treated as live.  
7. Poll budget **not** diverted to S2/R2-P4 capture until this checklist PASSes.

### C. Listing readiness for the next freeze (Scout re-confirm; no invent)
8. `KXNFLSPREAD` listing **200** with open markets on **same-event** (or same-slate) NFL games as ML incumbent — Scout already confirmed SPREAD inventory elsewhere; **re-confirm** at ungating time.  
9. `KXNFLTOTAL` (and team total if desired): **200** with open markets **or** explicit DEFER TOTAL in the S2 freeze (TOTAL was **429** on maximize pass — do not invent).  
10. Series fee metadata readable for SPREAD/TOTAL (expect maker_fees-class; pin via R1-P1 — never inherited Q7 literals).

### D. Process gates
11. Conductor (or Collector) stamps **C1 smoke = PASS** in writing (brief/packet).  
12. R1-P1 feebook + R1-P5 rails pins still current (or Archivist tip).  
13. Dead-overlap **high** (same kickoffs/T−7d as `000`) will be named on S2/R2-P4 freeze — measurement contrast only.

---

## Pass / fail

| Outcome | Action |
|---|---|
| **PASS** (A–D) | Conductor kicks Deep Research → freeze S2 (`KXNFLSPREAD` ± TOTAL if clear) and/or R2-P4 per triage; null results; R1-P1/P5 pins |
| **FAIL / incomplete** | Stay WAIT; no S2/R2-P4 freeze; optional Scout throttle retry on TOTAL/NHL/weather **without** inventing inventory |
| **429 / 401 on side series** | Record honest block; freeze only what Scout confirms; do not ask Logan for RFQ key for this gate |

---

## Explicit non-smoke (do not wait on these)

- R1-P2 challenger bakeoff open  
- RFQ `/communications` 401 clear  
- Scoring S1/S4/S5/R2-P3 (stubs remain NOT_SCORED until panels)  
- Any live order or `000` parameter change  

---

## SoT correction (2026-09-22 evening)

Conductor: ADMIT-1 recorder HEALTHY standby; S2/R2-P4 remains WAIT. Production smoke not before T−7d **`2026-09-25T03:15Z`** (kickoff SoT **`2026-10-02T03:15:00Z`**). Scout’s earlier 20:15 ET wall-clock is noted but **not** the smoke gate.

## Cite

- `SCOUT_BRIEF_2026-09-22.md` · `SCOUT_TRIAGE_2026-09-22.md` · `SCOUT_MAXIMIZE_DELTA_2026-09-22.md`  
- `packets/ADMIT1_2026-09-22.md`  
- `briefs/MAXIMIZE_BACKLOG_2026-09-22.md`  

**Filed-at:** `2026-09-22T23:46:13+00:00` UTC · desk 2026-09-22 ET
