from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')
LEVEL_POS = (-250, 275)


class Scoreboard(Turtle):
    def __init__(self):
        """
        Initializes turtles settings
        """
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(LEVEL_POS)
        self.update()

    def update(self) -> None:
        """
        clears previous level and updates the text to the new level
        :return: None
        """
        self.clear()
        self.write(f"Level: {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def increase_level(self) -> None:
        """
        increases the level on the board
        :return: None
        """
        self.level += 1
        self.update()

    def game_over(self) -> None:
        """
        visual representation of dead turtle
        :return: None
        """
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)