import pygame
from constants import *
from circleshape import *
from shoot import *

class player(CircleShape):
    containers = None
    cooldown = 0
    # in the player class
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def update(self, dt):
        self.cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:  # Move forward
            self.move(dt)
        if keys[pygame.K_s]:  # Move backward
            self.rotation += 180  # Temporarily rotate 180 for backward movement
            self.move(dt)
            self.rotation -= 180  # Reset rotation
        if keys[pygame.K_a]:  # Rotate left
            self.rotation -= 200 * dt
        if keys[pygame.K_d]:  # Rotate right
            self.rotation += 200 * dt
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def check_collision(self, circle):
        return super().check_collision(circle)
    
    def shoot(self):
        if self.cooldown <= 0:
            self.cooldown = PLAYER_SHOOT_COOLDOWN
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            velocity = forward * PLAYER_SHOOT_SPEED
            Shoot(self.position.x, self.position.y, velocity)
