import typing as ty
from logging import Logger

from elements.state.desired_state import DesiredState
from waitings.conditional_wait import ConditionalWait

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


T = ty.TypeVar('T', bound=RemoteWebDriver)
E = ty.TypeVar('E', bound=Exception)

class ElementFinder:
    __was_any_element_found: bool

    def __init__(self, web_driver: T, logger: Logger, conditional_wait: ConditionalWait):
        self._web_driver = web_driver
        self._logger = logger
        self._conditional_wait = conditional_wait

    def _try_to_find_elements(self, locator: str, desired_state: DesiredState,
                              result_elements: ty.Optional[list, ty.List[WebElement]]) -> bool:
        """Try to find elements.
        :return: Elements is found or not.
        :rtype: bool.
        """

    def find_elements(self, by: str, locator: str) -> list:
        """Get list with elements.
        :return: List with WebElements.
        :rtype: list.
        """

    def find_not_visible_elements(self, by: str, locator: str, expected_conditional=ty.Callable[..., object]) -> list:
        """Get list with elements if elements is not visible
        :param by:
        :param locator:
        :param expected_conditional:

        :return: List with WebElements.
        :rtype: list.
        """
    def _handle_timeout_exceptions(self, exception: E, locator: str, desired_state: DesiredState) -> None:
        """Handler error."""
