from abc import ABC
from dependency_injector.wiring import inject, Provide

from selenium.common.exceptions import NoSuchElementException
from elements.element_cache_handler import ElementCacheHandler
from application.ioc_config_container import IocConfigContainer


class BaseElement(ABC):
    """Abstract class for any element."""
    __element_cache_handler = None

    @inject
    def __init__(self, element_finder, element_cache_configuration, locator, name, state,
                 logger=Provide[IocConfigContainer.logger]):
        self._element_finder = element_finder
        self._element_cache_configuration = element_cache_configuration
        self._logger = logger
        self._locator = locator
        self._state = state
        self._name = name

    def _get_element_finder(self):
        return self._element_finder

    def _get_element_cache_configuration(self):
        return self._element_cache_configuration

    def _get_logger(self):
        return self._logger

    def _get_cache(self):
        if self.__element_cache_handler is None:
            self.__element_cache_handler = ElementCacheHandler(self._locator, self._state, self._get_element_finder())
        return self.__element_cache_handler

    @property
    def name(self):
        return self._name

    @property
    def locator(self):
        return self._locator

    def get_element(self, timeout):
        try:
            element_cache_is_enabled = self._get_element_cache_configuration().is_enabled
            return self._get_cache().get_element(timeout) if element_cache_is_enabled else self._get_element_finder().\
                find_element(self._locator, self._state, timeout)
        except NoSuchElementException as e:
            self._logger.error("Element not found")
            raise e
