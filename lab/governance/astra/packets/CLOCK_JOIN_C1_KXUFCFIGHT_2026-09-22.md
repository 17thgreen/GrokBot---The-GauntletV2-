# CLOCK JOIN — C1 KXUFCFIGHT panel stub (SoT / freshness only)

**Issued by:** The Clock  
**Issued UTC:** 2026-09-23T00:42:39Z  
**Issued ET:** 2026-09-22 20:42:39 ET  
**Packet:** `C1-KXUFCFIGHT-MEAS`  
**panel_version:** `2026-09-22.c1-kxufcfight-v0`  
**Stub:** `/workspace/lab/governance/astra/packets/C1_KXUFCFIGHT_PANEL_STUB_2026-09-22.json`  
**Capture:** `/workspace/lab/astra-capture/c1-kxufcfight/`

---

## DATA VERDICT (join / SoT scope): **CONDITIONAL — ADMIT REFUSED / RESOLUTION SoT PASS (settled N=2); active legs DEFERRED**

**Scope:** SoT integrity + freshness of the panel stub seed. **Not** admit. **Not** Examiner. **Not** Feature READY. Trade FORBIDDEN.

### PASS [V]
| Check | Result |
|-------|--------|
| `admitted_at` | **null** (honest); `stub_status`=`PANEL_SCHEMA_STUB_SEED`; `admit_gate` waits Clock/Conductor |
| Settled / finalized with non-empty `result` N | **2** — `KXUFCFIGHT-26SEP22CONGUA-GUA`=`yes`, `-CON`=`no` (live_get matched; not invented) |
| Active / empty-result N | **2** — `KXUFCFIGHT-26SEP22DEGMOR-MOR`, `-DEG` (`result` empty; pre-settlement) |
| Freeze SHA-256 | **PASS** — file `a191c9b3f71030445d1d32684feb6dc1bf09abb7e09403d5dbdf1927eafc63c9` == stub `freeze_packet_sha256` |
| Capture ↔ packet stub | **PASS** — byte-identical (`sha256` `2cc661d8…c81a00`) |
| `occurrence_datetime` SoT vs live_get | **PASS** — CONGUA both `2026-09-23T04:20:00Z`; DEGMOR both `2026-09-23T04:40:00Z` |
| `close_time` / `status` / `result` / last_price vs live_get | **PASS** — all 4 seed tickers; zero field mismatches |
| `close_time` vs Clock now | **PASS** — CONGUA close `2026-09-23T00:04:31Z` past (finalized); DEGMOR close `2026-10-06T23:40:00Z` still future |
| ORTDAS drop honesty | **PASS** — http_log: ORT `429`×2; DAS `200` unpaired; stub `dropped_from_seed` matches |
| 429 handling honesty | **PASS** — series first `429`→retry `200`; open list `429`; seed shrunk; http_log aligns |
| `results` / `pnl` / `volume` | **null** (honest) |
| ADMIT-1 prospective isolation | **PASS** (light) — `capture.sqlite` mtime `2026-09-22 17:21 ET`; `admission_log.jsonl` `17:18 ET`; untouched vs stub window |
| Stub freshness | stubbed `2026-09-23T00:33:00Z` (~minutes before this join) |

### REFUSE / DEFER [V]
| Gate | Stamp |
|------|-------|
| `admit.py` / panel admit | **REFUSED** — Clock does not admit; mixed panel (2 finalized + 2 active); measurement objects null |
| Full-panel resolution / outcome join | **DEFERRED** for DEGMOR active legs until they settle with real non-empty `result` |
| Treating stub as admitted panel | **REFUSED** |
| Backfill / invent ORTDAS or other tickers | **REFUSED** (ORT 429; honest shrink) |
| Binance / non-L2 as settlement oracle | **REFUSED** — official settlement-index tape is L2; fight `result` here is Kalshi public GET artifact only |
| `EXPIRATION_VALUE` as SoT | **REFUSED** (audit-only if present) |

### SoT notes
- `occurrence_source`: `live_get_market` — verified against `packets/scout_c1_kxufcfight/live_get_2026-09-22/market_KXUFCFIGHT_*.json` for all four seed tickers.
- Settled-result SoT [V]: CONGUA-GUA `result=yes`, CONGUA-CON `result=no` match live GET artifacts exactly; `settlement_ts` remains null in stub (not invented).
- Fee+queue honesty bakeoff / measurement shells remain null until Examiner — out of Clock admit scope.
- Cohort after honest shrink: markets_n=4; dropped ORTDAS pair.

### Required next (Collector / Conductor — not Clock admit)
1. Hold DEGMOR active legs; re-GET when finalized if resolution join for full panel is requested.
2. Do **not** run `admit.py` from this join alone — Conductor gate still owns admit.
3. Keep ADMIT-1 / C3 / C5 / PIT@CLE budget isolation.

---

## Clock seal

**ADMIT: REFUSED.** **Settled-result SoT: PASS (N=2 CONGUA).** **Active-leg resolution: DEFERRED (DEGMOR).**  
SoT occurrence + close/status/result on seed markets: **PASS**.  
Stub is not an admitted panel.
