import arcade
from objectCreate import Creator
from platform import BluePlatform, RedPlatform

 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
 
class SrslyPongGame(arcade.Window):
      def __init__(self, width, height):
            super().__init__(width, height)

            arcade.set_background_color(arcade.color.BLACK)

            self.bluePlatform_sprite = arcade.Sprite('images\BluePlatform.png')
            self.redPlatform_sprite = arcade.Sprite('images\RedPlatform.png')
            
            self.creator = Creator(width, height) 
            #self.bluePlatform = BluePlatform(25, 300)
            #self.redPlatform = RedPlatform(975, 300)

      def on_draw(self):
            arcade.start_render()
            self.bluePlatform_sprite.draw()
            self.redPlatform_sprite.draw()
            
      def animate(self,delta):
            #bluePlatform = self.bluePlatform
            #redPlatform = self.redPlatform
            #bluePlatform.animate(delta)
            #redPlatform.animate(delta)
            self.creator.animate(delta)
            self.bluePlatform_sprite.set_position(self.creator.bluePlatform.x, self.creator.bluePlatform.y)
            self.redPlatform_sprite.set_position(self.creator.redPlatform.x, self.creator.redPlatform.y)

                  
if __name__ == '__main__':
      window = SrslyPongGame(SCREEN_WIDTH, SCREEN_HEIGHT)
      arcade.run()
