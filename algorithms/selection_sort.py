def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i, item in enumerate(arr):
        if item < smallest:
            smallest = item
            smallest_index = i
    return smallest_index


def selection_sort(arr): # with generator comprehension
    return [arr.pop(find_smallest(arr)) for i in range(len(arr))]
