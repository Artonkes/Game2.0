import sys
from player import *
from enemy import *

pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
clock.tick(120)

enemies = pygame.sprite.Group()

for i in range(10):  # Создаем 10 врагов
    enemy = Enemy()
    enemies.add(enemy)

players = Player(WIDTH/2, HEIGHT/2, 1)
a=0
def collide():
    global enemies,a
    for enemy in enemies:
        if players.rect.collidepoint(enemy.rect.center):
            enemy.kill()
            a+=1


if __name__ == "__main__":
    while True:
        screen.fill('black')
        screen.blit(players.img, players.rect)
        players.update()
        enemies.draw(screen)
        enemies.update(1)
        collide()
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(a)
                sys.exit()

