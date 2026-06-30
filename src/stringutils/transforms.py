"""String transformation utilities."""


def capitalize_words(text):
    """Capitalize the first letter of each word."""
    if not text:
        return text
    return " ".join(word.capitalize() for word in text.split())


def reverse_string(text):
    """Reverse a string."""
    return text[::-1]


def snake_to_camel(text):
    """Convert snake_case to camelCase."""
    if not text:
        return text
    components = text.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def camel_to_snake(text):
    """Convert camelCase to snake_case."""
    if not text:
        return text
    result = [text[0].lower()]
    for char in text[1:]:
        if char.isupper():
            result.append("_")
            result.append(char.lower())
        else:
            result.append(char)
    return "".join(result)
