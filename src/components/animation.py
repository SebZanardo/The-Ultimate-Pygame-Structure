from typing import Hashable
import pygame


class AnimationPlayer:
    def __init__(
        self,
        unique_identifier: Hashable,
        frames: list[pygame.Surface],
        duration: float
    ) -> None:
        self.animations = {}
        self.state = None
        self.frame_index = 0
        self.elasped_time = 0.0
        self.frames = []
        self.frame_duration = 0.0

        self.add_animation(unique_identifier, frames, duration)
        self.switch_animation(unique_identifier)

    def update(self, dt: float) -> None:
        self.elasped_time += dt
        if self.elasped_time > self.frame_duration:
            self.frame_index += 1
            self.frame_index %= len(self.frames)
            self.elasped_time = 0.0

    def get_frame(self) -> pygame.Surface:
        return self.frames[self.frame_index]

    def add_animation(
        self,
        unique_identifier: Hashable,
        frames: list[pygame.Surface],
        duration: float
    ) -> None:
        self.animations[unique_identifier] = (frames, duration)

    def switch_animation(self, unique_identifier: Hashable) -> None:
        if self.state == unique_identifier:
            return

        self.state = unique_identifier
        self.frames = self.animations[unique_identifier][0]
        self.frame_duration = self.animations[unique_identifier][1]

        self.reset()

    def reset(self) -> None:
        self.frame_index = 0
        self.elasped_time = 0.0
