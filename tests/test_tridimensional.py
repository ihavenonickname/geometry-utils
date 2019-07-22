import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sv_geometry import tridimensional, SVGeometryException

class Tridimensional(unittest.TestCase):
    def test_volume_cone(self):
        expected = 1047.2

        actual = tridimensional.volume_cone(10, 10)

        self.assertAlmostEqual(actual, expected, places=1)

    def test_volume_cylinder(self):
        expected = 3141.6

        actual = tridimensional.volume_cylinder(10, 10)

        self.assertAlmostEqual(actual, expected, places=1)

    def test_volume_right_frustum(self):
        expected = 1162.4

        actual = tridimensional.volume_frustum(10, 1, 10)

        self.assertAlmostEqual(actual, expected, places=1)

    def test_volume_cone_should_fail_with_negative_parameters(self):
        with self.assertRaises(SVGeometryException):
            tridimensional.volume_cone(-10, 10)

        with self.assertRaises(SVGeometryException):
            tridimensional.volume_cone(10, -10)

    def test_volume_cylinder_should_fail_with_negative_parameters(self):
            with self.assertRaises(SVGeometryException):
                tridimensional.volume_cylinder(-10, 10)

            with self.assertRaises(SVGeometryException):
                tridimensional.volume_cylinder(10, -10)

    def test_volume_right_frustum_should_fail_with_negative_parameters(self):
            with self.assertRaises(SVGeometryException):
                tridimensional.volume_frustum(-10, 1, 10)

            with self.assertRaises(SVGeometryException):
                tridimensional.volume_frustum(10, -1, 10)

            with self.assertRaises(SVGeometryException):
                tridimensional.volume_frustum(10, 1, -10)

if __name__ == '__main__':
    unittest.main()
