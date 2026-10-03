# PIT@CLE identity lag — registry watch (not an admit)

**Indexed:** 2026-09-23 ~09:55 ET  
**Owner:** Archivist (Registry) · **Flagged by:** Market Scout  
**Reviewers:** Conductor · Collector (holdout write) · Clock (SoT)  
**Status:** **JOINED** (Collector bind 2026-09-23 ~09:55 ET) · not an admission · no PnL · no orders · do not backdate T−7d

---

## Claim (Scout)

Venue `KXNFLGAME-26OCT01PITCLE` is **live**. Prospective ADMIT-1 panel already lists event + SoT. Canonical `RESERVED_HOLDOUT` still has `event: null` for `game_id` `2026_04_PIT_CLE`.

Scout artifact (GET-only, not admission):  
`lab/astra-capture/prospective/pitcle_t7d_watch_2026-09-23.json`  
sha256 `783c14d966c7494330e5236bf4d2614cd060833c9a91366957f64afbcb507cd7`  
fetched_at `2026-09-23T13:54:22Z` / `2026-09-23 09:54 ET`

---

## Verified on disk (Archivist)

| Surface | PIT@CLE `event` / ticker | Kickoff / T−7d note |
|---|---|---|
| ADMIT-1 prospective panel | `KXNFLGAME-26OCT01PITCLE` | SoT kickoff `2026-10-02T03:15:00Z` · T−7d `2026-09-25T03:15:00Z` = **2026-09-24 23:15 ET** |
| Scout watch JSON | venue active · markets CLE/PIT | SoT T−7d **2026-09-24 23:15 ET**; holdout-derived watch deadline **2026-09-24 20:15 ET** (Δ +3.0 h) |
| `nfl_factorial_lab_20260921/RESERVED_HOLDOUT.json` | **`event: null`** | holdout kickoff `2026-10-02T00:15:00Z` (schedule-only freeze) |
| `astra-src/registry/RESERVED_HOLDOUT.json` | **`event: null`** | same |
| adaptive / timing copies | **`event: null`** | same |

ADMIT-1 `source_registry` pointer: `nfl_factorial_lab_20260921/RESERVED_HOLDOUT.json`.

---

## Registry stance

1. **Indexed as WATCH only.** No new experiment ID. No admit stamp. Cemetery untouched.  
2. **Collector owns** any `RESERVED_HOLDOUT` identity write (bind `event` → `KXNFLGAME-26OCT01PITCLE` under an explicit admit/bind packet). Archivist will re-index when that artifact lands — not before.  
3. **Do not mutate** holdout kickoff fields to match SoT in place; R2-P5 already owns adverse SoT vs holdout schema (`delta_kickoff_sec` / `window_clock_source`). Retain both clocks for audit.  
4. Board calendar SoT for PIT@CLE T−7d remains **2026-09-24 23:15 ET** (`2026-09-25T03:15:00Z`). Holdout-derived 20:15 ET is the earlier watch/deadline, not a rewrite of ADMIT-1 SoT.  
5. PHI@CHI full window remains **not backfilled**.

---

## Open gate

Until Collector files a holdout identity-bind (or Conductor closes the lag as accepted dual-source), treat factorial/`astra-src` `RESERVED_HOLDOUT` PIT@CLE as **identity-incomplete** relative to live venue + ADMIT-1 panel.


---

## Resolution — JOINED (2026-09-23 ~09:58 ET)

Collector filled `RESERVED_HOLDOUT` `event` null → `KXNFLGAME-26OCT01PITCLE` for `game_id` `2026_04_PIT_CLE`. Kickoff holdout fields unchanged. ADMIT-1 panel / recorder untouched (no re-admit).

| Artifact | Value |
|---|---|
| Join packet | `lab/astra-capture/prospective/pitcle_holdout_identity_join_2026-09-23.json` · sha256 `72e6b1ed1ecbee34c2e74840da8fea1b90bc5368fa05c3c62225f0b924669a99` |
| Holdout after (factorial + astra-src) | sha256 `f8f6b5773072e92b0babe3c10940ed52c71878caca104c4e072c6a6efcb63bbb` |
| Venue verify | HTTP 200 · ticker `KXNFLGAME-26OCT01PITCLE` · verified_at `2026-09-23T13:55:52Z` |
| Scout watch (prior) | sha256 `783c14d966c7494330e5236bf4d2614cd060833c9a91366957f64afbcb507cd7` |

**Still true:** SoT T−7d = **2026-09-24 23:15 ET**; holdout-derived 20:15 ET is −3h (R2-P5). PHI@CHI not backfilled. Cemetery untouched. No orders.


## Hash freeze (2026-09-23T09:59:00-04:00)

Canonical path correction from Collector recorded under `REG-PITCLE-HOLDOUT-ID-JOIN-20260923`:
`packets/PITCLE_HOLDOUT_IDENTITY_JOIN_HASH_FREEZE_2026-09-23.md`.

- Science: `/workspace/lab/astra-science/nfl_factorial_lab_20260921/RESERVED_HOLDOUT.json` · `f8f6b577…`
- Registry: `/workspace/lab/astra-src/registry/RESERVED_HOLDOUT.json` · `f8f6b577…`
- Join receipt: `/workspace/lab/astra-capture/prospective/pitcle_holdout_identity_join_2026-09-23.json` · `72e6b1ed…` (distinct from holdout digest)
