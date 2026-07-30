import pygame, sys, random
from pygame.locals import QUIT

# setup stuff
pygame.init()
w = 600
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')
screen.fill((255, 255, 255))

# TODO initialize the variables
tick = 0




# the animation loop   
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # clear the screen
    screen.fill((255, 255, 255))
    
    # TODO set the position, draw
    
    
    
    pygame.display.update()
    pygame.time.delay(500)
    
    # TODO increment 'tick' 
    

