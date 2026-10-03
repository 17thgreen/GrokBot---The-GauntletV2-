# Examiner (Kalshi) scorecard TEMPLATE — v1

**Seat:** Examiner (Kalshi) · Astra desk  
**Revision date:** 2026-09-24 (ET) · commissioned by Conductor 2026-09-24 7:30 PM ET (routing step 0)  
**Machine-readable:** `lab/governance/astra/templates/EXAMINER_KALSHI_SCORECARD_TEMPLATE_v1.json`  
**Supersedes:** implicit v0 (there was no explicit template file). v0 was derived from these stamps: `EXAMINER_SCORECARD_STUB_C1_KXUFCFIGHT_SETTLED_JOIN_HARNESS_2026-09-24.md`, `EXAMINER_ACK_C1_RJ_PR49_STUB_READY_NOT_SCORED_2026-09-24.json`, `EXAMINER_SCORECARD_Q7_B_REHAB_P1_TAPE_WALK_KILL_2026-09-23.md` (+ its ACK), `EXAMINER_SCORECARD_STUBS_S1_S4_S5_R2P3_2026-09-22.json`  
**Research source:** `lab/governance/astra/research/KALSHI_EDGE_RESEARCH_2026-09-24.pdf` pp. 15–16 (the PDF footer reads "research, not a profit claim")  
**Scope:** This is a template revision only. It applies to new scorecards stamped after this revision. **No existing stamp was edited, re-scored, or re-opened.**

## Changelog
- **v0 (implicit):** the shape used by the EXAMINER_SCORECARD_STUB_* / EXAMINER_ACK_* / EXAMINER_SCORECARD_* stamps from 2026-09-22 to 09-24.
- **v1 (2026-09-24):** keeps the v0 shape unchanged and adds these blocks:
  - `common_scorecard`: 11 metrics, all null
  - `controls`: per-packet controls, all null
  - `fee_regime`: the standing feebook pin plus a placeholder for the Archivist manifest (status: pending)
  - `proposed_optional`: listed only, not adopted
  - `common_scorecard_rules`

---

## Section A — v0 shape (unchanged; codified)

Header: `id`, `seat`, `desk`, `packet`, `feature_family`, `lab`, `main_pin`, PR block (`number`, `merged`, `main`, `head_sha_pre_merge`, `base_pre_merge`, `merge_method`, `merged_at_et`, `units_ok`, `arms`, `arm_values`, `url`).

| Field | Allowed values / rule |
|---|---|
| `status` | NOT_SCORED · SCORED · HOLD_PRE_PR · SUPERSEDED |
| `verdict` | KEEP · ITERATE · KILL · READY_NOT_SCORED · HOLD · NOT_SCORED |
| `stub_ready` / `scored` / `promote` / `live_promotion` / `counted_as_experiment_pnl` | booleans; `promote=false` and `live_promotion=false` unless Conductor/Logan gates are cleared |
| `admit_alone_neq_score` / `units_neq_score` | always true |
| `selection_status` / `selection_reason` / `fallback_shadow_candidate` | when a frozen selection bar exists |
| `supersedes_hold*` / `supersedes_stub` | pointer + sha256 |
| `pins{name:{path,sha256}}` / `digest_verify` / `source_pins_copies` / `parent_source_pins` / `positive_control` | sha256 on box, head and main |
| `metrics` (packet-specific) / `metrics_null` / `metrics_fill_policy` | null until measured |
| `bar_table` / `pnl_by_scenario` | only for scored packets |
| `score_gate` / `refuse` / `refuse_binds` / `does_not_ungate` / `orthogonal_to` | lists |
| `evidence_tags` / `corpse_route` / `doc_nits_non_blocking` / `cite` | — |
| `stub_path` / `ready_packet_path` / `merge_stamp` / `canonical_ready_*` / `conductor_route` / `stamped_at_et` | — |

MD stamp sections, in this order:
1. Header
2. Pins table
3. Gates
4. Verdict table + desk headline
5. Arms
6. Metrics
7. Frozen bar / fee-honest P&L (only when scored)
8. **Common scorecard (v1)**
9. **Controls (v1)**
10. ScorecardPromotionRefused-if list
11. Score gate
12. ACK/READY/merge pointers + Stamped time

---

## Section B — Fee regime (v1)

| Field | Value |
|---|---|
| `feebook_formula_id` | `astra.r1p1.feebook.claude_order_level_ceil.v1`: the standing R1-P1 pin, required for any fee-honest claim |
| `fee_account_version_manifest.path` / `sha256` / `manifest_id` | **null** |
| `fee_account_version_manifest.status` | **pending**. The Archivist is drafting it. Its contents and formula ids are **not** assumed here. |

Relevant PDF text, p15: "The repo's older cent-ceiling convention requires a version-and-account reconciliation, not an assumption that one formula covers every historical and current trade. Prefer actual recorded fee components."

---

## Section C — Common scorecard (v1; all `value=null`, `measured=false`)

`source_ref` for every row: KALSHI_EDGE_RESEARCH_2026-09-24.pdf p15-16. The list of metrics comes from p16: "Track net P&L with and without rewards; calibration; fill rate; adverse selection after fills; feasible versus requested size; unresolved inventory; capital-hours; drawdown; and event concentration."

| Field | Unit | Definition (quoted from p15–16) | Formula |
|---|---|---|---|
| `net_pnl_without_rewards` | USD ("net dollars", p15) | "Report trading P&L excluding rewards, exchange rewards actually earned, fees, inventory liquidation or settlement, and capital cost." EV: "q - p - net fees - other costs", where q is conditional on our order filling. | pending_definition. Requires the feebook formula_id and the pending Archivist manifest. |
| `net_pnl_with_rewards` | USD | "net P&L with and without rewards"; rewards = "exchange rewards actually earned" | pending_definition. Same fee requirements as above. |
| `rewards_actually_earned` | USD (implied by "cash received") | "do not count an ideal reward estimate as cash received" | pending_definition |
| `calibration` | pending_definition | named only on p15–16 (p5 and p9 give context, but no definition) | pending_definition |
| `fill_rate` | pending_definition | named only | pending_definition |
| `adverse_selection_after_fills` | pending_definition | "A maker's unconditional forecast can be right while its filled orders are systematically bad." | pending_definition (horizon and method) |
| `feasible_vs_requested_size` | pending_definition | "A 20% return on $5 of available depth is a curiosity … A quote can disappear, and consuming it changes the opportunity." | pending_definition |
| `unresolved_inventory` | pending_definition | "inventory liquidation or settlement" is reported as a separate profit source | pending_definition |
| `capital_hours` | capital-hour (name only) | "risk-adjusted net dollars per constrained capital-hour" | pending_definition |
| `drawdown` | pending_definition | "stress drawdown" | pending_definition |
| `event_concentration` | pending_definition | "Contracts on one election, game, weather system or crypto price path share risk. Event-cluster uncertainty matters more than the raw number of fills or timestamps." | pending_definition |

## Section D — Controls (v1; per packet)

From p16: "Compare with market-only, simple-model and no-trade controls where relevant." Pages 15–16 give no further definition of any control.

| Control | `applies` | `result` | Note |
|---|---|---|---|
| `market_only` | null | null | Stays null/not applicable until the packet freeze declares it. Context: p5 "market-only, model-only and hybrid baselines". |
| `simple_model` | null | null | Stays null until declared. The model must be frozen before the test, never chosen after seeing results. |
| `no_trade` | null | null | Stays null until declared. Context: p9 "abstention policies". |

## Section E — Rules
1. Every common_scorecard value stays null with `measured=false` until it is measured on a frozen packet with artifacts.
2. **Never back-fill** from scout N, unit counts, fixtures, admit flags, or estimates.
3. A field marked pending_definition gets no Examiner-invented formula. Either the packet freeze or a Conductor-ratified template revision must declare the formula before scoring.
4. P&L with rewards and P&L without rewards are **always reported side by side**.
5. P&L that includes rewards never substitutes for P&L without rewards in a KEEP decision, unless the packet freeze declares it. Basis, p15: "Do not hide a negative forecasting strategy inside a positive subsidy." Even when the freeze declares it, both figures are still reported.
6. `rewards_actually_earned` counts only rewards actually earned. Estimated rewards are not admissible.
7. Fee-honest P&L requires `astra.r1p1.feebook.claude_order_level_ceil.v1`. Once the Archivist files its fee/account-version manifest, that manifest must be pinned too. Until then the reference stays null/pending.
8. Controls apply per packet and stay null until that packet's freeze declares them.
9. This revision does not re-score, re-open, or alter any existing stamped verdict.

## Section F — Proposed optional (listed only, NOT adopted; Conductor to decide)
These appear on pp. 15–16 but are not in the commissioned list:
- uncertainty by event or day
- sensitivity to worse queues, latency and costs
- executable dollars per day
- independent opportunities
- correlation with existing positions
- fees reported separately
- capital cost
- inventory liquidation/settlement P&L
- risk-adjusted net dollars per constrained capital-hour (the headline objective)
- study label: unit-only / synthetic / historical replay / prospective shadow / live (Archivist task)
- log of attempted variants
- separation of discovery, tuning and evaluation periods
- preregistration checklist
- dependence on a single event
