# R2-P5 — Schema stub landed

**Status:** SCHEMA_STUB · Archivist **SCHEMA_ACCEPTED** (`REG-R2-P5-SCHEMA-20260922`)  
**Stubbed_at:** `2026-09-22T23:01:07Z`  
**Owners:** Collector + Archivist (+ Clock provenance)  
**Cite:** `briefs/R2_DEEP_RESEARCH_2026-09-22.md` §R2-P5 · `packets/R2-P5_ADVERSE_FIELD_LIST_2026-09-22.md` · `packets/R2-P5_SCHEMA_ACCEPT_2026-09-22.md`

## Canonical path (ping this)
`lab/governance/astra/registry/schemas/r2_p5_admit_fields.schema.json`

## Companion artifacts
| Path | Role |
|---|---|
| `registry/schemas/r2_p5_admit_fields.schema.json` | **Canonical** JSON Schema |
| `packets/R2-P5_KICKOFF_ADVERSE_SCHEMA_STUB_2026-09-22.json` | Mirror copy |
| `packets/R2-P5_SEED_INSTANCE_ADMIT1_SOT_ONLY_2026-09-22.json` | SoT-only seed (16 ADMIT-1 events; adverse null) |
| `packets/R2-P5_SCHEMA_ACCEPT_2026-09-22.md` | Archivist acceptance |
| `packets/R2-P5_ADVERSE_FIELD_LIST_2026-09-22.md` | Deep Research field list |

## Field map
| Conductor | Archivist / schema |
|---|---|
| `holdout_kickoff_utc` | `holdout_kickoff_utc` |
| `kalshi_occurrence_datetime` | `kalshi_occurrence_datetime` + `sot_pin` |
| `delta_sec` | `delta_kickoff_sec` |
| which clock windows used | `window_clock_source` + `t_minus_7d_utc` |
| `edge_at_quote` / `edge_at_fill` | same (null until odds) |
| `hedge_complete_flag` | same; `fee_model_ref` = `astra.r1p1.feebook.claude_order_level_ceil.v1` when non-null |
| `odds_age_sec` | same |

## Guards
- GET-only provenance gate — **not** a strategy; no experiment id minted  
- ADMIT-1 recorder untouched (pid left running) · no poll-budget steal · no orders  
- Missing R1-P3 four-core → `measurement_gap`, not strategy failure  
- S1 KXMLBGAME panel stub remains separate
