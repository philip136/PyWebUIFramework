import typing as ty
from abc import ABC, abstractmethod

from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from core.elements.states.element_count import ElementCount
from core.elements.states.element_state import Displayed, ExistsInAnyState
from core.elements.base_parent_element import BaseParentElement
from core.configurations.element_cache_configuration import ElementCacheConfiguration
from core.localization.configurations.interfaces.logger_configuration_interface import ILoggerConfiguration
from core.localization.managers.interfaces.localization_interface import ILocalizationManager
from core.localization.loggers.interfaces.localized_logger_interface import ILocalizedLogger
from core.elements.element_finder_interface import IElementFinder
from core.localization.loggers.logger_config import Logger
from core.elements.states.element_state_provider import ElementStateProvider
from core.waitings.interfaces.conditional_wait_interface import IConditionalWait
from core.elements.base_element_factory import BaseElementFactory
from core.applications.interfaces.application_interface import IApplication
from core.utilities.interfaces.action_repeater_interface import IActionRepeater
from core.elements.base_element_cache_handler import BaseElementCacheHandler
from core.elements.element_cache_handler import ElementCacheHandler
from core.elements.states.cached_element_state_provider import CachedElementStateProvider
from core.elements.actions.js_actions import JsActions

T = ty.TypeVar('T')
TR = ty.TypeVar('TR')
APP = ty.TypeVar('APP', bound=IApplication)


class BaseElement(BaseParentElement, ABC):
    """Base class for any custom element."""
    __element_cache_handler = None

    def __init__(self, locator: ty.Tuple[By, str], name: str,
                 element_state: ty.Type[ty.Union[Displayed, ExistsInAnyState]],
                 element_factory: BaseElementFactory) -> None:
        self.__name = name
        self.__locator = locator
        self.__element_state = element_state
        self.__element_factory = element_factory

    @property
    def locator(self) -> ty.Tuple[By, str]:
        """Get locator of element.
        :return: Element locator.
        :rtype: str.
        """
        return self.__locator

    @property
    def name(self) -> str:
        """Get name of element.
        :return: Element name.
        :rtype: str.
        """
        return self.__name

    @property
    def _element_state(self) -> ty.Type[ty.Union[Displayed, ExistsInAnyState]]:
        return self.__element_state

    @property
    def state(self) -> ty.Union[CachedElementStateProvider, ElementStateProvider]:
        """Get element state provider."""
        if self._element_cache_configuration.is_enabled:
            return CachedElementStateProvider(self.locator, self._conditional_wait, self._element_finder, self._cache)
        else:
            return ElementStateProvider(self.locator, self._conditional_wait, self._element_finder)

    @property
    def text(self) -> str:
        """Get text of item (inner text).
        :return: Text of element.
        :rtype: str.
        """
        self._log_element_action("loc.get.text")
        value = self._do_with_retry(lambda: str(self.get_element().text))
        self._log_element_action("loc.text.value", value)
        return value

    def get_attribute(self, attr: str) -> str:
        """Get attribute value of the element.
        :param attr: Attribute name.
        :return: Attribute value.
        :rtype: str.
        """
        self._log_element_action("loc.el.getattr", attr)
        value = self._do_with_retry(lambda: str(self.get_element().get_attribute(attr)))
        self._log_element_action("loc.el.attr.value", attr, value)
        return value

    def _do_with_retry(self, expression: ty.Callable[..., TR]) -> TR:
        """Retry action.
        :param expression: Callable object to be repeated.
        :return: Result of expression.
        :rtype: TR.
        """
        return self._element_action_repeater.do_with_retry(expression)

    def send_keys(self, keys: str) -> None:
        """Send keys.
        :param keys: keys for sending.
        """
        self._log_element_action("loc.text.sending.key", keys)

        def func():
            self.get_element().send_keys(keys)
            return True

        self._do_with_retry(func)

    def click(self) -> None:
        """Click on the item."""
        self._log_element_action("loc.clicking")

        def func():
            self.get_element().click()
            return True

        self._do_with_retry(func)

    def get_element(self, timeout: int = 0) -> WebElement:
        """Get current element by specified locator.
        Default timeout is provided in TimeoutConfiguration.
        :raises: NoSuchElementException if element not found.
        :return: Instance of WebElement if found.
        :rtype: WebElement.
        """
        try:
            if self._element_cache_configuration.is_enabled:
                element = self._cache.get_element(timeout)
            else:
                element = self._element_finder.find_element(self.__locator, self._element_state, timeout)
            return element
        except NoSuchElementException:
            if self._logger_configuration.log_page_source:
                self.__log_page_source()
            raise

    def __log_page_source(self) -> None:
        """Logging page source or logging error."""
        try:
            Logger.debug(f"Page source:\n{self._application.driver.page_source}")
        except WebDriverException:
            Logger.error("An exception occurred while tried to save the page source")

    @property
    def _application(self) -> APP:
        """Get application instance.
        :return: Instance inherited from IApplication.
        :rtype: IApplication.
        """
        return self._element_factory.application

    @property
    def _element_action_repeater(self) -> IActionRepeater:
        """Get action repeater instance.
        :return: Instance inherited from IActionRepeater.
        :rtype: IActionRepeater.
        """
        return self._element_factory.action_repeater

    @property
    def _element_finder(self) -> IElementFinder:
        """Get element finder instance.
        :return: Instance inherited from IElementFinder.
        :rtype: IElementFinder.
        """
        return self._element_factory.element_finder

    @property
    def _element_cache_configuration(self) -> ElementCacheConfiguration:
        """Get element cache configuration instance.
        :return: Element cache configuration instance.
        :rtype: ElementCacheConfiguration.
        """
        return self._element_factory.cache_configuration

    @property
    def _localized_logger(self) -> ILocalizedLogger:
        """Get localized logger instance.
        :return: Instance inherited from ILocalizedLogger.
        :rtype: ILocalizedLogger.
        """
        return self._element_factory.localized_logger

    @property
    def _localization_manager(self) -> ILocalizationManager:
        """Get localization manager instance.
        :return: Instance inherited from ILocalizationManager.
        :rtype: ILocalizationManager.
        """
        return self._element_factory.localization_manager

    @property
    def _element_factory(self) -> BaseElementFactory:
        """Get element factory instance.
        :return: Instance inherited from BaseElementFactory.
        :rtype: BaseElementFactory.
        """
        return self.__element_factory

    @property
    def _conditional_wait(self) -> IConditionalWait:
        """Get conditional wait instance.
        :return: Instance inherited from IConditionalWait.
        :rtype: IConditionalWait.
        """
        return self._element_factory.conditional_wait

    @property
    @abstractmethod
    def _element_type(self) -> str:
        """Get element type.
        :return: Element type as string.
        :rtype: str.
        """
        pass

    @property
    def js_action(self) -> JsActions:
        """Get Java Script actions.
        :return: Instance of JsActions.
        :rtype: JsActions.
        """
        return JsActions(self, self._element_state, self._localized_logger,
                         self._element_action_repeater, self._application)

    @property
    def _logger_configuration(self) -> ILoggerConfiguration:
        """Get logger configuration.
        :return: Instance inherited from ILoggerConfiguration.
        :rtype: ILoggerConfiguration.
        """
        return self._localized_logger.configuration

    @property
    def _cache(self) -> BaseElementCacheHandler:
        """Get element cache handler.
        :return: Instance inherited from BaseElementCacheHandler.
        :rtype: BaseElementCacheHandler.
        """
        if self.__element_cache_handler is None:
            self.__element_cache_handler = ElementCacheHandler(self.__locator, self._element_state,
                                                               self._element_finder)
        return self.__element_cache_handler

    def _log_element_action(self, message_key: str, *message_args, **logger_kwargs) -> None:
        """Logging element action.
        :param message_key: Message key from resource file.
        :param message_args: Additional arguments for formatting message_key.
        :param logger_kwargs: Additional arguments for logger.
        """
        self._localized_logger.info_element_action(
            self._element_type, self.name, message_key, message_args, logger_kwargs)

    def find_child_element(self, supplier: ty.Callable[[ty.Tuple[By, str], str, str], T],
                           child_locator: ty.Tuple[By, str], name: str,
                           state: ty.Callable[[WebElement], bool] = Displayed) -> T:
        """
        Find child element of type TElement of current element by its locator.
        :param supplier: Callable object that defines constructor of child element in case of custom element.
        :param child_locator: Locator of child element.
        :param name: Child element name.
        :param state: Child element state.
        :return: Instance of child element.
        :rtype: T.
        """
        return self._element_factory.find_child_element(self, supplier, child_locator, name, state)

    def find_child_elements(self, supplier: ty.Callable[[ty.Tuple[By, str], str, str], T],
                            child_locator: ty.Tuple[By, str], name: str,
                            state: ty.Callable[[WebElement], bool] = Displayed,
                            expected_count: ElementCount = ElementCount.ANY) -> ty.List[T]:
        """
        Find child elements of type TElement of current element by its locator.
        :param supplier: Callable object that defines constructor of child element in case of custom element.
        :param child_locator: Locator of child elements relative to their parent.
        :param name: Child elements name.
        :param state: Child elements state.
        :param expected_count: Expected number of elements that have to be found (zero, more than zero, any).
        :return: List of child elements.
        :rtype: ty.List[T].
        """
        return self._element_factory.find_child_elements(self, supplier, child_locator, name, state, expected_count)
