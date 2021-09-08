import typing as ty

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from core.elements.base_element_factory import BaseElementFactory
from core.elements.states.element_state import Displayed
from core.elements.states.element_count import ElementCount
from core.elements.base_element import BaseElement

T = ty.TypeVar('T')


class ElementFactory(BaseElementFactory):
    """Factory that creates elements."""

    def get_custom_element(self, element_supplier: ty.Callable[[ty.Tuple[By, str], str,
                                                                ty.Callable[[WebElement], bool]], T],
                           locator: ty.Tuple[By, str], name: str,
                           state: ty.Callable[[WebElement], bool] = Displayed) -> T:
        """
        Create custom element according to passed parameters.
        :param element_supplier: Delegate that defines constructor of element.
        :param locator: Locator of the target element.
        :param name: Name of the target element.
        :param state: State of the target element.
        :return: Instance of custom element.
        """
        return element_supplier(locator, name, state)

    def find_child_element(self, parent_element: BaseElement,
                           element_supplier: ty.Callable[[ty.Tuple[By, str], str,
                                                          ty.Callable[[WebElement], bool]], T],
                           child_locator: ty.Tuple[By, str], name: str = str(),
                           state: ty.Callable[[WebElement], bool] = Displayed) -> T:
        """
        Find child element by its locator relative to parent element.
        :param parent_element: Parent element.
        :param element_supplier: Callable object that defines constructor of element in case of custom element.
        :param child_locator: Locator of child element relative to its parent.
        :param name: Child element name.
        :param state: Child element state.
        :return: Instance of child element.
        """
        element_name = name if name else f"Child element of {parent_element.name}"
        locator = self._generate_absolute_child_locator(parent_element.locator, child_locator)
        return element_supplier(locator, element_name, state)

    def find_child_elements(self, parent_element: BaseElement,
                            element_supplier: ty.Callable[[ty.Tuple[By, str], str,
                                                           ty.Callable[[WebElement], bool]], T],
                            child_locator: ty.Tuple[By, str], name: str = str(),
                            state: ty.Callable[[WebElement], bool] = Displayed,
                            expected_count: ElementCount = ElementCount.ANY.value) -> ty.List[T]:
        """
        Find child element by its locator relative to parent element.
        :param parent_element: Parent element.
        :param element_supplier: Callable object that defines constructor of element in case of custom element.
        :param child_locator: Locator of child element relative to its parent.
        :param name: Child element name.
        :param state: Child element state.
        :param expected_count: Expected number of elements that have to be found (zero, more than zero, any).
        :return: Instance of child element.
        """
        elements_name = name if name else f"Child element of {parent_element.name}"
        locator = self._generate_absolute_child_locator(parent_element.locator, child_locator)
        return self.find_elements(element_supplier, locator, elements_name, state, expected_count)

    def find_elements(self, element_supplier: ty.Callable[[ty.Tuple[By, str], str, ty.Callable[[WebElement], bool]], T],
                      locator: ty.Tuple[By, str], name: str = str(), state: ty.Callable[[WebElement], bool] = Displayed,
                      expected_count: ElementCount = ElementCount.ANY.value) -> ty.List[T]:
        """
        Find list of elements by base locator.
        :param element_supplier: Callable object that defines constructor of element in case of custom element.
        :param locator: Base elements locator.
        :param name: Elements name.
        :param state: Elements state.
        :param expected_count: Expected number of elements that have to be found (zero, more than zero, any).
        :return: List of elements that found by locator.
        """
        self.__check_elements_count(locator, state, expected_count)

        web_elements = self._element_finder.find_elements(locator, state, 0)

        found_elements = []
        for element_index in range(1, len(web_elements) + 1):
            element_locator = self._generate_xpath_locator(locator, element_index)
            element_name = f"{name if name else 'element'} {element_index}"
            found_elements.append(element_supplier(element_locator, element_name, state))
        return found_elements

    def __check_elements_count(self, locator: ty.Tuple[By, str], state: ty.Callable[[WebElement], bool] = Displayed,
                               expected_count: ElementCount = ElementCount.ANY.value) -> None:
        if expected_count == ElementCount.ZERO:
            self._conditional_wait.wait_for_true(
                lambda: not any(
                    self._element_finder.find_elements(locator, state, 0)
                ),
                message=self._localization_manager.get_localized_message(
                    "loc.elements.found.but.should.not", locator, "desired"
                ),
            )
        elif expected_count == ElementCount.MORE_THAN_ZERO:
            self._conditional_wait.wait_for_true(
                lambda: any(
                    self._element_finder.find_elements(locator, state, 0)
                ),
                message=self._localization_manager.get_localized_message(
                    "loc.no.elements.found.by.locator", locator
                ),
            )
        elif expected_count == ElementCount.ANY:
            self._conditional_wait.wait_for(
                lambda: self._element_finder.find_elements(locator, state, 0) is not None
            )
        else:
            raise ValueError(f"No such expected value: {expected_count}")

    def _generate_absolute_child_locator(self, parent_locator: ty.Tuple[By, str], child_locator: ty.Tuple[By, str]) \
            -> ty.Tuple[By, str]:
        if self._is_locator_supported_for_xpath_extraction(
                parent_locator
        ) and self._is_locator_supported_for_xpath_extraction(child_locator):
            parent_locator_str = self._extract_xpath_from_locator(parent_locator)
            child_locator_str = self._extract_xpath_from_locator(child_locator)
            cropped_child_locator_str = (
                child_locator_str[1:]
                if child_locator_str.startswith(".")
                else child_locator_str
            )
            return By.XPATH, parent_locator_str + cropped_child_locator_str
        else:
            raise ValueError(
                f"Locator types {parent_locator} and {child_locator} not supported for building absolute locator"
            )

    def _generate_xpath_locator(self, base_locator: ty.Tuple[By, str], element_index: int) -> ty.Tuple[By, str]:
        if self._is_locator_supported_for_xpath_extraction(base_locator):
            return (
                By.XPATH,
                f"({self._extract_xpath_from_locator(base_locator)})[{element_index}]",
            )
        else:
            raise ValueError(
                f"Multiple elements' base_locator type {base_locator} is not supported yet"
            )

    @staticmethod
    def _is_locator_supported_for_xpath_extraction(locator: ty.Tuple[By, str]) -> bool:
        return locator[0] in [By.XPATH, By.TAG_NAME]

    @staticmethod
    def _extract_xpath_from_locator(locator: ty.Tuple[By, str]) -> str:
        locator_type = locator[0]
        locator_value = locator[1]
        locators_map = {By.XPATH: locator_value, By.TAG_NAME: f"//{locator_value}"}
        if locator_type not in locators_map:
            ValueError(
                f"Cannot define xpath from locator {locator_value}. Locator type {locator_type} is not supported yet."
            )
        return locators_map[locator_type]
