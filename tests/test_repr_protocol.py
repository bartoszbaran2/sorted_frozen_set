# Repr protocol(repr) - '__repr__'
from sorted_frozen_set.sorted_frozen_set import SortedFrozenSet


def test_repr_empty():
    s = SortedFrozenSet()
    assert repr(s) == 'SortedFrozenSet()'


def test_repr():
    s = SortedFrozenSet([42, 40, 19])
    assert repr(s) == 'SortedFrozenSet([19, 40, 42])'
