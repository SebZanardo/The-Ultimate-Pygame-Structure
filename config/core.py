import asyncio  # For running the game in browser
import sys
import platform
import pygame

from utilities.decorators import singleton
from utilities.typehints import InputBuffer
from baseclasses.scenemanager import SceneManager
from config.settings import WINDOW_SETUP, FPS, CAPTION, action_mappings
from config.input import InputState, MouseButton, Action
from scenes.mainmenu import MainMenu


@singleton
class Core:
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

    last_mouse_pressed = (False, False, False)
    last_action_pressed = {action: False for action in Action}
    last_action_mapping_pressed = {
        action: action_mappings[action][0] for action in Action
    }

    unfocused = False

    def __init__(self) -> None:
        self.scene_manager = SceneManager(MainMenu)
        self.debug_font = pygame.font.Font("assets/joystix.ttf", 10)

    async def run(self) -> None:
        while True:
            elapsed_time = self.clock.tick(FPS)
            dt = elapsed_time / 1000.0  # Convert to seconds

            self.scene_manager.switched = False

            self.check_for_window_events()
            input_buffer = self.get_input()

            self.scene_manager.handle_input(input_buffer)
            self.scene_manager.update(dt)
            self.scene_manager.render(self.window)

            # For easy performance testing
            fps_debug = self.debug_font.render(
                f"FPS {self.clock.get_fps():.0f}", False, (255, 255, 255), (0, 0, 0)
            )
            dt_debug = self.debug_font.render(
                f"DT {dt}", False, (255, 255, 255), (0, 0, 0)
            )
            self.window.blit(fps_debug, (0, 0))
            self.window.blit(dt_debug, (0, 10))

            pygame.display.flip()
            await asyncio.sleep(0)

    def get_input(self) -> InputBuffer:
        # pygame.key.get_just_pressed() and get_just_released() aren't recognized by browser yet :(
        keys_held = pygame.key.get_pressed()

        action_buffer = {}
        for action in Action:
            for mapping in action_mappings.get(action):
                # Check if any alternate keys were just pressed
                if mapping == self.last_action_mapping_pressed[action]:
                    continue

                # If an alternate key was pressed, set that bind as the current bind to 'track'
                if keys_held[mapping]:
                    self.last_action_mapping_pressed[action] = mapping

            tracked_mapping = self.last_action_mapping_pressed[action]
            action_buffer[action] = {
                InputState.PRESSED: keys_held[tracked_mapping]
                and not self.last_action_pressed[action],
                InputState.HELD: keys_held[tracked_mapping],
                InputState.RELEASED: not keys_held[tracked_mapping]
                and self.last_action_pressed[action],
            }
            self.last_action_pressed[action] = keys_held[tracked_mapping]

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

    def check_for_window_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.terminate()

            # Can use these events to pause audio tracks or whatever else you need
            elif event.type == pygame.WINDOWFOCUSLOST:
                pass
            elif event.type == pygame.WINDOWFOCUSGAINED:
                pass
            elif event.type == pygame.VIDEORESIZE:
                pass

            # HACK: For quick development
            # NOTE: It overrides exitting fullscreen when in browser
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.terminate()

    def terminate(self) -> None:
        pygame.quit()
        raise SystemExit
