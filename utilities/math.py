def clamp(value: float, minimum: float, maximum: float) -> float:
    return min(max(value, minimum), maximum)


def lerp(a: float, b: float, t: float) -> float:
    return a * (1 - t) + b * t
