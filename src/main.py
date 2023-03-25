import pygame
from pygame.locals import *
import quadtree as qT
import random as rng

pygame.init()

root = pygame.display.set_mode(pygame.Vector2(500,500), pygame.RESIZABLE)

running = True
qTree = qT.Quadtree(pygame.Rect(50,50,800,800), 4)
for x in range(300):
    qTree.insert(
        pygame.Vector2(
            rng.randint(0,qTree.bounds.bottomright[0]),
            rng.randint(0,qTree.bounds.bottomright[1])
        )
    )
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            qTree.insert(pygame.Vector2(pygame.mouse.get_pos()))

        elif event.type == pygame.VIDEORESIZE:
            root = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    
    qTree.draw(root)

    pygame.display.flip()
    root.fill((66,59,56))


pygame.quit()
