import typing as ty
from abc import ABC, abstractmethod

from injector import inject
from selenium.webdriver.common.by import By
from core.elements.states.element_state import ElementState
from core.elements.states.element_count import ElementCount
from core.waitings.conditional_wait import ConditionalWait
from core.elements.base_element_finder import BaseElementFinder
from core.localization.managers.base_localization_manager import BaseLocalizationManager
from core.localization.loggers.base_localized_logger import BaseLocalizedLogger
from core.applications.base_application import BaseApplication
from core.utilities.base_action_retrier import BaseActionRetrier
from core.configurations.element_cache_configuration import ElementCacheConfiguration

T = ty.TypeVar('T')


class BaseElementFactory(ABC):
    @inject
    def __init__(self, conditional_wait: ConditionalWait, element_finder: BaseElementFinder,
                 localization_manager: BaseLocalizationManager, application: BaseApplication,
                 action_retrier: BaseActionRetrier, cache_configuration: ElementCacheConfiguration,
                 localized_logger: BaseLocalizedLogger):
        """Initialize factory with required dependencies."""
        self._conditional_wait = conditional_wait
        self._element_finder = element_finder
        self._localization_manager = localization_manager
        self._application = application
        self._action_retrier = action_retrier
        self._cache_configuration = cache_configuration
        self._localized_logger = localized_logger

    @abstractmethod
    def get_custom_element(self, element_supplier: ty.Callable[[ty.Tuple[By, str], str, str], T],
                           locator: ty.Tuple[By, str], name: str,
                           state: str = ElementState.DISPLAYED.value) -> T:
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
                           state: str = ElementState.DISPLAYED.value) -> T:
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
                            state: str = ElementState.DISPLAYED.value,
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
                      locator: ty.Tuple[By, str], name: str = str(), state: str = ElementState.DISPLAYED.value,
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
    def action_retrier(self):
        return self._action_retrier

    @property
    def cache_configuration(self):
        return self._cache_configuration

    @property
    def localized_logger(self):
        return self._localized_logger
