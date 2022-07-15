import pytest
from algorithms.selection_sort import find_smallest
from algorithms.selection_sort import selection_sort


def test_find_smallest():
    assert find_smallest([3, 5, 1, 6, 8, -1]) == 5


def test_find_smallest_with_empty_arr():
    with pytest.raises(IndexError):
        find_smallest([]) == 0


def test_selection_sort():
    assert selection_sort([2, 5, 6, 8, 1, -6, -10]) == [-10, -6, 1, 2, 5, 6, 8]
