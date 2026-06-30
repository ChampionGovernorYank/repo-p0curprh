"""Tests for stringutils.analysis module."""

from src.stringutils.analysis import count_vowels, count_consonants, is_palindrome, word_frequency


class TestCountVowels:
    def test_basic(self):
        assert count_vowels("hello") == 2

    def test_all_vowels(self):
        assert count_vowels("aeiou") == 5

    def test_no_vowels(self):
        assert count_vowels("rhythm") == 0

    def test_empty_string(self):
        assert count_vowels("") == 0

    def test_mixed_case(self):
        assert count_vowels("AeIoU") == 5


class TestCountConsonants:
    def test_basic(self):
        assert count_consonants("hello") == 3

    def test_no_consonants(self):
        assert count_consonants("aeiou") == 0

    def test_all_consonants(self):
        assert count_consonants("bcdfg") == 5

    def test_empty_string(self):
        assert count_consonants("") == 0

    def test_with_spaces_and_digits(self):
        assert count_consonants("hi 123") == 1


class TestIsPalindrome:
    def test_simple_palindrome(self):
        assert is_palindrome("racecar") is True

    def test_with_spaces(self):
        assert is_palindrome("a man a plan a canal panama") is True

    def test_mixed_case(self):
        assert is_palindrome("Madam") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False

    def test_single_char(self):
        assert is_palindrome("a") is True

    def test_empty_string(self):
        assert is_palindrome("") is True


class TestWordFrequency:
    def test_basic(self):
        result = word_frequency("the cat and the dog")
        assert result == {"the": 2, "cat": 1, "and": 1, "dog": 1}

    def test_case_insensitive(self):
        result = word_frequency("Hello hello HELLO")
        assert result == {"hello": 3}

    def test_empty_string(self):
        assert word_frequency("") == {}

    def test_whitespace_only(self):
        assert word_frequency("   ") == {}

    def test_single_word(self):
        assert word_frequency("word") == {"word": 1}
