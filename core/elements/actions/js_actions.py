import typing as ty

from browser.browser import Browser
from browser.java_script import JavaScript
from core.utilities.base_action_retrier import BaseActionRetrier
from core.localization.loggers.base_localized_logger import BaseLocalizedLogger


class JsActions:
    def __init__(self, element, element_type, localized_logger: BaseLocalizedLogger, action_retrier: BaseActionRetrier,
                 browser: Browser):
        self.__element = element.get_element()
        self.__element_type = element_type
        self.__name = element.name
        self.__localized_logger = localized_logger
        self.__action_retrier = action_retrier
        self.__browser = browser

    def click(self):
        self.__log_element_action('loc.clicking.js')
        self.__execute_script(JavaScript.CLICK_ELEMENT.get_script(), self.__element)

    def scroll_by(self, x: int, y: int):
        self.__log_element_action('loc.scrolling.js')
        self.__execute_script(JavaScript.SCROLL_BY.get_script(), self.__element, x, y)

    def __execute_script(self, script, *args):
        return self.__action_retrier.do_with_retry(lambda: self.__browser.execute_script(script, self.__element, *args))

    def __log_element_action(self, message_key, *args):
        return self.__localized_logger.info_element_action(self.__element_type, self.__name, message_key, *args)

    def __get_action_retrier(self):
        return self.__action_retrier

