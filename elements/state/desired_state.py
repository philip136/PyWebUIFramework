class DesiredState:
    __is_except_timeout_exception = False
    __is_except_no_such_element_exception = False

    def __init__(self, desired_state, state_name):
        self._desired_state = desired_state
        self._state_name = state_name

    @property
    def desired_state(self):
        return self._desired_state

    @property
    def state_name(self):
        return self._state_name

    @property
    def is_except_timeout_exception(self):
        return self.__is_except_timeout_exception

    @property
    def is_except_no_such_element_exception(self):
        return self.__is_except_no_such_element_exception

    def get_element_state_condition(self):
        return self._desired_state

    def with_except_timeout_exception(self):
        self.__is_except_timeout_exception = True
        return self

    def with_except_no_such_element_exceptions(self):
        self.__is_except_no_such_element_exception = True
        return self

