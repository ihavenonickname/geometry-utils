import math

def volume_cylinder(h, r):
    return math.pi * r * r * h

def volume_cone(h, r):
    return volume_cylinder(h, r) / 3

def volume_frustrum(h, r, R):
    return math.pi * h / 3 * (r*r + R*R + r*R)
