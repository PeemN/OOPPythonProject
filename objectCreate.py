from platform import BluePlatform,RedPlatform

class Creator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.bluePlatform = BluePlatform(25, 300)
        self.redPlatform = RedPlatform(975, 300)
 
 
    def animate(self, delta):
        self.bluePlatform.animate(delta)
        self.redPlatform.animate(delta)
