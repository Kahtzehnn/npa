import pygame
import numpy as np

pygame.init()
WIDTH, HEIGHT = 1700, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NEC")


inputs = np.array([0,0,0,0,0])
inters = np.array([
    [0,0,0,0,0,0,7,0,0,0], 
    [0,0,0,4,0,0,0,0,0,0], 
    [0,0,3,0,0,0,0,0,0,0]
])
outputs = np.array([0,0,0,0,0])

def setLayers():
    screen.fill((100, 100, 100))





while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()