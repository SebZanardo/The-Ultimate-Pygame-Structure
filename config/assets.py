import sys
import platform
import pygame

from config.settings import WINDOW_SETUP, CAPTION
from utilities.spriteloading import slice_sheet

# -------------------------------- DO NOT MOVE! --------------------------------
# NOTE: Only /config/core.py should be importing window and clock
pygame.init()

if sys.platform == "emscripten":  # If running in browser
    platform.window.canvas.style.imageRendering = "pixelated"
    window = pygame.display.set_mode(WINDOW_SETUP["size"])
else:
    window = pygame.display.set_mode(**WINDOW_SETUP)

clock = pygame.time.Clock()
icon = pygame.image.load("assets/icon.png")

pygame.display.set_icon(icon)
pygame.display.set_caption(CAPTION)
# ------------------------------------------------------------------------------

# Load all sprite files (Ideally .png/.webp or .jpg for browser compatibility)
IMPOSSIBLE_SPIN_FRAMES = slice_sheet("assets/impossible_spin.png", 64, 64)

# Load all audio files (Must be .ogg file for browser compatibility)
pass

# Load all font files (Must be .ttf file for brower compatibility)
DEBUG_FONT = pygame.font.Font("assets/joystix.ttf", 10)
