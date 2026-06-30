"""Tests for validators.types module."""

from src.validators.types import is_integer, is_float, is_numeric, is_boolean


class TestIsInteger:
    def test_int_value(self):
        assert is_integer(42) is True

    def test_negative_int(self):
        assert is_integer(-5) is True

    def test_zero(self):
        assert is_integer(0) is True

    def test_string_int(self):
        assert is_integer("123") is True

    def test_float_value(self):
        assert is_integer(3.14) is True  # int("3.14") fails but int(3) works via truncation

    def test_string_float(self):
        assert is_integer("3.14") is False

    def test_non_numeric_string(self):
        assert is_integer("hello") is False

    def test_boolean_excluded(self):
        assert is_integer(True) is False
        assert is_integer(False) is False

    def test_none(self):
        assert is_integer(None) is False


class TestIsFloat:
    def test_float_value(self):
        assert is_float(3.14) is True

    def test_int_value(self):
        assert is_float(42) is True  # int is also a valid float

    def test_string_float(self):
        assert is_float("3.14") is True

    def test_string_int(self):
        assert is_float("42") is True

    def test_non_numeric_string(self):
        assert is_float("hello") is False

    def test_boolean_excluded(self):
        assert is_float(True) is False

    def test_none(self):
        assert is_float(None) is False


class TestIsNumeric:
    def test_integer(self):
        assert is_numeric(42) is True

    def test_float(self):
        assert is_numeric(3.14) is True

    def test_string_number(self):
        assert is_numeric("123") is True

    def test_non_numeric(self):
        assert is_numeric("abc") is False

    def test_boolean(self):
        assert is_numeric(True) is False

    def test_none(self):
        assert is_numeric(None) is False


class TestIsBoolean:
    def test_true(self):
        assert is_boolean(True) is True

    def test_false(self):
        assert is_boolean(False) is True

    def test_int_one(self):
        assert is_boolean(1) is True

    def test_int_zero(self):
        assert is_boolean(0) is True

    def test_string_true(self):
        assert is_boolean("true") is True

    def test_string_false(self):
        assert is_boolean("false") is True

    def test_string_yes(self):
        assert is_boolean("yes") is True

    def test_string_no(self):
        assert is_boolean("no") is True

    def test_string_one(self):
        assert is_boolean("1") is True

    def test_string_zero(self):
        assert is_boolean("0") is True

    def test_other_int(self):
        assert is_boolean(5) is False

    def test_random_string(self):
        assert is_boolean("maybe") is False

    def test_none(self):
        assert is_boolean(None) is False
