import pygame
import numpy as np

pygame.init()
WIDTH, HEIGHT = 1700, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NPA")

def setLayers():
    screen.fill((100, 100, 100))
    inputColor = (220, 220, 100)
    interColor = (180, 180, 180)
    LayerGap = 80
    NeuronGap = WIDTH//10 #CHANGE TO number of neurons per layer

    #INPUTS
    for j in range(10): #CHANGE TO number of neurons per layer
        pygame.draw.circle(screen, inputColor, (100+LayerGap,(NeuronGap+j*NeuronGap)),10)

    #INTERNEURONS
    for i in range(10):
        for j in range(5):
            pygame.draw.circle(screen, interColor, (300 +i*40, (50 + j*40)), 6, 3)

    #OUTPUTS
    for i in range(10):
        pygame.draw.circle(screen, interColor, (300 +i*40, (50 + i*40)), 15, 4)





while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()

    setLayers()
    pygame.display.update()