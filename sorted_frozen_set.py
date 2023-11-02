class SortedFrozenSet:
    def __init__(self, items=None):
        self._items = sorted(set(items) if items is not None else set())

    def __contains__(self, item):
        # return self._items.__contains__(item)  # low level api
        return item in self._items
