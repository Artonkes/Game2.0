import sys
from player import *
pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
clock.tick(120)

players = Player(WIDTH/2, HEIGHT/2, 1)
while True:
    screen.fill('black')
    screen.blit(players.img, players.rect)
    players.update()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
