import arcade
from dataclasses import dataclass

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Breakout"

PADDLE_WIDTH = 150
PADDLE_HEIGHT = 20

MOVEMENT_SPEED = 8

BALL_DIAMETER = 7


@dataclass
class Paddle:
    center_x: float
    center_y: float
    change_x: float = 0
    change_y: float = 0
    width: float = 150
    height: float = 20
    color: arcade.Color = arcade.color.ANTI_FLASH_WHITE

    def draw(self):
        arcade.draw_rectangle_filled(
            center_x = self.center_x,
            center_y = self.center_y,
            width = self.width,
            height = self.height,
            color = self.color,
        )

    def move(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


@dataclass
class Ball:
    center_x: float
    center_y: float
    change_x: float = 0
    change_y: float = 0
    radius: float = 7
    color: arcade.Color = arcade.color.ANTI_FLASH_WHITE

    def draw(self):
        arcade.draw_circle_filled(
            center_x = self.center_x,
            center_y = self.center_y,
            radius = self.radius,
            color = self.color,
        )

    def move(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


class Breakout(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.paddle = None
        self.ball = None

    def setup(self):
        self.paddle = Paddle(
            center_x = SCREEN_WIDTH / 2,
            center_y = PADDLE_HEIGHT,
        )
        self.ball = Ball(
            center_x = SCREEN_WIDTH / 2,
            center_y = PADDLE_HEIGHT * 3,
        )


    def on_draw(self):
        arcade.start_render()
        self.paddle.draw()
        self.ball.draw()

    def on_update(self, delta_time):
        self.paddle.move()


    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.paddle.change_x -= MOVEMENT_SPEED
        if key == arcade.key.RIGHT:
            self.paddle.change_x += MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.paddle.change_x += MOVEMENT_SPEED
        if key == arcade.key.RIGHT:
            self.paddle.change_x -= MOVEMENT_SPEED



def main():
    breakout = Breakout(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    breakout.setup()

    arcade.run()
