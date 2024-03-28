import pygame

from utilities.typehints import ActionBuffer, MouseBuffer
from config.input import InputState, MouseButton, Action
from baseclasses.scenemanager import Scene, SceneManager
import scenes.mainmenu
from utilities.spriteloading import slice_sheet
from components.animationplayer import AnimationPlayer


class Game(Scene):
    def __init__(self, scene_manager: SceneManager) -> None:
        super().__init__(scene_manager)

        # To test animation system, and because it looks cool :))
        debug_spin_frames = slice_sheet("assets/impossible_spin.png", 64, 64)
        self.debug_animation = AnimationPlayer("spin", debug_spin_frames, 0.05)

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
        surface.fill((0, 255, 255))
        surface.blit(self.debug_animation.get_frame(), (288, 148))
