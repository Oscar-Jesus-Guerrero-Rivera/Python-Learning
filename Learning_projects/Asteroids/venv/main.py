import pygame
from constants import *


def main():
    print("Game is starting...")
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    # Initialize the game here
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    is_running = True
    clock = pygame.time.Clock()
    dt = 0

    # Add other game logic or setup
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.display.flip() 
        dt = clock.tick(60)/1000
    
    

if __name__ == "__main__":
    main()
