# imports
import pygame
from objects import Circle
import random

# initialize pygame
pygame.init()

# set up canvas
canvas = pygame.display.set_mode((500, 500))

# game loop (runs until quit)
running = True
while running: 
    # checks for user input
    for event in pygame.event.get(): 
        # ends event loop if game quit
        if event.type == pygame.QUIT: 
            running = False
        # adds circle with random radius at mouse click location
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            # check mouse click location
            mouse_pos = event.pos
            # assign random radius
            radius = random.randint(10, 50)
            # create circle object
            newCircle = Circle(radius, mouse_pos)
            # generate random RGB values
            red_amt = random.randint(0, 255)
            green_amt = random.randint(0, 255)
            blue_amt = random.randint(0, 255)
            # initialize circle object
            newCircle.draw(canvas, (red_amt, green_amt, blue_amt))
    # updates canvas
    pygame.display.flip()

pygame.quit()