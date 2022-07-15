import pytest
from algorithms.quicksort import sum_elem
from algorithms.quicksort import sum_arr
from algorithms.quicksort import max


def test_sum_elem():
    assert sum_elem([3, 5, 1, 6, 8, -1]) == 6


def test_sum_arr():
    assert sum_arr([3, 5, 1, 6, 8, -1]) == 22


def test_max():
    assert max([3, 5, 1, 6, 8, -1]) == 8


def test_fmax_with_elem_less_than_two():
    with pytest.raises(RecursionError):
        max([]) == 0
