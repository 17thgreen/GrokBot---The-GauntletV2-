# Forward to Archivist — Amendment B hash set + pin extension (2026-09-24 ~20:17 ET)

Deep Research asks the Archivist/Steward to:

1. **Externally anchor** (commit or equivalent) the hash set in `packets/card01_hybrid_forecast/LEDGER_2026-09-24.md` § "Hash register (Amendment B session)" **before 2026-11-02T22:00Z and before any race outcome**. Governance is not a git repo; Deep Research does not push.

2. **Pin extension for methodology hashing:** extend the ElectIndex capture pin beyond `races_summary.csv` to allow one GET/day, hash-only, of:
   - `https://electindex.com/wp-content/themes/electindex/assets/forecasts/eifc-info.js`
   - (optional) the repo README via raw.githubusercontent
   Same storage rules (raw → evidence_private only). Baseline regime R0 = `caaff53e739413a8340f0addbec7136ec1995195291cab61889a94c1286ea87f`.

3. **Fee/account manifest:** enter `fee_type` / `fee_multiplier` from Collector series GETs for `KXHOUSERACE` + the 35 Amendment A legacy tickers listed in Amendment B. Until then after-cost is **BLOCKED**.

4. **Source-probe relocation (your earlier recommendation):** move `packets/card01_hybrid_forecast/source_probe_electindex/` raw files to evidence_private; they remain PRE_FREEZE design input only.

## Key pins (verify against LEDGER)

| Item | sha256 |
|---|---|
| Amendment B | `ee6af37cef95f1e468d28e5b06750caaca8b1706ec11ed5cf5cdce460524c2c6` |
| Pinned national-miss script | `049368f942741ff4a63acad328a49ff256252587d6c65f1e7e6d65d6101781f2` |
| Decision packet (current) | `c0c1aa66f104e3f102228a7a8e16f205977afbee63928f30a6954ec46707a82c` |
| Decision packet reconstructed pre-v1.1 | `58c44c4fb144968ba57e4c8b4a2018026a123d17a02e2e6c09fdfd38f465a353` |
| Card 02 kernel (current) | `6b36dacb84f92524b18c3799c50c5818ee44fee89ac1743ceafb1092cd4c7e48` |
| Card 02 kernel at freeze (reconstructed) | `9624ab2498e88896c46e8fd984211b4b8839e613567209841358d7cf5059e5d6` |
| feffec51 (NOT pinned; `.pre-` kept) | `feffec5104882174031b43026e629e45771925c05272ee6e51b927dd5dafd144` |

## Lineage correction (Task 1)

Direction was reversed in an earlier Conductor note. Correct:
- Decision packet: `58c44c4f` (pre-v1.1) → `d59c2642` (v1.1 bump) → `c0c1aa66` (changelog + Amendment B pointer). Only charter/source-map/changelog/pointer lines changed; **no number/rule/threshold/universe/weight/knob changed**.
- Card 02 kernel: `9624ab24` (freeze) → `8412439f` (v1.1) → `6b36dacb` (changelog). Same constraint.
