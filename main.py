import turtle
import pandas as  pd

CSV_FILE = "50_states.csv"
IMG_SCREEN = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape(IMG_SCREEN)

turtle.shape(IMG_SCREEN)

data = pd.read_csv(CSV_FILE)
all_states = data.state.to_list()
guessed_states = set()
while len(guessed_states) < 50:
  answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
  if answer_state == "Exit":
    missing_states = [(state) for state in all_states if state not in guessed_states]
    new_data = pd.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv", index=False)
    break

  if answer_state in all_states and answer_state not in guessed_states:
    guessed_states.add(answer_state)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(state_data.x.item(), state_data.y.item())
    t.write(answer_state)