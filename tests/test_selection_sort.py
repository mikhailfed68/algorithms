from algorithms.selection_sort import find_smallest
from algorithms.selection_sort import selection_sort


def test_find_smallest():
    assert find_smallest([3, 5, 1, 6, 8, -1]) == 5


def test_selection_sort():
    assert selection_sort([2, 5, 6, 8, 1, -6, -10, 9]) == [-10, -6, 1, 2, 5, 6, 8, 9]
