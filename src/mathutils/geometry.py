"""Geometry calculations."""

import math


def circle_area(radius):
    """Calculate the area of a circle.

    Raises:
        ValueError: If radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


def rectangle_area(width, height):
    """Calculate the area of a rectangle.

    Raises:
        ValueError: If width or height is negative.
    """
    if width < 0 or height < 0:
        raise ValueError("Width and height cannot be negative")
    return width * height


def triangle_area(base, height):
    """Calculate the area of a triangle.

    Raises:
        ValueError: If base or height is negative.
    """
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative")
    return 0.5 * base * height


def sphere_volume(radius):
    """Calculate the volume of a sphere.

    Raises:
        ValueError: If radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return (4 / 3) * math.pi * radius ** 3
