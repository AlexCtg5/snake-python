from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 259)
        self.update_score()
    def update_score(self):
        self.clear()
        self.color("orange")
        self.write(f"Score: {self.score}  Highscore: {self.highscore}", False, "center", ("Style", 25, "bold"))

    def update_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score.txt", "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()



