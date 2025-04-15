from dataclasses import dataclass
from enum import IntEnum, auto
from math import atan2, degrees
import pygame


class Direction(IntEnum):
    N = 0
    NE = auto()
    E = auto()
    SE = auto()
    S = auto()
    SW = auto()
    W = auto()
    NW = auto()


def direction_from_angle(angle: float) -> Direction:
    return Direction(round((90 - angle) / 45) % 8)


def direction_from_delta(dx: float, dy: float) -> Direction:
    return direction_from_angle(degrees(atan2(-dy, dx)))


def angle_from_direction(dir: Direction) -> float:
    return 90 - dir.value * 45


@dataclass
class Motion:
    position: pygame.Vector2
    velocity: pygame.Vector2
    acceleration: pygame.Vector2

    def copy(self):
        return Motion(
            self.position.copy(),
            self.velocity.copy(),
            self.acceleration.copy()
        )

    @staticmethod
    def empty():
        return Motion(pygame.Vector2(), pygame.Vector2(), pygame.Vector2())


def motion_update(motion: Motion, dt: float) -> None:
    motion.velocity.x += motion.acceleration.x * dt
    motion.velocity.y += motion.acceleration.y * dt
    motion.position.x += motion.velocity.x * dt
    motion.position.y += motion.velocity.y * dt
