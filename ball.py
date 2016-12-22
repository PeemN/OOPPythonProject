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
        if Ball.STATE == 0 or Ball.STATE == 2:
            Ball.direction = randint(0,1)
            Ball.STATE = 1
        if self.y > 500:
            self.y -= 5 
        if self.y < 100:
            self.y += 5
        if self.x < 0:
            self.red_score += 1
            self.x = Ball.SAVE_POINT_X
            Ball.STATE = 0
        if self.x > 1000:
            self.blue_score += 1
            self.x = Ball.SAVE_POINT_X
            Ball.STATE = 0
        if Ball.direction == 1:
            self.x += 5
        elif Ball.direction == 0:
            self.x -= 5
        
        def hit(self, other, hit_size):
            return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)
