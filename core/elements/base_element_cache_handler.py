import typing as ty
from abc import ABC, abstractmethod

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from core.elements.states.element_state import Displayed, ExistsInAnyState
from core.elements.element_finder_interface import IElementFinder


class BaseElementCacheHandler(ABC):
    """Allows to use cached element."""

    def __init__(self, locator: ty.Tuple[By, str], state: ty.Type[ty.Union[Displayed, ExistsInAnyState]],
                 finder: IElementFinder):
        """Initialize handler with default state and finder."""
        self._locator = locator
        self._state = state
        self.__element_finder = finder
        self.__remote_element = None

    @property
    def is_stale(self) -> bool:
        """Determine is the element stale."""
        return self.__remote_element is not None and self.is_refresh_needed()

    def is_refresh_needed(self, custom_state: ty.Callable[[WebElement], bool] = None) -> bool:
        """
        Determine is the cached element refresh needed.
        :param custom_state: Element custom state.
        :return: true if needed and false otherwise.
        """
        if self.__remote_element is None:
            return True

        state = self._state if custom_state is None else custom_state
        is_displayed = self.__remote_element.is_displayed()
        return isinstance(state, Displayed) and not is_displayed

    @abstractmethod
    def get_element(self, timeout: int = 0, custom_state: ty.Callable[[WebElement], bool] = None) -> WebElement:
        """
        Allow to get cached element.
        :param timeout: Timeout used to retrieve the element when refresh is needed.
        :param custom_state: Element custom state.
        :return: Cached element.
        """
        pass
