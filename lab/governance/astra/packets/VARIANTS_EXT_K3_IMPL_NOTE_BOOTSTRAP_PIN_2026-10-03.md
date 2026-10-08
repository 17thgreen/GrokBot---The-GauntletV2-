# IMPLEMENTATION NOTE: EXT-K3 NFL injury-window toxicity, bootstrap draw-method and draw-order pin (pre-implementation, docs-only)

**Dated:** 2026-10-03 (ET). **Status:** `DRAFT, AWAITING_CONDUCTOR_ACCEPT` (not filed; the filer adds the filed timestamp).
**Kind:** **implementation note, no change to gates/thresholds/verdict rules/estimand.** It only resolves ambiguity. It changes no seed (20261003), no B (10,000), no cluster unit (event), no population (29 primary events), no percentile type (type-7), no drop rule, no N6/floor threshold (5% / 20% / 5 events), no window, control, horizon or fee rule, and no verdict map (§7). It is not a re-freeze.
**Pre-implementation:** K3 has no code and no results. No markout, mid, price or outcome was read for this note. The only K3 data opened were the label-free packet fixtures (`WINDOWS.json`, `MEMBERSHIP_FIXTURE.json`: window ids and fill row indices).
**Evidence tags:** [V] verified on the box this session · [I] inferred · [A] assumption / choice made by this note · [U] unknown / provenance not on the box.

## 0. Lineage

| Artifact | Path (under `packets/`) | sha256 | Role |
|---|---|---|---|
| K3 freeze md | `VARIANTS_EXT_K3_INJURY_WINDOW_TOXICITY_FREEZE_2026-10-03.md` | `705872df98073344f19f875b18d5e9a732920f1e4a8b5228eaa0b9d85957b1e6` | [V] re-hashed |
| K3 freeze json | `VARIANTS_EXT_K3_INJURY_WINDOW_TOXICITY_FREEZE_2026-10-03.json` | `34031760c144708ba29cd3dc5ac9ea1b9790eb876ff318ca898a6ec3d8c2950a` | [V] |
| Conductor ACCEPT | `CONDUCTOR_ACCEPT_EXT_K3_FREEZE_2026-10-03.json` | `bdda8ed6c6e84627b786790a1b38f2758b1bfdfa73c252529f84f7c2b1f187c1` | [V]; condition 2 = LOO table incl. DETBUF-0916 drop, `SENSITIVITY_NOT_SELECTION` |
| Packet MANIFEST | `EXT_K3_INJURY_WINDOW/MANIFEST.sha256` | `af5067e433f267045f6924e7a1e1ea960bb52dfa726ed1075e540eb4edb8bac3` | [V] = ACCEPT `verified.manifest` |
| WINDOWS / MEMBERSHIP / FROZEN_EXPERIMENT / DESIGN_PREDECLARATION | `EXT_K3_INJURY_WINDOW/…` | `79756fc5…` / `ecc2b1a8…` / `57be8552…` / `ba5ec554…` | [V] |
| N6 ruling | `CONDUCTOR_RULING_EXT_K1_N6_UNDEFINED_DELTA_2026-10-03.json` | `0b68c4bf…` (as cited in freeze L19) | "undefined Delta* or undefined CI => verdict INCONCLUSIVE" |
| **Rule source** | `CONDUCTOR_SCORE_ACCEPT_EXT_K2_PARTA_2026-10-03.md` | `6824793a44f5a10ee1d6e869e694d6681cfaba1681ff9b4bfb7cd0ed98242502` | [V] line 9: "STANDING RULE from today: every new freeze must pin the bootstrap draw method and order (RNG, seed, resampling unit, draw sequence)." |
| Precedent: K1 merged code | repo @ `0dc940c3` (`/workspace/v68/repo`), `kalshi_ext_k1_q6000_legging_audit_lab_20261003/report.py` | file sha `233e6692…`; `contrast()` L144–L211, `_percentile()` L108–L120 | [V] |
| Precedent: K2 merged code | repo @ `f30145c7` (`/workspace/v67b/repo`), `kalshi_ext_k2_optimism_tax_lab_20261003/dev_pipeline/markouts.py` L300–L345; `terciles.py` `q7` L25–L35 | — | [V] |

The remedy for already-ACCEPTED freezes (an implementation note ACCEPTed by the Conductor, not a re-freeze) comes from the Conductor via the delegation text; no on-box file states it [U].

## 1. What the freeze already pins (verbatim, with line numbers) [V]

Freeze md `705872df`:
- **L285 (R23):** "**Bootstrap (vectorized, game-clustered).** Cluster = event. The population is the **29 primary events** (fixed by `WINDOWS.json`, including events with zero in-window or control fills). Sorted by event ticker. `rng = random.Random(20261003)`; for b in 1..10,000: `idx = rng.choices(range(29), k=29)`. **Per-event sufficient statistics** (Σw·MO and Σw for IN and for CTRL, gross and net, built once with `math.fsum`) give Δ_b = ΣIN_num/ΣIN_den − ΣCTRL_num/ΣCTRL_den. A resample with a zero denominator is undefined: it is dropped and counted. The 95% CI is the type-7 (linear) percentile of the kept Δ_b at 0.025 / 0.975. **Equivalence (T06):** the naive row-level resampler … must give the same Δ_b sequence within 1e-12 for B = 200 … The full run must finish in ≤ 120 s …"
- **L286 (R24):** n_eff includes "kept/dropped resamples".
- **L287 (R25):** "**N6:** Δ\* undefined (zero valid IN or zero valid CTRL contracts at H\*) or CI undefined (fewer than 2 kept resamples or any None); dropped resamples > 5% of B; …" → INCONCLUSIVE; "Each sensitivity cell gets a **cell label** under the same (a)–(c) logic (`CELL_UNDEFINED` / `CELL_CI_EXCLUDES_0` / `CELL_CI_INCLUDES_0`)".
- **L288 (R26):** only gross Δ\* moves the verdict (family_size = 1).
- **L289 (R27):** "(1) leave-one-event-out Δ\* (29 values; …) … (4) a **release-day-cluster** bootstrap (6 days; B = 10,000; seed 20261003) flagged `LOW_CLUSTER_COUNT`."
- **L322:** "dropped resamples > 5% …" → INCONCLUSIVE. **L338 (T03):** "For 20 seeded permutations (`random.Random(20261003)`) …". **L351–L355 (T06):** identical Δ_b (≤ 1e-12) for B = 200; a 3-game hand fixture with a type-7 CI; "the same seed gives byte-identical CI output"; dropped-resample counting on a zero-IN fixture.
- L21 / L31 (commission, C7): "clustered vectorized bootstrap with an equivalence test, n_eff"; "game-cluster bootstrap, fixed seed/B".

Freeze json `34031760` L14–L23 and `FROZEN_EXPERIMENT.json` L2–L11: `"B": 10000`, `"ci": "type-7 percentile 95%"`, `"cluster": "event"`, `"equivalence": "naive row-level, B=200, <=1e-12"`, `"method": "per-event sufficient statistics (math.fsum)"`, `"population": "29 primary events (fixed)"`, `"rng": "random.Random(20261003).choices(range(29),k=29)"`, `"runtime_budget_s": 120`. `DESIGN_PREDECLARATION.txt` L31–L33: "B = 10,000, random.Random(20261003).choices over sorted events, per-event sufficient statistics, percentile type-7 95% CI".

## 2. Item-by-item status

| Item | Status | Ref |
|---|---|---|
| RNG / library | **Pinned**: `random.Random` | L285; json L21 [V] |
| Seed | **Pinned**: 20261003 | L285, L289 [V] |
| Number of resamples | **Pinned**: 10,000 (T06 equivalence B = 200) | L285, L289, L352 [V] |
| Resampling unit / population | **Pinned**: event; 29 primary events, fixed | L285 [V] |
| Unit sort key | **Pinned**: "Sorted by event ticker" (Python `str` order assumed [I]) | L285 [V] |
| Draw call | **Pinned**: `rng.choices(range(29), k=29)` | L285 [V] |
| Stratification | **Pinned (none)**, by omission plus fixed population [I] | L285 |
| RNG instance isolation | **AMBIGUOUS**: T03 also uses `random.Random(20261003)` (L338). Nothing says the bootstrap stream is a separate instance | L285, L338 |
| One draw vector shared across gross/net | **Implied, not explicit**: "gross and net" sufficient statistics in one sentence | L285 |
| Shared across sensitivity cells | **SILENT**: R25 needs a CI for every sensitivity cell (cell labels), but no draws are named for cells | L287 |
| S_INTL population (30 events) | **SILENT** | L259, L287 |
| Per-draw aggregation arithmetic | **SILENT** past per-event `math.fsum` (K1 uses `+=` in draw order; K2 uses `fsum` over pooled rows) | L285 |
| Valid-fill rule inside sufficient statistics | **Implied** (R16/R19/R24 "valid"); not stated in R23 | L274, L277, L285 |
| Net per-draw (denominators, fee float conversion) | **SILENT** | L278, L285 |
| Percentile formula | **Named** (type-7 at 0.025/0.975); the exact float expression is not pinned (K1 and K2 forms differ by ulps) | L285, L353 |
| Dropped / undefined | **Pinned**: zero denominator → drop + count; > 5% dropped → INCONCLUSIVE; < 2 kept or None → CI undefined → INCONCLUSIVE (N6) | L285, L287, L322 [V] |
| Release-day bootstrap (R27(4)) | **Partly pinned**: 6 days, B, seed. **Silent** on RNG class, draw call, day order, and **how CTRL fills map to release days** (controls are de-duplicated per event, R11) | L289, L265 |
| LOO table (R27(1) + ACCEPT condition 2) | **Silent on CIs**; "DETBUF-0916 drop" undefined as event-drop vs window-drop | L289; ACCEPT `conditions[1]` |
| Within-event paired contrast (R27(3)) | **Silent on CI** | L289 |

## 3. Pins (govern implementation)

**K3-P1. RNG instances [A].** Every consumer builds its own `random.Random(20261003)`; no instance is shared. In particular, the T03 permutation generator (L338) is a **separate** instance and never advances the bootstrap stream. Nothing else draws from a bootstrap instance. No numpy RNG and no `random` module-level functions.

**K3-P2. Primary draw sequence [V restated + A].** `EVENTS = sorted(e for e in WINDOWS.json primary events)`, i.e. the 29 `KXNFLGAME-…` tickers with a `primary_included` window, in Python default `str` order. That runs from `KXNFLGAME-26SEP13ARILAC` (index 0) to `KXNFLGAME-26SEP20WASDAL` (index 28) [V], and the list is asserted equal to the frozen list in `WINDOWS.json`. `rng = random.Random(20261003)`; then, **before any statistic is computed**, `IDX = [rng.choices(range(29), k=29) for _ in range(10000)]` (b = 0..9999 in order; each vector in draw order). `IDX` is the single draw sequence for every 29-event statistic.

**K3-P3. Sharing [A].** **One draw vector per resample, shared across all statistics on the 29-event population:** gross and net, every horizon h ∈ {60, 300, 900, 1800}, every width (W1800, W900, W3600, LATE), every control design (C_PRIMARY_K2, C_ALL, C_SAMEDAY, C_CLEANDAY) and MO^mid. Each cell's Δ_b(b) uses `IDX[b]`. Loop order: for cell (any order; output is order-independent), for b in 0..9999. Precedent: K1 `contrast()` draws one vector per resample for gross and net (L168, L183–L184); K2 `becker_pipeline._bootstrap_many` shares one draw across all fields [V].

**K3-P4. S_INTL [A].** Population = the 29 primary events plus `KXNFLGAME-26SEP10SFLAR`, sorted (30 events; SFLAR sorts to index 0 [V]). A fresh `random.Random(20261003)`; `IDX30 = [rng.choices(range(30), k=30) for _ in range(10000)]`. Same statistic, drop and percentile rules. Cell label only.

**K3-P5. Per-event sufficient statistics [A, consistent with L285].** For event e, set S ∈ {IN, CTRL}, cell c: the valid fills are those with a non-null MO_h (R19). Iterate them in fills-ledger file order. Then `den[e][S] = math.fsum(size_f)` and `num[e][S] = math.fsum(size_f * MO_h(f))`, where `size_f` and MO are Python floats and the product is a float. Net: `num_net[e][S] = math.fsum(size_f * (MO_h(f) - fc_f))`, where `fc_f = float(F_o / C_o)` is computed in `decimal.Decimal` (default context) from the R20 headline order fee F_o and the order's total contracts C_o, then converted once with `float()`. Net uses the **same** denominators as gross (net is valid iff MO is valid). Events with no valid fills have `num = den = 0.0`.

**K3-P6. Per-draw statistic [A].** For resample b: `IN_den = math.fsum(den[EVENTS[i]]["IN"] for i in IDX[b])`, and likewise `IN_num`, `CTRL_den`, `CTRL_num` (the multiset in draw order; `fsum` is exactly rounded, so the result does not depend on order). If `IN_den <= 0.0` or `CTRL_den <= 0.0`, the resample is **dropped** and counted (K1 L180 precedent). Otherwise `Δ_b = IN_num/IN_den − CTRL_num/CTRL_den`, and the net Δ_b uses the net numerators over the same denominators (so net and gross drop together). The point estimate Δ\* is computed directly from the fill rows: `fsum` over all valid IN fills, divided by its `fsum` of sizes, minus the same for CTRL. It is not a bootstrap mean.

**K3-P7. Percentile [A; K1 merged formula].** Collect the kept Δ_b in b order, then `kept.sort()` (ascending). If `len(kept) < 2`, the CI is `None`, i.e. **undefined → INCONCLUSIVE** (R25/N6) for the primary, or `CELL_UNDEFINED` for a cell. Otherwise, for p ∈ {0.025, 0.975} (Python float literals): `pos = p * (n - 1)`; `lo = math.floor(pos)`; `hi = math.ceil(pos)`; the value is `kept[lo]` if `lo == hi`, else `kept[lo] * (1.0 - w) + kept[hi] * w` with `w = pos - lo`. This is exactly K1 `report._percentile` (L108–L120, merged and unchanged in `0dc940c3`). It equals `numpy.percentile(kept, [2.5, 97.5], method='linear')` mathematically, but numpy is **not** used, and the K2 `q7` expression is **not** used, so the output is byte-reproducible. For n = 10,000, pos = 249.975 and 9749.025.

**K3-P8. Dropped-draw accounting [V restated].** Report `kept`, `dropped` and `dropped_share = dropped / 10000` per cell. Primary: `dropped_share > 0.05` → INCONCLUSIVE (L287, L322). A cell uses the same rule for its cell label. Nothing is imputed, re-drawn or replaced; B is never topped up.

**K3-P9. T06 equivalence [A, consistent with L285/L352].** The naive row-level reference consumes `IDX[0:200]` from its **own** fresh `random.Random(20261003)` (identical to the first 200 vectors of the main run). It concatenates the drawn events' valid fill rows in draw order and recomputes with `math.fsum`, and must match the sufficient-statistic Δ_b element-wise within 1e-12. The 3-game hand fixture uses `random.Random(20261003).choices(range(3), k=3)` and the K3-P7 formula.

**K3-P10. Release-day-cluster bootstrap, R27(4) (descriptive, `LOW_CLUSTER_COUNT`) [A].** Population: the 6 release days from `WINDOWS.json` `release_days`, sorted by ISO date (`2026-09-09` … `2026-09-18`), fixed, including days with zero fills. Cluster d holds: IN fills in primary windows whose `report_day_et == d`; and CTRL fills of each primary control window (event e, control date D′), assigned to the **one** in-scope primary window of e that selected D′ in `C_PRIMARY_K2` with the smallest |D′ − D|, ties to the earlier D. That mirrors R11's own ranking, so each CTRL fill sits in exactly one day and the all-days estimate equals Δ\*. A fresh `random.Random(20261003)`; `IDXD = [rng.choices(range(6), k=6) for _ in range(10000)]`. Same K3-P5…P8 rules, gross and net. Never verdict-moving. [I] Under this mapping CTRL fills fall on 9/11, 9/16 and 9/18 only, so roughly (1/2)^6 ≈ 1.6% of resamples drop.

**K3-P11. Leave-one-event-out table (R27(1) + ACCEPT condition 2) [A].** 29 rows, one per event in `EVENTS` order. Row e = Δ\* (gross, with net beside) recomputed from fill rows with all IN **and** CTRL fills of e removed, plus n_eff for the remaining set. **No CI is recomputed, and no bootstrap draws are used** for any LOO row; R27(1) specifies "Δ\* (29 values)". A Δ\* that becomes undefined is reported as `UNDEFINED`, never imputed. The table carries `SENSITIVITY_NOT_SELECTION` and never moves the verdict. **The DETBUF-0916 drop is the row for `KXNFLGAME-26SEP17DETBUF`, labelled `DETBUF-0916 drop`.** DET@BUF has exactly one in-scope window, `K3W-26SEP17DETBUF-20260916-WED` (freeze L113; `WINDOWS.json`) [V], and in the primary design it has 59 IN fills and **0 CTRL fills** (`MEMBERSHIP_FIXTURE.json`; consistent with freeze L232) [V]. So "drop the event" and "drop only the 9/16 window's IN fills" give the identical Δ\*, and the two readings coincide [V by construction].

**K3-P12. Other R27 extras [A].** (2) max single-event share of IN contracts and (3) the within-event paired contrast are **point estimates only**, with no CI and no draws.

**K3-P13. Provenance [A].** `CONTRAST.json` records `bootstrap_sampler: "random.Random(20261003).choices(range(29),k=29) over sorted primary event tickers; one IDX shared by all 29-event cells"`, `percentile_method: "type-7, K1 report._percentile expression"`, `aggregation: "math.fsum per event and per draw"`, and the `IDX` digest: sha256 of the canonical JSON (R34) of `IDX`, so that any re-implementation can prove it consumed the identical draws. `IDXD` and `IDX30` digests are recorded the same way.

## 4. Precedent: how K1 and K2 actually drew [V]

- **K1** (`report.py` `contrast()`, merged `09b56273`, unchanged in `0dc940c3`): `events = sorted(weeks)` (all 31 cohort events, a fixed population; orchestrator L486). `rng = random.Random(20261003)`, a fresh instance per call. Per resample, `draw = rng.choices(events, k=len(events))`. Per-event `[Σsize, Σsize·gross, Σsize·net]` are accumulated with float `+=`, and the drawn events are summed with `+=` in draw order. A resample is dropped if the ON or AGAINST weight is `<= 0`. Gross and net come from the same draw and the same denominators. Values are sorted, and `_percentile` is linear at `p*(n−1)` as `a*(1−w) + b*w`. Records `bootstrap_sampler: "random.Random(20261003).choices(events, k=31)"`.
- **K2 part (a)** (`dev_pipeline/markouts.py` `bootstrap_delta`, `a940355a`/`f30145c7`): `games = list(week_membership.json keys)`, i.e. **file key order, unsorted** (`load.py` L105). `rng = random.Random(20261003)`. Per resample, `draw = [games[rng.randrange(n)] for _ in range(n)]`. The drawn events' (size, value) pairs are pooled, then reduced with `math.fsum` weighted means. A resample is dropped if T1 or T3 is empty. Net is appended only if both net pools are non-empty, so net can drop separately. The CI uses `q7` (type-7, `a + (h−lo)·(b−a)`). `randrange` and `choices` consume the Mersenne Twister differently, so the streams differ. That plus the key order is the source of the Examiner anomaly. Examiner alternates: randrange over sorted games [−0.001023, 0.000444]; K1-style choices over sorted events [−0.001039, 0.000438]; code [−0.001030989, 0.000450135] (5th-decimal shifts; verdict invariant) (scorecard `ffd008a4` L87–L93; Conductor `6824793a` L6, L9).
- **K2 part (b)** (`becker_pipeline/metrics.py` `_bootstrap_many`, code only, no data read): `events = sorted(...)`; `rng.randrange(n)` per position. One draw is shared across all fields. A field whose value is `None` in a resample is silently skipped and **not counted**, which is unlike K1/K3.
- K3 already chose the K1 primitive (`choices` over sorted tickers). This note keeps it and pins the rest the K1 way.

## 5. Open questions for the Conductor

- **Q1 (could affect the verdict at the margin):** K3-P5/P6 fix the per-draw arithmetic (`fsum` over draws) and K3-P7 fixes the percentile expression. Alternatives (K1 `+=`, K2 `q7`, numpy) differ only at the ~1e-16 relative level, and could flip "CI excludes 0" only if an endpoint lies within ~1e-16 of 0 [I]. This is pinned to remove even that.
- **Q2 (reporting, internal ambiguity):** the release-day bootstrap (R27(4)) needs a CTRL-to-day mapping that R11's per-event de-duplication does not supply. K3-P10 picks "nearest selecting window, ties earlier". This is descriptive only, but the Conductor may prefer IN-only day resampling with CTRL fixed.
- **Q3 (reporting):** K3-P11 gives LOO rows **no CIs**. If the Conductor wants CIs on LOO rows (e.g. the DETBUF row), a further pin is needed. The proposed form would be a fresh `random.Random(20261003)` with `choices(range(28), k=28)` over the remaining sorted events, same rules, labelled `SENSITIVITY_NOT_SELECTION`. This note does not adopt it.
- **Q4 (provenance):** the rule source in the delegation was described as an "Examiner ACCEPT" with "~5e-5" differences "on the taker-sweep fields". On the box, `6824793a` is the **Conductor score-accept** of EXT-K2 part (a). The anomaly is on the Δ\*_a gross CI (T3−T1 flow-tercile markout), and the shifts are about 8e-6 to 1.2e-5 [V]. The citation used here is the on-box file.

## 6. No change

No gate, threshold, verdict rule or estimand changes. Sequencing (§9; ACCEPT condition 1) is unchanged. No new variant. `results = null`.
