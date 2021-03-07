import pygame

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
            playerX = -0.1
        if event.key == pygame.K_RIGHT:
            player_change = 0.1
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            player_change = 0
    playerX += player_change
    player(playerX, playerY)
    pygame.display.update()
