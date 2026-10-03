# Scout sports / microstructure screen vs Q6-000
**Seat:** Market Scout (executor / Astra-Kalshi)  
**Timestamp:** **2026-09-25 00:00 ET** (America/New_York, UTC−4)  
**Mode:** Conductor maximize-next after Card 06 company-KPI ACCEPT (freeze `1413603c…`). Card 06 open-window differentiator **CLOSED this wave**. GET-only · no orders · no invented volume/OI/PnL · no `SHADOW_CANDIDATE_FREEZE` / `000` retune · no Cap-SR / RFQ · no hard `KXNFLSPREAD`/`TOTAL` poll.  
**Hosts:** `https://api.elections.kalshi.com/trade-api/v2` (primary); one `external-api` probe on ANYTD (also 429). `trading-api` skipped. Throttle ~55–90s.  
**Kickoff SoT:** Kalshi `occurrence_datetime` → ET.  
**Freeze:** `packets/scout_sports_q6_screen/FREEZE_SPORTS_Q6_SCREEN_2026-09-24.md` · sha256 `552314d2822f86bf4127be5de03b8d64aa8c16d6c0c81887bdc0cfbd411571df` · freeze_time_ET **2026-09-24 23:46:51 EDT**  
**Raw:** `packets/scout_sports_q6_screen/raw/` + `MANIFEST.sha256`  
**Fee pins:** labeled **cache** from `scout_house_fee_2026-09-24/raw/kalshi/nonstandard_fee_series.json` (live `/series` not polled).  

**Cite prior:** `SCOUT_Q6_STRESS_KERNELS_2026-09-22.md`, `SCOUT_CASHCOW_HUNT_2026-09-22.md`, `SCOUT_R2P3_PROP_SLATE_2026-09-22.md`, `SCOUT_MAXIMIZE_DELTA_2026-09-22.md`, Card 06 ACCEPT / CEM-ASTRA-20260924-006 / company-KPI freeze `1413603c…`.

---

## ≤5 slots (frozen templates → post-freeze inventory)

| ID | Series / structure | Measurement kernel (1 sentence) | Dead-overlap vs Q6-000 | Fee / queue honesty hook | Raw inventory proof (GET 200 page) | Rec |
|---|---|---|---|---|---|---|
| **Q6S1** | `KXATPMATCH` (ATP match ML) | Do tennis match-clock ML books under R1-P1 fee + R1-P5 freshness/queue instruments produce fee-honest completed-net stats that beat/stress `000`’s NFL T−window shadow EV under shared $5k bakeoff? | **Low** — tennis match SoT, not NFL week/T−7d allocator; no pair-router. (Reinforces prior ATP fee/queue harness lane; **not** a cash-cow C* re-nominate.) | Fee **cache:** `quadratic_with_maker_fees` / **1**. Same maker path as NFL game books → clean OOS honesty compare. | **200** · 28 mkts / 14 events · Σ vol≈**3.4828e5** · Σ vol24≈**3.4119e5** · Σ oi≈**3.3057e5** · cursor empty. Samples: `…KOPSHA-SHA` vol24≈39379 oi≈39103 occ→**2026-09-25 06:00 ET**; `…JACETC-ETC` vol24≈38979 oi≈37392 occ→**2026-09-25 04:00 ET**. | **TRY** |
| **Q6S2** | `KXNHLGAME` (NHL game ML) | Does NHL game ML (C2 reinforce/refine) generalize daily-sports maker-fee + queue fragility vs `000` on puck-drop SoT without silently retuning the NFL ML allocator? | **Low** — hockey clock; not NFL ML retune. | Fee **cache:** `quadratic_with_maker_fees` / **1**. | **200** · 40 mkts / 20 events · Σ vol≈**2.7597e5** · Σ vol24≈**2.6486e5** · Σ oi≈**2.0217e5**. Samples: `…ANASJ-ANA` vol24≈39286 oi≈35688 occ→**2026-09-25 01:00 ET**; `…ANASJ-SJ` oi≈29072. | **TRY** (reinforce/refine C2; do not steal ADMIT-1) |
| **Q6S3** | `KXNFLANYTD` (+ `KXNFLFIRSTTD` / `KXNFL2TD`) | On NFL anytime/first/multi-TD props **beyond** occupied R2-P3 PASSYDS slate, do sparse multi-player binaries show near-0/1 fee + queue honesty failures that stress `000` binary-ML fee assumptions? | **Medium** (if inventory) — same NFL calendar, different contracts; not `000` retune. | Fee **cache:** `quadratic_with_maker_fees` / **1** (all three). | **ANYTD:** elections **429** ×2 + external-api **429** — **no inventory claimed**. **FIRSTTD:** **429**. **2TD:** **200** · markets `[]` (empty). | **DEFER** (429 on primary/alt; empty 2TD) |
| **Q6S4** | `KXBUNDESLIGAGAME` (soccer; first non-empty alt) | On soccer game ML under maker fees, does a non-US sports clock displace/stress `000` under R1-P1/P5? | **None / low** — European football calendar. | Fee **cache:** `quadratic_with_maker_fees` / **1**. | **UCL/EPL 200 empty.** **Bundesliga 200** · 3 mkts / 1 event · Σ vol=**12** · Σ vol24=**12** · Σ oi=**12**. Sample: `…BVBSVW-BVB` oi=12 occ→**2026-10-09 17:30 ET**. Structure live; tape too thin for bakeoff. | **HOLD** (thin tape) |
| **Q6S5** | `KXMLBSPREAD` (**distinct** MLB microstructure vs occupied S1 `KXMLBGAME` ML) | Does MLB spread book under `quadratic`×**0.5** (not S1 game-ML) create fee/queue honesty stress that threatens `000`’s inherited maker/taker assumptions vs NFL `quadratic_with_maker_fees`×1? | **Low** — baseball clock; **distinct contract family** from S1 ML (explicit non-retune). | Fee **cache:** `quadratic` / **0.5** — strongest fee-channel stress in this ≤5. | **200** · 93 mkts / 15 events · Σ vol≈**1.6900e6** · Σ vol24≈**1.6179e6** · Σ oi≈**1.1246e6**. Samples: `…SDLAD-LAD2` vol24≈588961 oi≈379288 occ→**2026-09-25 01:10 ET**; `…HOUATH-HOU2` oi≈233709. | **TRY** |

---

## Rank among TRY (analysis lock §8)

1. **Q6S5 `KXMLBSPREAD`** — fee multiplier 0.5 divergence + deepest raw tape this screen.  
2. **Q6S1 `KXATPMATCH`** — solid OOS tennis maker-fee path; inventory confirmed.  
3. **Q6S2 `KXNHLGAME`** — C2 reinforce; strong tape; lower novelty than S5/S1.  

**HOLD:** Q6S4 (structure OK, oi≈12). **DEFER:** Q6S3 (429).  

**Narrative only (no hard poll):** S2/R2-P4 `KXNFLSPREAD`(+`TOTAL`) remains **TRY-after-C1** — do not steal ADMIT-1 budget.

---

## Explicitly out / occupied (not re-nominated as new)

| Item | Status |
|---|---|
| Card 06 macro CEM-006 / CPI CEM-003 / company-KPI reopen | **CLOSED** this wave |
| More `KXNFLGAME` ML / `000` retune / Cap-SR / RFQ | **OUT** |
| S5 `KXMVECROSSCATEGORY*` / C1 UFC / C3 HIGHNY / C5 BTC15M | Occupied — not re-nominated |
| S1 `KXMLBGAME` game-ML / S4 `KXNCAAFGAME` game-ML / R2-P3 PASSYDS slate | Occupied — Q6S5 is **spread** kernel only |
| Hard `KXNFLSPREAD`/`TOTAL` GET | **Not called** (TRY-after-C1 gate) |

---

## GitHub / open-repo (inventory-backed only)

| Pointer | Slot |
|---|---|
| Internal prior: `packets/ATP_KXATPMATCH_FEEQUEUE_HARNESS*` / settled-join (Conductor-accepted) | **Q6S1** — fee/queue measurement surface already stubbed; this screen re-proves live open inventory for Q6 bakeoff candidacy |
| Internal prior: `packets/C2_KXNHLGAME_FEEQUEUE_HARNESS*` / NHL settled-join | **Q6S2** — reinforce C2 |
| No new external GitHub exclusive pin claimed this pass for MLB spread / Bundesliga | — |

---

## API blockers (honest)

| Call | Result |
|---|---|
| `KXATPMATCH` / `KXNHLGAME` / `KXUCLGAME` / `KXEPLGAME` / `KXBUNDESLIGAGAME` / `KXMLBSPREAD` / `KXNFL2TD` open markets | **200** (see table; UCL/EPL/2TD empty) |
| `KXNFLANYTD` elections | **429** (first + retry) |
| `KXNFLFIRSTTD` elections | **429** |
| `KXNFLANYTD` external-api | **429** |
| Live `/series` list | **Not called** — fee pins from house-fee **cache** (labeled) |
| `KXNFLSPREAD` / `KXNFLTOTAL` | **Not called** (budget / C1 gate) |
| `trading-api.kalshi.com` | Skipped |

---

## Scout next

1. Hand Conductor: **TRY** Q6S5 MLB spread (fee×0.5 stress) + Q6S1 ATP + Q6S2 NHL reinforce — ≤3 runnable challengers without reopening Card 06 or `000`.  
2. **DEFER** NFL TD-prop slot until ANYTD/FIRSTTD 429 clears (do not invent).  
3. **HOLD** soccer until denser than Bundesliga oi≈12.  
4. Keep S2 SPREAD/TOTAL as TRY-after-C1 only.  
5. No orders · no panel admits · no invented Δ.

*End Scout sports Q6 screen 2026-09-24/25 · GET-only · freeze-first*
