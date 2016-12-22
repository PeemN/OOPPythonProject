from random import randint
from platform import BluePlatform, RedPlatform

class Ball:

    SAVE_POINT_X = 0
    SAVE_POINT_Y = 0
    STATE = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.red_score = 0
        self.blue_score = 0
        self.to_normal = 0
        self.state = Ball.STATE
        Ball.SAVE_POINT_X = x
        Ball.SAVE_POINT_Y = y
        
    def animate(self, delta):
        if Ball.STATE == 0:
            Ball.direction_x = randint(0,1)
            Ball.direction_y = randint(0,1)
            Ball.STATE = 1
        if self.y > 600:
            Ball.direction_y = 0
        if self.y < 0:
            Ball.direction_y = 1
        if Ball.direction_x == 1:
            self.x += 5
        elif Ball.direction_x == 0:
            self.x -= 5
        if Ball.direction_y == 1:
            self.y += 5
        elif Ball.direction_y == 0:
            self.y -= 5
        
    def inverse_direction_x(self, player):
        if player == 1:
            Ball.direction_x = 1
        elif player == 2:
            Ball.direction_x = 0

    def trans_back(self):
        self.to_normal = 1
        return self.to_normal

class NormalBall(Ball):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ball_type = 0
        
    def animate(self, delta):
        super().animate(delta)
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

    def inverse_direction_x(self, player):
        super().inverse_direction_x(player)

class BlueBall(Ball):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ball_type = 1
        
    def animate(self, delta):
        super().animate(delta)
        if self.x < 0:
            self.blue_score += 1
            self.x = Ball.SAVE_POINT_X
            self.Y = Ball.SAVE_POINT_Y
            Ball.to_normal = 0
            super().trans_back()
            Ball.STATE = 0
        if self.x > 1000:
            self.x = Ball.SAVE_POINT_X
            self.Y = Ball.SAVE_POINT_Y
            Ball.to_normal = 0
            super().trans_back()
            Ball.STATE = 0

    def inverse_direction_x(self, player):
        super().inverse_direction_x(player)

class RedBall(Ball):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ball_type = 2
        
    def animate(self, delta):
        super().animate(delta)
        if self.x < 0:
            self.x = Ball.SAVE_POINT_X
            self.Y = Ball.SAVE_POINT_Y
            Ball.to_normal = 0
            super().trans_back()
            Ball.STATE = 0
        if self.x > 1000:
            self.red_score += 1
            self.x = Ball.SAVE_POINT_X
            self.Y = Ball.SAVE_POINT_Y
            Ball.to_normal = 0
            super().trans_back()
            Ball.STATE = 0

    def inverse_direction_x(self, player):
        super().inverse_direction_x(player)
