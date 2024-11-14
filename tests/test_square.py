import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):

    def test_area_positive_side(self):
        self.assertEqual(area(4), 16)

    def test_perimeter_positive_side(self):
        self.assertEqual(perimeter(4), 16)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            area(-4)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(-4)


if __name__ == '__main__':
    unittest.main()
