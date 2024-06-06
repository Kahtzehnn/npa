import pygame

class InputLayer:
    def __init__(self, numInputs, colour): #add more params later
        self.numInputs = numInputs
        self.colour = colour
        
        
class OutputLayer:
    def __init__(self, numOutputs, colour):
        self.numOutputs = numOutputs
        self.colour = colour
        
class InterLayer:
    def __init__(self, numInputs, numOutputs, colour):
        self.numInputs = numInputs
        self.numOutputs = numOutputs
        self.colour = colour
        