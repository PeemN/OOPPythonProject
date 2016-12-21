
TestVelocity = 5

class BluePlatform:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def animate(self, delta):
        if self.y > 600:
            self.y = 500
            TestVelocitty = 0
        if self.y < 0:
            self.y = 100
        self.y += TestVelocity

class RedPlatform:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def animate(self, delta):
        if self.y > 600:
            self.y = 500
            TestVelocitty = 0
        if self.y < 0:
            self.y = 100
        self.y -= TestVelocity

