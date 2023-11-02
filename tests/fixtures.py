import pytest
from sorted_frozen_set.sorted_frozen_set import SortedFrozenSet


@pytest.fixture(scope='function')
def s():
    """return SortedFrozenSEt object"""
    return SortedFrozenSet([6, 7, 3, 9])


@pytest.fixture
def s1():
    return SortedFrozenSet([7, 2, 1, 1, 9])


@pytest.fixture
def s2():
    return SortedFrozenSet([1, 4, 9, 13, 15])
