import pytest
from sorted_frozen_set.tests.fixtures import s2


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
    assert 'list index out of range' in str(ctx)


def test_index_one_before_the_beginning(s2):
    with pytest.raises(IndexError) as ctx:
        s = s2[-6]
    assert 'list index out of range' in str(ctx)
