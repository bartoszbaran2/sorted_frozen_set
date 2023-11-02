from sorted_frozen_set.tests.fixtures import s


# Container protocol(in/not) - '__contains__'
def test_positive_contained(s):
    assert 7 in s


def test_negative_contained(s):
    assert not (10 in s)


def test_positive_not_contained(s):
    assert 10 not in s


def test_negative_not_contained(s):
    assert not (7 not in s)
