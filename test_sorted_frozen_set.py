from sorted_frozen_set.sorted_frozen_set import SortedFrozenSet


def test_construct_empty():
    SortedFrozenSet([])


def test_construct_from_non_empty_list():
    SortedFrozenSet([7, 8, 3, 1])


def test_construct_no_args():
    SortedFrozenSet()


def test_construct_from_an_iterator():
    items = [7, 8, 3, 1]
    iterator = iter(items)
    SortedFrozenSet(iterator)
