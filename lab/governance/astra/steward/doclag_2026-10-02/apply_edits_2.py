#!/usr/bin/env python3
"""Doc-lag follow-up edits, round 2 (steward, 2026-10-02; Conductor GO 19:14 ET).
Usage: apply_edits_2.py <primary|fleet> <repo_root>
Run on the existing PR branch after the round-1 commit. Touches ONLY the round-2 file per repo
(plus its _prev copy). Exact-string replacements; each anchor must occur exactly once. Checks old
AND expected new sha256 for every file before writing anything; any mismatch aborts with nothing
written. _prev copies follow RULE-FROZEN-EDIT-PREV-BYTES-001."""
import hashlib, sys, pathlib, json

R18 = "52a6b8a1378b120a241ce9c6b302ca214b0a04b7360773269293d845b8623d3d"
BURST = "9a2870dba116645900809026be14303b61cf53913920688197f27d94cbd43362"
R18_PATH = "lab/incidents/ADMIT1_TRUNCATION_BOX_REBUILD_2026-10-02_v2_CORRECTED.json"
BURST_PATH = "lab/astra-capture/prospective/ADMIT1_POST_RUN_NOTE_2026-10-02.md"

EDITS = {
 "primary": {
  # Lab README: pinned by the PR64 settled run's runner_tree provenance manifest (box) -> treated as frozen.
  "kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/README.md": {
   "expect_old_sha256": "9a8bc5c6727c8abd30d83e4bfc1b9e6553aae6c449331d11b37b1bcd5ec5b83c",
   "expect_new_sha256": "c9cd9b68ec32b72692a4ed959f40cbdfff42a57e54457f74ff86534a2c6e545a", "prev": True, "repl": [
   ("The Examiner file in this directory is `HOLD_PRE_PR`. This lab does not place orders and does not open a network client.\n",
    "The Examiner hold file in this directory is `SUPERSEDED` (PR64 merged `eb33f094`; Examiner SCORE `961f72fa` ITERATE, Conductor ACCEPT `57a9f5e6`). This lab does not place orders and does not open a network client.\n"),
  ]},
 },
 "fleet": {
  # Fleet registry file -> treated as frozen, same as registry/STATUS.md in round 1.
  "registry/PACKET_INDEX.md": {
   "expect_old_sha256": "92320112b06f48f60d4a8aac5e793462e70eddf52acbd58ad007b56968c880e0",
   "expect_new_sha256": "0b8aa0ca5bd927b47053e9ddfa3744af4ecfedff2e94888f8ced6ff91947331c", "prev": True, "repl": [
   ("| ADMIT-1 | **LIVE** — PIT@CLE `KXNFLGAME-26OCT01PITCLE`; admitted_at `2026-09-22T21:18:13Z`; 16 events. GET-only recorder alive on Conductor host. |",
    "| ADMIT-1 | **CLOSED/DOWN** per Conductor ruling. Run 18 closed truncated: record `%s` sha256 `%s`. Burst-profile spec: `%s` sha256 `%s`. Recorder **DOWN**: no recorder is running (was GET-only on Conductor host). Previously LIVE: PIT@CLE `KXNFLGAME-26OCT01PITCLE`; admitted_at `2026-09-22T21:18:13Z`; 16 events. |" % (R18_PATH, R18, BURST_PATH, BURST)),
  ]},
 },
}

def sha(b): return hashlib.sha256(b).hexdigest()

def main():
    which, root = sys.argv[1], pathlib.Path(sys.argv[2])
    plan = []
    for rel, spec in EDITS[which].items():
        p = root / rel
        old = p.read_bytes()
        if sha(old) != spec["expect_old_sha256"]:
            sys.exit("ABORT: %s old sha256 %s != expected %s (nothing written)" % (rel, sha(old), spec["expect_old_sha256"]))
        text = old.decode("utf-8")
        for a, b in spec["repl"]:
            n = text.count(a)
            if n != 1:
                sys.exit("ABORT: %s: anchor found %d times (nothing written): %r" % (rel, n, a[:80]))
            text = text.replace(a, b)
        new = text.encode("utf-8")
        if sha(new) != spec["expect_new_sha256"]:
            sys.exit("ABORT: %s new sha256 %s != expected %s (nothing written)" % (rel, sha(new), spec["expect_new_sha256"]))
        prev = (p.parent / "_prev" / ("%s.%s" % (sha(old), p.name))) if spec["prev"] else None
        if prev is not None and prev.exists() and prev.read_bytes() != old:
            sys.exit("ABORT: %s exists with different bytes (nothing written)" % prev)
        plan.append((rel, p, old, new, prev))
    out = []
    for rel, p, old, new, prev in plan:
        if prev is not None:
            prev.parent.mkdir(parents=True, exist_ok=True)
            prev.write_bytes(old)
        p.write_bytes(new)
        out.append({"path": rel, "old_sha256": sha(old), "new_sha256": sha(new),
                    "prev_copy": str(prev.relative_to(root)) if prev is not None else None})
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
