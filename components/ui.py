import pygame.freetype

pygame.freetype.init()

font = pygame.freetype.Font("assets/joystix monospace.otf", 10)
font.antialiased = False
font.fgcolor = (255, 255, 255)
font.bgcolor = (0, 0, 0)
