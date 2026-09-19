"""Metrics: NW HAC CI, placebos, concentration, grid summary — code-measured only."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Optional

import numpy as np
import pandas as pd


@dataclass
class SliceMetrics:
    slice_name: str
    signal_count: int
    distinct_utc_days: int
    mean_gross_bps: Optional[float]
    mean_net_bps: Optional[float]
    hit_rate: Optional[float]
    low_high_gap_bps: Optional[float]
    gap_nw_ci_low: Optional[float]
    gap_nw_ci_high: Optional[float]
    gap_ci_excludes_zero: Optional[bool]
    concentration_day_frac: Optional[float]
    notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _utc_days(timestamps: pd.Series) -> pd.Series:
    ts = pd.to_datetime(timestamps, utc=True)
    return ts.dt.floor("D")


def distinct_signal_days(df: pd.DataFrame, signal_col: str = "signal") -> int:
    if df.empty or signal_col not in df.columns:
        return 0
    sig = df.loc[df[signal_col]]
    if sig.empty:
        return 0
    return int(_utc_days(sig["timestamp"]).nunique())


def concentration_frac(df: pd.DataFrame, signal_col: str = "signal") -> float:
    """Fraction of RESEARCH (slice) days that carry ≥1 signal."""
    if df.empty:
        return 0.0
    all_days = _utc_days(df["timestamp"]).nunique()
    if all_days == 0:
        return 0.0
    sig_days = distinct_signal_days(df, signal_col)
    return float(sig_days) / float(all_days)


def mean_or_none(x: np.ndarray) -> Optional[float]:
    if x.size == 0:
        return None
    return float(np.mean(x))


def hit_rate(gross_bps: np.ndarray) -> Optional[float]:
    if gross_bps.size == 0:
        return None
    return float(np.mean(gross_bps > 0))


def newey_west_mean_se(x: np.ndarray, lag: int) -> tuple[Optional[float], Optional[float]]:
    """Newey-West HAC SE for the mean of a 1-d series. lag documented = h."""
    n = x.size
    if n < 2:
        return (mean_or_none(x), None)
    x = np.asarray(x, dtype=float)
    mu = float(np.mean(x))
    u = x - mu
    lag = max(0, int(lag))
    gamma0 = float(np.dot(u, u) / n)
    var = gamma0
    for k in range(1, lag + 1):
        w = 1.0 - k / (lag + 1.0)
        gamma_k = float(np.dot(u[k:], u[:-k]) / n)
        var += 2.0 * w * gamma_k
    var = max(var, 0.0)
    se = float(np.sqrt(var / n))
    return mu, se


def nw_ci_for_gap(
    low_returns: np.ndarray,
    high_returns: np.ndarray,
    lag: int,
    alpha: float = 0.05,
) -> dict[str, Any]:
    """CI for (mean_low - mean_high) via NW on concatenated contrast series.

    Constructs per-observation gap proxy by treating low and high as two groups
    and estimating SE of difference of means with NW on the pooled demeaned
    contrast: we form a single series of low samples and high samples is handled
    by difference of means with conservative SE = sqrt(se_l^2 + se_h^2)
    (groups treated as separate HAC processes).
    """
    low = np.asarray(low_returns, dtype=float)
    high = np.asarray(high_returns, dtype=float)
    low = low[np.isfinite(low)]
    high = high[np.isfinite(high)]
    if low.size == 0 or high.size == 0:
        return {
            "gap": None,
            "ci_low": None,
            "ci_high": None,
            "excludes_zero": None,
            "method": "newey_west_diff_means",
            "lag": lag,
        }
    mu_l, se_l = newey_west_mean_se(low, lag)
    mu_h, se_h = newey_west_mean_se(high, lag)
    gap = float(mu_l - mu_h)  # type: ignore[operator]
    if se_l is None or se_h is None:
        return {
            "gap": gap,
            "ci_low": None,
            "ci_high": None,
            "excludes_zero": None,
            "method": "newey_west_diff_means",
            "lag": lag,
        }
    se = float(np.sqrt(se_l**2 + se_h**2))
    # normal approx z for alpha=0.05
    z = 1.959963984540054
    ci_low = gap - z * se
    ci_high = gap + z * se
    return {
        "gap": gap,
        "ci_low": ci_low,
        "ci_high": ci_high,
        "excludes_zero": bool(ci_low > 0 or ci_high < 0),
        "method": "newey_west_diff_means",
        "lag": lag,
        "se": se,
    }


def bootstrap_gap_ci(
    low_returns: np.ndarray,
    high_returns: np.ndarray,
    n_boot: int = 500,
    seed: int = 20260910,
    alpha: float = 0.05,
) -> dict[str, Any]:
    """Optional bootstrap CI for mean_low - mean_high."""
    rng = np.random.default_rng(seed)
    low = np.asarray(low_returns, dtype=float)
    high = np.asarray(high_returns, dtype=float)
    low = low[np.isfinite(low)]
    high = high[np.isfinite(high)]
    if low.size == 0 or high.size == 0:
        return {"gap": None, "ci_low": None, "ci_high": None, "excludes_zero": None}
    gaps = np.empty(n_boot)
    for i in range(n_boot):
        lb = rng.choice(low, size=low.size, replace=True)
        hb = rng.choice(high, size=high.size, replace=True)
        gaps[i] = float(np.mean(lb) - np.mean(hb))
    lo = float(np.quantile(gaps, alpha / 2))
    hi = float(np.quantile(gaps, 1 - alpha / 2))
    gap = float(np.mean(low) - np.mean(high))
    return {
        "gap": gap,
        "ci_low": lo,
        "ci_high": hi,
        "excludes_zero": bool(lo > 0 or hi < 0),
        "method": "bootstrap",
        "n_boot": n_boot,
        "seed": seed,
    }


def slice_metrics(
    df: pd.DataFrame,
    C: float,
    h: int,
    slice_name: str,
    signal_col: str = "signal",
    high_col: str = "high_rv",
    gross_col: str = "gross_bps",
) -> SliceMetrics:
    """Compute metrics for one slice. Empty → None means, not invented zeros-as-evidence."""
    if df.empty:
        return SliceMetrics(
            slice_name=slice_name,
            signal_count=0,
            distinct_utc_days=0,
            mean_gross_bps=None,
            mean_net_bps=None,
            hit_rate=None,
            low_high_gap_bps=None,
            gap_nw_ci_low=None,
            gap_nw_ci_high=None,
            gap_ci_excludes_zero=None,
            concentration_day_frac=0.0,
            notes="empty slice",
        )
    sig = df.loc[df[signal_col] & df[gross_col].notna()]
    high = df.loc[df[high_col] & df[gross_col].notna()]
    gross = sig[gross_col].to_numpy(dtype=float)
    high_g = high[gross_col].to_numpy(dtype=float)
    gap_info = nw_ci_for_gap(gross, high_g, lag=h)
    mean_g = mean_or_none(gross)
    mean_n = None if mean_g is None else float(mean_g - C)
    return SliceMetrics(
        slice_name=slice_name,
        signal_count=int(len(sig)),
        distinct_utc_days=distinct_signal_days(df, signal_col),
        mean_gross_bps=mean_g,
        mean_net_bps=mean_n,
        hit_rate=hit_rate(gross),
        low_high_gap_bps=gap_info["gap"],
        gap_nw_ci_low=gap_info["ci_low"],
        gap_nw_ci_high=gap_info["ci_high"],
        gap_ci_excludes_zero=gap_info["excludes_zero"],
        concentration_day_frac=concentration_frac(df, signal_col),
        notes=f"NW lag=h={h}",
    )


def time_half_stability(
    df_half1: pd.DataFrame,
    df_half2: pd.DataFrame,
    h: int,
    C: float = 7.0,
) -> dict[str, Any]:
    m1 = slice_metrics(df_half1, C=C, h=h, slice_name="research_half1")
    m2 = slice_metrics(df_half2, C=C, h=h, slice_name="research_half2")
    gap1 = m1.low_high_gap_bps
    gap2 = m2.low_high_gap_bps
    same_sign = (
        gap1 is not None
        and gap2 is not None
        and np.sign(gap1) == np.sign(gap2)
        and gap1 != 0
        and gap2 != 0
    )
    return {
        "half1": m1.to_dict(),
        "half2": m2.to_dict(),
        "gap_same_sign": bool(same_sign),
    }


def placebo_tests(
    df: pd.DataFrame,
    h: int,
    seed: int = 20260910,
    Q_hi_default: float = 0.80,
) -> dict[str, Any]:
    """Three placebos vs real low-high gap (RESEARCH frame with features).

    (1) shuffled RV ranks
    (2) random equal-count low-RV bins
    (3) scrambled signs inside low-RV
    """
    rng = np.random.default_rng(seed)
    work = df.copy()
    # Real gap: signal vs high_rv using gross already computed from true signs
    real = slice_metrics(work, C=0.0, h=h, slice_name="real_gross")
    real_gap = real.low_high_gap_bps

    # (1) shuffle RV ranks — reassign RV order, recompute signal vs high
    if work["RV"].notna().sum() == 0:
        return {"real_gap": real_gap, "placebos": {}, "seed": seed, "note": "no RV"}

    rv_vals = work["RV"].to_numpy().copy()
    valid = np.isfinite(rv_vals)
    shuffled = rv_vals.copy()
    shuffled[valid] = rng.permutation(rv_vals[valid])
    p1 = work.copy()
    p1["RV"] = shuffled
    # rebuild signals from shuffled RV vs same trailing quantiles (rank shuffle)
    p1["signal"] = p1["RV"].notna() & p1["Q_lo_trail"].notna() & (p1["RV"] <= p1["Q_lo_trail"]) & (
        p1["r"].abs() > 0
    )
    p1["high_rv"] = p1["RV"].notna() & p1["Q_hi_trail"].notna() & (p1["RV"] >= p1["Q_hi_trail"])
    m1 = slice_metrics(p1, C=0.0, h=h, slice_name="placebo_shuffled_rv")

    # (2) random equal-count low-RV bins
    n_low = int(work["signal"].sum())
    eligible = work["RV"].notna() & work["gross_bps"].notna() & work["r"].notna()
    eligible_idx = np.flatnonzero(eligible.to_numpy())
    p2 = work.copy()
    p2["signal"] = False
    p2["high_rv"] = False
    if n_low > 0 and eligible_idx.size >= n_low:
        chosen = rng.choice(eligible_idx, size=n_low, replace=False)
        p2.loc[p2.index[chosen], "signal"] = True
        # random high bin same count as real high if possible
        n_high = int(work["high_rv"].sum())
        remain = np.setdiff1d(eligible_idx, chosen, assume_unique=False)
        if n_high > 0 and remain.size >= n_high:
            hchosen = rng.choice(remain, size=n_high, replace=False)
            p2.loc[p2.index[hchosen], "high_rv"] = True
    m2 = slice_metrics(p2, C=0.0, h=h, slice_name="placebo_random_bins")

    # (3) scrambled signs inside low-RV — flip sign of gross randomly on signals
    p3 = work.copy()
    sig_mask = p3["signal"].to_numpy()
    g = p3["gross_bps"].to_numpy(dtype=float).copy()
    flips = rng.choice([-1.0, 1.0], size=g.size)
    g[sig_mask] = np.abs(g[sig_mask]) * flips[sig_mask]
    p3["gross_bps"] = g
    m3 = slice_metrics(p3, C=0.0, h=h, slice_name="placebo_scrambled_signs")

    def beats(real_g, placebo_g, ci_low, ci_high) -> Optional[bool]:
        if real_g is None or placebo_g is None:
            return None
        # placebo matches or beats real within CI noise if placebo_gap >= real
        # or placebo inside real CI
        if ci_low is not None and ci_high is not None:
            if ci_low <= placebo_g <= ci_high:
                return True
        return bool(placebo_g >= real_g)

    return {
        "real_gap": real_gap,
        "real_ci": {"low": real.gap_nw_ci_low, "high": real.gap_nw_ci_high},
        "placebos": {
            "shuffled_rv_ranks": {
                "gap": m1.low_high_gap_bps,
                "matches_or_beats_real": beats(
                    real_gap, m1.low_high_gap_bps, real.gap_nw_ci_low, real.gap_nw_ci_high
                ),
            },
            "random_equal_count_bins": {
                "gap": m2.low_high_gap_bps,
                "matches_or_beats_real": beats(
                    real_gap, m2.low_high_gap_bps, real.gap_nw_ci_low, real.gap_nw_ci_high
                ),
            },
            "scrambled_signs_in_low_rv": {
                "gap": m3.low_high_gap_bps,
                "matches_or_beats_real": beats(
                    real_gap, m3.low_high_gap_bps, real.gap_nw_ci_low, real.gap_nw_ci_high
                ),
            },
        },
        "seed": seed,
    }


def grid_w_stability(gap_by_W: dict[int, Optional[float]]) -> dict[str, Any]:
    """≥2/3 W keep gap sign (relative to primary / majority non-null)."""
    signs = []
    for w, g in sorted(gap_by_W.items()):
        if g is None or g == 0:
            signs.append((w, 0))
        else:
            signs.append((w, int(np.sign(g))))
    nonzero = [s for _, s in signs if s != 0]
    if not nonzero:
        return {"keep_sign_count": 0, "pass": False, "signs": dict(signs), "ref_sign": None}
    # reference = mode of nonzero signs
    ref = int(np.sign(sum(nonzero)))  # if tie mixed, sum works for ±1 counts
    if sum(nonzero) == 0:
        ref = nonzero[0]
    keep = sum(1 for _, s in signs if s == ref)
    return {
        "keep_sign_count": keep,
        "pass": keep >= 2,
        "signs": {str(w): s for w, s in signs},
        "ref_sign": ref,
    }


def qlo_cliff_flag(gap_by_qlo: dict[float, Optional[float]]) -> bool:
    """True if only a single quantile shows positive gap (overfit cliff)."""
    pos = [q for q, g in gap_by_qlo.items() if g is not None and g > 0]
    return len(pos) == 1 and len(gap_by_qlo) >= 2
