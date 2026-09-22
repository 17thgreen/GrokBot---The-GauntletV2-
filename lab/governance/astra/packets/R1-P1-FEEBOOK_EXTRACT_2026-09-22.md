# R1-P1-FEEBOOK — EXTRACT + PIN SPEC 2026-09-22 (ET)

**Owner:** R&D Variants (freeze / pin ownership)  
**Implementer:** Cloud agent → Simulator review  
**Reviewer:** Examiner (Kalshi) — tests only  
**Status:** PINS ON DISK (governance); code PR pending  
**Cite:** `SIBLING_DEATHMATCH_REVIEW_2026-09-22.md`; `briefs/R1_DEEP_RESEARCH_2026-09-22.md` §R1-P1  
**Repo:** `https://github.com/17thgreen/GPT-6-Astra-Deathmatch`  
**Hard rules:** No Q6/Q7 retune. No live orders. New lab directory preferred (do not mutate frozen Q labs).

---

## Sources pinned (sibling SHAs)

| Kernel | Repo | Ref | Path |
|---|---|---|---|
| Claude FeeModel | `17thgreen/Claude-SportsBetting-Competition-to-the-Death` | `claude/kind-hamilton-gdfr9q` @ `11e00f182e0fa1f97ed80eb69fec1269d43d8f5a` | `src/flatstake/paper/fees.py` |
| Grok fees.ts | `17thgreen/Grok-Deathmatch` | `main` @ `2b343c2af2917ba1c98076eb6d9b5ff635a6532c` | `src/lib/linewright/fees.ts` + `config.ts` `EXCHANGE_V1` |
| Venue docs | Kalshi | public | orderbook reciprocity; fee schedule PDF / fee-schedule page |

Local mirrors (text extracts): `packets/extracts/claude_fees.py.txt`, `packets/extracts/grok_fees.ts.txt`

---

## Pin A — Reciprocal YES/NO book algebra (bids-only)

Kalshi books are bids-only. Complementarity:

```
ask_YES = 1 − best_NO_bid
ask_NO  = 1 − best_YES_bid
bid_YES = best_YES_bid          # as reported
bid_NO  = best_NO_bid
spread_YES = ask_YES − bid_YES = 1 − best_NO_bid − best_YES_bid
```

**Unit fixtures required:** reconstruct asks from a captured bids-only fixture; refuse completed-profit claims if fee channel missing (minimal refuse gate).

---

## Pin B — Fee formula (order-level, venue-shaped)

Published shape (Deep Research / siblings agree on rates):

```
raw = M × rate × C × P × (1 − P)
fee = round_up_to_cent(raw)     # Math.ceil(raw*100 - eps)/100
fee = min(fee, 0.035 × C)       # Claude per-contract cap; pin as optional series flag
```

| Role | rate | Notes |
|---|---|---|
| taker | 0.07 | Always ceil to cent on the **order** |
| maker | 0.0175 | Claude: ceil when `round_up=True`; Grok paper: **unrounded** for microstructure study |
| maker (some series) | 0 | `maker_fees_enabled=False` / series override stub |

**Partial fills (Claude discipline — pin for Astra):** apply `round_up=False` on partials so the order-level cent ceiling is not multiplied per partial; omitted rounding ≤ 1¢/order.

**Grok vs Claude discrepancy (document in tests, do not silently merge):**

| Aspect | Claude `FeeModel` | Grok `fees.ts` |
|---|---|---|
| Contract count `C` | Yes — order-level | Per-unit (C=1 implicit) |
| Maker rounding | ceil when round_up | unrounded |
| Cap | `$0.035` per contract × C | none in fees.ts |

**Astra R1-P1 default:** Claude order-level + ceil + optional cap; series `M` / maker-fee flag table stub (JSON). Grok unrounded maker retained as **paper-role** comparator only (for MICRO / Adversary), not as Examiner completed-profit channel.

---

## Pin C — Minimal refuse gate

Scorecard helpers must refuse labeling a run “completed profit” unless a fee channel is present (taker/maker fee fields non-null and formula_id pinned). Extrapolations stay labeled projections.

---

## Deliverables (code — cloud agent)

1. New dir e.g. `nfl_feebook_lab_20260922/` (or `kalshi_feebook_lab_20260922/`) with:
   - `EXPERIMENT_SPEC.md` + `FROZEN_EXPERIMENT.json` **before** any result files
   - `feebook.py` (Decimal preferred) implementing Pin A + Pin B
   - `series_fee_table.stub.json` (M=1, maker enabled; empty overrides)
   - `tests/test_feebook.py` with PDF/public examples + Claude/Grok cross-check table
   - Registry pointer update only after freeze commit
2. Do **not** change `nfl_factorial_lab_20260921`, Q7 paircheck arms, or allocator code.
3. No live orders / credentials.

## Done = 

Pins in this MD + extracts on disk; cloud agent PR opened with passing unit tests; Variants reports Conductor.

## Follow-on

R1-P5-RAILS (see `R1-P5-RAILS_EXTRACT_2026-09-22.md`) after R1-P1 fee algebra lands.
