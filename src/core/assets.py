import pygame

from utilities.sprite import slice_sheet


# Load sprites (png, webp or jpg for web compatibility)
ICON = pygame.image.load("assets/icon.png")
DEBUG_SPRITE = pygame.image.load("assets/img/dvd_logo.png")
DEBUG_FRAMES = slice_sheet("assets/img/impossible_spin.png", 64, 64)

# Load audio (ogg for web compatibility)
DEBUG_THEME = pygame.mixer.Sound("assets/sfx/theme.ogg")

# Load fonts (ttf for web compatibility)
DEBUG_FONT = pygame.font.Font("assets/joystix.ttf", 10)

print("Loaded assets")
