"""Tests for stringutils.transforms module."""

from src.stringutils.transforms import capitalize_words, reverse_string


class TestCapitalizeWords:
    def test_basic(self):
        assert capitalize_words("hello world") == "Hello World"

    def test_empty_string(self):
        assert capitalize_words("") == ""


class TestReverseString:
    def test_basic(self):
        assert reverse_string("hello") == "olleh"

    def test_palindrome(self):
        assert reverse_string("racecar") == "racecar"
