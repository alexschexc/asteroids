from circleshape import *
from constants import *
import random
class Asteroid(CircleShape):

    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)


    def draw(self,screen):
        pygame.draw.circle(screen, WHITE, (int(self.position.x),int(self.position.y)), int(self.radius), 2)


    def update(self, dt):
        self.position += self.velocity * dt

    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
           angle = random.uniform(20,50) 
           newVel1 = self.velocity.rotate(angle)
           newVel2 = self.velocity.rotate(-angle)
           newRad = self.radius - ASTEROID_MIN_RADIUS
           newAst1 = Asteroid(self.position.x,self.position.y,newRad)
           newAst2 = Asteroid(self.position.x,self.position.y,newRad)
           finVel1 = newVel1 * 1.2
           finVel2 = newVel2 * 1.2
           newAst1.velocity = finVel1
           newAst2.velocity = finVel2

