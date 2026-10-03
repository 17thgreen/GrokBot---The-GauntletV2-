# CLOCK AUDIT REPORT — DATA-PROV-PM-001

- Audited UTC: `2026-09-11T20:52:32.978683+00:00`
- Recommended verdict: **CONDITIONAL**
- Overall hard-tests pass: **True**
- JSON: `/workspace/lab/data/DATA-PROV-PM-001/provenance/CLOCK_AUDIT_REPORT.json`
- Script: `/workspace/lab/data/DATA-PROV-PM-001/provenance/clock_audit_DATA-PROV-PM-001.py`
- Card: `/workspace/lab/archive/datasets/DATA-PROV-PM-001.md`
- Plan: `/workspace/lab/governance/TRACK_B_DATA_PLAN_2026-09-11.md`

## Executive verdict

**CONDITIONAL** — Venue-published RESOLUTION labels are internally consistent (YES/NO, temporal order OK, adapters tagged, no illegal pool). Independent oracle recompute UNTESTED and books absent → CONDITIONAL for label-only Examiner use; mid/path and oracle-verified settlement remain blocked.

### Why not APPROVED
- CONDITIONAL: Independent CF BRTI / Chainlink TWAP raw oracle replay UNTESTED [U] — settlement source VENUE_DECLARED [V]
- CONDITIONAL: Historical order books / decision-time mid paths ABSENT — do not APPROVE books
- CONDITIONAL: CONTRACT_IDs are provisional PROV-* pending Archivist
- CONDITIONAL: Polymarket coverage shorter than Kalshi (~3d vs ~7d) due to intentional row cap
- CONDITIONAL: Some contracts show long settlement publish lags (label knowable only at RESOLVE_TIME; see lag buckets)
- CONDITIONAL: Fee schedule PDF (Kalshi) UNTESTED [U]
- CONDITIONAL: Not a sealed holdout — provisional sample only
- Never APPROVE books that do not exist (this sample has none).

## Knowability (resolution labels vs decision timestamps)

- **Rule:** RESOLUTION label becomes knowable only after venue settlement publish, proxied here by RESOLVE_TIME (Kalshi settlement_ts / Polymarket closedTime). Any feature that uses RESOLUTION at decision time t where t < RESOLVE_TIME is LOOKAHEAD. CLOSE_TIME is trade cutoff — oracle inputs for the window may exist at CLOSE, but the *label* is not guaranteed published until RESOLVE_TIME. Conservative Examiner rule: label-only evaluation may use RESOLUTION only for decisions with t >= RESOLVE_TIME.
- **Settlement source:** VENUE_DECLARED [V]
- **Independent oracle recompute:** UNTESTED [U]
- **LOOKAHEAD:** feature_uses_RESOLUTION_at_t_before_RESOLVE_TIME => LOOKAHEAD; also LOOKAHEAD if using RESOLUTION before CLOSE when resolution not yet knowable
- **Safe:** post-RESOLVE_TIME label-only evaluation / grading
- **Unsafe:** any intra-window or pre-RESOLVE decision that consumes RESOLUTION / OUTCOME_PRICES winner / terminal LAST_PRICE as if known at t

## Venue semantics (NOT equivalent)

- Equivalent mechanisms: **False**
- Kalshi ≠ Polymarket. Never pool rows for joint stats / training without VENUE_ADAPTER tags and separate evaluation strata. YES on Kalshi is CF BRTI end>=start; YES on Polymarket Global is Chainlink TWAP Up (end>=start, flat→Up). Oracles, fee schedules, tick sizes, dispute paths, and settlement clocks differ.
- Pooling: `FORBIDDEN_WITHOUT_ADAPTER_STRATA`

## Hard tests A–I

| Test | Pass | Notes |
|------|------|-------|
| A HASH_VERIFY | True | checksums=79 all_match=True; rows kalshi=1328 poly=2496 combined=3824 |
| B SCHEMA | True | adapters={'KALSHI': 1328, 'POLYMARKET_GLOBAL': 2496}; CONTRACT_ID unique=True |
| C RESOLUTION | True | counts={'YES': 1889, 'NO': 1935}; Poly Up/Down map ok=2496 bad=0 |
| D TEMPORAL | True | open<close=3824; resolve>=close=3824; window_ok=3824 |
| E DUPLICATES | True | dup_native=0; dup_cid=0 |
| F CROSS-VENUE | True | separate coverage; pooling forbidden without adapter strata |
| G BOOKS/PRICES | True | books=ABSENT_OR_INCOMPLETE_BY_DESIGN; approve_books=False |
| H ORACLE | True | raw_series_attached=False; sources=3 distinct |
| I COVERAGE | True | strata=6 |

### A — Hash / row counts

- `normalized/kalshi_15m_btc_eth_resolved.ndjson`: rows=1328 expected=1328 match=True
- `normalized/polymarket_global_5m_15m_btc_eth_resolved.ndjson`: rows=2496 expected=2496 match=True
- `normalized/binary_contracts_provisional.ndjson`: rows=3824 expected=3824 match=True
- card hash `normalized/kalshi_15m_btc_eth_resolved.ndjson`: match=True sha256=`c1a09fd7eb4e97ef4672f2d9d281299695125185bc6be0743ca6bb26c8e8186d`
- card hash `normalized/polymarket_global_5m_15m_btc_eth_resolved.ndjson`: match=True sha256=`e199d2478b015a4210fa153883a020856f17c81169ca50558dbbf020601b8867`
- card hash `normalized/binary_contracts_provisional.ndjson`: match=True sha256=`431f7bd1f3d5d7b96b1419c2cdd3f200c05a91086f0983a738897c7243e1f027`
- CHECKSUMS.sha256 entries verified: True (79 files)
- Combined composition: {'combined_len': 3824, 'parts_sum': 3824, 'prefix_is_kalshi': True, 'suffix_is_poly': True, 'id_set_equal': True, 'pass': True}

### C — Resolution by venue×asset×horizon

| Stratum | n | YES | NO |
|---------|--:|----:|---:|
| KALSHI|BTC|15m | 664 | 321 | 343 |
| KALSHI|ETH|15m | 664 | 339 | 325 |
| POLYMARKET_GLOBAL|BTC|15m | 312 | 151 | 161 |
| POLYMARKET_GLOBAL|BTC|5m | 938 | 461 | 477 |
| POLYMARKET_GLOBAL|ETH|15m | 311 | 159 | 152 |
| POLYMARKET_GLOBAL|ETH|5m | 935 | 458 | 477 |

### D — Settlement lag (RESOLVE − CLOSE)

| Venue | n | min | median | p95 | max | >10m | >1h | buckets |
|-------|--:|----:|-------:|----:|----:|-----:|----:|---------|
| KALSHI | 1328 | 3.697 | 5.506 | 15.506 | 7203.868 | 4 | 2 | `{'<60s': 1322, '1h-1d': 2, '5m-1h': 2, '1-5m': 2}` |
| POLYMARKET_GLOBAL | 2496 | 51.000 | 55.000 | 450.000 | 22959.000 | 113 | 15 | `{'<60s': 1522, '1-5m': 801, '5m-1h': 158, '1h-1d': 15}` |

Long lags do **not** violate RESOLVE>=CLOSE; they reinforce that labels are knowable at RESOLVE_TIME, not at CLOSE_TIME.

### F — Separate coverage (do not pool)

- **KALSHI** n=1328 assets={'BTC': 664, 'ETH': 664} windows={'15m': 1328} oracle=['CF Benchmarks'] native=yes/no (Kalshi result)
- **POLYMARKET_GLOBAL** n=2496 assets={'BTC': 1250, 'ETH': 1246} windows={'5m': 1873, '15m': 623} oracle=['Chainlink'] native=Up/Down mapped to YES/NO

### G — Books / prices

- Historical books present: **False**
- Mid paths present: **False**
- Verdict: `ABSENT_OR_INCOMPLETE_BY_DESIGN`
- Do NOT APPROVE this dataset as if historical books / mid paths exist. Label-only evaluation may proceed under CONDITIONAL. Mid/path evaluation is UNTESTED/blocked until CLOB prices-history or trade tapes are attached as a separate DATA-* with its own Clock.
- Field `LAST_PRICE_DOLLARS` (KALSHI): Terminal last on settled market object — NOT a decision-time mid path. Must not be used as m_t at arbitrary t < CLOSE/RESOLVE. (usable_as_path=False)
- Field `OUTCOME_PRICES` (POLYMARKET_GLOBAL): Resolved outcomePrices (typically ['1','0'] or ['0','1']) — terminal settlement encoding, not an intra-window CLOB mid path. (usable_as_path=False)

### H — Oracle mapping

**KALSHI**
- provider: CF Benchmarks
- indices: BRTI (BTC) / ETHUSDRTI (ETH)
- method: simple average of 60×1s RTI prints in last minute before window start vs before window end; Yes if end >= start
- evidence_tag: [V] rules_primary / settlement_sources on settled markets
- independent_raw_replay: UNTESTED [U]

**POLYMARKET_GLOBAL**
- provider: Chainlink
- streams: btc-usd-twap-60s / eth-usd-twap-60s
- method: TWAP at end of titled range >= TWAP at beginning → Up (YES); flat → Up
- evidence_tag: [V] resolutionSource / rules description / docs
- independent_raw_replay: UNTESTED [U]

- RESOLUTION_SOURCE counts: `{'CF Benchmarks RTI 60s average (BRTI/ETHUSDRTI per series rules)': 1328, 'https://data.chain.link/streams/btc-usd-twap-60s-streams': 1250, 'https://data.chain.link/streams/eth-usd-twap-60s-streams': 1246}`
- Raw CF/Chainlink series attached: **False**

### I — Coverage windows + recommended freeze

| Stratum | n | OPEN min→max | CLOSE min→max | RESOLVE min→max | YES/NO |
|---------|--:|--------------|---------------|-----------------|--------|
| KALSHI|BTC|15m | 664 | 2026-09-04T20:45:00+00:00 → 2026-09-11T20:30:00+00:00 | 2026-09-04T21:00:00+00:00 → 2026-09-11T20:45:00+00:00 | 2026-09-04T21:00:05.506188+00:00 → 2026-09-11T20:45:08.528178+00:00 | 321/343 |
| KALSHI|ETH|15m | 664 | 2026-09-04T20:45:00+00:00 → 2026-09-11T20:30:00+00:00 | 2026-09-04T21:00:00+00:00 → 2026-09-11T20:45:00+00:00 | 2026-09-04T21:00:05.507885+00:00 → 2026-09-11T20:45:08.500660+00:00 | 339/325 |
| POLYMARKET_GLOBAL|BTC|15m | 312 | 2026-09-08T14:30:00+00:00 → 2026-09-11T20:15:00+00:00 | 2026-09-08T14:45:00+00:00 → 2026-09-11T20:30:00+00:00 | 2026-09-08T14:46:25+00:00 → 2026-09-11T20:30:54+00:00 | 151/161 |
| POLYMARKET_GLOBAL|BTC|5m | 938 | 2026-09-08T14:30:00+00:00 → 2026-09-11T20:35:00+00:00 | 2026-09-08T14:35:00+00:00 → 2026-09-11T20:40:00+00:00 | 2026-09-08T14:36:25+00:00 → 2026-09-11T20:40:52+00:00 | 461/477 |
| POLYMARKET_GLOBAL|ETH|15m | 311 | 2026-09-08T14:30:00+00:00 → 2026-09-11T20:15:00+00:00 | 2026-09-08T14:45:00+00:00 → 2026-09-11T20:30:00+00:00 | 2026-09-08T14:46:25+00:00 → 2026-09-11T20:30:52+00:00 | 159/152 |
| POLYMARKET_GLOBAL|ETH|5m | 935 | 2026-09-08T14:40:00+00:00 → 2026-09-11T20:35:00+00:00 | 2026-09-08T14:45:00+00:00 → 2026-09-11T20:40:00+00:00 | 2026-09-08T14:46:25+00:00 → 2026-09-11T20:40:54+00:00 | 458/477 |

#### Usable coverage for Examiner (label-only)

- Status: **USABLE_UNDER_CONDITIONAL**
- Knowability: use RESOLUTION only at/after RESOLVE_TIME
- Strata rule: Evaluate Kalshi and Polymarket Global separately; never pool YES rates

- `KALSHI|BTC|15m` n=664: OPEN≥`2026-09-04T20:45:00+00:00` … CLOSE≤`2026-09-11T20:45:00+00:00` (RESOLVE max `2026-09-11T20:45:08.528178+00:00`) — ~7d settled sample 2026-09-04 → 2026-09-11 UTC
- `KALSHI|ETH|15m` n=664: OPEN≥`2026-09-04T20:45:00+00:00` … CLOSE≤`2026-09-11T20:45:00+00:00` (RESOLVE max `2026-09-11T20:45:08.500660+00:00`) — ~7d settled sample 2026-09-04 → 2026-09-11 UTC
- `POLYMARKET_GLOBAL|BTC|5m` n=938: OPEN≥`2026-09-08T14:30:00+00:00` … CLOSE≤`2026-09-11T20:40:00+00:00` (RESOLVE max `2026-09-11T20:40:52+00:00`) — Bounded cap; ~3d dense 5m-heavy from 2026-09-08 UTC
- `POLYMARKET_GLOBAL|ETH|5m` n=935: OPEN≥`2026-09-08T14:40:00+00:00` … CLOSE≤`2026-09-11T20:40:00+00:00` (RESOLVE max `2026-09-11T20:40:54+00:00`) — Bounded cap; ~3d dense 5m-heavy from 2026-09-08 UTC
- `POLYMARKET_GLOBAL|BTC|15m` n=312: OPEN≥`2026-09-08T14:30:00+00:00` … CLOSE≤`2026-09-11T20:30:00+00:00` (RESOLVE max `2026-09-11T20:30:54+00:00`) — Sparser than 5m within same Poly fetch window
- `POLYMARKET_GLOBAL|ETH|15m` n=311: OPEN≥`2026-09-08T14:30:00+00:00` … CLOSE≤`2026-09-11T20:30:00+00:00` (RESOLVE max `2026-09-11T20:30:52+00:00`) — Sparser than 5m within same Poly fetch window

#### Mid/path evaluation

- Status: **UNTESTED_BLOCKED** — No historical order books or decision-time mid paths in this sample. Kalshi LAST_PRICE_DOLLARS and Poly OUTCOME_PRICES are terminal only.

#### Independent oracle evaluation

- Status: **UNTESTED_BLOCKED** — CF BRTI / Chainlink TWAP raw series not attached; settlement is VENUE_DECLARED [V] only.

## Safe vs unsafe features

### Safe (under CONDITIONAL)
- Venue-declared RESOLUTION (YES/NO) consumed only at/after RESOLVE_TIME
- Per-venue strata counts / calibration with VENUE_ADAPTER held fixed
- Window metadata OPEN/CLOSE/WINDOW/ASSET as schedule features (no label leak)

### Unsafe / blocked
- Any use of RESOLUTION / OUTCOME_PRICES winner before RESOLVE_TIME (LOOKAHEAD)
- Treating LAST_PRICE_DOLLARS or OUTCOME_PRICES as decision-time mid path
- Pooling Kalshi + Polymarket into one unlabeled YES rate or model
- Claiming independent CF/Chainlink oracle verification from this sample
- Claiming historical book / microstructure backtests from this sample
- Trading / execution (mission forbidden)

## Required remediation (to move beyond CONDITIONAL)

1. Attach independently replayable CF BRTI / ETHUSDRTI and Chainlink TWAP history → re-Clock as L2
2. Optional: attach CLOB `prices-history` / public trades as separate DATA-* for m_t paths
3. Archivist assign non-provisional CONTRACT_IDs for any pilot basket freeze
4. Optional: extend Polymarket slug enumeration to match Kalshi ~7d+ span
5. Do not treat this provisional sample as sealed holdout

## Policy notes

- No trading. No alpha. No invented oracle values.
- Auth: none (public APIs only) per FETCH_LOG / MANIFEST.
- Examiner / League: label-only route may proceed under CONDITIONAL; mid/path blocked.

*End CLOCK AUDIT — DATA-PROV-PM-001.*
