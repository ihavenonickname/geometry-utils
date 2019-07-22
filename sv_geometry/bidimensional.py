from .exception import SVGeometryException

__all__ = [
    'split_trapezium'
]

def split_trapezium(R, r, H, h):
    '''Split a trapezium in two halves.

    It is expected to be a right trapezium, i.e. its apex is at its center.

    Arguments:
        R (float): Upper radius of the trapezium.
        r (float): Lower radius of the trapezium.
        H (float): Height of the trapezium.
        h (float): Height where the trapezium must be splitted.

    Returns:
        dict: A dict with two keys, "upper" and "lower", each one containing
        another dict with keys "upper_radius", "lower_radius" and "H". The
        "upper" dict describes the property of the upper half of the trapezium,
        whilst "lower" describes the lower half.

    Raises:
        SVGeometryException: If any argument is nonpositive or if "h"
        is greater than "H".
    '''

    if r <= 0:
        raise SVGeometryException('"r" must be greater than 0')

    if R <= 0:
        raise SVGeometryException('"R" must be greater than 0')

    if H <= 0:
        raise SVGeometryException('"H" must be greater than 0')

    if h <= 0:
        raise SVGeometryException('"h" must be greater than 0')

    if H < h:
        raise SVGeometryException('"H" must be greater than "h"')

    x1 = R
    y1 = 0.0
    x2 = r
    y2 = H

    a = (y2 - y1) / (x2 - x1)
    b = -a*x1 + y1

    r_apos = ((h - b) / a)

    return {
        'upper': { 'upper_radius': r, 'lower_radius': r_apos, 'H': H - h },
        'lower': { 'upper_radius': r_apos, 'lower_radius': R, 'H': h },
    }
