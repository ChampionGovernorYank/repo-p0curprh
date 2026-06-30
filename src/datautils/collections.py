"""Collection manipulation utilities."""


def flatten(nested_list):
    """Flatten a nested list into a single list."""
    result = []
    for item in nested_list:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def chunk(lst, size):
    """Split a list into chunks of the specified size.

    Raises:
        ValueError: If size is less than 1.
    """
    if size < 1:
        raise ValueError("Chunk size must be at least 1")
    return [lst[i : i + size] for i in range(0, len(lst), size)]


def unique(lst):
    """Return unique elements while preserving order."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def group_by(lst, key_func):
    """Group elements by the result of key_func.

    Args:
        lst: List of items to group.
        key_func: Function that returns the grouping key for each item.

    Returns:
        Dictionary mapping keys to lists of items.
    """
    groups = {}
    for item in lst:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups
