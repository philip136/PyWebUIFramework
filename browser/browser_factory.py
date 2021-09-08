import typing as ty
from abc import ABC, abstractmethod
from injector import inject

from browser.browser import Browser
from configuration.browser_profile import BrowserProfile
from core.utilities.base_action_retrier import BaseActionRetrier
from core.localization.loggers.base_localized_logger import BaseLocalizedLogger
from configuration.timeout_configuration import TimeoutConfiguration
from selenium.common.exceptions import SessionNotCreatedException, WebDriverException, TimeoutException

WD = ty.TypeVar('WD')


class BrowserFactory(ABC):
    """Abstract class BrowserFactory that defines the required web driver."""

    @inject
    def __init__(self, browser_profile: BrowserProfile, localized_logger: BaseLocalizedLogger,
                 timeouts: TimeoutConfiguration, action_retrier: BaseActionRetrier) -> None:
        """Provides a BrowserProfile to select the required settings.
        Provides a LocalizedLogger for selecting the required messages in the logs.
        Provides a TimeoutConfiguration for selecting the required timeouts (implicit, page_load, script and etc).
        Provides a ActionRetrier for executing functions or methods multiple times.
        """
        self._browser_profile = browser_profile
        self._localized_logger = localized_logger
        self._timeouts = timeouts
        self._action_retrier = action_retrier

    @abstractmethod
    def get_driver(self) -> WD:
        """Abstract method for selecting the required driver (Firefox, Chrome and etc).
        :return: WebDriver.
        :rtype: WD.
        """
        pass

    def get_browser(self) -> Browser:
        """Get Browser instance.
        :return: Browser instance.
        :rtype: Browser.
        """
        driver = self._action_retrier.do_with_retry(function=self.get_driver, handled_exceptions=[
            SessionNotCreatedException, WebDriverException, TimeoutException])
        browser = Browser(driver=driver, localized_logger=self._localized_logger,
                          browser_profile=self._browser_profile, timeouts=self._timeouts)
        self._localized_logger.info("loc.browser.ready", self._browser_profile.browser_name)
        return browser
