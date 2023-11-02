import pytest
from sorted_frozen_set.tests.fixtures import s2
from sorted_frozen_set.sorted_frozen_set import SortedFrozenSet


# Sequence protocol(seq[idx]) - '__getitem__'
def test_index_zero(s2):
    assert s2[0] == 1


def test_index_last(s2):
    assert s2[-1] == 15


def test_index_three(s2):
    assert s2[3] == 13


def test_index_one_beyond_the_end(s2):
    with pytest.raises(IndexError) as ctx:
        s = s2[5]
    assert 'tuple index out of range' in str(ctx)


def test_index_one_before_the_beginning(s2):
    with pytest.raises(IndexError) as ctx:
        s = s2[-6]
    assert 'tuple index out of range' in str(ctx)


def test_slice_from_start(s2):
    assert s2[:3] == SortedFrozenSet([1, 4, 9])


def test_slice_to_end(s2):
    assert s2[3:] == SortedFrozenSet([13, 15])


def test_slice_empty(s2):
    assert s2[10:] == SortedFrozenSet([])


def test_slice_arbitrary(s2):
    assert s2[2:4] == SortedFrozenSet([9, 13])


def test_slice_step(s2):
    assert s2[0:5:2] == SortedFrozenSet([1, 9, 15])


def test_slice_ful(s2):
    assert s2[:] == s2
