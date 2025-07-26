import pygame
from constants import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("My Awesome Asteroids Game!")
    game = True
    while(game == True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        color1 = (0,0,0)
        screen.fill(color1)


        dt = clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
