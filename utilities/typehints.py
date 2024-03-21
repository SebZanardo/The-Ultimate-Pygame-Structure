from config.settings import Key, MouseButton, InputState

KeyBuffer = dict[Key, dict[InputState, bool]]
MouseBuffer = dict[MouseButton, dict[InputState, bool]]
InputBuffer = tuple[KeyBuffer, MouseBuffer]
