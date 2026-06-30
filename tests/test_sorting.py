"""Tests for datautils.sorting module."""

from src.datautils.sorting import bubble_sort, merge_sort, quick_sort


class TestBubbleSort:
    def test_sorted_list(self):
        assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]

    def test_reverse_list(self):
        assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4]

    def test_unsorted_list(self):
        assert bubble_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]

    def test_empty_list(self):
        assert bubble_sort([]) == []

    def test_single_element(self):
        assert bubble_sort([42]) == [42]

    def test_duplicates(self):
        assert bubble_sort([5, 3, 5, 1, 3]) == [1, 3, 3, 5, 5]

    def test_does_not_modify_original(self):
        original = [3, 1, 2]
        bubble_sort(original)
        assert original == [3, 1, 2]


class TestMergeSort:
    def test_sorted_list(self):
        assert merge_sort([1, 2, 3, 4]) == [1, 2, 3, 4]

    def test_reverse_list(self):
        assert merge_sort([4, 3, 2, 1]) == [1, 2, 3, 4]

    def test_unsorted_list(self):
        assert merge_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]

    def test_empty_list(self):
        assert merge_sort([]) == []

    def test_single_element(self):
        assert merge_sort([42]) == [42]

    def test_negative_numbers(self):
        assert merge_sort([-3, -1, -2, 0]) == [-3, -2, -1, 0]

    def test_does_not_modify_original(self):
        original = [3, 1, 2]
        merge_sort(original)
        assert original == [3, 1, 2]


class TestQuickSort:
    def test_sorted_list(self):
        assert quick_sort([1, 2, 3, 4]) == [1, 2, 3, 4]

    def test_reverse_list(self):
        assert quick_sort([4, 3, 2, 1]) == [1, 2, 3, 4]

    def test_unsorted_list(self):
        assert quick_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]

    def test_empty_list(self):
        assert quick_sort([]) == []

    def test_single_element(self):
        assert quick_sort([42]) == [42]

    def test_all_same(self):
        assert quick_sort([7, 7, 7]) == [7, 7, 7]

    def test_does_not_modify_original(self):
        original = [3, 1, 2]
        quick_sort(original)
        assert original == [3, 1, 2]
