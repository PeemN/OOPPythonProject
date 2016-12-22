from random import randint
from platform import BluePlatform, RedPlatform

class Ball:

    SAVE_POINT_X = 0
    SAVE_POINT_Y = 0
    STATE = 0
    direction = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.red_score = 0
        self.blue_score = 0
        self.state = Ball.STATE
        Ball.SAVE_POINT_X = x
        Ball.SAVE_POINT_Y = y
        
    def animate(self, delta):
        if Ball.STATE == 0:
            Ball.direction_x = 1#randint(0,1)
            Ball.direction_y = randint(0,1)
            Ball.STATE = 1
        if self.y > 600:
            Ball.direction_y = 0
        if self.y < 0:
            Ball.direction_y = 1
        if self.x < 0:
            self.red_score += 1
            self.x = Ball.SAVE_POINT_X
            self.Y = Ball.SAVE_POINT_Y
            Ball.STATE = 0
        if self.x > 1000:
            self.blue_score += 1
            self.x = Ball.SAVE_POINT_X
            self.Y = Ball.SAVE_POINT_Y
            Ball.STATE = 0
        if Ball.direction_x == 1:
            self.x += 5
        elif Ball.direction_x == 0:
            self.x -= 5
        if Ball.direction_y == 1:
            self.y += 5
        elif Ball.direction_y == 0:
            self.y -= 5
        
    def inverse_direction_x(self):
        if Ball.direction_x == 1:
            Ball.direction_x = 0
        if Ball.direction_x == 0:
            Ball.direction_x = 1
            
