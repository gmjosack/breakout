import arcade
from dataclasses import dataclass

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Breakout"

MOVEMENT_SPEED = 8

PADDLE_WIDTH = 150
PADDLE_HEIGHT = 20


class Paddle(arcade.SpriteSolidColor):


    def __init__(self,
        center_x, center_y,
        width=PADDLE_WIDTH, height=PADDLE_HEIGHT,
        color=arcade.color.ANTI_FLASH_WHITE,
    ):
        super().__init__(width=width, height=height, color=color)
        self.center_x = center_x
        self.center_y = center_y

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH - 1



class Ball(arcade.SpriteCircle):
    def __init__(self,
        center_x, center_y, change_x=0, change_y=0,
        radius=7, color=arcade.color.ANTI_FLASH_WHITE,
    ):
        super().__init__(radius=radius, color=color)
        self.change_x = change_x
        self.change_y = change_y
        self.center_x = center_x
        self.center_y = center_y

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x = -self.change_x
        elif self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x

        if self.bottom < 0:
            self.change_y = -self.change_y
        elif self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y


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
            change_x = 5,
            change_y = 5,
        )


    def on_draw(self):
        arcade.start_render()
        self.paddle.draw()
        self.ball.draw()

    def on_update(self, delta_time):
        self.paddle.update()
        self.ball.update()


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
