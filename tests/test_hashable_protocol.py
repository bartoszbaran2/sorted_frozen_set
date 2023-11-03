from collections.abc import Hashable

from sorted_frozen_set.sorted_frozen_set import SortedFrozenSet


# Hashable protocol(hash) - '__hash__'

def test_equal_sets_have_the_same_hash_code():
    assert hash(SortedFrozenSet([5, 3, 1, 4])) == hash(SortedFrozenSet([5, 3, 1, 4]))


def test_hashable_protocol():
    assert issubclass(SortedFrozenSet, Hashable)
