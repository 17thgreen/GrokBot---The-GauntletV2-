# ALMANAC Examiner — scorecard schema (locked)

As-of: 2026-09-15. Evidence rules: no fabricated rates; quote/bind = `[SF]` directional only; no Model 3 lead prices; no backfills; no "almost" retune of a killed creative without a new frozen variant.

## Cohort keys (required on every row)

| Field | Source | Notes |
|---|---|---|
| `radar_id` | Radar export | Immutable owner/property key |
| `token` | Drop | Shared across mail + email + QR |
| `list_id` | Radar / Drop | `live_sale_1` \| `live_sale_2` \| `live_sale_3` |
| `creative_id` | Quill freeze | Frozen variant id; kill/iterate by this |
| `mail_post_date` | Drop send log | Touch 1 |
| `email_send_date` | Drop send log | Touch 2; null if suppressed / no email |
| `purchase_date` | Radar | For Live Sale 1 clock |
| `days_to_anniversary` | Derived | At mail_post_date: anniversary ≈ purchase_date + 1y |

## Denominator (mailed / emailed)

| Metric | Definition |
|---|---|
| `n_mailed` | Rows with Touch 1 shipped for the score week’s cohorts |
| `n_emailed` | Rows with Touch 2 sent (responders already suppressed) |
| `n_exposed` | Primary denom for response rate = mailed (unless Conductor freezes otherwise) |

## Numerators (response)

A **response** is any inbound that maps to a token/list within the measurement window (default: from mail_post through score date), first-touch channel tagged when known.

| Channel | Counts as response | Source |
|---|---|---|
| DID | Call/text to dedicated DID | Switchboard inbound log |
| QR | Scan → tracked land / call path with token | Drop / Switchboard |
| Email | Reply / tracked click-to-CTA if Conductor freezes click-as-response | Drop / Switchboard |

Do **not** invent channel when unknown — tag `channel=unknown` and chase same day (Switchboard).

## Primary score lines

1. **Response rate by list** — responses / `n_exposed` for Live Sale 1, 2, 3 (and by `creative_id` when >1 frozen).
2. **Live Sale 1 clock falsifier** — response rate vs `days_to_anniversary` bins (e.g. ≤−120, −119…−91, −90…−61, −60…−45, >−45). Peak near −90 = clock supported; flat = creative/mail baseline, clock weak.
3. **Channel mix** — DID vs QR vs email vs unknown among responses.
4. **Time-to-answer** — Switchboard: inbound → tagged/handed to producer (SLA target &lt;5 min).
5. **[SF] quote / bind** — producer dispositions only; directional counts; never per-bind pricing claims.

## Mail-only vs mail+email

Split response attribution:
- Mail-only window: response before email_send_date (or never emailed).
- Mail+email: response on/after email_send_date for emailed rows.
- Email open/click/reply reported separately when tracked email exists.

## Bands (default — Conductor may retune)

| Band | Action |
|---|---|
| ≥1.5% | Keep list/trigger (+ creative) |
| 1–1.5% | One creative iteration only |
| &lt;1% | Kill that list/trigger before more spend |

Minimum N: do not green/kill on tiny samples — flag `insufficient_n` and recommend hold vs kill only when Conductor sets an N floor.

## Packet output

Weekly file under `almanac-fleet/scorecards/YYYY-MM-DD.md` plus a short go/no-go for Conductor: KEEP / ITERATE / KILL / NO_SCORE / HOLD per list×creative.
