import pygame

from utilities.decorators import singleton
from utilities.typehints import InputBuffer
from config.settings import (
    WINDOW_SETUP,
    FPS,
    CAPTION,
    Action,
    action_mappings,
    InputState,
    MouseButton,
)
from baseclasses.scenemanager import SceneManager
from scenes.mainmenu import MainMenu


@singleton
class Core:
    pygame.init()
    window = pygame.display.set_mode(**WINDOW_SETUP)
    clock = pygame.time.Clock()
    icon = pygame.image.load("assets/icon.png")

    pygame.display.set_icon(icon)
    pygame.display.set_caption(CAPTION)

    last_mouse_pressed = (False, False, False)
    last_action_mapping_pressed = {
        action: action_mappings[action][0] for action in Action
    }

    def __init__(self) -> None:
        self.scene_manager = SceneManager(MainMenu)

    def run(self) -> None:
        while True:
            elapsed_time = self.clock.tick(FPS)
            dt = self.calculate_delta_time(elapsed_time)

            self.scene_manager.switched = False

            self.check_for_quit()
            input_buffer = self.get_input()

            self.scene_manager.handle_input(input_buffer)
            self.scene_manager.update(dt)
            self.scene_manager.render(self.window)

            pygame.display.flip()

    def calculate_delta_time(self, elapsed_time: int) -> float:
        return elapsed_time / 1000  # Convert to ms

    def get_input(self) -> InputBuffer:
        keys_pressed = pygame.key.get_just_pressed()
        keys_held = pygame.key.get_pressed()
        keys_released = pygame.key.get_just_released()

        action_buffer = {}
        for action in Action:
            for mapping in action_mappings.get(action):
                # Check if any alternate keys were just pressed
                if mapping == self.last_action_mapping_pressed[action]:
                    continue

                # If an alternate key was pressed, set that bind as the current bind to 'track'
                if keys_pressed[mapping]:
                    self.last_action_mapping_pressed[action] = mapping

            tracked_mapping = self.last_action_mapping_pressed[action]
            action_buffer[action] = {
                InputState.PRESSED: keys_pressed[tracked_mapping],
                InputState.HELD: keys_held[tracked_mapping],
                InputState.RELEASED: keys_released[tracked_mapping],
            }

        mouse_pressed = pygame.mouse.get_pressed()
        mouse_buffer = {}
        for button in MouseButton:
            mouse_buffer[button] = {
                InputState.PRESSED: (
                    mouse_pressed[button.value]
                    and not self.last_mouse_pressed[button.value]
                ),
                InputState.HELD: mouse_pressed[button.value],
                InputState.RELEASED: (
                    not mouse_pressed[button.value]
                    and self.last_mouse_pressed[button.value]
                ),
            }
        self.last_mouse_pressed = mouse_pressed

        return action_buffer, mouse_buffer

    def check_for_quit(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.terminate()

            # For quick development
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.terminate()

    def terminate(self) -> None:
        pygame.quit()
        raise SystemExit
