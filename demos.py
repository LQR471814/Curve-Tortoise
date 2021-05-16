import threading
import turtle

import bezier
import renderer
from common.types import *

A = Point(0.1, 0.1)
B = Point(0.3, 0.5)
C = Point(0.7085, 0.376)
D = Point(0.811, 0.084)

test_bezier_points = [
    Line(A, B),
    Line(B, C),
    Line(C, D),
]  # ? All bezier points are between 0 and 1 for easy scaling, this assumes the lines are connected together in the order that the list defines


def draw_original_lines(t: turtle.Turtle, scale: int):
    for line in test_bezier_points:
        t.penup()
        t.goto(line.p1.x * scale, line.p1.y * scale)
        t.pendown()
        t.goto(line.p2.x * scale, line.p2.y * scale)


def demo_renderer():
    scale = 400

    # ? Construct Line turtle
    line_renderer = turtle.Turtle()
    line_renderer.speed(4.5)

    line_renderer.shape('circle')
    line_renderer.shapesize(0.5, 0.5)

    line_renderer.color('green')
    line_renderer.pensize(2)

    # ? Construct Bezier turtle
    tortoise = turtle.Turtle()

    tortoise.shape('circle')
    tortoise.shapesize(0.5, 0.5)

    tortoise.color('red')
    tortoise.pensize(2)

    # ? Run both at the same time
    threading.Thread(
        target=draw_original_lines,
        args=(
            line_renderer,
            scale
        ), daemon=True
    ).start()

    threading.Thread(
        target=renderer.draw,
        args=(
            tortoise,
            scale,
            test_bezier_points,
            40
        ),
        kwargs={
            'closed': True
        }, daemon=True
    ).start()

    # ? Wait for window close
    turtle.done()


def demo_bezier():
    print(" ============= Bezier Points ============= ")
    for point in bezier.bezier_interpolation(test_bezier_points, 20, closed=True):
        print(point)


if __name__ == '__main__':
    demo_bezier()
    demo_renderer()
