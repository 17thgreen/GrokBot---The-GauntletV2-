# ORACLE RECON — CF Benchmarks BRTI / ETHUSDRTI (F2)
**Document:** `ORACLE_RECON_CF_BRTI_2026-09-12.md`  
**Date (UTC):** 2026-09-12  
**Authority:** Feature Wave 001 data support · JOB A (no purchase)  
**Target window:** 2026-09-04 → 2026-09-11 UTC · resolution 1s or 1m  
**Kalshi settlement oracle (from DATA-PROV-PM-001 / Track B §1.4):** CF Benchmarks **BRTI** (BTC) / **ETHUSDRTI** / CF id **ETHUSD_RTI** (ETH); method = simple average of **60×1s** RTI prints in the last minute before window start vs end  
**Non-goals:** purchase · inventing API keys · treating Binance as settlement oracle · downloading full history · Examiner numbers · trading

---

## Verdict

| Item | Result |
|------|--------|
| Free public historical archive (1s/1m) covering window? | **NO** `[V]` |
| Independent L2 replay feasible without secrets? | **NO** |
| **JOB A status** | **BLOCKED** |
| Sample downloaded? | **None** (no free archive to sample) |
| F2 DATA-BLOCKED lifted? | **No** — remains DATA-BLOCKED pending licensed/auth path |

---

## Endpoints discovered `[V]`

| Path | URL / channel | Auth | Historical 2026-09-04→11? |
|------|---------------|------|---------------------------|
| CF Benchmarks REST live values | `GET https://www.cfbenchmarks.com/api/v1/values?id={BRTI\|ETHUSD_RTI}` | **Licensed / credentialed** (unauth → HTTP 400 `"Unknown id"` for all probed ids) | N/A without auth |
| CF Benchmarks REST history | `GET https://www.cfbenchmarks.com/api/v1/history/values?id=…&timespan=…&timestamp=…` | Requires authorization for index **and** `STREAM_HISTORICAL_VALUES` (CF docs) | Yes **if** entitled — **not** free |
| CF Benchmarks public index pages | `https://www.cfbenchmarks.com/data/indices/BRTI` · `…/ETHUSD_RTI` | None for **marketing page** (shows current print only) | **No** downloadable history |
| Kalshi CF REST passthrough | `GET https://external-api.kalshi.com/trade-api/v2/cfbenchmarks/values?id=BRTI` · `…/cfbenchmarks/history/values?…` | **Kalshi API key + RSA-PSS signature** + entitlement | Forwards to CF `/api/v1/…`; docs show history example with `timespan=HOUR` |
| Kalshi CF WebSocket | `cfbenchmarks_value` channel | **Authenticated**; live (+ trailing 60s / quarter-hour averages per docs) | Live / forward — **not** a multi-day historical archive |
| CME streaming web service | CME Client Systems Wiki “24-7 CME CF Cryptocurrency Indices” | CME-assigned username/password (HTTP Basic); `seek` limited to **past 24 hours** | **Not** multi-day free archive |
| CME DataMine / MDP | CME commercial market-data products | Paid / licensed | Commercial |
| FirstRateData (third party) | `firstratedata.com` lists BRTI in US Indices Bundle | **Paid** download product | Paid; not free public |
| Licensing contact | `licensing@cfbenchmarks.com` (stated on CF index pages) | Commercial license | Required for product/historic use per CF |

**Index ID note:** Kalshi rules / PM-001 `ORACLE.index` use **ETHUSDRTI**; CF Benchmarks / Kalshi WS docs use **ETHUSD_RTI**. Treat as the same ETH RTI family; confirm id string with the licensed feed before any replay.

---

## Auth `[V]`

- **No free anonymous path** returned historical BRTI/ETHUSD_RTI prints for the target window.
- Unauthenticated probes 2026-09-12:
  - CF `/api/v1/values?id=BRTI|ETHUSD_RTI|ETHUSDRTI|BRR|…` → **HTTP 400** `{"error":"Unknown id"}` (ids not even acknowledged without credentials).
  - Kalshi `/trade-api/v2/cfbenchmarks/values?id=BRTI` (elections + external hosts) → **HTTP 401** `token_authentication_failure`.
- Kalshi docs: passthrough “requires an authenticated Kalshi Trade API request” and “appropriate entitlement.”
- CF docs: historical values require user authorized for the index and `STREAM_HISTORICAL_VALUES`; recent values may lag up to ~15 minutes.
- **No keys invented. No purchase. STOP on paid/auth-only path.**

---

## Coverage vs Feature Wave window

| Need | Status |
|------|--------|
| 2026-09-04 → 2026-09-11 UTC | **Unavailable** on free public path |
| 1-second RTI prints (for exact 60s average replay) | Documented on licensed CF/Kalshi channels; **not** free |
| 1-minute aggregates | Not found as free public CF archive; paid third parties advertise 1m bars |
| Independent recompute of Kalshi `floor_strike` / `expiration_value` | **Not feasible** without licensed feed |

Venue-provided labels (`result`, `floor_strike`, `expiration_value` on settled markets) remain available via **public** Kalshi market APIs (DATA-PROV-PM-001) — that is **L1 resolution label**, not independent L2 oracle replay.

---

## Independent replay feasible?

**No** under Wave 001 JOB A constraints (no purchase, no invented keys).

To lift F2 DATA-BLOCKED, Governor would need to authorize **one** of:

1. Kalshi API credentials **with CF passthrough entitlement**, then bounded `history/values` pulls for BRTI + ETHUSD_RTI over the window; or  
2. Direct CF Benchmarks license / API credentials (`STREAM_HISTORICAL_VALUES`); or  
3. CME commercial DataMine/MDP (or other licensed redistributor) under lab licensing review.

Until then: **do not** substitute Binance (or any L3 spot/perp) as the Kalshi settlement oracle.

---

## Blockers

| ID | Blocker | Impact |
|----|---------|--------|
| O1 | CF REST history requires license / `STREAM_HISTORICAL_VALUES` | Hard block on free independent replay |
| O2 | Kalshi CF passthrough + WS require API key + entitlement | Hard block without secrets vault / Governor-provisioned key |
| O3 | CME stream `seek` ≤ 24h; DataMine paid | No free multi-day archive |
| O4 | Third-party BRTI bars (e.g. FirstRateData) are paid | Out of scope (no purchase) |
| O5 | No free public CSV/NDJSON dump found for BRTI/ETHUSDRTI covering 2026-09-04→11 | Nothing to sample |

Soft / non-blockers for *other* work: Kalshi public settled-market fields still supply resolution labels without L2 replay (Track B B5-class for oracle audit only).

---

## Licensing `[V]` / `[A]`

- CF Benchmarks index pages: real-time or historic data for product/service use → contact **licensing@cfbenchmarks.com**.
- BRTI / ETHUSD_RTI are regulated UK BMR benchmarks; redistribution typically restricted.
- Kalshi passthrough does **not** remove upstream licensing — it only reuses Kalshi credentials for entitled accounts.
- Lab rule this job: **no purchase**; therefore licensing path = **BLOCKED**, escalate to Governor if F2 must proceed.

---

## Sample policy

Per job brief: *If a free public archive exists, do NOT download the full history yet — sample 1–2 windows and report.*  

**No free public archive found → no sample downloaded → stop.**

---

## Explicit non-substitutes (Wave 001)

| Source | Role |
|--------|------|
| Binance Vision / API OHLCV (DATA-PROV-L3-001) | **L3 external predictor only** — NOT settlement oracle |
| PM-001 `EXPIRATION_VALUE` / terminal last | **Forbidden** as decision-time feature (leakage) |
| Kalshi `result` | Resolution **label** (L1), not independent oracle tape |

---

## Source checklist (reproducible)

| Check | Result | Tag |
|-------|--------|-----|
| CF `/api/v1/values?id=BRTI` unauth | 400 Unknown id | `[V]` |
| CF `/api/v1/values?id=ETHUSD_RTI` unauth | 400 Unknown id | `[V]` |
| Kalshi CF passthrough unauth | 401 | `[V]` |
| Kalshi docs REST passthrough + history | Auth + entitlement required; history example documented | `[V]` |
| CF docs historical-values | Auth + STREAM_HISTORICAL_VALUES | `[V]` docs |
| CF public BRTI page | Current print; licensing CTA; no free hist dump | `[V]` |
| CME 24/7 stream wiki | Basic auth; seek ≤24h | `[V]` docs |
| Free BRTI CSV archive search | None found; paid vendors only | `[V]`/`[U]` completeness of web search |
| API keys created | **No** | `[V]` |
| Purchase / download full hist | **No** | `[V]` |

---

## Bottom line for Conductor / F2

**BLOCKED.** Independent CF BRTI / ETHUSDRTI historical replay for 2026-09-04→11 UTC is **not** available on a free public path. F2 remains DATA-BLOCKED. Cards may stay HYPOTHESIS with DATA requirement; **no Examiner** until Clock clears a licensed oracle DATA-*. Do **not** treat Binance L3 as the oracle.

*End ORACLE_RECON_CF_BRTI_2026-09-12 — JOB A.*
