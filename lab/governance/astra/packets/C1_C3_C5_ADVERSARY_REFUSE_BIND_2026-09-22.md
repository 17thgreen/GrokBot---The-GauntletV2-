# Adversary refuse-bind — C1 / C3 / C5 cash-cow freezes
**Date:** 2026-09-22 (America/New_York)  
**Packets:** C1-KXUFCFIGHT-MEAS · C3-KXHIGHNY-MEAS · C5-KXBTC15M-MEAS (**FROZEN** — Conductor ACCEPTED / ADMIT FREEZE NOW)  
**Owner:** The Adversary · **Reviewer:** Conductor  
**Cite:** `C1_KXUFCFIGHT_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md` · `C3_KXHIGHNY_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md` · `C5_KXBTC15M_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md` · `briefs/CASH_COW_FREEZE_ACK_2026-09-22.md` · `SCOUT_TRIAGE_CASHCOW_2026-09-22.md` · stubs `scout_c1_kxufcfight/` · `scout_c3_kxhighny/` · `scout_c5_kxbtc15m/`  
**Stance:** Bind refuse rules on freeze accept. No verdict change on Q6-000. No orders. No invented edge/PnL. Measurement / provenance refuse — not a strategy kill. Examiner of record unchanged.

---

## Direct answer

**Yes — refuse.**

Adversary **must refuse** any scorecard, brief, or unit note that:

1. **(C1)** Claims a **UFC strategy** / maker EV / “beats `000`” from `KXUFCFIGHT` tape — freeze is fee+queue honesty bakeoff only. Shared **$5k** is a **bakeoff label only**, not a strategy bankroll or capacity claim.  
2. **(C3)** Treats GitHub weather-spread (`Ciarnan-Moloney/Kalshi-Weather-Spread-Algo` or sibling) structure / author figures as **Astra EV** — **HYPOTHESIS ONLY**. Bordering-strike objects are measurement, not imported edge.  
3. **(C5)** Frames `KXBTC15M` as **live crypto trading**, or ports **bacchus** / **kxeth15m** strategy as Astra line — freeze is 15m fee/queue honesty stress only; GET-only public tape.  
4. Invents fills, PnL, OI/liquidity beyond Scout cite / live GET, or scores before Examiner with `results`/`pnl` null.

Label: **measurement / provenance refuse** — not a Q6-000 reopen, not a strategy kill.

---

## Refuse matrix (short)

| Claim | Packet | Adversary stamp |
|---|---|---|
| UFC strategy / maker EV / “beats `000`” | C1 | **REFUSE** — measurement bakeoff only |
| Shared $5k as strategy bankroll / additive capacity | C1 | **REFUSE** — bakeoff label only |
| GitHub weather-spread as Astra EV / edge | C3 | **REFUSE** — hypothesis only |
| Cross-city arb / settlement-penalty EV invented | C3 | **REFUSE** — RESULTS_NULL |
| Live crypto trading / signed order routes | C5 | **REFUSE** / **DENIED** |
| bacchus or kxeth15m strategy port as Astra line | C5 | **REFUSE** port |
| Fee-honest completed-profit | C1/C3/C5 | **REFUSE** without R1-P1 feebook pin |
| Invented PnL / premature scorecard | C1/C3/C5 | **REFUSE** — RESULTS_NULL until Examiner |
| `000` retune / promote / live orders | Suite | **DENIED** (out of scope) |

---

## Simulator spot-check (this wake)

**Simulator units for C1 / C3 / C5:** **NOT_FOUND** / **RESULTS_NULL**.

| Path | State |
|---|---|
| `packets/scout_c1_kxufcfight/results.json` + `results/EMPTY_RESULTS.json` | `status=NOT_RUN` · `results`/`pnl` null |
| `packets/scout_c1_kxufcfight/FROZEN_EXPERIMENT.json` | `FROZEN_NOT_RUN` · packet `C1-KXUFCFIGHT-MEAS` |
| `packets/scout_c3_kxhighny/results.json` + `results/EMPTY_RESULTS.json` | `status=NOT_RUN` · `results`/`pnl` null |
| `packets/scout_c3_kxhighny/FROZEN_EXPERIMENT.json` | `FROZEN_NOT_RUN` · packet `C3-KXHIGHNY-MEAS` |
| `packets/scout_c5_kxbtc15m/results.json` + `results/EMPTY_RESULTS.json` | `status=NOT_RUN` · `results`/`pnl` null |
| `packets/scout_c5_kxbtc15m/FROZEN_EXPERIMENT.json` | `FROZEN_NOT_RUN` · packet `C5-KXBTC15M-MEAS` |
| `astra-science/` / Simulator unit dirs for C1/C3/C5 | **None** |

Collector stubs under `scout_c*/COLLECTOR_STUB.md` are **not** Simulator units and do **not** authorize scoring.

**Spot-check:** **deferred** until Simulator units land. When they do: re-check refuse triggers (UFC strategy claim / $5k bankroll; weather-spread as EV; live crypto / bacchus·kxeth15m port) — do not invent scores.

---

## Explicit non-actions

- No change to Q6-000 KEEP / Q7 KILL_B.  
- No Examiner replacement; results stay null until Examiner.  
- No orders / no live launcher.  
- Does not merge C3 into R3-P3 as a strategy (weather panel material preference only, per C3 freeze).

**Artifact:** `lab/governance/astra/packets/C1_C3_C5_ADVERSARY_REFUSE_BIND_2026-09-22.md`
