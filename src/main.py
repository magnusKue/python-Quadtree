import pygame
from pygame.locals import *
import quadtree as qT
import random as rng

pygame.init()

root = pygame.display.set_mode(pygame.Vector2(500,500), pygame.RESIZABLE)

running = True

pos = 0
qTree = qT.Quadtree(pygame.Rect(50,50,800,800), 4)
[
    qTree.insert(
        pygame.Vector2(
            rng.randint(0,qTree.bounds.bottomright[0]),
            rng.randint(0,qTree.bounds.bottomright[1])
        )
    ) for I in range(0)
]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif pygame.mouse.get_pressed(3)[0]:
            qTree.insert(pygame.Vector2(pygame.mouse.get_pos()))

        elif event.type == pygame.VIDEORESIZE:
            root = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    
    qTree.draw(root)

    pygame.display.flip()
    root.fill((66,59,56))


pygame.quit()
