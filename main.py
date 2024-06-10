import pygame
import numpy as np

pygame.init()
WIDTH, HEIGHT = 1700, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NPA")

numInputs = 50
numOutputs = 15

def setLayers():
    screen.fill((100, 100, 100))
    inputColor = (100, 100, 220)
    interColor = (180, 180, 180)
    outerColor = (240, 240, 100)
    LayerGap = 27
    inpNeuronGap = (HEIGHT - 100)//numInputs
    outNeuronGap = (HEIGHT - 100)//numOutputs

    #INPUTS
    for j in range(numInputs): #CHANGE TO number of neurons per layer
        pygame.draw.circle(screen, inputColor, (100,(10+j*inpNeuronGap)), (inpNeuronGap//2))

    #INTERNEURONS
    for i in range(50):
        for j in range(35):
            pygame.draw.circle(screen, interColor, (190 +i*LayerGap, (20 + j*25)), 8, 2)

    #OUTPUTS
    for i in range(numOutputs):
        pygame.draw.circle(screen, outerColor, (1600,(80+i*outNeuronGap)),20)





while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()

    setLayers()
    pygame.display.update()