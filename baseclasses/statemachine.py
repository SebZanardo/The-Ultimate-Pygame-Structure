from __future__ import annotations
from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, sm: StateMachine) -> None:
        self.sm = sm

    @abstractmethod
    def enter(self) -> None: ...

    @abstractmethod
    def excecute(self) -> None: ...

    @abstractmethod
    def exit(self) -> None: ...


class StateMachine:
    def __init__(self) -> None:
        self.current_state = None

    def switch_state(self, next_state: State) -> None:
        if self.current_state is not None:
            self.current_state.exit()
        self.current_state = next_state
        self.current_state.enter()

    def excecute(self) -> None:
        self.current_state.excecute()
