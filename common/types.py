from typing import List


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f'P({self.x}, {self.y})'

    def offset(self, x, y):
        return Point(self.x + x, self.y + y)

class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

        # ? This is literally just an implementation of stuff you learn in algebra, y'know y = mx + b and all that jazz
        self.slope = (p2.y - p1.y) / (p2.x - p1.x)
        self.y_intercept = p1.y - self.slope*p1.x

    # ? Finds a point on a line given the 'percentage' of the line that the point is on (see: https://javascript.info/article/bezier-curve/bezier3-draw1.svg)
    def point_from_line_proportion(self, proportion: float) -> Point:
        # ? x is 'percentage' of the line segment + the start of the line segment
        x = (self.p2.x - self.p1.x) * proportion + self.p1.x
        y = self.slope * x + self.y_intercept  # ? y = mx + b

        return Point(x, y)

    def __str__(self):
        return f'L (m: {self.slope}, b: {self.y_intercept}): {self.p1} -> {self.p2}'
