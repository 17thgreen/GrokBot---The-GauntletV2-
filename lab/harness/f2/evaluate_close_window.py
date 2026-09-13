"""FEAT-20260912-005 frozen Map-2 remainder. Synthetic fixtures only. No Examiner until CF ticks."""
import math

FROZEN = "FEAT-20260912-005/evaluate_close_window/2026-09-12-patch2"


def evaluate_close_window(
    ticks: list[dict],
    floor_strike: float,
    close_start_ms: int,
    now_ms: int,
    m_t: float,
    pre_close_last: float = None,
) -> dict:
    if close_start_ms % 1000 != 0:
        return {"status": "BAD_WINDOW"}

    s_start = close_start_ms // 1000

    locked_slots = []
    for i in range(60):
        s = s_start + i
        if (s + 1) * 1000 <= now_ms:
            locked_slots.append((i, s))
        else:
            break

    k = len(locked_slots)

    slot_candidates = {}
    for t in ticks:
        ts = t.get("timestamp_ms")
        price = t.get("price")
        s = ts // 1000
        if s_start <= s < s_start + 60:
            i = s - s_start
            slot_candidates.setdefault(i, []).append((ts, price))

    slot_prints = {}
    for i, candidates in slot_candidates.items():
        winning_print = max(candidates, key=lambda x: x[0])
        slot_prints[i] = winning_print[1]

    for i, s in locked_slots:
        if i not in slot_prints:
            return {"status": "MISSING", "k": k}

    locked_prices = [slot_prints[i] for i, s in locked_slots]

    if k > 0:
        locked_sum = math.fsum(locked_prices)
        locked_mean = locked_sum / k
        last = locked_prices[-1]
    else:
        locked_sum = 0.0
        locked_mean = 0.0
        last = None

    lock_yes = (locked_sum >= floor_strike * 60.0) if k == 60 else False
    lock_no = k == 60 and locked_sum < floor_strike * 60.0

    if lock_yes:
        p_map1 = 1.0
    elif lock_no:
        p_map1 = 0.0
    else:
        p_map1 = m_t

    if k == 0:
        if pre_close_last is not None:
            last = pre_close_last
            projected_sum = 60.0 * last
        else:
            return {"status": "MISSING", "k": 0}
    else:
        projected_sum = locked_sum + (60 - k) * last

    p_remainder = 1.0 if projected_sum >= floor_strike * 60.0 else 0.0
    delta_vs_mid = p_remainder - m_t

    return {
        "status": "OK",
        "k": k,
        "locked_mean": round(locked_mean, 4),
        "required_remaining_avg": (
            round((floor_strike * 60.0 - locked_sum) / (60.0 - k), 4) if k < 60 else None
        ),
        "lock_yes": lock_yes,
        "lock_no": lock_no,
        "p_map1": round(p_map1, 4),
        "p_remainder": round(p_remainder, 4),
        "delta_vs_mid": round(delta_vs_mid, 4),
    }
