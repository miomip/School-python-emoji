from turtle import *


def snurt():
    screensize(bg="black")
    begin_fill()
    circle(120, color("Yellow"))
    end_fill()
    lt(90)
    penup()
    fd(100)
    rt(90)
    fd(50)
    pendown()
    begin_fill()
    circle(35, color("black"))
    end_fill()
    bk(100)
    begin_fill()
    circle(35, color("black"))
    end_fill()
    screensize(500, 500, bg="black")
    hideturtle()
    exitonclick()
