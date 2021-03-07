import pygame
import random

# initialize game
pygame.init()

# Creating the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('./Utils/images/background.png')

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
enemyX_change = 2
enemyY_change = 15


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Bullet
# Ready - You cant see the bullet on the screen
# Fire - Bullet moving
bulletImg = pygame.image.load('./Utils/images/bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    # print(bullet_state)
    screen.blit(bulletImg, (x + 16, y + 10))


# Game Loop
running = True
while running:

    # RGB background color
    screen.fill((0, 0, 0))

    # Background Image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # movement algorithm
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_change = -2
        if event.key == pygame.K_RIGHT:
            player_change = 2
        if event.key == pygame.K_SPACE:
            print("space")
            fire_bullet(playerX, bulletY)
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            player_change = 0

    # Player Bound Check
    playerX += player_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    enemyX += enemyX_change
    if enemyX >= 672:
        enemyX = 672
        enemyY += enemyY_change
        enemyX_change = -2
    elif enemyX <= 64:
        enemyX = 64
        enemyY += enemyY_change
        enemyX_change = 2

    # Bullet Movement
    if bullet_state == "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
