import time
from turtle import Screen, clearscreen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

SCREEN_RESOLUTION = (600, 600)  # Should be square!
SCREEN_BG_COLOR = "black"
SCREEN_TITLE = "Snake Game"
SCREEN_REFRESH_RATE = .06
COLLISION_DISTANCE = 15
SEGMENT_SIZE = 20
COLLISION_WALL_LIMIT = SCREEN_RESOLUTION[0]/2 - SEGMENT_SIZE  # 280
COLLISION_WITH_TAIL_LIMIT = 10


def start_game():
    clearscreen()

    # Screen Setup
    screen = Screen()
    screen.setup(*SCREEN_RESOLUTION)
    screen.bgcolor(SCREEN_BG_COLOR)
    screen.title(SCREEN_TITLE)

    # Make Animation Update Manual
    screen.tracer(0)

    # Snake Startup
    snake = Snake()

    # Scoreboard Startup
    scoreboard = Scoreboard()

    # Init Food
    food = Food()

    def map_keys(array_of_keys):
        for key in array_of_keys:
            screen.onkeypress(key["function"], key["biding"])

    def exit_game():
        screen.bye()

    # Key mapping
    key_mapping = [
        {
            "function": snake.go_up,
            "biding": "Up"
        },
        {
            "function": snake.go_down,
            "biding": "Down"
        },
        {
            "function": snake.go_left,
            "biding": "Left"
        },
        {
            "function": snake.go_right,
            "biding": "Right"
        },
        {
            "function": exit_game,
            "biding": "Escape"
        },
        {
            "function": start_game,
            "biding": "R"
        },
        {
            "function": start_game,
            "biding": "r"
        }
    ]
    screen.listen()
    map_keys(key_mapping)

    game_over = False

    while not game_over:
        screen.update()
        time.sleep(SCREEN_REFRESH_RATE)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < COLLISION_DISTANCE:
            scoreboard.increase_score()
            snake.extend()
            food.spawn()

        # Detect collision with wall
        x_collision = snake.head.xcor() > COLLISION_WALL_LIMIT or snake.head.xcor() < -COLLISION_WALL_LIMIT
        y_collision = snake.head.ycor() > COLLISION_WALL_LIMIT or snake.head.ycor() < -COLLISION_WALL_LIMIT
        if x_collision or y_collision:
            game_over = True
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.body[1:]:
            if snake.head.distance(segment) < COLLISION_WITH_TAIL_LIMIT:
                game_over = True
                scoreboard.game_over()

    screen.exitonclick()


start_game()
