import pygame

from utilities.typehints import KeyBuffer, MouseBuffer
from config.settings import Key, MouseButton, InputState
from baseclasses.scenemanager import Scene, SceneManager
import scenes.mainmenu


class Game(Scene):
    def __init__(self, scene_manager: SceneManager) -> None:
        super().__init__(scene_manager)

    def handle_input(self, key_buffer: KeyBuffer, mouse_buffer: MouseBuffer) -> None:
        if (
            key_buffer[Key.START][InputState.PRESSED]
            or mouse_buffer[MouseButton.LEFT][InputState.PRESSED]
        ):
            self.scene_manager.switch_scene(scenes.mainmenu.MainMenu)

    def update(self, dt: float = 0.0) -> None:
        pass

    def render(self, surface: pygame.Surface) -> None:
        surface.fill((0, 0, 0))
