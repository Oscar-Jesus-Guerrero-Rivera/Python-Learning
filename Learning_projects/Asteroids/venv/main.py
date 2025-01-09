import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shoot import *

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group() 

    player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shoot.containers = (shots, updatable, drawable)

    # Initialize the game here
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    is_running = True
    clock = pygame.time.Clock()
    dt = 0
    player_instance = player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    asteroidfield_instance = AsteroidField()

    # Add other game logic or setup
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for thing in updatable:
            thing.update(dt)

        for thing in drawable:
            thing.draw(screen)

        for thing in asteroids:
            if thing.check_collision(player_instance) == True:
                print ("Game Over!")
                is_running = False
        
        pygame.display.flip() 
        dt = clock.tick(60)/1000
    
    

if __name__ == "__main__":
    main()
