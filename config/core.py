import pygame

from utilities.decorators import singleton
from utilities.typehints import InputBuffer
from config.settings import DISPLAY_SETUP, FPS, CAPTION, Key, KeyState
from baseclasses.scenemanager import SceneManager
from scenes.game import Game


@singleton
class Core:
    pygame.init()
    window = pygame.display.set_mode(**DISPLAY_SETUP)
    clock = pygame.time.Clock()
    icon = pygame.image.load("assets/icon.png")

    pygame.display.set_icon(icon)
    pygame.display.set_caption(CAPTION)

    def __init__(self) -> None:
        self.scene_manager = SceneManager(Game)

    def run(self) -> None:
        while True:
            elapsed_time = self.clock.tick(FPS)
            dt = self.get_delta_time(elapsed_time)

            self.scene_manager.switched = False
            self.check_for_quit()
            input_buffer = self.get_input()

            self.scene_manager.handle_input(input_buffer)
            self.scene_manager.update(dt)
            self.scene_manager.render(self.window)

            pygame.display.flip()

    def get_delta_time(self, elapsed_time: int) -> float:
        delta = elapsed_time / 1000  # Convert to ms

        if DISPLAY_SETUP['vsync']:
            delta_buffer = 0
            delta += delta_buffer
            last_dt = delta
            delta = 1 / pygame.display.get_current_refresh_rate()
            delta_buffer = last_dt - delta

        return delta

    def get_input(self) -> InputBuffer:
        keys_pressed = pygame.key.get_just_pressed()
        keys_held = pygame.key.get_pressed()
        keys_released = pygame.key.get_just_released()

        input_buffer = {}
        for key in Key:
            input_buffer[key] = {
                KeyState.PRESSED: keys_pressed[key.value],
                KeyState.HELD: keys_held[key.value],
                KeyState.RELEASED: keys_released[key.value]
            }

        return input_buffer

    def check_for_quit(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.terminate()

    def terminate(self) -> None:
        pygame.quit()
        raise SystemExit
