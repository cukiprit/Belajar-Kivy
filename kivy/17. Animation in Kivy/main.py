from kivy.app import App
from kivy.clock import Clock
from kivy.core import window
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import ListProperty
from random import random

class Root(Widget):
    pass

class ClockRect(Widget):
    velocity = ListProperty([10, 15])

    def __init__(self, **kwargs):
        super(ClockRect, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1/60.)
    
    def update(self, *args):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
 
        if self.x < 0 or (self.x + self.width) > Window.width:
            self.velocity[0] *= -1
        if self.y < 0 or (self.y + self.height) > Window.height:
            self.velocity[1] *= -1

class AnimRect(Widget):
    def animation_to_random_position(self):
        Animation.cancel_all(self)
        random_x = random() * (Window.width - self.width)
        random_y = random() * (Window.height - self.height)

        animation = Animation(
            x = random_x,
            y = random_y,
            duration = 4,
            t = 'out_elastic'
        )
        animation.start(self)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.animation_to_random_position()

class AnimationApp(App):
    def build(self):
        return Root()

AnimationApp().run()