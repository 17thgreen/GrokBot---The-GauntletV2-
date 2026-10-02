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


if __name__ == "__main__":
    close_start = 1776548400000
    K = 64150.0

    ticks_f1 = [
        {"timestamp_ms": close_start + (i * 1000) + 100, "price": 64200.0} for i in range(30)
    ]
    res1 = evaluate_close_window(ticks_f1, K, close_start, now_ms=close_start + 30000, m_t=0.5)
    assert res1["k"] == 30 and res1["p_remainder"] == 1.0 and res1["lock_yes"] is False

    res2 = evaluate_close_window(ticks_f1, K, close_start, now_ms=close_start + 10000, m_t=0.5)
    assert res2["k"] == 10

    ticks_f3 = [
        {"timestamp_ms": close_start + (i * 1000) + 100, "price": 64200.0}
        for i in range(11)
        if i != 7
    ]
    assert evaluate_close_window(ticks_f3, K, close_start, now_ms=close_start + 11000, m_t=0.5)[
        "status"
    ] == "MISSING"

    ticks_f4 = [
        {"timestamp_ms": close_start + (i * 1000) + 100, "price": 64149.99} for i in range(60)
    ]
    res4 = evaluate_close_window(ticks_f4, K, close_start, now_ms=close_start + 60000, m_t=0.5)
    assert res4["k"] == 60 and res4["lock_no"] is True and res4["p_remainder"] == 0.0

    ticks_f5_sorted = [
        {"timestamp_ms": close_start + (i * 1000), "price": 64200.0} for i in range(5)
    ]
    ticks_f5_shuffled = [
        ticks_f5_sorted[3],
        ticks_f5_sorted[0],
        ticks_f5_sorted[4],
        ticks_f5_sorted[1],
        ticks_f5_sorted[2],
    ]
    assert evaluate_close_window(
        ticks_f5_sorted, K, close_start, now_ms=close_start + 5000, m_t=0.5
    ) == evaluate_close_window(
        ticks_f5_shuffled, K, close_start, now_ms=close_start + 5000, m_t=0.5
    )

    ticks_f6 = [
        {"timestamp_ms": close_start + 200, "price": 60000.0},
        {"timestamp_ms": close_start + 800, "price": 64200.0},
    ]
    res6 = evaluate_close_window(
        ticks_f6, K, close_start, now_ms=close_start + 1000, m_t=0.5, pre_close_last=64200.0
    )
    assert res6["k"] == 1 and res6["locked_mean"] == 64200.0

    ticks_f7 = [
        {"timestamp_ms": close_start + 800, "price": 64200.0},
        {"timestamp_ms": close_start + 200, "price": 60000.0},
    ]
    res7 = evaluate_close_window(ticks_f7, K, close_start, now_ms=close_start + 1000, m_t=0.5)
    assert res7["k"] == 1 and res7["locked_mean"] == 64200.0

    assert (
        evaluate_close_window([], K, close_start + 123, now_ms=close_start + 1000, m_t=0.5)[
            "status"
        ]
        == "BAD_WINDOW"
    )

    print("FROZEN FIXTURES PASSED", FROZEN)
