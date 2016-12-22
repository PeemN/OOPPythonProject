import arcade.key
from random import randint
from platform import BluePlatform,RedPlatform
from ball import NormalBall,BlueBall,RedBall

DIR_UP = 1
DIR_STOP = 0
DIR_DOWN = -1
BLUE = 1
Red = 0

class Creator:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.end_state = 0 
        self.hit_count = 0
        self.ball_type = 0
        self.reset = 0
        self.save_ball_pos_x = 0
        self.save_ball_pos_y = 0
        self.blue_platform = BluePlatform(25, 300)
        self.red_platform = RedPlatform(975, 300)   
        self.ball = NormalBall(515, 315)
 
    def animate(self, delta):
        self.blue_platform.animate(delta)
        self.red_platform.animate(delta)
        self.ball.animate(delta)
        if self.hit_count - 5 == 1 and self.reset == 0:
            self.ball_type = randint(0,1)
            if self.ball_type == 0:
                self.ball = BlueBall(515, 315)
            elif self.ball_type == 1:
                self.ball = RedBall(515, 315)
            self.reset = 1
        if self.hit_count - 5 == 0 and self == 1:
            self.reset = 0
        self.ball_reflextion()

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.W:
            self.blue_platform.controller(DIR_UP)
        if key == arcade.key.Q:
            self.red_platform.controller(DIR_STOP)
        if key == arcade.key.S:
            self.blue_platform.controller(DIR_DOWN)
        if key == arcade.key.O:
            self.red_platform.controller(DIR_UP)
        if key == arcade.key.P:
            self.blue_platform.controller(DIR_STOP)
        if key == arcade.key.L:
            self.red_platform.controller(DIR_DOWN)

    def score_count(self, player_type):
        if player_type == 1:
            blue_score = self.ball.blue_score 
            return blue_score
        if player_type == 2:
            red_score = self.ball.red_score 
            return red_score

    def game_end(blue_score, red_score):
        if blue_score == 5:
            self.end_state = 1
        elif red_score == 5:
            self.end_state = 1
    
    def ball_reflextion(self):
        if self.blue_platform.hit(self.ball):
            self.hit_count += 1
            self.ball.inverse_direction_x(1)
        if self.red_platform.hit(self.ball):
            self.hit_count += 1
            self.ball.inverse_direction_x(2)
