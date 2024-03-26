from config.input import InputState, MouseButton, Action

ActionBuffer = dict[Action, dict[InputState, bool]]
MouseBuffer = dict[MouseButton, dict[InputState, bool]]
InputBuffer = tuple[ActionBuffer, MouseBuffer]
