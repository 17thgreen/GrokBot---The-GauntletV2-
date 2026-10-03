# EXT-K3 — NFL INJURY-REPORT WINDOW TOXICITY (BOX HALF) vs Q6-000 — MEASUREMENT-ONLY FREEZE (spec only; no implementation; no results)

**File date:** `2026-10-03` (ET). **Frozen / declared at:** `2026-10-03T18:07:03-04:00` (ET, America/New_York, UTC−4). Every rule below, including each UNPINNED resolution, is stated **before** any implementation. **No outcome metric was computed before freezing:** for this packet Variants computed **no markout, no adverse-selection figure, no mid at any horizon, no price move, no in-window vs control comparison, no PnL and no ROI**. The only numbers computed are (i) the window table, derived from the NFL's published report schedule before any market byte was read, (ii) label-free structural counts (rows, fills, contracts, trades, quote rows, control windows available), and (iii) a reproduction of K1's published whole-ledger fee total ($1,286.22), which the Conductor asked to be locked by a Decimal test.
**Owner:** R&D Variants (freeze; implement only after Conductor ACCEPT, and only after the sequencing in §9) → one Variants cloud (implement + run on dev data) → Adversary → Examiner (verdict, account-class pin)
**Status:** FROZEN, FREEZE_ONLY. Awaiting Conductor **ACCEPT**; implementation comes **LATER** (after the K2 PR67 merge, the K1 follow-up PR for N1/N3/N5/N6, and the card01 Amendment C code). No cloud launched, no PR, no commit, no push, no message, no Kalshi call, no orders, no `admit.py`, no `capture.sqlite`, no weather `archive.sqlite`, no Becker byte. This packet writes new files on the box only.
**Experiment id:** `EXT-K3-NFL-INJURY-WINDOW-TOXICITY` · **Kernel:** EXT-K3 box half (Scout external hunt 2026-10-03) · **Incumbent measured:** Q6-000 (`q3300_d0.25_000`, NFL `KXNFLGAME` maker pairing allocator, SHADOW)
**Sister freezes / format templates:** EXT-K1 `5c40fb9d…` (ACCEPT `02129007…`, merged `09b56273`, scored DESCRIPTIVE) and EXT-K2 `d69a4f62…` (ACCEPT `d76779e1…`; PR67 in flight). K3 **cites** K1 definitions ("K1 R19") rather than redefining them.
**Feature family:** `scheduled_news_window_toxicity` (measurement). **Knobs on 000: zero. Parameters of 000 changed: zero.**
**Evidence tags:** [V] verified on box / in a saved source this session · [I] inferred · [H] hypothesis · [A] assumption · [U] unknown.
**Proposed lab dir:** `kalshi_ext_k3_injury_window_lab_20261003/`. Not created.

## 0. Governing ruling, kick and commission

- **Ruling** `packets/CONDUCTOR_RULING_SCOUT_EXTERNAL_HUNT_2026-10-03.json` sha256 `870895a58e80fd1442d0ce97e42df02426bf7e38f64dcd091efc6fbf26b74ebf` [V] (full bytes quoted in K1 §0). Binding keys, verbatim:
  > `"EXT-K3": "TRY box half third (Wed-Fri injury-report windows). Inactives half HOLD on egress."`
  > `"fee_rounding": "Examiner pins. Until account member-type is resolved, score with the conservative non-direct-member rule (fees rounded up to $0.01 per order); may also report the $0.0001 direct-member figure as a sensitivity, never as the headline."`
  > `"dev_grade": "All box-scorable results on the reused 31-game dev cohort are dev-grade, not OOS; no KEEP from them."`
- **Kick** `packets/CONDUCTOR_KICK_VARIANTS_EXT_K3_INJURY_WINDOW_FREEZE_2026-10-03.json` sha256 `3816c54e…` (full in `SOURCE_PINS.json`) [V], issued 17:54 ET. `scope`, verbatim: "Freeze measurement-only on 31-game DEV B1+B2 (±15–30 min around Wed/Thu/Fri 16:00 ET injury windows). Inactives T−90 half WAIT on Logan egress. No Kalshi GET. No live orders. Verdict domain DESCRIPTIVE/ITERATE/INCONCLUSIVE only unless freeze says otherwise."
- **N6 ruling** `packets/CONDUCTOR_RULING_EXT_K1_N6_UNDEFINED_DELTA_2026-10-03.json` sha256 `0b68c4bf…` [V], verbatim: "Prospective only: undefined Delta* or undefined CI => verdict INCONCLUSIVE." K3 adopts it **from the start** (R25).
- **K2 PR67 ruling** `packets/CONDUCTOR_RULING_EXT_K2_PR67_R45_HISTORY_2026-10-03.json` sha256 `ac8e26c8…` [V]: "freeze md/json pinned by sha not vendored"; merge gate "Decimal fee fix". Both bind here (R20, R33).
- **Commission (Conductor scope, relayed in the delegation text; no on-box file beyond the kick → provenance [U], Archivist to file).** Binding points, paraphrased as received: box half only (Wed/Thu/Fri injury-report windows ≈16:00 ET on the DEV tape + 000 ledgers B1/B2; 000 fill markout and adverse selection inside windows vs matched outside windows); inactives T−90 = HOLD, out of scope; no Kalshi GET, no Becker, no holdout, nothing in ADMIT-1 `[2026-09-27T00:00Z, 2026-09-30T04:00Z)`; dev-grade; verdict ∈ {DESCRIPTIVE, ITERATE, INCONCLUSIVE}; N6; fee headline $0.01 per order round-up with **Decimal** and a test (K2 float bug $1,286.59 vs $1,286.22), `CACHE_NOT_R1P1`; **window times fixed from the NFL's published schedule before anything touches markouts**; primary half-width chosen a priori with sensitivities; controls, estimand, clustered vectorized bootstrap with an equivalence test, n_eff; outputs carry python_version + platform; full-rebuild invariance with a constancy sha; tests vs fixtures; freeze md/json pinned by sha, never vendored; no third-party redistribution; implementation later.

| # | Requirement | Where met |
|---|---|---|
| C1 | Window times from NFL's published schedule, fixed first, sources saved with sha | §3, R04–R07, `nfl_sources/`, §6 ordering log |
| C2 | DST-aware ET→UTC; concrete frozen window table | R06, §3.4, `WINDOWS.json` `79756fc5…` |
| C3 | Primary half-width a priori + sensitivities | R08 |
| C4 | Inactives half out of scope | R32 |
| C5 | Metrics: markout at pre-declared horizons, signed from 000's side; AS = −MO; one primary horizon | R15–R19 |
| C6 | Matched controls, deterministic, no overlap with windows / ADMIT-1 | R10–R13, `WINDOWS.json` controls |
| C7 | Δ = in − control; game-cluster bootstrap, fixed seed/B, vectorized + equivalence test; n_eff | R22–R24, T06 |
| C8 | Verdict map; ITERATE cap; N6 → INCONCLUSIVE | R25, §7 |
| C9 | Fee headline Decimal $0.01/order, test, CACHE_NOT_R1P1 | R20, T05 |
| C10 | python_version + platform; full-rebuild invariance + constancy sha; tests vs fixtures; freeze pinned by sha not vendored; no redistribution | R29, R33, R36, T03, T12, T16 |
| C11 | Refuse list | R30, R31, §12 |
| C12 | Structural counts allowed; no outcome metric before freezing | §4, §6 |
| C13 | Packet folder with SOURCE_PINS, WINDOWS, MANIFEST; optional bundle | §10 |

## 1. What is measured (read from box)

- Q6-000 = `q3300_d0.25_000`, SHADOW-only hypothetical replay; every fill is a "public tape hypothetical match" (K1 §1) [V]. **All quantities describe the replayed 000, not real execution.** 000 rests NO bids on both teams and fills when a YES-taker prints (`replay_v2.py:218`, `queue_policies.py:37`; Scout §0) [V]. 000's entry band is `full` (quotes from tape start) and its replay ends at K−3h per event (`queue_policies.py:205`) [V].
- Thesis [H] (Scout §3 EXT-K3): scheduled injury news at the ≈16:00 ET report deadline lets informed takers hit resting quotes before makers react, so 000's fills inside report windows may mark out worse than comparable fills outside. K3 **measures** that contrast. It does not test, tune, gate, keep or kill 000; any stand-down arm is a separate freeze (R28).

## 2. Pins (re-hashed on box 2026-10-03 18:00–18:05 ET; every K1-reused pin MATCHES)

| Item | Path (relative to `/workspace/`) | sha256 | Notes |
|---|---|---|---|
| **Governing ruling** | `lab/governance/astra/packets/CONDUCTOR_RULING_SCOUT_EXTERNAL_HUNT_2026-10-03.json` | `870895a58e80fd1442d0ce97e42df02426bf7e38f64dcd091efc6fbf26b74ebf` | [V] |
| **K3 kick** | `…/packets/CONDUCTOR_KICK_VARIANTS_EXT_K3_INJURY_WINDOW_FREEZE_2026-10-03.json` | `3816c54e` (full in SOURCE_PINS) | [V] |
| **Scout brief (post-edit)** | `lab/governance/astra/SCOUT_EXTERNAL_HUNT_2026-10-03.md` | `13e442892d27466f3ee3082509a47ac9706c7f3448aa079de798bec8cb1a1dfb` | K3 = §2 row + §3 "EXT-K3" [V] |
| N6 ruling / K2 PR67 ruling | `…/CONDUCTOR_RULING_EXT_K1_N6_UNDEFINED_DELTA_2026-10-03.json` / `…/CONDUCTOR_RULING_EXT_K2_PR67_R45_HISTORY_2026-10-03.json` | `0b68c4bf…` / `ac8e26c8…` | [V] |
| K1 freeze md / json / ACCEPT / packet MANIFEST | `…/VARIANTS_EXT_K1_Q6000_LEGGING_RISK_AUDIT_FREEZE_2026-10-03.{md,json}` / `…/CONDUCTOR_ACCEPT_EXT_K1_FREEZE_2026-10-03.json` / `…/EXT_K1_LEGGING_AUDIT/MANIFEST.sha256` | `5c40fb9d03a924e40577a81f262231701e331c98922f60f6dc7ab65a2dbed6d3` / `be3e88336389bc62c40413785e6ffb4a572e1dbd006d7cf3dfbc962f8184efaa` / `021290077cbbed277455145d2e56e1335f6ae331d56c2ad79d4d85b405559397` / `5e8f79063f132fe2db97ad3ecff5fea463d429f167abed09c58398a87fcadf01` | MANIFEST 9/9 OK; K1 SOURCE_PINS 38/38 re-hashed OK [V] |
| K1 Examiner scorecard / score / Adversary review / merge | `…/EXAMINER_SCORECARD_EXT_K1_Q6000_LEGGING_AUDIT_PR66_2026-10-03.md` / `…/EXAMINER_SCORE_…json` / `…/ADVERSARY_EXT_K1_PRESCORE_REVIEW_2026-10-03.md` / `…/CONDUCTOR_MERGE_PR66_EXT_K1_2026-10-03.json` | `b5e08bf8…` / `0e5b1060…` / `676ba2fa…` / `9de0933b…` | N1/N3/N5/N6 pre-empted in R25/R29/T03/T12/T16 [V] |
| K2 freeze md / json / ACCEPT / MANIFEST | `…/VARIANTS_EXT_K2_OPTIMISM_TAX_DEPENDENCE_STRESS_FREEZE_2026-10-03.{md,json}` / `…/CONDUCTOR_ACCEPT_EXT_K2_FREEZE_2026-10-03.json` / `…/EXT_K2_OPTIMISM_TAX/MANIFEST.sha256` | `d69a4f62…` / `025a01a1…` / `d76779e1…` / `3478b405…` | template [V] |
| **K1 pin bundle (reused by sha)** | `EXT_K1_authentic_pins_2026-10-03.tgz` (+ `.part-00` / `.part-01` / `.PARTS.sha256`) | `0f8f529733bfd1ccb01b36f312cdc20865cc2811c04dcd3c812d50c67295db38` (25,008,407 B); parts `3fd70f7b…` / `1f8b2ac1…`; PARTS `a92df01d…` | concat(parts) = `0f8f5297` re-verified [V]; holds B1, B2 fills, markets, cohort, nflverse csv, holdout + fee pins |
| **B1 dev tape** | `lab/astra-science/nfl_factorial_lab_20260921/inputs/events.jsonl.gz` | `cd300e664c2c5f2ff344c4b1eb17dd3f8e5f3326168b9dd8e3ade94a3a7382b4` | 681,732 trades + 364,988 quotes; 62 tickers / 31 events [V] |
| B1 markets / manifest / cohort | `…/inputs/markets.json` / `…/inputs/manifest.json` / `…/inputs/week_membership.json` | `66cc07e9e9e1543b3fdcbcded30ff50af0abae87bb2aa3d5fcb3d0be7925632f` / `375ea6e2c9125a411d5444a88115213542d5b19c874d73a2bed0b9355fd6277d` / `a47d0e0dc5a64d79335bc5588f8aa5e1d937503d36ebcbaaf219965a68adf88c` | kickoff epochs = game-day source [V] |
| **B2 000 fills** | `…/results/q3300_d0.25_000_fills.jsonl.gz` | `9d56f5d3c599e092606be9f4a1ad41ae8baabff4921d3d722adf0b57ac944a3f` | 12,853 rows (12,837 maker / 16 taker) [V] |
| B2 orders / summary / decisions | `…/results/q3300_d0.25_000_orders.jsonl.gz` / `…/results/q3300_d0.25_000.json` / `…_decisions.jsonl.gz` | `c390801b…` / `78b94ae5…` / `e6db5237…` | orders pinned not used; summary = config only; decisions pinned, not read. B2 = q3300_d0.25_000 arm only (K2 §2.1) |
| Replay code | `…/replay_v2.py` / `…/queue_policies.py` / `…/run_experiment.py` | `5aba1bf3…` / `641d0df3…` / `c1a0fd2d…` | untouched (T14) |
| NFL reserved holdout / KXMLBSPREAD prereg / ADMIT-1 ruling | `…/RESERVED_HOLDOUT.json` / `…/CONDUCTOR_ACCEPT_VARIANTS_HOLDOUT_PREREG_ADDENDUM_…json` + `…md` / `…/CONDUCTOR_RULING_ADMIT1_OUTAGE_GAP_WEATHER_CARD03_RELAUNCH_2026-09-29.json` | `74507e1a…` / `9a987a77…` + `370dc31d…` / `ac7cfe63…` | refusal only [V] |
| nflverse games.csv | `lab/governance/astra/packets/scout_external_hunt_2026-10-03/raw/nflverse_nfldata_games.csv` | `683673b5f33c46c1c0fbe6535964b245ceea6984e144bf4b52bd8afaeec91cd6` | **schedule columns only** (`season, game_type, week, gameday, weekday, game_id, location, stadium`) for the full W1–W2 slate (clean-day sensitivity + weekday cross-check). No score, result or moneyline column read |
| Fee CACHE | `…/scout_house_fee_2026-09-24/raw/docs/{kalshi_fee_schedule.txt, docs_fee_rounding.txt, nonstandard_fee_series.json}` | `d9435b8b…` / `7591cf0f…` / `558a4fa7…` | KXNFLGAME maker M=1 [V cache] |
| Registry 0860cbe2 | `…/r3_p3_fl_maker_taker/bands_registry_10c.json` | `0860cbe28d28ecc6142ddf6f1ebb67792084264ed82e0b4d868c3b3138ea5312` | refuse-bind only; never read, never rebinned |
| K1 merged modules (read-only reuse) | repo `17thgreen/GPT-6-Astra-Deathmatch` @ `09b56273eb3b11ec3968e273a28767569e368561`: `kalshi_ext_k1_q6000_legging_audit_lab_20261003/{markouts.py, fees.py, canonical.py}` | sha256 `1bc9cfbb…` / `ce3d0bc9…` / `6ea67d12…` (git blobs `eb24d47e…` / `0c8540f7…` / `66730e65…`) | local git object only (`/workspace/tmp/pr57-verify/repo`); origin containment conductor-attested, not fetched |
| card01 Amendment C ACCEPT | `…/CONDUCTOR_ACCEPT_CARD01_AMENDMENT_C_2026-10-03.json` | `2225c3fa…` | sequencing dependency only (§9) |
| RULE-FROZEN-EDIT-PREV-BYTES-001 / Examiner template v1.2 | `…/registry/RULE_FROZEN_EDIT_PREV_BYTES_2026-09-24.md` / `…/templates/EXAMINER_KALSHI_SCORECARD_TEMPLATE_v1.2.{json,md}` | `f0aab7d1…` / `56bcf626…` / `ad1dd283…` | [V] |
| **K3 packet files** | `packets/EXT_K3_INJURY_WINDOW/{DESIGN_PREDECLARATION.txt, derive_windows.py, WINDOWS.json, structural_verify.py, STRUCTURAL_VERIFY.json, MEMBERSHIP_FIXTURE.json, SOURCE_PINS.json, EMPTY_RESULTS.json}` | `ba5ec554d518ff68f1655e22f3facbd34bcddf80f9df1a481d888171caf7b2c0` / `190c43f6ce568b69934bc7652a0d12660a976db2c25f64bd3bd42a519ce2777c` / **`79756fc5a054a6e3148ba9a648ce7f15389ff91fc8f6a289aa46630e9d3263f2`** / `6dd175729d0ccd46ef2267d9442baf2d986cf630b3cf3cf6208037e6b2bcd820` / `6c5c650a26464a0317ea6bff80abdb0fa601a50ad2e8acc2b35a778685e57386` / **`ecc2b1a860646b7c248a527dc45ce8efe7559326880f40fe6d587652ae959588`** / **`cc9c2f75caacdbad68ce8e2d1b0e89e402b21326777bfbfce416bdf512d0ec29`** / `82578c97413b1fe00e8d3be29ea218a2bacb364a2c5449a334c2cc745d99e45e` | this freeze |
| **Constancy sha** | sha256 of canonical JSON `{"membership_fixture_sha256":…,"windows_json_sha256":…}` | **`bc6f692d7a5631fc56cbdcbb4d880d4710310b446d5851baef6828cc0c4ffc71`** | T03 asserts it after every full rebuild |

`SOURCE_PINS.json` lists every input above (31 governance, 15 data, 4 bundle files, 3 code refs, 20 NFL-source files, 6 K3 files) with path, sha256 and bytes.

## 3. The NFL injury-report rule (fixed FIRST, from published sources, before any market byte was read)

### 3.1 Sources (saved in `packets/EXT_K3_INJURY_WINDOW/nfl_sources/`; fetch log `SOURCES_FETCH_LOG.json` `945910fd…`; **box-only**, third-party copyright, never bundled or committed)

| id | URL | fetched (UTC) | sha256 (raw) | role |
|---|---|---|---|---|
| **S1** | https://www.nfl.com/news/2026-27-national-football-league-important-dates | 2026-10-03T22:00:37Z (also WebFetch ≈22:01Z, same text) | `5b1548c9d09d7ea8cbf77afd0dd3735e92eb33d451e3cc581e304991ba7a00c9` | **PRIMARY**: NFL's 2026-27 league calendar, entry "September 6-12" |
| S2 | https://www.chargers.com/news/national-football-league-important-dates-2026-2027 | 22:00:16Z | `44de1c5727b294ab48ebb124715265e3d87a294417218caca7d6d19422f3399a` | same calendar, club copy (1 p.m. PT = 4 p.m. ET) |
| S3 | https://www.profootballwriters.org/nfl-calendar/ | 22:00:17Z | `a49a0c8f95b7f461cab848501ccd404348633f9b1697fbdae19db2c9a4fcc244` | same calendar, PFWA copy |
| S4 | https://fliphtml5.com/uryp/sdbq/NFL_Operations_Manual_2022-2023/104/ | 22:00:21Z | `4668d786da7252f323735a5127cf1703e433098ed456c9777bef0bd5a4a8659e` | NFL Game Ops manual 2022, Appendix A (Sunday game Wed/Thu/Fri detail; league-wide release) [A host] |
| S5 | https://fliphtml5.com/uryp/sdbq/NFL_Operations_Manual_2022-2023/99/ | 22:00:22Z | `cc12056d25af3894a61d7990ce87e9c33dc4bd101ea595810ae598273227cb94` | time-zone clause [A host] |
| S6 | https://nyc3.digitaloceanspaces.com/sportsarchive-documents/prod/681949c029f45/06-07-16-2016-injury-report-policy.pdf | 22:00:22Z | `ab76f91caa46f4c805acbf5b9405a1d4b0b77fc508a4816d1d535670bf81b3ca` | 2016 policy (game-day tables; time-zone clause) — history [A] |
| S7 | https://www.nfl.com/news/competition-committee-approves-revisions-to-injury-report-0ap3000000688693 | 22:00:40Z | `c3a27089cbd7c87bc7e380861d6d5e2375bf3675812736962e9bcb1f1f0f17c6` | report categories (context) |
| S8 / S9 | https://www.nfl.com/schedules/2026/by-week/week-1 · …/week-2 | 22:00:41Z / 22:00:43Z | `d1c931c7f3f51d1f97f1c8080f26c824d476fc3c2cab1d7ba882c37b475580ba` / `39a87e6f943e7b0887417e0c7b08c8dd7924e95fabf0f6ab191a1fb5456a0570` | game weekdays cross-check. **Contain final scores; never read by any runner** (§6) |

Deterministic `.txt` extracts (by `nfl_sources/extract_text.py` `137e1ab9…`) sit beside each file; their shas are in SOURCE_PINS. operations.nfl.com policy/schedule URLs returned 404 (logged as failed fetches).

### 3.2 The rule (S1, verbatim; S2/S3 identical; S4/S6 consistent)

> "September 6-12 — In accordance with the Personnel (Injury) Report Policy, each club is required to file a Practice Report by 4:00 p.m., New York time, (or as soon as possible after the completion of practice) every Thursday, Friday, and Saturday for a regular season Monday game; Sunday, Monday, and Tuesday for a Wednesday game; Monday, Tuesday, and Wednesday for a Thursday game; Tuesday, Wednesday, and Thursday for a Friday game; Tuesday, Wednesday, and Thursday for a Saturday game; and Wednesday, Thursday, and Friday for a Sunday game. […] Each club must also file a weekly regular season Game Status Report by 4:00 p.m., New York time (or as soon as possible after the completion of practice) on Saturday for a Monday game; Tuesday for a Wednesday game; Wednesday for a Thursday game, Thursday for a Friday game, Thursday for a Saturday game, and Friday for a Sunday game."

Also from S1: "September 6 — Final day of preseason training camp for all clubs" and "September 10 - NFL International Game at Melbourne Cricket Ground (Melbourne, Australia): San Francisco 49ers vs. Los Angeles Rams". S4: "The League office will release a league-wide Practice Report to the media and clubs each Wednesday […]" and teams whose practice ends after 4:00 p.m. ET report "as soon as possible after the completion of practice". S5/S6 time-zone clause: "If a team is scheduled to play an opponent from another time zone, the team is not required to report its information until after the completion of its opponent's practice."

| Game weekday | Practice Report days | Game Status Report day |
|---|---|---|
| Sunday | Wed, Thu, Fri | Fri |
| Monday | Thu, Fri, Sat | Sat |
| Wednesday | Sun, Mon, Tue | Tue |
| Thursday | Mon, Tue, Wed | Wed |
| Friday | Tue, Wed, Thu | Thu |
| Saturday | Tue, Wed, Thu | Thu |

Every deadline is **16:00 America/New_York**. "Report day" = the latest date strictly before the game date with that weekday. The deadline is a **nominal** release time; actual postings can come earlier (club posts) or later (late practice, time-zone clause) [V source text], so the window is an approximation of the news instant [A] (tag `SCHEDULE_RULE_NOMINAL_DEADLINE_A`).

### 3.3 Game-week exceptions on the tape (B1 covers 2026-09-03T00:20Z → 2026-09-20T21:26Z)

Game days come from `markets.json` kickoffs (ET date). They agree with the nflverse `weekday` column for 31/31 and with S1/S8/S9 [V].
- **Wed 2026-09-09 opener NE@SEA** (Wednesday game): reports Sun 9/6, Mon 9/7, Tue 9/8 (GSR). **No Wed/Thu/Fri report day → no in-scope window.**
- **Thu 2026-09-10 SF–LA in Melbourne** (Thursday game, international): reports Mon 9/7, Tue 9/8, Wed 9/9 (PR+GSR). The Wed 9/9 window exists but is **excluded from the primary** (`INTL_TZ_U`, R09).
- **Mon 2026-09-14 DEN@KC** (Monday game): reports Thu 9/10, Fri 9/11, Sat 9/12 (GSR). In scope: Thu 9/10 and Fri 9/11.
- **Thu 2026-09-17 DET@BUF** (Thursday game): reports Mon 9/14, Tue 9/15, Wed 9/16 (PR+GSR). In scope: Wed 9/16 only.
- **Sunday games** (13 W1 on 9/13; 14 W2 on 9/20 incl. SNF IND@KC): Wed/Thu/Fri (Fri = PR+GSR).
- Mon 2026-09-21 NYG@LA is not in the cohort (RESERVED_HOLDOUT measurement-development event); refused.
- No Friday or Saturday games in W1–W2.
- **Correction to the Scout's "8 windows".** Two of the Scout's eight calendar days, **2026-09-03 and 2026-09-04, are not report days**: camp ends 9/6, and the first reports fall on Sun 9/6 for the Wednesday opener (S1). The Scout's counts reproduce exactly on its own calendar definition (8 days × [15:30, 16:30) ET, all tickers: **22,392 trades, 7,943 quote rows** [V]). The rule gives **6 in-scope release days**: Wed 9/9, Thu 9/10, Fri 9/11, Wed 9/16, Thu 9/17, Fri 9/18.

### 3.4 Derived windows (deterministic; `derive_windows.py` `190c43f6…` → `WINDOWS.json` `79756fc5…`)

The window unit is **(event, in-scope report day)**. Nominal release T = report day 16:00 America/New_York → UTC via `zoneinfo`. All six days are EDT, so T = 20:00Z. The primary window is **[T − 1800 s, T + 1800 s) = [19:30Z, 20:30Z) = [15:30, 16:30) EDT**, half-open. Run twice → byte-identical [V].

| Release day (ET) | Weekday | Reports | Window [start, end) UTC | Event-windows (primary) | 000 maker fills (contracts) | trades / quote rows (event tickers) |
|---|---|---|---|---|---|---|
| 2026-09-09 | WED | Sun-game PR; Thu-game PR+GSR (SF–LA, excl.) | 2026-09-09T19:30Z → 20:30Z | 14 (13) | 0 (0) | 746 / 899 |
| 2026-09-10 | THU | Sun-game PR; Mon-game PR | 2026-09-10T19:30Z → 20:30Z | 14 (14) | 0 (0) | 966 / 978 |
| 2026-09-11 | FRI | Sun-game PR+GSR; Mon-game PR | 2026-09-11T19:30Z → 20:30Z | 14 (14) | 32 (1,498.88) | 1,385 / 1,310 |
| 2026-09-16 | WED | Sun-game PR; Thu-game PR+GSR | 2026-09-16T19:30Z → 20:30Z | 15 (15) | 63 (1,649.17) | 2,131 / 1,389 |
| 2026-09-17 | THU | Sun-game PR | 2026-09-17T19:30Z → 20:30Z | 14 (14) | 18 (354.95) | 954 / 1,216 |
| 2026-09-18 | FRI | Sun-game PR+GSR | 2026-09-18T19:30Z → 20:30Z | 14 (14) | 23 (670.49) | 1,662 / 1,339 |
| **Total** | | | | **85 (84)** over 30 events (29 primary) | **136 (4,173.49)** | **7,844 / 7,131** |

Full frozen window table (primary width; per-window counts are structural; C_PRIMARY_K2 = the two selected control days, R11):

| # | window_id | wk | report day (ET) | reports | nominal release ET | window [start, end) UTC | primary | 000 maker fills (contracts) | trades / quote rows | C_PRIMARY_K2 control days (ET) | C_ALL / C_SAMEDAY / C_CLEANDAY |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `K3W-26SEP10SFLAR-20260909-WED` | 1 | 2026-09-09 WED | PR+GSR | 16:00 EDT | 09-09T19:30Z → 20:30Z | NO (INTL_TZ_U) | 45 (612.17) | 361 / 119 | 09-06 SUN, 09-05 SAT | 3 / 2 / 2 |
| 2 | `K3W-26SEP13ARILAC-20260909-WED` | 1 | 2026-09-09 WED | PR | 16:00 EDT | 09-09T19:30Z → 20:30Z | YES | 0 (0) | 45 / 82 | 09-08 TUE, 09-07 MON | 3 / 2 / 0 |
| 3 | `K3W-26SEP13ATLPIT-20260909-WED` | 1 | 2026-09-09 WED | PR | 16:00 EDT | 09-09T19:30Z → 20:30Z | YES | 0 (0) | 42 / 67 | 09-08 TUE, 09-07 MON | 4 / 2 / 0 |
| 4 | `K3W-26SEP13BALIND-20260909-WED` | 1 | 2026-09-09 WED | PR | 16:00 EDT | 09-09T19:30Z → 20:30Z | YES | 0 (0) | 35 / 48 | 09-08 TUE, 09-07 MON | 4 / 2 / 0 |
| 5 | `K3W-26SEP13BUFHOU-20260909-WED` | 1 | 2026-09-09 WED | PR | 16:00 EDT | 09-09T19:30Z → 20:30Z | YES | 0 (0) | 63 / 58 | 09-08 TUE, 09-07 MON | 4 / 2 / 0 |
| 6 | `K3W-26SEP13CHICAR-20260909-WED` | 1 | 2026-09-09 WED | PR | 16:00 EDT | 09-09T19:30Z → 20:30Z | YES | 0 (0) | 51 / 79 | 09-08 TUE, 09-07 MON | 4 / 2 / 0 |
| 7 | `K3W-26SEP13CLEJAC-20260909-WED` | 1 | 2026-09-09 WED | PR | 16:00 EDT | 09-09T19:30Z → 20:30Z | YES | 0 (0) | 38 / 101 | 09-08 TUE, 09-07 MON | 4 / 2 / 0 |
| 8 | `K3W-26SEP13DALNYG-20260909-WED` | 1 | 2026-09-09 WED | PR | 16:00 EDT | 09-09T19:30Z → 20:30Z | YES | 0 (0) | 103 / 85 | 09-08 TUE, 09-07 MON | 3 / 2 / 0 |
| 9 | `K3W-26SEP13GBMIN-20260909-WED` | 1 | 2026-09-09 WED | PR | 16:00 EDT | 09-09T19:30Z → 20:30Z | YES | 0 (0) | 80 / 72 | 09-08 TUE, 09-07 MON | 3 / 2 / 0 |
| 10 | `K3W-26SEP13MIALV-20260909-WED` | 1 | 2026-09-09 WED | PR | 16:00 EDT | 09-09T19:30Z → 20:30Z | YES | 0 (0) | 121 / 66 | 09-08 TUE, 09-07 MON | 3 / 2 / 0 |
| 11 | `K3W-26SEP13NODET-20260909-WED` | 1 | 2026-09-09 WED | PR | 16:00 EDT | 09-09T19:30Z → 20:30Z | YES | 0 (0) | 68 / 62 | 09-08 TUE, 09-07 MON | 4 / 2 / 0 |
| 12 | `K3W-26SEP13NYJTEN-20260909-WED` | 1 | 2026-09-09 WED | PR | 16:00 EDT | 09-09T19:30Z → 20:30Z | YES | 0 (0) | 24 / 66 | 09-08 TUE, 09-07 MON | 4 / 2 / 0 |
| 13 | `K3W-26SEP13TBCIN-20260909-WED` | 1 | 2026-09-09 WED | PR | 16:00 EDT | 09-09T19:30Z → 20:30Z | YES | 0 (0) | 34 / 55 | 09-08 TUE, 09-07 MON | 4 / 2 / 0 |
| 14 | `K3W-26SEP13WASPHI-20260909-WED` | 1 | 2026-09-09 WED | PR | 16:00 EDT | 09-09T19:30Z → 20:30Z | YES | 0 (0) | 42 / 58 | 09-08 TUE, 09-07 MON | 3 / 2 / 0 |
| 15 | `K3W-26SEP13ARILAC-20260910-THU` | 1 | 2026-09-10 THU | PR | 16:00 EDT | 09-10T19:30Z → 20:30Z | YES | 0 (0) | 31 / 57 | 09-08 TUE, 09-12 SAT | 3 / 2 / 0 |
| 16 | `K3W-26SEP13ATLPIT-20260910-THU` | 1 | 2026-09-10 THU | PR | 16:00 EDT | 09-10T19:30Z → 20:30Z | YES | 0 (0) | 207 / 106 | 09-08 TUE, 09-12 SAT | 4 / 2 / 0 |
| 17 | `K3W-26SEP13BALIND-20260910-THU` | 1 | 2026-09-10 THU | PR | 16:00 EDT | 09-10T19:30Z → 20:30Z | YES | 0 (0) | 42 / 59 | 09-08 TUE, 09-12 SAT | 4 / 2 / 0 |
| 18 | `K3W-26SEP13BUFHOU-20260910-THU` | 1 | 2026-09-10 THU | PR | 16:00 EDT | 09-10T19:30Z → 20:30Z | YES | 0 (0) | 152 / 103 | 09-08 TUE, 09-12 SAT | 4 / 2 / 0 |
| 19 | `K3W-26SEP13CHICAR-20260910-THU` | 1 | 2026-09-10 THU | PR | 16:00 EDT | 09-10T19:30Z → 20:30Z | YES | 0 (0) | 55 / 61 | 09-08 TUE, 09-12 SAT | 4 / 2 / 0 |
| 20 | `K3W-26SEP13CLEJAC-20260910-THU` | 1 | 2026-09-10 THU | PR | 16:00 EDT | 09-10T19:30Z → 20:30Z | YES | 0 (0) | 48 / 63 | 09-08 TUE, 09-12 SAT | 4 / 2 / 0 |
| 21 | `K3W-26SEP13DALNYG-20260910-THU` | 1 | 2026-09-10 THU | PR | 16:00 EDT | 09-10T19:30Z → 20:30Z | YES | 0 (0) | 86 / 96 | 09-08 TUE, 09-12 SAT | 3 / 2 / 0 |
| 22 | `K3W-26SEP13GBMIN-20260910-THU` | 1 | 2026-09-10 THU | PR | 16:00 EDT | 09-10T19:30Z → 20:30Z | YES | 0 (0) | 85 / 63 | 09-08 TUE, 09-12 SAT | 3 / 2 / 0 |
| 23 | `K3W-26SEP13MIALV-20260910-THU` | 1 | 2026-09-10 THU | PR | 16:00 EDT | 09-10T19:30Z → 20:30Z | YES | 0 (0) | 37 / 53 | 09-08 TUE, 09-12 SAT | 3 / 2 / 0 |
| 24 | `K3W-26SEP13NODET-20260910-THU` | 1 | 2026-09-10 THU | PR | 16:00 EDT | 09-10T19:30Z → 20:30Z | YES | 0 (0) | 72 / 76 | 09-08 TUE, 09-12 SAT | 4 / 2 / 0 |
| 25 | `K3W-26SEP13NYJTEN-20260910-THU` | 1 | 2026-09-10 THU | PR | 16:00 EDT | 09-10T19:30Z → 20:30Z | YES | 0 (0) | 30 / 45 | 09-08 TUE, 09-12 SAT | 4 / 2 / 0 |
| 26 | `K3W-26SEP13TBCIN-20260910-THU` | 1 | 2026-09-10 THU | PR | 16:00 EDT | 09-10T19:30Z → 20:30Z | YES | 0 (0) | 35 / 56 | 09-08 TUE, 09-12 SAT | 4 / 2 / 0 |
| 27 | `K3W-26SEP13WASPHI-20260910-THU` | 1 | 2026-09-10 THU | PR | 16:00 EDT | 09-10T19:30Z → 20:30Z | YES | 0 (0) | 30 / 46 | 09-08 TUE, 09-12 SAT | 3 / 2 / 0 |
| 28 | `K3W-26SEP14DENKC-20260910-THU` | 1 | 2026-09-10 THU | PR | 16:00 EDT | 09-10T19:30Z → 20:30Z | YES | 0 (0) | 56 / 94 | 09-09 WED, 09-08 TUE | 3 / 2 / 1 |
| 29 | `K3W-26SEP13ARILAC-20260911-FRI` | 1 | 2026-09-11 FRI | PR+GSR | 16:00 EDT | 09-11T19:30Z → 20:30Z | YES | 0 (0) | 52 / 85 | 09-12 SAT, 09-08 TUE | 3 / 2 / 0 |
| 30 | `K3W-26SEP13ATLPIT-20260911-FRI` | 1 | 2026-09-11 FRI | PR+GSR | 16:00 EDT | 09-11T19:30Z → 20:30Z | YES | 0 (0) | 192 / 111 | 09-12 SAT, 09-08 TUE | 4 / 2 / 0 |
| 31 | `K3W-26SEP13BALIND-20260911-FRI` | 1 | 2026-09-11 FRI | PR+GSR | 16:00 EDT | 09-11T19:30Z → 20:30Z | YES | 0 (0) | 67 / 99 | 09-12 SAT, 09-08 TUE | 4 / 2 / 0 |
| 32 | `K3W-26SEP13BUFHOU-20260911-FRI` | 1 | 2026-09-11 FRI | PR+GSR | 16:00 EDT | 09-11T19:30Z → 20:30Z | YES | 14 (770.06) | 221 / 109 | 09-12 SAT, 09-08 TUE | 4 / 2 / 0 |
| 33 | `K3W-26SEP13CHICAR-20260911-FRI` | 1 | 2026-09-11 FRI | PR+GSR | 16:00 EDT | 09-11T19:30Z → 20:30Z | YES | 0 (0) | 80 / 76 | 09-12 SAT, 09-08 TUE | 4 / 2 / 0 |
| 34 | `K3W-26SEP13CLEJAC-20260911-FRI` | 1 | 2026-09-11 FRI | PR+GSR | 16:00 EDT | 09-11T19:30Z → 20:30Z | YES | 1 (250) | 74 / 104 | 09-12 SAT, 09-08 TUE | 4 / 2 / 0 |
| 35 | `K3W-26SEP13DALNYG-20260911-FRI` | 1 | 2026-09-11 FRI | PR+GSR | 16:00 EDT | 09-11T19:30Z → 20:30Z | YES | 8 (126.98) | 143 / 107 | 09-12 SAT, 09-08 TUE | 3 / 2 / 0 |
| 36 | `K3W-26SEP13GBMIN-20260911-FRI` | 1 | 2026-09-11 FRI | PR+GSR | 16:00 EDT | 09-11T19:30Z → 20:30Z | YES | 0 (0) | 105 / 97 | 09-12 SAT, 09-08 TUE | 3 / 2 / 0 |
| 37 | `K3W-26SEP13MIALV-20260911-FRI` | 1 | 2026-09-11 FRI | PR+GSR | 16:00 EDT | 09-11T19:30Z → 20:30Z | YES | 0 (0) | 60 / 80 | 09-12 SAT, 09-08 TUE | 3 / 2 / 0 |
| 38 | `K3W-26SEP13NODET-20260911-FRI` | 1 | 2026-09-11 FRI | PR+GSR | 16:00 EDT | 09-11T19:30Z → 20:30Z | YES | 8 (101.84) | 110 / 90 | 09-12 SAT, 09-08 TUE | 4 / 2 / 0 |
| 39 | `K3W-26SEP13NYJTEN-20260911-FRI` | 1 | 2026-09-11 FRI | PR+GSR | 16:00 EDT | 09-11T19:30Z → 20:30Z | YES | 0 (0) | 44 / 72 | 09-12 SAT, 09-08 TUE | 4 / 2 / 0 |
| 40 | `K3W-26SEP13TBCIN-20260911-FRI` | 1 | 2026-09-11 FRI | PR+GSR | 16:00 EDT | 09-11T19:30Z → 20:30Z | YES | 1 (250) | 75 / 93 | 09-12 SAT, 09-08 TUE | 4 / 2 / 0 |
| 41 | `K3W-26SEP13WASPHI-20260911-FRI` | 1 | 2026-09-11 FRI | PR+GSR | 16:00 EDT | 09-11T19:30Z → 20:30Z | YES | 0 (0) | 60 / 80 | 09-12 SAT, 09-08 TUE | 3 / 2 / 0 |
| 42 | `K3W-26SEP14DENKC-20260911-FRI` | 1 | 2026-09-11 FRI | PR | 16:00 EDT | 09-11T19:30Z → 20:30Z | YES | 0 (0) | 102 / 107 | 09-09 WED, 09-13 SUN | 3 / 2 / 1 |
| 43 | `K3W-26SEP17DETBUF-20260916-WED` | 2 | 2026-09-16 WED | PR+GSR | 16:00 EDT | 09-16T19:30Z → 20:30Z | YES | 59 (997.59) | 740 / 120 | 09-13 SUN, 09-12 SAT | 3 / 2 / 1 |
| 44 | `K3W-26SEP20CARATL-20260916-WED` | 2 | 2026-09-16 WED | PR | 16:00 EDT | 09-16T19:30Z → 20:30Z | YES | 2 (500) | 267 / 99 | 09-15 TUE, 09-14 MON | 4 / 2 / 1 |
| 45 | `K3W-26SEP20CINHOU-20260916-WED` | 2 | 2026-09-16 WED | PR | 16:00 EDT | 09-16T19:30Z → 20:30Z | YES | 0 (0) | 74 / 96 | 09-15 TUE, 09-14 MON | 4 / 2 / 1 |
| 46 | `K3W-26SEP20CLETB-20260916-WED` | 2 | 2026-09-16 WED | PR | 16:00 EDT | 09-16T19:30Z → 20:30Z | YES | 0 (0) | 96 / 91 | 09-15 TUE, 09-14 MON | 4 / 2 / 1 |
| 47 | `K3W-26SEP20GBNYJ-20260916-WED` | 2 | 2026-09-16 WED | PR | 16:00 EDT | 09-16T19:30Z → 20:30Z | YES | 0 (0) | 86 / 107 | 09-15 TUE, 09-14 MON | 4 / 2 / 1 |
| 48 | `K3W-26SEP20INDKC-20260916-WED` | 2 | 2026-09-16 WED | PR | 16:00 EDT | 09-16T19:30Z → 20:30Z | YES | 0 (0) | 52 / 83 | 09-15 TUE, 09-14 MON | 3 / 2 / 0 |
| 49 | `K3W-26SEP20JACDEN-20260916-WED` | 2 | 2026-09-16 WED | PR | 16:00 EDT | 09-16T19:30Z → 20:30Z | YES | 0 (0) | 64 / 91 | 09-15 TUE, 09-14 MON | 3 / 2 / 0 |
| 50 | `K3W-26SEP20LVLAC-20260916-WED` | 2 | 2026-09-16 WED | PR | 16:00 EDT | 09-16T19:30Z → 20:30Z | YES | 0 (0) | 71 / 104 | 09-15 TUE, 09-14 MON | 3 / 2 / 0 |
| 51 | `K3W-26SEP20MIASF-20260916-WED` | 2 | 2026-09-16 WED | PR | 16:00 EDT | 09-16T19:30Z → 20:30Z | YES | 2 (151.58) | 188 / 103 | 09-15 TUE, 09-14 MON | 3 / 2 / 0 |
| 52 | `K3W-26SEP20MINCHI-20260916-WED` | 2 | 2026-09-16 WED | PR | 16:00 EDT | 09-16T19:30Z → 20:30Z | YES | 0 (0) | 94 / 87 | 09-15 TUE, 09-14 MON | 4 / 2 / 1 |
| 53 | `K3W-26SEP20NOBAL-20260916-WED` | 2 | 2026-09-16 WED | PR | 16:00 EDT | 09-16T19:30Z → 20:30Z | YES | 0 (0) | 66 / 82 | 09-15 TUE, 09-14 MON | 4 / 2 / 1 |
| 54 | `K3W-26SEP20PHITEN-20260916-WED` | 2 | 2026-09-16 WED | PR | 16:00 EDT | 09-16T19:30Z → 20:30Z | YES | 0 (0) | 160 / 85 | 09-15 TUE, 09-14 MON | 4 / 2 / 1 |
| 55 | `K3W-26SEP20PITNE-20260916-WED` | 2 | 2026-09-16 WED | PR | 16:00 EDT | 09-16T19:30Z → 20:30Z | YES | 0 (0) | 82 / 87 | 09-15 TUE, 09-14 MON | 4 / 2 / 1 |
| 56 | `K3W-26SEP20SEAARI-20260916-WED` | 2 | 2026-09-16 WED | PR | 16:00 EDT | 09-16T19:30Z → 20:30Z | YES | 0 (0) | 46 / 83 | 09-15 TUE, 09-14 MON | 3 / 2 / 0 |
| 57 | `K3W-26SEP20WASDAL-20260916-WED` | 2 | 2026-09-16 WED | PR | 16:00 EDT | 09-16T19:30Z → 20:30Z | YES | 0 (0) | 45 / 71 | 09-15 TUE, 09-14 MON | 3 / 2 / 0 |
| 58 | `K3W-26SEP20CARATL-20260917-THU` | 2 | 2026-09-17 THU | PR | 16:00 EDT | 09-17T19:30Z → 20:30Z | YES | 0 (0) | 77 / 86 | 09-15 TUE, 09-19 SAT | 4 / 2 / 1 |
| 59 | `K3W-26SEP20CINHOU-20260917-THU` | 2 | 2026-09-17 THU | PR | 16:00 EDT | 09-17T19:30Z → 20:30Z | YES | 12 (104.95) | 74 / 92 | 09-15 TUE, 09-19 SAT | 4 / 2 / 1 |
| 60 | `K3W-26SEP20CLETB-20260917-THU` | 2 | 2026-09-17 THU | PR | 16:00 EDT | 09-17T19:30Z → 20:30Z | YES | 0 (0) | 40 / 92 | 09-15 TUE, 09-19 SAT | 4 / 2 / 1 |
| 61 | `K3W-26SEP20GBNYJ-20260917-THU` | 2 | 2026-09-17 THU | PR | 16:00 EDT | 09-17T19:30Z → 20:30Z | YES | 6 (250) | 61 / 94 | 09-15 TUE, 09-19 SAT | 4 / 2 / 1 |
| 62 | `K3W-26SEP20INDKC-20260917-THU` | 2 | 2026-09-17 THU | PR | 16:00 EDT | 09-17T19:30Z → 20:30Z | YES | 0 (0) | 40 / 99 | 09-15 TUE, 09-19 SAT | 3 / 2 / 0 |
| 63 | `K3W-26SEP20JACDEN-20260917-THU` | 2 | 2026-09-17 THU | PR | 16:00 EDT | 09-17T19:30Z → 20:30Z | YES | 0 (0) | 48 / 70 | 09-15 TUE, 09-19 SAT | 3 / 2 / 0 |
| 64 | `K3W-26SEP20LVLAC-20260917-THU` | 2 | 2026-09-17 THU | PR | 16:00 EDT | 09-17T19:30Z → 20:30Z | YES | 0 (0) | 79 / 94 | 09-15 TUE, 09-19 SAT | 3 / 2 / 0 |
| 65 | `K3W-26SEP20MIASF-20260917-THU` | 2 | 2026-09-17 THU | PR | 16:00 EDT | 09-17T19:30Z → 20:30Z | YES | 0 (0) | 68 / 90 | 09-15 TUE, 09-19 SAT | 3 / 2 / 0 |
| 66 | `K3W-26SEP20MINCHI-20260917-THU` | 2 | 2026-09-17 THU | PR | 16:00 EDT | 09-17T19:30Z → 20:30Z | YES | 0 (0) | 96 / 80 | 09-15 TUE, 09-19 SAT | 4 / 2 / 1 |
| 67 | `K3W-26SEP20NOBAL-20260917-THU` | 2 | 2026-09-17 THU | PR | 16:00 EDT | 09-17T19:30Z → 20:30Z | YES | 0 (0) | 49 / 90 | 09-15 TUE, 09-19 SAT | 4 / 2 / 1 |
| 68 | `K3W-26SEP20PHITEN-20260917-THU` | 2 | 2026-09-17 THU | PR | 16:00 EDT | 09-17T19:30Z → 20:30Z | YES | 0 (0) | 154 / 73 | 09-15 TUE, 09-19 SAT | 4 / 2 / 1 |
| 69 | `K3W-26SEP20PITNE-20260917-THU` | 2 | 2026-09-17 THU | PR | 16:00 EDT | 09-17T19:30Z → 20:30Z | YES | 0 (0) | 76 / 103 | 09-15 TUE, 09-19 SAT | 4 / 2 / 1 |
| 70 | `K3W-26SEP20SEAARI-20260917-THU` | 2 | 2026-09-17 THU | PR | 16:00 EDT | 09-17T19:30Z → 20:30Z | YES | 0 (0) | 48 / 102 | 09-15 TUE, 09-19 SAT | 3 / 2 / 0 |
| 71 | `K3W-26SEP20WASDAL-20260917-THU` | 2 | 2026-09-17 THU | PR | 16:00 EDT | 09-17T19:30Z → 20:30Z | YES | 0 (0) | 44 / 51 | 09-15 TUE, 09-19 SAT | 3 / 2 / 0 |
| 72 | `K3W-26SEP20CARATL-20260918-FRI` | 2 | 2026-09-18 FRI | PR+GSR | 16:00 EDT | 09-18T19:30Z → 20:30Z | YES | 0 (0) | 101 / 87 | 09-19 SAT, 09-15 TUE | 4 / 2 / 1 |
| 73 | `K3W-26SEP20CINHOU-20260918-FRI` | 2 | 2026-09-18 FRI | PR+GSR | 16:00 EDT | 09-18T19:30Z → 20:30Z | YES | 2 (250.92) | 120 / 102 | 09-19 SAT, 09-15 TUE | 4 / 2 / 1 |
| 74 | `K3W-26SEP20CLETB-20260918-FRI` | 2 | 2026-09-18 FRI | PR+GSR | 16:00 EDT | 09-18T19:30Z → 20:30Z | YES | 0 (0) | 59 / 102 | 09-19 SAT, 09-15 TUE | 4 / 2 / 1 |
| 75 | `K3W-26SEP20GBNYJ-20260918-FRI` | 2 | 2026-09-18 FRI | PR+GSR | 16:00 EDT | 09-18T19:30Z → 20:30Z | YES | 0 (0) | 95 / 101 | 09-19 SAT, 09-15 TUE | 4 / 2 / 1 |
| 76 | `K3W-26SEP20INDKC-20260918-FRI` | 2 | 2026-09-18 FRI | PR+GSR | 16:00 EDT | 09-18T19:30Z → 20:30Z | YES | 0 (0) | 47 / 85 | 09-19 SAT, 09-15 TUE | 3 / 2 / 0 |
| 77 | `K3W-26SEP20JACDEN-20260918-FRI` | 2 | 2026-09-18 FRI | PR+GSR | 16:00 EDT | 09-18T19:30Z → 20:30Z | YES | 0 (0) | 97 / 105 | 09-19 SAT, 09-15 TUE | 3 / 2 / 0 |
| 78 | `K3W-26SEP20LVLAC-20260918-FRI` | 2 | 2026-09-18 FRI | PR+GSR | 16:00 EDT | 09-18T19:30Z → 20:30Z | YES | 4 (41.44) | 210 / 109 | 09-19 SAT, 09-15 TUE | 3 / 2 / 0 |
| 79 | `K3W-26SEP20MIASF-20260918-FRI` | 2 | 2026-09-18 FRI | PR+GSR | 16:00 EDT | 09-18T19:30Z → 20:30Z | YES | 0 (0) | 80 / 78 | 09-19 SAT, 09-15 TUE | 3 / 2 / 0 |
| 80 | `K3W-26SEP20MINCHI-20260918-FRI` | 2 | 2026-09-18 FRI | PR+GSR | 16:00 EDT | 09-18T19:30Z → 20:30Z | YES | 0 (0) | 125 / 95 | 09-19 SAT, 09-15 TUE | 4 / 2 / 1 |
| 81 | `K3W-26SEP20NOBAL-20260918-FRI` | 2 | 2026-09-18 FRI | PR+GSR | 16:00 EDT | 09-18T19:30Z → 20:30Z | YES | 0 (0) | 104 / 97 | 09-19 SAT, 09-15 TUE | 4 / 2 / 1 |
| 82 | `K3W-26SEP20PHITEN-20260918-FRI` | 2 | 2026-09-18 FRI | PR+GSR | 16:00 EDT | 09-18T19:30Z → 20:30Z | YES | 17 (378.13) | 333 / 103 | 09-19 SAT, 09-15 TUE | 4 / 2 / 1 |
| 83 | `K3W-26SEP20PITNE-20260918-FRI` | 2 | 2026-09-18 FRI | PR+GSR | 16:00 EDT | 09-18T19:30Z → 20:30Z | YES | 0 (0) | 146 / 104 | 09-19 SAT, 09-15 TUE | 4 / 2 / 1 |
| 84 | `K3W-26SEP20SEAARI-20260918-FRI` | 2 | 2026-09-18 FRI | PR+GSR | 16:00 EDT | 09-18T19:30Z → 20:30Z | YES | 0 (0) | 64 / 80 | 09-19 SAT, 09-15 TUE | 3 / 2 / 0 |
| 85 | `K3W-26SEP20WASDAL-20260918-FRI` | 2 | 2026-09-18 FRI | PR+GSR | 16:00 EDT | 09-18T19:30Z → 20:30Z | YES | 0 (0) | 81 / 91 | 09-19 SAT, 09-15 TUE | 3 / 2 / 0 |

## 4. Structural facts (label-free; counts only; `structural_verify.py` `6dd17572…` → `STRUCTURAL_VERIFY.json` `6c5c650a…`, python 3.13.5 / Linux-6.12.94+-x86_64-with-glibc2.41)

| Fact | Value | Tag |
|---|---|---|
| Fills / maker / taker; trades / quotes; tickers / events | 12,853 / 12,837 / 16; 681,732 / 364,988; 62 / 31 (= K1 R36) | [V] |
| Tape rows / fills in ADMIT-1 | 0 / 0 | [V] |
| Primary in-window 000 maker fills | **136 fills, 4,173.49 contracts**, in **13 of 84** event-windows, from **12 of 29** events; taker fills in windows 0 | [V] |
| Biggest single-window share | `K3W-26SEP17DETBUF-20260916-WED`: 59 fills (997.59 contracts) = 43% of in-window fills, 24% of contracts | [V] |
| Primary controls (C_PRIMARY_K2, deduplicated) | **86 control windows; 160 fills, 4,252.57 contracts; 13 events** with control fills (by day: 9/12 39, 9/13 53, 9/15 2, 9/19 66 fills) | [V] |
| Events with both in-window and control fills | **7** (BUFHOU, CLEJAC, DALNYG, CINHOU, GBNYJ, MIASF, PHITEN); union 18 | [V] |
| Control availability per in-scope window | C_ALL 3–4 days (48 windows have 4, 37 have 3); C_SAMEDAY 2 for all 85; C_CLEANDAY 0 for 57, 1 for 27, 2 for 1 | [V] |
| Sensitivity W900 | in 47 fills / 2,629.88 (9 events); controls 48 / 1,850.43 | [V] |
| Sensitivity W3600 | in 254 / 6,982.61 (15 events); controls 358 / 7,450.75 | [V] |
| Sensitivity LATE [T, T+3600) | in 127 / 3,947.08 (12 events); controls 190 / 3,686.61 | [V] |
| Control sensitivities (primary width) | C_ALL 103 windows, 160 / 4,252.57 (13 events); C_SAMEDAY 168 windows, 307 / 6,019.54 (16 events); C_CLEANDAY 10 windows, 53 / 766.83 (**1 event**) | [V] |
| Excluded SF–LA Melbourne window (S_INTL) | 45 fills, 612.17 contracts | [V] |
| Whole-ledger headline fee (K1 R24, Decimal(str)) | **$1,286.22** over 1,846 maker orders = K1 merged figure; `Decimal(float)` path gives **$1,286.59** (the K2 N4 bug) | [V]; `CACHE_NOT_R1P1` |
| Scout reproduction (8 calendar days × [15:30,16:30) ET, all tickers) | 22,392 trades / 7,943 quote rows = Scout | [V] |

Membership fixture `MEMBERSHIP_FIXTURE.json` (`ecc2b1a8…`) maps every in-window and control fill row index (0-based, ledger file order) to its window id. It uses only fill `at`, `event` and `kind`.

## 5. Rules (every degree of freedom pinned; UNPINNED = ambiguity resolved conservatively before implementation)

Conservative criterion (K1 §5 / K2 §5, extended): (i) only pinned bytes; (ii) never invent a value or impute a null; (iii) never choose by looking at markouts, mids, price moves or any outcome; (iv) take the less favorable / less dramatic reading of any claim about 000's toxicity exposure; (v) add no number without a stated label-free rationale; (vi) **for K3: timing comes from the published NFL rule only, fixed before any market byte, and is never tuned to the tape.**

### 5.A Universe, timing and windows
| # | Rule | Source / resolution | Tag |
|---|---|---|---|
| R01 | **Universe** = K1 R01 (31 cohort events, 62 tickers). **Primary estimand events** = the 29 events with ≥1 on-tape in-scope window and no `INTL_TZ_U` flag, listed in `WINDOWS.json`. Excluded: `26SEP09NESEA` (Wednesday game, no Wed/Thu/Fri report day) and `26SEP10SFLAR` (R09). Anything else → `ClosedUniverseRefused`. | commission + R04 | [V] |
| R02 | **Closed input manifest.** The runner reads only files in `SOURCE_PINS.json` (via the K1 bundle `0f8f5297` and the K3 bundle). It checks each sha256 before reading and fails closed. | K1 R02 | [V] |
| R03 | **000 is read, never re-run or retuned** (K1 R03 in full). | ruling | [V] |
| R04 | **Release rule** = §3.2 table (S1), encoded as constants in `derive_windows.py`. The runner never fetches the NFL sources; it re-derives windows from the constants and asserts `WINDOWS.json` byte-equality (R36). | commission ("published schedule") | [V] |
| R05 | **Game day** = America/New_York calendar date of `markets.json` kickoff. **Report day** = the latest date strictly before the game date with the rule's weekday. **UNPINNED** (the source of game days). Resolution: use the pinned kickoff epoch, cross-checked against the nflverse `weekday` (31/31) and S8/S9 (box-only). No other schedule input. | UNPINNED → resolved | [V] |
| R06 | **Nominal release instant** T = report day 16:00 `America/New_York`, converted with `zoneinfo` (DST-aware). All tape dates are EDT, so T = 20:00Z; the DST fixtures are in T01. **UNPINNED** (the actual posting time is unrecorded on the box). Resolution: use the published deadline as the nominal news instant, tagged `SCHEDULE_RULE_NOMINAL_DEADLINE_A`. No posting timestamp is inferred from the tape (that would be outcome-driven timing). | UNPINNED → resolved | [A] |
| R07 | **In-scope report days** = those whose ET weekday ∈ {WED, THU, FRI} (Conductor scope), for any game. Report days on SUN/MON/TUE/SAT (`OFFSCOPE_REPORT`: 9/6, 9/7, 9/8, 9/12, 9/14, 9/15 for cohort games) are never measured and **can never serve as a control day for that event**. **UNPINNED** (for non-Sunday games the rule puts reports on other weekdays). Resolution: the scope is the weekday set, so DEN@KC contributes Thu/Fri and DET@BUF contributes Wed; off-scope report days are only excluded. | UNPINNED → resolved | [V] |
| R08 | **PRIMARY half-width w = 1800 s**: window [T − 1800, T + 1800), half-open. **A priori justification** (pinned in `DESIGN_PREDECLARATION.txt` 18:01:56 ET, before any window or count existed): (a) the deadline is "no later than 4:00 p.m. … or as soon as possible after the completion of practice", and the time-zone clause can delay a club's posting, so the news instant is spread on both sides of 16:00 [V source]; ±15 min would miss early club posts and late West-Coast filers; (b) B1 quotes are one-minute rows [V], so ±15 min gives at most 30 quote rows per ticker per window; (c) it equals the Scout's pre-registered 15:30–16:30 ET definition, so it is not a new degree of freedom. **Sensitivities (declared then, reported, never selected):** W900 [T−900, T+900), W3600 [T−3600, T+3600), LATE [T, T+3600) (post-deadline only). | commission + UNPINNED → resolved | [A] |
| R09 | **International / time-zone flag.** `KXNFLGAME-26SEP10SFLAR` (Melbourne, UTC+10): under the time-zone clause and Melbourne practice times, the ET release clock of its Wed 9/9 report is [U]. It is **excluded from the primary** (its window and its controls). Sensitivity **S_INTL** adds it back. Domestic cross-time-zone games stay in the primary: their delay is covered by w and by LATE. **UNPINNED.** Resolution: exclude, because the window cannot be pinned. | UNPINNED → resolved | [U] |
| R10 | **Window / control eligibility.** Both event tickers have B1 rows (any kind) at or before the window start and at or after its end (per-ticker coverage, `WINDOWS.json events.*.tape_coverage_utc`). The window end ≤ K − 10800 s (000's replay ends at K−3h). No overlap with ADMIT-1. Primary result: 85/85 in-scope windows on tape [V]. **UNPINNED** (coverage definition). Resolution as stated; it uses only timestamps. | UNPINNED → resolved | [V] |

### 5.B Controls and fill membership
| # | Rule | Source / resolution | Tag |
|---|---|---|---|
| R11 | **PRIMARY controls `C_PRIMARY_K2`.** For in-scope window (e, D): the candidate days D′ are the same event and the same ET clock window [16:00 − w, 16:00 + w) on days with D′ ≠ D, **not any report day of e** (in-scope or off-scope), **not e's game day**, |D′ − D| ≤ 21, and eligible per R10. Rank by \|D′ − D\| ascending; ties go to the **earlier** D′; take **k = 2**. The per-event control set is the **de-duplicated union** over that event's windows. The selection uses only the calendar and coverage; it reads no fill, price or quote value. Resulting days: W1 Sunday games {Mon 9/7, Tue 9/8, Sat 9/12}; W2 Sunday games {Mon 9/14, Tue 9/15, Sat 9/19}; DEN@KC {Tue 9/8, Wed 9/9, Sun 9/13}; DET@BUF {Sat 9/12, Sun 9/13} [V]. Matching = same game and tickers, same clock time, nearest time-to-kickoff. **UNPINNED** (control definition, k, ties, game-day exclusion). Resolution: nearest-day same-clock gives the best time-to-kickoff match without reusing the event's news days. Game day is excluded because pregame-day flow is a different regime. k = 2 balances the windows before and after. | UNPINNED → resolved | [A] |
| R12 | **Control sensitivities** (reported, never selected): **C_ALL** (all eligible candidate days); **C_SAMEDAY** (the same report day, clock windows centred T − 3h and T + 3h, i.e. 13:00 / 19:00 ET, no overlap with any report window; time-to-kickoff matched within hours, different intraday clock); **C_CLEANDAY** (candidate days with no 16:00 ET report for **any** W1–W2 game under the rule; on the tape that means 9/3, 9/4, 9/5 and 9/13; only 10 windows and 1 event with fills → expected to be undefined/low-n, R25b). | UNPINNED → resolved | [V] |
| R13 | **Membership.** A fill f of event e is **IN** iff `kind == maker` and f.at ∈ a primary window of e; it is **CTRL** iff f.at ∈ a selected control window of e. Assignment uses `fills.event` and `fills.at` only. A fill in both raises `MembershipConflict` (impossible by construction; asserted). Fills outside both sets are unused. Expected: IN 136 / 4,173.49 contracts; CTRL 160 / 4,252.57; byte-identical to `MEMBERSHIP_FIXTURE.json` `ecc2b1a8…` (T02). | — | [V] |
| R14 | **Fill universe** = B2 maker fills; unit = fill row; weight = `size` (contracts). This covers every resting fill, both opening and pairing legs, because both are exposed to news-takers. The 16 taker flatten fills are excluded (0 in any window [V]). **UNPINNED** (all fills vs K1 opening portions). Resolution: all maker fills. Per-fill toxicity is the thesis, and the K1 open-leg split is a different question. | UNPINNED → resolved | [V] |

### 5.C Metrics
| # | Rule | Source / resolution | Tag |
|---|---|---|---|
| R15 | **Mid** = K1 R19 verbatim: B1 quote rows of the fill's own ticker; mid(t) = (bid + ask)/2 of the latest quote row with `at ≤ t`. Valid iff 0 < bid < ask < 1 and 0 ≤ t − asof < 300. mid_out = mid if fill `outcome` = yes, else 1 − mid. No print-derived mid; **Lee-Ready refused**. Implementations should import K1's merged `QuoteBook` / `outcome_mid` (`markouts.py` `1bc9cfbb…`) read-only, or re-implement them and pass K1 T08 vectors. | K1 R19 | [V] |
| R16 | **Markout** MO_h(f) = mid_out(t_f + h) − price_f, in $/contract, **signed from 000's side** (+ = moved in favor of 000's fill). **Adverse selection** AS_h(f) = −MO_h(f) (+ = against 000). Contract-weighted mean over a set; the unweighted median, n, censored n and censored contracts are also reported. | K1 R20 | [V] |
| R17 | **Horizons** H = {60, 300, 900, 1800} s. **PRIMARY H\* = 300 s.** A priori: (a) scheduled-news repricing on a 1-minute quote grid should show within minutes, while 60 s is a single quote-row step (noisy); (b) 300 s is the Scout's first pre-registered point (+5 min); (c) H\* < w, so the post-fill horizon of most in-window fills stays inside or near the news window; (d) 1800 s (K1 H\*) is kept for comparability, as a sensitivity. **UNPINNED** (grid, primary). | UNPINNED → resolved | [A] |
| R18 | **Secondary** MO^mid_h = mid_out(t_f + h) − `outcome_mid_at_fill` (K2 R18 secondary; strips spread capture, isolating the price move). Descriptive only. | UNPINNED → resolved | [I] |
| R19 | **Nulls / censoring** = K1 R21: an invalid mid at t + h gives a null MO (censored); no forward fill past validity, no interpolation, no substitute. A horizon may run past the window end; past the ticker's last tape row it is null. | K1 R21 | [A] |
| R20 | **Fees.** HEADLINE = K1 R24: per maker order o, F_o = ceil_to_$0.01(Σ_{f∈o} ceil_6dp(0.0175·1·C_f·p_f·(1−p_f))), allocated pro rata by contracts over **all** of o's fills (orders that span window edges are allocated the same way). **All arithmetic in `decimal.Decimal` built from `str()` of the JSON number.** `Decimal(float)` is forbidden: the converter raises `FloatDecimalRefused`. T05 locks the whole-ledger total at **$1,286.22** (1,846 orders) and shows that the float path ($1,286.59) is rejected. Net MO = MO − f_c. SENSITIVITY: direct-member $0.0001 (ledger `fee`/`size`), never the headline. Labels `CACHE_NOT_R1P1`, `NON_DIRECT_CENT_HEADLINE`; `examiner_pin_account_class: null`. | ruling `fee_rounding` + K2 N4 | [V cache] |

### 5.D Estimand, inference, verdict
| # | Rule | Source / resolution | Tag |
|---|---|---|---|
| R21 | **Per-set aggregates** for IN and CTRL (primary and every sensitivity) at every h, gross and net: contract-weighted mean MO and AS, median, n fills, contracts, censored; per window and per game (descriptive). Also fill intensity (contracts per window-hour). No PnL, ROI, "edge", "would have earned" or Sharpe. | — | — |
| R22 | **Primary estimand** Δ\* = MO_{300}(IN) − MO_{300}(CTRL), contract-weighted, **gross**, primary width and primary controls; net beside it. ΔAS\* = −Δ\* (Δ\* < 0 means in-window fills mark out worse, i.e. more toxic). | commission | — |
| R23 | **Bootstrap (vectorized, game-clustered).** Cluster = event. The population is the **29 primary events** (fixed by `WINDOWS.json`, including events with zero in-window or control fills). Sorted by event ticker. `rng = random.Random(20261003)`; for b in 1..10,000: `idx = rng.choices(range(29), k=29)`. **Per-event sufficient statistics** (Σw·MO and Σw for IN and for CTRL, gross and net, built once with `math.fsum`) give Δ_b = ΣIN_num/ΣIN_den − ΣCTRL_num/ΣCTRL_den. A resample with a zero denominator is undefined: it is dropped and counted. The 95% CI is the type-7 (linear) percentile of the kept Δ_b at 0.025 / 0.975. **Equivalence (T06):** the naive row-level resampler (flatten the drawn events' fill rows and recompute) must give the same Δ_b sequence within 1e-12 for B = 200 on the real membership and on a 3-game fixture. The full run must finish in ≤ 120 s on the box (K2 B5: a naive row bootstrap was estimated at ≈5.5 days). **UNPINNED** (cluster unit and population). Resolution: event, because game-week has only 2 levels (degenerate), and a fixed design population avoids selecting clusters on fill availability. | UNPINNED → resolved | [A] |
| R24 | **n_eff (reported with every estimate):** events contributing ≥1 valid IN fill at H\*; events contributing valid CTRL fills; events with both; windows and release days with valid IN fills; kept/dropped resamples. Structural expectation: 12 / 13 / 7 events; 13 windows; 4 release days. With only 6 release days (4 with fills), **the verdict is capped at ITERATE** (R25). | commission | [V] |
| R25 | **Verdict (Examiner-owned; proposal).** **(a) INCONCLUSIVE** if any of: R35 structural gate fails; R36 fixture gate fails (WINDOWS / MEMBERSHIP / constancy sha); **N6:** Δ\* undefined (zero valid IN or zero valid CTRL contracts at H\*) or CI undefined (fewer than 2 kept resamples or any None); dropped resamples > 5% of B; censored at H\* > 20% of IN contracts or of CTRL contracts; fewer than 5 events with valid IN fills or fewer than 5 with valid CTRL fills at H\*. **(b)** Otherwise **ITERATE** if the 95% CI of gross Δ\* excludes 0, either sign: a window effect is visible on the dev cohort and warrants a separate counterfactual stand-down freeze. **(c)** Otherwise (CI includes 0) **DESCRIPTIVE**. **Cap: ITERATE.** KEEP, KILL of 000, retune and promotion are impossible. Each sensitivity cell gets a **cell label** under the same (a)–(c) logic (`CELL_UNDEFINED` / `CELL_CI_EXCLUDES_0` / `CELL_CI_INCLUDES_0`); cell labels are descriptive and never move the verdict. **UNPINNED** (thresholds 5% / 20% / 5 events). Resolution: stated now, label-free, mirroring K1 R32 / K2 R23. | commission + N6 | [A] |
| R26 | **Multiplicity.** Only gross Δ\* (R22) can move the verdict (family_size = 1). Every other horizon, width, control design, MO^mid, net figure, per-window, per-game and S_INTL figure is descriptive and labelled as such. | — | — |
| R27 | **Extra descriptives, declared after the structural counts were seen (disclosed; never verdict-moving):** (1) leave-one-event-out Δ\* (29 values; motivated by DET@BUF holding 43% of IN fills); (2) the max single-event share of IN contracts; (3) a **within-event paired** contrast, the mean over events with both IN and CTRL fills of (MO_IN,e − MO_CTRL,e), unweighted and contract-weighted; (4) a **release-day-cluster** bootstrap (6 days; B = 10,000; seed 20261003) flagged `LOW_CLUSTER_COUNT`. **UNPINNED** (whether to add these). Resolution: add them as descriptives only; adding them cannot change the verdict. | UNPINNED → resolved | [I] |
| R28 | **Static attribution only.** The contrast says how recorded replay fills in news windows mark out versus matched controls. It does not say what a 000 that stood down would have earned (that would change queue position, pairing and later fills). Any stand-down or widen arm is a **new Variants freeze + Conductor ACCEPT** (a 000 variant, never a retune). | K1 R30 analog | [I] |

### 5.E Integrity, exclusions, house rules
| # | Rule | Source / resolution | Tag |
|---|---|---|---|
| R29 | **Provenance on every output (N5 pre-empted).** Every JSON output, **including `INVARIANCE.json`**, is built by one `common_header()` with: `python_version`, `platform`, `experiment_id`, `freeze_md_sha256`, `windows_json_sha256`, `membership_fixture_sha256`, `constancy_sha256`, input shas, and tags `DEV_GRADE_REUSED_31_GAME_COHORT`, `HYPOTHETICAL_REPLAY_FILLS`, `IN_SAMPLE_DEV`, `SCHEDULE_RULE_NOMINAL_DEADLINE_A`. Fee fields also carry `CACHE_NOT_R1P1`. T12 asserts this on every file. | Examiner N5 | — |
| R30 | **Exclusions (code-enforced).** (a) ADMIT-1 `[2026-09-27T00:00:00Z, 2026-09-30T04:00:00Z)` half-open → `Admit1WindowRejected` (expected 0 rows [V]). (b) `HoldoutRefused` for: RESERVED_HOLDOUT `holdout_games`; `measurement_development_events` (`KXNFLGAME-26SEP21NYGLAR`, `KXNFLGAME-26SEP24ATLGB`); any `KXMLBSPREAD` ticker. (c) `capture.sqlite` and weather `archive.sqlite` paths are refused. No `sqlite3`, `urllib`, `requests`, `http`, `socket` or `subprocess` import (AST test). | K1 R34 / K2 R07 | [V] |
| R31 | **Refuse binds.** Lee-Ready refused; no tick rule or print-derived mid. Registry `0860cbe2` is never read or rebinned, and no price-band split exists in K3. No `admit.py`. No Kalshi GET or any network GET by the runner. **No Becker byte** (path `becker` or `*.parquet` → `BeckerRefused`). No holdout. No ADMIT-1. No new nflverse pull. No NFL source re-fetch. | commission | [V] |
| R32 | **Inactives (T−90 min) half = OUT OF SCOPE / HOLD.** Every ticker's last B1 row is at K−174 min [V], so the 90-minute inactive release is not on the tape. It waits on Logan egress and a fresh ruling, and must never come from the ADMIT-1 holdout. | ruling | [V] |
| R33 | **Third-party data and vendoring.** NFL source copies (`nfl_sources/*.html, *.pdf, *.txt`) are **box-only**: never committed, bundled, gisted or uploaded; the repo cites URL + sha only. No Becker data anywhere. **The freeze md/json are pinned by sha and never vendored into the repo** (K2 PR67 ruling); the cloud receives them out-of-band and records their shas in `FROZEN_EXPERIMENT.json`. | commission + PR67 ruling | — |
| R34 | **Precision / canonical JSON** = K1 R37: $/contract 6 dp, shares 6 dp; `sort_keys`, `separators=(',',':')`, UTF-8; times stored as UTC epoch plus ISO `Z` and an ET rendering. | K1 R37 | — |
| R35 | **Pre-run structural gate** (before any mid is read): 12,853 / 12,837 / 16 fills; 681,732 / 364,988 rows; 62 tickers; 31 events; ADMIT-1 rows 0; Scout reproduction 22,392 / 7,943. Any failure → stop, INCONCLUSIVE, no markout output. | — | [V] |
| R36 | **Window/membership fixture gate** (before any mid is read): re-derived `WINDOWS.json` sha == `79756fc5…`, membership sha == `ecc2b1a8…`, constancy == `bc6f692d…`. Any mismatch → stop, INCONCLUSIVE. | — | [V] |
| R37 | **Label hygiene.** The implementer may not open any markout aggregate until T01–T05 and T09–T11 are green and the R35/R36 gates have passed in the run log. Then results are written once, with no re-run after seeing them except for a documented bug fix that carries a new commit sha and a note. | K2 R50 analog | — |

**UNPINNED rules (18), each resolved above:** R05 (game-day source), R06 (nominal deadline as news instant), R07 (non-Sunday report weekdays), R08 (primary width + sensitivities), R09 (Melbourne exclusion), R10 (coverage definition), R11 (control definition, k, ties, game-day exclusion), R12 (control sensitivities), R14 (all maker fills, row unit), R17 (horizon grid + H\*), R18 (MO^mid secondary), R20 (fee allocation for orders spanning window edges), R23 (cluster unit + fixed population), R25 (verdict thresholds), R27 (post-count descriptives), plus three non-rule items: (U16) the Scout's 8 windows corrected to 6 rule-based release days; (U17) NE@SEA excluded for having no in-scope report day; (U18) repo base not network-verified (§9).
**Key ones:** R08/R17 (width and horizon), R11 (controls), R06 (nominal vs actual release), R09 (Melbourne), R23 (bootstrap population).
**BLOCKERS: none for freezing.** Implementation is sequenced later (§9).

## 6. Ordering log, lookahead and label-exposure declaration

- **Ordering (ET, 2026-10-03).** ~17:58 read the inputs (kick, Scout brief, rulings, K1/K2 freezes, Examiner/Adversary notes). Six WebSearch queries. **18:00:16–18:00:43** saved S1–S9 (curl); WebFetch of S1. **18:01:56 `DESIGN_PREDECLARATION.txt` (`ba5ec554…`) written**: rule, release clock, in-scope weekdays, primary width + sensitivities, Melbourne exclusion, controls, horizons, H\*, estimand, bootstrap, verdict thresholds, fee rule. This was **before any window, count or market value was computed**. 18:02–18:04 windows derived (`79756fc5…`, twice, byte-identical) and structural counts run. The structural counts changed **no** pre-declared parameter. Only R27's descriptive extras were added after them, and they are disclosed as such.
- **Market bytes touched.** Tape: `ticker`, `at` and the `kind` key only (coverage and counts). Fills: `at`, `event`, `ticker`, `kind`, `size`, `order_id`, plus `price` **only** inside the whole-ledger fee-total reproduction. The `outcome` field of one fill row was printed while checking timestamp formats. **No mid, quote value, trade price, markout, price move or PnL was computed or viewed. No in-window vs control comparison of any value exists.**
- **Outcome exposure (disclosed).** (1) While checking game weekdays in S8/S9 (NFL.com schedule pages), the extraction printed W1/W2 **team records and some final scores**. K3 uses no settlement or score anywhere: it is label-free, and T03 is a strict invariance. (2) Prior exposure: the author read the K1 Examiner scorecard (whole-ledger open-leg MO_1800 by consensus bucket, ≈0.005 $/contract gross) and the K2 v67 report (Δ\*_a). Neither is window-split. Neither informed any K3 parameter; H\* = 300 s and w = 1800 s were fixed on the a-priori grounds in R08/R17.
- **Label-free design.** Windows, controls and membership are functions of (rule constants, kickoff epochs, per-ticker coverage timestamps, fill `at`/`event`/`kind`) only. Permuting quote values, trade prices or sides, fill prices or `outcome_mid_at_fill`, or any score must leave `WINDOWS.json`, `MEMBERSHIP_FIXTURE.json` and the constancy sha byte-identical (T03).

## 7. Verdict mapping and scope

| Condition (evaluated in order) | Verdict |
|---|---|
| R35 or R36 gate fails | INCONCLUSIVE |
| N6: Δ\* undefined (0 valid IN or 0 valid CTRL contracts at H\*) or CI undefined | INCONCLUSIVE |
| dropped resamples > 5%; censored at H\* > 20% of IN or CTRL contracts; < 5 events with valid IN or < 5 with valid CTRL fills | INCONCLUSIVE |
| 95% CI of gross Δ\* excludes 0 (either sign) | **ITERATE** (cap) |
| 95% CI of gross Δ\* includes 0 | DESCRIPTIVE |

- **KEEP, KILL of 000, retune and promotion are impossible.** `counts_toward_keep=false`, `promote=false`, `live_promotion=false`, `feeds_gate=false`.
- Evidence class `IN_SAMPLE_DEV` / `HISTORICAL_REPLAY`, the reused 31-game cohort (dev-grade, not OOS). Hypothetical replay fills only (v1.2: simulated fills never count toward KEEP). family_size = 1. Cluster population 29 events; expected n_eff 12 IN / 13 CTRL / 7 both.
- The NFL RESERVED_HOLDOUT `74507e1a…`, the KXMLBSPREAD prereg `9a987a77…` / `370dc31d…` and the ADMIT-1 window stay untouched and are refused in code. The inactives half is out of scope (R32).

## 8. Required tests (named; all green before the PR leaves draft; **every expected value comes from this packet's fixtures or a hand-written vector, never from the PR's own output** — N3/A6 pre-empted)

- **T01 Window derivation fixture.** Re-derive windows from the R04 constants plus pinned inputs and assert `WINDOWS.json` is byte-identical (`79756fc5…`).
  - Rule vectors per game weekday (§3.2 table).
  - DST vectors: 2026-09-09 16:00 ET → 20:00Z; 2026-11-04 16:00 ET → 21:00Z; 2026-03-08 16:00 ET (DST start day) → 20:00Z; 2026-11-01 16:00 ET (DST end day) → 21:00Z.
  - Half-open edges: a fill at start_epoch is IN; a fill at end_epoch is not.
  - 6 release days, 85 / 84 event-windows, 29 primary events; NE@SEA has no window; SF–LA is flagged `INTL_TZ_U`.
- **T02 Membership fixture.** `MEMBERSHIP_FIXTURE.json` is byte-identical (`ecc2b1a8…`). IN 136 / 4,173.49; CTRL 160 / 4,252.57. Per-window counts equal `STRUCTURAL_VERIFY.json` `per_window`. The sensitivity totals equal §4.
- **T03 Full-rebuild invariance (N1 pre-empted).** For 20 seeded permutations (`random.Random(20261003)`) plus one shift-by-1 derangement:
  - Permute the quote rows' (bid, ask, asof) across rows, the trade rows' (yes_price, taker_side, size), and the fills' (price, outcome_mid_at_fill), and attach a synthetic per-game result vector.
  - Rebuild **from bytes, through the PR code, with no cache**: windows → controls → membership.
  - Assert the constancy sha == **`bc6f692d…`** every time.
  - **Positive controls (must change the constancy sha):** (a) release clock 17:00; (b) FRI removed from the in-scope set; (c) k = 3.
  - Also assert the markout-table sha **differs** under the quote permutation, which proves the test reaches the markout path. Assert inequality only; print no values.
  - Write `INVARIANCE.json` with the R29 header.
- **T04 Timing inputs are price-free.** `derive_windows` / `select_controls` / `assign_membership` accept no price, quote or markout argument (`TimingInputRefused`). An AST scan of those modules finds no reference to `yes_price`, `bid`, `ask`, `price` or `outcome_mid_at_fill`.
- **T05 Fee Decimal.**
  - K1 T05 vectors, verbatim.
  - Whole-ledger headline **$1,286.22** over 1,846 orders.
  - The converter raises `FloatDecimalRefused` on a float, and a test shows that a `Decimal(float)` path would give $1,286.59.
  - Direct-member sensitivity is never the headline; `CACHE_NOT_R1P1`; `examiner_pin_account_class` is null.
- **T06 Bootstrap equivalence + performance.**
  - The sufficient-statistic and naive row-level resamplers produce identical Δ_b (≤ 1e-12) for B = 200 on the real membership.
  - 3-game hand fixture: a known Δ\* and percentile CI computed by hand (type-7).
  - The full B = 10,000 run takes ≤ 120 s; the same seed gives byte-identical CI output.
  - Dropped-resample counting is exercised on a fixture with a zero-IN draw.
- **T07 Verdict / N6 fixtures.** Each of these maps to its R25 verdict: zero IN; zero CTRL; CI None; dropped 6%; censored 21% (IN) and 21% (CTRL); 4 IN events; CI excluding 0 on each side; CI including 0. The verdict is never KEEP or KILL. Sensitivity cells get cell labels only.
- **T08 Markout sign, nulls and fill-membership edges.**
  - Sign: a NO fill at 0.40 with yes-mid 0.60 → 0.65 gives mid_out 0.35, MO = −0.05 and AS = +0.05. A YES fill at 0.40 with yes-mid 0.40 → 0.43 gives MO = +0.03.
  - K1 T08 null vectors (t − asof 299.999 valid, 300.0 null; no prior quote → null; past the last row → null; bid ≥ ask → null; a print never changes the mid).
- **T09 Structural gate (R35)**, asserted from the vendored pins.
- **T10 ADMIT-1 / holdout refusal**, using K1 T04 vectors: 2026-09-27T00:00:00Z rejected; 2026-09-30T03:59:59.999Z rejected; 2026-09-30T04:00:00Z accepted; `26SEP21NYGLAR` / `26SEP24ATLGB` / `2026_03_PHI_CHI` / `KXMLBSPREAD-…` refused; sqlite paths refused; AST import scan.
- **T11 Closed manifest.** A one-byte tamper of any vendored pin, `SOURCE_PINS.json`, `WINDOWS.json`, `MEMBERSHIP_FIXTURE.json` or a bundle part → hard fail before any read.
- **T12 Provenance header (N5 pre-empted).** Every committed JSON, including `INVARIANCE.json`, carries `python_version`, `platform`, the R29 shas and the four tags; fee fields carry `CACHE_NOT_R1P1`.
- **T13 No ROI / KEEP framing.** `EMPTY_RESULTS.json` keeps `results` / `pnl` / `roi` = null. No output key matching `/(^|_)(pnl|roi|keep|profit|sharpe|return)(_|$)/i` has a non-null value. Verdict ∈ {DESCRIPTIVE, ITERATE, INCONCLUSIVE, null}.
- **T14 000 untouched.** The shas of `replay_v2.py`, `queue_policies.py` and the q3300_d0.25_000 files equal the pins; the git diff of `nfl_factorial_lab_20260921/` is empty.
- **T15 Refusals and redistribution.**
  - Lee-Ready key or call → refused. Any band or rebin call → `RebinRefused`. A `becker` / `*.parquet` path → `BeckerRefused`.
  - The git tree contains no `nfl_sources/*.html|pdf|txt`, no freeze md/json copy (the shas may appear; the bytes may not) and no parquet.
- **T16 Fixture policy.** A meta-test lists every numeric assertion's expected-value source; all are packet fixtures (`WINDOWS.json`, `MEMBERSHIP_FIXTURE.json`, `STRUCTURAL_VERIFY.json`) or literal vectors. None compares an output with itself.

Test command: `python3 -m unittest discover -s tests -v` from the lab dir (K1 convention).

## 9. Implementation sequencing and cloud instructions (LATER; only after Conductor ACCEPT + IMPLEMENT GO)

0. **Sequencing (binding).** Implementation starts only after: (1) the **K2 PR67 merge** (gate per ruling `ac8e26c8`), (2) the **K1 follow-up PR** with N1/N3/N5/N6 fixes (ACCEPT-score `530cca94` "K1 follow-up (N1/N5/N3/N6) after K2"), and (3) the **card01 Amendment C code** (ACCEPT `2225c3fa`). No cloud is launched by this freeze.
1. **One** cloud, repo `17thgreen/GPT-6-Astra-Deathmatch`, **draft PR**, base = main HEAD at launch (recorded). Last recorded main = `09b56273` (PR66 merge; local object only; **UNPINNED U18**, not network-verified). Proceed only if `nfl_factorial_lab_20260921/` is byte-identical to the pins (T14).
2. **Lab layout.** `kalshi_ext_k3_injury_window_lab_20261003/`:
   - `timing/` (rule constants, windows, controls, membership: price-free, T04)
   - `markouts.py` (import K1 `QuoteBook` / `outcome_mid` read-only if present on main, else re-implement against K1 T08)
   - `fees.py` (Decimal(str) only)
   - `bootstrap.py` (sufficient statistics plus the naive equivalence reference)
   - `verdict.py`, `orchestrator.py`, `common_header.py`
   - `tests/`, `pins/`, `results/`
   - `EXPERIMENT_SPEC.md` (a summary; **not** a copy of this md)
   - `FROZEN_EXPERIMENT.json` (embeds this md's and the json twin's sha256)
   - `README.md`, an Examiner HOLD_PRE_PR file, and one registry row that mentions §6 outcome exposure (A9 pre-empted)
3. **Vendoring.** Vendor the K1 bundle `0f8f5297…` (parts) and the K3 bundle (§10) verbatim under `pins/`, and check each MANIFEST. `*.jsonl.gz` is git-ignored, so force-add it under `pins/` only, as in K1. **Never vendor `nfl_sources/` HTML/PDF/TXT, the freeze md/json bytes, or any Becker byte.**
4. **Committed outputs (markouts ARE the measurement, so they are allowed):** `results/STRUCTURAL.json`, `results/WINDOWS_RECHECK.json`, `results/MARKOUTS.json` (IN / CTRL × h × gross/net/MO^mid, per window, per event, all sensitivities with cell labels), `results/CONTRAST.json` (Δ\*, CI, n_eff, dropped, verdict proposal), `results/INVARIANCE.json`, `results/EMPTY_RESULTS.json`, `results/UNIT_RESULTS.md`. **Not allowed:** PnL, ROI, Sharpe, "would have earned", KEEP/KILL language, or a per-fill dump of the real ledger.
5. No `sqlite3`, no network imports, no `subprocess`, no `admit.py`, no orders. 000's lab, the K1/K2 labs and feebook/rails stay byte-unchanged.
6. The Adversary reviews T03, T06 and §6 before the Examiner scores within {DESCRIPTIVE, ITERATE, INCONCLUSIVE} and pins the account class.

## 10. Integrity

- **Packet folder `packets/EXT_K3_INJURY_WINDOW/`.** Contents:
  - `DESIGN_PREDECLARATION.txt`, `derive_windows.py`, `WINDOWS.json`, `structural_verify.py`, `STRUCTURAL_VERIFY.json`, `MEMBERSHIP_FIXTURE.json`, `SOURCE_PINS.json`, `EMPTY_RESULTS.json`, `FROZEN_EXPERIMENT.json`, `BUNDLE_RECEIPT.json`, `MANIFEST.sha256`
  - `nfl_sources/` (S1–S9 raw, `.txt` extracts, `extract_text.py`, `SOURCES_FETCH_LOG.json`)

  `MANIFEST.sha256` covers every file in the folder, recursively, plus the freeze md/json via `../`. JSON twin: `packets/VARIANTS_EXT_K3_INJURY_WINDOW_TOXICITY_FREEZE_2026-10-03.json` (embeds this md's sha256).
- **Cloud pin bundle (K3 delta).** `/workspace/EXT_K3_authentic_pins_2026-10-03.tgz` holds the packet files **except** `nfl_sources/*.html|pdf|txt`, plus `DEPENDS_ON.txt` (names K1 bundle `0f8f5297`) and an inner `MANIFEST.sha256`. It carries **no freeze md/json, no NFL source copy and no Becker byte.** Its sha and size are in `BUNDLE_RECEIPT.json`, because the bundle cannot contain its own sha.
- **New files only.** Under RULE-FROZEN-EDIT-PREV-BYTES-001 this freeze creates only new files. No frozen file was edited, so there was no `_prev` write.
- `results = null`, `pnl = null`, `roi = null`.

## 11. Data gaps / attention items (not blockers)

1. **Thin in-window sample.** 136 fills / 4,173.49 contracts in 13 windows from 12 events; zero fills in the W1 Wed/Thu windows; DET@BUF holds 43% of IN fills. The verdict is likely DESCRIPTIVE or INCONCLUSIVE, and is capped at ITERATE. R27 descriptives expose the concentration.
2. **Nominal vs actual release time [A].** The deadline is "no later than 4:00 p.m. or ASAP after practice", and actual postings are unrecorded on the box. LATE and W3600 bracket the late-filer case.
3. **Scout window count corrected:** 8 → 6 rule-based release days (9/3 and 9/4 are not report days). The Scout's row counts reproduce on its own definition.
4. **Melbourne game** excluded from the primary (R09); S_INTL reports it.
5. **C_CLEANDAY** has only 1 event with control fills and will be `CELL_UNDEFINED` / low-n.
6. **Account class open** (Examiner pin); the headline is the $0.01-per-order bound.
7. **Repo base** (`09b56273` or later) is not network-verified; `/workspace/lab` is not itself a git checkout (`astra-science` clone is at `eb33f09`). The cloud records HEAD.
8. **Outcome exposure** (§6): NFL.com schedule pages showed W1/W2 scores. K3 is label-free.
9. **Commission provenance:** the Conductor scope text exists only in the delegation [U]; the Archivist should file it.

## 12. Refuse binds

invent fills / quotes / release timestamps · infer release time from the tape · re-run or retune 000 · KEEP or KILL 000 · ROI/PnL framing · stand-down counterfactual without a new freeze · Lee-Ready · tick-rule or print-derived mids · rebin registry `0860cbe2` · price-band splits · holdout rows (NFL RESERVED_HOLDOUT `74507e1a`, KXMLBSPREAD prereg `9a987a77` / `370dc31d`, NYG@LA / ATL@GB measurement-dev events) · ADMIT-1 window data · `capture.sqlite` · weather `archive.sqlite` · `admit.py` · any Kalshi or network GET · Becker archive · new nflverse pull · NFL source re-fetch or redistribution · inactives (T−90) half · vendoring freeze md/json bytes · `Decimal(float)` fees · headline the direct-member fee · claim CACHE as R1-P1 · dual cloud · launching before the §9 sequencing · moving any rule after a run · editing any frozen byte
