# R3-P3 COLLECTOR STUB — settled public tape panel 2026-09-22 (ET)

**To:** The Collector (GET-only)  
**From:** R&D Variants (Conductor maximize-next after PR11)  
**Freeze:** `packets/R3-P3_FL_MAKER_TAKER_BANDS_FREEZE_KERNEL_2026-09-22.md`  
**Status:** STUB — kick only; no strategy; no live orders

## Ask
Stand up a **bounded settled public trades + resolution** capture/admission path for R3-P3 (Maker/Taker + favorite–longshot 10¢ bands).

## Requirements
1. GET-only public trades with native `taker_outcome_side` / `taker_book_side` (refuse Lee-Ready).  
2. Join resolutions for settled markets.  
3. Prefer weather/politics/economics first; avoid frozen S1/S4/S5/R2-P3 series as first panel.  
4. Pre-register 10¢ bands **before** looking at outcomes (Examiner checklist).  
5. Fee channel for post-fee ROI later = R1-P1 @ `22371178…` (post-Apr-2025 maker) — Collector need not compute ROI.  
6. Coverage report / panel version with real UTC admit stamps; no backfill of past windows.

## Out of scope
- No private order routes / no demo resting / no live orders  
- No Q6-000 retune / no capital A2/A3  
- No inventing PnL or citing paper +2.6% as evidence

## Suggested landing
`lab/astra-capture/r3-p3-fl-maker-taker/` (panel JSON + sqlite/coverage) — Collector chooses concrete layout.

## Stubbed-at
`2026-09-23T00:12:00.364598+00:00` UTC
