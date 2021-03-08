import pygame
from pygame import mixer as mx
import random
import math

# initialize game
pygame.init()

# Creating the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('./Utils/images/background.png')

# Background Music
mx.music.load("./Utils/sounds/background.wav")
mx.music.play(-1)

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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for num in range(num_of_enemies):
    enemyImg.append(pygame.image.load('./Utils/images/enemy.png'))
    enemyX.append(random.randint(64, 672))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    enemyY_change.append(15)


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


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
    screen.blit(bulletImg, (x + 16, y + 10))


# Collision handler
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow((enemyX - bulletX), 2) + math.pow((enemyY - bulletY), 2))
    if distance < 27:
        return True
    else:
        return False


# Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10


def showScore(x, y):
    score_screen = font.render("Score: " + str(score), True, (255, 255, 255), (0, 0, 0))
    screen.blit(score_screen, (x, y))


# Game over handler
over_font = pygame.font.Font('freesansbold.ttf', 70)


def gameover():
    over_screen = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_screen, (200, 250))

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
                if bullet_state == "ready":
                    # Bullet sound
                    bullet_sound = mx.Sound("./Utils/sounds/laser.wav")
                    bullet_sound.play()
                    # Bullet Shoot
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

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
    for i in range(num_of_enemies):

        # Game over
        if enemyY[i] > 200:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            gameover()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] >= 672:
            enemyX[i] = 672
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = -2
        elif enemyX[i] <= 64:
            enemyX[i] = 64
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = 2

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            # Collision sound
            collision_sound = mx.Sound("./Utils/sounds/explosion.wav")
            collision_sound.play()
            # Collision handler
            bulletY = 480
            bullet_state = "ready"
            score += 100
            enemyX[i] = random.randint(64, 672)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    showScore(textX, textY)
    pygame.display.update()
