"""Sorting algorithm implementations."""


def bubble_sort(lst):
    """Sort a list using bubble sort algorithm.

    Returns a new sorted list without modifying the original.
    """
    arr = lst[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def merge_sort(lst):
    """Sort a list using merge sort algorithm.

    Returns a new sorted list without modifying the original.
    """
    if len(lst) <= 1:
        return lst[:]

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return _merge(left, right)


def _merge(left, right):
    """Merge two sorted lists into a single sorted list."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(lst):
    """Sort a list using quick sort algorithm.

    Returns a new sorted list without modifying the original.
    """
    if len(lst) <= 1:
        return lst[:]

    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
