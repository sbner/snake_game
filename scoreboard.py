from turtle import Turtle

TEXT_LOCATION = (0.0, 270.0)
TEXT_COLOR = "white"
TEXT_ALIGN = "center"
FONT = ('Courier', 16, 'bold')
SMALLER_FONT = ('Courier', 12, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.teleport(*TEXT_LOCATION)
        self.color(TEXT_COLOR)
        self.print_score()

    def increase_score(self, amount=1):
        self.clear()
        self.score += amount
        self.print_score()

    def print_score(self):
        self.write(f"Score: {self.score}", align=TEXT_ALIGN, font=FONT)

    def game_over(self):
        self.home()
        self.write("Game Over.", align=TEXT_ALIGN, font=FONT)
        self.teleport(0,-30)
        self.write(f"To try again type 'r'.", align=TEXT_ALIGN, font=SMALLER_FONT)
