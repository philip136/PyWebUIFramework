import typing as ty

from browser.java_script import JavaScript
from selenium.webdriver.remote.webdriver import WebDriver
from core.applications.interfaces.application_interface import IApplication
from core.localization.loggers.interfaces.localized_logger_interface import ILocalizedLogger

B = ty.TypeVar('B', bound=IApplication)
WD = ty.TypeVar('WD', bound=WebDriver)
TAB = ty.TypeVar('TAB')


class BrowserTabNavigation:
    """Class for navigation through tabs."""

    def __init__(self, web_driver: WD, localized_logger: ILocalizedLogger, browser: B):
        self.__web_driver = web_driver
        self.__localized_logger = localized_logger
        self.__browser = browser

    @property
    def current_tab_handle(self) -> TAB:
        """Get current tab.
        :return: Current tab.
        :rtype: TAB.
        """
        self.__localized_logger.info('loc.browser.get.tab.handle')
        return self.__web_driver.current_window_handle

    @property
    def tab_handles(self) -> ty.List[TAB]:
        """Get list of tabs.
        :return: List of tabs.
        :rtype: List[TAB].
        """
        self.__localized_logger.info('loc.browser.get.tab.handles')
        return self.__web_driver.window_handles

    def switch_to_tab(self, index: int, close_current: bool) -> None:
        """Switch to tab.
        :param index: Tab number among all.
        :param close_current: Flag indicating whether to close the current tab.
        """
        self.__localized_logger.info('loc.browser.switch.to.tab.handle', index)
        handles = self.tab_handles
        if index < 0 or len(handles) <= index:
            raise IndexError(f'Index of browser tab {index} you provided is out of range 0..{len(handles)}')
        new_tab = handles[index]
        self.__close_and_switch(new_tab, close_current)

    def switch_to_last_tab(self, close_current: bool = False) -> None:
        """Switch to last tab among all.
        :param close_current: Flag indicating whether to close the current tab.
        """
        self.__localized_logger.info('loc.browser.switch.to.new.tab')
        self.__close_and_switch(self.tab_handles[-1], close_current)

    def open_new_tab(self, switch_to_new: bool) -> None:
        """Open new tab.
        :param switch_to_new: Flag indicating whether to switch to a new tab.
        """
        self.__localized_logger.info('loc.browser.tab.open.new')
        self.__browser.execute_script(JavaScript.OPEN_NEW_TAB.get_script())
        if switch_to_new:
            self.switch_to_last_tab()

    def close_tab(self) -> None:
        """Close current tab."""
        self.__localized_logger.info('loc.browser.tab.close')
        self.__web_driver.close()

    def __close_and_switch(self, name: str, close_current: bool) -> None:
        """Close and switch to tab.
        :param name: Tab name.
        :param close_current: Flag indicating whether to close the current tab.
        """
        if close_current:
            self.close_tab()

        self.__web_driver.switch_to.window(name)
