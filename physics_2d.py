import numpy as np
import math

# sry abt that didn't mean to delete this

# https://pltzltgp-5000.use2.devtunnels.ms/

# ok so i need some code here which will call all the physics functions u need on each of these objects
def update_positions(objects): 
    # in case u need the index for some reason idk
    for i, object in enumerate(objects): 
        # call necessary functions, update x and y at the end with set_coords object function
        # i just filled in some random code here to check if the objects were updating on the canvas and demo how to use get_coords and set_coords
        x, y = object.get_coords()
        x_vel, y_vel = object.get_velocity()


        x -= x_vel
        y -= y_vel
        # set_coords method takes a tuple
        coords = (x, y)
        object.set_coords(coords)
    return objects

# i would definitely recommend writing more functions rather than keeping everything in update_positions, bc that will just be a mess
# also pls let me know if there is anything else we need to keep track of, like maybe object area, and then if we should change the frame rate
# we may also need to have a few unit conversion functions so u aren't working with weird units like pixels which aren't really generalizable to the usual formulas
# the screen is 500 x 500 pixels, and coords are given in relation to that (for calculating like bouncing off of the edges if u want to)
# pls add some bouncing off walls logic so i can test my reset button! 