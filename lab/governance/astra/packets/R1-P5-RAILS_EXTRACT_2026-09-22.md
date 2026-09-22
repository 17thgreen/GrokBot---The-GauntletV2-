# R1-P5-RAILS — EXTRACT + INSTRUMENT SPEC 2026-09-22 (ET)

**Owner:** R&D Variants (freeze / pin ownership)  
**Implementer:** Simulator (+ Collector freshness hooks) after R1-P1  
**Reviewer:** Examiner (Kalshi) / Adversary spot-check  
**Status:** QUEUED — depends on R1-P1 fee algebra  
**Cite:** `SIBLING_DEATHMATCH_REVIEW_2026-09-22.md`; `briefs/R1_DEEP_RESEARCH_2026-09-22.md` §R1-P5  
**Hard rules:** Measurement rails only. Not a strategy. No live launcher / no live orders. No Q6/Q7 retune. Do **not** reopen HX spread picker.

---

## 1. Claude queue/fill instrument (`execution.py`)

**Source:** `Claude-SportsBetting…` `src/flatstake/paper/execution.py` @ `claude/kind-hamilton-gdfr9q`

| Parameter | Default | Role |
|---|---|---|
| `queue_ahead_contracts` | **3300** | Measured median resting at best; Astra also uses **10000** stress |
| `fill_participation` | **0.5** | Share of post-queue volume we win |
| `queue_model` | `measured` \| `front` | front = optimistic bound (0 ahead) |
| Same-price keep place | yes | Unfilled same price keeps consumed queue |
| New price / new order | back of queue | Classic anti-invention rule |
| `taker_side` polarity | `"yes"` → fills our **NO**; `"no"` → fills our **YES** | Must have unit assert |

Partial maker fee: `fees.maker(price, got, round_up=False)`.

**Astra use:** instrument for queue-attribution vs assumed early queue 3300/10000 — **not** a strategy claim. Align labels to Q1–Q6 scenario grid without mutating frozen labs.

Local extract: `packets/extracts/claude_execution.py.txt`

---

## 2. Fee-credit floor refuse (spencerfletcher + R1 brief)

Evaluate maker fee with venue rounding; **refuse** quotes whose maker credit floors to zero (no fee-blind “free quote” claims).

Depends on R1-P1 Decimal fee + round_up.

---

## 3. Content-fresh book predicate

Book freshness = content / transaction-time change, **not** WS ping keepalive. Collector hook later; stub interface only in first R1-P5 pass.

---

## 4. Grok MICRO_V1 print-role lab shape (adverse / fee scorecard only)

**Source:** `Grok-Deathmatch` `src/lib/linewright/micro.ts` + `config.ts` `MICRO_V1` @ `main`

| Field | Value | Use |
|---|---|---|
| `takerRate` / `makerRate` | 0.07 / 0.0175 | Fee honesty |
| `nflInplayHours` | 3.25 | Kickoff proxy only |
| `thinN` | 500 | THIN vs scored |
| `surviveRoi` | 0 | Role ROI gate |
| `skipBlockTrades` | true | Filter |
| Verdicts | SURVIVES / FAILS / THIN / CONTROL | Adversary refuse-criteria |

**Scoring discipline (pin):**
- Each print scored as unique maker **or** taker counterparty — **overstates** executable size; size-weighted ROI required beside 1-lot.
- Fees: taker ceiled; maker unrounded (Grok paper convention).
- CONTROL strategies never SURVIVES.
- Evidence stage: `HISTORICAL_OUT_OF_SAMPLE` only — not Examiner completed profit for Astra incumbent.

**Do not reopen:** HX spread picker (`HX_SPREAD_V1` / holdout −6.7%); weather cheap-YES lottery; directional pickers. MICRO is orthogonal measurement / Adversary scorecard, **not** a Q6 challenger.

Local extracts: `packets/extracts/grok_micro.ts.txt`, `packets/extracts/grok_config_MICRO_V1.json`

---

## Explicit non-actions

- No live `KalshiExecutionAdapter` implementation.
- No import of Claude paper MM ROI / “+34%” framings.
- No silent retune of Q6 `000` or Q7 arms A–D.
- Event YES/YES netting (`account.py`) = **post-Q7 Adversary reference only**, not this packet’s code.

## Done =

Instrument stubs + tests in a new rails lab dir (or extensions under feebook lab) with freeze-before-results; queue polarity tests green; MICRO verdict helpers optional in same PR or follow-on. Variants reports Conductor when on disk.
