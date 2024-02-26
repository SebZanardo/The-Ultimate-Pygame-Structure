from config.settings import Key, MouseButton, InputState

RGB = tuple[int, int, int]
Vector2 = tuple[float, float]

KeyBuffer = dict[Key, dict[InputState, bool]]
MouseBuffer = dict[MouseButton, dict[InputState, bool]]
InputBuffer = tuple[KeyBuffer, MouseBuffer]
