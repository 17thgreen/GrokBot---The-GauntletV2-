# Amendment Rule — Institutional Governance Changes

**Locked with:** `INSTITUTIONAL_LOCK_2026-09-11.md`  
**Default:** Governance changes are **NOT retroactive**.

Material changes to doctrine, authority lattice, hard vetoes, promotion chain, evidence discipline, dataset/raw-data policy, routing gates, or Conductor limits require a filed amendment. Informal chat agreement does not amend the institution.

---

## Schema

| Field | Required | Description |
|-------|----------|-------------|
| `AMENDMENT_ID` | YES | Archivist- or Governor-assigned ID, e.g. `AMD-20260911-001` |
| `RULE_BEFORE` | YES | Exact prior rule text or precise pointer (file + section) |
| `RULE_AFTER` | YES | Replacement rule text (operable, not vibes) |
| `REASON` | YES | Why the change is necessary |
| `EVIDENCE` | YES | What institutional or market evidence motivates the change; tag `[V][I][H][A][U]` |
| `PROPOSED_BY` | YES | Role + name/agent |
| `AFFECTED_ROLES` | YES | List of roles whose authority or duties change |
| `RETROACTIVE` | YES | `YES` or `NO` — **default `NO`** |
| `APPROVER` | YES | Human Governor (Logan) unless explicitly delegated in writing |
| `DATE` | YES | UTC date of approval |
| `GAUNTLET_VERSION` | YES | Tag or baseline label this amendment applies after, e.g. `gauntlet-v2.0-alpha` |

---

## Process

1. Propose via blank template: `templates/AMENDMENT.md`.
2. Cite `RULE_BEFORE` precisely (do not paraphrase away the freeze).
3. Conductor may route discussion; Conductor may **not** approve alone.
4. Human Governor sets `APPROVER` + `DATE` and may set `RETROACTIVE` (default remains NO).
5. Archivist files the approved amendment under `governance/` (and indexes if required).
6. Update affected operable docs (`AUTHORITY.md`, `ROUTING.md`, etc.) to match `RULE_AFTER` — with a one-line pointer to the amendment ID.

---

## Retroactivity

- **`RETROACTIVE: NO` (default):** Past tests, kills, promotions, and seals stand under the rules then in force. New rule applies going forward only.
- **`RETROACTIVE: YES`:** Requires explicit Human Governor justification in `REASON` + `EVIDENCE`. Does not authorize rewriting raw data or fabricating replacement performance.

---

## Non-amendments (no AMD required)

- Typo / formatting fixes that do not change meaning
- New Edge Cards, tests, cemetery entries, dataset registrations under existing rules
- Cycle research orders that commission work without altering gates

If unsure whether a change is material → treat as material and file an amendment.
