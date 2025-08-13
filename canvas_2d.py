# imports
import pygame
from objects import Circle, Square
import random
import importlib
from physics_2d import update_positions

# initialize pygame
pygame.init()

# import physics
physics_module = importlib.import_module("physics_2d")

# set up canvas
canvas = pygame.display.set_mode((500, 500))

# keep track of objects so that they can be used in physics sim
objects = []

# set up frame rate with clock
clock = pygame.time.Clock()

# game loop (runs until quit)
running = True
while running: 
    # resets canvas
    canvas.fill((255, 255, 255))

    for object in objects: 
        object.draw(canvas)

    # updates existing objects based on physics calculations
    update_positions(objects)

    # checks for user input (after physics so that when the user clicks the object actually appears where they clicked)
    for event in pygame.event.get(): 
        # ends event loop if game quit
        if event.type == pygame.QUIT: 
            running = False
        # adds circle with random radius at mouse click location
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            # check mouse click location
            mouse_pos = event.pos
            # generate random RGB values
            red_amt = random.randint(0, 255)
            green_amt = random.randint(0, 255)
            blue_amt = random.randint(0, 255)
            color = (red_amt, green_amt, blue_amt)
            # generate random object type
            object_type_num = random.randint(1, 2)
            # circle
            if object_type_num == 1: 
                # assign random radius
                radius = random.randint(10, 50)
                # create circle object and add to objects list
                newCircle = Circle(radius, mouse_pos, color)
                objects.append(newCircle)
                # add new circle object to canvas
                newCircle.draw(canvas)
            # square
            elif object_type_num == 2: 
                # assign random side length
                side = random.randint(10, 50)
                # update coords for mouse position so that they are for center of square
                x, y = mouse_pos
                x -= side/2
                y -= side/2
                mouse_pos = (x, y)
                # create square object and add to objects list
                newSquare = Square(side, mouse_pos, color)
                objects.append(newSquare)
                # add new square object to canvas
                newSquare.draw(canvas)
    # updates canvas
    pygame.display.flip()
    clock.tick(60)

pygame.quit()