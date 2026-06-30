"""Tests for mathutils.statistics module."""

import pytest
from src.mathutils.statistics import mean, median, mode, standard_deviation


class TestMean:
    def test_basic(self):
        assert mean([1, 2, 3, 4, 5]) == 3.0

    def test_single_value(self):
        assert mean([7]) == 7.0

    def test_negative_numbers(self):
        assert mean([-1, -2, -3]) == -2.0

    def test_floats(self):
        assert abs(mean([1.5, 2.5, 3.5]) - 2.5) < 1e-10

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            mean([])


class TestMedian:
    def test_odd_length(self):
        assert median([1, 3, 5]) == 3

    def test_even_length(self):
        assert median([1, 2, 3, 4]) == 2.5

    def test_single_value(self):
        assert median([42]) == 42

    def test_unsorted_input(self):
        assert median([5, 1, 3]) == 3

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            median([])


class TestMode:
    def test_single_mode(self):
        assert mode([1, 2, 2, 3]) == 2

    def test_multiple_modes(self):
        result = mode([1, 1, 2, 2, 3])
        assert set(result) == {1, 2}

    def test_all_same(self):
        assert mode([5, 5, 5]) == 5

    def test_no_repeats(self):
        result = mode([1, 2, 3])
        assert isinstance(result, list)

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            mode([])


class TestStandardDeviation:
    def test_basic(self):
        result = standard_deviation([2, 4, 4, 4, 5, 5, 7, 9])
        assert abs(result - 2.0) < 0.01

    def test_all_same(self):
        assert standard_deviation([5, 5, 5, 5]) == 0.0

    def test_two_values(self):
        result = standard_deviation([0, 10])
        assert abs(result - 5.0) < 1e-10

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            standard_deviation([])
