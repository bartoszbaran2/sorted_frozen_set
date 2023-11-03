# Set operations
from collections.abc import Set

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


def test_issubset_eq_positive():
    s = SortedFrozenSet({1, 2, 3})
    t = [1, 2, 3]
    assert s.issubset(t)


def test_issubset_lt_positive():
    s = SortedFrozenSet({1, 2})
    t = [1, 2, 3]
    assert s.issubset(t)


def test_issubset_negative():
    s = SortedFrozenSet({1, 2, 3})
    t = [1, 2]
    assert not s.issubset(t)


def test_issuperset_gt_positive():
    s = SortedFrozenSet({1, 2, 3})
    t = [1, 2]
    assert s.issuperset(t)


def test_issuperset_eq_positive():
    s = SortedFrozenSet({1, 2, 3})
    t = [1, 2, 3]
    assert s.issuperset(t)


def test_issuperset_negative():
    s = SortedFrozenSet({1, 2})
    t = [1, 2, 3]
    assert not s.issuperset(t)


def tes_isdisjoint_positive():
    s = SortedFrozenSet([1, 2, 3])
    t = [4, 5, 6]
    assert s.isdisjoint(t)


def tes_isdisjoint_negative():
    s = SortedFrozenSet([1, 2, 3])
    t = [3, 4, 5]
    assert s.isdisjoint(t)


def test_intersection_method():
    s = SortedFrozenSet([1, 2, 3])
    t = [2, 3, 4]
    assert s.intersection(t) == SortedFrozenSet({2, 3})


def test_intersection_operator():
    s = SortedFrozenSet([1, 2, 3])
    t = SortedFrozenSet([2, 3, 4])
    assert s & t == SortedFrozenSet({2, 3})


def test_union_method():
    s = SortedFrozenSet([1, 2, 3])
    t = [2, 3, 4]
    assert s.union(t) == SortedFrozenSet({1, 2, 3, 4})


def test_union_operator():
    s = SortedFrozenSet([1, 2, 3])
    t = SortedFrozenSet([2, 3, 4])
    assert s | t == SortedFrozenSet({1, 2, 3, 4})


def test_symmetric_difference_method():
    s = SortedFrozenSet([1, 2, 3])
    t = [2, 3, 4]
    assert s.symmetric_difference(t) == SortedFrozenSet({1, 4})


def test_symmetric_difference_operator():
    s = SortedFrozenSet([1, 2, 3])
    t = SortedFrozenSet([2, 3, 4])
    assert s ^ t == SortedFrozenSet({1, 4})


def test_difference_method():
    s = SortedFrozenSet([1, 2, 3])
    t = [2, 3, 4]
    assert s.difference(t) == SortedFrozenSet({1})


def test_difference_operator():
    s = SortedFrozenSet([1, 2, 3])
    t = SortedFrozenSet([2, 3, 4])
    assert s - t == SortedFrozenSet({1})


def test_set_protocol():
    assert issubclass(SortedFrozenSet, Set)
