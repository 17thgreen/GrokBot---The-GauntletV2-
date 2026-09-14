"""Warmup drop + RESEARCH 60% / VALIDATION 20% / SEALED HOLDOUT 20%.

Holdout is SEALED by default: code may assert it exists but MUST NOT evaluate
holdout metrics unless open_holdout=True AND a Conductor order file exists.

When DATA-PROV arrives pre-sliced (SEAL_LOCK / slices/*_{RESEARCH,VALIDATION,...}),
do NOT re-split the full series — use provided slice files. Still compute
RESEARCH time-half 50/50 diagnostic within the research slice.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import pandas as pd

WARMUP_BARS = 624  # max(W)+max(L) = 48+576


@dataclass(frozen=True)
class SplitBounds:
    warmup_end: int  # exclusive end index of warmup (first eligible bar)
    research_start: int
    research_end: int  # exclusive
    validation_start: int
    validation_end: int
    holdout_start: int
    holdout_end: int  # exclusive == n
    n_post_warmup: int
    n_total: int
    pre_sliced: bool = False

    def slice_mask(self, n: int, name: str) -> pd.Series:
        idx = pd.RangeIndex(n)
        if name == "warmup":
            return idx < self.warmup_end
        if name == "research":
            return (idx >= self.research_start) & (idx < self.research_end)
        if name == "validation":
            return (idx >= self.validation_start) & (idx < self.validation_end)
        if name == "holdout":
            return (idx >= self.holdout_start) & (idx < self.holdout_end)
        if name == "research_half1":
            mid = self.research_start + (self.research_end - self.research_start) // 2
            return (idx >= self.research_start) & (idx < mid)
        if name == "research_half2":
            mid = self.research_start + (self.research_end - self.research_start) // 2
            return (idx >= mid) & (idx < self.research_end)
        raise ValueError(f"Unknown slice: {name}")


def compute_split_bounds(
    n_bars: int,
    warmup: int = WARMUP_BARS,
    research_frac: float = 0.60,
    validation_frac: float = 0.20,
    holdout_frac: float = 0.20,
) -> SplitBounds:
    """Deterministic fractional splits AFTER warmup drop.

    Uses floor for research/validation counts; holdout gets the remainder so
    fractions sum exactly to post-warmup length.

    Only for contiguous (non-pre-sliced) series. Prefer bounds_from_presliced
    when DATA-PROV ships slice files.
    """
    if abs(research_frac + validation_frac + holdout_frac - 1.0) > 1e-9:
        raise ValueError("Split fractions must sum to 1.0")
    if n_bars <= warmup:
        # Degenerate: no post-warmup — still return structured zeros for asserts
        return SplitBounds(
            warmup_end=min(warmup, n_bars),
            research_start=min(warmup, n_bars),
            research_end=min(warmup, n_bars),
            validation_start=min(warmup, n_bars),
            validation_end=min(warmup, n_bars),
            holdout_start=min(warmup, n_bars),
            holdout_end=n_bars,
            n_post_warmup=max(0, n_bars - warmup),
            n_total=n_bars,
            pre_sliced=False,
        )
    post = n_bars - warmup
    n_research = int(post * research_frac)
    n_validation = int(post * validation_frac)
    n_holdout = post - n_research - n_validation  # remainder = sealed holdout
    rs = warmup
    re = rs + n_research
    vs = re
    ve = vs + n_validation
    hs = ve
    he = hs + n_holdout
    assert he == n_bars
    return SplitBounds(
        warmup_end=warmup,
        research_start=rs,
        research_end=re,
        validation_start=vs,
        validation_end=ve,
        holdout_start=hs,
        holdout_end=he,
        n_post_warmup=post,
        n_total=n_bars,
        pre_sliced=False,
    )


def bounds_from_presliced(
    n_warmup: int,
    n_research: int,
    n_validation: int,
    n_holdout: int = 0,
) -> SplitBounds:
    """Bounds mirroring on-disk slice lengths (no re-split of a full series).

    Index space is conceptual concat: warmup | research | validation | holdout.
    Holdout length may be 0 when sealed file is not loaded; holdout_file_present
    is tracked separately by the loader.
    """
    rs = n_warmup
    re = rs + n_research
    vs = re
    ve = vs + n_validation
    hs = ve
    he = hs + n_holdout
    post = n_research + n_validation + n_holdout
    return SplitBounds(
        warmup_end=n_warmup,
        research_start=rs,
        research_end=re,
        validation_start=vs,
        validation_end=ve,
        holdout_start=hs,
        holdout_end=he,
        n_post_warmup=post,
        n_total=n_warmup + post,
        pre_sliced=True,
    )


def research_time_halves(n_research: int) -> tuple[int, int]:
    """50/50 diagnostic split within the research slice (indices into research)."""
    mid = n_research // 2
    return mid, n_research - mid


def holdout_is_sealed(
    open_holdout: bool,
    conductor_order_path: Optional[Path] = None,
) -> bool:
    """Holdout sealed unless BOTH --open-holdout AND Conductor order file exist."""
    if not open_holdout:
        return True
    if conductor_order_path is None:
        return True
    return not Path(conductor_order_path).exists()


def assert_holdout_exists(bounds: SplitBounds, *, file_present: Optional[bool] = None) -> None:
    """May compute/assert holdout region exists without evaluating metrics.

    For pre-sliced data, pass file_present from SliceBundle.holdout_file_present
    (Path.exists only — must not open sealed parquet).
    """
    if file_present is not None:
        if not file_present and bounds.holdout_end <= bounds.holdout_start:
            raise AssertionError("Holdout slice missing (pre-sliced sealed file absent)")
        if file_present:
            return
    if bounds.n_post_warmup <= 0:
        raise AssertionError("No post-warmup bars; cannot form holdout")
    if bounds.holdout_end <= bounds.holdout_start:
        raise AssertionError("Holdout slice empty after fractional split")


def apply_slice(df: pd.DataFrame, bounds: SplitBounds, name: str) -> pd.DataFrame:
    mask = bounds.slice_mask(len(df), name)
    return df.loc[mask].copy()
