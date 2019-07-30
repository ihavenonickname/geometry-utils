import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sv_geometry import bidimensional, SVGeometryException

class Bidimensional(unittest.TestCase):
    def test_split_trapezium_half(self):
        expected = {
            'upper': { 'upper_radius': 10, 'lower_radius': 15, 'height': 10 },
            'lower': { 'upper_radius': 15, 'lower_radius': 20, 'height': 10 },
        }

        actual = bidimensional.split_trapezium(10, 20, 20, 10)

        self.assertEqual(expected, actual)

    def test_split_trapezium_quarter(self):
        actual = bidimensional.split_trapezium(10, 20, 10, 4)

        self.assertGreater(actual['upper']['height'], actual['lower']['height'])

    def test_split_trapezium_should_fail_when_h_is_too_large(self):
        with self.assertRaises(SVGeometryException):
            bidimensional.split_trapezium(1, 1, 2, 3)

    def test_split_trapezium_should_fail_when_radius_is_negative(self):
        with self.assertRaises(SVGeometryException):
            bidimensional.split_trapezium(-1, 1, 2, 1)

        with self.assertRaises(SVGeometryException):
            bidimensional.split_trapezium(1, -1, 2, 1)

    def test_split_trapezium_should_fail_with_height_is_negative(self):
        with self.assertRaises(SVGeometryException):
            bidimensional.split_trapezium(1, 1, -2, 1)

        with self.assertRaises(SVGeometryException):
            bidimensional.split_trapezium(1, 1, 2, -1)

if __name__ == '__main__':
    unittest.main()
