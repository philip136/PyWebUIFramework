from abc import ABC, abstractmethod
from injector import inject

from browser.browser import Browser
from configuration.browser_profile import BrowserProfile
from core.utilities.base_action_retrier import BaseActionRetrier
from core.localization.loggers.base_localized_logger import BaseLocalizedLogger
from configuration.timeout_configuration import TimeoutConfiguration
from selenium.common.exceptions import SessionNotCreatedException, WebDriverException, TimeoutException


class BrowserFactory(ABC):
    @inject
    def __init__(self, browser_profile: BrowserProfile, logger: BaseLocalizedLogger,
                 timeouts: TimeoutConfiguration, action_retrier: BaseActionRetrier):
        self._browser_profile = browser_profile
        self._logger = logger
        self._timeouts = timeouts
        self._action_retrier = action_retrier

    @abstractmethod
    def get_driver(self):
        pass

    def get_browser(self):
        driver = self._action_retrier.do_with_retry(function=self.get_driver, handled_exceptions=[
            SessionNotCreatedException, WebDriverException, TimeoutException])
        browser = Browser(driver=driver,  logger=self._logger, browser_profile=self._browser_profile,
                          timeouts=self._timeouts)
        self._logger.info("loc.browser.ready", self._browser_profile.browser_name)
        return browser
