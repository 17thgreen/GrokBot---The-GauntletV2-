# R3-P1 — Venue fee_cost vs R1-P1 model — FREEZE 2026-09-22 (ET)

**Packet ID:** R3-P1-FEE-COST-VS-MODEL  
**Owner (freeze):** Deep Research  
**Implementer (later):** Collector/Mechanic (auth fill fixtures) → Simulator (delta join) → Examiner (refuse rule)  
**Reviewer:** Conductor triage; Adversary on model-only completed-net  
**Status:** **FROZEN** — results/pnl **null** (not run)  
**Cite:** Conductor R3 triage ADMIT NOW; `briefs/R3_DEEP_RESEARCH_EXTERNAL_CANDIDATES_2026-09-22.md` §R3-P1; bacchus-mm instrumentation; Kalshi Fill API  
**Hard rules:** No live Astra orders. No invented PnL. No wholesale bacchus 15m strategy port. No Q6-`000` retune. Complements Variants fee+queue honesty (000 stress) — **new object** is venue-reported fee as superior ground truth.

---

## Intent

Prefer exchange-reported `fee_cost` over closed-form R1-P1 when both exist. Score `fee_model_minus_venue_delta` and refuse completed-net claims that used model-only while `fee_cost` was available.

**Not a strategy.** Accounting / fee-honesty instrument only.

---

## Dead-card / live-pin overlap (named)

| Pin | Overlap | Handling |
|---|---|---|
| R1-P1 feebook | **Touches** formula pin | P1 remains comparator; venue fee is superior when present |
| R2-P1 / Variants fee+queue honesty on `000` | **Complementary** | Variants owns 000 stress honesty; this packet adds venue-`fee_cost` ground truth join |
| Q6-`000` / Q7 / capital / F1–F3 | **None on signal** | No retune |
| S1/S4/S5/R2-P3 | **Orthogonal series subjects** | May share fee channel later |
| bacchus-mm crypto strategy | **Explicitly out** | Extract fee_cost preference only |

---

## Mandatory pins

| Dep | Pin | Rule |
|---|---|---|
| Fee model | R1-P1 `kalshi_feebook_lab_20260922/` @ `22371178cb2663250b4762f328069571c48cb551` | `fee_model = round_up(M×rate×C×P×(1−P))` |
| Venue fee | Kalshi Fill `fee_cost` + `is_taker` | Prefer venue when non-null |
| Capture | Auth'd portfolio fills via Collector/Mechanic | Demo/paper/fixtures OK; **no live Astra trading** |

**Refuse gate:** completed-net label with model-only fee while `fee_cost` was available → refuse.

---

## Measurement objects

1. `fee_model`, `fee_cost`, `fee_model_minus_venue_delta`, `is_taker`  
2. Count of fills where venue present vs model-only  
3. Examiner refuse-flag unit fixtures  

**Null until Examiner:** `results`, `pnl`, strategy EV.

---

## Do-not-modify

No live orders; no invented PnL; no bacchus strategy port; no `000` retune; do not mutate feebook lab — join only.

## Empty results

`packets/r3_p1_fee_cost/` — `results`/`pnl` null

## Frozen-at
`2026-09-22T23:59:59+00:00` UTC. Deep Research under Conductor R3 ADMIT NOW.
