"""String validation utilities."""

import re


def is_email(value):
    """Check if a string is a valid email address format."""
    if not isinstance(value, str):
        return False
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, value))


def is_url(value):
    """Check if a string is a valid URL format."""
    if not isinstance(value, str):
        return False
    pattern = r"^https?://[a-zA-Z0-9]([a-zA-Z0-9.-]*[a-zA-Z0-9])?\.[a-zA-Z]{2,}(/.*)?$"
    return bool(re.match(pattern, value))


def is_phone_number(value):
    """Check if a string matches common phone number formats.

    Supports formats like:
    - (123) 456-7890
    - 123-456-7890
    - +1-123-456-7890
    - 1234567890
    """
    if not isinstance(value, str):
        return False
    pattern = r"^(\+\d{1,3}[- ]?)?\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}$"
    return bool(re.match(pattern, value))


def is_strong_password(value):
    """Check if a password meets strength requirements.

    Requirements:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character
    """
    if not isinstance(value, str):
        return False
    if len(value) < 8:
        return False
    if not re.search(r"[A-Z]", value):
        return False
    if not re.search(r"[a-z]", value):
        return False
    if not re.search(r"\d", value):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
        return False
    return True
