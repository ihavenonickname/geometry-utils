def split_trapezium(R, r, H, h):
    x1 = R
    y1 = 0
    x2 = r
    y2 = H

    a = (y2 - y1) / (x2 - x1)
    b = -a*x1 + y1

    r_apos = ((h - b) / a)

    return {
        'upper': { 'upper_radius': r, 'lower_radios': r_apos, 'H': H - h },
        'lower': { 'upper_radius': r_apos, 'lower_radios': R, 'H': h },
    }
