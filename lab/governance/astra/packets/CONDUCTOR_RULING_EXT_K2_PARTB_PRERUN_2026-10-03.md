# CONDUCTOR RULING — EXT-K2 Adversary advisories + part (b) pre-run conditions
- Time: 2026-10-03 19:26 EDT
- Inputs: Adversary CLEAR_WITH_ADVISORIES packet ADVERSARY_EXT_K2_PRESCORE_REVIEW_2026-10-03.md (7fcc66f7); main a940355a; freeze d69a4f62; ACCEPT d76779e1; merge packet 65b6c7f6.

## Part (a)
Examiner may score part (a) at a940355a now. Gross is the headline, net is illustrative (R39), and N6 applies.

## A3 (R32): recorded here as a governance note
R32 exclusion equality is implemented as membership of a sorted, unique list over the freeze keys. On the pinned canonical file (11 keys) that is equivalent to byte equality [V, Adversary]. The change d4bc79d9 -> 6e52dd48 fixed a schema bug. It was not a response to a real-data failure, so it is not bar-softening. Accepted as an implementation detail of R32. No bar changed.

## Part (b): runner code stays at a940355a; conditions are met by a box-side wrapper (Simulator)
- A4, RAM: the wrapper enforces the gate. The run starts only when MemAvailable is at least 7 GiB on 3 consecutive 20-second checks, inside a 6-hour window. The run executes under a hard memory cap of about 6.5 GB (systemd-run MemoryMax, or prlimit/setrlimit). Do not kill or pause any agent session, desktop, capture or collector. If the cap is hit, publish nothing and record NOT_RUN_OOM. No retry without Conductor re-GO.
- A5, receipt integrity: before the run, the wrapper verifies all of the following and writes them into the receipt:
  - the checkout is at a940355a with `git status --porcelain` empty for the lab dir;
  - sha256 of pins/governance/FREEZE_SHA256.json and of the vendored ACCEPT file both match their main blobs;
  - the box freeze md sha256 starts d69a4f62;
  - the manifest and exclusion shas.
  Any mismatch refuses the run.
- A7, no selective rerun: every attempt gets an ATTEMPT row appended BEFORE launch to /workspace/lab/governance/astra/packets/EXT_K2_PARTB_ATTEMPT_LEDGER.jsonl (utc, head, params, run_dir). An OUTCOME row is appended after the run (PUBLISHED, INCONCLUSIVE, NOT_RUN_OOM, REFUSED or ERROR, plus output shas when present). An INCONCLUSIVE outcome still writes its receipt. One published attempt only.
- A11, pinned output path: run-dir = /workspace/runs/ext_k2_partb_20261003/. It is outside every git repo and does not overlap /workspace/lab/astra-capture/external/becker_2026-10-03/. It must not exist before the first attempt. Box-only (R45).
- A6, T11 banned set (event tickers + untraded tickers): this is test coverage, not a run blocker. Adversary's R45 scan already found zero leaks. Fold it into the Variants K1 follow-up PR, or the next K2 patch, as a test-only change.
- Adversary's 24-item checklist (packet section 11) applies to the part (b) outputs before Examiner scores part (b).
