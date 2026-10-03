# CLOCK AUDIT — W2C SIBLING MID JOIN

- **AUDIT_ID:** `CLOCK_AUDIT_W2C_SIBLING_JOIN`
- **FEATURE:** `DRAFT-FEAT-20260913-001` (sibling-asset mid blend)
- **GATE:** `DRAFT-ABST-20260913-001`
- **WAVE:** W2-C
- **AUDITED_AT_UTC:** 2026-09-13T19:11:39.112154+00:00
- **VERDICT (join only):** **CLEARED**
- **VERDICT_SCOPE:** join_only

## Scope (hard)

- No alpha / no Examiner Δ or scores
- No CF / no L3
- No EXPIRATION_VALUE as feature or join key
- No new fetch; sources listed below

## Sources

- **checkpoints:** `/workspace/lab/data/DATA-PROV-PM-003/derived/checkpoints.ndjson`
- **contract_coverage:** `/workspace/lab/data/DATA-PROV-PM-003/derived/contract_coverage.ndjson`
- **pm001_labels:** `/workspace/lab/data/DATA-PROV-PM-001/normalized/kalshi_15m_btc_eth_resolved.ndjson`
- **feature_card:** `/workspace/lab/archive/features/DRAFT-FEAT-20260913-001-W2C-sibling-mid.md`
- **gate_card:** `/workspace/lab/archive/features/DRAFT-ABST-20260913-001-W2C-bad-cal.md`
- **prior_clock:** `PM-003 mid CLEARED at rem 840/600/300 with excludes`
- **new_fetch:** `False`

## Join rule (fail-closed)

Pair KALSHI 15m BTC↔ETH by same `OPEN_TIME` + `CLOSE_TIME` (PM-001 / coverage) and same `time_remaining_sec` ∈ {840, 600}.

| Headline / cell | Scored | Sibling |
|-----------------|--------|---------|
| A `KALSHI\|15m\|ETH\|T-14m\|mid` | ETH rem=840 mid | BTC rem=840 mid |
| B `KALSHI\|15m\|BTC\|T-10m\|mid` | BTC rem=600 mid | ETH rem=600 mid |
| Annex `KALSHI\|15m\|BTC\|T-14m\|mid` (DARK) | BTC rem=840 mid | ETH rem=840 mid (coverage only) |

Sibling excludes (mirror TEST-007):

- `implied_p_method == mid` (no last-fallback)
- same `decision_time` as scored (same OPEN/CLOSE + rem)
- no future rem / no later window
- drop if sibling `implied_p` ≤ 0.02 or ≥ 0.98
- VOID/DISPUTED sibling → missing
- missing sibling → fail-closed `p_t := m_t`

## Universe OPEN/CLOSE twinning

- Unique BTC OPEN/CLOSE keys: **604**
- Unique ETH OPEN/CLOSE keys: **604**
- Shared windows: **604**
- BTC without ETH twin: **0**
- ETH without BTC twin: **0**

## Exact counts per cell

### headline_A — `KALSHI|15m|ETH|T-14m|mid` (headline)

- **N scored** after TEST-007-style excludes (mid, rem=840, not near-deg): **604**
- **N with pairable sibling** (opposite=BTC, same OPEN/CLOSE, same rem, mid, not near-deg): **604**
- **N missing sibling** (fail-closed → own mid): **0**
- **N sibling present but excluded** (method/near-deg; count as missing for feature speak): **0**
- Decision_time equality when paired: 604 equal / 0 unequal (all_equal=True)
- No look-ahead: rem_eq=604, rem_ne=0, future_window=0, violations=0 (pass=True)
- Scored exclude breakdown: `{'non_mid_at_rem_dropped': 0, 'near_deg_scored_dropped': 0, 'void_disputed_scored_dropped': 0}`
- Missing reasons: `{}`

### headline_B — `KALSHI|15m|BTC|T-10m|mid` (headline)

- **N scored** after TEST-007-style excludes (mid, rem=600, not near-deg): **604**
- **N with pairable sibling** (opposite=ETH, same OPEN/CLOSE, same rem, mid, not near-deg): **604**
- **N missing sibling** (fail-closed → own mid): **0**
- **N sibling present but excluded** (method/near-deg; count as missing for feature speak): **0**
- Decision_time equality when paired: 604 equal / 0 unequal (all_equal=True)
- No look-ahead: rem_eq=604, rem_ne=0, future_window=0, violations=0 (pass=True)
- Scored exclude breakdown: `{'non_mid_at_rem_dropped': 0, 'near_deg_scored_dropped': 0, 'void_disputed_scored_dropped': 0}`
- Missing reasons: `{}`

### annex_BTC_T14m — `KALSHI|15m|BTC|T-14m|mid` (annex_coverage_only)

- Card DARK on annex: Feature card DARK on annex; coverage measured only
- **N scored** after TEST-007-style excludes (mid, rem=840, not near-deg): **604**
- **N with pairable sibling** (opposite=ETH, same OPEN/CLOSE, same rem, mid, not near-deg): **604**
- **N missing sibling** (fail-closed → own mid): **0**
- **N sibling present but excluded** (method/near-deg; count as missing for feature speak): **0**
- Decision_time equality when paired: 604 equal / 0 unequal (all_equal=True)
- No look-ahead: rem_eq=604, rem_ne=0, future_window=0, violations=0 (pass=True)
- Scored exclude breakdown: `{'non_mid_at_rem_dropped': 0, 'near_deg_scored_dropped': 0, 'void_disputed_scored_dropped': 0}`
- Missing reasons: `{}`

## Knowability answers

- **Knowable at t?** **Yes**
  - Rule: Sibling m*_t is the opposite-asset PM-003 checkpoint mid at the same OPEN_TIME/CLOSE_TIME window and same time_remaining_sec / decision_time as the scored row. Cell identity and mid are L1 observables at t; pairing key is contemporaneous (no future rem, no later window).
- **Look-ahead?** **No**
  - Rule: Look-ahead would require sibling rem < scored rem, sibling decision_time > scored decision_time, or sibling from a later OPEN/CLOSE window. Audit requires sibling rem == scored rem AND sibling decision_time == scored decision_time AND same OPEN/CLOSE.

## Integrity footnotes

- Enriched rows: 6040 (ckpt=6040, cov=1208, pm001=1328)
- Coverage vs PM-001 OPEN/CLOSE mismatches: **0**
- Elapsed check (`decision_time == open + (900-rem)`): ok=2416 bad=0

## Verdict recommendation (join only)

**CLEARED** — Join-only CLEARED: every scored headline/annex row after TEST-007-style excludes has a same-OPEN/CLOSE same-rem mid sibling with equal decision_time; no look-ahead; fail-closed rule defined but unused (0 missing). Shared BTC↔ETH windows = 604/604. No EXPIRATION_VALUE in join. Not an alpha verdict.

This is not an Examiner skill verdict and not permission to trade. Prior PM-003 mid CLEARED at rem 840/600/300 with excludes remains the incumbent m_t clearance.
