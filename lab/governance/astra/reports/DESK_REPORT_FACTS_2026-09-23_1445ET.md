# DESK_REPORT_FACTS — 2026-09-23 14:45 ET

Gather scope: `/workspace/lab` + `/home/box/.secrets` metadata only. No secret values printed. No orders placed.
Primary pulse: `lab/governance/pulses/PULSE_2026-09-23_1413ET.md`.
Post-pulse packet confirms: ATP-FQ PR34 MERGED + Examiner ACK READY NOT_SCORED; ETH-FQ FREEZE ACCEPTED implement:true; DEMO_KEYS_VERIFIED; Mechanic first demo poll.

---

## 1) SCOREBOARD_ROWS

| line | dollar_pnl_or_null | pct_or_null | funded | sample_size | status | notes |
|---|---:|---:|---|---|---|---|
| Q6 `000` | 345.24 | 6.90 | $5000 shared pool | 31-game DEV | KEEP shadow incumbent | = Q7 Arm D; fee-honest; live_promotion DENIED |
| Q7 Arm D | 345.24 | 6.90 | $5000 shared pool | 31-game DEV | SCORED · reference KEEP | primary `q3300_d0.25`; packet CLOSED |
| Q7 Arm B | 290.99 | 5.82 | $5000 shared pool | 31-game DEV | SCORED · KILL candidacy | B/D=0.843 fails 95% bar; cemetery CEM-ASTRA-20260922-001 |
| Q7 Arm C | 205.94 | 4.12 | $5000 shared pool | 31-game DEV | SCORED · ablation | not a candidate |
| Q7 Arm A | 201.52 | 4.03 | $5000 shared pool | 31-game DEV | SCORED · control | original router · check off |
| ADMIT-1 | null | null | n/a (capture not P&L) | 16-event panel; recorder run | LIVE capture | pid **1251007** · started 2026-09-23 09:17:45 ET · `--seconds 86400` · etime now 05:29:47 · pulse active_markets=0 pre T−7d · WAL idle since ~09:18 (metadata polls continue) |
| C1-KXUFCFIGHT | null | null | — | — | ADMITTED · Examiner NOT_SCORED | empty books pin `e07d09f1…` · EMPTY-OB gate MERGED PR30 |
| Cap-SR soft blended (SR0/SR1/SR2) | null | null | — | — | MERGED instrument (PR20) · NOT_SCORED | pnl null |
| Cap-SR-FX effects (FX0/FX1) | null | null | — | — | MERGED (PR24) · NOT_SCORED | pnl null |
| C5 honesty harness | null | null | — | — | MERGED (PR21) · NOT_SCORED | pnl null |
| C3 bordering harness | null | null | — | — | MERGED (PR22) · NOT_SCORED | pnl null |
| R3-P3 FL maker/taker | null | null | — | — | MERGED (PR23) · NOT_SCORED | Lee-Ready REFUSED |
| S5 MVE fill-vs-legs | null | null | — | — | MERGED (PR25) · NOT_SCORED | pnl null |
| S4 NCAAF fee+queue harness | null | null | — | — | MERGED (PR26) · ACK stub_ready NOT_SCORED | pnl null |
| R2-P3 prop ladder | null | null | — | — | MERGED (PR27) · ACK stub_ready NOT_SCORED | pnl null |
| R3-P4 L2-CAT harness | null | null | — | — | MERGED (PR28) · ACK stub_ready NOT_SCORED | pnl null |
| R2-P5 SOT-ID harness | null | null | — | — | MERGED (PR29) · ACK stub_ready NOT_SCORED | pnl null |
| C1 EMPTY-OB harness | null | null | — | — | MERGED (PR30 `d7b935951c9d…`) · ACK stub_ready NOT_SCORED | pnl null |
| R3-P4 L2-SF harness | null | null | — | — | MERGED (PR31 `ead2cb41d5d1…`) · ACK stub_ready NOT_SCORED | freeze `f0042526…` |
| C2 NHL-FQ harness | null | null | — | — | MERGED (PR32 `677d5d4f0d5e…`) · ACK stub_ready NOT_SCORED | freeze `a36ec351…` |
| C4 CPI-FQ harness | null | null | — | — | MERGED (PR33 `6e55a99790f4…`) · ACK stub_ready NOT_SCORED | freeze `949b2558…` |
| ATP-FQ harness | null | null | — | 13 unit OK ≠ Examiner score | **MERGED PR34** `438f4abf28a3…` · Examiner ACK **READY NOT_SCORED** | post-pulse merge+ACK ~14:26–14:28 ET · arms ATPA0/ATPA1 · build cloud `bc-44c064c2…` · dup PR35 closed |
| ETH-FQ (KXETH15M) harness | null | null | — | — | **FREEZE ACCEPTED** · implement:true · pre-PR | Conductor ACCEPT @14:41 ET · digests match · Examiner HOLD pre-PR · claimed cloud `bc-4589dc64` **absent** from packets/pulses (only mentioned in this facts file) |
| Fee+queue honesty `000` | null | null | — | — | NOT_SCORED · harness on main | pnl null |
| R1-P1 Feebook / R1-P5 Rails | null | null | — | — | MERGED instruments | not strategy scores |
| Capital-structure A1/A2/A3 | null | null | — | — | MERGED rails (PR5) | Cap-SR soft-policy twin |
| R2-P1 / QF / fixture-join | null | null | — | — | MERGED measurement · NOT_SCORED | metrics null |
| R3-P1 fee-cost | null | null | — | — | NOT_SCORED · PR12 merged | demo keys VERIFIED 2026-09-23 → unblocked demo-only; FIXTURE_GAP until demo fills |
| R3-P2 queue_position | null | null | — | — | scaffold · demo-unblocked | DEMO_KEYS_VERIFIED · Mechanic first poll NULL_API (create HTTP 410 deprecated_v1) @14:43 ET |
| R3-P4 L2-shape (parent) | null | null | — | — | NOT_SCORED · PR13 merged | pnl null until Clock-admitted L2 |
| S1 | null | null | — | — | FREEZE ACCEPTED · empty-events deferred | NOT_SCORED |

Q7 packet **CLOSED** (`SCORED_KILL_B_KEEP_000`). No new Examiner **SCORED** card since Q7 close (stubs only).

---

## 2) Q7_ARMS

Sources: `packets/Q7_EXAMINER_SCORECARD_2026-09-22.md`, `reports/RPT-Q7.md`.
Account **$5,000** · sample **31** DEV games (W1+W2) · maker 0.0175 / taker 0.07 · primary `q3300_d0.25` · HISTORICAL_DEV · not live · not annualized.

| arm | role | fee_honest_net_usd | pct_on_5k | sample_size | kill_keep |
|---|---|---:|---:|---|---|
| A | original router · check off (control) | +201.52 | 4.03% | 31 games | control (not candidate) |
| B | original router · check on | +290.99 | 5.82% | 31 games | **KILL** candidacy (`retains_95pct_of_D=false`; B/D=0.843) |
| C | Q6 `000` · check off (ablation) | +205.94 | 4.12% | 31 games | ablation only |
| D / Q6-000 | Q6 `000` · check on (reference) | +345.24 | 6.90% | 31 games | **KEEP** shadow incumbent |

Also: `live_promotion=false` · `NO_NEW_SELECTION` · cemetery `cemetery/CEM-ASTRA-20260922-001_Q7_ARM_B.md`.

---

## 3) SEAT_FACTS

Facts grounded in files dated **2026-09-22 or 2026-09-23** only.

### Archivist
- FACT: registry STATUS board sync 2026-09-23T09:59:00-04:00 — PIT@CLE holdout identity JOINED/HASH_FROZEN.
- FACT: holdout copies under astra-science + astra-src share digest `f8f6b577…` after join.
- FACT: pulse 14:13 — board bump PR19–33 still owed next quiet slot (STATUS still 09:59).
- FACT: indexes PITCLE identity lag watch + hash-freeze packets dated 2026-09-23.

### Collector
- FACT: ADMIT-1 recorder LIVE pid 1251007 since 09:17:45 ET 2026-09-23 (86400s · interval 30).
- FACT: PIT@CLE holdout identity JOINED ~09:55–09:59 ET; not a re-admit; admitted_at remains 2026-09-22T21:18:13Z.
- FACT: pulse — active_markets=0 expected pre T−7d; metadata polls alive; WAL idle since ~09:18.
- FACT: capture sqlite trades=0; metadata responses accumulating.

### Simulator
- FACT: Q7 measurement CLOSED 2026-09-22 (scorecard + RPT-Q7).
- FACT: pulse 14:13 — since 13:20 pulse PR31–33 merged; ATP-FQ ACCEPT+IMPLEMENT kicked (now PR34 merged).
- FACT: DEMO_KEYS_VERIFIED unblocks R3-P1 fee_cost join when demo fills exist — no invent.
- FACT: ETH-FQ ACCEPT implement:true routes implement path pre-PR.

### Examiner (Kalshi)
- FACT: Q7 scorecard stands KILL B / KEEP 000; no new SCORED card.
- FACT: PR31–33 ACK stub_ready NOT_SCORED (pulse); PR34 ATP-FQ ACK READY NOT_SCORED ~14:28 ET.
- FACT: ETH-FQ Examiner HOLD pre-PR stands until branch sha verify + merge.
- FACT: stub scorecards 2026-09-22/23 on disk; metrics/pnl null until Clock admit + Examiner-ready.

### Deep Research
- FACT: latest dated briefs 2026-09-22 under `briefs/` (R1/R2/R3 deep-research + triage ACKs).
- FACT: pulse 14:13 — maximize backlog wait→S2/R2-P4 after C1 PIT@CLE smoke.
- FACT: no 2026-09-23 Deep Research brief found under `briefs/`.
- FACT: hard WAIT unchanged on ungating S1/S2/R2-P4.

### R&D Variants
- FACT: pulse 14:13 — ATP-FQ cloud `bc-44c064c2` running+watched → PR34 MERGED post-pulse.
- FACT: ETH-FQ freeze ACCEPTED implement:true @14:41 ET.
- FACT: MAXIMIZE_PIN ~14:40 ET lists ETH-FQ as active Feature.
- FACT: cloud id `bc-4589dc64` absent from packets/pulses/maximize pins; disk confirms ACCEPT+implement:true only.

### Adversary
- FACT: refuse binds stand (C1/C3/C5, S4/S5, R2-P3, R3-P3, R3 suite, R2-P5 hygiene) — packets 2026-09-22.
- FACT: cemetery untouched except CEM-001 Q7 Arm B.
- FACT: Q6-000 complacency spotcheck filed 2026-09-22 (hygiene; no verdict change).
- FACT: pulse 14:13 — refuse binds stand; cemetery untouched.

### Market Scout
- FACT: cashcow / maximize / Q6 stress / R2P3 slate hunts dated 2026-09-22.
- FACT: ETH hunt packet + panel stub dated 2026-09-23.
- FACT: PIT@CLE identity lag flagged → Collector join (watch packet 2026-09-23).
- FACT: pulse — backlog wait→S2/R2-P4 after PIT@CLE T−7d smoke; ATP optional-watch leftover completed via PR34.

### Reporter
- FACT: BOARD still 2026-09-22 18:47 ET — no new scored line.
- FACT: pulse — next ≥3h brief ~16:20 ET (last WakeParent ~13:20).
- FACT: RPT-Q7 / RPT-Q6-000 / RPT-ADMIT1 on disk; no post-Q7 SCORED card to publish.
- FACT: numbers-only rule from Examiner packets / Simulator ledgers.

### Mechanic
- FACT: SEATS_ASSIGNED_2026-09-22 listed Mechanic not staffed yet; demo path now active.
- FACT: demo key check HOLD cleared by DEMO_KEYS_VERIFIED_2026-09-23.
- FACT: first demo queue poll @14:43 ET — balance GET 200; create order 410 deprecated_v1; verdict NULL_API; no live Astra.
- FACT: authorized demo resting queue_position polls only; cancel-safe; no invent.

### Clock
- FACT: Clock join packets dated 2026-09-22: C1 (join+rejoin), C3, C5, R3-P3 FL maker/taker.
- FACT: Examiner HOLD C1 Clock conditions met packet dated 2026-09-22 on disk.
- FACT: C1 Clock join CONDITIONAL — admit refused / resolution SoT pass on settled N=2; active legs deferred.
- FACT: no new Clock join packet dated 2026-09-23 found under packets/.

### Treasurer
- FACT: **idle / not staffed** — SEATS_ASSIGNED_2026-09-22: Treasurer (near-live only).
- FACT: no Treasurer packet dated 2026-09-22/23 under astra packets.
- FACT: near-live only by charter; pulse shows no Treasurer actions.
- FACT: no live capital movements observed in gather window.

### Conductor-relevant maximize pin
- FACT: latest pin packets/MAXIMIZE_PIN_2026-09-23_1440ET.md.
- FACT: Active Feature ETH-FQ (KXETH15M) — freeze filed; ACCEPT+IMPLEMENT after digest verify (ACCEPT stamped 14:41).
- FACT: UNBLOCKED R3-P2/R3-P1 demo keys (DEMO_KEYS_VERIFIED_2026-09-23).
- FACT: Hard WAIT — S2/R2-P4 until C1 T−7d smoke; S1 empty-events; Cap-SR/QF/L2/EMPTY-OB/SOT-ID/L2-SF/NHL-FQ/CPI-FQ/ATP-FQ reopen; Q6-000 retune; live orders.

### ALMANAC seats (PARKED)
- Radar — PARKED
- Quill — PARKED
- Drop — PARKED
- Switchboard — PARKED
- Examiner ALMANAC — PARKED

### Gauntlet science
- IDLE / capture-only — GAUNTLET_SCIENCE_PAUSE_2026-09-14.md + pulse 14:13.

---

## 4) CAPTURE_HEALTH

| id | pid | state | notes |
|---|---:|---|---|
| LIQ | 159645 | connected | reconnects=6; parse_failures=0; kept_events=6346; last_msg/last_kept seconds-fresh (pulse) |
| PM-006 | 159646 | running | failures=0; n_tokens=8; raw book seconds-fresh |
| PM-008 | 159649 | running | failures=349 (429s non-blocking per pulse); last mid minutes-fresh; series=['KXBTC15M', 'KXETH15M'] |
| CB-002 | 159650 | running | failures=3 lifetime; last bar minutes-fresh; products=['BTC-USD', 'ETH-USD'] |
| PM-009 | 1902503 | **done** | updated_at=2026-09-14T21:53:08Z; ok=4 empty=0 skip=714 fail=0; Starter done |
| ADMIT-1 | 1251007 | running | etime 05:29:47 of 86400; active_markets=0 (pulse); trades=0; metadata polls continue |

---

## 5) WATCHES

| watch | fact | which files say which |
|---|---|---|
| C1 PIT@CLE T−7d SoT | **2026-09-24 23:15 ET** (`2026-09-25T03:15:00Z`) | PITCLE identity lag watch + holdout identity join hash-freeze packets 2026-09-23; registry PACKET_INDEX / STATUS_2026-09-23 |
| C1 PIT@CLE holdout-derived watch deadline | **2026-09-24 20:15 ET** (Δ −3.0h vs SoT; R2-P5) | same PITCLE watch/hash-freeze packets; also pulse 14:13 ADMIT-1 row |
| S2 / R2-P4 | **WAIT** until C1 PIT@CLE T−7d smoke | pulse 14:13; MAXIMIZE_PIN_1440ET; ETH freeze excluded list |
| S1 | **deferred** (empty-events) | pulse scoreboard; MAXIMIZE_PIN hard WAIT |

---

## 6) CHART_DATA_JSON

```json
{
  "q7_arms": [
    {
      "name": "A",
      "pnl_usd": 201.52,
      "pct": 4.03
    },
    {
      "name": "B",
      "pnl_usd": 290.99,
      "pct": 5.82
    },
    {
      "name": "C",
      "pnl_usd": 205.94,
      "pct": 4.12
    },
    {
      "name": "D",
      "pnl_usd": 345.24,
      "pct": 6.9
    }
  ],
  "harness_pipeline": [
    {
      "name": "C1 empty-books pin",
      "pr": 19,
      "status": "MERGED \u00b7 NOT_SCORED \u00b7 tip=n/a"
    },
    {
      "name": "Cap-SR soft blended",
      "pr": 20,
      "status": "MERGED \u00b7 NOT_SCORED \u00b7 tip=45863037"
    },
    {
      "name": "C5 honesty",
      "pr": 21,
      "status": "MERGED \u00b7 NOT_SCORED \u00b7 tip=ee69245a"
    },
    {
      "name": "C3 bordering",
      "pr": 22,
      "status": "MERGED \u00b7 NOT_SCORED \u00b7 tip=63764496"
    },
    {
      "name": "R3-P3 FL maker/taker",
      "pr": 23,
      "status": "MERGED \u00b7 NOT_SCORED \u00b7 tip=cfd5f95a\u2026"
    },
    {
      "name": "Cap-SR-FX effects",
      "pr": 24,
      "status": "MERGED \u00b7 NOT_SCORED \u00b7 tip=79347f0e\u2026"
    },
    {
      "name": "S5 fill-vs-legs",
      "pr": 25,
      "status": "MERGED \u00b7 NOT_SCORED \u00b7 tip=6626c6892298\u2026"
    },
    {
      "name": "S4 NCAAF fee+queue",
      "pr": 26,
      "status": "MERGED \u00b7 ACK stub_ready NOT_SCORED \u00b7 tip=d7584dd4\u2026"
    },
    {
      "name": "R2-P3 prop ladder",
      "pr": 27,
      "status": "MERGED \u00b7 ACK stub_ready NOT_SCORED \u00b7 tip=3b0d1429\u2026"
    },
    {
      "name": "R3-P4 L2-CAT",
      "pr": 28,
      "status": "MERGED \u00b7 ACK stub_ready NOT_SCORED \u00b7 tip=e54554ff\u2026"
    },
    {
      "name": "R2-P5 SOT-ID",
      "pr": 29,
      "status": "MERGED \u00b7 ACK stub_ready NOT_SCORED \u00b7 tip=6f1e22e15d88\u2026"
    },
    {
      "name": "C1 EMPTY-OB",
      "pr": 30,
      "status": "MERGED \u00b7 ACK stub_ready NOT_SCORED \u00b7 tip=d7b935951c9d\u2026"
    },
    {
      "name": "R3-P4 L2-SF",
      "pr": 31,
      "status": "MERGED \u00b7 ACK stub_ready NOT_SCORED \u00b7 tip=ead2cb41d5d1\u2026"
    },
    {
      "name": "C2 NHL-FQ",
      "pr": 32,
      "status": "MERGED \u00b7 ACK stub_ready NOT_SCORED \u00b7 tip=677d5d4f0d5e\u2026"
    },
    {
      "name": "C4 CPI-FQ",
      "pr": 33,
      "status": "MERGED \u00b7 ACK stub_ready NOT_SCORED \u00b7 tip=6e55a99790f4\u2026"
    },
    {
      "name": "ATP-FQ",
      "pr": 34,
      "status": "MERGED \u00b7 ACK READY NOT_SCORED \u00b7 tip=438f4abf28a3\u2026"
    },
    {
      "name": "ETH-FQ",
      "pr": null,
      "status": "FREEZE ACCEPTED \u00b7 implement:true \u00b7 pre-PR HOLD"
    }
  ],
  "capital": {
    "shared_pool": 5000,
    "scored_best_pnl": 345.24,
    "scored_best_pct": 6.9
  }
}
```

---

## Secrets metadata (values not printed)

| file | mode | bytes | mtime |
|---|---|---:|---|
| `/home/box/.secrets/KALSHI_DEMO_API_KEY_ID` | 600 | 36 | 2026-09-23 14:40:37 ET |
| `/home/box/.secrets/KALSHI_DEMO_PRIVATE_KEY` | 600 | 119 | 2026-09-23 14:40:52 ET |
| `/home/box/.secrets/POLYORDERBOOKS_API_KEY` | 600 | 48 | 2026-09-21 01:44:34 ET |

DEMO_KEYS_VERIFIED_2026-09-23: signed demo balance GET HTTP 200; Ed25519; R3-P2/R3-P1 unblocked demo-only.

