import arcade
from objectCreate import Creator
from platform import BluePlatform, RedPlatform
from ball import Ball
 
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

            self.blue_platform_sprite = ModelSprite('images\BluePlatform.png',model=self.creator.blue_platform)
            self.red_platform_sprite = ModelSprite('images\RedPlatform.png',model=self.creator.red_platform)
            self.ball_sprite = ModelSprite('images\Ball.png',model=self.creator.ball)

            
      def on_draw(self):
            arcade.start_render()
            arcade.draw_text(str(self.creator.ScoreCount(1)), 350, 300,arcade.color.WHITE, 100)
            arcade.draw_text(str(self.creator.ScoreCount(2)), 650, 300,arcade.color.WHITE, 100)
            self.ball_sprite.draw()
            self.blue_platform_sprite.draw()
            self.red_platform_sprite.draw()
            
      def animate(self,delta):
            self.creator.animate(delta)
            
      def on_key_press(self, key, key_modifiers):
            self.creator.on_key_press(key, key_modifiers)
            
if __name__ == '__main__':
      window = SrslyPongGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
      arcade.run()
