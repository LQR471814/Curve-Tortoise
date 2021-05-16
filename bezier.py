from common.types import *

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


def bezier_interpolation(point_lines: List[Line], steps: int, closed: bool = False) -> List[Point]:
    def find_point_recursive(lines: List[Line]) -> Point:
        new_lines: List[Line] = []

        for i in range(len(lines)):
            if i == 0:
                continue

            last_point = lines[i - 1].point_from_line_proportion(t)
            current_point = lines[i].point_from_line_proportion(t)

            new_lines.append(Line(last_point, current_point))

        if len(new_lines) == 1:
            return new_lines[0].point_from_line_proportion(t)

        return find_point_recursive(new_lines)

    if closed:
        point_lines.append(Line(point_lines[-1].p2.offset(0.001, 0), point_lines[0].p1.offset(0.001, 0)))

    step_size = 1/steps
    t = step_size

    result_points: List[Point] = []
    for i in range(steps):
        result_points.append(find_point_recursive(point_lines))
        t += step_size

    return result_points
