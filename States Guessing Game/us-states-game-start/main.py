from turtle import Turtle, Screen
import pandas
from scoreboard import Scoreboard
from statetracker import StateTracker
import csv
screen = Screen()
screen.setup(width=600, height=600)
score_board = Scoreboard()
tracker = StateTracker()
tracker.pu()
tracker.hideturtle()
screen.bgpic('./blank_states_img.gif')
data = pandas.read_csv('./50_states.csv')
states = data.state.tolist()
correct_guesses = []
while(score_board.points!=50):
    answer_state = screen.textinput(title="Guess a state", prompt="What's another state?")
    answer = answer_state.title()

    if answer == 'Exit':
        states_to_learn = []
        for state in states:
            if state not in correct_guesses:
                states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv('states to learn.csv')
        break
    if(answer in states):
        score_board.update()
        x = int(data[data.state == answer].x.iloc[0])
        y = int(data[data.state == answer].y.iloc[0])
        tracker.write_state(x, y, answer)
        correct_guesses.append(answer)

    if(score_board.points == 50):
        score_board.game_over()


# states to learn csv


# with open ('states_to_learn.csv', mode='w') as file:
#     writer = csv.writer(file)
