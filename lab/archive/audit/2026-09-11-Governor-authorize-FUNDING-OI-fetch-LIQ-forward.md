# Audit — Human Governor DATA fetch authorization

- **UTC:** 2026-09-11
- **Actor:** Archivist (ledger from Conductor)
- **Event:** GOVERNOR_AUTHORIZE_FETCH
- **Authorized:**
  1. Free Binance Vision fetch → **DATA-PROV-FUNDING-001** + **DATA-PROV-OI-001**
  2. **DATA-PROV-LIQ-001** = **live forward capture only** (no paid historical backfill)
- **Not authorized:** paid LIQ history vendor
- **EDGE-20260911-003:** remains **historically blocked** (no free UM liq hist) until forward-only policy + Clock say otherwise
- **Archivist:** do **not** invent dataset files; **index DATA cards when registered** after fetch+provenance
- **Related:** `governance/DATA_PROV_CATALYST_SOURCES_2026-09-11.md`
