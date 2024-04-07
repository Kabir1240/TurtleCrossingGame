from turtle import Turtle
TURTLE_SPEED = 10
TURTLE_START = (0, -280)
FINISH_LINE = 300


class CrossingTurtle(Turtle):
    def __init__(self):
        """
        initializes turtle
        """
        super().__init__()
        # initialize turtle settings
        self.shape("turtle")
        self.speed("fastest")
        self.penup()

        # send turtle to bottom of the screen
        self.goto_starting_pos()

    def move(self) -> None:
        """
        moves turtle forward
        :return: None
        """
        self.forward(TURTLE_SPEED)

    def is_at_finish_line(self) -> bool:
        if self.ycor() >= FINISH_LINE:
            self.goto_starting_pos()
            return True
        else:
            return False

    def goto_starting_pos(self) -> None:
        """
        send turtle to starting position
        :return: None
        """
        self.hideturtle()
        self.setheading(90)
        self.goto(TURTLE_START)
        self.showturtle()

    def dead(self) -> None:
        self.shapesize(stretch_wid=2)
        self.color("tomato")

    def do_nothing(self) -> None:
        """
        does nothing :)
        :return: None
        """
        return