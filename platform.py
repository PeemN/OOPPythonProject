DIR_UP = 1
DIR_STOP = 0
DIR_DOWN = -1
PLATFORM_VELOCITY = 5


class BluePlatform:

    DIR = 0
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def controller(self, direction):
        if direction == DIR_UP:
            BluePlatform.DIR = 1 
        if direction == DIR_STOP:
            BluePlatform.DIR = 0 
        if direction == DIR_DOWN:
            BluePlatform.DIR = -1 

    def animate(self, delta):
        if self.y > 500:
            self.y = 500
        if self.y < 100:
            self.y = 100
        self.y += PLATFORM_VELOCITY*BluePlatform.DIR

class RedPlatform:

    DIR = 0
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def controller(self, direction):
        if direction == DIR_UP:
            RedPlatform.DIR = 1
        if direction == DIR_STOP:
            RedPlatform.DIR = 0 
        if direction == DIR_DOWN:
            RedPlatform.DIR = -1

    def animate(self, delta):
        if self.y > 500:
            self.y = 500
        if self.y < 100:
            self.y = 100
        self.y += PLATFORM_VELOCITY*RedPlatform.DIR

