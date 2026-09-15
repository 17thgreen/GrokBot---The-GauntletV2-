# ALMANAC × Grok Bot Fleet — Operational Playbook v2 (2026-09-14)

**Status:** Active desk plan under Governor lock (Gauntlet science paused; captures passive).  
**First revenue path:** State Farm producer trial → measure response → then independent/E&S for bind economics.  
**Doctrine:** branch `claude/event-triggered-insurance-design-cdxgsw` (`15`, `19`, `21`); PropertyRadar skill `operate-propertyradar-for-almanac-lists`.

---

## 1. Why this fleet shape

ALMANAC fails in two places: **bad lists** and **bad words**. Everything else is plumbing.

So the fleet is built around three factories:

1. **Radar** — right owners, right timing, right suppressions  
2. **Copy** — short personable letters that invite a 10-minute quote without inventing facts  
3. **Instrument** — every touch measurable (DID, email, token, dispositions)

Human producer answers the phone. Grok Bot does not sell insurance; it runs the factory and measures.

---

## 2. Fleet org chart (serious version)

### Tier 0 — Governor / Conductor
| Seat | Who | Mandate |
|---|---|---|
| **Human Governor** | Logan | Budget, DID/SAN spend, lock lists, reopen Gauntlet, counsel |
| **The Conductor** | This bot | Allocate seats; freeze variants; enforce evidence tags; weekly go/no-go; never invent rates |

Conductor does **not** write final customer-facing copy alone when Copy seat exists — Conductor **approves**.

### Tier 1 — Core operate seats (create these)

| Seat | Name suggestion | Owns | Success metric |
|---|---|---|---|
| **Radar Operator** | The Radar | PropertyRadar REF/STOCK/SELL; exports; monitoring; suppress sold/listed | Clean cuts on time; count drift logged |
| **Copy Chief** | The Quill | Hard-mail + email wording; A/B variants; `15 §1` gate; soft close | Response rate lift; zero compliance violations |
| **Mailer** | The Drop | Print/post calendar; **email send at day 8–10**; QR/token per row; postage + send log | On-time mail + email; token completeness 100% |
| **Line Desk** | The Switchboard | Dedicated DID → producer cell; missed-call SMS; inbound log | Every inbound tagged &lt;5 min |
| **Examiner** | The Examiner (ALMANAC) | Scorecards; response vs days-to-anniversary; channel mix; [SF] bind labels | Weekly packet; kill/green calls |
| **Compliance** | The Governor’s Counsel (ops) | SAN scrub cadence; CALL_OK stamps; disclosure text; counsel flags | No cold dial of DNC; 31-day scrub |

### Tier 2 — Human
| Seat | Who | Owns |
|---|---|---|
| **Producer** | State Farm partner | Answer DID; quote; dispositions same day; SF compliance |

### Tier 3 — Do not staff yet
Book Guardian attach, Model 3 lead marketplace, Tax Appeal, SiteWorks land-pack, national multi-agency SAN sharing.

### Explicit non-reuse
Crypto Gauntlet seats (Tape, Clock research, Cartographer, etc.) stay **idle**. Do not dual-hat Examiner crypto ↔ ALMANAC without renaming — different evidence rules.

**MVP to first drop (5 bots + 1 human):** Conductor, Radar, Quill, Drop, Switchboard — Examiner scorecard can start as Conductor-held for week 1; Compliance held by Conductor until SAN live.

---

## 3. First-revenue operating loop

```text
Radar freezes 3 SELL cuts
    → Quill freezes 1 letter variant per list (+ soft close)
    → Drop mails with DID + QR token
    → Switchboard logs every inbound → Producer
    → Examiner scores weekly
    → Conductor kills list/creative or scales
```

### Cadence (locked)

| Touch | Channel | Timing | Who gets it |
|---|---|---|---|
| **1** | Hard mail | Day 0 (post date) | Full SELL cut |
| **2** | Email follow-up | **Day 8–10 after mail post** (default **Day 9**) | Same cohort, **email-present rows only** (lists already filtered for Owner Email where required) |
| **3** | Manual live call | Later, only after SAN + dual DNC scrub + `CALL_OK` | DNC-clear subset; never autodial |

**Why 8–10 (not same-week, not 14+):** mail usually hits the box in ~3–5 business days; day 8–10 is “letter just landed / still on the fridge,” not a cold second pitch and not so late the trigger window drifts. Default **Day 9** unless Examiner later shows a better band.

**Drop owns the calendar:** for each batch, schedule email send = mail_post_date + 9 days (or within 8–10 if weekend/holiday shift). Quill owns a shorter email that **references the letter**, same soft close, same DID — not a new claim set.

**Measurement:** score response as mail-only vs mail+email (and email open/click/reply separately). Do not treat email as optional filler in week 2.

### Three lists (default)
| ID | Source | Role |
|---|---|---|
| **A** | `SELL - 8-9 Months Phone and Email` / SELL-1 | Clock test + first renewal |
| **B** | `SELL-2 landlord renewals` | Coverage question |
| **C** | `SELL-5` cash landlords **or** `SELL-4` entity | Event / named-insured question |

Volume: **100–150 pieces/list** (or ~100 total if producer capacity tight).

### Tracking before drop 1
1. Dedicated DID → always forward to her cell  
2. Tracked email (opens/clicks/replies) — **required for Touch 2**, not optional  
3. Immutable token shared across mail + email ↔ Radar ID  
4. Disposition codes (same-day), tagged by first-touch channel when known

### SAN (third touch later)
Seller (her/agency) owns SAN. First 5 GA codes free; +5 statewide ≈ $410–425/yr. PropertyRadar DNC = Pass-0; official registry scrub = Pass-1 before `CALL_OK`. Manual live only. Mail/email remain touches 1–2.

---

## 4. Copy doctrine — first-class product

### Voice
Short. Simple. Personable. One idea per letter. Sounds like a local agent, not a lead mill.

### Hard rules (`15 §1`)
| Say | Never |
|---|---|
| Records show X / mailing differs / entity on title | “You are uninsured” / “policy will not pay” |
| Happy to compare options | “We know your renewal date” as fact |
| Soft invite | Fake urgency / fake government tone |

**Governing line:** *The event is a reason to start a conversation — not proof of the answer.*

### Structure (one page / postcard-able)
1. **Hook** — property-specific observation (1–2 sentences)  
2. **Why reach out** — seasonal / timing without false certainty (1 sentence)  
3. **Offer** — free quote / brief review  
4. **Soft close** — no pressure; ~10 minutes  
5. **CTA** — dedicated DID + QR (and email if used)  
6. **Sign-off** — her name, State Farm / license as compliance allows  

### Soft close (default — Quill may tune)
> No pressure at all. If you’d like a free quote, I’d be happy to help — it won’t take more than about ten minutes of your time. Call or text [DID], or scan the code.

### Example skeleton (first renewal — illustrative)
> Hi [Name],  
>  
> I’m [Producer], a local State Farm agent. Public records show [Address] changed hands in the last year or so, and a lot of Georgia homeowners are looking at coverage again as renewals come through.  
>  
> I don’t know how your policy is set up today — I’m just offering a quick, no-obligation comparison.  
>  
> No pressure at all. If you’d like a free quote, I’d be happy to help — it won’t take more than about ten minutes. Call or text [DID], or scan the code.  
>  
> [Producer] · [License #]

Landlord / entity variants swap only the observation paragraph; keep the same soft close.

### Quill QA gate (before any print)
- [ ] Under ~150–180 words  
- [ ] One CTA  
- [ ] Soft close present  
- [ ] No forbidden claims  
- [ ] DID + QR correct  
- [ ] Producer signed off for SF compliance  

---

## 5. Measurement (Examiner)

| Metric | Label | Use |
|---|---|---|
| Response rate by list | primary | Creative vs trigger |
| Response vs days-to-anniversary (A) | primary | Clock thesis |
| Channel mix | primary | DID vs QR vs email |
| Time-to-answer | ops | Switchboard SLA |
| Quote / bind | **[SF] only** | Directional — not Model 3 pricing |

**Green/learn bands:** ≥1.5% keep; 1–1.5% one creative iteration; &lt;1% kill list/trigger before spend.

---

## 6. 30-day build order

| Week | Deliverable |
|---|---|
| 0 | Create Tier-1 bots; DID live; token sheet; freeze A/B/C counts |
| 1 | Quill: 3 letters + soft close; producer compliance OK; Drop: first mail batch |
| 2 | Inbounds flowing; **Touch-2 email at day 8–10** on email rows; Examiner first scorecard |
| 3–4 | Second drop / follow-up; decide kill/iterate; SAN for DNC-clear third touch if ready |

---

## 7. What “getting ALMANAC right” means

Not a perfect national lead marketplace on day one.  

**Right =** measurable response from personable mail + a producer who answers + a factory that can repeat. First revenue can be her book’s new policies and/or the proof that lets you sell the system to an independent next.

