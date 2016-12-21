import arcade
 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
 
class SrslyPongGame(arcade.Window):
      def __init__(self, width, height):
            super().__init__(width, height)

            arcade.set_background_color(arcade.color.BLACK)

            self.bluePlatform = arcade.Sprite('images\BluePlatform.png')
            self.bluePlatform.set_position(25, 400)

      def on_draw(self):
            arcade.start_render()
            self.bluePlatform.draw()


if __name__ == '__main__':
      window = SrslyPongGame(SCREEN_WIDTH, SCREEN_HEIGHT)
      arcade.run()
