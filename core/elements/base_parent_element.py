import typing as ty
from abc import ABC, abstractmethod

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from core.elements.states.element_state import ElementState
from core.elements.states.element_count import ElementCount

T = ty.TypeVar('T')


class BaseParentElement(ABC):
    @abstractmethod
    def find_child_element(self, supplier: ty.Callable[[ty.Tuple[By, str], str, ty.Callable], T],
                           child_locator: ty.Tuple[By, str], name: str,
                           state: ty.Callable[[WebElement], bool] = ElementState.DISPLAYED) -> T:
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
