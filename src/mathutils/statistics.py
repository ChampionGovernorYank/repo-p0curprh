"""Statistical functions."""

from collections import Counter


def mean(numbers):
    """Calculate the arithmetic mean of a list of numbers.

    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(numbers) / len(numbers)


def median(numbers):
    """Calculate the median of a list of numbers.

    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]


def mode(numbers):
    """Find the mode (most common value) of a list of numbers.

    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate mode of empty list")
    counter = Counter(numbers)
    max_count = max(counter.values())
    modes = [num for num, count in counter.items() if count == max_count]
    return modes[0] if len(modes) == 1 else modes


def standard_deviation(numbers):
    """Calculate the population standard deviation.

    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate standard deviation of empty list")
    avg = mean(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5
