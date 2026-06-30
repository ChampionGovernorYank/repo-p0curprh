"""Additional tests for stringutils.transforms module (snake_to_camel, camel_to_snake)."""

from src.stringutils.transforms import snake_to_camel, camel_to_snake


class TestSnakeToCamel:
    def test_basic(self):
        assert snake_to_camel("hello_world") == "helloWorld"

    def test_multiple_words(self):
        assert snake_to_camel("one_two_three") == "oneTwoThree"

    def test_single_word(self):
        assert snake_to_camel("hello") == "hello"

    def test_empty_string(self):
        assert snake_to_camel("") == ""


class TestCamelToSnake:
    def test_basic(self):
        assert camel_to_snake("helloWorld") == "hello_world"

    def test_multiple_words(self):
        assert camel_to_snake("oneTwoThree") == "one_two_three"

    def test_single_word(self):
        assert camel_to_snake("hello") == "hello"

    def test_empty_string(self):
        assert camel_to_snake("") == ""

    def test_starts_with_upper(self):
        assert camel_to_snake("HelloWorld") == "hello_world"
