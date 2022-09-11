import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.label import Label


import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

class Myapp(App):
    def build(self):
        return Label(text="Hello i am Fury")

if __name__ == "__main__":
    Myapp().run()