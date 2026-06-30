"""Type validation utilities."""


def is_integer(value):
    """Check if a value can be converted to an integer."""
    if isinstance(value, bool):
        return False
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False


def is_float(value):
    """Check if a value can be converted to a float."""
    if isinstance(value, bool):
        return False
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def is_numeric(value):
    """Check if a value is numeric (integer or float)."""
    return is_integer(value) or is_float(value)


def is_boolean(value):
    """Check if a value represents a boolean.

    Accepts: True, False, 'true', 'false', '1', '0', 1, 0
    """
    if isinstance(value, bool):
        return True
    if isinstance(value, int) and value in (0, 1):
        return True
    if isinstance(value, str) and value.lower() in ("true", "false", "1", "0", "yes", "no"):
        return True
    return False
