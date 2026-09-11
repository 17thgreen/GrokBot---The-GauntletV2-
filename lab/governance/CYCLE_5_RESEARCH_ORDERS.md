# RESEARCH PRIORITIES — Cycle 5 (Catalyst / positioning stress)
Opened 2026-09-11 by Logan + Conductor.
Institutional baseline: `gauntlet-v2.0-alpha` (`INSTITUTIONAL_LOCK_2026-09-11.md`). Amendments non-retroactive (`AMENDMENT_RULE.md`).

## Objective (explicit)
**Not** “make EDGE-009/010 pass” and **not** a rescue of dead Tape or OHLCV cemetery.
**Yes:** Determine whether **positioning stress / forced-flow** information has **incremental** predictive value beyond OHLCV and ordinary trade flow at **5 / 10 / 15m** (horizons reported **separately**).

If Catalyst labels add nothing beyond the co-occurring price/volume (or trade-flow) move → classify **REDUNDANT** and kill cheaply before capital or L2 spend.

## Priorities (research order)
1. **Liquidation bursts / deceleration** — forced-flow exhaust then partial reversion (primary family for EDGE-20260910-009 lineage).
2. **OI shocks / OI–price divergence** — open-interest jumps or OI moving against price; atomic cards if not already covered.
3. **Funding extremes** — settled, knowable-at-t funding extremes alone (control vs interaction).
4. **Funding × OI** — crowded inventory (primary family for EDGE-20260910-010 lineage).
5. **Forced deleveraging / crowded unwind** — broader unwind packaging only after (1)–(4) atomicity is clear; do not blend into a kitchen-sink signal.

## Explicit control (mandatory)
Does Catalyst / positioning-stress info add value **beyond the co-occurring price/volume move** (and, where available, ordinary trade-flow features from DATA-PROV-TRADES-001)?

| Control | Rule |
|---------|------|
| Matched OHLCV placebo | High-range / high-volume / return-impulse bars **without** Catalyst event labels |
| Trade-flow nested | Where trades exist: Catalyst feature must beat ordinary aggressor/volume features already tested |
| Label ablation | Funding-only vs funding×OI; liq-label vs range-matched no-liq |
| Verdict if fail | **REDUNDANT** → cemetery / stand-down; do not “enrich” with L2 |

## Hard locks (Conductor cannot waive)
- **EDGE-20260910-005 / 006:** remain **UNMEASURABLE WITHOUT L2**. Frozen cards stay frozen. No trade/OHLCV proxy rewrite.
- **No L2 acquisition** without a **surviving mechanism case** that justifies book-state spend (Cycle 4 doctrine stands).
- **No rescue** of **CEM-20260911-001 / CEM-20260911-002** (Tape incremental FAIL) or the **OHLCV cemetery** (CEM-20260910-001/002/003 and kin).
- **No Cartographer rescue** of dead Tape — Cartographer maps abstention/regimes; does not revive killed trade-flow theses.
- **No silent rewrite** of EDGE-009/010 to fit convenient columns. Versioning (new card / explicit VERSION) if SIGNAL, knowability, or venue lock must change — never mutate frozen hypothesis text in place to chase data.

## Existing Catalyst cards — status recommendation (skim only; files untouched)

| EDGE | Informal | Cycle-5 fit | Recommendation |
|------|----------|-------------|----------------|
| **EDGE-20260910-009** | CAT_LIQ_EXHAUST — liq burst + same-direction impulse + aggression decelerate → fade | Priority (1); placebo-without-liq already in FALSIFICATION | **KEEP AS HYPOTHESIS** — valid as-is for Cycle 5 intake. **VERSION** only if Clock/DATA registration forces SIGNAL/knowability/venue changes (do not silent-edit). **RETIRE** not indicated (UNTESTED; not cemetery). |
| **EDGE-20260910-010** | CAT_FUND_OI_CROWD — funding extreme persistence × elevated OI → against crowded side | Priorities (3)/(4); funding-only ablation already in FALSIFICATION; 5m secondary/skeptical | **KEEP AS HYPOTHESIS** — valid as-is. **VERSION** if funding settlement convention, OI timestamp semantics, or “no future funding leak” Clock rules require SIGNAL text change. **RETIRE** not indicated. |

Both remain **PRIMARY_CANDIDATE / HYPOTHESIS / CLEAR_TO_TEST** pending distinct Catalyst DATA-* + Clock VERDICT. Venue, lineage, and costs stay **[U]** until registered.

## Data discipline
- **Distinct DATA-* family** — provisional stub: `DATA_PROV_CATALYST_001_SPEC.md` → register as **DATA-PROV-CATALYST-001** (or Archivist-assigned sibling). **Not** merged into DATA-PROV-001 (OHLCV) or DATA-PROV-TRADES-001.
- **Clock audit** before Examiner: event-time vs receive-time; ordering; duplicates; venue clock; bar alignment; knowability before entry.
- **Event timestamps** honest and immutable; **venue/source** explicit per series.
- **No future funding leak** — only **settled** funding prints knowable at decision t; no using the not-yet-settled interval’s eventual rate.
- **No inferred liquidations** if the card claims **actual** liquidation events (EDGE-009 claims venue liq feed — do not synthesize liq from price wicks).
- **Primary cell pre-register** before RESEARCH TEST (horizons, side splits, cost stack, Δ_exec if applicable).
- **OHLCV + trade-flow redundancy controls** mandatory (see Explicit control).
- **Horizons separate** — 5m | 10m | 15m never pooled as a single claim.
- **Holdout sealed** — align seal policy to existing SEAL_LOCK calendars where timestamps allow; researchers do not inspect holdout.
- **Cross-venue + forward** before capital (`CONSTITUTIONAL_AMENDMENT_FORWARD_AND_CROSS_VENUE.md`). Provisional reference venue ≠ venue marriage.

## Routing (gated)
```
Catalyst proposes / refreshes Edge Cards
        → Archivist pretest search
        → Clock DATA VERDICT on Catalyst DATA-*
        → Conductor routes Examiner (RESEARCH TEST)
```
Default: no whole-team chat (`ROUTING.md`). Hard authorities (Clock / Examiner / Prosecutor / Mechanic / Treasurer) non-waivable.

## Dual hypotheses (institutional lock §13)
| Track | Cycle 5 question |
|-------|------------------|
| **Market** | Does forced-flow / positioning-stress info beat OHLCV (+ trade-flow) at 5/10/15m after costs? |
| **Institutional** | Did distinct DATA family, Clock knowability (esp. funding), redundancy→REDUNDANT kills, and non-rescue of cemetery work as designed? |

## Attention lock
| Bucket | Items |
|--------|--------|
| **PRIMARY** | Catalyst DATA-* registration stub → Clock; incremental cards on priorities (1)–(4); EDGE-009 / EDGE-010 KEEP AS HYPOTHESIS pending data |
| **DATA-BLOCKED** | EDGE-005 / 006 (UNMEASURABLE WITHOUT L2) |
| **DARK / NO RESCUE** | EDGE-002; CEM-20260910-*; CEM-20260911-001/002; dead Tape revival via Cartographer |
| **CEMETERY** | OHLCV + Tape incremental kills stand; amendments do not rewrite prior verdicts |

## Next orders (operational)
1. Archivist: index Cycle 5 orders; do **not** edit EDGE-009/010 bodies.
2. Catalyst + Clock: complete first provisional registration fields per `DATA_PROV_CATALYST_001_SPEC.md` (**spec only** — no market-data fetch in this commission).
3. Conductor: route Examiner only after Archivist CLEAR/WARN-ack + Clock VERDICT on Catalyst DATA-*.
4. No L2 acquisition; no cemetery/Examiner output mutation under this cycle open.

*End Cycle 5 research orders.*
