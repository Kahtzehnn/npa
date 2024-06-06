import pygame

class InputLayer:
    def __init__(self, numInputs, colour): #add more params later
        self.numInputs = numInputs
        self.colour = colour
        for i in range(self.numInputs):
            pygame.draw