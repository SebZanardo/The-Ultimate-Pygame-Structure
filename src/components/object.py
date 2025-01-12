from dataclasses import dataclass


@dataclass
class SimulatedObject:
    x: float
    y: float
    vx: float
    vy: float
    ax: float
    ay: float

    def update(self, dt: float) -> None:
        self.vx += self.ax * dt
        self.vy += self.ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt

    def get_pos(self) -> tuple[float, float]:
        return (self.x, self.y)
