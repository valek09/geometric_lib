import unittest
from calculate import calc
from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter


class TestCalculate(unittest.TestCase):

    def test_calc_circle_area(self):
        result = calc('circle', 'area', [5])
        expected = circle_area(5)
        self.assertAlmostEqual(result, expected, places=5)

    def test_calc_circle_perimeter(self):
        result = calc('circle', 'perimeter', [5])
        expected = circle_perimeter(5)
        self.assertAlmostEqual(result, expected, places=5)

    def test_calc_square_area(self):
        result = calc('square', 'area', [4])
        expected = square_area(4)
        self.assertEqual(result, expected)

    def test_calc_square_perimeter(self):
        result = calc('square', 'perimeter', [4])
        expected = square_perimeter(4)
        self.assertEqual(result, expected)

    def test_calc_invalid_figure(self):
        with self.assertRaises(AssertionError):
            calc('triangle', 'area', [3, 4, 5])

    def test_calc_invalid_function(self):
        with self.assertRaises(AssertionError):
            calc('circle', 'volume', [5])


if __name__ == '__main__':
    unittest.main()
