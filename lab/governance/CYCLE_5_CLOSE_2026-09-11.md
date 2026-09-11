# CYCLE 5 CLOSE — Outcome B (Funding / OI formulation)
**Document:** `CYCLE_5_CLOSE_2026-09-11.md`  
**Authority:** Logan M (Human Governor) · Conductor close  
**Date (UTC):** 2026-09-11  
**Cycle:** 5 (Catalyst / positioning-stress)  
**Classification:** CYCLE CLOSE · ATTENTION RELIEF  
**RETROACTIVE:** **NO**  
**Baseline:** `gauntlet-v2.0-alpha` **unchanged** (`BASELINE_gauntlet-v2.0-alpha.md` · `INSTITUTIONAL_LOCK_2026-09-11.md`)  
**Does not:** rewrite Edge Card bodies · unseal holdout · acquire L2 · retune killed cells · fetch market data · start Track B Examiner

Opened under `CYCLE_5_RESEARCH_ORDERS.md` / `CYCLE_5_EXECUTION_ORDER_2026-09-11.md`. Cemetery already filed: `CEM-20260911-003` / `004` / `005` (`archive/audit/2026-09-11-CEMETERY-ROUTE-Cycle5-Catalyst-OutcomeB.md`). This file **closes the cycle** and states Outcome B in Governor-operable language. It does **not** replace TEST artifacts as the numeric source of truth.

---

## 1. Outcome B (binding)

**This Funding / OI formulation, on the pre-registered primary cells that were actually tested, did NOT establish sufficient incremental predictive value for promotion.**

| Claim | Binding |
|-------|---------|
| **What was asked** | Does settled-funding / OI-shock / funding×OI information add **incremental** 5/10/15m predictive value beyond OHLCV and ordinary trade-flow after costs, BTC and ETH **separate**? (`CYCLE_5_RESEARCH_ORDERS.md`) |
| **What was measured** | EDGE-20260911-005 (funding extremes), EDGE-20260911-004 (OI shock), EDGE-20260911-006 (funding×OI) under frozen Catalyst splits (`CATALYST_SPLITS_FROZEN_2026-09-11.md`) |
| **Promotion** | **Not earned.** No VALIDATION. Holdout remains **SEALED**. No Champion, no capital path, no L2 spend justified by these cells |
| **Family status** | Deprioritize the **funding/OI futures-edge family** pending a **new orthogonal** card — **do not retune** Z / D / L / Q_oi / T_wait on these cards |
| **What this is not** | Not a proof that positioning-stress information can never have edge. Not a rescue license. Not a rewrite of parents EDGE-20260910-009 / 010 (those remain KEEP AS HYPOTHESIS / UNTESTED) |

**Outcome A** (promote / keep family PRIMARY) is **not** taken.  
**Outcome B** (close cycle; deprioritize this formulation; do not retune) **is** taken.

---

## 2. FAIL-INSUFFICIENT ≠ proven absence of edge

**Explicit (Governor):** a `FAIL-INSUFFICIENT` Examiner verdict is **not** a proof that the mechanism is empty.

| Verdict | Meaning | What it does **not** mean |
|---------|---------|---------------------------|
| **FAIL** (powered) | Primary cell was measurable at pre-registered sample gates and **did not** support the claim (gross/net and/or redundancy) | Not a license to retune the same card |
| **FAIL-INSUFFICIENT** | Sample / distinct-day gates were **not met**; the formulation **did not establish** incremental predictive value **sufficient for promotion** on this cell | **≠ proven absence of edge.** Underpowered. Do not upgrade to `NO_EDGE` by narrative. Do not treat sparse negative diagnostics as a powered kill of the whole family |
| **HISTORICAL_DATA_BLOCKED** | Required DATA-* not available for seal-window RESEARCH | **≠ FAIL.** Unmeasured. Not cemetery |

Operable consequences:

1. Cemetery rows that carry `FAIL-INSUFFICIENT` record **insufficient evidence for promotion**, not a metaphysical “no alpha exists.”
2. Reuse of the **idea** later requires a **new atomic Edge Card** (or, on Track B, a **Feature Card**) that **cites** the CEM ids — not a silent parameter search on the dead card.
3. Mixing `NO_EDGE` and `FAIL-INSUFFICIENT` on one row is a **taxonomy tension**; the TEST artifact is authoritative for which instruments were underpowered vs powered-fail. See §3 pointers. Interpretation of `FAIL-INSUFFICIENT` is this section — not a cemetery rewrite.

Pointer (cemetery): `CEM-20260911-003`, `CEM-20260911-005`.

---

## 3. Disposition table (Cycle 5 Catalyst cells)

Numeric sample, horizons, BTC vs ETH, cost stack, redundancy controls, and retest conditions live on the **TEST artifacts**. This table is an index. Do **not** treat the close doc as a second scoreboard.

| Informal | EDGE | TEST | CEM | Examiner (headline) | Close status |
|----------|------|------|-----|---------------------|--------------|
| CAT_FUND_EXT_C5 | **EDGE-20260911-005** | **TEST-20260911-003** | **CEM-20260911-003** | FAIL (per-symbol **FAIL-INSUFFICIENT**; BTC/ETH gross-sign disagree) | Outcome B — **not promoted**. `FAIL-INSUFFICIENT ≠ proven absence` (§2) |
| CAT_OI_SHOCK_C5 | **EDGE-20260911-004** | **TEST-20260911-004** | **CEM-20260911-004** | FAIL (powered; gross≤0; nested/REDUNDANT) | Outcome B — **not promoted**. Do not retune |
| CAT_FUND_OI_C5 | **EDGE-20260911-006** | **TEST-20260911-005** | **CEM-20260911-005** | **FAIL-INSUFFICIENT** | Outcome B — **not promoted**. `FAIL-INSUFFICIENT ≠ proven absence` (§2) |
| CAT_LIQ_EXHAUST_C5 | **EDGE-20260911-003** | *(none)* | *(none)* | **HISTORICAL_DATA_BLOCKED** | **Unmeasured.** Not cemetery. LIQ forward continues **passive** (§5) |

Parents (untouched by this close as cemetery targets):

| Informal | EDGE | Status after Cycle 5 close |
|----------|------|----------------------------|
| CAT_LIQ_EXHAUST | EDGE-20260910-009 | KEEP AS HYPOTHESIS / UNTESTED — **do not silent-edit**; not a rescue vehicle |
| CAT_FUND_OI_CROWD | EDGE-20260910-010 | KEEP AS HYPOTHESIS / UNTESTED — **do not silent-edit**; not a retune of 005/006 |

### TEST artifact pointers (binding numeric source)

Preserve **sample / horizons / BTC–ETH split / costs / redundancy / retest** by reading the TEST records — do not re-copy numbers here as truth.

| Cell | Artifacts | What to read there (do not re-litigate here) |
|------|-----------|-----------------------------------------------|
| EDGE-005 / TEST-003 / CEM-003 | `archive/tests/TEST-20260911-003.md` · `TEST-20260911-003-EDGE-20260911-005.md` · `TEST-20260911-003-EDGE-20260911-005.json` · harness `harness/examiner/out/TEST-20260911-003-*` | n / distinct days vs min gates; primary cell `Z,D,L,Δ_exec,h`; C_base + stress; BTC vs ETH gross/net; nested OHLCV + trade-flow + D1=D≥2; holdout SEALED; VALIDATION skipped; retest = new EDGE citing CEM ids |
| EDGE-004 / TEST-004 / CEM-004 | `archive/tests/TEST-20260911-004.md` · `TEST-20260911-004-EDGE-20260911-004.md` · `TEST-20260911-004-EDGE-20260911-004.json` · harness `harness/examiner/out/TEST-20260911-004-*` | n; primary cell `Z,L_oi,Q_lo,T_wait,Δ_exec,h,flush-with-trigger`; C_base; BTC vs ETH; large-\u005c|r\u005c| cohort / OHLCV / trade-flow nested; SORT+DEDUPE; retest = new EDGE citing CEM ids |
| EDGE-006 / TEST-005 / CEM-005 | `archive/tests/TEST-20260911-005.md` · `TEST-20260911-005-EDGE-20260911-006.md` · `TEST-20260911-005-EDGE-20260911-006.json` · harness `harness/examiner/out/TEST-20260911-005-*` | n / distinct days vs min gates; primary cell `Z,D,L,Q_oi,L_oi,Δ_exec,h`; C_base; funding-carry [U]; interaction vs funding-only / OI-only; retest = new EDGE citing CEM ids |
| EDGE-003 | Edge card `archive/edges/EDGE-20260911-003.md` · Clock `data/DATA-PROV-LIQ-001/provenance/DATA_VERDICT_DATA-PROV-LIQ-001.md` | No TEST. Historical RESEARCH **BLOCKED**. Forward capture only |

Splits (frozen; not reopened by close): `governance/CATALYST_SPLITS_FROZEN_2026-09-11.md`.  
Cemetery retest condition (all three filed rows): **NONE** until Conductor commissions a **new** EDGE citing the CEM ids — not parameter retune.

Binary scoreboard was **skipped** on TEST-003/004/005 (no Kalshi / PM contract sample in those TESTs) `[V]`. Track B builds that measurement path (`TRACK_B_ORDERS_2026-09-11.md`) — it does **not** reopen these futures TESTs.

---

## 4. Hard locks after close (Conductor cannot waive)

| Lock | Binding |
|------|---------|
| **No retune** | Do not grid-search Z / D / L / Q_oi / T_wait / h on EDGE-20260911-004 / 005 / 006 to chase a pass. New claim ⇒ new card + pretest vs cemetery |
| **No L2** | EDGE-20260910-005 / 006 remain **UNMEASURABLE WITHOUT L2**. Cycle 5 Outcome B does **not** justify book-state spend |
| **No rescue** | CEM-20260910-001/002/003 (OHLCV) and CEM-20260911-001/002 (Tape) stand. Cartographer does not revive them. Feature Cards on Track B may **reuse signals as forecast inputs** only via `archive/templates/FEATURE.md` — not by rewriting dead Edges |
| **No silent rewrite** | Frozen hypothesis text on 004/005/006/003 and parents 009/010 stays frozen. VERSION / new card if SIGNAL, knowability, or venue lock must change |
| **Holdout** | Catalyst holdout **SEALED**. Not opened for result fishing. VALIDATION was not earned |
| **PROV_VS_REAL** | Preserved as a **future** protocol under a **new** claim + venue economics — not a rescue of these cards |
| **Amendments** | `AMD-20260911-PM-001` / `PM-002` remain **RETROACTIVE: NO**. This close does not rewrite them |

---

## 5. LIQ forward continues **passive**

EDGE-20260911-003 remains **HISTORICAL_DATA_BLOCKED** (`DATA-PROV-LIQ-001` Clock VERDICT: REJECTED for historical seal-window RESEARCH; FORWARD_CAPTURE_ONLY).

| Item | After Cycle 5 close |
|------|---------------------|
| Live `forceOrder` capture | **Continues passively** — do not stop the stream to “close the cycle” |
| Historical RESEARCH TEST on EDGE-003 | **Still blocked** (no paid UM hist; no wick-inferred liqs) |
| Forward-only measurement | **Not commissioned** by this close. Requires later Clock stream-quality audit + Conductor route |
| Paid LIQ / Tardis hist | **Not authorized** |

---

## 6. Dual hypotheses (institutional lock §13) — Cycle 5 close

| Track | Question | Close answer |
|-------|----------|--------------|
| **Market** | Does this Funding/OI formulation beat OHLCV (+ trade-flow) at 5/10/15m after costs on tested cells? | **Not established.** Insufficient incremental predictive value for promotion (Outcome B). `FAIL-INSUFFICIENT ≠ proven absence` |
| **Institutional** | Distinct DATA family, Clock knowability, frozen splits, redundancy→kill, non-rescue of cemetery, non-retroactive baseline? | **Held.** Cemetery filed; holdout sealed; no L2; no retune; `gauntlet-v2.0-alpha` tag **unchanged**; LIQ honest as blocked rather than inferred |

Honest failure to promote is **successful institution-learning**.

---

## 7. Attention lock (post-close)

| Bucket | Items |
|--------|-------|
| **PRIMARY** | **Track B** — prediction-market data + measurement (`TRACK_B_ORDERS_2026-09-11.md`) |
| **PASSIVE** | DATA-PROV-LIQ-001 forward capture (no hist RESEARCH) |
| **DATA-BLOCKED** | EDGE-20260910-005 / 006 (L2); EDGE-20260911-003 historical LIQ |
| **DARK / NO RESCUE** | EDGE-20260910-002; Tape cemetery; OHLCV cemetery; funding/OI **retune** of 004/005/006 |
| **CEMETERY** | CEM-20260910-001/002/003; CEM-20260911-001/002; **CEM-20260911-003/004/005** — stand; amendments do not rewrite |

Cycle 5 Catalyst research attention is **released**. Track B is additive domain work under existing baseline — **not** a new science family (§ Track B orders).

---

## 8. Institutional stamps

| Field | Value |
|-------|-------|
| **RETROACTIVE** | **NO** — past TEST / CEM / EDGE verdicts stand under rules then in force |
| **gauntlet-v2.0-alpha** | **Unchanged.** Do not move, recreate, or silently reinterpret the tag |
| **INSTITUTIONAL_LOCK / AUTHORITY / DOCTRINE bodies** | **Unmodified** by this close |
| **Change control** | `AMENDMENT_RULE.md` — this close is a cycle order, not an AMD |

---

## 9. Pointers (read-only)

| Doc | Role |
|-----|------|
| `CYCLE_5_RESEARCH_ORDERS.md` | Cycle-open objective, hard locks, dual hypotheses |
| `CYCLE_5_EXECUTION_ORDER_2026-09-11.md` | Fetch / Clock / freeze / Examiner gate |
| `CATALYST_SPLITS_FROZEN_2026-09-11.md` | Frozen RESEARCH / VALIDATION / HOLDOUT bounds |
| `TRACK_B_ORDERS_2026-09-11.md` | Successor attention — PM data+measurement |
| `BINARY_EXAMINER_SPEC.md` | Required forecast metrics (missing = UNTESTED) |
| `PREDICTION_MARKET_MISSION_2026-09-11.md` | Domain objective (AMD-PM-001) |
| `AMD-20260911-PM-002.md` | KALSHI + POLYMARKET_GLOBAL co-primary |
| `archive/audit/2026-09-11-CEMETERY-ROUTE-Cycle5-Catalyst-OutcomeB.md` | Cemetery confirm |
| `archive/cemetery/CEM-20260911-003.md` · `004` · `005` | Filed kills (pointer-only edits for FAIL-INSUFFICIENT) |

---

*End Cycle 5 close — 2026-09-11. Outcome B. RETROACTIVE: NO. Baseline `gauntlet-v2.0-alpha` unchanged. No retune. No L2. LIQ forward continues passive.*
