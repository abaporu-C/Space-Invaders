import pygame

#initialize game
pygame.init()

#Creating the screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Space Invaders", "./Utils/logo/ufo.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False