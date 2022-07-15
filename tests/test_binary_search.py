from algorithms.binary_search import binary_search


def test_item():
    assert binary_search([5, 4, 3, 2, 1], 3) == 2


def test_none():
    assert binary_search([5, 4, 3, 2, 1], 0) is None
