import pytest
from sorted_frozen_set.sorted_frozen_set import SortedFrozenSet


@pytest.fixture(scope='function')
def s():
    """return SortedFrozenSEt object"""
    return SortedFrozenSet([6, 7, 3, 9])
