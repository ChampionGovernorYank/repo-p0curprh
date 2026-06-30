"""Tests for mathutils.geometry module."""

import math
import pytest
from src.mathutils.geometry import circle_area, rectangle_area, triangle_area, sphere_volume


class TestCircleArea:
    def test_unit_circle(self):
        assert abs(circle_area(1) - math.pi) < 1e-10

    def test_radius_5(self):
        assert abs(circle_area(5) - 25 * math.pi) < 1e-10

    def test_zero_radius(self):
        assert circle_area(0) == 0

    def test_negative_radius_raises(self):
        with pytest.raises(ValueError):
            circle_area(-1)


class TestRectangleArea:
    def test_basic(self):
        assert rectangle_area(3, 4) == 12

    def test_square(self):
        assert rectangle_area(5, 5) == 25

    def test_zero_dimension(self):
        assert rectangle_area(0, 10) == 0

    def test_negative_width_raises(self):
        with pytest.raises(ValueError):
            rectangle_area(-1, 5)

    def test_negative_height_raises(self):
        with pytest.raises(ValueError):
            rectangle_area(5, -1)


class TestTriangleArea:
    def test_basic(self):
        assert triangle_area(6, 4) == 12

    def test_zero_base(self):
        assert triangle_area(0, 5) == 0

    def test_negative_base_raises(self):
        with pytest.raises(ValueError):
            triangle_area(-1, 5)

    def test_negative_height_raises(self):
        with pytest.raises(ValueError):
            triangle_area(5, -1)


class TestSphereVolume:
    def test_unit_sphere(self):
        expected = (4 / 3) * math.pi
        assert abs(sphere_volume(1) - expected) < 1e-10

    def test_radius_3(self):
        expected = (4 / 3) * math.pi * 27
        assert abs(sphere_volume(3) - expected) < 1e-10

    def test_zero_radius(self):
        assert sphere_volume(0) == 0

    def test_negative_radius_raises(self):
        with pytest.raises(ValueError):
            sphere_volume(-2)
