# Authors: Jeffrey Ni 
# Assignment: Lab #5
# Completed (or last revision):  02/28/2023

import turtle


# side of a basketball
turtle = turtle.Turtle()
turtle.speed(1)

turtle.pencolor('black')
turtle.fillcolor('orange')
turtle.begin_fill()
turtle.circle(-100)
turtle.end_fill()
turtle.pencolor('black')
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
for i in range(8):
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.setheading(i * 45)
    turtle.forward(100)
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()


# full view of ball
turtle.reset()
turtle.up()
turtle.goto(50, 0)
turtle.down()
turtle.up()
turtle.fillcolor("orange")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
turtle.down()
turtle.up()
turtle.goto(0, 50)
turtle.down()
turtle.fd(100)
turtle.up()
turtle.goto(50, 100)
turtle.down()
turtle.rt(90)
turtle.fd(100)
turtle.up()
turtle.lt(90)
turtle.circle(50, 135)
turtle.down()
turtle.lt(90)
turtle.circle(50, 90)
turtle.up()
turtle.lt(90)
turtle.circle(50, 270)
turtle.down()
turtle.lt(90)
turtle.circle(50, 90)
turtle.ht()
turtle.done()

