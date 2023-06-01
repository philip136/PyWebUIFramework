from abc import ABC
from injector import inject

from src.browser.browser import Browser
from src.browser.interfaces.browser_factory_interface import IBaseBrowserFactory
from src.core.utilities.interfaces.action_repeater_interface import IActionRepeater
from src.core.localization.loggers.interfaces.localized_logger_interface import ILocalizedLogger
from src.core.configurations.interfaces.browser_profile_interface import IBrowserProfile
from src.core.configurations.interfaces.timeout_configuration_interface import ITimeoutConfiguration
from selenium.common.exceptions import SessionNotCreatedException, WebDriverException, TimeoutException


class BaseBrowserFactory(IBaseBrowserFactory, ABC):
    """Abstract class BaseBrowserFactory that defines the required web driver."""

    @inject
    def __init__(self, browser_profile: IBrowserProfile, localized_logger: ILocalizedLogger,
                 timeouts: ITimeoutConfiguration, action_repeater: IActionRepeater) -> None:
        """Provides a BrowserProfile to select the required settings.
        Provides a LocalizedLogger for selecting the required messages in the logs.
        Provides a TimeoutConfiguration for selecting the required timeouts (implicit, page_load, script and etc).
        Provides a ActionRepeater for executing functions or methods multiple times.
        """
        self._browser_profile = browser_profile
        self._localized_logger = localized_logger
        self._timeouts = timeouts
        self._action_repeater = action_repeater

    def get_browser(self) -> Browser:
        """Get Browser instance.
        :return: Browser instance.
        :rtype: Browser.
        """
        driver = self._action_repeater.do_with_retry(function=self.get_driver, handled_exceptions=[
            SessionNotCreatedException, WebDriverException, TimeoutException])
        browser = Browser(driver=driver, localized_logger=self._localized_logger,
                          browser_profile=self._browser_profile, timeouts=self._timeouts)
        self._localized_logger.info("loc.browser.ready", self._browser_profile.browser_name)
        return browser
