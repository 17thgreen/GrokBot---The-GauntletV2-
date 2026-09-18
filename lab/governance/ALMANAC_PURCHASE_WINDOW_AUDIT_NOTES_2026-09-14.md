# ALMANAC Purchase-Window Audit Notes

**Date:** 2026-09-14  
**Repo:** `17thgreen/ClaudeCodeInsuranceOS` · branch `claude/event-triggered-insurance-design-cdxgsw`  
**Access:** GitHub MCP (`user-Github`); local `gh` CLI not authenticated. Docs pulled via `get_file_contents` on that ref.  
**Purpose:** Capture ALMANAC doctrine on renewal-letter timing / anniversary clock, external premium-inflation & shopping stats (cited only), and which purchase-date bands test which thesis.

---

## 1. What ALMANAC docs say (exact lines)

### 1.1 Deed = anniversary clock (purchase → renewal month)

From `docs/06_OPPORTUNITY_BRIEF.md` §1:

> A home closing is recorded in the public record. Homeowners insurance is bound at closing — the lender requires it — and it renews on that anniversary every year afterward, for as long as the household owns the house.
>
> **So the recorded purchase date predicts the renewal month, roughly ten months in advance, for essentially every mortgaged household in the state.** [H — the load-bearing hypothesis; measurable against any agency's book in a day]

From the same brief §1 (refi correction):

> **A refinance never moves the date.** A refi changes the mortgagee clause, not the policy anniversary. … Use the *original arms-length sale date* or the calendar is wrong.

From branch `README.md`:

> the deed is a clock, not an event — a recorded closing date predicts the household's insurance renewal month ~10 months ahead, forever

From `docs/01_VERDICT_AND_AUDIT.md` §1:

> Homeowner policies bind at closing and renew annually on roughly the closing anniversary — this inference is literally the product basis of Cole X-Dates…

### 1.2 Carrier renewal letters: ~45–75 / −70 to −45 (not a single “45–70” constant)

ALMANAC does **not** hard-code the string “45–70 days” as verified law. It uses two closely related bands:

**A. Working hypothesis for when carriers mail offers** — `docs/06_OPPORTUNITY_BRIEF.md` §6 and `docs/10_STRATEGY_MEMO_01.html` §3:

> Carriers mail renewal offers somewhere around **−70 to −45** [H — verify against three real renewal declarations; this is the load-bearing input]

Strategy Memo No. 1 (HTML) restates:

> Carriers mail renewal offers around **−70 to −45**, and increasingly they mail a *save attempt* alongside it…

**B. Cross-check from an independent pass** — `docs/06_OPPORTUNITY_BRIEF.md` §8:

> Carrier renewal notices at **45–75 days** before expiration, corroborated across four industry cadences (Dataman 30–45, PostcardMania 30–90, GloveBox 60/40/30). This closes an input previously flagged unverified in §6.

**Operational mail targets (ALMANAC’s own drops, not carrier mail):** −90 primer / −45 follow-up (`06` §6; `10` §3; `docs/15_PRODUCER_FIELD_MANUAL.md` §6 notes the −90/−45 campaign clock separately from the 21-day producer cadence).

> | Touch | Lands at | Drop at | Job |
> |---|---|---|---|
> | **1 · Primer** | **−90** | −97 | Arrives *before any carrier notice*… |
> | **2 · Follow-up** | **−45** | −52 | Arrives with or just after the notice… |

> **−90 lands −120 to −60, which beats a −70 notice in nearly every case.**

Georgia statutory **non-renewal** notice (different from ordinary renewal offers): Act 277 extends notice from 30 → **60 days** (`06` §3; `research_georgia` §2; `research_product_econ` §10).

### 1.3 Premium shock + shopping propensity (as ALMANAC cites)

From `docs/01_VERDICT_AND_AUDIT.md` §1:

> In a market where Georgia premiums are up ~40% since 2021, **57% of customers shopped last year (a record)**, carriers are mass non-renewing over roof age, and Act 277 mandates a 60-day non-renewal notice `[V research_georgia §2, research_product_econ §10]`…

From `docs/06_OPPORTUNITY_BRIEF.md` §4:

> **57% of insurance customers shopped in the 2025 study year, up from 49% — a record.** [V — J.D. Power 2025 Insurance Shopping Study]
>
> Home insurance is the striking one: a **record 6.8% of customers were actively shopping, but only 2.2% actually switched.** [V — J.D. Power 2025 Home Insurance Study]
>
> **43%** of customers hit with an increase and unlikely to renew name the price hike as the switching trigger; **45%** of high-value multi-product customers cite repeated increases. [V]

**Note on “~56%”:** ALMANAC’s cited shopping figure is **57%** (J.D. Power 2025 Insurance Shopping Study — auto/shopping study), not 56%. Do not invent a 56% ALMANAC source; treat “~56%” as informal rounding of the 57% cite unless a different doc is found later.

Placement constraint (shopping ≫ switching) — `docs/15_PRODUCER_FIELD_MANUAL.md` §2 and `docs/01` §2.2.5:

> …placement constraint (**6.8% shopping against 2.2% switching**).
>
> Record **6.8%** of home customers shopping, only **2.2%** switching — carrier appetite is the bottleneck `[V research_product_econ §10]`.

First-renewal premium step — `docs/06` §2 / `docs/19_WHAT_WE_SELL.md` §5 / Strategy Memo §2:

> Their first renewal is the first time they see the real number without closing-day distraction, and in Georgia it arrives **8–10% higher** than the one they agreed to.
>
> **B0 · FIRST-RENEWAL** | The best calendar cohort — bought under time pressure, never shopped, first renewal 8–10% higher

### 1.4 Purchase-date windows ALMANAC already uses

| Cohort | Purchase window (as stated) | Doc |
|---|---|---|
| First renewal / softest calendar entry | Bought **8–12 months** ago (`06`); **9–13 months** (`10`); pilot list `SELL-1` = bought **6–10 months** ago (`21` §2) | `06`, `10`, `21` |
| Rolling calendar | Twelve month-lists by **original purchase month** = inferred renewal month | `06` §6, `19` |
| Fresh cash / landlord formation | Last **30 / 90 / 180** days (event play, not anniversary) | `19` §2d |

Pilot measurement design that *uses* purchase-date spread to test the clock — `docs/21_THE_PILOT.md` §2:

> **`SELL-1` is defined as bought 6–10 months ago. That means its records are already spread across the thing we are trying to test.**
>
> A household that bought 10 months ago is **~60 days** from its anniversary. One that bought 6 months ago is **~180 days** out. Same list, same letter, same drop date.
>
> **Mail them all at once and plot response rate against days-to-anniversary.**
>
> **If response peaks near −90 and falls away on both sides, the clock is real.** If the curve is flat, we have a decent mail programme and a false thesis.

Local ops echo (box, not GitHub): `/workspace/lab/governance/ALMANAC_GROK_FLEET_PLAYBOOK_2026-09-14.md` — List A = `SELL - 8-9 Months Phone and Email` / “Clock test + first renewal”; Examiner metric “Response vs days-to-anniversary (A)”.

---

## 2. External sources — premium inflation & shopping/switching

*Only cited numbers below; no invented stats. “Shopping” vs “switching” are different metrics — keep them separate.*

### 2.1 Premium inflation (US / national)

| Claim | Source | Link |
|---|---|---|
| Regulator-approved home rates **+10.7% (2023), +12.5% (2024), +5.9% (2025)**; cumulative **+45.8%** 2020–2025 vs **+26.1%** inflation | LendingTree (RateWatch-based study) | https://www.lendingtree.com/insurance/rates-inflation-income-study/ |
| Cumulative home rates **+46.8%** 2020–2025; annual peak **+12.7% in 2024**, then **+6.0% in 2025** | LendingTree State of Home Insurance | https://www.lendingtree.com/insurance/state-of-home-insurance/ |
| Mortgaged SF average property insurance **$2,290 in 2024**, **+$276 / +14%** YoY; **+61% over 5 years** | ICE Mortgage Monitor (Mar 2025 release, via Business Wire / Morningstar mirror) | https://www.morningstar.com/news/business-wire/20250303971478/ice-mortgage-monitor-property-insurance-costs-rose-at-a-record-rate-in-2024-prompting-homeowners-to-shop-for-better-rates-accept-higher-deductibles |
| Average HO premiums rose faster than inflation **2018–2024** by region (e.g. West **+43%** inflation-adjusted over the period per CNBC summary of NAIC) | NAIC MCAS / CNBC coverage | https://content.naic.org/industry/mcas/homeowners-insurance-report · https://www.cnbc.com/2026/08/06/homeowners-insurance-costs-soar-naic-report.html |
| Q2 2026: costs still rising but slowing (**+8.7% YoY**; switchers cut premiums **6.6%** vs **+10.4%** for stayers; ~**$440**/yr savings) | ICE Mortgage Monitor Sep 2026 (HousingWire / Financial Content) | https://www.housingwire.com/articles/ice-property-insurance-record-high/ · https://markets.financialcontent.com/wss/article/bizwire-2026-9-10-ice-mortgage-monitor-property-insurance-costs-rise-87-annually-but-rate-of-growth-is-sharply-slowing |

### 2.2 Shopping / switching propensity

| Claim | Population | Source | Link |
|---|---|---|---|
| **57%** actively shopped for a new auto policy in the past year (record; up from **49%**) | Auto insurance customers | J.D. Power 2025 U.S. Insurance Shopping Study (press release 29 Apr 2025) | https://www.jdpower.com/business/press-releases/2025-us-insurance-shopping-study |
| **47%** of homeowners experienced a premium increase in the past year; among those unlikely to renew after an increase, **43%** cite the hike; **45%** of high-value multi-product customers cite repeated increases | Homeowners | J.D. Power 2025 U.S. Home Insurance Study (press release 16 Sep 2025) | https://www.jdpower.com/business/press-releases/2025-us-home-insurance-study |
| ALMANAC additionally attributes **6.8% home shopping / 2.2% switched** to the same Home Insurance Study `[V]` — **not re-found in the public press-release body fetched 2026-09-14**; treat as ALMANAC-cited until full study deck is re-checked | Home | ALMANAC `06` / `research_product_econ` §10 → same J.D. Power URL family | https://www.jdpower.com/business/press-releases/2025-us-home-insurance-study/ |
| Record **11.4%** of mortgaged borrowers **switched carriers in 2024** (up from **9.4%** in 2023; <8% historically) | Mortgaged SF | ICE Mortgage Monitor | Same Business Wire / StockTitan mirrors as above |
| **19%** shopped home insurance in past 12 months; **8%** switched (NerdWallet survey, via InsuranceNewsNet) | Home | InsuranceNewsNet / NerdWallet | https://insurancenewsnet.com/oarticle/worried-about-insurance-rates-your-loyalty-might-be-costing-you-3 |

**Read carefully:** 57% (J.D. Power shopping study) is a **broad shopping** rate in that study’s auto/shopping frame; ICE’s 11.4% is **completed carrier switches** among mortgaged borrowers; NerdWallet’s 19%/8% is another survey’s shop/switch pair. Do not collapse these into one “~56% switch” number.

### 2.3 Georgia-specific (ALMANAC research briefs, externally sourced)

From `docs/research/research_product_econ.md` §10 and `docs/research/research_georgia.md` §2 (each carries its own URL list): GA HO **~+40% since 2021**, **+24% 2023–2025**, **~+7.3–8.6% in 2025**; Act 277 **30→60 day** non-renewal notice. Primary external anchors include AJC, Live Insurance News, IIAG, Insurance Journal, MoneyGeek/Insurify.

---

## 3. Analytical frame — three purchase bands and which thesis each captures

| Band | Definition (purchase-date filter) | What it captures | Thesis under test |
|---|---|---|---|
| **A. First-renewal band** | Purchased **~10–12 months ago** in a **narrow calendar-month band** (e.g. one purchase month → one inferred anniversary month). ALMANAC variants: 8–12 mo (`06`), 9–13 mo (`10`), operational `SELL-1` 6–10 mo (`21`) with Examiner slice near −90. | Households about to hit **first** post-closing renewal; policy often chosen under closing pressure; low loyalty; first “real” premium shock (ALMANAC: **8–10% higher**). | **Clock + first-shock:** purchase month ≈ renewal month **and** first-renewal pain converts better than later anniversaries. Flat response vs days-to-anniversary falsifies the clock (`21` §2). |
| **B. Multi-year same-calendar-month renewals** | Purchased **2–5 years ago** in the **same season/month** as the campaign’s target renewal month (twelve month-lists / rolling anniversary book). | Experienced renewers on the **same anniversary season**; includes multi-year rate stacking, non-renewal / roof-cliff overlays, not “new to insurance.” | **Scale calendar / shock overlay:** anniversary timing still predicts shopping moments for **seasoned** books; SERFF + roof + hail ranking matters more than first-time sticker shock. |
| **C. Last 12 months, any month** | Any purchase in the trailing year (**all months**), not aligned to a single anniversary month. | Mix of first-renewal-near, mid-policy, and far-from-anniversary households in one drop. | **Mail / creative baseline (non-clock):** measures whether “recent buyer” messaging works **without** timing. Per `21` §2, if band C responds like a timed first-renewal cut, the **trigger is weak** and the letter is doing the work. Closest to the killed “recent homebuyer = event” thesis (`01` §2.2.1) if used as acquisition without anniversary alignment. |

**How to use them together (audit recommendation):**

1. Hold creative constant.  
2. Compare **A vs C** on the same drop → isolates **timing** (clock) from **recency**.  
3. Compare **A vs B** (same target renewal month) → isolates **first-renewal shock** from **multi-year anniversary** demand.  
4. Within A (or `SELL-1` 6–10 mo), plot response vs **days-to-anniversary** exactly as `21` §2 specifies.

---

## 4. Access / provenance notes

- **GitHub:** branch tip listed via MCP `list_branches` (`claude/event-triggered-insurance-design-cdxgsw`). Key files read: `README.md`, `docs/01`, `06`, `10`, `15`, `19`, `21`, `docs/research/research_lead_market.md`, `research_product_econ.md`, `research_georgia.md`.  
- **Not used:** `gh api` / `gh search` (CLI unauthenticated); anonymous GitHub REST rate-limited (403). Code search returned 0 hits (private-repo search limitation); directory listing + direct file fetch worked.  
- **Local box:** `/workspace/lab/governance/ALMANAC_GROK_FLEET_PLAYBOOK_2026-09-14.md` aligns with doctrine (`15`/`19`/`21`) but is an ops playbook, not a substitute for the research brief.  
- **No fabricated stats.** Where ALMANAC’s secondary cite (6.8%/2.2%) was not visible in the public J.D. Power press-release HTML fetched today, that is flagged explicitly above.

---

## 5. One-line takeaway

ALMANAC’s load-bearing timing story is: **original purchase date → annual renewal anniversary (~10 months ahead)**; carriers’ own renewal letters are hypothesized around **−70 to −45 / 45–75 days** before expiration, so ALMANAC mails **−90 then −45**; shopping tailwinds are cited as **~57% shopped (J.D. Power)** with home **shop ≫ switch**; audit purchase windows by separating **first-renewal month band**, **multi-year same-month renewals**, and **last-12-months any month** so clock, first-shock, and creative-only effects are not confounded.
