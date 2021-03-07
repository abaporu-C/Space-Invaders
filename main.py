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

def player():
    screen.blit(playerImg, (playerX, playerY))

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB background color
    screen.fill((178, 30, 110))
    player()
    pygame.display.update()
