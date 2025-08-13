import pygame
from abc import ABC, abstractmethod
import math

pygame.init()

class Object: 
    def __init__(self, coords, color): 
        # unpack and assign coordinates
        x, y = coords
        self.x = x
        self.y = y
        self.color = color
    
    def set_coords(self, new_coords): 
        x, y = new_coords
        self.x = x
        self.y = y
    
    def get_coords(self): 
        return (self.x, self.y)

    @abstractmethod
    def draw(self, surface): 
        pass

class Circle(Object): 
    def __init__(self, radius, coords, color):
        super().__init__(coords, color)
        self.radius = radius
    
    def draw(self, surface): 
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

class Square(Object): 
    def __init__(self, side, coords, color): 
        super().__init__(coords, color)
        self.side = side
    
    def draw(self, surface): 
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.side, self.side))

class Polygon(Object): 
    # circumradius = distance from center to vertices
    def __init__(self, num_sides, circumradius, center_coords, color): 
        super().__init__(center_coords, color)
        vertices = calc_vertices(center_coords, num_sides, circumradius)
        self.vertices = vertices
        self.num_sides = num_sides
        self.circumradius = circumradius
    
    def set_coords(self, new_coords): 
        x, y = new_coords
        self.x = x
        self.y = y
        self.vertices = calc_vertices(new_coords, self.num_sides, self.circumradius)
    
    def get_vertices(self): 
        return self.vertices
    
    def draw(self, surface): 
        pygame.draw.polygon(surface, self.color, self.vertices)

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
    cos_comp = circrad * math.cos((2*math.pi*vertex_num)/num_vertices)
    sin_comp = circrad * math.sin((2*math.pi*vertex_num)/num_vertices)
    x += cos_comp
    y += sin_comp
    return (x, y)