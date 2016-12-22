import arcade
from objectCreate import Creator
from platform import BluePlatform, RedPlatform

 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class ModelSprite(arcade.Sprite):
      def __init__(self, *args, **kwargs):
            self.model = kwargs.pop('model', None)
 
            super().__init__(*args, **kwargs)
 
      def sync_with_model(self):
            if self.model:
                  self.set_position(self.model.x, self.model.y)
 
      def draw(self):
            self.sync_with_model()
            super().draw()

class SrslyPongGameWindow(arcade.Window):
      def __init__(self, width, height):
            super().__init__(width, height)

            arcade.set_background_color(arcade.color.BLACK)

            self.creator = Creator(width, height)            

            self.bluePlatform_sprite = ModelSprite('images\BluePlatform.png',model=self.creator.bluePlatform)
            self.redPlatform_sprite = ModelSprite('images\RedPlatform.png',model=self.creator.redPlatform)
            
      def on_draw(self):
            arcade.start_render()
            self.bluePlatform_sprite.draw()
            self.redPlatform_sprite.draw()
            
      def animate(self,delta):
            self.creator.animate(delta)                  
if __name__ == '__main__':
      window = SrslyPongGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
      arcade.run()
