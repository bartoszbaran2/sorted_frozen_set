# Set operations
from sorted_frozen_set.sorted_frozen_set import SortedFrozenSet


def test_lt_positive():
    s = SortedFrozenSet({1, 2})
    t = SortedFrozenSet({1, 2, 3})
    assert s < t


def test_lt_negative():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({1, 2, 3})
    assert not s < t


def test_le_lt_positive():
    s = SortedFrozenSet({1, 2})
    t = SortedFrozenSet({1, 2, 3})
    assert s <= t


def test_le_eq_positive():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({1, 2, 3})
    assert s <= t


def test_le_negative():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({1, 2})
    assert not s <= t


def test_gte_positive():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({1, 2})
    assert s > t


def test_gte_negative():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({1, 2, 3})
    assert not s > t


def test_ge_gt_positive():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({1, 2})
    assert s >= t


def test_ge_eq_positive():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({1, 2, 3})
    assert s >= t


def test_ge_negative():
    s = SortedFrozenSet({1, 2})
    t = SortedFrozenSet({1, 2, 3})
    assert not s >= t
