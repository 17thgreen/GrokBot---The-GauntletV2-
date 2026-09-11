# CONTRACT REGISTRY (template)

**Purpose:** Append-only ledger of binary contracts in the working universe.  
**Per-contract body:** `archive/templates/BINARY_CONTRACT.md` (`CONTRACT-YYYYMMDD-NNN`) — **do not duplicate** that schema here.  
**Do not use:** a parallel `CONTRACT.md` template; `BINARY_CONTRACT.md` already is the contract ground-truth card.  
**Active instance (when opened):** `archive/contracts/CONTRACT_REGISTRY.md` (Archivist creates; not opened by this template file).  
**Track B:** first milestone = clean **resolved** historical sample with rules, settlement source, checkpoint \(m_t\), final resolution (`governance/TRACK_B_ORDERS_2026-09-11.md`).  
**RETROACTIVE:** NO. **No market-data fetch** implied by this template.

Venue adapters: `KALSHI` + `POLYMARKET_GLOBAL` co-primary (`AMD-20260911-PM-002`); `POLYMARKET_US` watchlist.

---

## Schema (one row per CONTRACT_ID)

| Column | Meaning |
|--------|---------|
| `CONTRACT_ID` | Archivist-assigned `CONTRACT-YYYYMMDD-NNN` |
| `VENUE_ADAPTER` | `KALSHI` \| `POLYMARKET_GLOBAL` \| `POLYMARKET_US` \| (other registered) |
| `VENUE_NATIVE_ID` | Venue’s own market/contract id |
| `UNDERLYING` | BTC \| ETH \| (explicit other) |
| `TENOR` | 5m \| 15m \| (explicit other) — never pooled as a claim |
| `TITLE` | Short question text (verbatim pointer ok) |
| `STATUS` | OPEN \| CLOSED \| RESOLVED \| VOID \| DISPUTED \| QUARANTINED |
| `RULES_URI` | Resolution rules pointer |
| `RULES_HASH` | Content hash when frozen (empty ⇒ not frozen) |
| `RESOLUTION_SOURCE` | Official oracle / venue resolver |
| `RESOLUTION` | YES \| NO \| VOID \| (empty if unresolved) |
| `RESOLUTION_EVIDENCE` | Pointer + tag `[V]` / `[U]` |
| `OPEN_TIME` / `CLOSE_TIME` / `RESOLVE_TIME` | UTC |
| `CHECKPOINT_MT_OK` | `Y` / `N` / `PARTIAL` — historical \(m_t\) present at pre-declared checkpoints |
| `CHECKPOINT_SPEC_REF` | Named checkpoint set (see below) |
| `DATA_L1` / `DATA_L2` | PM prints DATA-* / oracle DATA-* |
| `BODY_PATH` | Path to filled `BINARY_CONTRACT` card |
| `FIRST_MILESTONE_COMPLETE` | `Y` only if rules + settlement source + checkpoint \(m_t\) + final resolution all present and Clock-gradable |
| `NOTES` | Quarantine / mapping / slice notes |

### Row table (copy into active ledger)

```
| CONTRACT_ID | VENUE_ADAPTER | VENUE_NATIVE_ID | UNDERLYING | TENOR | TITLE | STATUS | RULES_URI | RULES_HASH | RESOLUTION_SOURCE | RESOLUTION | RESOLUTION_EVIDENCE | OPEN_TIME | CLOSE_TIME | RESOLVE_TIME | CHECKPOINT_MT_OK | CHECKPOINT_SPEC_REF | DATA_L1 | DATA_L2 | BODY_PATH | FIRST_MILESTONE_COMPLETE | NOTES |
|-------------|----------------|-----------------|------------|-------|-------|--------|-----------|------------|-------------------|------------|---------------------|-----------|------------|--------------|------------------|---------------------|---------|---------|-----------|--------------------------|-------|
```

---

## First-milestone completeness (per row)

A row may be marked `FIRST_MILESTONE_COMPLETE=Y` only if **all** are true:

1. **Rules** — `RULES_URI` set; `RULES_HASH` frozen (or explicit `[U]` why hash pending, not “complete”)  
2. **Settlement source** — `RESOLUTION_SOURCE` official; not LLM  
3. **Market prices at checkpoints** — `CHECKPOINT_MT_OK=Y` under a named spec  
4. **Final resolution** — `STATUS=RESOLVED` (or VOID with evidence) and `RESOLUTION` + `RESOLUTION_EVIDENCE` tagged  

`PARTIAL` checkpoint coverage ⇒ not complete. Disputed rules ⇒ `QUARANTINED`, not complete.

---

## Checkpoint spec (declare; do not invent prints)

Named sets are registered by Archivist/Clock **before** Examiner peek. Example skeleton (times relative to `CLOSE_TIME` trade cutoff unless stated):

| Checkpoint id | Meaning | Knowability |
|---------------|---------|-------------|
| `T_OPEN` | At or after `OPEN_TIME` when first usable \(m_t\) exists | print time ≤ t |
| `T_MINUS_15M` | 15 minutes before cutoff | print time ≤ t |
| `T_MINUS_5M` | 5 minutes before cutoff | print time ≤ t |
| `T_CLOSE` | Trade cutoff | print time ≤ t; no post-close leak |

Construction of \(m_t\) (mid / microprice / last) is **per BINARY_CONTRACT `BENCHMARK_PRICE_RULE`**. Missing checkpoint → mark missing, do not forward-fill from after \(t\).

This template does **not** populate prices.

---

## Hard rules

- IDs assigned only by Archivist.  
- One native venue market ↦ one `CONTRACT_ID` (binary slice explicit if the venue is multi-outcome).  
- Co-primary venues are **not** merged into a single row.  
- Join to L3 predictors (incl. Binance/Vision) only with decision-time timestamps — L3 is not L1.  
- Cemetery Edges reused as forecast inputs require a **Feature Card** citing CEM ids — registry rows do not revive Edges.  
- No validation laundering: checkpoint files used for tuning cannot later be labeled sealed holdout (`DATASET_USE_LEDGER`).

---

## Pointers

| Doc | Role |
|-----|------|
| `archive/templates/BINARY_CONTRACT.md` | Per-contract ground-truth card (canonical; skip extra `CONTRACT.md`) |
| `governance/TRACK_B_ORDERS_2026-09-11.md` | Sequence; first milestone |
| `governance/BINARY_EXAMINER_SPEC.md` | Metrics on this sample |
| `governance/PREDICTION_MARKET_MISSION_2026-09-11.md` | Schema summary §3 |
| `governance/AMD-20260911-PM-002.md` | Co-primary venues |

---

*End CONTRACT_REGISTRY template. Not a fetch. Not a cockpit. BINARY_CONTRACT.md remains the card.*
