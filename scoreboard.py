from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.status = ""
        self.level = 1
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f"LEVEL: {self.level}", align="center", font=FONT)
        self.goto(0, 0)
        self.write(self.status, align="center", font=FONT)
        
    def gameover(self):
        self.status = "Game Over"
        self.update_scoreboard()
        
    def level_up(self):
        self.level += 1
        self.update_scoreboard()
