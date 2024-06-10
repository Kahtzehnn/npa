import pygame

def init():
    pygame.init()
    pygame.time.Clock.tick(20)
    screen = pygame.display.set_mode((1600, 900))
    pygame.display.set_caption("NPA")
    running = True
