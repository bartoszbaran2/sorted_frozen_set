from sorted_frozen_set.sorted_frozen_set import SortedFrozenSet


# Inequality protocol(!=)

def test_positive_unequal():
    assert SortedFrozenSet([4, 5, 6]) != SortedFrozenSet([1, 2, 3])


def test_negative_unequal():
    assert not SortedFrozenSet([4, 5, 6]) != SortedFrozenSet([6, 5, 4])


def test_type_mismatch_unequal():
    assert SortedFrozenSet([1, 2, 3]) != [1, 2, 3]


def test_identical_unequal():
    s = SortedFrozenSet([1, 2, 3])
    assert not (s != s)
