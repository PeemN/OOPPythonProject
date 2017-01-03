import arcade
import arcade.key
from objectCreate import Creator
from platform import BluePlatform, RedPlatform
from ball import Ball,NormalBall,BlueBall,RedBall
 
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

            self.blue_platform_sprite = ModelSprite('images\blueplatform.png',model=self.creator.blue_platform)
            self.red_platform_sprite = ModelSprite('images\redplatform.png',model=self.creator.red_platform)
            
      def on_draw(self):
            if self.creator.ball.ball_type == 0:
                  self.ball_sprite = ModelSprite('images\ball.png',model=self.creator.ball)
            elif self.creator.ball.ball_type == 1:
                  self.ball_sprite = ModelSprite('images\blueball.png',model=self.creator.ball)
            elif self.creator.ball.ball_type == 2:
                  self.ball_sprite = ModelSprite('images\redball.png',model=self.creator.ball)
            if self.creator.end_state == 0:
                  arcade.start_render()
                  arcade.draw_text(str(self.creator.score_count(1)), 300, 280,arcade.color.GRAY, 100)
                  arcade.draw_text(str(self.creator.score_count(2)), 620, 280,arcade.color.GRAY, 100)
                  #arcade.draw_text(str(self.creator.hit_count), 200, 450,arcade.color.GRAY, 50)
                  self.ball_sprite.draw()
                  self.blue_platform_sprite.draw()
                  self.red_platform_sprite.draw()
            else:
                  if self.creator.score_count(1) > self.creator.score_count(2):
                        arcade.draw_text(str("Player 1 Won"), 150, 250,arcade.color.WHITE, 100)
                  elif self.creator.score_count(2) > self.creator.score_count(1):
                        arcade.draw_text(str("Player 2 Won"), 150, 250,arcade.color.WHITE, 100)
            
      def animate(self,delta):
            self.creator.animate(delta)
            
      def on_key_press(self, key, key_modifiers):
            self.creator.on_key_press(key, key_modifiers)
            
if __name__ == '__main__':
      window = SrslyPongGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
      arcade.run()
