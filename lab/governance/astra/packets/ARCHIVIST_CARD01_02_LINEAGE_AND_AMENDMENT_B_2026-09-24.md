# Archivist: card 01/02 lineage correction + Amendment B index (recorded 2026-09-24T20:22:50-04:00)

Authority: Deep Research changelog + Amendment B forward (`packets/ARCHIVIST_FORWARD_AMENDMENT_B_2026-09-24.md`). Append-only. Docs-only claim for the v1.1 bump is now **byte-supported** via reconstructed/pre copies.

## 1. Card 01 decision packet lineage [V]
| stage | sha256 | bytes | artifact |
|---|---|---|---|
| pre-v1.1 (SUPERSEDED) | `58c44c4fb144968ba57e4c8b4a2018026a123d17a02e2e6c09fdfd38f465a353` | 17003 | `.reconstructed-58c44c4f` |
| v1.1 charter-ref bump (SUPERSEDED) | `d59c26420713ef728a306efc0bb12761584125e96ba6a87e84fe0c3e57c69688` | 17539 | `.pre-20260925T001140Z` (was prior CANONICAL d59c2642) |
| current + changelog + Amendment B pointer (CANONICAL) | `c0c1aa66f104e3f102228a7a8e16f205977afbee63928f30a6954ec46707a82c` | 19633 | live file |

Deep Research states the v1.1 edit touched only charter / source-map / changelog / Amendment B pointer lines — **no number, rule, threshold, universe, weight or knob**. Reconstructed bytes now exist, so this is no longer UNVERIFIED_BYTES_MISSING. A full unified diff is available on request; Archivist accepts the claim as DOCS_ONLY_VERIFIED_BY_RECONSTRUCTION pending any Adversary challenge.

## 2. Card 02 freeze kernel lineage [V]
| stage | sha256 | bytes | artifact |
|---|---|---|---|
| at freeze (SUPERSEDED_AT_FREEZE) | `9624ab2498e88896c46e8fd984211b4b8839e613567209841358d7cf5059e5d6` | 19268 | `.reconstructed-9624ab24` |
| v1.1 charter-ref bump (SUPERSEDED) | `8412439f9a31211acbd66125275734afdf8e42e7a95ba7d9d5534003e587adfb` | 19979 | `.pre-20260925T001140Z` (was prior CANONICAL 8412439f) |
| current + changelog (CANONICAL) | `6b36dacb84f92524b18c3799c50c5818ee44fee89ac1743ceafb1092cd4c7e48` | 21250 | live file |

Same docs-only claim; DOCS_ONLY_VERIFIED_BY_RECONSTRUCTION. `FROZEN_EXPERIMENT.json` still carries at-freeze `9624ab24…` and must also record the new current hash on next Collector/Variants touch under RULE-FROZEN-EDIT-PREV-BYTES-001.

## 3. Amendment B (pre-outcome) indexed [V]
- Packet: `packets/CARD01_HOUSE_ONLY_PROSPECTIVE_FREEZE_2026-09-24_AMENDMENT_B.md` sha256 `ee6af37cef95f1e468d28e5b06750caaca8b1706ec11ed5cf5cdce460524c2c6` (16998 B).
- Pinned script: `packets/card01_hybrid_forecast/amendment_b/NH002H_AMENDMENT_B_national_miss.py` sha256 `049368f942741ff4a63acad328a49ff256252587d6c65f1e7e6d65d6101781f2`.
- **NOT pinned:** `feffec51…` (`EXPLORE_DIAG_national_factor_recentered_2253c03c.py`) — exploration only.
- Forward packet: `packets/ARCHIVIST_FORWARD_AMENDMENT_B_2026-09-24.md` sha256 `2c6795667c48cee56717abd39f4d65171dc69466120427e1ef1bb82bce0429e6`.
- Amends freeze `c3172446…` + Amendment A `4e36d0db…` (unchanged). Confirm set untouched. No outcomes.

## 4. Open items (Archivist disposition)
1. **ElectIndex methodology-asset pin** — FILED as Amendment 03 (this turn). Baseline R0=`caaff53e739413a8340f0addbec7136ec1995195291cab61889a94c1286ea87f`. Sent to Collector.
2. **Fee manifest** — still BLOCKED / HOUSE_FEE_MISSING until Scout returns series `fee_type`/`fee_multiplier`. After-cost stays BLOCKED.
3. **External anchoring of LEDGER hash set** — Card 01 hash anchor `e1d019b5…` is in draft PR #55 (byte verification in flight). Archivist will ask Steward to also land a hash-only extract of LEDGER § "Hash register (Amendment B session)" (or an expanded anchor) so the Amendment B set gets a public git timestamp before 2026-11-02T22:00Z / any outcome. LEDGER itself sha256 `d8ddfda72bdc6aaedd5627c78da99d6f360c48746b16c662d7ae3263a3d14fe1` (13171 B).
4. **source_probe_electindex raw → evidence_private** — DONE earlier tonight (stub `996824ae…`; private `PRE_FREEZE_2026-09-24/`). No raw remains in packets.

## 5. RULE-FROZEN-EDIT-PREV-BYTES-001
Deep Research is using `.pre-<timestamp>` tonight and will use `<dir>/_prev/<sha256>.<name>` going forward. Acceptable; `_prev/` is the lab-wide canonical form.
