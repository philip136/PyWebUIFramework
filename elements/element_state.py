from enum import Enum


class ElementState(Enum):
    DISPLAYED = 'displayed'
    EXISTS_IN_ANY_STATE = 'exists'

    def __init__(self, state):
        self.state = state
