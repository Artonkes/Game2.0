import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.Surface((40, 40))
        self.img.fill('white')
        self.rect = self.img.get_rect(center=(x, y))
        self.speed = speed

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key[pygame.K_s] and self.rect.y < 760:
            self.rect.y += self.speed
        if key[pygame.K_d] and self.rect.x < 760:
            self.rect.x += self.speed
        if key[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
