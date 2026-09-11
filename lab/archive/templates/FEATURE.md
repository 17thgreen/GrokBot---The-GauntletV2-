# FEAT-YYYYMMDD-NNN

Feature Card — companion to Atomic Edge Cards for forecast inputs.
Blank schema per `governance/PREDICTION_MARKET_MISSION_2026-09-11.md`.
Does not replace Edge Cards; does not authorize Edge Card rewrites.

- **FEATURE_ID:** (Archivist-assigned)
- **NAME:**
- **STATUS:** HYPOTHESIS | RESEARCH | ACTIVE | INACTIVE | RETIRED | CEMETERY
- **PROVENANCE:** originator · date UTC · related FEAT/EDGE/CONTRACT/DATA/TEST/CEM IDs
- **CONFIDENCE:** tagged belief [H]/[I]/[A] — not a validity self-grade

## DEFINITION
Exact computable definition of the feature (formula / event rule). Not vibes.

## MECHANISM
Why this input could move \(P(\text{YES} \mid \mathcal{I}_t)\). Economic / informational — not “indicator crossed.”

## CONTRACT / UNIVERSE SCOPE
- CONTRACT_ID(s) or selection rule:
- VENUE_ADAPTER(s):

## DECISION-TIME / KNOWABILITY
- Available at timestamp t?
- Latency from event time → usable time:
- Look-ahead / revision hazards:
- Clock constraints:

## DATA LAYER
- L1 PM | L2 oracle | L3 external
- DATA-* refs:
- Fields / columns:

## TRANSFORM / NORMALIZATION
Missingness, winsorization, venue quirks — explicit. No silent cleaning of raw.

## EXPECTED SIGN / USE IN FORECAST
How the feature enters \(p_t\) (direction, model family). Ensemble role if any.

## FAILURE REGIME
Where the feature is expected to be useless, inverted, or unavailable.

## FALSIFICATION
Concrete measurement that rejects the feature’s claimed value (e.g. no Δ log-loss vs market / ablation).

## LEAKAGE & REDUNDANCY CONTROLS
- Ablation vs market \(m_t\) alone
- Ablation vs trivial contract metadata
- Cross-layer redundancy notes

## Evidence notes
Tag every material claim: [V] [I] [H] [A] [U]. Untested = UNTESTED.
