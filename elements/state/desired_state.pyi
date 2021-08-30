class DesiredState:
    __is_except_timeout_exception: bool
    __is_except_no_such_element_exception: bool

    def __init__(self, desired_state: bool, state_name: str) -> None:
        self._desired_state = desired_state
        self._state_name = state_name

    @property
    def state_name(self) -> str:
        """Get state name for example: Clickable, Enabled and etc."""

    @property
    def is_except_timeout_exception(self) -> bool:
        """Except timeout exception or not."""

    @property
    def is_except_no_such_element_exception(self) -> bool:
        """Except no such element exception or not."""

    def get_element_state_condition(self) -> bool:
        """Get desired state."""
