"""Tests for datautils.collections module."""

import pytest
from src.datautils.collections import flatten, chunk, unique, group_by


class TestFlatten:
    def test_flat_list(self):
        assert flatten([1, 2, 3]) == [1, 2, 3]

    def test_nested_list(self):
        assert flatten([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

    def test_deeply_nested(self):
        assert flatten([[[1]], [[2]], [[3]]]) == [1, 2, 3]

    def test_empty_list(self):
        assert flatten([]) == []

    def test_mixed_types(self):
        assert flatten([1, [2, "a"], ["b", [3]]]) == [1, 2, "a", "b", 3]

    def test_tuples_are_flattened(self):
        assert flatten([1, (2, 3), [4, (5,)]]) == [1, 2, 3, 4, 5]


class TestChunk:
    def test_even_chunks(self):
        assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]

    def test_uneven_chunks(self):
        assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

    def test_chunk_size_equals_length(self):
        assert chunk([1, 2, 3], 3) == [[1, 2, 3]]

    def test_chunk_size_larger_than_length(self):
        assert chunk([1, 2], 5) == [[1, 2]]

    def test_chunk_size_one(self):
        assert chunk([1, 2, 3], 1) == [[1], [2], [3]]

    def test_empty_list(self):
        assert chunk([], 3) == []

    def test_invalid_size_raises(self):
        with pytest.raises(ValueError):
            chunk([1, 2, 3], 0)

    def test_negative_size_raises(self):
        with pytest.raises(ValueError):
            chunk([1, 2, 3], -1)


class TestUnique:
    def test_duplicates_removed(self):
        assert unique([1, 2, 2, 3, 3, 3]) == [1, 2, 3]

    def test_preserves_order(self):
        assert unique([3, 1, 2, 1, 3]) == [3, 1, 2]

    def test_no_duplicates(self):
        assert unique([1, 2, 3]) == [1, 2, 3]

    def test_empty_list(self):
        assert unique([]) == []

    def test_strings(self):
        assert unique(["a", "b", "a", "c"]) == ["a", "b", "c"]


class TestGroupBy:
    def test_group_by_length(self):
        result = group_by(["hi", "hey", "hello", "yo"], len)
        assert result == {2: ["hi", "yo"], 3: ["hey"], 5: ["hello"]}

    def test_group_by_even_odd(self):
        result = group_by([1, 2, 3, 4, 5], lambda x: "even" if x % 2 == 0 else "odd")
        assert result == {"odd": [1, 3, 5], "even": [2, 4]}

    def test_empty_list(self):
        assert group_by([], len) == {}

    def test_single_group(self):
        result = group_by([2, 4, 6], lambda x: "even")
        assert result == {"even": [2, 4, 6]}
