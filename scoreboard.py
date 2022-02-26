from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
GAME_COORDS = (-200, 260)
HS_COORDS = (140, 260)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.final_score = 0
        self.high_score = 0
        self.load_high_score()
        self.write_score()

    def load_high_score(self):
        with open("highscore.txt", "r") as hsfile:
            self.high_score = hsfile.read()
            self.high_score = int(self.high_score)

    def write_score(self):
        self.penup()
        self.goto(GAME_COORDS)
        self.color("white")
        self.write(align=ALIGNMENT, font=FONT, arg=f"Score: {self.score}")
        self.goto(HS_COORDS)
        self.write(align=ALIGNMENT, font=FONT, arg=f"High Score: {self.high_score}")
        self.hideturtle()

    def game_over(self):
        self.reset_score()
        self.clear()
        self.penup()
        self.goto(x=0, y=50)
        self.color("white")
        self.write(align=ALIGNMENT, font=FONT, arg="GAME OVER")
        self.goto(x=0, y=-0)
        self.write(align=ALIGNMENT, font=FONT, arg=f"Score: {self.final_score}")
        self.goto(x=0, y=-50)
        self.write(align=ALIGNMENT, font=FONT, arg=f"High Score: {self.high_score}")
        self.goto(x=0, y=-100)
        self.write(align=ALIGNMENT, font=FONT, arg="Press Space to play again.")
        self.hideturtle()
        self.final_score = 0

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def reset_score(self):
        print(f"What is score: {self.score} and what is hs: {self.high_score}")
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", "w") as hsfile:
                hsfile.write(str(self.high_score))
        self.final_score = self.score
        self.score = 0
#         check high score

