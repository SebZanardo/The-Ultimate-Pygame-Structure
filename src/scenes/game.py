import pygame

import core.constants as const
import core.assets as asset
import core.input as input
from components.object import SimulatedObject

from scenes.scene import Scene
import scenes.menu


MAX_X = const.WINDOW_WIDTH - asset.DEBUG_SPRITE.get_width()
MAX_Y = const.WINDOW_HEIGHT - asset.DEBUG_SPRITE.get_height()

PIRATE = SimulatedObject(0, 0, 64, 64, 0, 0)


class Game(Scene):
    def enter(self) -> None:
        pygame.mixer.Channel(0).play(asset.DEBUG_THEME, -1)

    def execute(
        self,
        surface: pygame.Surface,
        dt: float,
        action_buffer: input.InputBuffer,
        mouse_buffer: input.InputBuffer
    ) -> None:
        if (
            action_buffer[input.Action.START] == input.InputState.PRESSED or
            mouse_buffer[input.MouseButton.LEFT] == input.InputState.PRESSED
        ):
            self.statemachine.change_state(scenes.menu.Menu)
            return

        if (
            PIRATE.vx > 0 and PIRATE.x > MAX_X or
            PIRATE.vx < 0 and PIRATE.x < 0
        ):
            PIRATE.vx *= -1

        if (
            PIRATE.vy > 0 and PIRATE.y > MAX_Y or
            PIRATE.vy < 0 and PIRATE.y < 0
        ):
            PIRATE.vy *= -1

        PIRATE.update(dt)

        surface.fill(const.MAGENTA)
        surface.blit(asset.DEBUG_SPRITE, PIRATE.get_pos())

    def exit(self) -> None:
        pygame.mixer.Channel(0).stop()
