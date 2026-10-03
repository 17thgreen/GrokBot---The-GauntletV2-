You are working in a real checkout of 17thgreen/GPT-6-Astra-Deathmatch. Task: a DOCS-ONLY DRAFT PR fixing doc lag (Conductor ruling 2026-10-02 18:53 ET, which explicitly includes the PR64 housekeeping). Do NOT merge. No force-push, no commits to main, no branch deletes, do not close or touch other PRs. Never edit results, cemetery entries, scoring logic, pinned routine prompts or recorder code. Never touch recorders.

1. git fetch origin && git checkout -B steward/doclag-admit1-closed-pr64-merged-2026-10-02 origin/main. Record HEAD. Expected base eb33f094f3341958746f83a8f2f8c1e2c37a7d0a. If main has moved, continue only if the script's sha guards pass. If they fail, STOP, do not push, and report.
2. Save the Python script below as /tmp/apply_edits.py (OUTSIDE the repo) and run: python3 /tmp/apply_edits.py primary "$PWD". It does exact-string replacements and checks each file's old AND expected new sha256 before writing. It writes the RULE-FROZEN-EDIT-PREV-BYTES-001 _prev copies for frozen files only and prints the old/new sha256 JSON. Any ABORT means STOP, push nothing, and report. Keep the JSON for the report.
3. git add -A. Verify that git status --porcelain lists EXACTLY these paths and nothing else, and that sha256sum of each matches:
M README.md  -> new sha256 a4e97325cc42d856b91cdaa618c6ea45f99668e94d7af5c55394e498cd519cc5 (not frozen; no _prev)
M docs/EXPERIMENT_REGISTRY.md  -> new sha256 d1d01784ddb50629a6842f0f9055e22f087c48c28eb43ba537e135f5f47660a6
M kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/EXAMINER_HOLD_Q6S5_PR60_SCORABILITY_PRE_PR_2026-10-02.json  -> new sha256 cf9ce7ca7c8bc677f70388e63cde75c49aa9a5afcdd70cc459fef451214e4880 (must still parse as JSON: python3 -m json.tool <file> >/dev/null)
A docs/_prev/8ee066c3f13fe4677b9a4f7b753a57ada43d8aa81229f2ec3c83af16c1a1e30f.EXPERIMENT_REGISTRY.md  -> sha256 8ee066c3f13fe4677b9a4f7b753a57ada43d8aa81229f2ec3c83af16c1a1e30f
A kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/_prev/ffab465a62587587b8630a994414cb1d7cd74741d56c935a81e803c2037ef6a2.EXAMINER_HOLD_Q6S5_PR60_SCORABILITY_PRE_PR_2026-10-02.json  -> sha256 ffab465a62587587b8630a994414cb1d7cd74741d56c935a81e803c2037ef6a2
   Each _prev file's sha256 must equal the hash in its name (byte-identical to the file on main). Also run the PR64 lab tests and require OK: (cd kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002 && python3 -m unittest discover -s tests). Expected: Ran 41 tests, OK.
4. Leakage check over the staged diff: (a) git diff --cached --name-only | grep -Ei 'evidence_private|source_probe_electindex|electindex|\.sqlite' must be empty. (b) Over the NON-_prev files: git diff --cached -U0 -- . ':(exclude)**/_prev/**' ':(exclude)_prev/**' | grep -E '^\+' | grep -v '^+++' | grep -Ei 'evidence_private|electindex|BEGIN .*PRIVATE KEY|api[_-]?key|secret|password' must be empty. No raw ElectIndex bytes and nothing under lab/evidence_private/ or source_probe_electindex/ may be committed.
5. Commit with message "docs: ADMIT-1 CLOSED/DOWN + PR64 registry MERGED (steward doc-lag)" and a body listing each file's old -> new sha256. Push the branch: git push -u origin steward/doclag-admit1-closed-pr64-merged-2026-10-02 (NO --force).
6. Open a DRAFT PR to main titled "docs: ADMIT-1 CLOSED/DOWN + PR64 registry MERGED (steward doc-lag)". Body: docs/registry-only; Conductor ruling 2026-10-02 18:53 ET; Conductor merges; the sha JSON; leakage check result.
7. Report: PR URL, PR number, head sha, draft=true, git diff --stat origin/main...HEAD, the sha JSON, test result if any, and the leakage check output.

----- /tmp/apply_edits.py -----
#!/usr/bin/env python3
"""Doc-lag edits (steward, 2026-10-02). Usage: apply_edits.py <primary|fleet> <repo_root>
Exact-string replacements only; each old string must occur exactly once. Checks old AND new sha256
before writing anything for a file, writes _prev copies (RULE-FROZEN-EDIT-PREV-BYTES-001) for
frozen files only (README.md is not frozen: no _prev), and prints old/new sha256."""
import hashlib, sys, pathlib, json

R18 = "52a6b8a1378b120a241ce9c6b302ca214b0a04b7360773269293d845b8623d3d"
BURST = "9a2870dba116645900809026be14303b61cf53913920688197f27d94cbd43362"
R18_PATH = "lab/incidents/ADMIT1_TRUNCATION_BOX_REBUILD_2026-10-02_v2_CORRECTED.json"
BURST_PATH = "lab/astra-capture/prospective/ADMIT1_POST_RUN_NOTE_2026-10-02.md"
MAIN = "eb33f094f3341958746f83a8f2f8c1e2c37a7d0a"
HOLD = "kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/EXAMINER_HOLD_Q6S5_PR60_SCORABILITY_PRE_PR_2026-10-02.json"

EDITS = {
 "primary": {
  "README.md": {"expect_old_sha256": "8a40c2123f4306908c9afae623592390cdc9ac5b3efddcd01b08470fc6efd18a", "expect_new_sha256": "a4e97325cc42d856b91cdaa618c6ea45f99668e94d7af5c55394e498cd519cc5", "prev": False, "repl": [
   ("| `nfl_prospective_recorder_20260922` | GET-only prospective recorder (ADMIT-1); deployed and running since 2026-09-22. Fleet evidence: `17thgreen/Grokbot-Deathmatch-Dedicated-Repo` commit `1825ec8c` |",
    "| `nfl_prospective_recorder_20260922` | GET-only prospective recorder (ADMIT-1). Deployed 2026-09-22 (fleet evidence: `17thgreen/Grokbot-Deathmatch-Dedicated-Repo` commit `1825ec8c`). ADMIT-1 is now CLOSED/DOWN per Conductor ruling; no recorder is running. Run 18 closed truncated: record `%s` sha256 `%s`. Burst-profile spec: `%s` sha256 `%s` |" % (R18_PATH, R18, BURST_PATH, BURST)),
   ("recorder (ADMIT-1) in `nfl_prospective_recorder_20260922/` has been deployed\nand running since 2026-09-22. Fleet evidence is\n`17thgreen/Grokbot-Deathmatch-Dedicated-Repo` commit `1825ec8c`. PHI@CHI's",
    "recorder (ADMIT-1) in `nfl_prospective_recorder_20260922/` was deployed on\n2026-09-22. Fleet evidence is\n`17thgreen/Grokbot-Deathmatch-Dedicated-Repo` commit `1825ec8c`. ADMIT-1 is now\nCLOSED/DOWN per Conductor ruling and no recorder is running. Run 18 closed\ntruncated: record\n`%s`\nsha256 `%s`.\nBurst-profile spec: `%s`\nsha256 `%s`. PHI@CHI's" % (R18_PATH, R18, BURST_PATH, BURST)),
  ]},
  "docs/EXPERIMENT_REGISTRY.md": {"expect_old_sha256": "8ee066c3f13fe4677b9a4f7b753a57ada43d8aa81229f2ec3c83af16c1a1e30f", "expect_new_sha256": "d1d01784ddb50629a6842f0f9055e22f087c48c28eb43ba537e135f5f47660a6", "prev": True, "repl": [
   ("`results`, `pnl`, and `roi` stay null. Examiner status `HOLD_PRE_PR`. Structural counts only: books 15,",
    "`results`, `pnl`, and `roi` stay null. Examiner status `SCORED ITERATE` (score `961f72fa`, Conductor ACCEPT `57a9f5e6`; ITERATE = carry the design to fresh data only, not edge evidence; PR64 merged to main as `%s` on 2026-10-02 00:29:59 ET; previously `HOLD_PRE_PR`). Structural counts only: books 15," % MAIN),
  ]},
  HOLD: {"expect_old_sha256": "ffab465a62587587b8630a994414cb1d7cd74741d56c935a81e803c2037ef6a2", "expect_new_sha256": "cf9ce7ca7c8bc677f70388e63cde75c49aa9a5afcdd70cc459fef451214e4880", "prev": True, "repl": [
   ('  "status": "HOLD_PRE_PR",\n', '  "status": "SUPERSEDED (PR64 merged eb33f094; Examiner SCORE 961f72fa ITERATE)",\n'),
  ]},
 },
 "fleet": {
  "registry/STATUS.md": {"expect_old_sha256": "7e22d2a95806e1797774cf0205a7b989fc671e4c3dd40ca2813d3a42efe0298a", "expect_new_sha256": "efc3a8c3a3e3e6aa434507f4b545dabba0318796c7c55807568ff05dd1a27017", "prev": True, "repl": [
   ("| ADMIT-1 | **LIVE** — PIT@CLE `KXNFLGAME-26OCT01PITCLE`; admitted_at `2026-09-22T21:18:13Z`; 16 events |",
    "| ADMIT-1 | **CLOSED/DOWN** per Conductor ruling. Run 18 closed truncated: record `%s` sha256 `%s`. Burst-profile spec: `%s` sha256 `%s`. Previously LIVE: PIT@CLE `KXNFLGAME-26OCT01PITCLE`; admitted_at `2026-09-22T21:18:13Z`; 16 events |" % (R18_PATH, R18, BURST_PATH, BURST)),
   ("| Recorder | **GET-only**, alive on Conductor host |",
    "| Recorder | **DOWN**: no recorder is running (was GET-only on Conductor host) |"),
   ("Last updated: ADMIT-1 live (`2026-09-22T21:18:13Z`). No invented backtest numbers. No scoring.",
    "Last updated: 2026-10-02, ADMIT-1 CLOSED/DOWN per Conductor ruling (run 18 record sha256 `%s`). No invented backtest numbers. No scoring." % R18),
  ]},
 },
}

def sha(b): return hashlib.sha256(b).hexdigest()

def main():
    which, root = sys.argv[1], pathlib.Path(sys.argv[2])
    out = []
    for rel, spec in EDITS[which].items():
        p = root / rel
        old = p.read_bytes()
        if spec["expect_old_sha256"] and sha(old) != spec["expect_old_sha256"]:
            sys.exit("ABORT: %s old sha256 %s != expected %s (main moved?)" % (rel, sha(old), spec["expect_old_sha256"]))
        text = old.decode("utf-8")
        for a, b in spec["repl"]:
            n = text.count(a)
            if n != 1:
                sys.exit("ABORT: %s: anchor found %d times: %r" % (rel, n, a[:80]))
            text = text.replace(a, b)
        new = text.encode("utf-8")
        if sha(new) != spec["expect_new_sha256"]:
            sys.exit("ABORT: %s new sha256 %s != expected %s (nothing written)" % (rel, sha(new), spec["expect_new_sha256"]))
        prev_rel = None
        if spec["prev"]:
            prev = p.parent / "_prev" / ("%s.%s" % (sha(old), p.name))
            prev.parent.mkdir(parents=True, exist_ok=True)
            prev.write_bytes(old)
            prev_rel = str(prev.relative_to(root))
        p.write_bytes(new)
        out.append({"path": rel, "old_sha256": sha(old), "new_sha256": sha(new), "prev_copy": prev_rel})
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
----- end -----
