from sorted_frozen_set.sorted_frozen_set import SortedFrozenSet


# Equality Protocol

def test_positive_equal():
    assert SortedFrozenSet([4, 5, 6]) == SortedFrozenSet([6, 5, 4])


def test_negative_equal():
    assert not SortedFrozenSet([4, 5, 6]) == SortedFrozenSet([1, 2, 3])


def test_type_mismatch():
    assert not (SortedFrozenSet([1, 2, 3]) == [1, 2, 3])


def test_identical_types():
    s = SortedFrozenSet([1, 2, 3])
    assert s == s
