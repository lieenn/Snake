from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.current_score = 0
        self.goto(0, 270)
        self.update()

    # make a helper method for duplicated codes
    def update(self):
        self.write(f"Score: {self.current_score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)

    def increase(self):
        self.clear()
        self.current_score += 1
        self.update()
