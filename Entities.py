import pygame, random
from constants import *

class Ball:
    def __init__(self) -> None:
        self.radius = 15
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.x_velocity = random.choice([-5, 5])
        self.y_velocity = random.choice([-5, 5])

    def move(self, coll = 0):
        """Move function for Ball class"""
        if coll:
            self.x_velocity = -self.x_velocity

        if self.x <= self.radius or self.x >= WIDTH - self.radius:
            self.x_velocity = -self.x_velocity
        if self. y <= self.radius or self.y >= HEIGHT - self.radius:
            self.y_velocity = -self.y_velocity

        self.x += self.x_velocity
        self.y += self.y_velocity

    def draw(self, surface):
        pygame.draw.circle(surface, (0, 255, 0), (self.x, self.y), self.radius)


class PlayerEntity:
    """Base class for all player objects"""
    def __init__(self, x, y) -> None:
        self.rect = pygame.Rect(x, y, 20, 100)
        self.color = RED
        self.speed = 5

    def move(self, *args, **kwargs):
        raise NotImplementedError("move() to be implemented in subclass")
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Player(PlayerEntity):
    def __init__(self, x, y, up, down) -> None:
        super().__init__(x, y)
        self.up = up
        self.down = down

    def move(self, keys):
        if keys[self.up] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[self.down] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

class ComputerPlayer(PlayerEntity):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    def move(self, ball: Ball):
        if ball.x_velocity < 0:
            if ball.y + random.randint(0, 50) < self.rect.centery:
                self.rect.y -= self.speed
            elif ball.y - random.randint(0, 50) > self.rect.centery:
                self.rect.y += self.speed

