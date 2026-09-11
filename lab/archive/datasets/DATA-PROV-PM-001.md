# DATA-PROV-PM-001

- **DATA_ID:** DATA-PROV-PM-001
- **NAME:** Provisional short-window BTC/ETH binary PM contracts (Kalshi 15m + Polymarket Global 5m/15m)
- **STATUS:** **CONDITIONAL**
- **Registered:** 2026-09-11 UTC (Track B provisional fetch)
- **Plan:** `/workspace/lab/governance/TRACK_B_DATA_PLAN_2026-09-11.md`
- **Manifest:** `/workspace/lab/data/DATA-PROV-PM-001/MANIFEST.json`
- **Checksums:** `/workspace/lab/data/DATA-PROV-PM-001/CHECKSUMS.sha256`
- **Path:** `/workspace/lab/data/DATA-PROV-PM-001/`
- **Role:** L1 prediction-market **resolved binary contract** sample for co-primary adapters `KALSHI` + `POLYMARKET_GLOBAL`. Not venue marriage. Not a trade feed. Not multi-GB archive.
- **Auth:** Public APIs only — **no API keys / secrets used** `[V]`
- **Schema:** Aligned to `archive/templates/BINARY_CONTRACT.md` (provisional `PROV-*` CONTRACT_IDs)

## Inventory `[V]`

| Slice | Rows | Window (approx UTC) | Resolution |
|-------|------|---------------------|------------|
| Kalshi `KXBTC15M` + `KXETH15M` settled | 1328 (664+664) | 2026-09-04 → 2026-09-11 (~7d) | YES/NO from `result` |
| Polymarket Global 5m/15m BTC+ETH | 2496 | 2026-09-08 → 2026-09-11 (bounded cap; 5m-heavy) | YES/NO ← Up/Down via `outcomePrices` |
| Combined NDJSON | 3824 | — | all labeled YES/NO in sample |
| Total bytes | ~38 MB | raw+normalized+manifest | NOT multi-GB |

### Key hashes (normalized)
| File | SHA256 |
|------|--------|
| `normalized/kalshi_15m_btc_eth_resolved.ndjson` | `c1a09fd7eb4e97ef4672f2d9d281299695125185bc6be0743ca6bb26c8e8186d` |
| `normalized/polymarket_global_5m_15m_btc_eth_resolved.ndjson` | `e199d2478b015a4210fa153883a020856f17c81169ca50558dbbf020601b8867` |
| `normalized/binary_contracts_provisional.ndjson` | `431f7bd1f3d5d7b96b1419c2cdd3f200c05a91086f0983a738897c7243e1f027` |

### Layout
- `raw/` — Gamma/Kalshi JSON pages + cutoff + historical smoke
- `normalized/` — BINARY_CONTRACT-aligned NDJSON
- `provenance/fetch_pm001.py` · `provenance/FETCH_LOG.json`
- `MANIFEST.json` · `CHECKSUMS.sha256`

## Oracle / L2 notes
- **Kalshi:** CF Benchmarks BRTI / ETHUSDRTI 60s average at window boundaries `[V]` rules_primary
- **Polymarket Global:** Chainlink BTC/ETH USD TWAP 60s `[V]` resolutionSource / docs
- Independent raw oracle replay: **UNTESTED** `[U]` — venue resolution labels used for this sample

## Access gates
| Path | Access |
|------|--------|
| raw/ | immutable provisional snapshot; Clock pending |
| normalized/ | provisional; do not treat as sealed holdout |
| Examiner / League | **Label-only CLEARED** under CONDITIONAL; mid/path blocked |
| Trading | **Forbidden** (mission + Track B) |
| Secrets | None present; none required for refresh of this path |

## Known limitations (for Clock)
- Polymarket span shorter than 7d due to intentional row cap (5m density) `[V]`
- Kalshi pre-2026-07-13 requires `/historical/*` dual-route (smoke only in raw/) `[V]`
- No historical order books; CLOB prices-history retention UNTESTED `[U]`
- Fee cents table (Kalshi PDF) UNTESTED `[U]`
- `CONTRACT_ID`s are provisional `PROV-*` pending Archivist
- US Global trading eligibility remains `[U]` counsel — capture allowed under Governor co-primary planning assumption

## Status history
1. **PENDING_CLOCK** ← current (2026-09-11) — provisional sample on disk; awaiting Clock DATA VERDICT

## Clock DATA VERDICT
- **Verdict:** CONDITIONAL (APPROVED_WITH_LIMITATIONS) — issued 2026-09-11T20:53:10Z
- **Failures:** none hard on venue labels
- **Safe features:** RESOLUTION YES/NO at/after RESOLVE_TIME; per-adapter strata
- **Unsafe features:** pre-RESOLVE labels; terminal prices as m_t; books; unlabeled venue pooling; independent-oracle claims
- **Required remediation:** L2 oracle replay DATA-*; optional mid/path DATA-*; Archivist IDs; not sealed holdout
- **Full:** `/workspace/lab/data/DATA-PROV-PM-001/provenance/DATA_VERDICT_DATA-PROV-PM-001.md`
- **Coverage:** `/workspace/lab/data/DATA-PROV-PM-001/provenance/USABLE_COVERAGE_DATA-PROV-PM-001.md`
