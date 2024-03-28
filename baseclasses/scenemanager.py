from __future__ import annotations
from abc import ABC, abstractmethod
import pygame

from utilities.decorators import singleton
from utilities.typehints import ActionBuffer, MouseBuffer, InputBuffer


class Scene(ABC):
    def __init__(self, scene_manager: SceneManager) -> None:
        self.scene_manager = scene_manager

    @abstractmethod
    def handle_input(
        self, action_buffer: ActionBuffer, mouse_buffer: MouseBuffer
    ) -> None: ...

    @abstractmethod
    def update(self, dt: float) -> None: ...

    @abstractmethod
    def render(self, surface: pygame.Surface) -> None: ...


@singleton
class SceneManager:
    switched = False  # To ensure scene does not switch mid game loop

    def __init__(self, starting_scene: Scene) -> None:
        self.switch_scene(starting_scene)

    def switch_scene(self, new_scene: Scene) -> None:
        self.scene = new_scene(self)
        self.switched = True
        print(f"Switched to {new_scene.__name__} Scene")

    def handle_input(self, input_buffer: InputBuffer) -> None:
        if self.switched:
            return
        self.scene.handle_input(*input_buffer)

    def update(self, dt: float) -> None:
        if self.switched:
            return
        self.scene.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        if self.switched:
            return
        self.scene.render(surface)
