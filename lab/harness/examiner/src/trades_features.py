"""Stream aggTrades → per-5m decision-bar trade-flow features; cache parquet [A].

Fast path: W_trade=1m windows on a 5m grid are non-overlapping, so each trade
maps to at most one decision bar via searchsorted — vectorized per day.
Trailing L_size size-quantile maintained with a rolling deque across days.
"""

from __future__ import annotations

import json
from collections import deque
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Deque, Optional

import numpy as np
import pandas as pd

from .trades_loader import (
    HOLDOUT_START_MS,
    day_zip_path,
    iter_days,
    load_ohlcv_slices_no_holdout,
    read_day_aggtrades,
)

CACHE_DIR_DEFAULT = Path("/workspace/lab/harness/examiner/cache/trades_001")


def _date_from_ms(ms: int) -> date:
    return datetime.fromtimestamp(ms / 1000.0, tz=timezone.utc).date()


def build_bar_trade_features(
    *,
    symbol: str,
    trades_raw_root: Path,
    ohlcv_root: Path,
    cache_dir: Path = CACHE_DIR_DEFAULT,
    w_trade_ms: int = 60_000,
    l_size: int = 2000,
    k_sub: int = 3,
    p_size: float = 0.95,
    placebo_seed: int = 20260911,
    force_rebuild: bool = False,
    max_days: Optional[int] = None,
) -> Path:
    cache_dir.mkdir(parents=True, exist_ok=True)
    suffix = f"_max{max_days}" if max_days else ""
    out_path = cache_dir / f"{symbol}_bar_flow{suffix}.parquet"
    meta_path = cache_dir / f"{symbol}_bar_flow{suffix}.meta.json"
    # Full cache canonical name without suffix
    if max_days is None:
        out_path = cache_dir / f"{symbol}_bar_flow.parquet"
        meta_path = cache_dir / f"{symbol}_bar_flow.meta.json"
    if out_path.exists() and not force_rebuild:
        print(f"[cache {symbol}] reuse {out_path}", flush=True)
        return out_path

    ohlcv = load_ohlcv_slices_no_holdout(ohlcv_root, symbol)
    close_ms = ohlcv["close_time_ms"].to_numpy(dtype=np.int64)
    open_ms = ohlcv["open_time_ms"].to_numpy(dtype=np.int64)
    n_bars = len(ohlcv)

    n_buy = np.zeros(n_bars, dtype=np.int32)
    n_sell = np.zeros(n_bars, dtype=np.int32)
    n_buy_scr = np.zeros(n_bars, dtype=np.int32)
    n_sell_scr = np.zeros(n_bars, dtype=np.int32)
    total_notional = np.zeros(n_bars, dtype=np.float64)
    lrg_side = np.zeros(n_bars, dtype=np.float64)
    lrg_side_scr = np.zeros(n_bars, dtype=np.float64)
    lrg_abs_notional = np.zeros(n_bars, dtype=np.float64)
    clust = np.zeros(n_bars, dtype=np.float64)
    pers = np.zeros(n_bars, dtype=np.float64)
    max_print_share = np.zeros(n_bars, dtype=np.float64)
    s_star = np.full(n_bars, np.nan, dtype=np.float64)
    n_prints_w = np.zeros(n_bars, dtype=np.int32)
    lrg_side_size_shuf = np.zeros(n_bars, dtype=np.float64)
    clust_size_shuf = np.zeros(n_bars, dtype=np.float64)
    pers_size_shuf = np.zeros(n_bars, dtype=np.float64)
    filled = np.zeros(n_bars, dtype=bool)

    size_hist: Deque[float] = deque(maxlen=l_size)
    # Keep a numpy mirror for fast quantile
    size_arr = np.full(l_size, np.nan, dtype=np.float64)
    size_count = 0
    size_pos = 0

    rng = np.random.default_rng(placebo_seed)

    first_close = int(close_ms[0])
    last_close = int(close_ms[-1])
    start_day = _date_from_ms(max(0, first_close - 86_400_000))
    end_day = _date_from_ms(min(last_close, HOLDOUT_START_MS - 1))

    days_done = 0
    # Map close_ms for searchsorted
    # Trade ts maps to bar i if close[i]-W < ts <= close[i]
    # idx = searchsorted(close_ms, ts, side='left') → close[idx] is first close >= ts
    # accept if idx < n and (close[idx] - ts) < w_trade_ms  (strict: ts > close-W)
    # Since close - ts <= W-epsilon for ts > close-W: close-ts < W

    for day in iter_days(start_day, end_day):
        if max_days is not None and days_done >= max_days:
            break
        zpath = day_zip_path(trades_raw_root, symbol, day)
        days_done += 1
        if not zpath.exists():
            continue
        day_df = read_day_aggtrades(zpath, holdout_start_ms=HOLDOUT_START_MS)
        if day_df.empty:
            continue

        ts = day_df["transact_time"].to_numpy(dtype=np.int64)
        qty = day_df["quantity"].to_numpy(dtype=np.float64)
        px = day_df["price"].to_numpy(dtype=np.float64)
        side = day_df["side"].to_numpy(dtype=np.int8)
        scr = np.where(rng.random(len(ts)) < 0.5, np.int8(1), np.int8(-1))
        notional = px * qty

        # Assign each trade to a decision bar (non-overlapping W windows)
        idx = np.searchsorted(close_ms, ts, side="left")
        ok = idx < n_bars
        # also require ts <= close and close-ts < W and open of that bar < holdout
        ok &= ts <= close_ms[np.clip(idx, 0, n_bars - 1)]
        dist = close_ms[np.clip(idx, 0, n_bars - 1)] - ts
        ok &= dist < w_trade_ms
        ok &= close_ms[np.clip(idx, 0, n_bars - 1)] < HOLDOUT_START_MS
        # idx may be n_bars when ts > last close — already ok=False

        # Walk chronologically to update size_hist and compute per-bar features
        # Group trades by bar idx for bars that receive trades today
        valid_i = np.nonzero(ok)[0]
        if valid_i.size == 0:
            # Still advance size hist for all trades (for S* continuity)
            for q in qty:
                size_arr[size_pos] = q
                size_pos = (size_pos + 1) % l_size
                size_count = min(size_count + 1, l_size)
            continue

        # Process in time order: for each trade, update size hist; when bar
        # changes / completes, finalize previous bar's S* at its close.
        # Simpler: first update size hist through all trades of day while
        # recording S* at each bar's close moment.

        # Determine unique bars touched, in order
        bar_ids = idx[ok]
        # For S*: need size hist state at each bar close. Walk all day's trades
        # in order; when we pass a close_time, snapshot S* for that bar.

        # Precompute which closes fall within this day's trade span
        day_t0 = int(ts[0])
        day_t1 = int(ts[-1])
        # Bars whose close is in [day_t0, day_t1] need S* snapshot during walk
        bar_lo = int(np.searchsorted(close_ms, day_t0, side="left"))
        bar_hi = int(np.searchsorted(close_ms, day_t1, side="right"))

        trade_ptr = 0
        n_tr = len(ts)
        for bi in range(bar_lo, min(bar_hi, n_bars)):
            t_close = int(close_ms[bi])
            if t_close >= HOLDOUT_START_MS:
                break
            # Ingest trades with ts <= t_close into size hist
            while trade_ptr < n_tr and ts[trade_ptr] <= t_close:
                size_arr[size_pos] = qty[trade_ptr]
                size_pos = (size_pos + 1) % l_size
                size_count = min(size_count + 1, l_size)
                trade_ptr += 1
            if size_count > 0:
                s_star[bi] = float(np.nanquantile(size_arr[:size_count] if size_count < l_size else size_arr, p_size))
            filled[bi] = True  # knowability reached for this close (even if 0 prints in W)

        # Consume remaining trades into size hist (after last bar close today)
        while trade_ptr < n_tr:
            size_arr[size_pos] = qty[trade_ptr]
            size_pos = (size_pos + 1) % l_size
            size_count = min(size_count + 1, l_size)
            trade_ptr += 1

        # Vectorized aggregates into bars
        bi_v = idx[ok]
        qty_v = qty[ok]
        not_v = notional[ok]
        side_v = side[ok]
        scr_v = scr[ok]
        ts_v = ts[ok]

        # Counts
        buy = side_v > 0
        sell = ~buy
        buy_s = scr_v > 0
        sell_s = ~buy_s
        np.add.at(n_buy, bi_v[buy], 1)
        np.add.at(n_sell, bi_v[sell], 1)
        np.add.at(n_buy_scr, bi_v[buy_s], 1)
        np.add.at(n_sell_scr, bi_v[sell_s], 1)
        np.add.at(total_notional, bi_v, not_v)
        np.add.at(n_prints_w, bi_v, 1)

        # max print share: per-bar max notional
        # use pandas groupby for max
        tmp = pd.DataFrame({"bi": bi_v, "notional": not_v, "qty": qty_v, "side": side_v, "scr": scr_v, "ts": ts_v})
        if len(tmp):
            gmax = tmp.groupby("bi")["notional"].max()
            for bi_i, mx in gmax.items():
                tot = total_notional[bi_i]
                max_print_share[bi_i] = float(mx / tot) if tot > 0 else 0.0

            # Large-print features need S* — for bars filled today
            for bi_i, g in tmp.groupby("bi"):
                s_val = s_star[bi_i]
                if not np.isfinite(s_val):
                    continue
                qa = g["qty"].to_numpy()
                na = g["notional"].to_numpy()
                sa = g["side"].to_numpy()
                sca = g["scr"].to_numpy()
                tsa = g["ts"].to_numpy()
                large = qa >= s_val
                tot = float(total_notional[bi_i])
                if large.any():
                    signed = na[large] * sa[large].astype(np.float64)
                    ls = float(signed.sum())
                    lrg_side[bi_i] = ls
                    lrg_abs_notional[bi_i] = float(np.abs(signed).sum())
                    clust[bi_i] = abs(ls) / max(tot, 1e-12)
                    t0 = int(close_ms[bi_i]) - w_trade_ms
                    pers[bi_i] = _persistence(tsa, na, sa, large, t0, int(close_ms[bi_i]), k_sub)
                    lrg_side_scr[bi_i] = float((na[large] * sca[large].astype(np.float64)).sum())
                # size shuffle placebo
                if len(qa) >= 2:
                    perm = rng.permutation(len(qa))
                    large_shuf = qa[perm] >= s_val
                    if large_shuf.any():
                        signed_ss = na[large_shuf] * sa[large_shuf].astype(np.float64)
                        ls2 = float(signed_ss.sum())
                        lrg_side_size_shuf[bi_i] = ls2
                        clust_size_shuf[bi_i] = abs(ls2) / max(tot, 1e-12)
                        t0 = int(close_ms[bi_i]) - w_trade_ms
                        pers_size_shuf[bi_i] = _persistence(
                            tsa, na, sa, large_shuf, t0, int(close_ms[bi_i]), k_sub
                        )

        if days_done % 50 == 0 or days_done == 1:
            print(
                f"[cache {symbol}] day={day} days={days_done} "
                f"filled={int(filled.sum())}/{n_bars}",
                flush=True,
            )

    out = pd.DataFrame(
        {
            "open_time_ms": open_ms,
            "close_time_ms": close_ms,
            "n_buy_1m": n_buy,
            "n_sell_1m": n_sell,
            "n_buy_1m_scrambled": n_buy_scr,
            "n_sell_1m_scrambled": n_sell_scr,
            "total_notional_1m": total_notional,
            "lrg_side": lrg_side,
            "lrg_side_scrambled": lrg_side_scr,
            "lrg_abs_notional": lrg_abs_notional,
            "clust": clust,
            "pers": pers,
            "max_print_share": max_print_share,
            "s_star": s_star,
            "n_prints_1m": n_prints_w,
            "lrg_side_size_shuf": lrg_side_size_shuf,
            "clust_size_shuf": clust_size_shuf,
            "pers_size_shuf": pers_size_shuf,
            "feature_filled": filled,
            "open": ohlcv["open"].to_numpy(dtype=np.float64),
            "high": ohlcv["high"].to_numpy(dtype=np.float64),
            "low": ohlcv["low"].to_numpy(dtype=np.float64),
            "close": ohlcv["close"].to_numpy(dtype=np.float64),
            "volume": ohlcv["volume"].to_numpy(dtype=np.float64),
        }
    )
    out = out.loc[out["open_time_ms"] < HOLDOUT_START_MS].reset_index(drop=True)
    out.to_parquet(out_path, index=False)
    meta = {
        "symbol": symbol,
        "n_bars": int(len(out)),
        "n_filled": int(out["feature_filled"].sum()) if "feature_filled" in out else None,
        "w_trade_ms": w_trade_ms,
        "l_size": l_size,
        "k_sub": k_sub,
        "p_size": p_size,
        "placebo_seed": placebo_seed,
        "holdout_start_ms": HOLDOUT_START_MS,
        "derived_tag": "[A]",
        "days_streamed": int(days_done),
        "max_days": max_days,
    }
    meta_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(f"[cache {symbol}] wrote {out_path} rows={len(out)} filled={meta['n_filled']}", flush=True)
    return out_path


def _persistence(
    ts: np.ndarray,
    notional: np.ndarray,
    side: np.ndarray,
    large_mask: np.ndarray,
    t0: int,
    t: int,
    k: int,
) -> float:
    if k < 1 or len(ts) == 0:
        return 0.0
    width = (t - t0) / float(k)
    if width <= 0:
        return 0.0
    signs = []
    for i in range(k):
        a = t0 + i * width
        b = t0 + (i + 1) * width
        m = large_mask & (ts > a) & (ts <= b)
        if not np.any(m):
            signs.append(0)
            continue
        s = float(np.sum(notional[m] * side[m].astype(np.float64)))
        signs.append(int(np.sign(s)) if s != 0 else 0)
    nonzero = [s for s in signs if s != 0]
    if not nonzero:
        return 0.0
    maj = 1 if sum(nonzero) > 0 else (-1 if sum(nonzero) < 0 else nonzero[0])
    agree = sum(1 for s in signs if s == maj)
    return agree / float(k)
