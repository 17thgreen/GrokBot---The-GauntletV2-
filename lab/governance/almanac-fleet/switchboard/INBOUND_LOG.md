# ALMANAC inbound log

SLA: tag every inbound in under 5 minutes. Chase unknown tokens same day.
Feed weekly raw counts to Examiner / measurement.

| time_utc | caller | channel | token | list | disposition | producer_notes | tagged_by |
|---|---|---|---|---|---|---|---|
|  |  | DID / QR / email |  | Live Sale 1/2/3 or unknown | pending |  | Switchboard |

## Disposition codes (producer reports same day)
- `answered` — producer took the call
- `missed_sms_sent` — missed; Conductor-approved SMS sent
- `callback` — producer will call back
- `quoted` — quote started [SF]
- `bound` — bound [SF]
- `declined` — no interest
- `wrong_number` / `spam`
- `unknown_token` — chasing

## Weekly rollup (raw counts for measurement)
| week_ending | did | qr | email | unknown | total |
|---|---|---|---|---|---|
