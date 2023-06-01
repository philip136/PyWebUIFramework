import typing as ty
from abc import ABC, abstractmethod

from injector import inject
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from src.core.elements.states.element_state import Displayed
from src.core.elements.states.element_count import ElementCount
from src.core.elements.element_finder_interface import IElementFinder
from src.core.waitings.interfaces.conditional_wait_interface import IConditionalWait
from src.core.localization.managers.interfaces.localization_interface import ILocalizationManager
from src.core.localization.loggers.interfaces.localized_logger_interface import ILocalizedLogger
from src.core.applications.interfaces.application_interface import IApplication
from src.core.utilities.interfaces.action_repeater_interface import IActionRepeater
from src.core.configurations.element_cache_configuration import ElementCacheConfiguration

T = ty.TypeVar('T')


class BaseElementFactory(ABC):
    @inject
    def __init__(self, conditional_wait: IConditionalWait, element_finder: IElementFinder,
                 localization_manager: ILocalizationManager, application: IApplication,
                 action_repeater: IActionRepeater, cache_configuration: ElementCacheConfiguration,
                 localized_logger: ILocalizedLogger):
        """Initialize factory with required dependencies."""
        self._conditional_wait = conditional_wait
        self._element_finder = element_finder
        self._localization_manager = localization_manager
        self._application = application
        self._action_repeater = action_repeater
        self._cache_configuration = cache_configuration
        self._localized_logger = localized_logger

    @abstractmethod
    def get_custom_element(self, element_supplier: ty.Callable[[ty.Tuple[By, str], str, str], T],
                           locator: ty.Tuple[By, str], name: str,
                           state: ty.Callable[[WebElement], bool] = Displayed) -> T:
        """
        Create custom element according to passed parameters.
        :param element_supplier: Callable object that defines constructor of element.
        :param locator: Locator of the target element.
        :param name: Name of the target element.
        :param state: State of the target element.
        :return: Instance of custom element.
        """
        pass

    @abstractmethod
    def find_child_element(self, parent_element,
                           element_supplier: ty.Callable[[ty.Tuple[By, str], str, str], T],
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
        pass

    @abstractmethod
    def find_child_elements(self, parent_element,
                            element_supplier: ty.Callable[[ty.Tuple[By, str], str, str], T],
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
        pass

    @abstractmethod
    def find_elements(self, element_supplier: ty.Callable[[ty.Tuple[By, str], str, str], T],
                      locator: ty.Tuple[By, str], name: str = str(),
                      state: ty.Callable[[WebElement], bool] = Displayed,
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
        pass

    @property
    def conditional_wait(self):
        return self._conditional_wait

    @property
    def element_finder(self):
        return self._element_finder

    @property
    def localization_manager(self):
        return self._localization_manager

    @property
    def application(self):
        return self._application

    @property
    def action_repeater(self):
        return self._action_repeater

    @property
    def cache_configuration(self):
        return self._cache_configuration

    @property
    def localized_logger(self):
        return self._localized_logger
