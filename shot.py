import pygame
from constants import *
from circleshape import *

class Shot (CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)


    def draw(self,screen):
        pygame.draw.circle(screen, WHITE, (int(self.position.x),int(self.position.y)), int(self.radius), 2)


    def update(self, dt):
        self.position += self.velocity * dt


