# PropertyRadar list audit — 2026-09-14

**Source:** live Discover Copy from `SELL - 8-9 Months Phone and Email` (no overwrite, no export).  
**As-of:** 2026-09-14.

## Primary list chips (base)

| Chip | Value |
|---|---|
| State | Georgia |
| Type | Single Family |
| Owner Occ? | Yes |
| Site Vacant? | No |
| Owner Type | Couple, Individual |
| Owner Mobile Phone? | Yes |
| Owner Email? | Yes |
| Est Value | 250000+ |
| Purchase Date | **12/10/2025 – 01/10/2026** |
| Listed for Sale? | No |
| **Count** | **1,904** |

**Clock read:** purchases ~8–9 months ago, but anniversaries land ~**87–118 days** ahead — **outside** the ~45–70 / −70 to −45 carrier letter band. Good contact gates; wrong month band for “letter is coming.”

## Experiment A — rolling first-renewal (45–70d anniversary)

| Change | Purchase Date **10/29/2025 – 11/23/2025** (other chips held) |
|---|---|
| Count | **1,694** |
| Anniversary | ~45–70 days ahead from 2026-09-14 |

## Transfer Month

- Path: Add Criteria → Sales & Transfers → All Transfers → **Transfer Month**
- Help (exact sense): purchase month = transfer month = anniversary date; useful for annual reminders in the month they originally purchased.
- Values: **month-of-year only** (Jan–Dec), not month+year.
- Test: Oct + Nov on the **original** 1,904 base → **729** (AND with existing Dec–Jan purchase band → intersection shrinks; expected).
- Combined Oct+Nov + rolling 10/29–11/23 band: **not separately verified** in this pass.

## Multiple date ranges

**Not verified** — do not assume OR vs AND / last-wins until a dedicated Discover test.

## Recommended recipes (do not overwrite production until Logan signs)

### A · First-renewal clock (falsifier / pilot)
Keep: GA, SFH, Owner Occ Yes, Vacant No, Couple+Individual, Mobile Yes, Email Yes, Listed No, Est Value 250k+ (revisit floor later).  
**Purchase Date:** rolling band whose anniversaries are **45–70 days ahead** (recompute each drop; example as-of 2026-09-14: 10/29/2025–11/23/2025).  
Optional: align ALMANAC own mail to −90/−45 relative to anniversary, not only carrier letter window.  
Do **not** use Last Transfer.

### B · Multi-year same-season (rate-hike / scale)
Keep contact + occupancy gates.  
**Transfer Month:** months whose anniversary season matches the campaign (e.g. Oct+Nov for a fall letter drop).  
**Purchase / Sale Date:** broad multi-year span (e.g. 2019–2024 or 2021–2025) — validate count before production.  
Prefer Purchase/Sale Date for tenure; Transfer Month for season.  
If multiple ranges OR: year-stacked same-season bands are cleaner than one fat blob (still untested).

### C · Creative baseline (optional control)
Last-12-months any month, same other chips — only if Examiner needs clock vs letter isolation.

## Non-goals this pass
No scratch lists saved. No exports. Multiple-range OR untested. SELL-2 / SELL-4 / SELL-5 not fully re-copied in wrap.
