import pygame
from constants import *
from circleshape import *

class Shoot(CircleShape):
    containers = None

    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        self.radius = SHOT_RADIUS
    
    def  check_collision(self, circle):
        return super().check_collision(circle)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", (self.position.x, self.position.y), SHOT_RADIUS)

    
    def update(self, dt):
        self.position += self.velocity * dt

        # Remove the shot if it goes off-screen
        if (
            self.position.x < -SHOT_RADIUS
            or self.position.x > SCREEN_WIDTH + SHOT_RADIUS
            or self.position.y < -SHOT_RADIUS
            or self.position.y > SCREEN_HEIGHT + SHOT_RADIUS
        ):
            self.kill()
    
    