# CARD 01 Exp-2: disagreement-and-depth census + October gate-count — FREEZE KERNEL (2026-09-24 ET)

**Packet ID:** `CARD01-NH-002-EXP2-CENSUS`
**Series:** same as NH-002-H — `KXHOUSERACE` Democratic `-D` contracts for the frozen 92-race House universe, plus Amendment A legacy HOUSEPARTY series where mapping resolves that way.
**Owner (freeze):** Deep Research
**Implementer (only after Conductor ACCEPT):** Collector (GET-only capture under Addendum 1). Variants may later join extracts; Examiner does **not** score this packet as a trading confirmation. Adversary checks overlap. Archivist records ElectIndex APPROVED_HASH_ONLY extracts and any fee-manifest updates that unblock gate-count.
**Reviewer:** Conductor
**Status:** **FROZEN**, not run. `results` = **null**, `pnl` = **null**. Study label: `prospective paper measurement` / **pre-rung** (no outcomes required; not a confirmation of NH-002-H).
**Governing charter:** `charters/DEEP_RESEARCH_MASTER_BRIEF_v1_1_2026-09-24.md`, sha256 `02272754b01da5b65edd837545e485f4fd4dff2903a7ae1f52d9cb5e616fec5d`.
**Parent freeze (cite, do not alter):** NH-002-H `packets/CARD01_HOUSE_ONLY_PROSPECTIVE_FREEZE_2026-09-24.md` sha256 `c31724463d81747702910a2d5296c2fc21d2a1dbc594727b26ac3d894b55ec59`, plus Amendment A sha256 `4e36d0db5728148d5bb4688fd8626eca9907a8933747f85e0bc17ede0ac0936b` and Amendment B sha256 `ee6af37cef95f1e468d28e5b06750caaca8b1706ec11ed5cf5cdce460524c2c6` (Conductor ACCEPT `packets/CONDUCTOR_ACCEPT_CARD01_NH002H_AMENDMENT_B_2026-09-24.json`, issued 2026-09-24T20:22-04:00).
**Decision packet Exp-2 / SOURCE_MAP D1:** ranked next experiment #2 in `packets/CARD01_NEGLECTED_HYBRID_DECISION_PACKET_2026-09-24.md` (sha256 `c0c1aa66f104e3f102228a7a8e16f205977afbee63928f30a6954ec46707a82c`); ElectIndex “October gate-count” smallest useful experiment in `packets/card01_hybrid_forecast/SOURCE_MAP_2026-09-24.md` (sha256 `2b38699de9f3bbb178675442fe5db4ed7d3941bba2ccb8386744ad85906610eb`) §D1.
**Hard rules:**
- No live orders. No paid data. No expert contact.
- No Q6-`000` retune. S2/R2-P4 stay gated.
- Exactly **one** knob (snapshot cadence). Results and pnl stay null.
- Never fill gaps. GET-only. **Deep Research issues zero Kalshi GETs**; Collector owns all Kalshi traffic per `COLLECTOR_KALSHI_GET_BUDGET_2026-09-24.md` Addendum 1.
- **No data pull until Conductor ACCEPT of this freeze.**
- This census is **pre-outcome support for Card 01**, not a new trading strategy and not a second NH-002-H scoring path.

---

## 1. Intent (one merged kernel)

**A. Disagreement-and-depth census (read-only).** At preregistered snapshot times from October through decision week, measure for each of the 92 frozen NH-002-H races:
- forecast-vs-market gap `|p_model − p_mkt|` (and logit gap) using ElectIndex `dem_prob` under Archivist **APPROVED_HASH_ONLY** rules (hashes / metadata / `dem_prob` for the 92 only; raw CSV stays in `evidence_private`);
- book depth at touch and visible size on the admitted YES/NO contracts (Collector orderbook GETs).

Closer to election night, densify book cadence in a short preregistered pre-decision window (hourly).

**B. October gate-count (same freeze, same snapshots).** At each weekly October snapshot, count how many of the frozen 92 races (and mapping-status subsets M1/M2/M3 from Amendment B) **pass the NH-002-H entry gate as written** — do **not** invent a new gate. Preregister the early-narrowing flag below. Flagging is measurement only; narrowing Card 01 to forecast-quality-only is a **Conductor** decision.

**Primary purpose:** early-warning / exploration support for whether 2026 disagreement and executable depth exist long enough to matter, and whether the after-cost path can produce any admitted signals before election night. **Not** confirmation of NH-002-H forecast quality.

## 2. Economic thesis (charter)

- **What mispricing / capacity risk this answers:** NH-002-H’s neglected-district thesis predicts persistent forecast–market gaps on thin House books. If gaps are ~0 by October, or depth at touch cannot support even the one-contract NH-002-H size, the after-cost / execution rung cannot produce evidence this cycle even if forecast Brier later looks fine. Conversely, large gaps with vanishing depth are capacity risk, not free edge.
- **Who trades with us (same as NH-002-H):** partisan/retail flow and thin passive quotes on race contracts; chamber-control (`CONTROLH`) is the liquid reference, not the trade universe.
- **What disproves usefulness of this census (any one):**
  - (i) Gaps are already negligible across October weekly snapshots (median `|p_model−p_mkt|` below the noise floor defined in §6), so “neglect” is not visible pre-decision.
  - (ii) Gate-pass count is about zero for consecutive October snapshots under the preregistered threshold (§7), so the after-cost path is empty before election night.
  - (iii) Visible touch depth is routinely `< 1` on races that would otherwise pass the entry gate, so disagreement is not executable.
  - (iv) Gaps collapse to ~0 inside the dense pre-decision window before any hypothetical taker could act (mechanism test of decision-packet critique (d)).

## 3. Status rung and explore vs confirm

| Rung | Status for this packet |
|---|---|
| Code verified | N/A (measurement extracts only; no scoring code required for the freeze) |
| Retrospective predictive evidence | N/A (no outcomes used) |
| Hypothetical after-cost result | **Out of scope** (pnl null; fee may be BLOCKED) |
| Prospective paper evidence | **Not claimed.** Outputs are unscored census tables. |
| Observed live execution | Forbidden |
| Scalable repeatability | N/A |

**Explore vs confirm ledger:** **EXPLORE / early-warning support** for Card 01. Does **not** confirm NH-002-H. Does **not** create a parallel confirmation study. Ledger row lives in `packets/card01_exp2_census/LEDGER_2026-09-24.md`.

## 4. Universe, mapping, pins (inherited; not re-tuned)

- **Universe:** the frozen 92 races in `packets/card01_hybrid_forecast/UNIVERSE_2026_HOUSE_FROZEN.json` (sha256 `d8af74515e449b151016105f956c5e54a4fb4eac3ec570364da58f8fe47d8ca6`). No race added or dropped by this freeze.
- **Mapping:** Amendment A search order; M1/M2/M3 split per Amendment B (d). Mapping still requires Collector verification before 2026-10-26; unresolved races count in M3 with reason, never imputed.
- **Blend weight for gate-count only:** `w = 0.5` exactly as NH-002-H headline (not a knob here). `p_hybrid = 0.5·p_ElectIndex + 0.5·p_mid`.
- **Entry gate (verbatim inheritance; do not invent a new gate):** a race **passes** at a snapshot iff there exists a side (D YES at YES ask, or D NO at `1 − YES bid`) such that
  `(p_hybrid of that side − price − fee − 2c buffer) > 3c reserve`,
  with fill feasible only if visible quantity at that price ≥ 1 (NH-002-H §5 / Amendment B unchanged statement). Feasible size = min(1, visible depth) is recorded but the **gate-pass count** is the number of races with at least one feasible passing side.
- **Fee:** R1-P1 feebook @ `22371178cb2663250b4762f328069571c48cb551`. Per Amendment B (c), House after-cost / gate evaluation that needs the true series `fee_type`/`fee_multiplier` is **BLOCKED** until the Archivist fee/account manifest holds Collector-fetched series-endpoint values for `KXHOUSERACE` and every Amendment A legacy series. The illustrative `0.07·p·(1−p)` remains a **labeled sensitivity only** and **must not** fire the early-narrowing flag (§7).
- **Rails / freshness:** R1-P5 @ `6a28e0d6254327ea4e6451c781bec56215ac6cac` wherever fee/freshness labels appear on extracts.
- **ElectIndex:** APPROVED_HASH_ONLY. Receipt time = Collector receipt. No backdating from `output/historical/`. Methodology regime monitoring remains under Amendment B (b) / Archivist pin extension (out of scope to execute here).

## 5. One knob: snapshot cadence

| Level | Role |
|---|---|
| **`weekly`** | **Headline.** Snapshot times below. |
| `twice_weekly` | Comparator level of the same knob (Mon+Thu 22:00Z). **Not collected unless Conductor selects this level at ACCEPT.** |

**Justification:** Cadence is the single design choice that most affects (a) Collector GET budget under Addendum 1, (b) lead time for the early-narrowing flag, and (c) whether disagreement is sampled densely enough to be actionable. Depth horizon and gate-count threshold are **fixed** below so they are not second knobs.

**All other settings fixed:** universe, w = 0.5, entry gate, gap definitions, dense-window schedule, gate-count threshold family, M1/M2/M3 reporting, fee/rails pins.

### Headline weekly snapshot grid (UTC)

Align with NH-002-H Collector dry-run passes so books can be shared, not duplicated:

| Snapshot ID | Target time (UTC) | Role |
|---|---|---|
| W1 | `2026-10-12T22:00:00Z` | NH-002-H dry-run #1; first October census |
| W2 | `2026-10-19T22:00:00Z` | NH-002-H dry-run #2 |
| W3 | `2026-10-26T22:00:00Z` | NH-002-H dry-run #3; last pure-October weekly |
| W4 | `2026-11-02T22:00:00Z` | NH-002-H decision snapshot (shared); decision-week census |

Book window per weekly snapshot: **21:45Z–22:15Z** on that date (same ±15 min rule as NH-002-H). Snapshot nearest 22:00Z used; books older than 15 minutes excluded and logged. Never imputed.

ElectIndex join: latest Collector-received `races_summary.csv` at or before snapshot time, subject to NH-002-H 24 h lag **only when this census is used to preview the decision-time gate**; for pure disagreement charts, also report the zero-lag receipt-at-snapshot extract as a labeled sensitivity (not a second knob — fixed dual report).

### Dense pre-decision book window (fixed; not the knob)

- **Hourly** orderbook GETs for all mapped universe `-D` contracts from **`2026-11-02T22:00:00Z` through `2026-11-04T04:00:00Z`** inclusive (30 hourly marks after the decision snapshot through early Nov 4 UTC).
- Purpose: measure how fast `|p_model−p_mkt|` and touch depth decay around election night (decision-packet Exp-2 / critique (d)).
- If Addendum 1 budget cannot sustain 92×30 books, Collector **thins** (e.g. every 2 h, or M1-only) and logs gaps; gaps are never filled. Thinning is a budget accommodation, not a redesign of this freeze.

## 6. Metrics (all descriptive; unscored as confirmation)

**Per race, per weekly snapshot:**
- `p_model` = ElectIndex `dem_prob`/100 (APPROVED_HASH_ONLY extract).
- `p_mkt` = YES mid = `(bid+ask)/2` when two-sided; else excluded with reason (`one_sided` / `crossed` / `no_book`).
- `gap_abs` = `|p_model − p_mkt|`.
- `gap_logit` = `|logit(clip(p_model)) − logit(clip(p_mkt))|` with clip to `[1e-4, 1−1e-4]`.
- Touch: `yes_bid`, `yes_ask`, `yes_bid_size`, `yes_ask_size` (visible).
- `depth_touch_contracts` = size at the purchased-side price that the NH-002-H taker would hit.
- `mapping_status` ∈ {M1, M2, M3}.
- `gate_pass` ∈ {true, false, `BLOCKED_FEE_UNVERIFIED`, `excluded_<reason>`}.

**Aggregates per snapshot (headline tables):**
- n admitted to gap table; median/IQR `gap_abs` and `gap_logit` overall and by M1/M2; by liquidity tercile of `depth_touch_contracts` when depth exists.
- **`n_gate_pass`:** count of races with `gate_pass = true` (fee-verified path only).
- **`n_gate_pass_illustrative_007`:** same count using fee = `0.07·p·(1−p)` — labeled **ILLUSTRATIVE_NOT_FOR_NARROW**; never feeds §7.
- Share of gap-table races with `depth_touch_contracts < 1`.

**Noise floor for “negligible disagreement” (fixed):** median `gap_abs` ≤ **0.02** (2¢ probability) across admitted races at a snapshot. Used only for usefulness critique (i), not for NH-002-H PASS/REJECT.

**Dense window:** time series of median `gap_abs` and median `depth_touch_contracts` hourly; half-life of median gap from W4 baseline (descriptive).

## 7. Gate-count early-narrowing rule (preregistered before any pull)

**Threshold for “about zero”:** at a weekly snapshot, **`n_gate_pass ≤ 2`** (at most two races in the 92-race universe pass the frozen NH-002-H entry gate under fee-verified evaluation).

**Flag `RECOMMEND_NARROW_FORECAST_QUALITY_ONLY`:** fires iff **`n_gate_pass ≤ 2` on ≥ 2 consecutive weekly snapshots among {W1, W2, W3}** (October dry-runs). W4 is reported but does not enter the consecutive-October trigger (it is the decision snapshot itself).

**Binding fee rule:** if `n_gate_pass` is `BLOCKED_FEE_UNVERIFIED` at a snapshot, that snapshot **does not count** toward the consecutive trigger. The illustrative `n_gate_pass_illustrative_007` **must not** fire the flag. Conductor may still read the illustrative series as soft context.

**Authority:** this freeze only **measures and flags**. Narrowing Card 01 is Conductor’s decision.

## 8. Preregistration (p16 / v1.2 §J checklist)

| # | Item | Declared in |
|---|---|---|
| 1 | Market universe | §4 (92 races; parent universe hash) |
| 2 | Exclusions | Parent §5 decision-time exclusions + M3 reasons; one-sided/crossed books excluded from gap table |
| 3 | Receipt-time information set | §5 weekly grid + dense window; ElectIndex APPROVED_HASH_ONLY; our receipt governs |
| 4 | Fee regime | §4 (R1-P1 pin; gate-count BLOCKED until Archivist manifest; 0.07 sensitivity labeled) |
| 5 | Order timing | Snapshot taker marks only; no orders |
| 6 | Sizing | Inherited NH-002-H one-contract gate for pass/fail count only |
| 7 | Fill model | Visible qty ≥ 1 at purchased-side price (inherited) |
| 8 | Stopping rules | Census ends after dense window completes or 2026-11-04T04:00Z, whichever data exist; no early stop that fills gaps. Flag in §7 may fire earlier as a **recommendation**, not a stop of NH-002-H capture. |
| 9 | Evaluation metrics | §6–§7 (descriptive; not NH-002-H PASS/REJECT) |
| 10 | Limit candidate variants | One knob `snapshot_cadence` ∈ {**weekly**, twice_weekly}. Nothing else. |
| 11 | Log every attempted variant | `packets/card01_exp2_census/LEDGER_2026-09-24.md` |
| 12 | Separate discovery / tuning / untouched evaluation | Discovery: Card 01 decision packet Exp-2 + SOURCE_MAP D1. Tuning: **none** (cadence headline chosen before any Exp-2 pull). Untouched evaluation: N/A for confirmation; census uses only pre-outcome snapshots. |

## 9. Rejection / stop rules (when this census is useless or harmful)

Stop or mark **USELESS** (do not keep pulling under this packet ID) if any of:
- (a) Conductor rejects this freeze, or Archivist refuses ElectIndex APPROVED_HASH_ONLY for the census extracts.
- (b) Mapping remains unresolved for > 50% of races past 2026-10-26 (M3 dominant) so gate-count and depth are not about the intended universe.
- (c) Collector cannot obtain any weekly book pass for W1–W3 under Addendum 1 after documented backoff (census has no October support).
- (d) The packet is used to retune NH-002-H w, universe, decision time, or entry gate — **forbidden**; any such attempt voids *this* packet’s outputs for decision use.

Mark **HARMFUL / do not interpret as confirmation** if:
- (e) Someone treats census gap charts or illustrative gate-counts as NH-002-H PASS/REJECT or as license for live orders.

## 10. Collector handoff (GET list; Deep Research does not call)

**Budget:** route through Collector only. Request ≤ **3 rpm**, ≥ **20 s** spacing, list/series/markets/orderbook public GETs counting inside the weather-archive Phase A slice per Addendum 1. Phase B: pause unless Conductor approves. On 429: honor budget backoff; log; never fill.

**Exact GET asks (after ACCEPT only):**

1. **Reuse / share** NH-002-H ElectIndex daily capture (Archivist pin). Exp-2 does not add ElectIndex GETs; it consumes hash + 92-race `dem_prob` extracts already allowed under APPROVED_HASH_ONLY.
2. **Weekly open-markets pagination** for `KXHOUSERACE` and Amendment A legacy series needed for the 92 mapped `-D` tickers (share with NH-002-H dry-runs at W1–W3 and decision at W4).
3. **Orderbook** `GET /trade-api/v2/markets/<ticker>/orderbook` (or Collector’s equivalent public path) for each mapped universe `-D` ticker inside each weekly 21:45–22:15Z window (≈92 requests/pass).
4. **Dense window:** same orderbook endpoint hourly 2026-11-02T22:00Z–2026-11-04T04:00Z for mapped tickers; thin and gap-log if over budget.
5. **Series fee fields** (if not already landed for Amendment B): `GET /trade-api/v2/series/<T>` for `KXHOUSERACE` + Amendment A legacy list — already requested under Amendment B; Exp-2 depends on that manifest to unblock `n_gate_pass`, and does not duplicate the ask beyond noting the dependency.

**Save paths:**
- Raw Collector landing (Collector-chosen layout OK): `/workspace/lab/astra-capture/card01-exp2-census/` (and/or shared NH-002-H dry-run paths under `/workspace/lab/astra-capture/card01-nh002-house/` with Exp-2 pointers).
- Governance extracts (hashes, dem_prob, book tops, gap/gate tables): `packets/card01_exp2_census/snapshots/<SNAPSHOT_ID>/`.
- Stub / null results: `packets/card01_exp2_census/` (this packet).

**Forbidden:** Deep Research Kalshi GETs; inventing mids/depths; backfilling missed hours; substituting another forecast source; scoring NH-002-H from these tables.

## 11. Dead-card / live-pin overlap

| Card | Overlap | Handling |
|---|---|---|
| **FEAT-20260912-001 / -002 (F1), TEST-20260912-002** | Nearest dead card: model/market blend over Kalshi mid failed REDUNDANT/FAIL-INSUFFICIENT. | Same blend *form* warning as NH-002-H; this census does not re-test F1. Named only. |
| **NH-002-H + Amendments A/B** | Parent. Shared universe, gate, dry-run times, ElectIndex pin. | **Complementary measurement**, not duplicate scoring. No change to NH-002-H PASS/REJECT. |
| Q6-`000` | None | Orthogonal; not retuned |
| C3 / Card 02 station weather | None | Orthogonal |
| S2 / R2-P4 | None | Remain gated |

## 12. Mandatory instrument pins

| Dep | Pin |
|---|---|
| Fee | R1-P1 `kalshi_feebook_lab_20260922/` @ `22371178cb2663250b4762f328069571c48cb551` |
| Rails | R1-P5 `kalshi_rails_lab_20260922/` @ `6a28e0d6254327ea4e6451c781bec56215ac6cac` |
| Parent NH-002-H | freeze `c31724463d81747702910a2d5296c2fc21d2a1dbc594727b26ac3d894b55ec59` + A `4e36d0db5728148d5bb4688fd8626eca9907a8933747f85e0bc17ede0ac0936b` + B `ee6af37cef95f1e468d28e5b06750caaca8b1706ec11ed5cf5cdce460524c2c6`; national-miss script `049368f942741ff4a63acad328a49ff256252587d6c65f1e7e6d65d6101781f2` |
| Predecessor (context only) | `17thgreen/GPT-6-Astra-Deathmatch` @ `2253c03cd86eb5515325f1d91b43bdcbea7a902c` |
| Charter | v1.1 `02272754b01da5b65edd837545e485f4fd4dff2903a7ae1f52d9cb5e616fec5d` |
| Universe | `d8af74515e449b151016105f956c5e54a4fb4eac3ec570364da58f8fe47d8ca6` |

## 13. Do-not-modify

1. No live orders; results/pnl stay null.
2. Do not pull data before Conductor ACCEPT of **this** freeze.
3. Do not alter NH-002-H universe, w, decision time, entry gate, or Amendments A/B.
4. Do not treat census outputs as NH-002-H confirmation.
5. Do not fire early-narrowing on illustrative 0.07 fee counts.
6. Do not issue Kalshi GETs from Deep Research.
7. No imputation / gap fills.

## 14. Empty results (on disk)

`packets/card01_exp2_census/FROZEN_EXPERIMENT.json`, `results.json`, `results/EMPTY_RESULTS.json` (NOT_RUN).

## 15. Done =

Freeze kernel + stubs + ACK one-pager on disk with sha256s. Then: Conductor ACCEPT → Collector capture under Addendum 1 → descriptive tables only → Conductor reads §7 flag if any.

## Frozen-at

`2026-09-25T00:24:00Z` UTC (2026-09-24 20:24 ET). Deep Research, under charter v1.1 `02272754…`.
