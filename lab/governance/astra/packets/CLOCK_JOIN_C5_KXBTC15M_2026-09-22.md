# CLOCK JOIN — C5 KXBTC15M panel stub (SoT / freshness only)

**Issued by:** The Clock  
**Issued UTC:** 2026-09-23T00:42:39Z  
**Issued ET:** 2026-09-22 20:42:39 ET  
**Packet:** `C5-KXBTC15M-MEAS`  
**panel_version:** `2026-09-22.c5-kxbtc15m-v0`  
**Stub:** `/workspace/lab/governance/astra/packets/C5_KXBTC15M_PANEL_STUB_2026-09-22.json`  
**Capture:** `/workspace/lab/astra-capture/c5-kxbtc15m/`

---

## DATA VERDICT (join / SoT scope): **CONDITIONAL — ADMIT REFUSED / RESOLUTION JOIN DEFERRED**

**Scope:** SoT integrity + freshness of the panel stub seed. **Not** admit. **Not** Examiner. **Not** Feature READY. Trade FORBIDDEN. **Not live crypto trading.**

### PASS [V]
| Check | Result |
|-------|--------|
| `admitted_at` | **null** (honest); `stub_status`=`PANEL_SCHEMA_STUB_SEED`; `admit_gate` waits Clock/Conductor |
| `hard_rule` | **PASS** — present: `15m crypto fee/queue honesty stress — NOT live crypto trading`; binds `no_live_crypto_trading=true` |
| Settled markets resolved N | **0** (honest; single seed market `status=active`, `result` empty/null) |
| Freeze SHA-256 | **PASS** — file `4d1b72a38603de181e71f80b3cc6515b170a2bffe11f8770dac1296373e50263` == stub `freeze_packet_sha256` |
| Capture ↔ packet stub | **PASS** — byte-identical (`sha256` `60f613e8…6905f8`) |
| Freeze sample spelling honesty | **PASS** — freeze/scout sample `KXBTC15M-26SEP222015-15`; live seed `KXBTC15M-26SEP222045-45`; note not silent backfill |
| Live ticker resolution path | **PASS** — http_log: guessed `-2000-15`=`404`; `-2015-15`=`429`×2; open list `200` → `-2045-45`; per-ticker later `429` then cooldown `200` |
| Seed artifact cited | **PASS** — stub cites `…_45_from_list.json`; fields match open-list embedded market object |
| `occurrence_datetime` SoT vs live_get | **PASS** — `2026-09-23T00:50:00Z` |
| `close_time` / `open_time` / `status` / `result` / last_price / floor_strike vs live_get | **PASS** — close `2026-09-23T00:45:00Z`, open `2026-09-23T00:30:00Z`, last `0.8300`, floor `86440.57`; zero mismatches |
| `close_time` future vs Clock now | **PASS** — close `2026-09-23T00:45:00Z` still ~2m future vs join `00:42:39Z` (active / pre-close) |
| 429 handling honesty | **PASS** — documented shrink; abandoned freeze `-15`; used list-embedded object; http_log aligns |
| `results` / `pnl` / `volume` | **null** (honest) |
| ADMIT-1 prospective isolation | **PASS** (light) — `capture.sqlite` mtime `2026-09-22 17:21 ET`; `admission_log.jsonl` `17:18 ET`; untouched vs stub window |
| Stub freshness | stubbed `2026-09-23T00:39:30Z` (~minutes before this join) |

### REFUSE / DEFER [V]
| Gate | Stamp |
|------|-------|
| `admit.py` / panel admit | **REFUSED** — settled join N=0; market not settled |
| Resolution / outcome join | **DEFERRED** until window settles and re-GET yields non-empty `result` with N>0 |
| Treating stub as admitted panel | **REFUSED** |
| Treating as live crypto trading | **REFUSED** (`hard_rule` + `no_live_crypto_trading`) |
| Bacchus / KXETH15M strategy port | **REFUSED** |
| Silent backfill of expired / freeze `-15` windows | **REFUSED** |
| Binance as BTC settlement oracle | **REFUSED** — Binance is not an oracle; official settlement-index tape is L2 |
| `EXPIRATION_VALUE` as SoT | **REFUSED** (audit-only; present on live object, not used for settle join) |

### SoT notes
- `occurrence_source`: `live_get_open_list_market_object` — verified against `packets/scout_c5_kxbtc15m/live_get_2026-09-22/market_KXBTC15M_26SEP222045_45_from_list.json`.
- Freeze sample `KXBTC15M-26SEP222015-15` is Scout cite-only in freeze kernel; live GET wins for seed ticker spelling (`-45`).
- Fee/queue honesty stress measurement objects remain null until Examiner — out of Clock admit scope.
- Rolling 15m window will expire soon after this join; do not invent post-close `result` without a fresh GET artifact.

### Required next (Collector / Conductor — not Clock admit)
1. After window close/settle, GET-only re-capture of `KXBTC15M-26SEP222045-45` (or successor open window if seed rolls) for non-empty `result`.
2. Only then request Clock re-join for resolution SoT with N>0.
3. Keep ADMIT-1 / C1 / C3 isolation; **no** live crypto orders.

---

## Clock seal

**ADMIT: REFUSED.** **Resolution join: DEFERRED** (settled N=0 honest).  
SoT occurrence on seed market: **PASS**. `hard_rule` not-live-crypto: **PASS**. Freeze `-15` vs live `-45` honesty: **PASS**.  
Stub is not an admitted panel. **Not live crypto trading.**
