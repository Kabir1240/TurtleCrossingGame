from turtle import Turtle
import random
COLORS = ["tomato", "spring green", "medium orchid", "orange", "yellow", "deep sky blue"]
X_COR = 300                      # max positive x coordinate on screen
STARTING_SPEED = 30              # starting car speed
SPEED_INCREMENT = 10             # increment of speed after each round
CAR_CHANCE = 1                   # chance of spawning a car every time generate_car() is called


class CarManager:
    def __init__(self):
        """
        Initializes car list
        """
        self.cars = []
        self.car_speed = STARTING_SPEED

    def generate_car(self) -> None:
        """
        Generates a car at the edge of the screen using a randomly generated color and y coordinate
        :return: None
        """
        chance = random.randint(1, CAR_CHANCE)
        if chance == 1:
            # generate random y_cor and color
            random_y_cor = random.randint(-250, 280)
            random_color = random.choice(COLORS)

            # generate a new car using x_cor, y_cor and color
            new_car = Turtle(shape="square", visible=False)
            new_car.speed("fastest")
            new_car.color(random_color)
            new_car.penup()
            new_car.goto(X_COR, random_y_cor)
            new_car.showturtle()
            new_car.shapesize(stretch_len=2)

            # add car to list
            self.cars.append(new_car)

    def move_cars(self) -> None:
        """
        moves all the cars
        :return: None
        """
        for car in self.cars:
            if car.xcor() >= -X_COR - 10:
                # car.goto(x=car.xcor()-self.car+peed, y=car.ycor())
                car.backward(self.car_speed)
            else:
                del car

    def has_collided(self, crossing_turtle:Turtle) -> bool:
        """
        returns True if the turtle has collided with a car, False otherwise
        :param crossing_turtle: a Turtle instance for the game, crossing turtle
        :return: True if the turtle has collided with a car, False otherwise
        """
        for car in self.cars:
            if (car.distance(crossing_turtle) <= 50 and
                    (car.ycor() - 25 < crossing_turtle.ycor() < car.ycor() + 25)):
                return True
        return False

    def increase_car_speed(self):
        # self.car_speed /= 10
        self.car_speed += SPEED_INCREMENT
