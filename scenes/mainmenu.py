import pygame

from utilities.typehints import InputBuffer
from config.settings import Key, KeyState
from baseclasses.scenemanager import Scene, SceneManager
import scenes.game


class MainMenu(Scene):
    def __init__(self, scene_manager: SceneManager) -> None:
        super().__init__(scene_manager)

    def handle_input(self, input_buffer: InputBuffer) -> None:
        if input_buffer[Key.START][KeyState.PRESSED]:
            self.scene_manager.switch_scene(scenes.game.Game)

    def update(self, dt: float = 0.0) -> None:
        pass

    def render(self, surface: pygame.Surface) -> None:
        surface.fill((255, 0, 255))
