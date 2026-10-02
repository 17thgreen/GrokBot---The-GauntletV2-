# SCOUT — Card 06 Open-Window Census (non-CPI)

- **Seat:** Market Scout (Astra/Kalshi desk)
- **Written:** 2026-09-24 21:36:56 EDT (ET)
- **Mode:** READ-ONLY. GET-only public Kalshi API + publishers' public pages (box browser when curl blocked). No orders, no build, no P&L, no fills, no VPN/proxy.
- **Freeze (must read first):** `packets/scout_card06_census/FREEZE_CARD06_CENSUS_2026-09-24.md` · sha256 `db3b0a18fd96e2f56d309f1a1b40e46bfd84953699e76163c2ad62440f0044fe` · freeze_time_ET **2026-09-24 20:05:11 EDT**
- **Amendments:** A01 (DOL standing-rule+exceptions; pull wrapper) `b8e263bf…`; A02 (429 second pass) `e3d403ba…`; A03 (historical step 5) `f245eeec…`
- **Raw:** `packets/scout_card06_census/raw/` (pointer also at `raw/README_CARD06_POINTER.md`). Pre-freeze pulls discarded in `packets/scout_card06_census/PRE_FREEZE_DISCARDED_2026-09-24/`.
- **Method:** `script/census.py` (frozen) on post-freeze bodies only. Open-window = arrival < close_time (tolerance **0 min**; equal = NO). Arrivals from official calendars only (UNSOURCED if absent).

## Family verdicts (headline)

| Family | Series | Verdict | n / sourced / YES / NO / UNSOURCED | Notes |
|---|---|---|---|---|
| Jobs (NFP) | KXPAYROLLS | **MIXED** | 20 / 19 / 1 / 18 / 1 | 18/19 close 1–5 min **before** BLS 08:30; one API anomaly (26JAN close_time 10:00 vs rules 8:29). |
| Initial claims | KXJOBLESSCLAIMS | **CEMETERY** | 20 / 20 / 0 / 20 / 0 | Close 08:25 ET; DOL 08:30 Thu. |
| GDP (Advance) | KXGDP | **MIXED** (lt20) | 6 / 6 / 1 / 5 / 0 | 5/6 close before BEA 08:30; one historical close_time 08:33 vs rules 8:25. Open/settled live GETs 429. |
| Core PCE | KXPCECORE | **CEMETERY** | 20 / 20 / 0 / 20 / 0 | Close 08:25 ET; BEA PIO 08:30. |
| Fed decision | KXFEDDECISION | **CEMETERY** (partial, lt20) | 13 / 2 / 0 / 2 / 11 | Sourced (Jul/Sep 2026 statements @ 2:00 PM ET): close ~1:55–1:59 PM. Future meetings UNSOURCED (no statement page yet). Historical GET 429. |
| Fed funds level | KXFED | **CEMETERY** (partial, lt20) | 17 / 6 / 0 / 6 / 11 | Same pattern: close before 2:00 PM statement. |
| EIA crude | KXEIACRUDEW | **CEMETERY** (lt20) | 5 / 5 / 0 / 5 / 0 | Close 10:29 ET; EIA 10:30 Wed (holiday shifts applied). Historical returned 0 markets. |
| Tesla deliveries | KXTESLA | **UNSOURCED** (lt20) | 5 / 0 / 0 / 0 / 5 | ir.tesla.com **403** (curl + browser). No official scheduled time sourced. |

**CEMETERY families (Conductor rule):** KXJOBLESSCLAIMS, KXPCECORE, KXFEDDECISION (sourced subset), KXFED (sourced subset), KXEIACRUDEW.
**MIXED (not cemetery; need per-contract review):** KXPAYROLLS, KXGDP.
**UNSOURCED:** KXTESLA.
**No OPEN-WINDOW family** (no family with every sourced row YES).

## Main table

Full machine table: `packets/scout_card06_census/out/census_rows.csv` (106 rows). Excerpt below (all selected events).

| family | contract (event) | settlement source (rule snippet) | source arrival ET (evidence) | close ET (API `close_time`) | open window | gap_min |
|---|---|---|---|---|---|---|
| KXPAYROLLS | KXPAYROLLS-26SEP | If the increase in total non-farm payroll employment is above -25000 as reported by the Bu… | 2026-10-02 08:30:00 EDT · dated-schedule · https://www.bls.gov/schedule/news_release/empsit.htm | 2026-10-02 08:29:00 EDT | **NO** | -1.0 |
| KXPAYROLLS | KXPAYROLLS-26OCT | If the increase in total non-farm payroll employment is above -25000 as reported by the Bu… | 2026-11-06 08:30:00 EST · dated-schedule · https://www.bls.gov/schedule/news_release/empsit.htm | 2026-11-06 08:29:00 EST | **NO** | -1.0 |
| KXPAYROLLS | KXPAYROLLS-26NOV | If the increase in total non-farm payroll employment is above -25000 as reported by the Bu… | 2026-12-04 08:30:00 EST · dated-schedule · https://www.bls.gov/schedule/news_release/empsit.htm | 2026-12-04 08:29:00 EST | **NO** | -1.0 |
| KXPAYROLLS | KXPAYROLLS-26JUN | If the increase in total non-farm payroll employment is above -25000 as reported by the Bu… | 2026-07-02 08:30:00 EDT · dated-schedule · https://www.bls.gov/schedule/news_release/empsit.htm | 2026-07-02 08:29:00 EDT | **NO** | -1.0 |
| KXPAYROLLS | KXPAYROLLS-26MAY | If the increase in total non-farm payroll employment is above -10000 as reported by the Bu… | 2026-06-05 08:30:00 EDT · dated-schedule · https://www.bls.gov/schedule/news_release/empsit.htm | 2026-06-05 08:29:00 EDT | **NO** | -1.0 |
| KXPAYROLLS | KXPAYROLLS-26APR | If the increase in total non-farm payroll employment is above -100000 as reported by the B… | 2026-05-08 08:30:00 EDT · dated-schedule · https://www.bls.gov/schedule/news_release/empsit.htm | 2026-05-08 08:29:00 EDT | **NO** | -1.0 |
| KXPAYROLLS | KXPAYROLLS-26MAR | If the increase in total non-farm payroll employment is above -100000 as reported by the B… | 2026-04-03 08:30:00 EDT · dated-schedule · https://www.bls.gov/schedule/news_release/empsit.htm | 2026-04-03 08:29:00 EDT | **NO** | -1.0 |
| KXPAYROLLS | KXPAYROLLS-26FEB | If the increase in total non-farm payroll employment is above -25000 as reported by the Bu… | 2026-03-06 08:30:00 EST · dated-schedule · https://www.bls.gov/schedule/news_release/empsit.htm | 2026-03-06 08:29:00 EST | **NO** | -1.0 |
| KXPAYROLLS | KXPAYROLLS-26JAN | If the increase in total non-farm payroll employment is above -25000 as reported by the Bu… | 2026-02-11 08:30:00 EST · dated-schedule · https://www.bls.gov/schedule/news_release/empsit.htm | 2026-02-11 10:00:00 EST | **YES** | 90.0 |
| KXPAYROLLS | KXPAYROLLS-25DEC | If the increase in total non-farm payroll employment is above -25000 as reported by the Bu… | 2026-01-09 08:30:00 EST · dated-schedule · https://www.bls.gov/schedule/news_release/empsit.htm | 2026-01-09 08:29:00 EST | **NO** | -1.0 |
| KXPAYROLLS | KXPAYROLLS-25NOV | If the increase in total non-farm payroll employment is above -100000 as reported by the B… | 2025-12-16 08:30:00 EST · dated-schedule · https://www.bls.gov/schedule/2025/home.htm | 2025-12-16 08:29:00 EST | **NO** | -1.0 |
| KXPAYROLLS | KXPAYROLLS-25OCT | If the increase in total non-farm payroll employment is above -100000 as reported by the B… | UNSOURCED · no BLS schedule row captured for reference month · — | 2025-11-07 08:29:00 EST | **UNSOURCED** |  |
| KXPAYROLLS | KXPAYROLLS-25SEP | If the increase in total non-farm payroll employment is above -100000 as reported by the B… | 2025-11-20 08:30:00 EST · dated-schedule · https://www.bls.gov/schedule/2025/home.htm | 2025-10-03 08:29:00 EDT | **NO** | -69121.0 |
| KXPAYROLLS | KXPAYROLLS-25AUG | If the increase in total non-farm payroll employment is above -100000 as reported by the B… | 2025-09-05 08:30:00 EDT · dated-schedule · https://www.bls.gov/schedule/2025/home.htm | 2025-09-05 08:29:00 EDT | **NO** | -1.0 |
| KXPAYROLLS | KXPAYROLLS-25JUL | If the increase in total non-farm payroll employment is above -100000 as reported by the B… | 2025-08-01 08:30:00 EDT · dated-schedule · https://www.bls.gov/schedule/2025/home.htm | 2025-08-01 08:29:00 EDT | **NO** | -1.0 |
| KXPAYROLLS | KXPAYROLLS-25JUN | If the increase in total non-farm payroll employment is above -100000 as reported by the B… | 2025-07-03 08:30:00 EDT · dated-schedule · https://www.bls.gov/schedule/2025/home.htm | 2025-07-03 08:25:00 EDT | **NO** | -5.0 |
| KXPAYROLLS | KXPAYROLLS-25MAY | If the increase in total non-farm payroll employment is above -100000 as reported by the B… | 2025-06-06 08:30:00 EDT · dated-schedule · https://www.bls.gov/schedule/2025/home.htm | 2025-06-06 08:25:00 EDT | **NO** | -5.0 |
| KXPAYROLLS | KXPAYROLLS-25APR | If the increase in total non-farm payroll employment is above -100000 as reported by the B… | 2025-05-02 08:30:00 EDT · dated-schedule · https://www.bls.gov/schedule/2025/home.htm | 2025-05-02 08:25:00 EDT | **NO** | -5.0 |
| KXPAYROLLS | KXPAYROLLS-25MAR | If the increase in total non-farm payroll employment is above -100000 as reported by the B… | 2025-04-04 08:30:00 EDT · dated-schedule · https://www.bls.gov/schedule/2025/home.htm | 2025-04-04 08:25:00 EDT | **NO** | -5.0 |
| KXPAYROLLS | KXPAYROLLS-25FEB | If the increase in total non-farm payroll employment is above -100000 as reported by the B… | 2025-03-07 08:30:00 EST · dated-schedule · https://www.bls.gov/schedule/2025/home.htm | 2025-03-07 08:25:00 EST | **NO** | -5.0 |
| KXJOBLESSCLAIMS | KXJOBLESSCLAIMS-26OCT01 | If there are at least 175,000 initial jobless claims for the week ending Sep 26, 2026, the… | 2026-10-01 08:30:00 EDT · standing-rule+exceptions · https://oui.doleta.gov/unemploy/claims_arch.asp | 2026-10-01 08:25:00 EDT | **NO** | -5.0 |
| KXJOBLESSCLAIMS | KXJOBLESSCLAIMS-26JUL23 | If there are at least 190,000 initial jobless claims for the week ending Jul 18, 2026, the… | 2026-07-23 08:30:00 EDT · standing-rule+exceptions · https://oui.doleta.gov/unemploy/claims_arch.asp | 2026-07-23 08:25:00 EDT | **NO** | -5.0 |
| KXJOBLESSCLAIMS | KXJOBLESSCLAIMS-26JUL16 | If there are at least 200,000 initial jobless claims for the week ending Jul 11, 2026, the… | 2026-07-16 08:30:00 EDT · standing-rule+exceptions · https://oui.doleta.gov/unemploy/claims_arch.asp | 2026-07-16 08:25:00 EDT | **NO** | -5.0 |
| KXJOBLESSCLAIMS | KXJOBLESSCLAIMS-26JUL09 | If there are at least 200,000 initial jobless claims for the week ending Jul 4, 2026, then… | 2026-07-09 08:30:00 EDT · standing-rule+exceptions · https://oui.doleta.gov/unemploy/claims_arch.asp | 2026-07-09 08:25:00 EDT | **NO** | -5.0 |
| KXJOBLESSCLAIMS | KXJOBLESSCLAIMS-26JUL02 | If there are at least 200,000 initial jobless claims for the week ending Jun 27, 2026, the… | 2026-07-02 08:30:00 EDT · standing-rule+exceptions · https://oui.doleta.gov/unemploy/claims_arch.asp | 2026-07-02 08:25:00 EDT | **NO** | -5.0 |
| KXJOBLESSCLAIMS | KXJOBLESSCLAIMS-26JUN25 | If there are at least 200,000 initial jobless claims for the week ending Jun 20, 2026, the… | 2026-06-25 08:30:00 EDT · standing-rule+exceptions · https://oui.doleta.gov/unemploy/claims_arch.asp | 2026-06-25 08:25:00 EDT | **NO** | -5.0 |
| KXJOBLESSCLAIMS | KXJOBLESSCLAIMS-26JUN18 | If there are at least 200,000 initial jobless claims for the week ending Jun 13, 2026, the… | 2026-06-18 08:30:00 EDT · standing-rule+exceptions · https://oui.doleta.gov/unemploy/claims_arch.asp | 2026-06-18 08:25:00 EDT | **NO** | -5.0 |
| KXJOBLESSCLAIMS | KXJOBLESSCLAIMS-26JUN11 | If there are at least 200000 initial jobless claims for the week ending Jun 6, 2026, then … | 2026-06-11 08:30:00 EDT · standing-rule+exceptions · https://oui.doleta.gov/unemploy/claims_arch.asp | 2026-06-11 08:25:00 EDT | **NO** | -5.0 |
| KXJOBLESSCLAIMS | KXJOBLESSCLAIMS-26JUN04 | If there are at least 195000 initial jobless claims for the week ending May 30, 2026, then… | 2026-06-04 08:30:00 EDT · standing-rule+exceptions · https://oui.doleta.gov/unemploy/claims_arch.asp | 2026-06-04 08:25:00 EDT | **NO** | -5.0 |
| KXJOBLESSCLAIMS | KXJOBLESSCLAIMS-26MAY28 | If there are at least 190000 initial jobless claims for the week ending May 23, 2026, then… | 2026-05-28 08:30:00 EDT · standing-rule+exceptions · https://oui.doleta.gov/unemploy/claims_arch.asp | 2026-05-28 08:25:00 EDT | **NO** | -5.0 |
| KXJOBLESSCLAIMS | KXJOBLESSCLAIMS-26MAY21 | If there are at least 190,000 initial jobless claims for the week ending May 16, 2026, the… | 2026-05-21 08:30:00 EDT · standing-rule+exceptions · https://oui.doleta.gov/unemploy/claims_arch.asp | 2026-05-21 08:25:00 EDT | **NO** | -5.0 |
| KXJOBLESSCLAIMS | KXJOBLESSCLAIMS-26MAY14 | If there are at least 180,000 initial jobless claims for the week ending May 9, 2026, then… | 2026-05-14 08:30:00 EDT · standing-rule+exceptions · https://oui.doleta.gov/unemploy/claims_arch.asp | 2026-05-14 08:25:00 EDT | **NO** | -5.0 |
| KXJOBLESSCLAIMS | KXJOBLESSCLAIMS-26MAY07 | If there are at least 165000 initial jobless claims for the week ending May 2, 2026, then … | 2026-05-07 08:30:00 EDT · standing-rule+exceptions · https://oui.doleta.gov/unemploy/claims_arch.asp | 2026-05-07 08:25:00 EDT | **NO** | -5.0 |
| KXJOBLESSCLAIMS | KXJOBLESSCLAIMS-26APR30 | If there are at least 185000 initial jobless claims for the week ending Apr 25, 2026, then… | 2026-04-30 08:30:00 EDT · standing-rule+exceptions · https://oui.doleta.gov/unemploy/claims_arch.asp | 2026-04-30 08:25:00 EDT | **NO** | -5.0 |
| KXJOBLESSCLAIMS | KXJOBLESSCLAIMS-26APR23 | If there are at least 185000 initial jobless claims for the week ending Apr 18, 2026, then… | 2026-04-23 08:30:00 EDT · standing-rule+exceptions · https://oui.doleta.gov/unemploy/claims_arch.asp | 2026-04-23 08:25:00 EDT | **NO** | -5.0 |
| KXJOBLESSCLAIMS | KXJOBLESSCLAIMS-26APR16 | If there are at least 195000 initial jobless claims for the week ending Apr 11, 2026, then… | 2026-04-16 08:30:00 EDT · standing-rule+exceptions · https://oui.doleta.gov/unemploy/claims_arch.asp | 2026-04-16 08:25:00 EDT | **NO** | -5.0 |
| KXJOBLESSCLAIMS | KXJOBLESSCLAIMS-26APR09 | If there are at least 185,000 initial jobless claims for the week ending Apr 4, 2026, then… | 2026-04-09 08:30:00 EDT · standing-rule+exceptions · https://oui.doleta.gov/unemploy/claims_arch.asp | 2026-04-09 08:25:00 EDT | **NO** | -5.0 |
| KXJOBLESSCLAIMS | KXJOBLESSCLAIMS-26APR02 | If there are at least 190000 initial jobless claims for the week ending Mar 28, 2026, then… | 2026-04-02 08:30:00 EDT · standing-rule+exceptions · https://oui.doleta.gov/unemploy/claims_arch.asp | 2026-04-02 08:25:00 EDT | **NO** | -5.0 |
| KXJOBLESSCLAIMS | KXJOBLESSCLAIMS-26MAR26 | If there are at least 185000 initial jobless claims for the week ending Mar 21, 2026, then… | 2026-03-26 08:30:00 EDT · standing-rule+exceptions · https://oui.doleta.gov/unemploy/claims_arch.asp | 2026-03-26 08:25:00 EDT | **NO** | -5.0 |
| KXJOBLESSCLAIMS | KXJOBLESSCLAIMS-26MAR19 | If there are at least 190000 initial jobless claims for the week ending Mar 14, 2026, then… | 2026-03-19 08:30:00 EDT · standing-rule+exceptions · https://oui.doleta.gov/unemploy/claims_arch.asp | 2026-03-19 08:25:00 EDT | **NO** | -5.0 |
| KXGDP | KXGDP-26APR30 | If real GDP (as measured by the BEA’s seasonally adjusted and annualized Advance Estimate)… | 2026-04-30 08:30:00 EDT · dated-schedule · https://www.bea.gov/news/schedule/full | 2026-04-30 08:29:00 EDT | **NO** | -1.0 |
| KXGDP | KXGDP-26JAN30 | If real GDP (as measured by the BEA’s seasonally adjusted and annualized Advance Estimate)… | 2026-02-20 08:30:00 EST · dated-schedule · https://www.bea.gov/news/schedule/full | 2026-02-20 08:29:00 EST | **NO** | -1.0 |
| KXGDP | KXGDP-25OCT30 | If real GDP (as measured by the BEA’s seasonally adjusted and annualized Advance Estimate)… | 2025-10-30 08:30:00 EDT · dated-schedule · https://www.bea.gov/news/schedule/full-2025 | 2025-10-30 08:29:00 EDT | **NO** | -1.0 |
| KXGDP | KXGDP-25JUL30 | If real GDP (as measured by the BEA’s seasonally adjusted and annualized Advance Estimate)… | 2025-07-30 08:30:00 EDT · dated-schedule · https://www.bea.gov/news/schedule/full-2025 | 2025-07-30 08:25:00 EDT | **NO** | -5.0 |
| KXGDP | KXGDP-25APR30 | If real GDP (as measured by the BEA’s seasonally adjusted and annualized Advance Estimate)… | 2025-04-30 08:30:00 EDT · dated-schedule · https://www.bea.gov/news/schedule/full-2025 | 2025-04-30 08:25:00 EDT | **NO** | -5.0 |
| KXGDP | KXGDP-25JAN31 | If real GDP (as measured by the BEA’s seasonally adjusted and annualized Advance Estimate)… | 2025-01-30 08:30:00 EST · dated-schedule · https://www.bea.gov/news/schedule/full-2025 | 2025-01-30 08:33:08 EST | **YES** | 3.14 |
| KXPCECORE | KXPCECORE-26AUG | If the (single-decimal) month-over-month percent change in the Personal Consumption Expend… | 2026-09-30 08:30:00 EDT · dated-schedule · https://www.bea.gov/news/schedule/full | 2026-09-30 08:25:00 EDT | **NO** | -5.0 |
| KXPCECORE | KXPCECORE-26SEP | If the (single-decimal) month-over-month percent change in the Personal Consumption Expend… | 2026-10-29 08:30:00 EDT · dated-schedule · https://www.bea.gov/news/schedule/full | 2026-10-29 08:25:00 EDT | **NO** | -5.0 |
| KXPCECORE | KXPCECORE-26OCT | If the (single-decimal) month-over-month percent change in the Personal Consumption Expend… | 2026-11-25 08:30:00 EST · dated-schedule · https://www.bea.gov/news/schedule/full | 2026-11-25 08:25:00 EST | **NO** | -5.0 |
| KXPCECORE | KXPCECORE-26NOV | If the (single-decimal) month-over-month percent change in the Personal Consumption Expend… | 2026-12-23 08:30:00 EST · dated-schedule · https://www.bea.gov/news/schedule/full | 2026-12-23 08:25:00 EST | **NO** | -5.0 |
| KXPCECORE | KXPCECORE-26MAY | If the (single-decimal) month-over-month percent change in the Personal Consumption Expend… | 2026-06-25 08:30:00 EDT · dated-schedule · https://www.bea.gov/news/schedule/full | 2026-06-25 08:25:00 EDT | **NO** | -5.0 |
| KXPCECORE | KXPCECORE-26APR | If the (single-decimal) month-over-month percent change in the Personal Consumption Expend… | 2026-05-28 08:30:00 EDT · dated-schedule · https://www.bea.gov/news/schedule/full | 2026-05-28 08:25:00 EDT | **NO** | -5.0 |
| KXPCECORE | KXPCECORE-26MAR | If the (single-decimal) month-over-month percent change in the Personal Consumption Expend… | 2026-04-30 08:30:00 EDT · dated-schedule · https://www.bea.gov/news/schedule/full | 2026-04-30 08:25:00 EDT | **NO** | -5.0 |
| KXPCECORE | KXPCECORE-26FEB | If the (single-decimal) month-over-month percent change in the Personal Consumption Expend… | 2026-04-09 08:30:00 EDT · dated-schedule · https://www.bea.gov/news/schedule/full | 2026-04-09 08:29:00 EDT | **NO** | -1.0 |
| KXPCECORE | KXPCECORE-26JAN | If the (single-decimal) month-over-month percent change in the Personal Consumption Expend… | 2026-03-13 08:30:00 EDT · dated-schedule · https://www.bea.gov/news/schedule/full | 2026-03-13 08:25:00 EDT | **NO** | -5.0 |
| KXPCECORE | KXPCECORE-25DEC | If the (single-decimal) month-over-month percent change in the Personal Consumption Expend… | 2026-02-20 08:30:00 EST · dated-schedule · https://www.bea.gov/news/schedule/full | 2026-01-29 08:25:00 EST | **NO** | -31685.0 |
| KXPCECORE | KXPCECORE-25NOV | If the (single-decimal) month-over-month percent change in the Personal Consumption Expend… | 2026-01-22 10:00:00 EST · dated-schedule · https://www.bea.gov/news/schedule/full | 2025-12-19 08:25:00 EST | **NO** | -49055.0 |
| KXPCECORE | KXPCECORE-25OCT | If the (single-decimal) month-over-month percent change in the Personal Consumption Expend… | 2026-01-22 10:00:00 EST · dated-schedule · https://www.bea.gov/news/schedule/full | 2025-11-26 08:25:00 EST | **NO** | -82175.0 |
| KXPCECORE | KXPCECORE-25SEP | If the (single-decimal) month-over-month percent change in the Personal Consumption Expend… | 2025-12-05 10:00:00 EST · dated-schedule · https://www.bea.gov/news/schedule/full-2025 | 2025-10-31 08:25:00 EDT | **NO** | -50495.0 |
| KXPCECORE | KXPCECORE-25AUG | If the (single-decimal) month-over-month percent change in the Personal Consumption Expend… | 2025-09-26 08:30:00 EDT · dated-schedule · https://www.bea.gov/news/schedule/full-2025 | 2025-09-26 08:25:00 EDT | **NO** | -5.0 |
| KXPCECORE | KXPCECORE-25JUL | If the (single-decimal) month-over-month percent change in the Personal Consumption Expend… | 2025-08-29 08:30:00 EDT · dated-schedule · https://www.bea.gov/news/schedule/full-2025 | 2025-08-29 08:25:00 EDT | **NO** | -5.0 |
| KXPCECORE | KXPCECORE-25JUN | If the (single-decimal) month-over-month percent change in the Personal Consumption Expend… | 2025-07-31 08:30:00 EDT · dated-schedule · https://www.bea.gov/news/schedule/full-2025 | 2025-07-31 08:25:00 EDT | **NO** | -5.0 |
| KXPCECORE | KXPCECORE-25MAY | If the (single-decimal) month-over-month percent change in the Personal Consumption Expend… | 2025-06-27 08:30:00 EDT · dated-schedule · https://www.bea.gov/news/schedule/full-2025 | 2025-06-27 08:25:00 EDT | **NO** | -5.0 |
| KXPCECORE | KXPCECORE-25APR | If the (single-decimal) month-over-month percent change in the Personal Consumption Expend… | 2025-05-30 08:30:00 EDT · dated-schedule · https://www.bea.gov/news/schedule/full-2025 | 2025-05-30 08:25:00 EDT | **NO** | -5.0 |
| KXPCECORE | KXPCECORE-25MAR | If the (single-decimal) month-over-month percent change in the Personal Consumption Expend… | 2025-04-30 10:00:00 EDT · dated-schedule · https://www.bea.gov/news/schedule/full-2025 | 2025-04-30 08:25:00 EDT | **NO** | -95.0 |
| KXPCECORE | KXPCECORE-25FEB | If the (single-decimal) month-over-month percent change in the Personal Consumption Expend… | 2025-03-28 08:30:00 EDT · dated-schedule · https://www.bea.gov/news/schedule/full-2025 | 2025-03-28 08:25:00 EDT | **NO** | -5.0 |
| KXFEDDECISION | KXFEDDECISION-26OCT | If the Federal Reserve does a Cut of 25bps on October 28, 2026, then the market resolves t… | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2026-10-28 13:59:00 EDT | **UNSOURCED** |  |
| KXFEDDECISION | KXFEDDECISION-26DEC | If the Federal Reserve does a Cut of 25bps on December 09, 2026, then the market resolves … | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2026-12-09 13:59:00 EST | **UNSOURCED** |  |
| KXFEDDECISION | KXFEDDECISION-27JAN | If the Federal Reserve does a Cut of 25bps on January 27, 2027, then the market resolves t… | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2027-01-27 13:59:00 EST | **UNSOURCED** |  |
| KXFEDDECISION | KXFEDDECISION-27MAR | If the Federal Reserve does a Cut of 25bps on March 17, 2027, then the market resolves to … | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2027-03-17 13:59:00 EDT | **UNSOURCED** |  |
| KXFEDDECISION | KXFEDDECISION-27APR | If the Federal Reserve does a Cut of 25bps on April 28, 2027, then the market resolves to … | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2027-04-28 13:59:00 EDT | **UNSOURCED** |  |
| KXFEDDECISION | KXFEDDECISION-27JUN | If the Federal Reserve does a Cut of 25bps on June 09, 2027, then the market resolves to Y… | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2027-06-09 13:59:00 EDT | **UNSOURCED** |  |
| KXFEDDECISION | KXFEDDECISION-27JUL | If the Federal Reserve does a Cut of 25bps on July 28, 2027, then the market resolves to Y… | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2027-07-28 13:59:00 EDT | **UNSOURCED** |  |
| KXFEDDECISION | KXFEDDECISION-27SEP | If the Federal Reserve does a Cut of 25bps on September 15, 2027, then the market resolves… | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2027-09-15 13:59:00 EDT | **UNSOURCED** |  |
| KXFEDDECISION | KXFEDDECISION-27OCT | If the Federal Reserve does a Cut of 25bps on October 27, 2027, then the market resolves t… | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2027-10-27 13:59:00 EDT | **UNSOURCED** |  |
| KXFEDDECISION | KXFEDDECISION-27DEC | If the Federal Reserve does a Cut of 25bps on December 08, 2027, then the market resolves … | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2027-12-08 13:59:00 EST | **UNSOURCED** |  |
| KXFEDDECISION | KXFEDDECISION-28JAN | If the Federal Reserve does a Cut of 25bps on January 26, 2028, then the market resolves t… | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2028-01-26 13:59:00 EST | **UNSOURCED** |  |
| KXFEDDECISION | KXFEDDECISION-26SEP | If the Federal Reserve does a Cut of 25bps on September 16, 2026, then the market resolves… | 2026-09-16 14:00:00 EDT · dated-release · https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm | 2026-09-16 13:59:00 EDT | **NO** | -1.0 |
| KXFEDDECISION | KXFEDDECISION-26JUL | If the Federal Reserve does a Cut of 25bps on July 29, 2026, then the market resolves to Y… | 2026-07-29 14:00:00 EDT · dated-release · https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm | 2026-07-29 13:59:00 EDT | **NO** | -1.0 |
| KXFED | KXFED-26OCT | If the upper bound of the target federal funds rate published on the Federal Reserve's off… | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2026-10-28 13:55:00 EDT | **UNSOURCED** |  |
| KXFED | KXFED-26DEC | If the upper bound of the target federal funds rate published on the Federal Reserve's off… | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2026-12-09 13:55:00 EST | **UNSOURCED** |  |
| KXFED | KXFED-27JAN | If the upper bound of the target federal funds rate published on the Federal Reserve's off… | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2027-01-27 13:55:00 EST | **UNSOURCED** |  |
| KXFED | KXFED-27MAR | If the upper bound of the target federal funds rate published on the Federal Reserve's off… | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2027-03-17 13:55:00 EDT | **UNSOURCED** |  |
| KXFED | KXFED-27APR | If the upper bound of the target federal funds rate published on the Federal Reserve's off… | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2027-04-28 13:55:00 EDT | **UNSOURCED** |  |
| KXFED | KXFED-27JUN | If the upper bound of the target federal funds rate published on the Federal Reserve's off… | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2027-06-09 13:55:00 EDT | **UNSOURCED** |  |
| KXFED | KXFED-27JUL | If the upper bound of the target federal funds rate published on the Federal Reserve's off… | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2027-07-28 13:55:00 EDT | **UNSOURCED** |  |
| KXFED | KXFED-27SEP | If the upper bound of the target federal funds rate published on the Federal Reserve's off… | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2027-09-15 13:55:00 EDT | **UNSOURCED** |  |
| KXFED | KXFED-27OCT | If the upper bound of the target federal funds rate published on the Federal Reserve's off… | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2027-10-27 13:55:00 EDT | **UNSOURCED** |  |
| KXFED | KXFED-27DEC | If the upper bound of the target federal funds rate published on the Federal Reserve's off… | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2027-12-08 13:55:00 EST | **UNSOURCED** |  |
| KXFED | KXFED-28JAN | If the upper bound of the target federal funds rate published on the Federal Reserve's off… | UNSOURCED · no dated Fed statement page (future or not captured) · — | 2028-01-26 13:55:00 EST | **UNSOURCED** |  |
| KXFED | KXFED-26SEP | If the upper bound of the target federal funds rate published on the Federal Reserve's off… | 2026-09-16 14:00:00 EDT · dated-release · https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm | 2026-09-16 13:55:00 EDT | **NO** | -5.0 |
| KXFED | KXFED-26JUL | If the upper bound of the target federal funds rate published on the Federal Reserve's off… | 2026-07-29 14:00:00 EDT · dated-release · https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm | 2026-07-29 13:55:00 EDT | **NO** | -5.0 |
| KXFED | KXFED-26JUN | If the upper bound of the target federal funds rate published on the Federal Reserve's off… | 2026-06-17 14:00:00 EDT · dated-release · https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm | 2026-06-17 13:55:00 EDT | **NO** | -5.0 |
| KXFED | KXFED-26APR | If the upper bound of the target federal funds rate published on the Federal Reserve's off… | 2026-04-29 14:00:00 EDT · dated-release · https://www.federalreserve.gov/newsevents/pressreleases/monetary20260429a.htm | 2026-04-29 13:55:00 EDT | **NO** | -5.0 |
| KXFED | KXFED-26MAR | If the upper bound of the target federal funds rate published on the Federal Reserve's off… | 2026-03-18 14:00:00 EDT · dated-release · https://www.federalreserve.gov/newsevents/pressreleases/monetary20260318a.htm | 2026-03-18 13:55:00 EDT | **NO** | -5.0 |
| KXFED | KXFED-26JAN | If the upper bound of the target federal funds rate published on the Federal Reserve's off… | 2026-01-28 14:00:00 EST · dated-release · https://www.federalreserve.gov/newsevents/pressreleases/monetary20260128a.htm | 2026-01-28 13:55:00 EST | **NO** | -5.0 |
| KXEIACRUDEW | KXEIACRUDEW-26SEP30 | If U.S. commercial crude oil inventories for the week ending Sep 25, 2026 are strictly abo… | 2026-09-30 10:30:00 EDT · standing-rule+exceptions · https://www.eia.gov/petroleum/supply/weekly/schedule.php | 2026-09-30 10:29:00 EDT | **NO** | -1.0 |
| KXEIACRUDEW | KXEIACRUDEW-26SEP23 | If U.S. commercial crude oil inventories for the week ending Sep 18, 2026 are strictly abo… | 2026-09-23 10:30:00 EDT · standing-rule+exceptions · https://www.eia.gov/petroleum/supply/weekly/schedule.php | 2026-09-23 10:29:00 EDT | **NO** | -1.0 |
| KXEIACRUDEW | KXEIACRUDEW-26SEP16 | If U.S. commercial crude oil inventories for the week ending Sep 11, 2026 are strictly abo… | 2026-09-16 10:30:00 EDT · standing-rule+exceptions · https://www.eia.gov/petroleum/supply/weekly/schedule.php | 2026-09-16 10:29:00 EDT | **NO** | -1.0 |
| KXEIACRUDEW | KXEIACRUDEW-26SEP09 | If U.S. commercial crude oil inventories for the week ending Sep 4, 2026 are strictly abov… | 2026-09-10 12:00:00 EDT · standing-rule+exceptions(exception row) · https://www.eia.gov/petroleum/supply/weekly/schedule.php | 2026-09-10 11:55:00 EDT | **NO** | -5.0 |
| KXEIACRUDEW | KXEIACRUDEW-26SEP02 | If U.S. commercial crude oil inventories for the week ending Aug 28, 2026 are strictly abo… | 2026-09-02 10:30:00 EDT · standing-rule+exceptions · https://www.eia.gov/petroleum/supply/weekly/schedule.php | 2026-09-02 10:29:00 EDT | **NO** | -1.0 |
| KXTESLA | KXTESLA-26-Q1 | If Tesla has at least 290000 total deliveries in Q1 2026, then the market resolves to Yes. | UNSOURCED · ir.tesla.com 403 (curl and browser); no official scheduled release time · — | 2026-04-02 11:34:52 EDT | **UNSOURCED** |  |
| KXTESLA | KXTESLA-25-Q4 | If Tesla has at least 380000 total deliveries in Q4 2025, then the market resolves to Yes. | UNSOURCED · ir.tesla.com 403 (curl and browser); no official scheduled release time · — | 2026-01-02 16:08:18 EST | **UNSOURCED** |  |
| KXTESLA | KXTESLA-25-Q3 | If Tesla has at least 300000 total deliveries in Q3 2025, then the market resolves to Yes. | UNSOURCED · ir.tesla.com 403 (curl and browser); no official scheduled release time · — | 2025-10-02 09:43:30 EDT | **UNSOURCED** |  |
| KXTESLA | KXTESLA-25-Q2 | If Tesla has at least 300000 total deliveries in Q2 2025, then the market resolves to Yes. | UNSOURCED · ir.tesla.com 403 (curl and browser); no official scheduled release time · — | 2025-07-02 12:48:47 EDT | **UNSOURCED** |  |
| KXTESLA | KXTESLA-25-Q1 | If Tesla has at least 270000 total deliveries in Q1 2025, then the market resolves to Yes. | UNSOURCED · ir.tesla.com 403 (curl and browser); no official scheduled release time · — | 2025-04-02 10:01:26 EDT | **UNSOURCED** |  |

## Family verdicts
- **KXPAYROLLS**: **MIXED** — n=20, sourced=19, YES=1, NO=18, UNSOURCED=1, lt20=False, partial=True
- **KXJOBLESSCLAIMS**: **CEMETERY** — n=20, sourced=20, YES=0, NO=20, UNSOURCED=0, lt20=False, partial=False
- **KXGDP**: **MIXED** — n=6, sourced=6, YES=1, NO=5, UNSOURCED=0, lt20=True, partial=False
- **KXPCECORE**: **CEMETERY** — n=20, sourced=20, YES=0, NO=20, UNSOURCED=0, lt20=False, partial=False
- **KXFEDDECISION**: **CEMETERY** — n=13, sourced=2, YES=0, NO=2, UNSOURCED=11, lt20=True, partial=True
- **KXFED**: **CEMETERY** — n=17, sourced=6, YES=0, NO=6, UNSOURCED=11, lt20=True, partial=True
- **KXEIACRUDEW**: **CEMETERY** — n=5, sourced=5, YES=0, NO=5, UNSOURCED=0, lt20=True, partial=False
- **KXTESLA**: **UNSOURCED** — n=5, sourced=0, YES=0, NO=0, UNSOURCED=5, lt20=True, partial=True
## Anomalies (reported, not overridden)
- **KXPAYROLLS-26JAN:** API `close_time` = 2026-02-11 10:00 EST → gap +90 vs BLS 08:30 → YES. Rules text still says "closes at 8:29 AM ET". Flagged; freeze uses API `close_time`.
- **KXGDP-25JAN31:** API `close_time` = 08:33:08 EST → gap +3.14 vs BEA 08:30 → YES. Rules text says "close at 8:25 AM".
- **KXPAYROLLS-25SEP:** BLS delayed Employment Situation for Sep 2025 to Nov 20, 2025; Kalshi closed Oct 3 → large negative gap (NO).
- **KXPAYROLLS-25OCT:** no Employment Situation for Oct 2025 on captured BLS 2025 schedule → UNSOURCED.

## Blockers
- Kalshi unauthenticated API: frequent **429**; settled live GETs exhausted retries for KXPAYROLLS, KXJOBLESSCLAIMS, KXGDP, KXPCECORE; open KXGDP; closed EIA/GDP/TESLA; historical KXFEDDECISION. ERRORBODY files retained.
- BLS empsit schedule: curl **403**; content captured via box browser.
- Tesla IR: curl **403** and browser **403** (Access Denied).
- DOL ui/data.pdf: curl **403** (standing schedule taken from claims_arch.asp instead, A01).

## Excluded
- **KXCPI / KXCPIYOY** — already CEMETERY (CEM-ASTRA-20260924-003).
- Aggregator-sourced series (Trading Economics etc.): KXUSNFP, KXUE, KXUSPPI, foreign GDP flash/prelim, …
- No scheduled official release / one_offs: Fed emergency, tweets, "move on FOMC day", …
- Legacy duplicates: PAYROLLS, PROLLS, JOBLESS, GDP, FED, FEDDECISION, PCECORE (non-KX).
- Same-release siblings deferred: KXU3, KXPCEHEAD, KXCONTCLAIMS.

## Sources (fetch times ET 2026-09-24; see `raw/official/_fetch_log.tsv` and `raw/kalshi/_call_log.tsv`)
- BLS Employment Situation schedule (browser): https://www.bls.gov/schedule/news_release/empsit.htm (20:07:31); 2025 home https://www.bls.gov/schedule/2025/home.htm (20:08:00)
- BEA: https://www.bea.gov/news/schedule/full and /full-2025 (20:05:44)
- Fed FOMC calendar + statement pages monetary2023–2026*a.htm (20:05:45 + batch)
- EIA WPSR: https://www.eia.gov/petroleum/supply/weekly/schedule.php (20:05:43)
- DOL claims archive: https://oui.doleta.gov/unemploy/claims_arch.asp (20:06:57)
- Kalshi: `api.elections.kalshi.com/trade-api/v2` series/markets/historical (20:05–21:34)

## Fee note (if fees arise later)
Per RULE from Conductor: state fees both **per side** and **round trip**, and label Scout arithmetic separately from doc-quoted figures. (Card 04 amendment already records Kalshi Prime Tier 0 taker 0.120%/side → 0.240% RT; maker 0.020%/side → 0.040% RT.)
