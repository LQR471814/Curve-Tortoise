# curve-tortoise

Draw Bezier Curves with Python turtle and interpolate points with curves! *This isn't a python package! It's just me having some fun, that's all.*

### Usage

#### `Calculating Bezier Interpolation`

Usually people think of Bezier curves as points that you can drag around and in doing so manipulate a curve.

That's true, however you also have to have lines that connect the points, otherwise the curve won't know how to flow!

So the easiest method to describe a curve is by defining some points using variables and then connecting them together!

```python
from common.types import *

A = Point(0.1, 0.1)
B = Point(0.3, 0.5)
C = Point(0.5, 0.1)

Line(A, B)
```

Although defining some lines isn't all enough either, you still need to describe how the lines connect! So instead of having some fancy type for this, just define a list, and the order that you put the lines is the order that they will be connected in!

```python
bezier_curve = [
    Line(A, B),
    Line(B, C)
]
```

Then, to calculate the interpolated points along the curve you defined. `Note that the amount of steps defines how many points of interpolation the curve will have (more points = smoother curve).`

```python
import bezier

bezier.bezier_interpolation(bezier_curve, steps=20)
```

#### `Drawing points`

This calculates the curve and draws it with turtle, you have to pass a turtle object to the `draw` function and give it a `scale` (you can give it `steps` too)

```python
import renderer
from common.types import *

tortoise = turtle.Turtle()

A = Point(0.1, 0.1)
B = Point(0.3, 0.5)
C = Point(0.5, 0.1)

renderer.draw(tortoise, 400, [
    Line(A, B),
    Line(B, C)
])
```
