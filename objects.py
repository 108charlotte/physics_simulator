import pygame

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