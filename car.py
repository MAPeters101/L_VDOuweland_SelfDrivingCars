import math
from pyglet.sprite import Sprite
from pyglet.window import key  # TODO: remove keyboard control


class Car:
    def __init__(self, image, batch):
        image.anchor_x = 25
        image.anchor_y = 25
        self.body = Sprite(image, batch=batch)
        self.body.x, self.body.y = 480, 260
        self.speed = 0.0
        self.rotation = 0.0

    def update(self, delta_time, keyboard):   # TODO: remove keyboard control
        self.speed -= 0.05  # friction
        acceleration = 0.0
        steer_position = 0.0
        if keyboard[key.UP]:
            acceleration = 1.0
        if keyboard[key.LEFT]:
            steer_position = -1.0
        elif keyboard[key.RIGHT]:
            steer_position = 1.0

        if acceleration > 0:
            self.speed += 0.1

        if self.speed < 0:
            self.speed = 0.0

        self.rotation -= steer_position * self.speed
        self.body.rotation = -self.rotation
        self.body.x += self.speed * math.cos(math.radians(self.rotation))
        self.body.y += self.speed * math.sin(math.radians(self.rotation))


