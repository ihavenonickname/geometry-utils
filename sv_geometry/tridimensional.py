import math

from .exception import SVGeometryException

__all__ = [
    'volume_cylinder',
    'volume_cone',
    'volume_right_frustum',
]

def volume_cylinder(h, r):
    if h <= 0:
        raise SVGeometryException('Height must be positive')

    if r <= 0:
        raise SVGeometryException('Radius must be positive')

    return math.pi * r * r * h

def volume_cone(h, r):
    if h <= 0:
        raise SVGeometryException('Height must be positive')

    if r <= 0:
        raise SVGeometryException('Radius must be positive')

    return volume_cylinder(h, r) / 3

def volume_right_frustum(h, r, R):
    if h <= 0:
        raise SVGeometryException('Height must be positive')

    if r <= 0:
        raise SVGeometryException('Lower radius must be positive')

    if R <= 0:
        raise SVGeometryException('Upper radius must be positive')

    return math.pi * h / 3 * (r*r + R*R + r*R)
