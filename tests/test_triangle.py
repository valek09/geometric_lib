import unittest
import math
from triangle import area, perimeter


class TestTriangle(unittest.TestCase):

    def test_area_valid_triangle(self):
        a, b, c = 3, 4, 5
        s = (a + b + c) / 2
        expected = math.sqrt(s * (s - a) * (s - b) * (s - c))
        self.assertAlmostEqual(area(a, b, c), expected, places=5)

    def test_perimeter_valid_triangle(self):
        a, b, c = 3, 4, 5
        self.assertEqual(perimeter(a, b, c), a + b + c)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            area(-3, 4, 5)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(3, -4, 5)

    def test_area_invalid_triangle(self):
        with self.assertRaises(ValueError):
            area(1, 2, 3)

    def test_perimeter_invalid_triangle(self):
        with self.assertRaises(ValueError):
            perimeter(1, 2, 3)


if __name__ == '__main__':
    unittest.main()
