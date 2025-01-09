import pygame
from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def check_collision(self, circle):
        return super().check_collision(circle)
    

    def split(self):

        if self.radius > ASTEROID_MIN_RADIUS:

            random_angle = random.uniform(20, 50)
            velocity_1 = self.velocity.rotate(random_angle) * 1.2  
            velocity_2 = self.velocity.rotate(-random_angle) * 1.2  
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = velocity_1
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2.velocity = velocity_2

            if self.containers:
                for container in self.containers:
                    container.add(asteroid_1, asteroid_2)

        self.kill()