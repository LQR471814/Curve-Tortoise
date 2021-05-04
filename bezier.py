# Bezier curves!

import turtle
from typing import List


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f'P({self.x}, {self.y})'


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

# ? Process (Inspired from https://javascript.info/bezier-curve)
# ? 1. Define recursive function below
# ?     2. For every line in the line list that is passed (that isn't the first one (exclude this rule if one is building a closed loop))
# ?         3. Get line before (i - 1) and evaluate the point from line proportion (which is t) (t is time)
# ?         4. Get current line and evaluate the point from line proportion (which is t)
# ?         5. Create a line from the point in step 3 to the point in step 4
# ?         6. Append to list of lines
# ?         7. If length of list is 1 then find the point from line proportion (which is t) of that one line and return point
# ?         8. Recurse and pass list of lines
# ? 10. For every time step execute the following
# ?     11. Call recursive function and append the result to a list of points
# ? 12. Return list of points


def bezier_interpolation(point_lines: List[Line], steps: int) -> List[Point]:
    def find_point_recursive(lines: List[Line]) -> Point:
        new_lines: List[Line] = []

        for i in range(len(lines)):
            if i - 1 < 0:
                continue

            last_point = lines[i - 1].point_from_line_proportion(t)
            current_point = lines[i].point_from_line_proportion(t)

            new_lines.append(Line(last_point, current_point))

        # print(' | '.join([str(line) for line in new_lines])) #? Debug

        if len(new_lines) == 1:
            return new_lines[0].point_from_line_proportion(t)

        return find_point_recursive(new_lines)

    step_size = 1/steps
    t = step_size

    result_points: List[Point] = []
    for i in range(steps):
        # print('----------------------------') #? Debug
        result_points.append(find_point_recursive(point_lines))
        t += step_size

    return result_points


if __name__ == '__main__':
    A = Point(0.1, 0.1)
    B = Point(0.3, 0.5)
    C = Point(0.7085, 0.376)
    D = Point(0.7465, 0.69)

    bezier_points = [
        Line(A, B),
        Line(B, C),
        Line(C, D),
    ]  # ? All bezier points are between 0 and 1 for easy scaling, this assumes the lines are connected together in the order that the list defines

    point_proportion_1 = bezier_points[0].point_from_line_proportion(0.5)
    print(bezier_points[0])
    print(point_proportion_1)

    for point in bezier_interpolation(bezier_points, 20):
        print(point)
