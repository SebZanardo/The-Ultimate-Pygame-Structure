from config.settings import Action, MouseButton, InputState

ActionBuffer = dict[Action, dict[InputState, bool]]
MouseBuffer = dict[MouseButton, dict[InputState, bool]]
InputBuffer = tuple[ActionBuffer, MouseBuffer]
