import arcade
from dataclasses import dataclass

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Breakout"

PADDLE_WIDTH = 150
PADDLE_HEIGHT = 20

NUM_X_BRICKS = 10
BRICK_PADDING = 8
BRICK_WIDTH = SCREEN_WIDTH // NUM_X_BRICKS - (BRICK_PADDING + 1)
BRICK_HEIGHT = PADDLE_HEIGHT


BRICK_COLORS = {
    "R": arcade.color.BITTERSWEET,
    "O": arcade.color.ATOMIC_TANGERINE,
    "Y": arcade.color.BANANA_YELLOW,
    "G": arcade.color.ANDROID_GREEN,
    "B": arcade.color.BLUE_GRAY,
}

LEVEL_1 = [
    "RRRRRRRRRR",
    "OOOOOOOOOO",
    "YYYYYYYYYY",
    "GGGGGGGGGG",
    "BBBBBBBBBB",
]


class Brick(arcade.SpriteSolidColor):
    def __init__(self,
        center_x, center_y, color,
        width=BRICK_WIDTH,
        height=BRICK_HEIGHT,
    ):
        super().__init__(width=width, height=height, color=color)
        self.center_x = center_x
        self.center_y = center_y


class Paddle(arcade.SpriteSolidColor):

    DEFAULT_SPEED = 8

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

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.change_x -= self.DEFAULT_SPEED
        if key == arcade.key.RIGHT:
            self.change_x += self.DEFAULT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.change_x += self.DEFAULT_SPEED
        if key == arcade.key.RIGHT:
            self.change_x -= self.DEFAULT_SPEED


class Ball(arcade.SpriteCircle):
    def __init__(self,
        center_x, center_y, change_x=0, change_y=0,
        radius=7, color=arcade.color.ANTI_FLASH_WHITE,
    ):
        super().__init__(radius=radius, color=color)
        self.window = arcade.get_window()
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

        if self.collides_with_sprite(self.window.paddle):
            self.change_y = -self.change_y

        bricks_hit = self.collides_with_list(self.window.brick_list)
        if bricks_hit:
            self.change_y = -self.change_y
            for brick in bricks_hit:
                brick.remove_from_sprite_lists()


class Breakout(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.paddle = None
        self.ball = None
        self.brick_list = None

    def setup(self):
        self.paddle = Paddle(
            center_x = SCREEN_WIDTH // 2,
            center_y = PADDLE_HEIGHT,
        )
        self.ball = Ball(
            center_x = SCREEN_WIDTH // 2,
            center_y = PADDLE_HEIGHT * 3,
            change_x = 5,
            change_y = 5,
        )

        self.brick_list = arcade.SpriteList(use_spatial_hash=True)
        for idx, row in enumerate(LEVEL_1):
            center_y = SCREEN_HEIGHT - (
                (BRICK_PADDING + (BRICK_HEIGHT // 2)) + ((BRICK_HEIGHT + BRICK_PADDING) * idx)
            )

            for brick_idx, color in enumerate(row):
                center_x = (BRICK_PADDING + (BRICK_WIDTH // 2)) + ((BRICK_WIDTH + BRICK_PADDING) * brick_idx)
                color = BRICK_COLORS[color]
                brick = Brick(center_x=center_x, center_y=center_y, color=color)
                self.brick_list.append(brick)


    def on_draw(self):
        arcade.start_render()
        self.paddle.draw()
        self.ball.draw()
        self.brick_list.draw()

    def on_update(self, delta_time):
        self.paddle.update()
        self.brick_list.update()
        self.ball.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.close()
        self.paddle.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.paddle.on_key_release(key, modifiers)


def main():
    breakout = Breakout(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    breakout.setup()

    arcade.run()
