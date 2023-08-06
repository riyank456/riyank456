from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.setpos(STARTING_POSITION)
        self.seth(90)
        self.shape("turtle")
        self.color("green")



    def move(self):
        self.forward(MOVE_DISTANCE)

