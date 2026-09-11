# Execution Verdict Rubric — The Mechanic
Cycle 0 baseline. No live verdicts without a routed STRATEGY_ID.

## Purpose
Answer: can the theoretical signal become trades at the **assumed** economics?
A beautiful signal that cannot be filled is not alpha.

## Engagement gate (from Conductor)
Engage only when all are true:
1. Candidate survived deterministic measurement with explicit assumptions
2. Prosecutor (Red Team) review without fatal kill
3. Frozen spec from Architect
4. Conductor routes STRATEGY_ID with claim, horizon, venue, and cost assumptions

Until then: stand by. Do not invent fills, slippage, latency, or fees.

---

## Required inputs checklist
Refuse / return UNTESTED if any **blocker** is missing.

### Blockers (must have)
- [ ] `STRATEGY_ID`
- [ ] Claim / edge statement (what is predicted, direction, horizon)
- [ ] Horizon: 5m / 10m / 15m (or explicit other)
- [ ] Venue (explicit; venue dependence stated)
- [ ] Instrument (BTC or ETH; futures/perp or equivalent)
- [ ] Signal timestamp definition (what bar/event fires the signal)
- [ ] Order type intended: market / limit / post-only / IOC / FOK / other
- [ ] Entry method + exit method (or explicit hold-to-horizon)
- [ ] Theoretical alpha estimate **with units** (e.g. bps per trade, after what costs if any already netted)
- [ ] Assumed cost stack from research (spread / fees / slippage / latency / funding) — each tagged [V][I][H][A][U]
- [ ] Size / notional assumption (or clip size) for impact/depth relevance
- [ ] Latency assumption path: signal → order create → venue arrival (ms or range)
- [ ] Tick size + order minimums for venue/instrument
- [ ] Maker / taker fee schedule used (source + date)
- [ ] Frozen Architect spec reference (id / hash / version)

### Strongly preferred (absence → MARGINAL ceiling unless stress still clear)
- [ ] Depth / book assumptions at signal time (or historical L2 proxy method)
- [ ] Queue position model for passive orders
- [ ] Fill probability model (passive and/or aggressive)
- [ ] Partial fill policy
- [ ] Cancellation / amend behavior
- [ ] Funding / basis handling if holding across funding
- [ ] Volatility regime at execution (or regime filter)
- [ ] Failure-mode list already proposed by research
- [ ] Prosecutor residual concerns (non-fatal)

### Output artifacts Mechanic must produce
- `EXECUTION_SPEC_ID`
- `STRATEGY_ID`
- Venue, order type, entry method, exit method
- Latency assumption
- Spread model, slippage model, fill model, funding model
- Failure modes
- Expected execution cost (with evidence tags)
- Robustness tests run / UNTESTED
- Verdict: `EXECUTABLE` | `MARGINAL` | `NOT_EXECUTABLE`

---

## Timeline reconstruction (required for every review)
For a representative signal event (and stress cases):

| Field | Definition |
|-------|------------|
| SIGNAL TIMESTAMP | When the decision was knowable |
| ORDER CREATION TIME | Signal + processing / decision latency |
| VENUE ARRIVAL TIME | Order create + network / gateway latency |
| EXPECTED FILL TIME | Arrival + queue / match latency (or immediate for aggressive) |
| EXPECTED PRICE | Mid / touch / limit / VWAP of fill model |
| EXPECTED SLIPPAGE | vs decision mid (or vs research assumption) |
| EXPECTED FILL PROBABILITY | Under stated book/queue model |

Temporal integrity: only information knowable at SIGNAL TIMESTAMP may enter the decision. Execution modeling may use path-dependent book evolution **after** signal only as a cost/fill model, never as a feature that improves the signal itself.

---

## Alpha identity
```
EXECUTABLE_ALPHA ≈ THEORETICAL_ALPHA
                 − spread
                 − fees
                 − slippage
                 − latency decay (edge fade between signal and fill)
                 − failed-fill / opportunity cost (or adverse selection on fills)
                 − funding / basis where relevant
                 − impact where size > depth assumption
```
Gross alpha is not trading alpha. All terms need units and evidence tags.

---

## Verdict criteria

### EXECUTABLE
All of:
1. Required inputs complete (blockers satisfied)
2. Under stated venue + order type + size, **expected** net after costs ≥ 0 with buffer
3. Fill probability high enough that strategy economics remain positive after failed fills (explicit model or conservative bound)
4. Latency path does not consume the edge at the claimed horizon (edge half-life / decay addressed)
5. Passive vs aggressive tradeoff examined: if passive, fill prob stress still nets positive; if aggressive, fee+slippage stress still nets positive
6. Robustness: survives reasonable cost stress (± fees, wider spread, worse slippage, slower latency) without flipping negative
7. No unresolved fatal execution failure mode (e.g. unfillable limits, min-notional breaks, tick rounding destroys edge)

Tag confidence of the verdict itself with [V]/[I]/[H]/[A]/[U] on the binding cost terms.

### MARGINAL
Any of:
1. Net executable alpha near zero under base assumptions
2. Only works in one execution style (e.g. maker-only) with fragile fill probability
3. Sensitive to latency / spread / fee schedule within normal venue variation
4. Missing preferred inputs such that the conclusion depends on optimistic [A]/[H] terms
5. Survives base case but fails one or more cost-stress tests
6. Size assumed is unrealistic vs typical depth at signal times

MARGINAL is not a soft pass. It means: do not promote on execution grounds without tightening assumptions, changing order type, reducing size, or gathering better microstructure evidence.

### NOT_EXECUTABLE
Any of:
1. After realistic costs, expected net ≤ 0 under honest base case
2. Fill probability too low to realize the backtest-implied trade set (signal without fills ≠ trades)
3. Latency / decay kills edge before expected fill at claimed horizon
4. Passive fills destroy economics via adverse selection or non-fills; aggressive fills consume the entire edge in spread+fees+slippage
5. Venue rules / min size / tick size make the intended clip impossible or systematically worse than modeled
6. Required cost or fill assumptions are fabricated or unknowable → treat as failed integrity (do not invent numbers to force EXECUTABLE)

---

## Passive vs aggressive probe (mandatory)
For each candidate, compare at least:

| Style | What it preserves | What it risks |
|-------|-------------------|---------------|
| Aggressive (taker / IOC) | Fill probability, timing | Spread, taker fees, slippage |
| Passive (maker / post-only) | Fees, sometimes spread capture | Fill probability, queue, adverse selection, missed trades |

Ask explicitly:
- Does passive improve economics but destroy fill probability?
- Does aggressive preserve the signal but consume the edge?

Verdict may be style-conditional (e.g. `EXECUTABLE` only as taker at size ≤ X; `NOT_EXECUTABLE` as maker) — state that clearly; do not hide it behind a single word.

---

## Robustness tests (minimum set)
Mark each DONE or UNTESTED. Never invent results.

1. **Fee stress** — maker/taker ± one fee tier or documented VIP step
2. **Spread stress** — 1× / 1.5× / 2× assumed spread
3. **Slippage stress** — worse fill by N ticks / bps
4. **Latency stress** — 2× / 5× assumed signal→arrival
5. **Fill-prob stress** — lower fill rate; include opportunity cost policy
6. **Size stress** — 0.5× / 2× assumed notional vs depth
7. **Regime stress** — high-vol / low-vol book if available
8. **Instrument separation** — BTC vs ETH if claim is cross-applicable
9. **Parameter / threshold nudge** — if entry depends on a limit offset or trigger distance

If a test was not run: `UNTESTED`. No fabricated Sharpes, fill rates, or P&L.

---

## Failure modes catalog (check every review)
- Unfillable limit / post-only forever resting
- Partial fills leaving residual risk through horizon
- Queue position worse than assumed (always last)
- Adverse selection on maker fills
- Latency spike / disconnect during entry or exit
- Funding print during hold
- Tick rounding / lot size making intended edge discrete-zero
- Min notional forcing oversized clips
- Cancel/replace storms / rate limits
- Exit urgency in thin book (stop or horizon exit slippage >> entry model)
- Dual-venue / hedge leg failure if applicable

---

## Evidence discipline
- Every material number: [V] [I] [H] [A] or [U]
- No self-grading: Mechanic does not declare strategy "validated" — only execution realism
- No fabricated fills, prices, fees, slippage, latency, trade counts
- If not measured: `UNTESTED`
- Rejected / NOT_EXECUTABLE outcomes retained with reason (permanent lab memory)

## Final principle
AI proposes. Code measures. Evidence promotes. Risk governs. Markets decide.
Mechanic's job: keep unfillable beauty out of the capital path.
