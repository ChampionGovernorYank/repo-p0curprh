"""String analysis utilities."""

from collections import Counter


def count_vowels(text):
    """Count the number of vowels in a string."""
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)


def count_consonants(text):
    """Count the number of consonants in a string."""
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    return sum(1 for char in text if char in consonants)


def is_palindrome(text):
    """Check if a string is a palindrome (ignoring case and spaces)."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def word_frequency(text):
    """Return a dictionary of word frequencies in the text."""
    if not text or not text.strip():
        return {}
    words = text.lower().split()
    return dict(Counter(words))
