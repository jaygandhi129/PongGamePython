from turtle import Turtle

COLOR = "white"
SHAPE = "circle"


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.shape(SHAPE)
        self.penup()
        self.setposition(x=0, y=0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # For collision with wall
    def bounce_y(self):
        self.y_move *= -1

    # for collision with paddle
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def does_collide_with_wall(self):
        y = self.ycor()
        if y > 282 or y < -282:
            return True
        else:
            return False

    def reset_ball(self):
        self.goto(x=0, y=0)
        self.move_speed = 0.1
        self.bounce_x()

