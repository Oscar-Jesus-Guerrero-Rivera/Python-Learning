import pygame
from constants import *
from circleshape import *

class Shoot(CircleShape):
    containers = None

    def __init__(self, x, y, velocity):
        super().__init__(x, y)
        self.velocity = velocity
        self.radius = SHOT_RADIUS
    
    def  check_collision(self, circle):
        return super().check_collision(circle)
    
    def draw(self, screen):
        return super().draw(screen)
    
    def update(self, dt):
        return super().update(dt)
    
    