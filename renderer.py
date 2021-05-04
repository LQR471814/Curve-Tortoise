import turtle

from bezier import *
from common.types import *


def draw(t: turtle.Turtle, scale: int, bezier_points: List[Line], steps: int = 20):
    # ? Go to starting position
    t.penup()
    t.goto(bezier_points[0].p1.x * scale, bezier_points[0].p1.y * scale)
    t.pendown()

    points = bezier_interpolation(bezier_points, steps)
    for point in points:
        t.goto(point.x * scale, point.y * scale)

    t.penup()
