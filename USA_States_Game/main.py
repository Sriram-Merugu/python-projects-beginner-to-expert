import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S, States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states_data = data["state"].to_list()
answer = 0
guessed_states = []
for _ in range(50):
    tom = turtle.Turtle()
    tom.hideturtle()
    tom.penup()
    answer_state = screen.textinput(title=f"{answer}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in states_data:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("state_to_learn.csv")
        break
    if answer_state in states_data:
        answer += 1
        guessed_states.append(answer_state)
        sd = data[data.state == answer_state]
        tom.goto(int(sd.x), int(sd.y))
        tom.write(answer_state)


