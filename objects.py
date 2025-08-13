import pygame

pygame.init()

class Circle: 
    def __init__(self, radius, coords): 
        # unpack coordinates
        x, y = coords
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self, surface, color): 
        pygame.draw.circle(surface, color, (self.x, self.y), self.radius)