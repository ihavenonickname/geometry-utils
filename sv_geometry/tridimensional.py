import math

__all__ = [
    'volume_cylinder',
    'volume_cone',
    'volume_right_frustum',
]

def volume_cylinder(h, r):
    return math.pi * r * r * h

def volume_cone(h, r):
    return volume_cylinder(h, r) / 3

def volume_right_frustum(h, r, R):
    return math.pi * h / 3 * (r*r + R*R + r*R)
