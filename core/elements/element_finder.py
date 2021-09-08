import typing as ty

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from core.elements.states.element_state import ExistsInAnyState
from core.elements.states.desired_state import DesiredState
from core.elements.base_element_finder import BaseElementFinder


class ElementFinder(BaseElementFinder):
    def find_element(self, locator: ty.Tuple[By, str],
                     desired_state: ty.Callable[[WebElement], bool] = ExistsInAnyState,
                     timeout: int = 0) -> WebElement:
        """
        Find element in desired state defined by callable object.
        :param locator: element locator.
        :param desired_state: desired element state as callable object.
        :param timeout: timeout for search.
        :return: Found element.
        :raises: NoSuchElementException if element was not found in time in desired state.
        """
        state = DesiredState(desired_state, "desired", False, True)
        return self.find_elements_in_state(locator, state, timeout)[0]

    def find_elements(self, locator: ty.Tuple[By, str],
                      desired_state: ty.Callable[[WebElement], bool] = ExistsInAnyState,
                      timeout: int = 0) -> ty.List[WebElement]:
        """
        Find elements in desired state defined by callable object.
        :param locator: element locator.
        :param desired_state: desired element state as callable object.
        :param timeout: timeout for search.
        :return: List of found elements.
        """
        state = DesiredState(desired_state, "desired", False, True)
        return self.find_elements_in_state(locator, state, timeout)

    def find_elements_in_state(self, locator: ty.Tuple[By, str], desired_state: DesiredState,
                               timeout: int = 0) -> ty.List[WebElement]:
        """
        Find elements in desired state defined by DesiredState object.
        :param locator: element locator.
        :param desired_state: desired element state.
        :param timeout: timeout for search.
        :return: List of found elements.
        """
        elements = {"found": [], "result": []}
        try:

            def find_elements_func(driver):
                elements["found"] = driver.find_elements(*locator)
                elements["result"] = list(
                    filter(lambda elem: desired_state.element_state_condition(elem), elements["found"])
                )
                return any(elements["result"])

            self._conditional_wait.wait_for_with_driver(find_elements_func, timeout)
        except TimeoutException as exception:
            self._handle_timeout_exception(
                exception, locator, desired_state, elements["found"]
            )
        return elements["result"]

    def _handle_timeout_exception(self, exception: TimeoutException, locator: ty.Tuple[By, str],
                                  desired_state: DesiredState, found_elements: ty.List[WebElement]) -> None:
        message = f"No elements with locator '{locator}'' were found in {desired_state.state_name} state"
        if desired_state.element_state_condition:
            if not any(found_elements):
                if desired_state.raise_no_such_element_exception:
                    raise NoSuchElementException(message)
                self._logger.debug("loc.no.elements.found.in.state", str(), locator, desired_state.state_name)
            else:
                self._logger.debug("loc.elements.were.found.but.not.in.state", str(), locator, desired_state.state_name)
        else:
            message = f"{exception.msg}: {message}"
            if desired_state.raise_no_such_element_exception and not any(found_elements):
                raise NoSuchElementException(message)
            raise TimeoutException(message)
