import typing as ty

from selenium.webdriver.remote.webelement import WebElement
from core.elements.base_element_cache_handler import BaseElementCacheHandler


class ElementCacheHandler(BaseElementCacheHandler):
    def get_element(self, timeout: int = 0, custom_state: ty.Callable[[WebElement], bool] = None) -> WebElement:
        """
        Allow to get cached element.
        :param timeout: Timeout used to retrieve the element when refresh is needed.
        :param custom_state: Element custom state.
        :return: Cached element.
        :rtype: WebElement.
        """
        if self.is_refresh_needed(custom_state):
            self.__remote_element = self.__element_finder.find_element(self._locator, self._state, timeout)
        return self.__remote_element
