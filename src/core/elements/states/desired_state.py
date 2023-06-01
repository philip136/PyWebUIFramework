import typing as ty

from core.elements.states.element_state import ExistsInAnyState, Displayed


class DesiredState:
    def __init__(self, element_state_condition: ty.Type[ty.Union[Displayed, ExistsInAnyState]], state_name: str,
                 except_timeout_exception: bool = False, raise_no_such_element_exception: bool = False):
        self.__element_state_condition = element_state_condition
        self.__except_timeout_exception = except_timeout_exception
        self.__raise_no_such_element_exception = raise_no_such_element_exception
        self.__state_name = state_name

    @property
    def element_state_condition(self):
        return self.__element_state_condition

    @property
    def state_name(self):
        return self.__state_name

    @property
    def raise_no_such_element_exception(self):
        return self.__raise_no_such_element_exception

    @property
    def except_timeout_exception(self):
        return self.__except_timeout_exception
