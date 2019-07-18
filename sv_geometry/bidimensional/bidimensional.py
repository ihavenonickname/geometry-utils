# import math
# import typing

# class Point():
#     def __init__(self, x: float, y: float):
#         self._x = x
#         self._y = y

#     @property
#     def x(self) -> float:
#         return self._x

#     @property
#     def y(self) -> float:
#         return self._y

#     def __repr__(self) -> str:
#         return f'Point({self._x}, {self._y})'

#     def __str__(self) -> str:
#         return f'({self._x}, {self._y})'

#     def __eq__(self, other) -> bool:
#         return (
#             isinstance(other, Point) and
#             other.x == self.x and
#             other.y == self.y
#         )

# class LineSegment():
#     def __init__(self, a: Point, b: Point):
#         if a.x < b.x:
#             self._a = a
#             self._b = b
#         else:
#             self._a = b
#             self._b = a

#     @property
#     def edges(self) -> typing.Tuple[Point, Point]:
#         return self._a, self._b

#     @property
#     def length(self) -> float:
#         x_diff = self._a.x - self._b.x
#         y_diff = self._a.y - self._b.y

#         return math.sqrt(math.pow(x_diff, 2) + math.pow(y_diff, 2))

#     @property
#     def slope(self) -> float:
#         return (self._b.y - self._a.y) / (self._b.x - self._a.x)

#     def __repr__(self) -> str:
#         return f'LineSegment({repr(self._a)}, {repr(self._b)})'

#     def __str__(self) -> str:
#         return f'({self._a}, {self._b})'

#     def __eq__(self, other) -> bool:
#         return isinstance(other, LineSegment) and other.edges == self.edges

# class Angle():
#     def __init__(self, line1: LineSegment, line2: LineSegment):
#         self._line1 = line1
#         self._line2 = line2

#     @property
#     def radians(self) -> float:
#         slope1 = self._line1.slope
#         slope2 = self._line2.slope

#         return (slope2 - slope1) / (1 + slope1 * slope2)

#     @property
#     def degrees(self) -> float:
#         return self.radians * 180 / math.pi

#     def __repr__(self) -> str:
#         return f'Angle{repr(self._line1)}, {repr(self._line2)})'

#     def __str__(self) -> str:
#         return f'{round(self.degrees)}°'

#     def __eq__(self, other) -> bool:
#         return  isinstance(other, Angle) and other.radians == self.radians

# class Triangle():
#     def __init__(self, a: Point, b: Point, c: Point):
#         self._a = a
#         self._b = b
#         self._c = c
#         self._ab = LineSegment(a, b)
#         self._bc = LineSegment(b, c)
#         self._ca = LineSegment(c, a)

#     @property
#     def edges(self) -> typing.Tuple[Point, Point, Point]:
#         return self._a, self._b, self._c

#     @property
#     def perimeter(self) -> float:
#         return self._ab.length + self._bc.length + self._ca.length

#     def __eq__(self, other) -> bool:
#         return isinstance(other, Triangle) and other.edges == self.edges

# ------------------------------------------------------------------------------

#
#        d
#       ¨¨¨
#       ___     :
#      /   \    :
#     /_____\   : H
#    /   :   \  :
#   /    : h  \ :
#  /_____:_____\:
#  ¨¨¨¨¨¨¨¨¨¨¨¨¨
#        D
#

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
