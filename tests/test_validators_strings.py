"""Tests for validators.strings module."""

from src.validators.strings import is_email, is_url, is_phone_number, is_strong_password


class TestIsEmail:
    def test_valid_email(self):
        assert is_email("user@example.com") is True

    def test_valid_email_with_dots(self):
        assert is_email("first.last@domain.org") is True

    def test_valid_email_with_plus(self):
        assert is_email("user+tag@gmail.com") is True

    def test_invalid_no_at(self):
        assert is_email("userexample.com") is False

    def test_invalid_no_domain(self):
        assert is_email("user@") is False

    def test_invalid_no_tld(self):
        assert is_email("user@domain") is False

    def test_non_string(self):
        assert is_email(123) is False

    def test_empty_string(self):
        assert is_email("") is False


class TestIsUrl:
    def test_valid_http(self):
        assert is_url("http://example.com") is True

    def test_valid_https(self):
        assert is_url("https://example.com") is True

    def test_valid_with_path(self):
        assert is_url("https://example.com/path/to/page") is True

    def test_invalid_no_scheme(self):
        assert is_url("example.com") is False

    def test_invalid_ftp_scheme(self):
        assert is_url("ftp://example.com") is False

    def test_non_string(self):
        assert is_url(None) is False

    def test_empty_string(self):
        assert is_url("") is False


class TestIsPhoneNumber:
    def test_simple_format(self):
        assert is_phone_number("1234567890") is True

    def test_dashed_format(self):
        assert is_phone_number("123-456-7890") is True

    def test_parentheses_format(self):
        assert is_phone_number("(123) 456-7890") is True

    def test_international_format(self):
        assert is_phone_number("+1-123-456-7890") is True

    def test_invalid_too_short(self):
        assert is_phone_number("12345") is False

    def test_invalid_letters(self):
        assert is_phone_number("123-abc-7890") is False

    def test_non_string(self):
        assert is_phone_number(1234567890) is False


class TestIsStrongPassword:
    def test_strong_password(self):
        assert is_strong_password("Str0ng!Pass") is True

    def test_too_short(self):
        assert is_strong_password("Ab1!") is False

    def test_no_uppercase(self):
        assert is_strong_password("str0ng!pass") is False

    def test_no_lowercase(self):
        assert is_strong_password("STR0NG!PASS") is False

    def test_no_digit(self):
        assert is_strong_password("Strong!Pass") is False

    def test_no_special_char(self):
        assert is_strong_password("Str0ngPass1") is False

    def test_non_string(self):
        assert is_strong_password(12345678) is False

    def test_exactly_8_chars(self):
        assert is_strong_password("Ab1!cdef") is True
