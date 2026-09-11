# Provisional Measurement Package — EDGE-20260910-001
**Package ID:** PROV-MEAS-20260910-001  
**Locked by:** Logan + Conductor · 2026-09-10 UTC  
**Status:** HARNESS_DEFINED · MEASUREMENT = UNTESTED  
**Rule:** Every non-observed execution input is **[A] ASSUMPTION**. No invented [V] fills, fees, or Sharpes.

---

## 0. Purpose & ceiling

This package lets the lab measure EDGE-20260910-001 **without locking a production venue**.

| Stage allowed under this package | Allowed? |
|----------------------------------|----------|
| RESEARCH TEST (provisional) | Yes, after Clock protocol review + Examiner code run |
| VALIDATION (provisional) | Yes, same [A] economics |
| SEALED HOLDOUT (provisional sample split) | Yes, on whatever series is used |
| Promotion beyond provisional validation | **No** |
| Mechanic EXECUTABLE verdict on real venue | **No** until venue-specific rerun |
| Capital / Treasurer | **No** |

When a real venue + data path lands: **Clock + Examiner must rerun from raw venue data** under venue-specific fees, timestamps, fills, latency. Preserve this provisional result for assumption-vs-reality comparison (`PROV_VS_REAL` audit later).

---

## 1. Venue-specificity gate (exception check)

**Question:** Is EDGE-001 inherently venue/microstructure-specific such that abstracting the venue destroys the mechanism?

**Conductor ruling [I]:**
- **Claim under test (narrow):** conditional sign-continuation of returns given trailing low RV vs high RV, BTC and ETH separate, 5/10/15m. This is a **price-series / statistical** claim measurable on any honest OHLCV with exchange event timestamps.
- **Mechanism story (OF persistence in calm tape):** partially microstructure; **OHLCV cannot verify OF**. Examiner measures the conditional-return claim only; does **not** validate the OF narrative.
- **Not like EDGE-005/006:** those require depth/aggressor semantics → venue/L2 before test.
- **Ruling:** Provisional OHLCV measurement **allowed**. Do **not** lock Binance/Coinbase/etc. merely for candles. Any later claim of “order-flow imbalance” remains [H] until microstructure data exists.

If future evidence shows the effect is pure venue artifact, Clock/Examiner may QUARANTINE provisional results at rerun.

---

## 2. Sample boundaries (pre-registered — before seeing results)

Boundaries are **fractional / structural**, not tied to a named venue calendar until a DATA-* series is attached.

### 2.1 Attachment rule
When a provisional series `DATA-PROV-*` is registered:
1. Sort bars by exchange event time ascending.
2. Drop incomplete warmup prefix per §5 (W_max, L_max).
3. Apply splits **only after** warmup drop, on the remaining timeline.

### 2.2 Split fractions (locked)
| Slice | Fraction of post-warmup bars | Use |
|-------|------------------------------|-----|
| RESEARCH | first **60%** | Hypothesis exploration / parameter grid under Examiner protocol |
| VALIDATION | next **20%** | One-shot confirmation; no re-optimizing W/Q_lo/L from this slice |
| SEALED HOLDOUT | final **20%** | Untouched until Conductor explicitly opens holdout protocol |

**[A]** Fractions chosen for first lab harness; may be revised only by Logan/Conductor **before** any results on a given DATA-* are seen. Once Examiner has run on a series, splits for that DATA_ID are frozen.

### 2.3 Instrument separation
BTC and ETH: **separate** full pipelines. No pooled-only claim. Joint reporting only as side-by-side.

### 2.4 Time-half split (within RESEARCH, diagnostic)
Also report first-half vs second-half of RESEARCH slice (50/50) as robustness diagnostic — not a second optimization surface.

---

## 3. Provisional execution economics — all [A]

Units: **basis points of notional per round-trip** unless noted. Close-to-close signal; entry at decision close; exit at horizon close (per Edge Card).

### 3.1 Fees [A]
| Item | Assumption | Tag |
|------|------------|-----|
| Round-trip fee (enter+exit) | **4.0 bps** | [A] |
| Rationale | ~2 bps taker each side, mid-tier perp schedule abstraction | [A] |
| Maker-only variant | **not** used in base case (signal is urgency-at-close) | [A] |

### 3.2 Spread [A]
| Item | Assumption | Tag |
|------|------------|-----|
| Half-spread paid at entry | **1.0 bp** | [A] |
| Half-spread paid at exit | **1.0 bp** | [A] |
| Round-trip spread | **2.0 bps** | [A] |
| Rationale | Abstract continuous book; not venue L1 | [A] |

### 3.3 Slippage [A]
| Item | Assumption | Tag |
|------|------------|-----|
| Extra slippage beyond spread, round-trip | **1.0 bp** | [A] |
| Rationale | Small clip, no impact model | [A] |

### 3.4 Latency [A]
| Item | Assumption | Tag |
|------|------------|-----|
| Signal→arrival | **500 ms** | [A] |
| Edge decay treatment | For provisional harness: **no intra-bar path**; latency stress widens effective cost only (see §6), does not invent mid-path prices | [A] |
| Rationale | Without L2 path, cannot simulate queue; cost proxy only | [A] |

### 3.5 Funding / basis [A]
| Item | Assumption | Tag |
|------|------------|-----|
| Funding | **0** for v0 (flat by close t+h; h≤3×5m ≪ typical funding interval) | [A] |
| If a trade spans a known funding print in data | subtract realized funding when timestamps exist; else keep 0 and flag | [A] |

### 3.6 Base round-trip cost stack
```
C_base = fees + spread_rt + slippage
       = 4.0 + 2.0 + 1.0
       = 7.0 bps per round-trip   [A]
```
Net provisional edge uses sign-aligned forward return in bps minus `C_base` (and stress multiples).

### 3.7 Size [A]
| Item | Assumption | Tag |
|------|------------|-----|
| Clip | **1.0** unit notional (normalized) | [A] |
| Impact | **0** (size ≪ depth assumed) | [A] |

---

## 4. Minimum sample / trade-count gates

Pre-registered. Fail = do not call PROMISING / VALIDATION_PASS.

| Gate | Threshold | Applies |
|------|-----------|---------|
| Min signals in RESEARCH (per instrument) | **200** | else UNTESTED / FAIL-INSUFFICIENT |
| Min signals in VALIDATION (per instrument) | **50** | else cannot provisional-validate |
| Min signals in SEALED HOLDOUT (per instrument) | **50** | else holdout inconclusive |
| Min distinct UTC days with ≥1 signal (RESEARCH) | **20** | kills “≤5% of days” concentration cousin |
| BTC and ETH both meet mins for any cross-instrument claim | required | else instrument-limited conclusion only |

If a DATA-* series is too short: Clock may CONDITIONAL-approve research-only; Conductor will not open holdout fictionally.

---

## 5. Parameter perturbation protocol (pre-registered)

Base grid from Edge Card — Examiner runs **all** cells; no cherry-pick after seeing P&L.

| Param | Grid | Pass rule |
|-------|------|-----------|
| W | {12, 24, 48} | Sign of (lowRV − highRV) continuation gap stable on ≥2 of 3 |
| Q_lo | {0.25, 0.33, 0.40} | Same; single-quantile cliff = overfit flag |
| L | {288, 576} | Same |
| h | {1, 2, 3} | Report **separately**; success at one h ≠ success at all |
| ε | {1 tick equiv, 2 tick} abstracted as {small, 2×small} return threshold | Must not drive result |

**Warmup:** require `max(W)+max(L)` completed bars before first eligible signal.

**Primary cell for headline (pre-registered, not chosen post-hoc):**  
`W=24, Q_lo=0.33, L=288, h=1, ε=small`  
All other cells = robustness. Headline may not silently switch to best cell.

---

## 6. Cost stress (locked)

For every instrument × horizon × primary cell (and summary across grid):

| Stress | Cost used | Tag |
|--------|-----------|-----|
| 1× | `C = 7.0 bps` | [A] |
| 2× | `C = 14.0 bps` | [A] |
| 3× | `C = 21.0 bps` | [A] |

Also report **gross** (C=0) as diagnostic only — **never** a promotion input.

Latency stress (cost proxy only): add **+1 bp / +3 bp** to C at 1× as sensitivity rows labeled LATENCY_STRESS_[A] — not a third promotion axis.

---

## 7. Metrics Examiner must output (code-measured only)

Per instrument × horizon × slice × cost stress:
- Signal count, distinct days
- Mean sign-aligned forward return (gross bps)
- Mean net = gross − C
- Hit rate (optional diagnostic; **not** objective)
- Low-RV vs high-RV continuation gap + bootstrap or Newey-West CI (method stated in code)
- Time-half stability (RESEARCH)
- Parameter-grid stability summary

**Forbidden:** LLM-estimated Sharpes, invented fills, hand-wavy p-values without code.

---

## 8. Exact failure / pass criteria (provisional)

### 8.1 FAIL (→ cemetery candidate / no promotion)
Any of:
1. RESEARCH signal count < minimum (§4)
2. At **1×** costs, primary cell net mean ≤ 0 on RESEARCH for an instrument under test
3. Low−high RV gap CI covers 0 on RESEARCH (primary cell) after pre-registered CI method
4. Effect present on ≤5% of RESEARCH days (concentration kill)
5. Parameter grid: fewer than 2 of 3 W values keep gap sign (overfit flag)
6. Placebo (shuffled RV ranks) matches or beats real gap within CI noise
7. VALIDATION (if reached): primary cell net ≤ 0 at 1× **or** gap CI covers 0

### 8.2 WEAK
Passes FAIL gates on gross or only at optimistic cells; fails 2× cost stress; fragile across h; one instrument only.

### 8.3 PROMISING (provisional)
All of:
1. RESEARCH mins met (per instrument claimed)
2. Primary cell net > 0 at **1×** and **2×** on RESEARCH
3. Gap CI excludes 0 on RESEARCH
4. ≥2/3 W grid keeps gap sign; Q_lo not a single-point cliff
5. Not concentrated in ≤5% days
6. Placebos do not reproduce the gap
7. VALIDATION: net > 0 at 1× and gap CI excludes 0 (primary cell)

**3× stress:** must be reported; failure at 3× alone → WEAK not FAIL if 1×/2× hold.

### 8.4 VALIDATION_PASS (provisional only)
PROMISING criteria + VALIDATION slice pass.  
**Ceiling:** cannot advance to venue-live stages on this package alone.

### 8.5 SEALED HOLDOUT
Not opened in the first RESEARCH TEST route. Separate Conductor order required. Opening criteria: provisional VALIDATION_PASS + Logan explicit approve. Holdout failure demotes regardless of RESEARCH charm.

---

## 9. Abstention overlays (007 / 008)

When testing 001:
- **007 / 008** may be applied as optional filters in a **pre-registered ablation**: base 001 vs 001∧007 vs 001∧007∧008.
- Overlay parameters must be fixed before results; no tuning on VALIDATION/HOLDOUT.
- Overlays cannot rescue a FAIL on base 001 to PROMISING without Conductor note (abstention ≠ alpha).

---

## 10. Required artifacts

| Artifact | Owner |
|----------|-------|
| This package (immutable once measurement starts on a DATA_ID) | Conductor |
| `DATA-PROV-*` registration | Archivist + Logan path |
| Clock DATA VERDICT on series + protocol | Clock |
| Examiner code + TEST-* record | Examiner |
| Preserve provisional JSON/MD results under `tests/` | Archivist |
| Later `PROV_VS_REAL` comparison | Conductor + Examiner |

---

## 11. Explicit non-claims

- Provisional net ≠ executable alpha
- OHLCV conditional autocorr ≠ proven order-flow mechanism
- Assumed 7 bps ≠ any venue’s true cost
- Consensus among agents ≠ evidence


---

## Amendment A1 — Forward holdout & cross-venue (2026-09-10)

See `/workspace/lab/governance/CONSTITUTIONAL_AMENDMENT_FORWARD_AND_CROSS_VENUE.md`.

Under this provisional package:
- Historical 60/20/20 sealed holdout remains in force for DATA-PROV series.
- **Capital promotion is impossible** under provisional economics alone.
- Before any capital path: **cross-venue replication** + **future sealed forward window** after spec freeze.
- Binance (or any) provisional reference ≠ venue marriage.
- Positive OHLCV on EDGE-001 ≠ confirmed OF mechanism ([H]).
