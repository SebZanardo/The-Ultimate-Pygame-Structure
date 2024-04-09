import pygame

from utilities.typehints import ActionBuffer, MouseBuffer
from config.input import InputState, MouseButton, Action
from baseclasses.scenemanager import Scene, SceneManager
from config.constants import CYAN
from config.assets import IMPOSSIBLE_SPIN_FRAMES
from components.animationplayer import AnimationPlayer

# Import the whole module of all scenes you want to switch to
import scenes.mainmenu


class Game(Scene):
    def __init__(self, scene_manager: SceneManager) -> None:
        super().__init__(scene_manager)

        self.debug_animation = AnimationPlayer("spin", IMPOSSIBLE_SPIN_FRAMES, 0.05)

    def handle_input(
        self, action_buffer: ActionBuffer, mouse_buffer: MouseBuffer
    ) -> None:
        if (
            action_buffer[Action.START][InputState.PRESSED]
            or mouse_buffer[MouseButton.LEFT][InputState.PRESSED]
        ):
            self.scene_manager.switch_scene(scenes.mainmenu.MainMenu)

    def update(self, dt: float) -> None:
        self.debug_animation.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        surface.fill(CYAN)
        surface.blit(self.debug_animation.get_frame(), (288, 148))
