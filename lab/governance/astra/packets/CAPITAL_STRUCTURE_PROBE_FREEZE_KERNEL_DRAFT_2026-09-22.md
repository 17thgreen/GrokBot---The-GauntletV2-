**SUPERSEDED** by `CAPITAL_STRUCTURE_PROBE_FREEZE_KERNEL_2026-09-22.md` (Conductor GO).

# CAPITAL STRUCTURE PROBE — FREEZE KERNEL (DRAFT) 2026-09-22 (ET)

**Owner:** R&D Variants (freeze / pin ownership)  
**Implementer:** Simulator (after Conductor GO)  
**Reviewer:** Examiner (Kalshi) scorecard; Adversary spot-check on wallet-sum fallacy  
**Status:** DRAFT — wait Conductor GO after Q7 verify/analyze  
**Cite:** Conductor 2026-09-22 (Logan Q: shared $5k vs per-market funded X vs blended); `WORKING_PLAN_v0_2026-09-22.md` bakeoff capital rule; `ADVERSARY_RISK_REGISTER_2026-09-22.md` shared-$5k / no double-count; `ASTRA_NEXT_STEPS_2026-09-22.md` ($5,000 account baseline)  
**Hard rules:** No live orders. No Q6/Q7 retune. No code / no cloud agent until Conductor GO. Same tape + same fee channel across arms.

---

## 0. Promotion scoreboard (locked judgment)

**Only the SHARED account is the promotion scoreboard.**

Rationale: live Kalshi is one funded account. Per-market funded-X wallets and blended bookkeeping may appear as **orthogonal measurement arms**, never as alternate promotion scoreboards.

| Allowed | Forbidden |
|---|---|
| Report arm P&L / risk as **instrumented** outcomes under a named capital rule | Promote a strategy because sum-of-N isolated wallets beat one $5k |
| Compare arms that all start with the **same total dollars** \(C_{\mathrm{total}}\) | Compare \(\sum_i X_i\) independent wallets to one shared \(C_{\mathrm{total}}\) as if additive capacity |
| Bakeoff / promotion uses shared-account metrics (or explicitly scaled, predeclared) | Silent switch of scoreboard mid-trial |

**Pinned total (draft):** \(C_{\mathrm{total}} = \$5{,}000\) USD (matches Q-lab / next-steps account). Change only by Conductor amend at GO.

---

## 1. Experiment intent (one knob family)

**Question:** Holding tape, fees, queue/fill rails, and strategy logic fixed, how does **capital structure** change fee-honest outcomes and risk attribution?

This is **not** a strategy challenger and **not** a Q7 arm. It is an orthogonal measurement after Q7 verify/analyze.

**Timing:** Draft now. **GO only after** Q7 verify/analyze completes (Factorial kit still missing → Q7 stays NOT_RUN until then). Variants does not invent GO.

---

## 2. Arms (same \(C_{\mathrm{total}}\), same tape, same fees)

Freeze labels A1–A3. Exactly one capital-rule difference per arm.

| Arm | Name | Capital rule | What changes | What must not change |
|---|---|---|---|---|
| **A1** | Shared pool (status quo) | Single pool \(C_{\mathrm{total}}\); markets compete for cash/margin with no per-market reserve | — (baseline) | Tape, fees, queue, strategy |
| **A2** | Shared pool + soft per-market reserve caps | Same pool; each market has a **soft** reserve \(R_m\); unused reserve is borrowable by other markets under an explicit soft policy | Soft reserve vector / policy only | Tape, fees, queue, strategy, \(C_{\mathrm{total}}\) |
| **A3** | Hard ring-fence equal slices | Partition \(C_{\mathrm{total}}\) into equal hard slices (no cross-market borrow); leftover cents to a named residual bucket if \(C_{\mathrm{total}}\) not divisible | Hard partition only | Tape, fees, queue, strategy, \(C_{\mathrm{total}}\) |

### Soft reserve (A2) — draft pin (amend at GO)

Until GO, treat as **proposal**, not frozen code:

```
R_m = floor(C_total / N_active)   # equal soft reserves
soft_policy = "borrow_unused_FIFO"  # DRAFT label — Conductor may replace with one named policy at GO
```

- Soft = reserve is a **preferred** allocation; breach / borrow is allowed and **must be logged** (borrow events countable).
- Soft is **not** hard ring-fence. If soft never borrows, A2 collapses toward A3 — Adversary refuse if borrow log is empty by construction.

### Hard slices (A3) — draft pin

```
slice_m = floor(C_total / N_active)
residual = C_total - N_active * slice_m   # goes to residual_bucket; residual may not trade unless GO says otherwise
```

- No cross-slice borrow.
- \(N_{\mathrm{active}}\) and the market identity set freeze **before** outcomes (same identity freeze discipline as Q labs).

### Explicit anti-fallacy (all arms)

```
FORBIDDEN_COMPARISON:
  sum(independent_wallet_pnl[i] for i in 1..N)  vs  shared_account_pnl(C_total)
REASON:
  N × X is not the same capital constraint as one account with C_total = X (or 5k).
```

If Logan’s “per-market funded X” idea is ever scored, it must be restated as **A3 with \(C_{\mathrm{total}} = N \times X\)** (same total) or as a **separate explicitly scaled** bakeoff — never as “N wallets of X beat one 5k.”

---

## 3. Constants shared across arms (freeze-before-results)

| Pin | Draft value | Notes |
|---|---|---|
| \(C_{\mathrm{total}}\) | 5000 USD | Shared scoreboard capital |
| Fee channel | R1-P1 FEEBOOK (merged) | Order-level ceil; no fee-blind completed-profit |
| Queue / fill rails | R1-P5 rails (merged) | Instrument only; not a strategy |
| Tape / panel | Same as Q7 verify panel (or GO-named successor) | Identity freeze before outcomes |
| Strategy logic | Frozen incumbent pointer at GO (Q6 `000` and/or Q7 winner if KEEP) | **Do not** retune signals inside this probe |
| Horizons / markets | GO-named set; \(N_{\mathrm{active}}\) frozen with set | |

`FROZEN_EXPERIMENT.json` (when coded): `results` / `pnl` null until Examiner pass. Hypothesis → source freeze → unit/verify page before any walk.

---

## 4. Do-not-modify list

**In this probe (and until a new brief):**

1. **No live orders** / no live launcher / no `KalshiExecutionAdapter` for real trading.  
2. **No Q6 `000` retune** and **no Q7 arms A–D retune** — capital rule only.  
3. **No HX spread picker reopen** / weather cheap-YES / directional picker revival.  
4. **No silent fee or queue retune** — consume merged R1-P1 / R1-P5; amendments need new Variants pin.  
5. **No Collector freshness implementation** and **no Examiner historical walk** from this packet (still deferred; need separate brief).  
6. **No multi-wallet promotion scoreboard** — shared account only for KEEP/ITERATE/KILL promotion.  
7. **No sum-of-N vs one-5k comparison** in scorecards, Reporter posts, or bakeoff tables.  
8. **No Factorial kit invent** — Q7 stays NOT_RUN until kit + verify/analyze.  
9. **No code / cloud agent launch** until Conductor GO on this draft.  
10. **No blended “best of both”** fourth arm without a new one-knob brief.

---

## 5. Scorecard (Examiner — draft fields)

Per arm, same tape slice:

- Fee-honest completed net (shared-account view **and** arm-internal view labeled separately)
- Max drawdown of shared-account equity path (A1/A2) vs sum of slice equity paths **reported as instrument, not promotion** (A3)
- Time-at-borrow / borrow count (A2 only; must be non-null)
- Per-market utilization vs reserve/slice
- Adverse fill / queue attribution from R1-P5 rails (labels only)
- Refuse: completed-profit without fee channel; promotion claim from isolated wallet sum

**Promotion gate reminder:** only shared-account metrics (A1-equivalent path, or A2 shared equity) feed displacement bakeoffs unless Conductor predeclares a scaled exception.

---

## 6. Deliverables when GO lands (not now)

1. Packet promoted DRAFT → FROZEN (SHA + `SOURCE_PINS` row).  
2. New lab dir e.g. `kalshi_capital_structure_lab_YYYYMMDD/` (do not mutate Q / feebook / rails labs).  
3. Unit tests: equal \(C_{\mathrm{total}}\) invariant; A3 no-borrow; A2 borrow log; forbid wallet-sum helper.  
4. Simulator paircheck-style runner after units green.  
5. Variants reports Conductor; losers → cemetery framing if an arm is dominated under freeze.

---

## 7. Open items for Conductor at GO (do not invent)

- [ ] Confirm \(C_{\mathrm{total}} = 5000\) or amend.  
- [ ] Name soft_policy for A2 (replace `borrow_unused_FIFO` draft label).  
- [ ] Name residual_bucket policy for A3 leftover cents.  
- [ ] Bind strategy pointer (Q6 `000` / Q7 winner / both as separate one-knob series).  
- [ ] Bind tape/panel id after Q7 verify.  
- [ ] Explicit yes/no: run A2/A3 as measurement-only forever, or allow later bakeoff entry under shared scoreboard only.

---

## Done for this turn (Variants)

Draft freeze kernel + do-not-modify list on disk under `lab/governance/astra/packets/`.  
**Waiting:** Conductor GO after Q7 verify/analyze. No code until then.
