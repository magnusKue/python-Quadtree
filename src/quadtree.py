import pygame
import random as rng

class Quadtree:
    def __init__(
            self, 
            boundary:pygame.Rect=pygame.Rect(0,0,400,400),
            capacity:int=4
        ):
        self.bounds = boundary
        self.capacity = capacity
        self.points=[]

        self.color = (rng.randint(0,255), rng.randint(0,255), rng.randint(0,255)) # for visualization, optional

        self.tR = None
        self.bR = None
        self.tL = None
        self.bL = None
        self.isSubdivided = False

    def subdiv(self):
        childSize = pygame.Vector2(self.bounds.width/2, self.bounds.height/2)
        self.tL = Quadtree(pygame.Rect( pygame.Vector2(self.bounds.x,               self.bounds.y),                childSize), self.capacity) 
        self.bL = Quadtree(pygame.Rect( pygame.Vector2(self.bounds.x,               self.bounds.y+childSize.y),    childSize), self.capacity)
        self.tR = Quadtree(pygame.Rect( pygame.Vector2(self.bounds.x+childSize.x,   self.bounds.y),                childSize), self.capacity)
        self.bR = Quadtree(pygame.Rect( pygame.Vector2(self.bounds.x+childSize.x,   self.bounds.y+childSize.y),    childSize), self.capacity)
        self.isSubdivided = True
        for point in self.points:
            if self.tL.inBounds(point):
                self.tL.insert(point)
            elif self.tR.inBounds(point):
                self.tR.insert(point)
            elif self.bL.inBounds(point):
                self.bL.insert(point)
            elif self.bR.inBounds(point):
                self.bR.insert(point)
            else:
                print(f"point escaped: {point.x-self.bounds.x} :: {point.y-self.bounds.y}")
        self.points = []

    def insert(self, point:pygame.Vector2):
        if len(self.points) < self.capacity and not self.isSubdivided:
            self.points.append(point)
        else:
            if not self.isSubdivided:
                self.subdiv()   
            
            if self.tL.inBounds(point):
                self.tL.insert(point)
            elif self.tR.inBounds(point):
                self.tR.insert(point)
            elif self.bL.inBounds(point):
                self.bL.insert(point)
            elif self.bR.inBounds(point):
                self.bR.insert(point)
            else:
                print(f"point escaped: {point.x-self.bounds.x} :: {point.y-self.bounds.y}")


    def inBounds(self, point:pygame.Vector2): # check if point is in bounds
        return  point.x >= self.bounds.left and \
                point.x <= self.bounds.right and \
                point.y >= self.bounds.top and \
                point.y <= self.bounds.bottom
    
    def draw(self, surf, col=None): # for visualization, optional
        if col == None:
            color = self.color
        pygame.draw.rect(surf, color, self.bounds, 1)
        if self.isSubdivided:
            self.bL.draw(surf, col)
            self.bR.draw(surf, col)
            self.tL.draw(surf, col)
            self.tR.draw(surf, col)

        for point in self.points:
            pygame.draw.circle(surf, color, point, 4)

    def query(rect:pygame.Rect):
        pass
