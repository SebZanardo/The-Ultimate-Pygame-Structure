import sys
import platform
import pygame

import core.constants as const


pygame.init()

if sys.platform == "emscripten":  # If running in browser
    platform.window.canvas.style.imageRendering = "pixelated"
    window = pygame.display.set_mode(const.WINDOW_SETUP["size"])
else:
    window = pygame.display.set_mode(**const.WINDOW_SETUP)

clock = pygame.time.Clock()

print("Setup complete")
