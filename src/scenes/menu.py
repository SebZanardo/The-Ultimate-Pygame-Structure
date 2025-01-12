import pygame

import core.constants as const
import core.input as input
import core.assets as assets
from components.animation import AnimationPlayer

from scenes.scene import Scene
import scenes.game


DEBUG = AnimationPlayer("spin", assets.DEBUG_FRAMES, 0.1)
DEBUG_X = const.WINDOW_CENTRE[0] - DEBUG.get_frame().get_width() // 2
DEBUG_Y = const.WINDOW_CENTRE[1] - DEBUG.get_frame().get_height() // 2


class Menu(Scene):
    def enter(self) -> None:
        DEBUG.reset()

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
            self.statemachine.change_state(scenes.game.Game)
            return

        DEBUG.update(dt)

        surface.fill(const.CYAN)
        surface.blit(DEBUG.get_frame(), (DEBUG_X, DEBUG_Y))

    def exit(self) -> None:
        pass
