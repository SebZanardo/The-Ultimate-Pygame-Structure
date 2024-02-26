from enum import Enum, auto
import pygame

# Nintendo DS Resolution
DISPLAY_WIDTH = 256
DISPLAY_HEIGHT = 192
DISPLAY_CENTER = (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2)
DISPLAY_SETUP = {
    "size": (DISPLAY_WIDTH, DISPLAY_HEIGHT),
    "flags": pygame.SCALED | pygame.RESIZABLE,
    "depth": 0,
    "display": 0,
    "vsync": 1,
}
CAPTION = "My New Pygame Project"
FPS = 60


class MouseButton(Enum):
    LEFT = 0
    MIDDLE = 1
    RIGHT = 2


class Key(Enum):  # Input map based on NES Controller
    LEFT = pygame.K_LEFT
    RIGHT = pygame.K_RIGHT
    UP = pygame.K_UP
    DOWN = pygame.K_DOWN
    A = pygame.K_z
    B = pygame.K_x
    SELECT = pygame.K_RSHIFT
    START = pygame.K_RETURN


class InputState(Enum):
    PRESSED = auto()
    HELD = auto()
    RELEASED = auto()
