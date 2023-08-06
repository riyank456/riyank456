from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.pu()
        self.goto(-250,250)
        self.pd()
        self.display()

    def update(self):
        self.clear()
        self.level+=1
        self.display()
    def display(self):
        self.write(f'Level: {self.level}', align="left", font=FONT)

    def game_over(self):
        self.pu()
        self.goto(-100,0)
        self.write('GAME OVER', align="left", font=FONT)