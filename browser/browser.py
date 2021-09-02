import typing as ty

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from core.applications.application import Application
from core.configurations.base_browser_profile import BaseBrowserProfile
from core.localization.loggers.base_localized_logger import BaseLocalizedLogger
from core.configurations.base_timeout_configuration import BaseTimeoutConfiguration
from browser.browser_tab_navigation import BrowserTabNavigation


WD = ty.TypeVar('WD', bound=RemoteWebDriver)


class Browser(Application):
    def __init__(self, web_driver: WD, logger: BaseLocalizedLogger, browser_profile: BaseBrowserProfile,
                 timeouts: BaseTimeoutConfiguration) -> None:
        self.__web_driver = web_driver
        self.__logger = logger
        self.__browser_profile = browser_profile
        self.__implicit_timeout = timeouts.implicit
        self.driver.implicitly_wait(self.__implicit_timeout)

    @property
    def driver(self):
        return self.__web_driver

    @property
    def browser_name(self):
        return self.__web_driver.name

    def maximize(self):
        self.__logger.info('loc.browser.maximize')
        self.__web_driver.maximize_window()

    @property
    def current_url(self):
        self.__logger.warning('loc.browser.getUrl')
        url = self.driver.current_url
        self.__logger.info('loc.browser.url.value', url)
        return url

    def go_to(self, url: str):
        self.__web_driver.get(url=url)

    def go_back(self):
        self.__web_driver.back()

    def refresh(self):
        self.__web_driver.refresh()

    def go_forward(self):
        self.__web_driver.forward()

    @property
    def tabs(self):
        return BrowserTabNavigation(self.__web_driver, self.__logger)

    def quit(self):
        self.__logger.warning("loc.browser.driver.quit")
        self.__web_driver.quit()

    def execute_script(self, script, *arguments):
        return self.__web_driver.execute_script(script=script, *arguments)

    @property
    def is_started(self):
        return self.__web_driver.session_id is not None

    @property
    def download_directory(self):
        return self.__browser_profile.get_driver_settings().get_download_dir()


