from turtle import *

tom = Turtle()
screen = Screen()


def move_forward():
    tom.forward(10)


def move_backward():
    tom.backward(10)


def move_clock():
    circle(10, )


def turn_left():
    tom.setheading(tom.heading() + 10)


def turn_right():
    tom.setheading(tom.heading() - 10)


def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
