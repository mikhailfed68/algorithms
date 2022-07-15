def sum_elem(arr):
    if arr == []:
        return 0
    return 1 + sum_elem(arr[1:])


def sum_arr(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])


def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max
