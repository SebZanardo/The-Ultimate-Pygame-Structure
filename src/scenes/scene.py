import pygame
from abc import abstractmethod

from components.statemachine import State
import core.input as input


class Scene(State):
    @abstractmethod
    def enter(self) -> None: ...

    @abstractmethod
    def execute(
        self,
        surface: pygame.Surface,
        dt: float,
        action_buffer: input.InputBuffer,
        mouse_buffer: input.InputBuffer
    ) -> None: ...

    @abstractmethod
    def exit(self) -> None: ...
