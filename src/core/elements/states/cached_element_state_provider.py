import typing as ty

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from core.elements.element_finder_interface import IElementFinder
from core.elements.states.element_state import ExistsInAnyState
from core.waitings.interfaces.conditional_wait_interface import IConditionalWait
from core.elements.base_element_cache_handler import BaseElementCacheHandler
from core.elements.states.base_element_state_provider import BaseElementStateProvider


class CachedElementStateProvider(BaseElementStateProvider):
    def __init__(self, element_locator: ty.Tuple[By, str], conditional_wait: IConditionalWait,
                 element_finder: IElementFinder, element_cache_handler: BaseElementCacheHandler):
        super(CachedElementStateProvider, self).__init__(element_locator, conditional_wait, element_finder)
        self.__element_cache_handler = element_cache_handler

    @property
    def is_displayed(self) -> bool:
        """
        Get element's displayed state.
        :return: true if displayed and false otherwise.
        """
        return not self.__element_cache_handler.is_stale and self._try_invoke_function(
            lambda element: bool(element.is_displayed()))

    @property
    def is_exist(self) -> bool:
        """
        Get element's exist state.
        :return: true if element exists in DOM (without visibility check) and false otherwise.
        """
        return not self.__element_cache_handler.is_stale and self._try_invoke_function(
            lambda element: True
        )

    @property
    def is_enabled(self) -> bool:
        """
        Get element's Enabled state, which means element is Enabled and does not have "disabled" class.
        :return: true if enabled, false otherwise.
        """
        return self._try_invoke_function(
            lambda element: bool(element.is_enabled()), [StaleElementReferenceException]
        )

    @property
    def is_clickable(self) -> bool:
        """
        Get element's clickable state, which means element is displayed and enabled.
        :return: true if element is clickable, false otherwise.
        """
        return self._try_invoke_function(
            lambda element: bool(element.is_displayed()) and bool(element.is_enabled())
        )

    def wait_for_displayed(self, timeout: int = 0) -> bool:
        """
        Wait for element is displayed on the page.
        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: true if element displayed after waiting, false otherwise.
        """
        return self._wait_for_condition(
            lambda: self._try_invoke_function(
                lambda element: bool(element.is_displayed())
            ),
            timeout,
        )

    def wait_for_not_displayed(self, timeout: int = 0) -> bool:
        """
        Wait for element is not displayed on the page.
        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: true if element is not displayed after waiting, false otherwise.
        """
        return self._wait_for_condition(lambda: not self.is_displayed, timeout)

    def wait_for_exist(self, timeout: int = 0) -> bool:
        """
        Wait for element exists in DOM (without visibility check).
        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: true if element exist after waiting, false otherwise.
        """
        return self._wait_for_condition(
            lambda: self._try_invoke_function(lambda element: True), timeout
        )

    def wait_for_not_exist(self, timeout: int = 0) -> bool:
        """
        Wait for element does not exist in DOM (without visibility check).
        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: true if element does not exist after waiting, false otherwise.
        """
        return self._wait_for_condition(lambda: not self.is_exist, timeout)

    def wait_for_enabled(self, timeout: int = 0) -> bool:
        """
        Wait for element has enabled state which means element is Enabled and does not have "disabled" class.
        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: True if enabled, false otherwise.
        :raises: NoSuchElementException when timeout exceeded and element not found.
        """
        return self._wait_for_condition(lambda: self.is_enabled, timeout)

    def wait_for_not_enabled(self, timeout: int = 0) -> bool:
        """
        Wait for element does not have enabled state which means element is not Enabled or does have "disabled" class.
        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: True if not enabled, false otherwise.
        :raises: NoSuchElementException when timeout exceeded and element not found.
        """
        return self._wait_for_condition(lambda: not self.is_enabled, timeout)

    def wait_for_clickable(self, timeout: int = 0) -> None:
        """
        Wait for element to become clickable which means element is displayed and enabled.
        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :raises: WebDriverTimeoutException when timeout exceeded and element is not clickable.
        """
        return self._conditional_wait.wait_for_true(lambda: self.is_clickable, timeout)

    def _try_invoke_function(self, func: ty.Callable[[WebElement], bool],
                             exceptions_to_handle: ty.List[ty.Type[Exception]] = [],) -> bool:
        handled_exceptions = (
            exceptions_to_handle
            if any(exceptions_to_handle)
            else self._handled_exceptions
        )
        try:
            return func(
                self.__element_cache_handler.get_element(0, ExistsInAnyState)
            )
        except Exception as exception:
            if any(
                    isinstance(exception, handled_exception)
                    for handled_exception in handled_exceptions
            ):
                return False
            raise

    @property
    def _handled_exceptions(self) -> ty.List[ty.Type[Exception]]:
        return [StaleElementReferenceException, NoSuchElementException]

    def _wait_for_condition(self, condition: ty.Callable[..., bool], timeout: int) -> bool:
        return self._conditional_wait.wait_for(condition, timeout)
