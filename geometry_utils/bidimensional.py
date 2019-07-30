from .helper import GeometryUtilsException

__all__ = [
    'split_trapezium'
]

def split_trapezium(r_top, r_bottom, H, h):
    '''Split a trapezium in two halves.

    It is expected to be a right trapezium, i.e. its apex is at its center.

    Arguments:
        r_top (float): Upper radius of the trapezium.
        r_bottom (float): Lower radius of the trapezium.
        H (float): Height of the trapezium.
        h (float): Height where the trapezium must be splitted.

    Returns:
        dict: A dict with two keys, "upper" and "lower", each one containing
        another dict with keys "upper_radius", "lower_radius" and "H". The
        "upper" dict describes the property of the upper half of the trapezium,
        whilst "lower" describes the lower half.

    Raises:
        GeometryUtilsException: If any argument is nonpositive or if "h"
        is greater than "H".
    '''

    if r_bottom <= 0:
        raise GeometryUtilsException('"r" must be greater than 0')

    if r_top <= 0:
        raise GeometryUtilsException('"R" must be greater than 0')

    if H <= 0:
        raise GeometryUtilsException('"H" must be greater than 0')

    if h <= 0:
        raise GeometryUtilsException('"h" must be greater than 0')

    if H < h:
        raise GeometryUtilsException('"H" must be greater than "h"')

    x1 = r_bottom
    y1 = 0.0
    x2 = r_top
    y2 = H

    a = (y2 - y1) / (x2 - x1)
    b = -a*x1 + y1

    r_apos = ((h - b) / a)

    return {
        'upper': {
            'upper_radius': r_top,
            'lower_radius': r_apos,
            'height': H - h
        },
        'lower': {
            'upper_radius': r_apos,
            'lower_radius': r_bottom,
            'height': h
        },
    }
