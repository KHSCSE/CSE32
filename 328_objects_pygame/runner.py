import pygame
from bouncy import Bouncy
# from filename import Classname

# setup
w = 800
h = 600
screen = pygame.display.set_mode([w, h])
screen.fill((255, 255, 255))

# TODO create a 'Bouncy' object (then more)


# TODO create a list of 'Bouncy' objects



# stay on screen
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fill the background with white (or don't!)
    screen.fill((255, 255, 255))
    
    # TODO draw and move here
    
    
    
    # pushes the screen to the current display
    pygame.display.flip()
    
    # delay a moment
    pygame.time.delay(3)


