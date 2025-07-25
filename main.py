import pygame
from constants import *


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game = True
    while(game == True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        color1 = (0,0,0)
        screen.fill(color1)


        pygame.display.flip()

if __name__ == "__main__":
    main()
