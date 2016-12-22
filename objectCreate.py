import arcade.key
from platform import Platform
from ball import Ball

DIR_UP = 1
DIR_STOP = 0
DIR_DOWN = -1
BLUE = 1
Red = 0

class Creator:

    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.blue_platform = BluePlatform(25, 300)
        self.red_platform = RedPlatform(975, 300)
        self.ball = Ball(515, 315)
 
    def animate(self, delta):
        self.blue_platform.animate(delta)
        self.red_platform.animate(delta)
        self.ball.animate(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.W:
            self.blue_platform.controller(DIR_UP)
        if key == arcade.key.Q:
            self.blue_platform.controller(DIR_STOP)
        if key == arcade.key.S:
            self.blue_platform.controller(DIR_DOWN)
        if key == arcade.key.O:
            self.red_platform.controller(DIR_UP)
        if key == arcade.key.P:
            self.red_platform.controller(DIR_STOP)
        if key == arcade.key.L:
            self.red_platform.controller(DIR_DOWN)

    def ScoreCount(self, player_type):
        if player_type == 1:
            blue_score = self.ball.blue_score 
            return blue_score
        if player_type == 2:
            red_score = self.ball.red_score 
            return red_score
