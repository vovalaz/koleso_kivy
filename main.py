import os
from kivy.app import App
from kivy.uix.widget import Widget

if os.name == 'nt':
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return PongGame()
    

if __name__ == "__main__":
    PongApp().run()