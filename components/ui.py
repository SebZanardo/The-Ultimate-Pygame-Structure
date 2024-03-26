import pygame

pygame.font.init()
font = pygame.font.Font("assets/joystix monospace.otf", 10)


def debug_text(
    string: str,
    colour: pygame.Color = (255, 255, 255),
    bgcolour: pygame.Color = (0, 0, 0),
) -> pygame.Surface:
    return font.render(string, False, colour, bgcolour)
