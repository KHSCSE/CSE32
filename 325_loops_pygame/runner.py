import pygame, sys, random
from pygame.locals import QUIT
# TODO import your file



# required stuff
w = 600
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')
screen.fill((255, 255, 255))


# call your functions here



pygame.display.update()
# the animation loop  
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()