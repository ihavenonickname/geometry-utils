import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sv_geometry import bidimensional, SVGeometryException

class Trapezium(unittest.TestCase):
    def test_split_in_half(self):
        result = bidimensional.split_trapezium(20, 10, 20, 10)

        self.assertEqual(result, {
            'upper': { 'upper_radius': 10, 'lower_radius': 15, 'H': 10 },
            'lower': { 'upper_radius': 15, 'lower_radius': 20, 'H': 10 },
        })

    def test_fail_when_h_too_high(self):
        with self.assertRaises(SVGeometryException):
            bidimensional.split_trapezium(1, 1, 2, 3)

    def test_fail_when_radius_is_negative(self):
        with self.assertRaises(SVGeometryException):
            bidimensional.split_trapezium(-1, 1, 2, 1)

        with self.assertRaises(SVGeometryException):
            bidimensional.split_trapezium(1, -1, 2, 1)

    def test_fail_with_height_is_negative(self):
        with self.assertRaises(SVGeometryException):
            bidimensional.split_trapezium(1, 1, -2, 1)

        with self.assertRaises(SVGeometryException):
            bidimensional.split_trapezium(1, 1, 2, -1)

if __name__ == '__main__':
    unittest.main()
