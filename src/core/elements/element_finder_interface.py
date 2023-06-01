import typing as ty
from abc import ABC, abstractmethod

from injector import inject
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from src.core.elements.states.element_state import ExistsInAnyState, Displayed
from src.core.elements.states.desired_state import DesiredState
from src.core.localization.loggers.interfaces.localized_logger_interface import ILocalizedLogger
from src.core.waitings.conditional_wait import ConditionalWait


class IElementFinder(ABC):
    @inject
    def __init__(self, logger: ILocalizedLogger, conditional_wait: ConditionalWait):
        """Initialize finder with required dependencies."""
        self._logger = logger
        self._conditional_wait = conditional_wait

    @abstractmethod
    def find_element(self, locator: ty.Tuple[By, str],
                     state: ty.Type[ty.Union[Displayed, ExistsInAnyState]] = ExistsInAnyState(),
                     timeout: int = 0) -> WebElement:
        """
        Find element in desired state defined by callable object.
        :param locator: Element locator.
        :param state: Element state as callable object.
        :param timeout: Timeout for search.
        :raises: NoSuchElementException if element was not found in time in desired state.
        :return: Found element.
        :rtype: WebElement.
        """
        pass

    @abstractmethod
    def find_elements(self, locator: ty.Tuple[By, str],
                      state: ty.Type[ty.Union[Displayed, ExistsInAnyState]] = ExistsInAnyState,
                      timeout: int = 0) -> ty.List[WebElement]:
        """
        Find elements in desired state defined by callable object.
        :param locator: Element locator.
        :param state: Desired element state as callable object.
        :param timeout: Timeout for search.
        :return: List of found elements.
        :rtype: ty.List[WebElement].
        """
        pass

    @abstractmethod
    def find_elements_in_state(self, locator: ty.Tuple[By, str], desired_state: DesiredState,
                               timeout: int = 0) -> ty.List[WebElement]:
        """
        Find elements in desired state defined by DesiredState object.
        :param locator: Element locator.
        :param desired_state: Desired element state.
        :param timeout: timeout for search.
        :return: List of found elements.
        :rtype: ty.List[WebElement].
        """
        pass
