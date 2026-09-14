"""Deterministic splits + holdout sealed by default."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.splits import (  # noqa: E402
    WARMUP_BARS,
    assert_holdout_exists,
    compute_split_bounds,
    holdout_is_sealed,
)


def test_warmup_constant():
    assert WARMUP_BARS == 48 + 576 == 624


def test_splits_60_20_20_deterministic():
    n = 624 + 1000  # post-warmup = 1000
    b1 = compute_split_bounds(n)
    b2 = compute_split_bounds(n)
    assert b1 == b2
    assert b1.warmup_end == 624
    post = 1000
    assert b1.research_end - b1.research_start == int(post * 0.60)
    assert b1.validation_end - b1.validation_start == int(post * 0.20)
    holdout_n = b1.holdout_end - b1.holdout_start
    assert holdout_n == post - int(post * 0.60) - int(post * 0.20)
    assert b1.holdout_end == n
    assert_holdout_exists(b1)


def test_holdout_remainder_exact():
    for post in (10, 17, 99, 1000, 3333):
        n = 624 + post
        b = compute_split_bounds(n)
        total = (
            (b.research_end - b.research_start)
            + (b.validation_end - b.validation_start)
            + (b.holdout_end - b.holdout_start)
        )
        assert total == post


def test_holdout_sealed_by_default(tmp_path):
    assert holdout_is_sealed(open_holdout=False, conductor_order_path=None) is True
    order = tmp_path / "order.txt"
    # flag without order file → still sealed
    assert holdout_is_sealed(open_holdout=True, conductor_order_path=order) is True
    order.write_text("Conductor opens holdout\n")
    assert holdout_is_sealed(open_holdout=True, conductor_order_path=order) is False


def test_research_halves_partition():
    n = 624 + 100
    b = compute_split_bounds(n)
    m1 = b.slice_mask(n, "research_half1")
    m2 = b.slice_mask(n, "research_half2")
    m_r = b.slice_mask(n, "research")
    assert int(m1.sum() + m2.sum()) == int(m_r.sum())
    assert not (m1 & m2).any()
