from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.hideturtle()
        self.pu()
        self.goto(-250,250)
        self.pd()
        self.display()

    def update(self):
        self.clear()
        self.points+=1
        self.display()
    def display(self):
        self.write(f'Points: {self.points}', align="left", font=FONT)

    def game_over(self):
        self.pu()
        self.goto(-200,0)
        self.write('All states are guessed!', align="left", font=FONT)