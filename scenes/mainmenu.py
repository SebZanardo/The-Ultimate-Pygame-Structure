import pygame

from utilities.typehints import ActionBuffer, MouseBuffer
from config.input import InputState, MouseButton, Action
from baseclasses.scenemanager import Scene, SceneManager
import scenes.game


class MainMenu(Scene):
    def __init__(self, scene_manager: SceneManager) -> None:
        super().__init__(scene_manager)

    def handle_input(
        self, action_buffer: ActionBuffer, mouse_buffer: MouseBuffer
    ) -> None:
        if (
            action_buffer[Action.START][InputState.PRESSED]
            or mouse_buffer[MouseButton.LEFT][InputState.PRESSED]
        ):
            self.scene_manager.switch_scene(scenes.game.Game)

    def update(self, dt: float = 0.0) -> None:
        pass

    def render(self, surface: pygame.Surface) -> None:
        surface.fill((255, 0, 255))
