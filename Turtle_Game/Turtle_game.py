from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? color: ")
y_positions = [-70, -40, -10, 20, 50, 80]
colors = ["red", "violet", "indigo", "blue", "green", "orange"]
all_turtles = []

for index in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[index])
    all_turtles.append(tim)
if user_bet:
    is_race_on = True

while is_race_on:

    for tom in all_turtles:
        if tom.xcor() > 230:
            is_race_on = False
            winning_color = tom.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 10)
        tom.forward(rand_distance)


screen.exitonclick()
