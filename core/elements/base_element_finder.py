import typing as ty
from abc import ABC, abstractmethod

from injector import inject
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from core.elements.states.element_state import ElementState
from core.elements.states.desired_state import DesiredState
from core.localization.loggers.base_localized_logger import BaseLocalizedLogger
from core.waitings.conditional_wait import ConditionalWait


class BaseElementFinder(ABC):
    @inject
    def __init__(self, logger: BaseLocalizedLogger, conditional_wait: ConditionalWait):
        """Initialize finder with required dependencies."""
        self._logger = logger
        self._conditional_wait = conditional_wait

    @abstractmethod
    def find_element(self, locator: ty.Tuple[By, str], desired_state: str = ElementState.EXIST_IN_ANY_STATE.value,
                     timeout: int = 0) -> WebElement:
        """
        Find element in desired state defined by callable object.
        :param locator: element locator.
        :param desired_state: desired element state as callable object.
        :param timeout: timeout for search.
        :return: Found element.
        :raises: NoSuchElementException if element was not found in time in desired state.
        """
        pass

    @abstractmethod
    def find_elements(self, locator: ty.Tuple[By, str], desired_state: str = ElementState.EXIST_IN_ANY_STATE.value,
                      timeout: int = 0) -> ty.List[WebElement]:
        """
        Find elements in desired state defined by callable object.
        :param locator: element locator.
        :param desired_state: desired element state as callable object.
        :param timeout: timeout for search.
        :return: List of found elements.
        """
        pass

    @abstractmethod
    def find_elements_in_state(self, locator: ty.Tuple[By, str], desired_state: DesiredState,
                               timeout: int = 0) -> ty.List[WebElement]:
        """
        Find elements in desired state defined by DesiredState object.
        :param locator: element locator.
        :param desired_state: desired element state.
        :param timeout: timeout for search.
        :return: List of found elements.
        """
        pass
