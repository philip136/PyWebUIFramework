import typing as ty

from selenium.webdriver.remote.webelement import WebElement
from src.core.elements.states.desired_state import DesiredState
from src.core.elements.states.element_state import Displayed, ExistsInAnyState
from src.core.elements.states.base_element_state_provider import BaseElementStateProvider


class ElementStateProvider(BaseElementStateProvider):
    @property
    def is_clickable(self) -> bool:
        return self.__is_element_clickable(0, True)

    def wait_for_displayed(self, timeout: int = 0) -> bool:
        return self.__is_any_element_found(timeout, Displayed())

    def wait_for_not_displayed(self, timeout: int = 0) -> bool:
        return self._conditional_wait.wait_for(lambda: not self.is_displayed, timeout)

    def wait_for_exist(self, timeout: int = 0) -> bool:
        return self.__is_any_element_found(timeout, ExistsInAnyState())

    def wait_for_not_exist(self, timeout: int = 0) -> bool:
        return self._conditional_wait.wait_for(lambda: not self.is_exist, timeout)

    def wait_for_enabled(self, timeout: int = 0) -> bool:
        return self.__is_element_in_desired_condition(timeout, lambda element: bool(element.is_enabled()), "ENABLED")

    def wait_for_not_enabled(self, timeout: int = 0) -> bool:
        return self.__is_element_in_desired_condition(
            timeout, lambda element: not bool(element.is_enabled()), 'NOT ENABLED')

    def wait_for_clickable(self, timeout: int = 0) -> None:
        self.__is_element_clickable(timeout, False)

    def __is_element_clickable(self, timeout: int, except_timeout_exception: bool) -> bool:
        desired_state = DesiredState(lambda element: element.is_displayed() and element.is_enabled(),
                                     'CLICKABLE', except_timeout_exception)
        return self.__is_element_in_desired_state(timeout, desired_state)

    def __is_element_in_desired_condition(self, timeout: int, desired_condition: ty.Callable[[WebElement], bool],
                                          state_name: str) -> bool:
        desired_state = DesiredState(desired_condition, state_name, True, True)
        return self.__is_element_in_desired_state(timeout, desired_state)

    def __is_element_in_desired_state(self, timeout: int, desired_state: DesiredState) -> bool:
        found_elements = self._element_finder.find_elements_in_state(self._element_locator, desired_state, timeout)
        return any(found_elements)

    def __is_any_element_found(self, timeout: int, state: ty.Callable[[WebElement], bool]) -> bool:
        found_elements = self._element_finder.find_elements(self._element_locator, state, timeout)
        return any(found_elements)
