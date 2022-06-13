import turtle
from turtle import*

t = turtle.Turtle()

t.speed(100)
bgcolor('black')

for i in range(250):
    t.color('cyan')
    t.circle(i)
    t.left(5)

turtle.done()

