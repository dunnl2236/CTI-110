# Use Turtle to draw triangle and square
# 12/07/2018
# CTI-110 P4T1-Turtle
# Lacey Dunn

import turtle
wn=turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Hello, Tess!')

tess=turtle.Turtle()
tess.color('blue')
tess.pensize(3)

tess.forward(50)
tess.left(120)
tess.forward(50)
tess.left(120)


tess.begin_poly
tess.forward(50)
tess.right(60)
tess.forward(50)
tess.left(90)
tess.forward(50)
tess.right(90)
tess.backward(50)
tess.right(90)
tess.forward(50)


