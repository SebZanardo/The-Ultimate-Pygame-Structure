def clamp(
    value: int | float,
    minimum: int | float,
    maximum: int | float
) -> int | float:
    return min(max(value, minimum), maximum)


def lerp(
    a: int | float,
    b: int | float,
    t: int | float
) -> int | float:
    return a * (1 - t) + b * t
