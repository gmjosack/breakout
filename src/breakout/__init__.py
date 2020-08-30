import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Breakout"


class Breakout(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()


def main():
    breakout = Breakout(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    breakout.setup()

    arcade.run()
