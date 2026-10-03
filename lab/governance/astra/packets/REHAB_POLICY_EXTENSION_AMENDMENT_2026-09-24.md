# Rehab policy amendment — extension passes / warm shelf — 2026-09-24 (ET)

**Source:** Logan's rule as relayed by The Conductor "KALSHI" to Refiner, 2026-09-24 ~19:31 ET (visible to Logan in the Refiner chat). Amends `REHAB_POLICY_3PASS_2026-09-23.md`; does not replace it.

At end of pass 3 the Refiner decides, without asking, against the SAME frozen bar and stress set:
- Up to 2 extension passes (5 total), or park on a **warm shelf** for new data (prospective/live), only if all hold:
  (a) gap to pass bar closed >=50% between pass 1 and pass 3;
  (b) gain holds across most stresses, not driven by one game/event;
  (c) no bar softened, no holdout touched;
  (d) every variant tried is logged.
- Each extension pass: one pre-declared orthogonal knob. A pass closing <10% of remaining gap => cemetery or warm shelf.
- More than 5 passes needs Conductor + Adversary. Adversary runs an overfit check each extension; no kill vote.
- Promotion still requires untouched prospective data; improvement is never a pass by itself.
- File decisions as `REFINER_EXTEND` / `REFINER_SHELVE` / `REFINER_CEMETERY` with pass-by-pass numbers.

**Refiner operationalization (frozen before any P2 outcome seen):** `REFINER_EXTENSION_GAP_METRIC_FREEZE_Q7_ARM_B_2026-09-24.json`. Baseline is the better of the original corpse (B0) and pass 1, so a pass that merely undoes a pass-1 regression does not count as closing the gap.

stamped_at_et: 2026-09-24T19:31:51-04:00
