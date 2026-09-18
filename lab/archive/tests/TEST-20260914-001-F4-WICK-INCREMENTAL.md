# TEST-20260914-001 — F4-WICK-INCREMENTAL vs MKT-KALSHI-15M-MID

**TEST_ID:** `TEST-20260914-001`
**Package:** `F4-WICK-INCREMENTAL`
**Feature:** `DRAFT-FEAT-20260914-008` (wick-gated structural Φ(z) blend, θ=1.5 W=5 λ=0.35 frozen)
**Gate:** `DRAFT-ABST-20260914-008` (speak-eligible only on BTC/ETH T-5m mid with W=5 lock-B lookback)
**Incumbent:** `MKT-KALSHI-15M-MID` (same-t PM-004 mid)
**Purpose:** F4 wick-gate incrementality of structural Φ(z) blend vs Kalshi mid on two AMD-005 headlines (full cell; off-wick Δ=0 by construction)
**DATA:** `DATA-PROV-PM-004` + `DATA-PROV-L3-002` lock B + `DATA-PROV-L3-001` Sep-11 edges/lookback + PM-004 settled FLOOR_STRIKE/RESULT (Sep-12; PM-001 ends Sep-11)
**Join:** DATA_VERDICT_PM004_L3002_JOIN **CONDITIONAL** + DATA_VERDICT_PM004_L3_SEP11_EDGE **CLEARED** · lock B (bar_end < decision_time) · named 855/855 · L3 ≠ oracle · no PM-003 · no CF
**Slice use:** USED_RESEARCH — not validation, not sealed holdout
**Overall verdict:** `REDUNDANT / FAIL-INSUFFICIENT`
**invented_numbers:** `False`
**Trading:** FORBIDDEN
**Stamp:** Sep-12 PM-004; lock B; L3 ≠ oracle; no PM-003; θ/W frozen no search; Governor SIGN F4.
**Annex:** N_wick + wick-subset Δ + λ grid report-only (not a leaderboard)
**Run UTC:** `2026-09-14T01:04:16Z`
**SHA256 recorded:** `True`

## Authority
- `governance/EXAMINER_ORDER_TEST-20260914-001-F4.md`
- `governance/GOVERNOR_SIGN_F4_WICK_2026-09-14.md`
- `archive/features/DRAFT-FEAT-20260914-008-F4-wick.md`
- `archive/features/DRAFT-ABST-20260914-008-F4-wick.md`
- `archive/features/DRAFT-FEAT-20260912-006.md`
- `data/DATA-PROV-PM-004/provenance/DATA_VERDICT_PM004_L3002_JOIN.md`
- `data/DATA-PROV-PM-004/provenance/DATA_VERDICT_PM004_L3_SEP11_EDGE.md`
- `governance/BINARY_EXAMINER_SPEC.md`

## Frozen map
- ε=0.0001; θ=1.5; W=5; λ=0.35; Wσ=60
- Lock B only: bar usable iff bar_end_ms < decision_time_ms
- m = PM-004 same-row mid (Sep-12 only; method=mid)
- S_t = close of last L3 bar with bar_end < t
- S_tW = close W completed steps back in same lock-B chain
- σhat = RMS(log returns of prior Wσ completed lock-B bars) * sqrt(365.25*24*60)
- τ = time_remaining_sec / (365.25*24*3600); K = FLOOR_STRIKE
- z = ln(S_t/K) / (σhat * sqrt(τ)); p_s = Φ(z)
- wick = abs(ln(S_t/S_tW)) > θ * σhat * sqrt(W/(365.25*24*60))
- if ABSTAIN or m missing or not lookback_ok: p = m
- elif not wick: p = m   # Feature silence; Δ=0 by construction
- else: p = clip((1-λ)*m + λ*p_s, ε, 1-ε) with λ=0.35
- Robustness annex λ∈[0.2, 0.35, 0.5] report-only — NO θ/W grid. λ=0 ⇒ Δ=0.

## Filters / join
- venue=KALSHI, window=15m; BTC/ETH **separate** (no pool)
- Sep-12 PM-004 mid only — **no** PM-003 · **no** Sep-13 · **no** PM-002 union
- Headlines only: T-5m (rem=300); **no** T-14m · **no** T-10m speak
- `implied_p_method == mid` only; last-fallback excluded
- exclude `implied_p ≤ 0.02` or `≥ 0.98` (near-deg)
- VOID/DISPUTED out of scored N
- L3 = L3-002 Sep-12 + L3-001 Sep-11 bars for lookback/edges under lock B; L3 ≠ CF settlement oracle
- Missing W=5 chain or incomplete Wσ → ABSTAIN (p:=m), not "no wick"
- **NOT** policy A. **NOT** PM-003. **NOT** F1-always-speak. **NOT** W2-B.

**Sign convention:** ΔBrier = Brier_model − Brier_market; ΔLogLoss = LogLoss_model − LogLoss_market; **negative = skill** vs mid.

**Skill rule:** both Δ < 0 on full cell. Kill if either Δ ≥ 0, N_wick < 80, or one headline works and the other inverts. Not NO_EDGE. Not Champion. N_wick / wick-subset Δ = annex only.

## Overall reason
Neither headline improves both Brier and LogLoss vs mid on full cell (BTC=REDUNDANT / FAIL-INSUFFICIENT; ETH=REDUNDANT / FAIL-INSUFFICIENT). REDUNDANT / FAIL-INSUFFICIENT (not NO_EDGE; not Champion). USED_RESEARCH; holdout closed; no trading. Sep-12 PM-004; lock B; L3 ≠ oracle; no PM-003; θ/W frozen no search; Governor SIGN F4.

## Headlines (AMD-005, no pool, no annex speak)

| Cell | N | N_wick | speak | Brier_model | Brier_market | ΔBrier | LogLoss_model | LogLoss_market | ΔLogLoss | mean(m) | mean(p) | ECE | Verdict |
|------|--:|-------:|------:|------------:|-------------:|-------:|--------------:|---------------:|---------:|--------:|--------:|-----|---------|
| `KALSHI|15m|BTC|T-5m|mid` | 96 | 12 | 12 | 0.163359 | 0.163466 | -0.000107 | 0.503169 | 0.499520 | 0.003648 | 0.5378 | 0.5382 | UNTESTED | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 95 | 10 | 10 | 0.137928 | 0.138166 | -0.000238 | 0.450463 | 0.452229 | -0.001766 | 0.4949 | 0.4953 | UNTESTED | `REDUNDANT / FAIL-INSUFFICIENT` |

### `KALSHI|15m|BTC|T-5m|mid`
- N=96; N_wick=12; n_speak=12; n_allow=96; n_off_wick=84; n_abstain=0; speak_rate=0.1250
- mean(m)_all=0.5378; mean(p)_all=0.5382; mean(m)_speak=0.5089; mean(p)_speak=0.5127
- mean(S_t)=77287.908750; mean(K)=77273.298125; mean(σhat)=0.116158; mean(p_s)_speak=0.519758
- Reason: N_wick=12 < 80; FAIL-INSUFFICIENT (not NO_EDGE; not Champion)
- Calibration: ECE UNTESTED: thin bins / underpowered (N=96, powered_bins=1; need ≥2 bins n≥20 and/or N≥100)
- ECE_market: UNTESTED
- Wick-subset annex (not leaderboard): N_wick=12; ΔBrier=-0.000858; ΔLogLoss=0.029188
- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no trading)

### `KALSHI|15m|ETH|T-5m|mid`
- N=95; N_wick=10; n_speak=10; n_allow=95; n_off_wick=85; n_abstain=0; speak_rate=0.1053
- mean(m)_all=0.4949; mean(p)_all=0.4953; mean(m)_speak=0.5047; mean(p)_speak=0.5085
- mean(S_t)=2525.006000; mean(K)=2524.698000; mean(σhat)=0.227131; mean(p_s)_speak=0.515593
- Reason: N_wick=10 < 80; FAIL-INSUFFICIENT (not NO_EDGE; not Champion)
- Calibration: ECE UNTESTED: thin bins / underpowered (N=95, powered_bins=1; need ≥2 bins n≥20 and/or N≥100)
- ECE_market: UNTESTED
- Wick-subset annex (not leaderboard): N_wick=10; ΔBrier=-0.002257; ΔLogLoss=-0.016774
- EV_gross / EV_net / cost_sensitivity: **UNTESTED** (no trading)

## Robustness annex (λ grid; not headline; do not pick winner)

| Cell | λ | N | N_wick | ΔBrier | ΔLogLoss | Verdict |
|------|--:|--:|-------:|-------:|---------:|---------|
| `KALSHI|15m|BTC|T-5m|mid` | 0.2 | 96 | 12 | -0.000129 | 0.001591 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-5m|mid` | 0.35 | 96 | 12 | -0.000107 | 0.003648 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-5m|mid` | 0.5 | 96 | 12 | 0.000016 | 0.006807 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.2 | 95 | 10 | -0.000143 | -0.001031 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.35 | 95 | 10 | -0.000238 | -0.001766 | `REDUNDANT / FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 0.5 | 95 | 10 | -0.000321 | -0.002469 | `REDUNDANT / FAIL-INSUFFICIENT` |

## Placebos (report, not headline switch)

| Placebo | Cell | N | N_wick_effective | ΔBrier | ΔLogLoss | Notes |
|---------|------|--:|-----------------:|-------:|---------:|-------|
| `lambda_0` | `KALSHI|15m|BTC|T-5m|mid` | 96 | 12 | 0.000000 | 0.000000 | λ=0 identity check pass=True |
| `lambda_0` | `KALSHI|15m|ETH|T-5m|mid` | 95 | 10 | 0.000000 | 0.000000 | λ=0 identity check pass=True |
| `shuffle_wick` | `KALSHI|15m|BTC|T-5m|mid` | 96 | 12 | 0.002127 | 0.004351 | wick labels shuffled within ALLOW rows; m fixed |
| `shuffle_wick` | `KALSHI|15m|ETH|T-5m|mid` | 95 | 10 | 0.000872 | 0.002152 | wick labels shuffled within ALLOW rows; m fixed |
| `reverse_gate` | `KALSHI|15m|BTC|T-5m|mid` | 96 | 12 | 0.007945 | 0.025003 | blend only when NO wick (reverse gate) |
| `reverse_gate` | `KALSHI|15m|ETH|T-5m|mid` | 95 | 10 | 0.001498 | 0.005326 | blend only when NO wick (reverse gate) |
| `sign_flip_ps` | `KALSHI|15m|BTC|T-5m|mid` | 96 | 12 | 0.006678 | 0.012953 | p_s → 1−p_s on wick rows |
| `sign_flip_ps` | `KALSHI|15m|ETH|T-5m|mid` | 95 | 10 | -0.001424 | -0.004381 | p_s → 1−p_s on wick rows |

- placebo_seed: `20260914`
- λ=0 must give ΔBrier=0 and ΔLogLoss=0 (identity vs mid).

## Filter / join stats
See full JSON in local harness out; N scored=191; n_speak=22; n_off_wick=169; policy B; join CONDITIONAL+EDGE_CLEARED; coverage 855/855; pm003_used false; theta_w_search false; policy_A_used false.

## Integrity
- checkpoints.ndjson sha256: `03b48e17cc1f018701a84dc2dfcf42427d4cd1de117dfdb9e19e8e4fe63cddf1`
- L3-002 BTC csv sha256: `b982e79e27a8ca5fdb2b2122788e210db10414e44287e7604be0d159388950f8`
- L3-002 ETH csv sha256: `47db79a2f741929cef6a23838cb5dad24ffb606899023afcf10de8f7bdb57f62`
- sha256_recorded: `True`
- Join verdict: **CONDITIONAL** (L3-002) + **CLEARED** (L3-001 edges); policy **B**
- PM-003 / Policy A / CF / F1-always-speak / W2-B: **not used**

## Overall package verdict
**`REDUNDANT / FAIL-INSUFFICIENT`** — Neither headline improves both Brier and LogLoss vs mid on full cell. USED_RESEARCH; holdout closed; no trading. Sep-12 PM-004; lock B; L3 ≠ oracle; no PM-003; θ/W frozen; Governor SIGN F4.

## Artifacts
- `lab/harness/examiner/out/TEST-20260914-001-F4-WICK-INCREMENTAL.md`
- `lab/archive/tests/TEST-20260914-001-F4-WICK-INCREMENTAL.md`

## Blockers
- KALSHI|15m|BTC|T-5m|mid: N_wick=12 < 80; skill fail ΔLogLoss>0
- KALSHI|15m|ETH|T-5m|mid: N_wick=10 < 80
