import pygame
from constants import *
from player import *


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
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while(game == True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BLACK)
        player.draw(screen)



        dt = clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
