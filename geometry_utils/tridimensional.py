import math

from .helper import GeometryUtilsException

__all__ = [
    'volume_cylinder',
    'volume_cone',
    'volume_frustum',
]

def volume_cylinder(h, r):
    '''Return the volume of the cylinder.

    Arguments:
        h (float): Height of the cylinder.
        r (float): Radius of the cylinder.

    Returns:
        float: The volume of the cylinder.

    Raises:
        GeometryUtilsException: If any argument is nonpositive.
    '''

    if h <= 0:
        raise GeometryUtilsException('Height must be positive')

    if r <= 0:
        raise GeometryUtilsException('Radius must be positive')

    return math.pi * r * r * h

def volume_cone(h, r):
    '''Return the volume of the cone.

    Arguments:
        h (float): Height of the cone.
        r (float): Radius of the cone.

    Returns:
        float: The volume of the cone.

    Raises:
        GeometryUtilsException: If any argument is nonpositive.
    '''

    if h <= 0:
        raise GeometryUtilsException('Height must be positive')

    if r <= 0:
        raise GeometryUtilsException('Radius must be positive')

    return volume_cylinder(h, r) / 3

def volume_frustum(h, r, R):
    '''Return the volume of the frustum.

    It is expected to be a right frustum, i.e. its apex is at its center.

    Arguments:
        h (float): Height of the frustum.
        r (float): Upper radius of the frumstum.
        R (float): Lower radius of the frumstum.

    Returns:
        float: The volume of the frustum.

    Raises:
        GeometryUtilsException: If any argument is nonpositive.
    '''

    if h <= 0:
        raise GeometryUtilsException('Height must be positive')

    if r <= 0:
        raise GeometryUtilsException('Lower radius must be positive')

    if R <= 0:
        raise GeometryUtilsException('Upper radius must be positive')

    return math.pi * h / 3 * (r*r + R*R + r*R)
