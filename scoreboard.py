from turtle import Turtle

TEXT_LOCATION = (0.0, 270.0)
TEXT_COLOR = "white"
TEXT_ALIGN = "center"
FONT = ('Courier', 16, 'bold')
SMALLER_FONT = ('Courier', 12, 'bold')
HIGH_SCORE_FILE = "high_score.txt"


def save_high_score(score):
    with open(HIGH_SCORE_FILE, mode="w") as file:
        file.write(str(score))


def get_high_score():
    try:
        with open(HIGH_SCORE_FILE) as file:
            return int(file.read())
    except FileNotFoundError:
        return 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = get_high_score()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.teleport(*TEXT_LOCATION)
        self.color(TEXT_COLOR)
        self.print_score()

    def increase_score(self, amount=1):
        self.score += amount
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=TEXT_ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            save_high_score(self.high_score)
        self.score = 0
        self.print_score()

    def game_over(self):
        self.reset()
        self.home()
        self.write("Game Over.", align=TEXT_ALIGN, font=FONT)
        self.teleport(0,-30)
        self.write(f"To try again type 'r'.", align=TEXT_ALIGN, font=SMALLER_FONT)
