DIR_UP = 1
DIR_STOP = 0
DIR_DOWN = -1
PLATFORM_VELOCITY = 5

class Platform:
    DIR = 0
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def controller(self, direction):
        if direction == DIR_UP:
            Platform.DIR = 1 
        if direction == DIR_STOP:
            Platform.DIR = 0 
        if direction == DIR_DOWN:
            Platform.DIR = -1
        return Platform.DIR

    def animate(self, delta):
        if self.y > 500:
            self.y = 500
        if self.y < 100:
            self.y = 100

class BluePlatform(Platform):

    DIR = 0
    
    def __init__(self,x,y):
        super().__init__(x, y)

    def controller(self, direction):
        BluePlatform.DIR = super().controller(direction) 

    def animate(self, delta):
        super().animate(delta)
        self.y += PLATFORM_VELOCITY*BluePlatform.DIR

class RedPlatform(Platform):

    DIR = 0
    
    def __init__(self,x,y):
        super().__init__(x, y)

    def controller(self, direction):
        RedPlatform.DIR = super().controller(direction) 

    def animate(self, delta):
        super().animate(delta)
        self.y += PLATFORM_VELOCITY*RedPlatform.DIR
