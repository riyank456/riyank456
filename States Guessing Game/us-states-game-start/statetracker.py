from turtle import Turtle

class StateTracker(Turtle):
    def __init__(self):
        super().__init__()
        turtle = Turtle()  # edits here
        turtle.pu()
        turtle.hideturtle()  # edits here

    def write_state(self, x, y, answer):
        self.goto(x, y)  # edits here
        self.pd()  # edits here
        self.write(answer)  # edits here
        self.pu()  # edits here