import typing as ty
from abc import ABC, abstractmethod

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from core.elements.states.element_state import Displayed
from core.elements.states.element_count import ElementCount

T = ty.TypeVar('T')


class BaseParentElement(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Get name of element.
        :return: Element name.
        :rtype: str.
        """
        pass

    @property
    @abstractmethod
    def locator(self) -> ty.Tuple[By, str]:
        """Get locator of element.
        :return: Element locator.
        :rtype: str.
        """
        pass

    @abstractmethod
    def find_child_element(self, supplier: ty.Callable[[ty.Tuple[By, str], str, ty.Callable], T],
                           child_locator: ty.Tuple[By, str], name: str,
                           state: ty.Callable[[WebElement], bool] = Displayed) -> T:
        """Find child element for current element.
        :param supplier: Callable object that defines constructor of child element.
        :param child_locator: Locator of child element.
        :param name: Child element name.
        :param state: Child element state.

        :return: Instance of child element.
        :rtype: T.
        """
        pass

    @abstractmethod
    def find_child_elements(self, supplier: ty.Callable[[ty.Tuple[By, str], str, ty.Callable], T],
                            child_locator: ty.Tuple[By, str], name: str, state: ty.Callable[[WebElement], bool],
                            expected_count: ElementCount = ElementCount.ANY) -> ty.List[T]:
        """Find child elements for current element.
        :param supplier: Callable object that defines constructor of child element.
        :param child_locator: Locator of child element.
        :param name: Child element name.
        :param state: Child element state.
        :param expected_count: Expected number of elements that have to be found (zero, more than zero, any).

        :return: Instance of child element.

        :rtype: T.
        """
        pass

    @abstractmethod
    def get_element(self, timeout: int = 0) -> WebElement:
        """Get current element by specified locator.
        Default timeout is provided in TimeoutConfiguration.
        :raises: NoSuchElementException if element not found.
        :return: Instance of WebElement if found.
        :rtype: WebElement.
        """
        pass
