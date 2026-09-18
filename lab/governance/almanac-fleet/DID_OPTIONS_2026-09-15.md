# ALMANAC DID Options Memo — Georgia Local Number

**Date:** 2026-09-15  
**Audience:** Logan M / ALMANAC Week 0 (State Farm insurance producer trial, Georgia)  
**Scope:** Research findings only — no purchases, sign-ups, or public posts made.  
**Use case:** One dedicated local GA DID that (1) always reaches the producer’s cell, (2) supports missed-call SMS (auto or easy manual with approved text), (3) is stable enough for hard mail + email CTAs, (4) is cheap/reliable at single-line trial scale.

---

## Executive recommendation

| Role | Option | Approx. all-in monthly |
| --- | --- | --- |
| **Default (Week 0)** | **Grasshopper True Solo** | **~$16–22** (plan + A2P; taxes extra) |
| **Backup** | **Quo Business** (formerly OpenPhone) | **~$25–36** (plan + A2P; taxes extra) |

**Hard mail / email:** YES — the recommended Grasshopper number (and the Quo backup) can be printed on hard mail and used in email CTAs, provided the producer keeps the account in good standing, completes US A2P/10DLC registration for business SMS, and ports the number if switching providers later. Prefer a newly provisioned local GA long code (e.g. 404 / 470 / 678 / 770 metro Atlanta when inventory allows), not a recycled consumer VoIP freebie.

**Why Grasshopper as default (3 bullets):**
1. Base True Solo plan already includes **call forwarding to any phone** + **Instant Response** (missed-call auto-SMS) — no forced plan upsell for the two ALMANAC must-haves.
2. Explicit **Georgia inventory** (incl. Atlanta-area codes 404, 470, 678, 770) and portability language suitable for printed collateral.
3. Lowest credible all-in cost among options that fully meet forward + missed-call SMS + professional DID (~$14–18 plan + ~$1.50–3 A2P/mo).

**Why Quo Business as backup:** Best-in-class native missed-call SMS autoresponder and modern shared-inbox app; external forward-to-cell is confirmed on Business/Scale (not Starter per Quo support matrix). Slightly higher cost.

---

## Important naming note: OpenPhone = Quo

**Quo is OpenPhone rebranded** (rebrand ~Sep 2025; legal entity still OpenPhone Technologies / Quo, Inc.). They are **not** competitors. This memo treats them as one product under **Quo (formerly OpenPhone)** and does not double-count them.

---

## Comparison table (single dedicated line)

| Option | Rough monthly cost (1 GA # + forward + SMS) | Local GA / metro Atlanta | Forward-to-cell | Missed-call SMS | Hard-mail suitability | Deal-breakers for ALMANAC |
| --- | --- | --- | --- | --- | --- | --- |
| **Grasshopper True Solo** | **~$14/mo annual or ~$18/mo monthly** + A2P ~$1.50/mo + ~$19.50 one-time TCR; taxes/fees ~extra | **Yes** — lists 229, 404, 470, 478, 678, 706, 762, 770, 912 (inventory varies) | **Yes** — forward to any phone; app optional for answering | **Native** — Instant Response auto-text on missed call | Strong — portable DID; stable if account paid | UI feels dated vs Quo; weak CRM integrations (OK for trial) |
| **Quo / OpenPhone** | **Starter ~$15 annual / $19 monthly**; **Business ~$23 annual / $33 monthly** + A2P $1.50–$3/mo + $19.50 one-time | Yes — US local/toll-free; Atlanta codes typically available (confirm at signup) | **App rings on all plans**; **external forward-to-cell = Business+** (Starter ✗ per Quo support) | **Native** — auto-replies for missed calls / voicemails / texts (all plans) | Strong — free porting; professional VoIP | Starter alone may fail “always forward to cell” without app/data; Fair Use Policy (no cold dialing) |
| **Google Voice** | **Free (personal)** or **Starter $10/mo** / Standard $20/mo (standalone); Workspace add-on same + Workspace cost | Yes — search by city/area code (US) | Forward to linked numbers (paid); free has limits | **Not native** — manual SMS only; IFTTT/workarounds unreliable | Weak–medium — free numbers less “business”; port-out unlock fee historically ~$3 on free | **No native missed-call SMS**; free tier poor for hard-mail brand; business SMS compliance murkier |
| **Twilio (programmable)** | Number **~$1.15/mo** + voice ~**$0.0085/min inbound** + ~**$0.014/min outbound** to cell + SMS ~**$0.0083/segment** + carrier fees + A2P; trial volume often **~$5–20/mo** | Yes — Atlanta 404/678/770 etc. via Available Numbers API (live inventory) | DIY: Studio/TwiML dial to cell (always-forward pattern) | **Webhook/Studio DIY** — not turnkey | Strong if account kept + number ported carefully | **Engineering required**; A2P + Studio setup slow for Week 0; no polished producer app |
| **Carrier secondary line** | **Verizon Second Number ~$10–15/mo**; **T-Mobile DIGITS Talk & Text ~$10/mo** (AutoPay; more if non-TMO); AT&T **NumberSync ≠ second DID** | Yes — carrier assigns local mobile number (area code depends on market/inventory) | Native on device (dual-SIM / DIGITS app); not “forward,” it’s a real second line | **Not supported** as auto missed-call SMS; manual text only | Medium–strong as real mobile DID; portability OK; feels consumer | **No auto missed-call SMS**; may require same-carrier primary; DIGITS is app-dependent for some setups |
| **RingCentral Core** | **~$20/mo annual or ~$30 monthly** (approx.; confirm live) + taxes | Yes — local/toll-free options | App + routing; forward features on paid plans | SMS included but **capped** (~25 SMS/user/mo on Core per secondary reports) — easy to overage | Strong enterprise brand | Heavier than needed; SMS limits awkward for missed-call text-back volume |
| **CallRail** | Lead Tracking **~$45–55/mo** class (often includes multiple numbers/minutes; confirm live) | Yes — tracking numbers widely available | Forwards to destination number | Messaging/auto-replies exist; **missed-call text-back not the core product** (attribution-focused) | OK but number is a *tracking* DID (swap-heavy culture) | **Overkill / expensive** for one stable hard-mail CTA number |
| **Dialpad / Nextiva / Phone.com** (honorable mentions) | Often **~$15+/user/mo** | Usually yes | Yes on paid plans | SMS yes; **native missed-call auto-SMS less clear** than Quo/Grasshopper | Generally fine | Not clearly better than Quo/Grasshopper for this exact checklist |

*Costs marked approx. where secondary sources or usage-based. Always re-check vendor pricing pages at purchase time. A2P/10DLC fees are carrier/TCR pass-throughs common to nearly all US business SMS providers.*

---

## Option-by-option detail

### 1. Grasshopper (True Solo) — **recommended default**

| Field | Detail |
| --- | --- |
| **Cost** | True Solo: **~$14/mo billed annually** or **~$18/mo monthly** (source: grasshopper.com pricing “starting at $14/month”; third-party 2026 breakdowns). Extra numbers ~$9/mo. A2P: ~$19.50 one-time + ~$1.50/mo (approx.). Taxes/fees extra (~$5–10/mo reported by reviewers; **uncertain** by GA billing address). |
| **GA numbers** | Explicitly markets GA codes incl. **404, 470, 678, 770** (Atlanta metro) plus 229, 478, 706, 762, 912. Confirm live inventory in signup search. |
| **Forward-to-cell** | Core product: forward GA number to any phone. App available but not required for PSTN forward. |
| **Missed-call SMS** | **Native** Instant Response — auto-text first-time/missed callers with customizable message (use State Farm–approved copy only). |
| **Hard mail** | Suitable. Grasshopper states end-user can port numbers away while account is in good standing. Print only after number is provisioned and tested. |
| **Setup steps (human)** | 1) Producer (or Logan with producer authorization) starts trial / selects True Solo. 2) Search & pick GA/Atlanta local number. 3) Set forward destination = producer cell. 4) Enable Instant Response with **approved** missed-call text. 5) Complete **A2P/10DLC** business registration (legal/entity info may need producer’s State Farm agency/business details — confirm with producer/compliance). 6) Test inbound call + missed-call SMS from a second phone. 7) Only then put number on mail/email. |
| **Deal-breakers** | None critical for Week 0. Watch: dated UX; confirm Instant Response + SMS enabled after A2P approval (deliverability can lag registration). |

### 2. Quo (formerly OpenPhone)

| Field | Detail |
| --- | --- |
| **Cost** | Official quo.com/pricing (fetched 2026-09-15): Starter **$15/user/mo annual** / **$19 monthly**; Business **$23** / **$33**; Scale **$35** / **$47**. Extra numbers **$5/mo**. A2P: **$19.50 one-time** + **$1.50–$3/mo**. Telecom taxes vary by billing address (GA not listed in Quo’s published state tax list as of support doc — still expect federal/regulatory fees; **confirm at checkout**). |
| **GA numbers** | US local numbers included; metro Atlanta typically available — confirm in-app. |
| **Forward-to-cell** | Mobile/web app can ring producer’s phone over data/Wi‑Fi on all plans. **External call forwarding to a US/CA cell number is Business & Scale only** per Quo support plan matrix. |
| **Missed-call SMS** | **Native** auto-replies for missed calls, voicemails, and texts (during/after hours). Strong product fit. |
| **Hard mail** | Suitable. Free port-in help; numbers retained ~60 days after cancel per pricing FAQ — still **port out before cancel** if keeping the printed number. |
| **Setup steps** | 1) Sign up Quo trial as producer business. 2) Choose **Business** if always-forward-to-cell (PSTN) is required; Starter only if producer commits to Quo app + reliable data. 3) Pick GA local number. 4) Configure call flow: ring app and/or forward to cell. 5) Set missed-call auto-SMS with approved copy. 6) Complete A2P registration. 7) Test end-to-end. 8) Print/email. |
| **Deal-breakers** | Choosing **Starter** when PSTN forward is mandatory. Fair Use Policy (cold calling / autodialer restricted) — fine for inbound ALMANAC CTAs. |

### 3. Google Voice

| Field | Detail |
| --- | --- |
| **Cost** | Free personal; paid Standalone Starter **$10/mo**, Standard **$20/mo** (Google Help, updated ~2026-09-10). Workspace add-ons same per-user rates + separate Workspace subscription. |
| **GA numbers** | Yes — pick by city/area code (US). |
| **Forward-to-cell** | Paid: forward to linked numbers. Free: more limited / legacy linking rules. |
| **Missed-call SMS** | **Not supported natively.** Manual text from Voice; third-party workarounds fragile. |
| **Hard mail** | Risky on **free** Voice (consumer perception, recycle risk, ToS). Paid Voice better but still weaker “agency brand” than Grasshopper/Quo. Port-out possible (unlock fee historically on free numbers). |
| **Setup steps** | Create Voice (prefer paid Starter), claim GA number, link producer cell, test. For missed calls: train producer to send approved SMS manually — or abandon for this use case. |
| **Deal-breakers** | **Missing native missed-call SMS** vs ALMANAC requirement #2. Free tier unsuitable for printed hard mail. |

### 4. Twilio (or similar programmable voice)

| Field | Detail |
| --- | --- |
| **Cost** | Local DID **$1.15/mo**; inbound voice **$0.0085/min**; outbound to US **$0.014/min** (twilio.com US Voice pricing); SMS long code **~$0.0083/segment** + carrier fees. Forwarding a call ≈ inbound + outbound legs. Low trial traffic often **under ~$20/mo**, but **engineering time** is the real cost. A2P/10DLC mandatory for business SMS. |
| **GA numbers** | Yes — search area codes 404/678/770/etc. |
| **Forward-to-cell** | Build `<Dial>` / Studio flow to producer mobile. Reliable if coded correctly. |
| **Missed-call SMS** | **Webhook / Studio** — e.g. on no-answer, Messages API send template. Not turnkey. |
| **Hard mail** | Fine if account funded and number not released. Portability supported. |
| **Setup steps** | Create Twilio account, buy GA number, verify business/A2P, build Studio: inbound → dial cell → on no-answer send SMS → optional voicemail. Monitor balance/alerts. |
| **Deal-breakers** | **Too much DIY for Week 0** unless Logan deliberately wants a programmable stack. No producer-friendly inbox without more build. |

### 5. Carrier DID / secondary line (AT&T, Verizon, T-Mobile)

| Field | Detail |
| --- | --- |
| **Cost** | Verizon Second Number **~$15/mo** or **~$10/mo** perk on eligible Unlimited; T-Mobile DIGITS Talk & Text **~$10/mo** with AutoPay (higher for non-TMO / without AutoPay per rate cards); AT&T NumberSync **shares existing number** — **not** a second DID. |
| **GA numbers** | Carrier-assigned; local GA common if activated in-market — confirm store/account. |
| **Forward-to-cell** | It *is* on the cell (dual-SIM / DIGITS). Separate ringtone possible. |
| **Missed-call SMS** | **Not native auto.** Producer must text back manually. |
| **Hard mail** | Real mobile number looks professional; portable with standard wireless port-out. Tied to carrier account health. |
| **Setup steps** | Producer adds second line/DIGITS on their carrier account (may need dual-SIM/eSIM phone). Test talk/text. Document number for mail. No A2P if only person-to-person SMS — but **business campaign SMS** may still need compliance care. |
| **Deal-breakers** | **No auto missed-call SMS**; carrier lock-in; AT&T lacks a clean “second number” product analogous to Verizon/T-Mobile. |

### 6. RingCentral (Core / RingEX entry)

| Field | Detail |
| --- | --- |
| **Cost** | Core commonly cited **~$20/mo annual / ~$30 monthly** per user (confirm ringcentral.com). Includes a number. |
| **GA numbers** | Yes. |
| **Forward / SMS** | Full softphone; SMS often **metered/capped** on low tiers (secondary sources: ~25 SMS/mo on Core — **verify**). |
| **Hard mail** | Fine. |
| **Deal-breakers** | Heavier product; SMS caps undermine missed-call text-back; more than ALMANAC needs. |

### 7. CallRail (tracking-focused)

| Field | Detail |
| --- | --- |
| **Cost** | Lead Tracking plans commonly **~$45–55/mo** class with pool of numbers/minutes (confirm callrail.com/pricing — page is dynamic). Extra numbers often ~$3/mo. |
| **Fit** | Excellent for **ad attribution**, weak as a **single permanent hard-mail CTA** (culture of swapping tracking numbers). |
| **Deal-breakers** | Price + tracking-oriented number lifecycle for trial-scale one-line use. |

---

## Compliance & hard-mail notes (all options)

1. **A2P 10DLC:** Required for application-to-person business SMS on long codes (Quo, Grasshopper, Twilio, most VoIP). Budget **~$19.50 one-time + ~$1.50–$3/mo**. Approval can take days; SMS deliverability may be limited until approved.
2. **Approved copy only:** Missed-call SMS must use State Farm / producer–approved language; include opt-out where required; no unsolicited marketing texts.
3. **TCPA / consent:** Inbound call from a mail piece is different from outbound blast SMS — still keep texts transactional/responsive unless compliance clears promotional content.
4. **Stability:** Do not print until: number provisioned, forward tested, missed-call SMS tested, billing method on file, A2P submitted (or SMS held until approved).
5. **Portability:** Prefer providers that document LNP (Grasshopper, Quo, Twilio, carriers). Avoid free consumer VoIP for anything that will be printed at volume.
6. **E911:** VoIP numbers need correct emergency address configured.

---

## Week 0 recommendation & setup checklist

### Default: Grasshopper True Solo

**Reasons:** Hits all four ALMANAC requirements on the cheapest coherent single-line plan; GA/Atlanta codes marketed; Instant Response = native missed-call SMS; forward-to-cell without forcing a mid-tier upsell.

**Confirm for hard mail / email:** **YES** — after live test and A2P path started, the Grasshopper GA number is appropriate for hard mail and email CTAs.

**Setup checklist (producer + Logan):**
1. [ ] Confirm producer’s preferred metro area code (Atlanta 404/470/678/770 vs other GA).
2. [ ] Open Grasshopper True Solo trial; select GA local number; screenshot number for records.
3. [ ] Set call forwarding → producer cell; verify simultaneous/app settings as desired.
4. [ ] Draft Instant Response SMS → **compliance review** → enable.
5. [ ] Submit A2P/10DLC with correct business entity info.
6. [ ] Test: answer path, no-answer → SMS, voicemail.
7. [ ] Only then: lock number into ALMANAC mail creative + email CTA.
8. [ ] Document account owner, billing owner, porting PIN/account number for future transfer.

### Backup: Quo Business (formerly OpenPhone)

Use if Grasshopper inventory lacks desired Atlanta code, Instant Response/A2P friction appears, or the producer prefers Quo’s app/shared inbox. Configure **Business** plan for external forward-to-cell; set native missed-call auto-SMS; same A2P + test-before-print discipline.

### Explicitly not default for Week 0
- Google Voice (no native missed-call SMS; free tier weak for print)
- Twilio (build cost)
- Carrier second number alone (no auto missed-call SMS)
- CallRail / full RingCentral stacks (cost/complexity)

---

## Sources (fetched / searched 2026-09-15)

- Quo pricing: https://www.quo.com/pricing  
- Quo support pricing / forwarding matrix: https://support.quo.com/core-concepts/administration/billing/pricing ; call-forwarding docs  
- Google Voice plan compare: https://support.google.com/a/answer/9229433 (updated 2026-09-10)  
- Twilio US Voice / SMS / numbers: https://www.twilio.com/en-us/voice/pricing/us ; SMS US pricing pages  
- Grasshopper GA numbers: https://grasshopper.com/numbers/local-numbers/georgia-phone-numbers  
- Grasshopper pricing start: https://grasshopper.com/pricing/  
- Verizon Second Number FAQs; T-Mobile DIGITS business/rate-card materials  
- Secondary price corroboration (Grasshopper True Solo $14/$18, RingCentral/CallRail ranges): industry blogs — treat as **approx.** and re-verify at vendor checkout  

**No purchases, account creations, or public posts were made for this research.**
