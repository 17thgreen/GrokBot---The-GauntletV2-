# CLOCK_PROVENANCE_BECKER_ARCHIVE_2026-10-03

**Seat:** The Clock (Data Integrity Sentinel), provenance and temporal validity only. No alpha, no scoring, no orders, no edits to other seats' data.
**Issued:** 2026-10-03T16:35:27-04:00 (ET). **Authority:** `/workspace/lab/governance/astra/packets/CONDUCTOR_RULING_SCOUT_EXTERNAL_HUNT_2026-10-03.json` sha256 `870895a58e80fd1442d0ce97e42df02426bf7e38f64dcd091efc6fbf26b74ebf` [V] ("Clock provenance audit required before any Examiner use").
**Target:** Collector extract of Jon Becker's public prediction-market dataset, `/workspace/lab/astra-capture/external/becker_2026-10-03/` (third-party, **[A] external prior**).
**Tags:** [V] verified on box, [I] inference, [H] hypothesis, [A] external prior, [U] unknown.

## VERDICT: **CAVEAT**

The archive is usable **only as an [A] external prior**, with the limitations below. There is no holdout, dev-cohort or ADMIT-1 contamination. Timestamp semantics are established for every time column. There is no structural defect: no duplicate rows, no duplicate trade_ids, no nulls in key fields, and all counts match the ADMISSION json.
**Tags stay [A]. This archive can never replay, score, or promote strategy 000 (or any Astra strategy), and it is never holdout, OOS, or confirmatory evidence.**

Named limitations: (a) it cannot be cross-checked against our own tape, because there is zero time or ticker overlap [V]. (b) Markets still open at the 2025-11-25 hard end are truncated [V]. (c) Trades exist only for markets with snapshot volume ≥ 100 [V code / I data]. (d) Closed-market trade sums fall slightly short of `volume` on some tickers [V]. (e) On no-result/void markets, `close_time` does not mark the end of trading [V]. (f) The data licence is unknown [U]. (g) The commission's LICENSE pin prefix is mislabelled (see Pins).

## Pins (re-hashed on box)

| pin | claimed prefix | sha256 (box) | result |
|---|---|---|---|
| conductor_ruling | `870895a5` | `870895a58e80fd1442d0ce97e42df02426bf7e38f64dcd091efc6fbf26b74ebf` | **MATCH** |
| admission_note_md | `b0763e60` | `b0763e606d2b8eaf4514debcb0a2490e354c783ad6f182384614549ccf6e0427` | **MATCH** |
| admission_note_json | `6ec7dc54` | `6ec7dc54da0eab2a64babcbe8f23bf9fb631b7f3d9255f278fe6388cbc7d07d0` | **MATCH** |
| t0_kxnflgame_trades_parquet | `a1e1027e` | `a1e1027e8fd1e5bda30c3a4124e990048d5a7700cf2b08df24c1fbc5a0054e99` | **MATCH** |
| license_file_LICENSE | `5690e332` | `a69ab694cc5a08793bc36673976a4bd97ef37a26786cd94a14072268550338f5` | **MISMATCH** |
| dev_tape_events_jsonl_gz | `cd300e66` | `cd300e664c2c5f2ff344c4b1eb17dd3f8e5f3326168b9dd8e3ade94a3a7382b4` | **MATCH** |
| holdout_nfl_RESERVED_HOLDOUT | `74507e1a` | `74507e1a4371d69bc79ea2369f9bff030a74f51ee80c8072ba9c0f5345d377ca` | **MATCH** |
| holdout_q6s5_accept_json | `9a987a77` | `9a987a77e6cd6293ddaeb14fadbf33a25c1a6cc392af25f46eaaaaae33ebb273` | **MATCH** |
| holdout_q6s5_addendum_md | `370dc31d` | `370dc31df17191446013b6cebb52d44ee8346f47d2f5b543a1c73049ba52c063` | **MATCH** |
| admit1_ruling | `ac7cfe63` | `ac7cfe63623ca342ab5b4285ff58382a8138b58fb6cd8e95310a5d30d90304f2` | **MATCH** |

- The LICENSE pin `5690e332` is the **Becker repo commit** recorded in `license/main_commit.txt`, not the sha256 of the LICENSE file [V]. The LICENSE file sha256 is `a69ab694cc5a08793bc36673976a4bd97ef37a26786cd94a14072268550338f5`, which matches the ADMISSION json. Its git blob is `1e4336d0e2293baf91b4fc0ecebce2d976e959d5`, identical to the GitHub blob of `LICENSE` at commit 5690e332 [V]. I record this as MISMATCH against the claim as worded. It is a labelling error, not a file defect.
- All 10 parquet files plus the license, script, manifest and rowcount files listed in the ADMISSION json were re-hashed, and all match it [V]:

| file | sha256 | vs ADMISSION |
|---|---|---|
| `data/becker_kalshi_markets_t0_KXNFLGAME_part000.parquet` | `7238e85874f3e231…` | MATCH |
| `data/becker_kalshi_markets_t1_KXNFL_other_part000.parquet` | `138054988eadd147…` | MATCH |
| `data/becker_kalshi_markets_t2_KXNCAAF_part000.parquet` | `f1f3a918d6604d72…` | MATCH |
| `data/becker_kalshi_markets_t3_KXMLB_KXNBA_KXNHL_part000.parquet` | `aebec3d1a155b6a0…` | MATCH |
| `data/becker_kalshi_markets_t4_other_sports_part000.parquet` | `b1e13d8901be26e6…` | MATCH |
| `data/becker_kalshi_trades_t0_KXNFLGAME_part000.parquet` | `a1e1027e8fd1e5bd…` | MATCH |
| `data/becker_kalshi_trades_t1_KXNFL_other_part000.parquet` | `8aded2615aa60d9d…` | MATCH |
| `data/becker_kalshi_trades_t2_KXNCAAF_part000.parquet` | `0c91d375fcf9deb4…` | MATCH |
| `data/becker_kalshi_trades_t3_KXMLB_KXNBA_KXNHL_part000.parquet` | `80413fcf0abc25cc…` | MATCH |
| `data/becker_kalshi_trades_t4_other_sports_part000.parquet` | `736915ea2c3a85b9…` | MATCH |
| `license/README.md` | `b60f3f35845f1fa0…` | MATCH |
| `license/LICENSE` | `a69ab694cc5a0879…` | MATCH |
| `license/SCHEMAS.md` | `5e2746fe38c0e2e8…` | MATCH |
| `scripts/becker_stream.py` | `a906018ee7f5c4cd…` | MATCH |
| `scripts/file_stats.py` | `7da55173e4572316…` | MATCH |
| `scripts/run.sh` | `f002ca1377184060…` | MATCH |
| `MANIFEST_becker_data_tar_2026-10-03.tsv` | `3a276efde19b0aa3…` | MATCH |
| `kalshi_trades_series_rowcounts_all.csv` | `d36dabf7b430c7c1…` | MATCH |
| `kalshi_markets_series_rowcounts_all.csv` | `f016486724145a2a…` | MATCH |

- t0 KXNFLGAME trades claims: sha prefix a1e1027e **MATCH**; rows **8,297,967** (≈8.30M ✓); tickers **484** ✓; created_time 2025-05-20 23:14:09.518383+00 → 2025-11-25 20:37:30.960305+00 UTC (2025-05-20 → 2025-11-25 ✓) [V].

## 1. Timestamp semantics and TZ — PASS with caveat

| file | column | arrow type | tz | unit | min | max | nulls |
|---|---|---|---|---|---|---|---|
| `becker_kalshi_trades_t0_KXNFLGAME_part000.parquet` | created_time | timestamp[ns, tz=UTC] | UTC | ns | 2025-05-20 23:14:09.518383+00 | 2025-11-25 20:37:30.960305+00 | 0 |
| `becker_kalshi_trades_t0_KXNFLGAME_part000.parquet` | _fetched_at | timestamp[ns] | None | ns | 2025-11-25 20:33:29.133937 | 2025-11-25 20:48:44.762967 | 0 |
| `becker_kalshi_trades_t1_KXNFL_other_part000.parquet` | created_time | timestamp[ns, tz=UTC] | UTC | ns | 2025-03-27 18:40:39.562869+00 | 2025-11-25 21:00:16.516256+00 | 0 |
| `becker_kalshi_trades_t1_KXNFL_other_part000.parquet` | _fetched_at | timestamp[ns] | None | ns | 2025-11-25 20:27:19.380847 | 2025-11-25 21:00:48.331177 | 0 |
| `becker_kalshi_trades_t2_KXNCAAF_part000.parquet` | created_time | timestamp[ns, tz=UTC] | UTC | ns | 2025-02-11 16:31:59.89298+00 | 2025-11-25 20:03:21.957915+00 | 0 |
| `becker_kalshi_trades_t2_KXNCAAF_part000.parquet` | _fetched_at | timestamp[ns] | None | ns | 2025-11-25 19:44:26.725722 | 2025-11-25 20:13:39.593772 | 0 |
| `becker_kalshi_trades_t3_KXMLB_KXNBA_KXNHL_part000.parquet` | created_time | timestamp[ns, tz=UTC] | UTC | ns | 2024-12-19 15:02:47.191753+00 | 2025-11-25 21:02:04.481638+00 | 0 |
| `becker_kalshi_trades_t3_KXMLB_KXNBA_KXNHL_part000.parquet` | _fetched_at | timestamp[ns] | None | ns | 2025-11-25 15:24:04.987534 | 2025-11-25 21:08:12.294551 | 0 |
| `becker_kalshi_trades_t4_other_sports_part000.parquet` | created_time | timestamp[ns, tz=UTC] | UTC | ns | 2025-01-04 15:01:47.079456+00 | 2025-11-25 21:35:44.268844+00 | 0 |
| `becker_kalshi_trades_t4_other_sports_part000.parquet` | _fetched_at | timestamp[ns] | None | ns | 2025-11-25 01:59:22.041477 | 2025-11-25 21:50:21.141852 | 0 |
| `becker_kalshi_markets_t0_KXNFLGAME_part000.parquet` | created_time | timestamp[ns, tz=UTC] | UTC | ns | 2025-05-20 03:18:52.023108+00 | 2025-11-18 02:02:36.111796+00 | 0 |
| `becker_kalshi_markets_t0_KXNFLGAME_part000.parquet` | open_time | timestamp[ns, tz=UTC] | UTC | ns | 2025-05-20 14:00:00+00 | 2025-11-18 02:06:00+00 | 0 |
| `becker_kalshi_markets_t0_KXNFLGAME_part000.parquet` | close_time | timestamp[ns, tz=UTC] | UTC | ns | 2025-08-01 03:54:11.506822+00 | 2025-12-16 01:15:00+00 | 0 |
| `becker_kalshi_markets_t0_KXNFLGAME_part000.parquet` | _fetched_at | timestamp[ns] | None | ns | 2025-11-23 19:01:58.146849 | 2025-11-23 23:54:10.417397 | 0 |
| `becker_kalshi_markets_t1_KXNFL_other_part000.parquet` | created_time | timestamp[ns, tz=UTC] | UTC | ns | 2025-03-26 20:57:29.639574+00 | 2025-11-23 16:31:52.784446+00 | 0 |
| `becker_kalshi_markets_t1_KXNFL_other_part000.parquet` | open_time | timestamp[ns, tz=UTC] | UTC | ns | 2025-03-27 14:00:00+00 | 2025-11-23 16:36:00+00 | 0 |
| `becker_kalshi_markets_t1_KXNFL_other_part000.parquet` | close_time | timestamp[ns, tz=UTC] | UTC | ns | 2025-08-21 10:47:08.973504+00 | 2028-01-26 15:00:00+00 | 0 |
| `becker_kalshi_markets_t1_KXNFL_other_part000.parquet` | _fetched_at | timestamp[ns] | None | ns | 2025-11-23 18:52:26.699476 | 2025-11-24 00:42:23.389503 | 0 |
| `becker_kalshi_markets_t2_KXNCAAF_part000.parquet` | created_time | timestamp[ns, tz=UTC] | UTC | ns | 2025-02-10 22:59:31.527794+00 | 2025-11-23 17:05:48.617263+00 | 0 |
| `becker_kalshi_markets_t2_KXNCAAF_part000.parquet` | open_time | timestamp[ns, tz=UTC] | UTC | ns | 2025-02-11 15:00:00+00 | 2025-11-23 17:49:00+00 | 0 |
| `becker_kalshi_markets_t2_KXNCAAF_part000.parquet` | close_time | timestamp[ns, tz=UTC] | UTC | ns | 2025-08-23 16:38:47.845874+00 | 2028-01-19 15:00:00+00 | 0 |
| `becker_kalshi_markets_t2_KXNCAAF_part000.parquet` | _fetched_at | timestamp[ns] | None | ns | 2025-11-23 18:52:18.186593 | 2025-11-24 01:17:26.249327 | 0 |
| `becker_kalshi_markets_t3_KXMLB_KXNBA_KXNHL_part000.parquet` | created_time | timestamp[ns, tz=UTC] | UTC | ns | 2024-12-18 20:59:10.238615+00 | 2025-11-23 14:02:09.158507+00 | 0 |
| `becker_kalshi_markets_t3_KXMLB_KXNBA_KXNHL_part000.parquet` | open_time | timestamp[ns, tz=UTC] | UTC | ns | 2024-12-19 15:00:00+00 | 2025-11-23 19:06:00+00 | 0 |
| `becker_kalshi_markets_t3_KXMLB_KXNBA_KXNHL_part000.parquet` | close_time | timestamp[ns, tz=UTC] | UTC | ns | 2025-02-17 04:48:12.951904+00 | 2030-01-01 15:00:00+00 | 0 |
| `becker_kalshi_markets_t3_KXMLB_KXNBA_KXNHL_part000.parquet` | _fetched_at | timestamp[ns] | None | ns | 2025-11-23 18:52:50.511407 | 2025-11-24 01:53:26.293634 | 0 |
| `becker_kalshi_markets_t4_other_sports_part000.parquet` | created_time | timestamp[ns, tz=UTC] | UTC | ns | 2025-01-03 23:44:21.790409+00 | 2025-11-23 17:05:44.117335+00 | 0 |
| `becker_kalshi_markets_t4_other_sports_part000.parquet` | open_time | timestamp[ns, tz=UTC] | UTC | ns | 2025-01-04 15:00:00+00 | 2025-11-23 22:09:00+00 | 0 |
| `becker_kalshi_markets_t4_other_sports_part000.parquet` | close_time | timestamp[ns, tz=UTC] | UTC | ns | 2025-02-09 16:30:16.102565+00 | 2028-09-12 14:00:00+00 | 0 |
| `becker_kalshi_markets_t4_other_sports_part000.parquet` | _fetched_at | timestamp[ns] | None | ns | 2025-11-23 18:52:18.313179 | 2025-11-24 01:39:57.87318 | 0 |

- `created_time`, `open_time` and `close_time` are tz-aware UTC in all 10 files [V]: arrow `timestamp[ns, tz=UTC]`, parquet `isAdjustedToUTC=true`, pandas metadata `timezone: UTC`. Becker's parser reads the Kalshi API ISO-8601 `Z` strings (`models.py`) [V code]. Precision is µs: no sub-µs digits, and ≥99.9998% of trade rows have a sub-second part [V].
- `created_time` is the Kalshi `/markets/trades` field `created_time`, i.e. the exchange-side trade creation time in UTC [I]. Corroboration [V]: on t0 KXNFLGAME markets with a yes/no result, post-close prints sit within ≤60.04 s after `close_time` (3,423 rows on 180 tickers), and t3 is the same (≤59.97 s). That is consistent with both stamps coming from the same exchange clock [I]. t1/t2/t4 have some resolved markets with longer post-close prints (max 23.9 h) [V], so close_time semantics vary by series [I]. A direct check against our own tape is impossible (§2) [U].
- **`_fetched_at` is tz-naive in the file, and its zone is now determined to be UTC:**
  - Code [V]: Becker sets `_fetched_at = datetime.utcnow()` for both trades (`indexers/kalshi/trades.py`) and markets (`common/storage.py`), at HEAD 5690e332 and at 8173db87 (2026-02-01, the earliest version of that path). That the 2025-11 run used the same call is [I], because the archive predates both commits.
  - Trades [V]: read as UTC, rows with `_fetched_at < created_time` = **0**. Each ticker was fetched exactly once (0 tickers have more than one `_fetched_at`, matching the code). The minimum last-trade-to-fetch gap is **1.149 s**, and 45 tickers had their last print within 60 s of the fetch. So the zone cannot be ahead of UTC by more than about 1 s. A zone behind UTC (e.g. ET) would require dozens of independent tickers to stop trading exactly 5 h before the fetch [I].
  - Markets [V]: read as UTC, rows with `_fetched_at < created_time` = 0. Offset scan (`02b`): cumulative `volume` at the snapshot should equal Σ trade `count` up to the true fetch instant. Exact matches by offset (true = naive + h): -8h:264, -7h:303, -6h:338, -5h:402, -4h:484, -3h:616, -2h:771, -1h:1217, 0h:2574, 1h:1551, 2h:1164, 3h:930, 4h:831, 5h:769, 6h:712, 7h:662, 8h:626. The peak is at **0 h**, with 2574/2619 offset-sensitive markets matching exactly. The ET hypothesis (+5 h) gets 769 [V]. Resolution is 1 h; half-hour zones were not scanned, which is moot given the peak at 0.
- Snapshot instants [V]: markets were fetched 2025-11-23 18:52 → 2025-11-24 01:53 UTC, and trades 2025-11-25 01:59 → 21:50 UTC.

## 2. Spot-check against our dev tape — NO OVERLAP [V]

- The dev tape `/workspace/lab/astra-science/nfl_factorial_lab_20260921/inputs/events.jsonl.gz` has sha256 `cd300e664c2c5f2ff344c4b1eb17dd3f8e5f3326168b9dd8e3ade94a3a7382b4` [V]. Four other byte-identical copies exist under astra-kits/astra-science. It holds 681,732 trade and 364,988 quote records: 681,732 trade rows on 62 tickers, spanning **2026-09-03T00:20:17.069481+00:00 → 2026-09-20T21:24:59.385427+00:00** (2026 season).
- Becker trades, all tiers: 81,305 tickers, **2024-12-19 15:02:47.191753+00 → 2025-11-25 21:35:44.268844+00**.
- Overlap: tickers **0**, events **0**, trade_ids **0** [V]. Match rate, price agreement, count agreement and timestamp offset are **not computable [U]**. The windows are about 9 months apart.
- Note for any future cross-check [V]: (ticker, price, count, side, time) is **not unique** in Becker (t0 has 57,027 rows that share that tuple but carry distinct trade_ids), so match on trade_id only. Also, the dev tape carries fractional `size` and dollar prices, while Becker carries integer counts and cents.

## 3. Overlap with dev cohort, holdouts and ADMIT-1 — ZERO [V]

- **Dev cohort** (RESERVED_HOLDOUT `development_events`, 31 = `week_membership.json`; `markets.json` 62 tickers): Becker ticker hits 0, event hits 0. Measurement-dev events (2): 0.
- **NFL holdout 74507e1a** (32 games, kickoffs 2026-09-29T00:15:00+00:00 → 2026-10-13T00:15:00+00:00; 1 named event; frozen 2026-09-21T15:29:51.413345+00:00): hits 0. ADMIT-1 panel d0b28e69 (16 events, admitted_at 2026-09-22T21:18:13+00:00): hits 0.
- **Q6S5 KXMLBSPREAD holdout 9a987a77 / 370dc31d** (untouched events after a not-yet-stamped `holdout_admitted_at` [U]; events ≤26SEP29 and the 6 in-sample/Sep-25 events excluded): named-event hits 0. Becker has 40 KXMLBSPREAD events (240 tickers), dated 25SEP30 → 25NOV01, with 0 dated 2026.
- **ADMIT-1** is defined in addendum 370dc31d §3.4 and ACCEPT 9a987a77 as `[2026-09-27T00:00Z, 2026-09-30T04:00Z)`, half-open. Ruling ac7cfe63 gives the gap 2026-09-27T13:31:52Z → 2026-09-29T20:39:41Z and panel admitted_at 2026-09-22T21:18:13Z. Observed instants (trade `created_time`, both `_fetched_at`, market `created_time`/`open_time`) that fall in the ADMIT-1 window: **0**; on/after the ADMIT-1 panel admission: **0**; inside the dev-tape window: **0**; at any 2026 instant: **0** [V]. Embedded ticker date codes ≥26SEP01: 0; the latest is 260705 [V].
- Schedule-only `close_time` values recorded in the 2025-11-23 snapshot: 0 fall in the ADMIT-1 window, and 1688 fall on/after 2026-09-22 [V]. These are long-dated futures (max 2030-01-01 15:00:00+00). They are scheduled values, not observations, and every such market is truncated at the archive end. This is not contamination [I].
- Conductor's expectation ("none, archive ends 2025-11") is **verified** rather than assumed.

## 4. Integrity — PASS with caveat

- Trades, all 5 files [V]: exact-duplicate rows **0**; duplicate trade_ids **0**, and **0** across files; nulls/empties in trade_id, ticker, count, yes_price, no_price, taker_side, created_time and _fetched_at = **0**; `yes_price+no_price≠100` = **0**; yes_price outside 1–99 = 0; count ≤ 0 = 0; taker_side ∈ {yes,no}.
- Markets, all 5 files [V]: duplicate tickers 0; exact-duplicate rows 0; nulls in key fields = 0.
- ADMISSION json row and ticker counts: **all 10 match** (True) [V].
- Per-ticker gaps [V]: the distribution of the maximum inter-trade gap per ticker is in json `items.4_integrity.detail.integrity.trades.*.per_ticker_max_gap_s`. t0: median 18.2 h, p90 10.2 d; 59 tickers have a gap >7 d (pre-listing quiet periods on markets listed weeks ahead [I]). Gaps of this kind cannot be told apart from true holes without a second source [U].
- Truncation and completeness by tier [V]:

| tier | trade rows | tickers | closed mkts Σcount==volume | missing / total contracts (closed) | open at trade fetch (truncated) | vol≥100 mkts w/o trades | prints after close_time | max close_time |
|---|---|---|---|---|---|---|---|---|
| t0 | 8,297,967 | 484 | 190/428 | 672,187 / 2,980,735,840 | 56 (530,529 rows) | 0 | 155,863 | 2025-12-16 01:15:00+00 |
| t1 | 1,823,905 | 19,421 | 17,087/17,308 | 46,429 / 436,583,278 | 2,091 (333,124 rows) | 87 | 1,059 | 2028-01-26 15:00:00+00 |
| t2 | 8,876,384 | 15,432 | 14,594/15,120 | 644,991 / 2,902,086,357 | 312 (106,233 rows) | 25 | 2,136 | 2028-01-19 15:00:00+00 |
| t3 | 13,543,800 | 17,124 | 15,398/16,213 | 490,191 / 3,524,255,270 | 911 (336,947 rows) | 7 | 583 | 2030-01-01 15:00:00+00 |
| t4 | 11,276,798 | 28,844 | 27,052/27,977 | 2,076,662 / 2,493,932,504 | 867 (288,790 rows) | 286 | 18,196 | 2028-09-12 14:00:00+00 |

  - **Archive hard end cuts open markets [V].** Each ticker's trades were fetched exactly once (2025-11-25) and never refreshed, so markets open then are truncated. For KXNFLGAME, 58 markets were `active` at the snapshot, with close 2025-12-07 18:00:00+00 → 2025-12-16 01:15:00+00. KXNFLGAME games not yet listed at the 2025-11-23 snapshot (latest listed close 2025-12-16 01:15:00+00) are absent entirely: no late regular season, no playoffs [V/I].
  - **Volume reconciliation [V].** On markets closed at the snapshot, 74,321/77,046 tickers (96.46%) have Σcount exactly equal to `volume`. Total shortfall is 3,930,460 of 12,337,593,249 contracts (0.0319%). t0 is the weakest by ticker count (190/428 exact) but tiny in contracts: median relative shortfall 7.13e-05, max 0.0044. Cause [U]; candidates are API-omitted prints or volume definitions [H].
  - **Selection [V code / I data].** Trades were fetched only for markets with snapshot `volume ≥ 100`. Markets with volume 1–99 have no trades by design, and a few markets with volume ≥100 lack trades (column above; Becker logs fetch errors and continues) [H].
  - **close_time semantics [V].** For t0 and t3 yes/no-resolved markets, post-close prints are ≤60.04 s after close. Resolved markets in t1/t2/t4 have post-close prints up to 23.9 h (see json `postclose_split`). The 8 t0 no-result markets carry 152,440 prints up to 12.26 h after `close_time`, e.g. `KXNFLGAME-25SEP28GBDAL-*` (a no-result game). So `close_time` is not a trading-end marker on void/no-result markets [I].
  - Many prints share an identical ns `created_time` (multi-fill taker sweeps [I]): t0 has 773,448 zero-gap pairs.

## 5. License — FLAG, not blocking

- `license/LICENSE` is MIT, "Copyright (c) 2026 Jonathan Becker", covering "this software and associated documentation files" [V]. sha256 `a69ab694cc5a08793bc36673976a4bd97ef37a26786cd94a14072268550338f5`; git blob `1e4336d0e2293baf91b4fc0ecebce2d976e959d5` equals the GitHub blob at 5690e332 [V].
- README (`b60f3f35…`): no licence or terms statement for the hosted `data.tar.zst`. It asks users to reach out (email/Twitter) and lists citations [V]. The repo root has no other licence/terms file, `pyproject.toml` has no licence field, and a GitHub code search for "license" returns only LICENSE [V].
- Whether MIT covers the data is **[U]**. Kalshi-side terms on redistributing API-derived market data are also **[U]/[A]**. Recommendation: internal research use only, with attribution, and no redistribution until resolved.

## Safe uses
- [A] external prior for season-scale descriptive stats on 2024-12..2025-11 Kalshi sports trades (e.g. EXT-K2 flow-mix tercile stress), labelled [A], gross of fees, trade-only
- Base rates / priors that are computed only on closed markets with yes/no results (filter close_time <= _fetched_at and result in {yes,no})
- Sanity ranges for print size, cadence, price-band mix, pre/in-game split

## Unsafe uses
- Any replay, scoring, KEEP or promotion of strategy 000 or any Astra strategy
- Any use as holdout, OOS, or confirmatory evidence; any mixing into dev-cohort, holdout, or ADMIT-1 rows
- Quote, depth, queue, fill, or fee modelling (no quotes/book; markets yes_bid/ask are a single 2025-11-23 snapshot)
- Per-game metrics on markets open at 2025-11-25 (truncated) or on no-result/void markets (close_time unreliable)
- Treating close_time as the trading end without checking it per series (t0/t3 resolved: prints up to 60 s after close; t1/t2/t4 and void markets: hours); using (ticker,price,count,side,time) as a unique key
- Any redistribution of the data until the data licence is resolved [U]

## Reproducibility
- Scripts are in `/workspace/lab/astra-capture/external/becker_2026-10-03/clock/scripts/` (run in order `clock_01`→`clock_06`, using `/workspace/lab/.venv-clock`: duckdb 1.5.6, pyarrow 25.0.1, pandas 3.0.6). Intermediate outputs are in `/workspace/lab/astra-capture/external/becker_2026-10-03/clock/out/`. Becker reference source fetched read-only is in `/workspace/lab/astra-capture/external/becker_2026-10-03/clock/ref_source/`, with sha256 in the json.
- No Collector file was modified; all were re-hashed before and after. No Kalshi endpoint was contacted, and ADMIT-1 `capture.sqlite` was not opened.
