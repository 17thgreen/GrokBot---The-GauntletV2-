# GPT-6-Astra-Deathmatch — Conductor review (2026-09-22)

**Repo:** https://github.com/17thgreen/GPT-6-Astra-Deathmatch  
**Tip (main):** `7da067ada9faf255e672791975c8835959ead75b` (Stern/NFL through Q6; 936-file tree)  
**Domain:** NFL sports prediction-market **maker / allocator** research on Kalshi — **not** BTC 5/10/15m binaries.

## What it is

A reproducible sports PM research lab with frozen experiment stages Q1–Q6, negative findings retained, 94 unit tests on Q6, no live order-enabled strategy validated or deployed. Doctrine matches Gauntlet habits: commit hypothesis before outcomes, separate sim vs live, no inventing holdouts, shared liquidity not double-awarded.

## Current incumbent (Q6)

- Selected: **core allocator** with optional F/P/R features **off**
- Dev sample: **31 NFL games**, shared **$5,000**, **250** event cap, assumed early queue **3,300**
- Simulated completed net: **$345.24** vs original router **$201.52** (queue 10k: $75.90 vs $10.35)
- Explicitly **hypothetical historical execution**, not live P&L
- Freeze pointer: `nfl_factorial_lab_20260921/SHADOW_CANDIDATE_FREEZE.json`

## Declared next (Q7) — PROPOSED, not run

Isolate **actual chosen-pair price check** in a 2×2 (original vs Q6 × check on/off). Same 31 games / capital / caps. See `docs/NEXT_EXPERIMENT.md`.

Parallel unmet gates (from registry + handoff):
1. Durable **GET-only public collector** (none always-on)
2. **Fresh-game / prospective cohort** admission before full T−7d windows (schedule reservation exists; most venue IDs unverified)
3. External kit restore for full replay/ledgers (`provenance/ARCHIVES.json` + `scripts/restore_kit.py`)
4. Live execution / risk limits — **out of research scope** until shadow + fresh data pass

Handoff notes first schedule-only window start **2026-09-22T00:15Z** — missing admission cannot be backdated.

## Fit with Conductor / Gauntlet layout

| Our muscle | Astra analogue |
|---|---|
| Frozen Feature / Wave specs | `EXPERIMENT_SPEC.md` / Q-labs |
| Examiner incrementality | Factorial + baseline router controls |
| Clock / provenance | hashes, manifests, external kit indexes |
| NO TRADE | AGENTS.md forbids live orders under research |
| Cemetery / negatives | failed hyps retained by design |

**Mismatch:** BTC short-horizon binary Gauntlet seats (Tape, Poly L2, mid beat) are the wrong fleet for this. Need sports-PM seats (collector, queue/sim Examiner, shadow ops) — dedicated fleet repo later per Logan.

## Recommended paused→live path (research “live”, not order-live)

1. **Restore kits** if full ledger replay needed; confirm SHA-256 indexes
2. **Freeze Q7 spec in code** then run the 2×2 (no live orders)
3. **Stand up GET-only public collector** + admit a **future** cohort before T−7d (do not backfill missed windows)
4. **Shadow** selected candidate vs original router on fresh public tape
5. Only after shadow + fee/queue/collateral verification: Mechanic/Treasurer-style live gates (separate GO)

## ALMANAC

Remains parked until explicit reopen. Examiner NO_SCORE stands.
