**Redaction header — Conductor ruling 3bff01cd (`CONDUCTOR_RULING_GV2_EXPOSURE_AND_CARD01_BUILDER_2026-10-03.md`):** ElectIndex values were redacted forward-only. The original is kept on the box only, sha256 `9be7f027a79af1807f9ac0579efffc63465aec5f66af4625976b8b24801691fb`.
# ADVERSARY: Card 01 / NH-002-H leakage & circularity check (2026-09-24 ET)

**Seat:** The Adversary "KALSHI" (Astra Drift Guard), Working Plan v0.1. **ADVISORY ONLY**: this packet blocks nothing, votes on nothing, changes no frozen parameter. No live orders. No messages sent.
**Target:** `packets/CARD01_HOUSE_ONLY_PROSPECTIVE_FREEZE_2026-09-24.md` (sha256 `c31724463d81747702910a2d5296c2fc21d2a1dbc594727b26ac3d894b55ec59`, re-hashed now: matches `FROZEN_EXPERIMENT.json`) and Amendment A (`..._AMENDMENT_A.md`, sha256 `4e36d0db5728148d5bb4688fd8626eca9907a8933747f85e0bc17ede0ac0936b`, matches).
**Prior Adversary ruling:** card 01 PROCEED_WITH_DIFFERENTIATOR (`packets/ADVERSARY_DEAD_CARD_OVERLAP_EDGE_RESEARCH_2026-09-24.md`).
**Tags:** [V] verified · [I] inferred · [H] hypothesis · [A] assumption · [U] unknown.
**Q6-`000`: unchanged.** S2/R2-P4 gating: unchanged.

---

## Verdict (top line)

| Question | Ruling |
|---|---|
| 1. Independence of ElectIndex House forecast | **INDEPENDENT** of prediction markets, as documented [V]. Market-price weight share = **0%** in every published component. Residual: model **code** (`src/model`) is not in the public repo, so this is a documentary + input-file check, not a code audit [U]. |
| 2. Timestamp (universe + w grid before any 2026 price) | **w grid: VERIFIED** before any 2026 price (git 04:53:45Z vs first 2026 book GET 05:19:58Z) [V]. **Universe: VERIFIED as price-independent by reproduction** (the 93-race rule reproduces exactly from the forecast-only snapshot) [V]. The claim "written before any 2026 price was viewed" is **ASSERTED only** [A]: 2026 book data for 3 contracts (incl. in-universe AL-02) was already on the box ~5 min before pre-commit. Low materiality. |
| 3. One-draw handling | **Both present** [V]: state-cluster bootstrap (PASS gate) and a national common-factor recentering check (REJECT (b)). PASS is judged on state-clustered uncertainty, not 92 iid races, and the freeze itself scopes a PASS to "this cycle" [V]. Gaps: recentering implementation not hash-pinned; no adverse-national scenario stress (§3). |
| 4. Other flags | 6 evidenced flags (fee pin does not cover the series; ElectIndex model changed 2–3 days pre-freeze, no methodology-version capture; unanchored timestamps; recentering spec ambiguity; legacy-series attrition/depth unmeasured; gate (c) text outdated). None is a leak of outcomes. |

**Overall advisory:** no leakage or circularity found that would invalidate NH-002-H. Proceed as frozen. The fixes below are cheap and pre-outcome.

---

## 1. INDEPENDENCE: what ElectIndex is and what it ingests

**Identity [V]:** freeze §2 names the source as "ElectIndex `output/races_summary.csv`, field `dem_prob` … from https://github.com/ElectIndex/26_us_forecast_data". Publisher site https://electindex.com (GitHub org `ElectIndex`, blog = electindex.com). The site says it was formerly "MapWise".

**Methodology location [V]:** there is no `/methodology/` URL (both `https://electindex.com/methodology/` and `/forecasts/methodology/` return 404, curl 2026-09-24 ~20:05 ET). The full methodology renders in the **Info tab at https://electindex.com/forecasts/#info**. It is served from `https://electindex.com/wp-content/themes/electindex/assets/forecasts/eifc-info.js?ver=1.9.989` (sha256 `caaff53e739413a8340f0addbec7136ec1995195291cab61889a94c1286ea87f`, fetched 2026-09-25T00:05Z = 20:05 ET). The summary is on https://electindex.com/forecasts/ (WebFetch 20:04 ET).

**Verbatim quotes (all accessed 2026-09-24 20:04–20:06 ET):**
- https://electindex.com/forecasts/ : "Every race combines two ingredients. A fundamentals estimate captures what we know before the polls — the seat's partisan lean, incumbency, candidate fundraising, and the demographic makeup of the electorate. A polling average captures what voters are telling pollsters right now." [V]
- same page: "Sitting on top of every race is the national environment — generic-ballot polling, presidential approval, and a basket of economic indicators from the Federal Reserve." [V]
- Methodology §6 (forecasts/#info): "The forecast margin is the weighted average of fundamentals and polling:" `margin = (1 - w) F + w P` [V]
- Methodology §3: F = lean + G + 0.75·ln((50,000+$_D)/(50,000+$_R)) + ⅔(I+s) + δ_demo [V]. §2: G blends "the de-biased generic-ballot polling average" with an approval model and an economy model on "jobs, real income, consumption, industrial production, inflation, real GDP and the S&amp;P 500 (all from FRED)" [V]. (The S&P 500 is an equity index, not an election or prediction market.)
- Methodology §8, on ratings: "They are an <em>output</em> of the model, never an input." [V]
- Data credits (forecasts/#info): "The forecast is built entirely from public data." Sources listed: NYT (polling averages and precinct results), cinyc9/RRH, DRA, VEST/RDH, FEC, MultiState, Ballotpedia, FRED, Census, us-atlas [V]. No prediction market, sportsbook or forecaster aggregate is listed.
- https://electindex.com/disclaimer/ (Last updated September 1, 2026): "Our models draw on third-party and public data — including polls, the FEC, FRED, the U.S. Census, and precinct and redistricting sources" [V]

**Input-file check [V]:** I read the repo root tree at tree sha `c60dc731…` (same tree sha recorded at the freeze probe, so the repo is unchanged since then) through the read-only GitHub connector. I pulled `race_polls.csv`, `manual_race_polls.csv`, `gcb_polls.csv`, `approval_polls.csv`, `pollster_ratings.csv`, `national*.csv`, `races.csv`, `fred_cache.json` and `predecessors.csv` from raw.githubusercontent.
- `rg -i 'kalshi|polymarket|predictit|betfair|betting|odds|market'` hit only the pollster name "Targoz Market Research".
- `fred_cache.json` keys are FRED series (GDP, PCE, CPIAUCSL, PAYEMS, PI, …).
- There is no input file for any forecaster, aggregator or market.

**Indirect channels:**
- *Other forecasters/aggregates:* none ingested [V: input list + credits]. The NYT feed supplies **poll rows** ("Per-race NYT matchup polls", README), not NYT model output [V]. Whether NYT's own averaging uses markets: not applicable, because ElectIndex re-averages the raw rows itself (§5) [V].
- *Expert ratings (Cook/Sabato/Inside Elections):* **not a House input** [V]. They appear only in the state-legislative input `leg_races_2026.csv` ("Cook/Sabato ratings where available", README), and the leg model formula (§17) has no ratings term [V]. Federal ratings are model outputs (quote above).
- *Non-market but non-public input (minor):* `manual_race_polls.csv` includes a poll memo with "no public URL, PDF supplied by the user" (OH-07) [V]. This is not a market channel. Noted only for provenance.

**Ruling: INDEPENDENT** (weight share of prediction-market prices = 0 in lean, G, F, P, the w blend and σ_t) [V documentary].
- **Residual [U]:** the methodology says "All of the code below lives in <code>src/model</code> of the open-source repository", but the public repo `ElectIndex/26_us_forecast_data` has **no `src/` tree** (root listing, 48 entries) [V]. Code-level absence of market inputs therefore cannot be audited.
- Freeze gate (b) can move from "UNVERIFIED" to "documented independent; code unaudited". That is the owner's call (Archivist/Conductor).
- **Reverse channel [H]:** ElectIndex is public, so Kalshi traders may already price it. That biases NH-002-H toward the null. It is not circularity.

## 2. TIMESTAMP: universe and w fixed before 2026 prices?

| Item | Evidence | Tag |
|---|---|---|
| w grid {0.25 sensitivity, 0.5 primary, model-only} | Predecessor `SPEC.md` lines 56–58 ("Primary hybrid: 0.5*p_model + 0.5*p_market", "Sensitivity only: 0.25…"). Committed in `7daf8665` "Preregister NH-001…", author/committer date **2026-09-24T04:53:45Z**. It is the only commit touching SPEC.md up to 2253c03c. The local blob `edfce090…` equals the GitHub blob at 2253c03c. The first 2026 book request started **05:19:58Z** (`current_book_smoke.json`, committed in `6de80155` at 05:30:51Z). | [V] (git dates are client-set, so there is no server-side push-time anchor) |
| Universe rule and list | `PRECOMMIT_UNIVERSE_WEIGHT_2026-09-24.json`: sha256 `2968f389…e77e` re-hashed and matching; `precommit_at_utc` 23:48:37Z; file mtime 19:48:37.18 ET. **Reproduced now:** from `source_probe_electindex/races_summary.csv` (sha256 `eb65e9aa…daf0`, received 23:45:43Z), House rows with dem_prob ∈ [10,90] = 93, identical to the pre-commit list. AK-01 exclusion uses forecast fields only. `UNIVERSE_2026_HOUSE_FROZEN.json` sha `d8af7451…8ca6` matches. | [V] |
| First live 2026 Kalshi price GET this session | `http_log.jsonl`: every KXHOUSERACE/CONTROLH GET before 23:48:55Z returned **429**. The first 200 was `markets/KXHOUSERACE-AL02-26-D` at **23:48:55Z**, 18 s after the pre-commit; page 0 came at 23:48:58Z. The series lists (23:34Z) contain no price fields (`rg yes_bid|yes_ask|last_price` = 0 hits). | [V] (log is self-written) |
| "Written BEFORE any 2026 KXHOUSERACE price was viewed" | The recovered predecessor files landed on the box at **19:43:53–19:43:54 ET** (mtimes), ~5 min **before** the pre-commit. They include `results/current_book_smoke.json` and `data/current_book_levels.json`: full 2026 books for KXHOUSERACE-AL01/**AL02**/AL03-26-D captured 05:20Z (AL-02 YES bid/ask 0.28/0.29, and AL-02 is in the universe). SOURCE_MAP C5/B3 mark them "inspected" with no time. Ledger E3 (~19:4x) lists RESULTS/SPEC/AMENDMENT_A/NEXT_EXPERIMENT/scorecard but not the smoke file. Local blobs equal GitHub blobs (`fbf81834…`, `bc72237d…`). | **[A]** (whether Deep Research read them before 23:48:37Z is [U]) |
| Freeze time | Freeze file mtime 19:52:48.49 ET = the stated `2026-09-24T23:52:48Z`. Amendment A mtime 19:59:50.52 ET = stated 23:59:50Z. | [V] mtimes; not externally anchored |
| Other pre-freeze price captures | `rg -l KXHOUSERACE` across `[REDACTED: private box path]` plus a filesystem name search: no other 2026 House price file predates the pre-commit. `astra-capture/card01-nh002-house/` does not exist yet. The Collector mapping run (`collector_mapping_get_2026-09-24/`) starts 20:05 ET, after the freeze. | [V] |

**Finding:** the headline w = 0.5 and the grid are verified to predate all 2026 price exposure. The universe is verified price-independent by mechanical reproduction from a forecast-only file. The narrative claim "no 2026 price viewed before pre-commit" is asserted and slightly contradicted by what was on disk. It is immaterial to selection, because the rule is mechanical and the only in-universe exposed race (AL-02) enters on its forecast ([REDACTED: ElectIndex ToS re-gate; box copy sha256 9be7f027a79af1807f9ac0579efffc63465aec5f66af4625976b8b24801691fb]%). **Ask (Deep Research/ledger owner):** add a ledger footnote disclosing the 3 pre-existing 2026 books. No re-freeze is needed.

## 3. ONE-DRAW: correlated House outcomes

- **State-cluster bootstrap: PRESENT [V].** Freeze §6: "State-cluster bootstrap, 10,000 resamples of states with replacement, seed 20261102", 95% percentile CI. PASS-FORECAST (i) requires CI upper < 0, and REJECT (a) fires if it is ≥ 0. Leave-one-state-out is reported.
  - Clusters: 28 states. The 3 largest hold 35/92 races (FL 15, TX 11, NC 9) [V, recount].
- **National-miss check: PRESENT as a diagnostic gate [V].** Freeze §6: "Recenter each forecaster by subtracting its own across-race mean logit error. This removes a uniform national miss. … If the recentered CI includes 0, the verdict is 'common-factor only'". This binds as REJECT (b) and PASS (ii).
- **Pass bar on correlated uncertainty? Partially, and honestly scoped [V].** Uncertainty is state-clustered (not iid races), plus the recentering test. The freeze states: "The state bootstrap does **not** capture the national common factor. One election is one draw of that factor … A PASS is therefore at most **prospective paper evidence for this cycle**, not repeatability". It also says "the report must state that it is conditional on one election."
- **Gaps (advisory):**
  - (a) [V] The recentering spec "mean logit error" is not well-defined against binary outcomes. The only implementation is `EXPLORE_DIAG_national_factor_recentered_2253c03c.py` (sha256 `feffec51…d144`), written at 19:53 ET after the freeze. It uses a calibration-in-the-large shift (bisection so mean p = mean y) and is **not pinned** in the freeze. **Ask:** Examiner/Variants declare that exact script (or a hash-pinned port) as the implementation before any 2026 outcome exists.
  - (b) [V] Recentering removes only a *uniform* shift. Heterogeneous exposure to the national factor remains; decision packet §6 admits this.
  - (c) [V] There is no adverse-national *scenario* (e.g. ±X-pt national swing applied to all races) for the hypothetical book. The predecessor NEXT_EXPERIMENT asked to "Track … both adverse national scenarios". The freeze has top-1/HHI concentration but no national-shift stress. Impact is low because P&L is descriptive (~9 signals), but it would make the one-draw exposure visible. **Ask:** add it as a reported (non-gating) row.

## 4. Other evidenced flags (leakage / lookahead / fee / capacity / drift)

1. **Fee pin does not cover the series [V].** R1-P1 @ `22371178` `series_fee_table.stub.json` has `"overrides": {}` with default M=1, taker 0.07. `KXHOUSERACE` and `HOUSE<ST><N>` therefore resolve as `default_unknown_series`, i.e. the **same** `0.07·p·(1−p)` the freeze calls "sensitivity only". Freeze §5 wording ("taken from the pinned feebook for `KXHOUSERACE`") overstates coverage. Because the fee enters the **signal gate** (side selection at feasible fills), the true House-series fee must be confirmed in the Archivist manifest before 2026-11-02. Otherwise the traded set itself is on an unverified fee. The real series fee is [U].
2. **Source drift: ElectIndex changed its model 2–3 days before the freeze [V].**
   - Methodology §5: "Added on 21 September 2026, part-way through the cycle. Forecasts published before that date were not re-run".
   - §7: the late-cycle boost "phases in over the final six weeks, so forecasts published through 22 September 2026 are unchanged."
   - The model scored on 2026-11-01 will not be the model admitted on 09-24, and more changes are possible [I].
   - The freeze captures CSV bytes/sha but no model version. The predecessor spec required "model version".
   - **Ask:** Collector also records daily sha256 of `eifc-info.js` / the #info methodology (hash only, per the Archivist ToS scope), so a mid-cycle methodology change is visible at scoring.
   - No-backfill is good [V]: ElectIndex says earlier forecasts "were not re-run", and the freeze already bars use of `output/historical/`.
3. **Forecast/quote alignment: no lookahead found [V].** The forecast is the latest *our-receipt* ≤ 2026-11-01T22:00Z (24 h lag, ≤ 7 d old). The book window is 21:45–22:15Z Nov 2, with snapshots older than 15 min excluded. The lag makes the forecast staler than the mid, which biases toward the null. Dry runs are unscored. Not a flag; recorded as a pass.
4. **Timestamps are not externally anchored [V].** `[REDACTED: private box path]` is not a git repo. Pre-commit, freeze and amendment times rest on file mtimes and a self-written http_log that agree with each other. **Ask:** Archivist commits or pushes the hash set (pre-commit, universe, freeze, Amendment A, ElectIndex snapshot) promptly, so the pre-outcome ordering has a third-party timestamp.
5. **Universe attrition and depth for legacy series [V].** 34/92 races sit in legacy HOUSE* series that are not yet verified: HOUSEPA10/HOUSEME2 GETs were 429 ×2. Their liquidity is unmeasured (Amendment A). If they fail mapping, the scored set drops the most competitive seats. The mapping rule is rules-text-only and price-blind [V], so this is not leakage. **Ask:** Examiner reports n and D by mapping status (KXHOUSERACE vs legacy vs excluded).
6. **Gate (c) text is out of date [V].** The ElectIndex Info tab now carries a track-record card: "Old Forecast … Published for 2022 &amp; 2024" (as MapWise) and "Current Forecast … 2026 model, backtested 2004–2024", described as "A backtest of today's model, not a forecast that was published at the time" (`eifc-trackrecord.js`, sha256 `6aed2d13…`). I did not check the numbers. The backtest is not out-of-sample evidence.

**Capacity [V, freeze §8 / Amendment A]:**
- about $380 top-of-book deployable;
- about $30 ex-ante EV for the cycle;
- median in-universe `volume_24h_fp` 3.04.
This is stated honestly and is not the headline, so no capacity-fantasy flag. The only gap is the unmeasured legacy-series depth (flag 5).

## Sources (accessed 2026-09-24 20:04–20:08 ET)

- https://electindex.com/forecasts/ (WebFetch)
- https://electindex.com/forecasts/#info, served by `…/assets/forecasts/eifc-info.js?ver=1.9.989` (curl; sha above)
- https://electindex.com/disclaimer/
- https://electindex.com/terms-of-service/
- https://electindex.com/sitemap.xml
- https://github.com/ElectIndex/26_us_forecast_data: tree `c60dc731…`, via the read-only GitHub connector; raw input files from raw.githubusercontent.com
- https://github.com/17thgreen/GPT-6-Astra-Deathmatch/commit/2253c03cd86eb5515325f1d91b43bdcbea7a902c (05:31:47Z); commits `7daf8665` (SPEC, 04:53:45Z) and `6de80155` (book smoke, 05:30:51Z)
- Local: freeze and Amendment A, `card01_hybrid_forecast/{PRECOMMIT…, UNIVERSE…, LEDGER…, SOURCE_MAP…, FROZEN_EXPERIMENT.json, live_get_2026-09-24/http_log.jsonl, source_probe_electindex/, recovered_2253c03c/}`, and the R1-P1 feebook @ `22371178` (read via `git show` in `[REDACTED: private box path]`, read-only)

**Not done / not found:**
- The local `[REDACTED: private box path]` clone does not contain `2253c03c` (it is 3 behind origin/main, with a dirty index). No fetch was run; GitHub connector reads were used instead.
- ElectIndex model code is not public.
- The ElectIndex track-record numbers were not checked.
- The live Collector mapping run (20:05 ET onward) was not reviewed.
