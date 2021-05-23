from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.setup(width=1200)
screen.title("US States")
image = 'blank_states_img.gif'
screen.addshape(image)

tim = Turtle(image)

writer = Turtle()
writer.hideturtle()
is_game_on = True

data = pandas.read_csv('50_states.csv')
states = data['state'].tolist()
answered_state = []
unanswered_state = []
count = 1
while is_game_on:
    state = screen.textinput(f"Name of State [{len(answered_state)}/50]", "Name of state:").title()

    if state == 'Exit':
        unanswered_state = [s for s in states if s not in answered_state]
        break
    if state in states and state not in answered_state:
        state_data = data[data['state'] == state]
        x_cor = int(state_data['x'])
        y_cor = int(state_data['y'])
        writer.penup()
        writer.goto(x_cor, y_cor)
        writer.pendown()
        writer.write(state)
        answered_state.append(state)

    if len(answered_state) > 50:
        is_game_on = False

if unanswered_state:
    csv_data = {'Unanswered State': unanswered_state}
    pandas.DataFrame(csv_data).to_csv('unans_state.csv')
