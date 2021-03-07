import pygame
import random

# initialize game
pygame.init()

# Creating the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('./Utils/images/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('./Utils/images/player.png')
playerX = 370
playerY = 480
player_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy
enemyImg = pygame.image.load('./Utils/images/enemy.png')
enemyX = random.randint(64, 672)
enemyY = random.randint(50, 150)
enemy_change = 0.1


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game Loop
running = True
while running:

    # RGB background color
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # movement algorithm
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_change = -0.2
        if event.key == pygame.K_RIGHT:
            player_change = 0.2
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            player_change = 0

    playerX += player_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemy_change
    if enemyX >= 672:
        enemyX = 672
        enemy_change = -0.1
    elif enemyX <= 64:
        enemyX = 64
        enemy_change = 0.1

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
