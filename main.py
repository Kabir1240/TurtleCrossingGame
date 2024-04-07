from car_manager import CarManager
from scoreboard import Scoreboard
from crossing_turtle import CrossingTurtle
from turtle import Screen
import time
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


# initialize screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("white")
screen.title("Turtle Crossing")

# initialize crossing turtle, car manager and scoreboard
timmy = CrossingTurtle()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.tracer(delay=0)

screen.listen()
screen.onkeypress(key="w", fun=timmy.move)

while True:
    time.sleep(0.1)
    screen.update()

    # generate random cars and move them
    car_manager.generate_car()
    car_manager.generate_car()
    car_manager.move_cars()

    # level complete
    if timmy.is_at_finish_line():
        car_manager.increase_car_speed()
        scoreboard.increase_level()

    # handle collisions with cars
    if car_manager.has_collided(timmy):
        timmy.dead()
        scoreboard.game_over()
        break

# stops user from controlling the turtle
screen.onkeypress(key="w", fun=timmy.do_nothing)
screen.exitonclick()