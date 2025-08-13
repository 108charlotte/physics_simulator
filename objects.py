import pygame
from abc import ABC, abstractmethod
import math

# idk what happened to the squares and polygons but the circles are working

pygame.init()

class Object(ABC): 
    def __init__(self, coords, color, velocity): 
        # unpack and assign coordinates
        x, y = coords
        self.x = x
        self.y = y
        self.color = color
        # passed as a tuple
        self.velocity = velocity
    
    def set_coords(self, new_coords): 
        x, y = new_coords
        self.x = x
        self.y = y
    
    def get_coords(self): 
        return (self.x, self.y)
    
    def get_velocity(self): 
        return self.velocity
    
    def set_velocity(self, new_velocity): 
        self.velocity = new_velocity

    @abstractmethod
    def get_size(self): 
        pass

class Circle(Object): 
    def __init__(self, radius, coords, color, velocity):
        super().__init__(coords, color, velocity)
        self.radius = radius
        self.type = "Circle"
    
    def get_size(self): 
        return math.pi * (self.radius**2)
    
    def get_radius(self): 
        return self.radius
    
    def to_dict(self):
        return {
            'type': 'Circle',
            'x': self.x,
            'y': self.y,
            'radius': self.radius,
            'color': f"rgb({self.color[0]},{self.color[1]},{self.color[2]})"
        }

class Square(Object): 
    def __init__(self, side, coords, color, velocity): 
        super().__init__(coords, color, velocity)
        self.side = side
        self.type = "Square"
    
    def get_size(self): 
        return self.side**2

    def to_dict(self):
        return {
            'type': 'Square',
            'x': self.x,
            'y': self.y,
            'side': self.side,
            'color': f"rgb({self.color[0]},{self.color[1]},{self.color[2]})"
        }

class Polygon(Object): 
    # circumradius = distance from center to vertices
    def __init__(self, num_sides, circumradius, center_coords, color, velocity): 
        super().__init__(center_coords, color, velocity)
        vertices = calc_vertices(center_coords, num_sides, circumradius)
        self.vertices = vertices
        self.num_sides = num_sides
        self.circumradius = circumradius
        self.type = "Polygon"
    
    def set_coords(self, new_coords): 
        x, y = new_coords
        self.x = x
        self.y = y
        self.vertices = calc_vertices(new_coords, self.num_sides, self.circumradius)
    
    def get_vertices(self): 
        return self.vertices
    
    def get_size(self): 
        apothem = self.circumradius * math.cos((math.pi/self.num_sides))
        side_len = (2 * self.circumradius) / self.num_sides
        return apothem * (side_len * self.num_sides)

    def to_dict(self):
        return {
            'type': 'Polygon',
            'vertices': self.vertices,
            'color': f"rgb({self.color[0]},{self.color[1]},{self.color[2]})"
        }

def calc_vertices(center_coords, num_sides, circumradius): 
    # for the draw function later, and just to have
    vertices = []
    curr_angle = 90
    for side in range(num_sides): 
        vertices.append(calc_vertex_coord(center_coords, curr_angle, circumradius, side, num_sides))
        curr_angle += 360/num_sides
    return vertices

def calc_vertex_coord(cent_coords, curr_angle, circrad, vertex_num, num_vertices):
    x, y = cent_coords
    # calculate angle degree
    # converted to radians, hopefully this will fix the issues with it looking weird
    angle_rad = math.radians(curr_angle)
    # update x and y based on sin and cosine
    x += circrad * math.cos(angle_rad)
    y -= circrad * math.sin(angle_rad)
    return (x, y)