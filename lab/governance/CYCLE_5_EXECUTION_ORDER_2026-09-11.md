# CYCLE 5 — Immediate execution order (Logan)
**Document:** `CYCLE_5_EXECUTION_ORDER_2026-09-11.md`  
**Authority:** Logan M (Human Governor)  
**Date (UTC):** 2026-09-11  
**RETROACTIVE:** **NO**  
**Does not:** modify Edge Cards · start Examiner · download data (this note only)

---

## Immediate sequence

1. **Fetch funding / OI** — provisional Vision pull for `DATA-PROV-FUNDING-001` + `DATA-PROV-OI-001` (authorized; no paid LIQ hist).
2. **Register** — Archivist dataset cards + provenance; ledger opens via `archive/datasets/DATASET_USE_LEDGER.md`.
3. **Live LIQ** — `DATA-PROV-LIQ-001` forward capture only (no paid backfill).
4. **Clock** — DATA VERDICT on Catalyst DATA-* (knowability, settlement, gaps, ETH OI asymmetry).
5. **Freeze splits** — research / validation / holdout / forward seals locked before peek; record in use ledger.
6. **Examiner after clear** — Conductor routes RESEARCH TEST only after Archivist CLEAR/WARN-ack + Clock VERDICT. **Do not start Examiner in this commission.**
7. **Vendor recon quiet** — no paid LIQ / Tardis (or kin) purchase; recon stays idle unless Logan re-opens.
8. **Index updates** — Archivist indexes new DATA-* / audit / this order; Edge Card bodies untouched.

---

## Pointers (binding context)

| Doc | Role |
|-----|------|
| `governance/CYCLE_5_RESEARCH_ORDERS.md` | Cycle 5 research priorities, hard locks, routing gate |
| `governance/DATA_PROV_CATALYST_001_SPEC.md` | Provisional Catalyst registration checklist |
| `governance/DATA_PROV_CATALYST_SOURCES_2026-09-11.md` | Source map (FUNDING / OI / LIQ) |
| `governance/US_LAWFUL_VENUE_CONSTRAINT_2026-09-11.md` | US-lawful execution / cockpit / capital constraint (`RETROACTIVE: NO`) |
| `archive/templates/DATASET_USE_LEDGER.md` | Use-ledger schema + no validation-laundering rule |
| `archive/datasets/DATASET_USE_LEDGER.md` | Active use ledger (initially empty) |

Binance / fapi / Vision remain **Layer-3 predictor data only** under the US lawful venue constraint — not PM execution venues.

*End Cycle 5 execution-order note.*
