import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))  # Цвет врагов
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800)  # Случайное появление по горизонтали
        self.rect.y = random.randint(100, 200)  # Случайное появление по вертикали

    def update(self, speed):

        self.speed = speed
        self.rect.y += self.speed
        if self.rect.y == 800:
            self.rect.y = random.randint(100, 200)
            self.rect.x = random.randint(10, 760)
