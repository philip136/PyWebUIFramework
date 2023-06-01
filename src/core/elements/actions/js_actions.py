import typing as ty

from src.browser.browser import Browser
from src.browser.java_script import JavaScript
from src.core.elements.highlight_state import HighlightState
from src.core.utilities.interfaces.action_repeater_interface import IActionRepeater
from src.core.localization.loggers.interfaces.localized_logger_interface import ILocalizedLogger
from src.core.elements.states.element_state import Displayed, ExistsInAnyState
from src.core.elements.base_parent_element import BaseParentElement

T = ty.TypeVar('T')


class JsActions:
    def __init__(self, element: BaseParentElement, element_type: ty.Type[ty.Union[Displayed, ExistsInAnyState]],
                 localized_logger: ILocalizedLogger, action_repeater: IActionRepeater, browser: Browser):
        self.__element = element.get_element()
        self.__element_type = element_type
        self.__name = element.name
        self.__localized_logger = localized_logger
        self.__action_repeater = action_repeater
        self.__browser = browser

    def highlight_element(self, highlight_state: HighlightState = HighlightState.DEFAULT):
        if (self.__browser.browser_profile.is_element_highlight_enabled or
                highlight_state.value == HighlightState.HIGHLIGHT.value):
            self.__execute_script(JavaScript.BORDER_ELEMENT.get_script(), self.__element)

    def click(self) -> None:
        """Clicking on an item with JS."""
        self.__log_element_action('loc.clicking.js')
        self.__execute_script(JavaScript.CLICK_ELEMENT.get_script(), self.__element)

    def click_and_wait(self) -> None:
        """Clicking on an item with JS and wait."""
        self.click()
        self.__browser.wait_for_page_to_load()

    def scroll_by(self, x: int, y: int) -> None:
        """Scroll to element.
        :param x: X coordinate.
        :param y: Y coordinate.
        """
        self.__log_element_action('loc.scrolling.js')
        self.__execute_script(JavaScript.SCROLL_BY.get_script(), self.__element, x, y)

    def __execute_script(self, script: str, *args: ty.Any) -> T:
        """Execute js script.
        :param script: JS script.
        :param args: Additional arguments for JS script.
        :return: Result of execute script method.
        :rtype: T.
        """
        return self.__action_repeater.do_with_retry(lambda: self.__browser.execute_script(
            script, self.__element, *args))

    def __log_element_action(self, message_key, *args):
        """Log action on an element.
        :param message_key: Key in resource file.
        :param args: Arguments, which will be provided to template of localized message.
        """
        return self.__localized_logger.info_element_action(self.__element_type, self.__name, message_key, *args)

