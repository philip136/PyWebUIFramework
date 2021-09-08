import typing as ty
from abc import ABC, abstractmethod

from selenium.webdriver.common.by import By
from core.elements.base_element_finder import BaseElementFinder
from core.waitings.base_conditional_wait import BaseConditionalWait


class BaseElementStateProvider(ABC):
    def __init__(self, element_locator: ty.Tuple[By, str], conditional_wait: BaseConditionalWait,
                 element_finder: BaseElementFinder):
        """Initialize provider with required dependencies."""
        self._element_locator = element_locator
        self._conditional_wait = conditional_wait
        self._element_finder = element_finder

    @property
    def is_displayed(self) -> bool:
        """Get element displayed state.
        :return: Element is displayed or not.
        :rtype: bool.
        """
        return self.wait_for_displayed()

    @property
    def is_exist(self) -> bool:
        """Get element exist state.
        :return: Element is exist or not.
        :rtype: bool.
        """
        return self.wait_for_exist()

    @property
    def is_enabled(self) -> bool:
        """Get element enabled state.
        :return Element is enabled or not.
        :rtype: bool.
        """
        return self.wait_for_enabled()

    @property
    @abstractmethod
    def is_clickable(self) -> bool:
        """Get element clickable state.
        :return: Element is clickable or not.
        :rtype: bool.
        """
        pass

    @abstractmethod
    def wait_for_displayed(self, timeout: int = 0) -> bool:
        """
        Wait for element is displayed on the page.
        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: true if element displayed after waiting, false otherwise.
        """
        pass

    @abstractmethod
    def wait_for_not_displayed(self, timeout: int = 0) -> bool:
        """
        Wait for element is not displayed on the page.
        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: true if element is not displayed after waiting, false otherwise.
        """
        pass

    @abstractmethod
    def wait_for_exist(self, timeout: int = 0) -> bool:
        """
        Wait for element exists in DOM (without visibility check).
        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: true if element exist after waiting, false otherwise.
        """
        pass

    @abstractmethod
    def wait_for_not_exist(self, timeout: int = 0) -> bool:
        """
        Wait for element does not exist in DOM (without visibility check).
        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: true if element does not exist after waiting, false otherwise.
        """
        pass

    @abstractmethod
    def wait_for_enabled(self, timeout: int = 0) -> bool:
        """
        Wait for element has enabled state which means element is Enabled and does not have "disabled" class.
        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: True if enabled, false otherwise.
        :raises: NoSuchElementException when timeout exceeded and element not found.
        """
        pass

    @abstractmethod
    def wait_for_not_enabled(self, timeout: int = 0) -> bool:
        """
        Wait for element does not have enabled state which means element is not Enabled or does have "disabled" class.
        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: True if not enabled, false otherwise.
        :raises: NoSuchElementException when timeout exceeded and element not found.
        """
        pass

    @abstractmethod
    def wait_for_clickable(self, timeout: int = 0) -> None:
        """
        Wait for element to become clickable which means element is displayed and enabled.
        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :raises: WebDriverTimeoutException when timeout exceeded and element is not clickable.
        """
        pass

