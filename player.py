from circleshape import *
from shot import *
from constants import *


class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0




# in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    def draw(self,screen):
        pygame.draw.polygon(screen, WHITE, self.triangle(), 2)


    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.timer > 0:
            self.timer -= dt
        else:
            pass

        if keys[pygame.K_s]:
            self.rotate(-dt)
        if keys[pygame.K_f]:
            self.rotate(dt)
        if keys[pygame.K_e]:
            self.move(dt)
        if keys[pygame.K_d]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        

    def shoot(self):
        if self.timer <= 0:
            bullet = Shot(self.position.x,self.position.y)
            velocity = pygame.Vector2(0, 1).rotate(self.rotation)
            bullet.velocity = velocity * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN
        else:
            pass
