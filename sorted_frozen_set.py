import sys
from bisect import bisect_left
from collections.abc import Set, Sequence
from itertools import chain


class SortedFrozenSet(Sequence, Set):
    def __init__(self, items=None):
        self._items = tuple(sorted(
            set(items) if items is not None
            else set()))

    def __contains__(self, item):
        # return self._items.__contains__(item)  # low level api
        return item in self._items

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        # for item in self._items:
        #     yield item
        return iter(self._items)

    def __getitem__(self, index):
        result = self._items[index]
        return (
            SortedFrozenSet(result)
            if isinstance(index, slice)
            else result
        )

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._items == other._items

    def __repr__(self):
        args = '[' + ', '.join(map(repr, self._items)) + ']' if self._items else ""
        return f'{type(self).__name__}({args})'

    def __hash__(self):
        return hash((type(self), self._items))

    def __add__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return SortedFrozenSet(chain(self._items, other._items))

    def __mul__(self, other):
        if isinstance(other, int):
            raise TypeError(f'Can not multiply sequence by non-int of type {type(other)}')
        return self if other > 0 else SortedFrozenSet()

    def __rmul__(self, other):
        return self * other

    def index(self, item, start=0, stop=sys.maxsize):
        idx = bisect_left(self._items, item, lo=start, hi=stop)
        if (idx < len(self._items)) and self._items[idx] == item:
            return idx
        raise ValueError(f"{item!r} not found")

    def count(self, item):
        return int(item in self)

    def issubset(self, iterable):
        # s = SortedFrozenSet(iterable)
        # for x in self._items:
        #     if x not in s._items:
        #         return False
        # return True

        return self <= SortedFrozenSet(iterable)

    def issuperset(self, iterable):
        return self >= SortedFrozenSet(iterable)

    def intersection(self, iterable):
        return self & SortedFrozenSet(iterable)

    def symmetric_difference(self, iterable):
        return self ^ SortedFrozenSet(iterable)

    def union(self, iterable):
        return self | SortedFrozenSet(iterable)

    def difference(self, iterable):
        return self - SortedFrozenSet(iterable)
