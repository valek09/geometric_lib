import unittest
import math
from circle import area, perimeter


class TestCircle(unittest.TestCase):

    def test_area_positive_radius(self):
        self.assertAlmostEqual(area(5), math.pi * 25, places=5)

    def test_perimeter_positive_radius(self):
        self.assertAlmostEqual(perimeter(5), 2 * math.pi * 5, places=5)

    def test_area_negative_radius(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            perimeter(-5)


if __name__ == '__main__':
    unittest.main()
