# CLOCK RE-JOIN — C1 KXUFCFIGHT panel (SoT / freshness / admit-conditions)

**Issued by:** The Clock  
**Issued UTC:** 2026-09-23T00:48:28Z  
**Issued ET:** 2026-09-22 20:48:28 EDT  
**Packet:** `C1-KXUFCFIGHT-MEAS`  
**panel_version:** `2026-09-22.c1-kxufcfight-v0`  
**Supersedes (join only):** `CLOCK_JOIN_C1_KXUFCFIGHT_2026-09-22.md` (prior: ADMIT REFUSED; settled N=2; DEGMOR DEFERRED)  
**Stub:** `/workspace/lab/governance/astra/packets/C1_KXUFCFIGHT_PANEL_STUB_2026-09-22.json`  
**Capture stub:** `/workspace/lab/astra-capture/c1-kxufcfight/panel_stub.json`  
**Resolution latest:** `/workspace/lab/astra-capture/c1-kxufcfight/resolutions/CONGUA_resolution_rows_latest.json`  
**live_get:** `/workspace/lab/governance/astra/packets/scout_c1_kxufcfight/live_get_2026-09-22/`

---

## DATA VERDICT (re-join / SoT scope): **CLEARED — ADMIT CONDITIONS MET (C1 UFC panel only) / ADMIT PASS (conditions)**

**Scope:** Independent SoT + freshness re-join after Conductor claim both CONGUA and DEGMOR finalized. **Clock stamps admit-conditions only** — does **not** run `admit.py`; does **not** write `admitted_at`. **Not** Examiner. **Not** Feature READY. Trade FORBIDDEN. Lee-Ready: **REFUSED**.

Settled / finalized with real non-empty `result` **N=4** (full panel). Resolution JSON contains **both** CONGUA and DEGMOR rows despite CONGUA-prefixed filename [V].

### PASS [V]
| Check | Result |
|-------|--------|
| Resolution latest contains CONGUA+DEGMOR | **PASS** — labels GUA, CON, MOR, DEG; `settled_n_congua=2`, `degmor_finalized_n=2`, `degmor_still_active=false`; sha256 `108576b05b40c035fa2f5366547688d4fb357faa0e22bec51bd16b8c02d7b522` == dated `…004604Z.json` |
| DEGMOR actually in resolution JSON | **YES [V]** — MOR+DEG rows present with `status=finalized` and real results |
| Settled N (full panel) | **4** — all seed markets finalized with non-empty result |
| Per-market result SoT vs resfresh live_get | **PASS** — see table below; resolution file sha cites match on-disk artifacts |
| `occurrence_datetime` SoT | **PASS** — CONGUA both `2026-09-23T04:20:00Z`; DEGMOR both `2026-09-23T04:40:00Z` (stub == live_get) |
| Stub `result` / `status_observed` / `settlement_ts` | **PASS** — all 4 match resolution + resfresh |
| Freeze SHA-256 | **PASS** — file `a191c9b3f71030445d1d32684feb6dc1bf09abb7e09403d5dbdf1927eafc63c9` == stub `freeze_packet_sha256` == claimed |
| Capture ↔ packet stub | **PASS** — byte-identical sha256 `cba203955686478f252117b2a63be24583a1408f3191227a1fcfb3a4a888b555` |
| `admitted_at` | **null** (honest; Clock did not write it) |
| `results` / `pnl` / `volume` panel fields | **null** (honest) — resolution admit-eligibility ≠ measurement completeness |
| measurement_objects (`reciprocal_book`, fee channel, rails, bakeoff) | **null** (Examiner/Simulator) — does not block resolution SoT admit-conditions |
| ORTDAS dropped | **PASS** — not in `markets[]`; `dropped_from_seed` retains ORT 429 / DAS unpaired |
| ADMIT-1 prospective isolation | **PASS** (light) — `prospective/` panel+sqlite+admission_log mtimes still `2026-09-22 17:09–17:24 ET`; Clock did not mutate. Log `prospective_record_20260922T212153Z.log` mtime `20:46 ET` is poll heartbeat only (`active_markets: 0`), not C1 write |
| Stub freshness vs resolution capture | resolution_capture `2026-09-23T00:46:05Z`; re-join minutes later |

### Per-market result table [V]
| Ticker | status (live) | result | settlement_ts | close_time (live/res) | occurrence | stub result match |
|--------|---------------|--------|---------------|----------------------|------------|-------------------|
| `KXUFCFIGHT-26SEP22CONGUA-GUA` | finalized | **yes** | `2026-09-23T00:10:28.225265Z` | `2026-09-23T00:04:31Z` | `2026-09-23T04:20:00Z` | yes |
| `KXUFCFIGHT-26SEP22CONGUA-CON` | finalized | **no** | `2026-09-23T00:10:28.225265Z` | `2026-09-23T00:04:31Z` | `2026-09-23T04:20:00Z` | yes |
| `KXUFCFIGHT-26SEP22DEGMOR-DEG` | finalized | **yes** | `2026-09-23T00:36:08.238225Z` | `2026-09-23T00:30:04Z` | `2026-09-23T04:40:00Z` | yes |
| `KXUFCFIGHT-26SEP22DEGMOR-MOR` | finalized | **no** | `2026-09-23T00:36:08.238225Z` | `2026-09-23T00:30:04Z` | `2026-09-23T04:40:00Z` | yes |

Resfresh artifacts [V]: GUA/CON/MOR `…_resfresh_20260923T004449Z.json`; DEG `…_resfresh_20260923T004604Z.json` (earlier DEG `004449Z` was 68-byte 429 stub — not used as SoT).

### REFUSE / DEFER [V]
| Gate | Stamp |
|------|-------|
| Lee-Ready | **REFUSED** always on this panel |
| Clock runs `admit.py` / writes `admitted_at` | **REFUSED** — Collector/Conductor owns admit execution; `admitted_at` remains null until they run it |
| Treating this seal as panel already admitted | **REFUSED** — conditions met only |
| Invented results / pnl / volume | **REFUSED** — panel `results`/`pnl`/`volume` stay null |
| Backfill ORTDAS | **REFUSED** — remains dropped |
| Binance / non-L2 settlement oracle | **REFUSED** |
| `EXPIRATION_VALUE` as SoT | **REFUSED** |
| Measurement completeness / Examiner scorecard | **DEFERRED** — objects null; distinct from resolution admit-eligibility |
| DEGMOR stub `close_time` field hygiene | **NOTE / patch before or with admit** — stub still has `2026-10-06T23:40:00Z` (= live `expiration_time`); resfresh close is `2026-09-23T00:30:04Z`. `status_at_stub=active` + cohort note "DEGMOR active" are historical stub-era strings; `status_observed=finalized` + results are current SoT. **Does not void result SoT PASS**; Collector should align stub `close_time` to resfresh on admit write |

### SoT notes
- Filename `CONGUA_resolution_rows_latest.json` is misleading; contents are full 4-market capture (CONGUA+DEGMOR) [V]. Purpose string still says `resolution_row_capture_CONGUA_only_pre_admit` — stale label; counts contradict (`degmor_finalized_n=2`).
- Occurrence SoT: `kalshi_occurrence_datetime` via live_get_market — CONGUA `2026-09-23T04:20:00Z` (00:20 ET); DEGMOR `2026-09-23T04:40:00Z` (00:40 ET).
- Raw `volume_fp` / OI exist on live_get/resolution rows; panel stub `volume_fp`/`open_interest_fp` remain **null** (honest; not copied into panel metrics).
- Prior join settled N=2 + DEGMOR DEFERRED is superseded by this re-join (N=4).

### Required next (Collector / Conductor — not Clock admit)
1. **Eligible:** Collector may run `admit.py` for **C1 UFC panel only** after this seal (full-panel scope; CONGUA-only partial no longer required).
2. Patch DEGMOR stub `close_time` → `2026-09-23T00:30:04Z` (and refresh cohort/status notes) when writing admit; keep `admitted_at` null until admit succeeds.
3. Do **not** invent panel `results`/`pnl`/`volume`; Examiner owns measurement objects.
4. Keep ADMIT-1 / C3 / C5 / PIT@CLE budget isolation; Lee-Ready remains refused.
5. ORTDAS stays dropped.

---

## Clock seal

**ADMIT PASS (conditions) — ADMIT CONDITIONS MET (C1 UFC panel only).**  
Settled-result SoT: **PASS (N=4)** — CONGUA GUA=yes/CON=no; DEGMOR DEG=yes/MOR=no.  
Lee-Ready: **REFUSED**. `admitted_at`: **null** (Clock did not admit).  
Clock does **not** run `admit.py`; Collector may admit after this seal.
