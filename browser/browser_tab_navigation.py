import typing as ty

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from core.localization.loggers.base_localized_logger import BaseLocalizedLogger

WD = ty.TypeVar('WD', bound=RemoteWebDriver)


class BrowserTabNavigation:
    def __init__(self, web_driver: WD, logger: BaseLocalizedLogger):
        self.__web_driver = web_driver
        self.__logger = logger

    @property
    def current_tab_handle(self):
        self.__logger.info('loc.browser.get.tab.handle')
        return self.__web_driver.current_window_handle

    @property
    def tab_handles(self):
        self.__logger.info('loc.browser.get.tab.handles')
        return self.__web_driver.window_handles

    def switch_to_tab(self, index: int, close_current: bool):
        self.__logger.info('loc.browser.switch.to.tab.handle', index)
        handles = self.tab_handles
        if index < 0 or len(handles) <= index:
            raise IndexError(f'Index of browser tab {index} you provided is out of range 0..{len(handles)}')
        new_tab = handles[index]
        self.__close_and_switch(new_tab, close_current)

    # TODO The first creating JavaScript Executor
    def open_new_tab(self, switch_to_new: bool):
        self.__logger.info('loc.browser.tab.open.new')

    def close_tab(self):
        self.__logger.info('loc.browser.tab.close')
        self.__web_driver.close()

    def __close_and_switch(self, name: str, close_current: bool):
        if close_current:
            self.close_tab()

        self.__web_driver.switch_to.window(name)
