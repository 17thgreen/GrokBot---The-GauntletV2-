Follow-up on 17thgreen/Grokbot-Deathmatch-Dedicated-Repo, Conductor GO 2026-10-02 19:14 ET: add one more doc file to the SAME draft PR. Do NOT merge. Do not open a new PR. No force-push, no rebase or amend of pushed commits, no commits to main, no branch deletes, and do not touch other PRs. Docs only: never edit results, cemetery entries, scoring logic, pinned routine prompts or recorder code, and never touch recorders.

1. git fetch origin && git checkout steward/doclag-admit1-closed-2026-10-02 && git pull --ff-only origin steward/doclag-admit1-closed-2026-10-02 (this is the existing PR branch: the draft PR opened from that branch by agent bc-83bd0164 (at 19:15 ET neither the branch nor the PR was visible yet)). If the branch or its open draft PR does not exist, STOP and report; do not create one. Confirm the working tree is clean.
2. Save the script below as /tmp/apply_edits_2.py (OUTSIDE the repo) and run: python3 /tmp/apply_edits_2.py fleet "$PWD". It touches only the round-2 file and its _prev copy. It checks old and expected new sha256 and aborts with nothing written on any mismatch. Any ABORT means STOP, push nothing, and report.
3. git add -A. git status --porcelain must list EXACTLY these paths and nothing else, with these sha256 (sha256sum). The _prev file's sha256 must equal the hash in its name:
M registry/PACKET_INDEX.md  -> new sha256 0b8aa0ca5bd927b47053e9ddfa3744af4ecfedff2e94888f8ced6ff91947331c
A registry/_prev/92320112b06f48f60d4a8aac5e793462e70eddf52acbd58ad007b56968c880e0.PACKET_INDEX.md  -> sha256 92320112b06f48f60d4a8aac5e793462e70eddf52acbd58ad007b56968c880e0
4. Leakage check: (a) git diff --cached --name-only | grep -Ei 'evidence_private|source_probe_electindex|electindex|\.sqlite' must be empty. (b) git diff --cached -U0 -- . ':(glob,exclude)**/_prev/**' ':(glob,exclude)_prev/**' | grep -E '^\+' | grep -v '^+++' | grep -Ei 'evidence_private|electindex|BEGIN .*PRIVATE KEY|api[_-]?key|secret|password' must be empty.
5. No tests apply (docs-only repo).
6. Make ONE additional commit with message "docs: ADMIT-1 CLOSED/DOWN in fleet PACKET_INDEX (steward doc-lag follow-up)" and a body giving old -> new sha256 and the _prev path. git push origin steward/doclag-admit1-closed-2026-10-02 (NO --force). Keep the PR a draft; do not change its title or mark it ready.
7. Report: the new head sha, the draft state, and the full PR file list (git diff --name-status origin/main...HEAD), which must be exactly:
registry/PACKET_INDEX.md
registry/STATUS.md
registry/_prev/7e22d2a95806e1797774cf0205a7b989fc671e4c3dd40ca2813d3a42efe0298a.STATUS.md
registry/_prev/92320112b06f48f60d4a8aac5e793462e70eddf52acbd58ad007b56968c880e0.PACKET_INDEX.md
   Also report the script's JSON output and the leakage/test results.

----- /tmp/apply_edits_2.py -----
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
----- end -----
