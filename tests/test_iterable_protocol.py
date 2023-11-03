from collections.abc import Iterable

import pytest

from sorted_frozen_set.sorted_frozen_set import SortedFrozenSet
from sorted_frozen_set.tests.fixtures import s1


# Iterable protocol(iter) - '__iter__'
def test_iter(s1):
    iterator = iter(s1)
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 7
    assert next(iterator) == 9

    with pytest.raises(StopIteration) as ctx:
        next(iterator)
    assert '<ExceptionInfo StopIteration()' in str(ctx)


def test_for_loop(s1):
    expected = [1, 2, 7, 9]
    index = 0

    for item in s1:
        assert item == expected[index]
        index += 1


def test_iterable_protocol():
    assert issubclass(SortedFrozenSet, Iterable)
