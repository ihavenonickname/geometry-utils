from .exception import SVGeometryException

__all__ = [
    'split_trapezium'
]

def split_trapezium(R, r, H, h):
    R = float(R)
    r = float(r)
    H = float(H)
    h = float(h)

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
