import numpy as np
import math

# variables

# https://pltzltgp-5000.use2.devtunnels.ms/

# ok so i need some code here which will call all the physics functions u need on each of these objects
def update_positions(objects): 
    # in case u need the index for some reason idk
    for i, object in enumerate(objects): 
        # call necessary functions, update x and y at the end with set_coords object function
        # i just filled in some random code here to check if the objects were updating on the canvas and demo how to use get_coords and set_coords
        x, y = object.get_coords()
        x_vel, y_vel = object.get_velocity()

        area = object.get_size()
        # so down is actually up bc canvas is weird, so increasing y means down
        g = -1
        a_x = 0
        a_y = -(g)
        # the y keeps increasinge even if it hits a wall, which is what's causing them to fall thru
        
        # in bounds condition
        in_bounds = True
        # I THINK I BROKE A LOT
        # we should prob go back to what we were doing before :)
        # i have to go tho so im going to push back to the repo do u know how to clone on ur own codespace? no 
        if (object.type == "Circle"): 
            if (x - object.get_radius() < 0 or x + object.get_radius() > 500) or (y - object.get_radius() < 0 or y + object.get_radius() > 500):
                in_bounds = False
                bounce_off_walls(object)
        if in_bounds: 
            x_vel += a_x
            y_vel += a_y
            x += x_vel
            y += y_vel
    
        # set_coords method takes a tuple
        coords = (x, y)
        object.set_coords(coords)
        bounce_off_walls(object)
    return objects

# i would definitely recommend writing more functions rather than keeping everything in update_positions, bc that will just be a mess
# also pls let me know if there is anything else we need to keep track of, like maybe object area, and then if we should change the frame rate
# we may also need to have a few unit conversion functions so u aren't working with weird units like pixels which aren't really generalizable to the usual formulas
# the screen is 500 x 500 pixels, and coords are given in relation to that (for calculating like bouncing off of the edges if u want to)
# TODO: add bouncing off walls logic
# TODO: add object physics and acceleration interaction logic ig idk

#def is_touching(object,object:
 #   x1,y1 = object.get_coords()
  #  x2,y2 = object.get_coords

# :( its not bouncing
# oh this is bc the speed is just getting set once in the animator and not revised
def bounce_off_walls(object): 
    x_vel, y_vel = object.get_velocity()
    x, y = object.get_coords()
    if object.type == "Circle":
        if x - object.get_radius() < 0 or x + object.get_radius() > 500:
            object.set_velocity((-x_vel, y_vel))
        if y - object.get_radius() < 0 or y + object.get_radius() > 500:
            object.set_velocity((x_vel, -y_vel))
        
def at_wall(object): 
    x, y = object.get_coords()
    if object.type == "Circle":
        if x - object.get_radius() < 0 or x + object.get_radius() > 500:
            return True
        if y - object.get_radius() < 0 or y + object.get_radius() > 500:
            return True
    return False