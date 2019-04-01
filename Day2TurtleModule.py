# module turtle practice

import turtle

jerry = turtle.Turtle()

jerry.color("red", "yellow")  # outline, fill
jerry.speed(10)

jerry.begin_fill()
for i in range(50):
    jerry.forward(300)
    jerry.left(170)

jerry.end_fill()

turtle.done()
